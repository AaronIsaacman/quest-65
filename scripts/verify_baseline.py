"""Independent checks of the generated ROM, IPS replay, and N64 checksums."""
import hashlib
import json
from pathlib import Path
import re
import struct
import sys
import zlib

ROOT = Path(__file__).resolve().parents[1]
STEM = "quest64-french-vanilla-baseline"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def apply_ips(original, patch):
    """Read bounded, non-expanding IPS records (including RLE)."""
    require(patch.startswith(b"PATCH"), "Invalid IPS header")
    result = bytearray(original)
    cursor = 5
    while True:
        require(cursor + 3 <= len(patch), "Missing IPS EOF")
        address_bytes = patch[cursor:cursor + 3]
        cursor += 3
        if address_bytes == b"EOF":
            require(cursor == len(patch), "Unexpected IPS trailer")
            return bytes(result)
        address = int.from_bytes(address_bytes, "big")
        require(cursor + 2 <= len(patch), "Truncated IPS length")
        length = int.from_bytes(patch[cursor:cursor + 2], "big")
        cursor += 2
        if length:
            require(cursor + length <= len(patch), "Truncated IPS payload")
            payload = patch[cursor:cursor + length]
            cursor += length
        else:
            require(cursor + 3 <= len(patch), "Truncated IPS RLE")
            count = int.from_bytes(patch[cursor:cursor + 2], "big")
            require(count > 0, "Empty IPS RLE")
            payload = patch[cursor + 2:cursor + 3] * count
            cursor += 3
        require(address + len(payload) <= len(result), "IPS record outside ROM")
        result[address:address + len(payload)] = payload


def crc6102(rom):
    """N64 CIC-6102 checksum; independent from Merrow's C# implementation.

    Algorithm adapted from Merrow/CRC.cs (Jonah Davidson, MIT license).
    This deliberately supports only the bootcode used by the verified US ROM.
    """
    require(len(rom) >= 0x101000, "ROM too small for N64 checksum")
    require(zlib.crc32(rom[0x40:0x1000]) == 0x90BB6CB5, "Unexpected N64 bootcode")
    mask = 0xFFFFFFFF
    t1 = t2 = t3 = t4 = t5 = t6 = 0xF8CA4DDC
    for (word,) in struct.iter_unpack(">I", rom[0x1000:0x101000]):
        total = t6 + word
        t4 = (t4 + (total > mask)) & mask
        t6 = total & mask
        t3 ^= word
        shift = word & 31
        rotated = ((word << shift) | (word >> ((32 - shift) % 32))) & mask
        t5 = (t5 + rotated) & mask
        t2 ^= rotated if t2 > word else t6 ^ word
        t1 = (t1 + (t5 ^ word)) & mask
    return t6 ^ t4 ^ t3, t5 ^ t2 ^ t1


def source_array(source, name, strings=False):
    match = re.search(r"public (?:string|int)\[\] " + re.escape(name) + r"\s*=\s*\{(.*?)\};", source, re.S)
    require(match is not None, "Missing upstream array: " + name)
    body = re.sub(r"//[^\n]*", "", match[1])
    return re.findall(r'"([^"\n]*)"', body) if strings else [int(n) for n in re.findall(r"\d+", body)]


def verify(rom_path, output):
    lock = json.loads((ROOT / "upstream.lock.json").read_text())
    original = rom_path.read_bytes()
    patched = (output / (STEM + ".z64")).read_bytes()
    patch = (output / (STEM + ".ips")).read_bytes()
    require(hashlib.sha1(original).hexdigest() == lock["supported_rom_sha1"], "Wrong clean ROM hash")
    require(len(original) == len(patched) == 0x1000000, "ROM size changed")
    require(original[:16] == patched[:16], "N64 boot header changed")
    require(original[0x18:0x1000] == patched[0x18:0x1000], "ROM identity or bootcode changed")
    require(crc6102(original) == struct.unpack_from(">II", original, 0x10), "Clean ROM checksum mismatch")
    require(crc6102(patched) == struct.unpack_from(">II", patched, 0x10), "Patched ROM checksum mismatch")
    require(apply_ips(original, patch) == patched, "IPS replay does not reproduce ROM")

    source = (ROOT / "tools/merrow/Merrow/Merrow/DataStore.cs").read_text(encoding="utf-8-sig")
    spells = source_array(source, "spells", strings=True)
    rebalance = source_array(source, "damageRebalance")
    require(len(spells) == 60 * 4 and len(rebalance) == 18 * 3, "Upstream spell table changed")
    changes = []
    for index, old, new in zip(rebalance[::3], rebalance[1::3], rebalance[2::3]):
        name, address = spells[index * 4:index * 4 + 2]
        offset = int(address, 16) + 12
        require(int.from_bytes(original[offset:offset + 2], "big") == old, name + ": unexpected original power")
        require(int.from_bytes(patched[offset:offset + 2], "big") == new, name + ": unexpected patched power")
        changes.append({"spell": name, "original_power": old, "baseline_power": new})
    for i in range(60):
        offset = int(spells[i * 4 + 1], 16)
        require(patched[offset:offset + 12] == original[offset:offset + 12], "Spell ownership/unlock/behavior changed")
        require(patched[offset + 15] == 100, "Spell accuracy normalization missing")
    encounter = {0x1D253: b"\x54", 0x1D28F: b"\x50", 0x1D28A: b"\x09\x60"}
    for offset, expected in encounter.items():
        require(patched[offset:offset + len(expected)] == expected, "Reduced encounter setting missing")
    # These are the locations changed by Merrow's level-99 option.
    cap_locations = [0x850A, 0x8546, 0x8563, 0x3ED7]
    cap_locations += [int(s, 16) for s in source_array(source, "elementCapLocations", strings=True)]
    for offset in cap_locations:
        require(original[offset:offset + 2] == patched[offset:offset + 2], "Element cap was modified")

    report = {
        "status": "binary checks passed; emulator playtesting pending",
        "merrow_commit": lock["commit"],
        "original_sha1": hashlib.sha1(original).hexdigest(),
        "output_sha1": hashlib.sha1(patched).hexdigest(),
        "output_sha256": hashlib.sha256(patched).hexdigest(),
        "ips_sha256": hashlib.sha256(patch).hexdigest(),
        "ips_bytes": len(patch),
        "rom_bytes": len(patched),
        "changed_bytes": sum(a != b for a, b in zip(original, patched)),
        "checks": ["clean US ROM hash", "ROM identity and size preserved", "original and patched CIC-6102 checksums",
                   "IPS exactly reproduces patched ROM", "18 upstream spell power changes", "60 spell accuracy values",
                   "reduced encounter settings", "spell ownership/unlocks preserved", "element cap preserved at 50"],
        "spell_power_changes": changes,
        "limitations": ["Not yet booted in an emulator", "No new project-specific spell or boss balance changes yet"]
    }
    (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


if __name__ == "__main__":
    try:
        require(len(sys.argv) == 3, "Usage: verify_baseline.py clean.z64 output-directory")
        report = verify(Path(sys.argv[1]), Path(sys.argv[2]))
        print("Verified baseline:", report["changed_bytes"], "changed bytes; IPS", report["ips_bytes"], "bytes")
    except (ValueError, OSError) as error:
        sys.exit(str(error))
