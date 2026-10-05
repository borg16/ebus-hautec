"""Offline protocol checks for broadcast definitions; never contacts a heating bus."""

import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("ebusd") and (ROOT / "node_modules/.bin/tsp").exists(),
                     "ebusd and the installed TypeSpec compiler are needed for offline replay")
class ControlCommandsTests(unittest.TestCase):
    def test_standard_and_tem_payloads(self):
        # Application Layer V1.6.1, section 3.4.3: D2B, D2B, D1B, BYTE, BYTE.
        # Include asymmetric fractional values, signed demand, and replacement values.
        samples = [
            ("10fe080207802540329c022a", "37.500;50.250;-100;2;42"),
            ("10fe08020780ff000a000000", "-0.500;10.000;0;0;0"),
            ("10fe0802070080008080ffff", "-;-;-;-;-"),
            ("10fe08020700130033640000", "19.000;51.000;100;0;0"),
        ]
        # Observed TEM extension values must not alter the seven standard fields.
        samples.extend(("10fe08020800130033640000" + extra, "19.000;51.000;100;0;0")
                       for extra in ("00", "27", "3f", "90", "91"))
        with tempfile.TemporaryDirectory(prefix="hautec-broadcast-test-") as temporary:
            compiled = subprocess.run(
                [str(ROOT / "node_modules/.bin/tsp"), "compile", "broadcast.tsp", "--emit",
                 "@ebusd/ebus-typespec", "--output-dir", temporary],
                cwd=ROOT, text=True, capture_output=True, timeout=60)
            self.assertEqual(compiled.returncode, 0, compiled.stdout + compiled.stderr)
            config = Path(temporary) / "@ebusd/ebus-typespec"
            replay = subprocess.run(
                ["ebusd", "--foreground", "--device=/dev/null", "--readonly", "--pollinterval=0",
                 "--port=18889", "--localhost", "--updatecheck=off", "--scanconfig=off",
                 f"--configpath={config}", "--log=update:info", "--inject=stop",
                 *[telegram + "/" for telegram, _ in samples]],
                text=True, capture_output=True, timeout=30)
            output = replay.stdout + replay.stderr
            self.assertEqual(replay.returncode, 0, output)
            self.assertNotIn("[update error]", output)
            decoded = re.findall(r"received update-read Broadcast ControlCommands QQ=10: (.*)", output)
            self.assertEqual(decoded, [expected for _, expected in samples], output)


if __name__ == "__main__":
    unittest.main()
