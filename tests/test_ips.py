import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from verify_baseline import apply_ips


class IpsTests(unittest.TestCase):
    def test_literal_and_rle_replay(self):
        patch = b"PATCH\x00\x00\x01\x00\x02AB\x00\x00\x04\x00\x00\x00\x03ZEOF"
        self.assertEqual(apply_ips(b"01234567", patch), b"0AB3ZZZ7")

    def test_records_cannot_extend_rom(self):
        with self.assertRaises(ValueError):
            apply_ips(b"1234", b"PATCH\x00\x00\x03\x00\x02ABEOF")

    def test_truncated_and_malformed_inputs_rejected(self):
        for patch in (b"", b"PATCH", b"PATCHEOFx", b"PATCH\x00\x00\x00\x00\x03A",
                      b"PATCH\x00\x00\x00\x00\x00\x00\x02", b"PATCH\x00\x00\x00\x00\x00\x00\x00AEOF"):
            with self.subTest(patch=patch), self.assertRaises(ValueError):
                apply_ips(b"1234", patch)


if __name__ == "__main__":
    unittest.main()
