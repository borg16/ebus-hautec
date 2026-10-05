"""Offline decoding regression checks for standard identification and temperature fields."""

import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("ebusd") and (ROOT / "node_modules/.bin/tsp").exists(),
                     "ebusd and the installed TypeSpec compiler are required")
class StandardMessageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix="hautec-standard-test-")
        cls.addClassCleanup(cls.temporary.cleanup)
        compiled = subprocess.run(
            [str(ROOT / "node_modules/.bin/tsp"), "compile", "main.tsp", "--emit",
             "@ebusd/ebus-typespec", "--output-dir", cls.temporary.name],
            cwd=ROOT, text=True, capture_output=True, timeout=60)
        if compiled.returncode:
            raise AssertionError(compiled.stdout + compiled.stderr)
        cls.config = Path(cls.temporary.name) / "@ebusd/ebus-typespec"

    def replay(self, telegrams):
        result = subprocess.run(
            ["ebusd", "--foreground", "--device=/dev/null", "--readonly", "--pollinterval=0",
             "--port=18889", "--localhost", "--updatecheck=off", "--scanconfig=off",
             f"--configpath={self.config}", "--log=update:info", "--inject=stop", *telegrams],
            text=True, capture_output=True, timeout=30)
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 0, output)
        self.assertNotIn("[update error]", output)
        return output

    def test_identification_broadcast_and_slave_reply(self):
        # Actual TEM broadcast; synthetic slave reply and alphanumeric ID/version fixture.
        output = self.replay([
            "10fe07040a10313733383501060100/",
            "1008070400/0a10313733383501060100",
            "1008070400/0a10414231325a01230456",
        ])
        decoded = re.findall(r"received (?:update-read Broadcast|read Signals) Identification(?: QQ=10)?: (.*)", output)
        self.assertEqual(decoded, ["TEM;17385;0106;0100", "TEM;17385;0106;0100",
                                   "TEM;AB12Z;0123;0456"], output)

    def test_all_outside_temperature_bytes_in_both_directions_and_burners(self):
        # Covers sign boundaries, -1 (FF), positive values, 3F, and SCH's 80 replacement.
        # This also catches ebusd's unsigned fallback for unmapped negative enum values.
        telegrams, expected = [], []
        for burner in (0x03, 0x13):
            for raw in range(256):
                value = ("unavailable" if raw == 0x3f else "-" if raw == 0x80
                         else str(raw if raw < 128 else raw - 256))
                telegrams.extend([
                    f"10{burner:02x}050105000c33{raw:02x}64/",
                    f"{burner:02x}10050308010048643117ff{raw:02x}/",
                ])
                expected.extend([value, value])
        output = self.replay(telegrams)
        decoded = re.findall(r"received update-write Burner[12] (\S+)(?: QQ=10)?: (.*)", output)
        actual = [values.split(';')[3] if name in ('Betriebsdaten1', 'Betriebsdaten2')
                  else values.split(';')[-1] for name, values in decoded]
        self.assertEqual(len(actual), len(expected), output)
        self.assertEqual(actual, expected)

    def test_tem_extensions_do_not_shift_temperature(self):
        output = self.replay([
            "100305010a000c330f6464010000e0/",
            "031005030a010048643117ff3f4000/",
        ])
        self.assertIn("Betriebsdaten1 QQ=10: Brennerabschalten;12;51;15;100", output)
        self.assertIn("BetriebsdatenFeuerungsautomat1AnRegler: 0;0;0;0;1;0;0;1;0;100;24.5;23;-;unavailable", output)


if __name__ == "__main__":
    unittest.main()
