"""Check a checkout and optionally replay Test 6 in memory; never execute MIPS.

The clean ROM is a private input, not a Git-tracked dependency. This script
does not download it, compile game code, or write a reconstructed ROM.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import struct
import subprocess

from verify_baseline import ROOT, apply_ips, crc6102, require


def sha(data):
    return hashlib.sha256(data).hexdigest()


def inspect_checkout():
    manifest = json.loads((ROOT / 'cloud/input-manifest.json').read_text())
    patch_path = ROOT / manifest['current_patch']['path']
    patch = patch_path.read_bytes()
    require(sha(patch) == manifest['current_patch']['sha256'], 'Current patch hash differs')
    tracked = subprocess.run(
        ['git', 'ls-files', '-z'], cwd=ROOT, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    ).stdout.decode('utf-8').split('\0')
    tracked = [name for name in tracked if name]
    require(bool(tracked), 'No tracked project files; initialize or clone the repository first')
    excluded_suffixes = {'.z64', '.n64', '.v64', '.rom', '.sav', '.state', '.mpk',
                         '.eep', '.sra', '.fla', '.bin', '.o', '.elf', '.zip',
                         '.7z', '.tar', '.tgz', '.gz', '.pem', '.key', '.pyc'}
    for name in tracked:
        path = Path(name)
        require(path.suffix.lower() not in excluded_suffixes, 'Private/binary file tracked: ' + name)
        require(not path.name.startswith('.env'), 'Environment file tracked: ' + name)
        require(not set(path.parts).intersection({'private', 'cloud-inputs', 'tools', 'build', 'outputs', '__pycache__'}),
                'Private/generated directory tracked: ' + name)
    report = dict(
        checkout='passed', tracked_files=len(tracked), patch_sha256=sha(patch),
        runtime=dict(system=platform.system(), machine=platform.machine(), python=platform.python_version()),
        rom_check='not run; private input not requested',
        game_code_executed=False, reconstructed_rom_written=False,
        gameplay_validation=False,
    )
    return manifest, patch, report


def check_rom(rom_path, manifest, patch, report):
    require(rom_path.stat().st_size == manifest['clean_us']['size'], 'Wrong clean ROM size')
    original = rom_path.read_bytes()
    require(sha(original) == manifest['clean_us']['sha256'], 'Wrong clean US ROM hash')
    require(struct.unpack_from('>II', original, 0x10) == crc6102(original), 'Clean checksum differs')
    result = apply_ips(original, patch)
    expected = manifest['expected_test6']
    require(len(result) == expected['size'], 'Reconstructed size differs')
    require(sha(result) == expected['sha256'], 'Reconstructed Test 6 hash differs')
    require(struct.unpack_from('>II', result, 0x10) == crc6102(result), 'Test 6 checksum differs')
    require(result[0x20:0x34].decode('ascii').rstrip(' \0') == expected['internal_name'], 'Build name differs')
    report.update(rom_check='passed', clean_sha256=sha(original), test6_sha256=sha(result),
                  changed_bytes=sum(a != b for a, b in zip(original, result)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--repository-only', action='store_true', help='Do not read any ROM')
    source.add_argument('--rom', type=Path, help='Private clean US ROM path; kept out of the report')
    parser.add_argument('--report', type=Path, default=ROOT / 'build/cloud-smoke.json')
    args = parser.parse_args()
    manifest, patch, report = inspect_checkout()
    if args.rom:
        check_rom(args.rom, manifest, patch, report)
    # Never accidentally commit a private input or overwrite a retained file.
    output = args.report.resolve()
    require(output.is_relative_to((ROOT / 'build').resolve()), 'Report must stay in ignored build/')
    require(output.suffix == '.json', 'Report must be JSON')
    require(not args.rom or output != args.rom.resolve(), 'Report cannot replace the input')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
