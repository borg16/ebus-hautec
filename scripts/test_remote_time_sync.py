"""Offline regression for TEM 30 00 time synchronization; never contacts the bus."""

import csv
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("ebusd") and (ROOT / "node_modules/.bin/tsp").exists(),
                     "ebusd and the installed TypeSpec compiler are required")
class RemoteTimeSyncTests(unittest.TestCase):
    def test_captured_time_blocks_and_passive_definitions(self):
        # CRC/ACK-checked captures: obsolete/StartRaw.txt:14,
        # input/complete.log:2849, ebusd.log:3568 and :43784.
        # ebusd's injection format omits CRC/ACK but retains the empty reply length.
        samples = [
            ("1090100a0e3000f008c0b4efefefefefef2690/00",
             "Remote1", "2288;46272;ef ef ef ef ef ef;26 90"),
            ("1090100a0e3000760dcfb4efefefefefef3590/00",
             "Remote1", "3446;46287;ef ef ef ef ef ef;35 90"),
            ("1090100a0e30003922d3b4efefefefefef4503/00",
             "Remote1", "8761;46291;ef ef ef ef ef ef;45 03"),
            ("1090100a0e30003b25d3b4efefefefefef4503/00",
             "Remote1", "9531;46291;ef ef ef ef ef ef;45 03"),
            # Additional start example from docs/FB-Initialization.md (no raw CRC).
            ("1090100a0e30004e0fc1b4efefefefefef2703/00",
             "Remote1", "3918;46273;ef ef ef ef ef ef;27 03"),
            # Synthetic remote-2 sample: verifies shared layout and all opaque bytes.
            # There is no captured 30 00 transaction to 91 in the examined logs.
            ("1091100a0e3000f008c0b40123456789ab2690/00",
             "Remote2", "2288;46272;01 23 45 67 89 ab;26 90"),
        ]
        with tempfile.TemporaryDirectory(prefix="hautec-time-sync-test-") as temporary:
            compiled = subprocess.run(
                [str(ROOT / "node_modules/.bin/tsp"), "compile", "main.tsp", "--emit",
                 "@ebusd/ebus-typespec", "--output-dir", temporary],
                cwd=ROOT, text=True, capture_output=True, timeout=60)
            self.assertEqual(compiled.returncode, 0, compiled.stdout + compiled.stderr)
            config = Path(temporary) / "@ebusd/ebus-typespec"
            for number, address in ((1, "90"), (2, "91")):
                with (config / "hautec" / f"remote{number}.csv").open() as stream:
                    rows = [row for row in csv.reader(stream)
                            if len(row) > 8 and row[3] == f"ZeitstatusBedienteil{number}"]
                self.assertEqual(len(rows), 1)
                # Passive-only, controller source, and 30 00 consumed by the ID.
                self.assertEqual(rows[0][0], "uw")
                self.assertEqual(rows[0][5:9], ["10", address, "100a", "3000"])
            replay = subprocess.run(
                ["ebusd", "--foreground", "--device=/dev/null", "--readonly", "--pollinterval=0",
                 "--port=18889", "--localhost", "--updatecheck=off", "--scanconfig=off",
                 f"--configpath={config}", "--log=update:info", "--inject=stop",
                 *[telegram for telegram, _, _ in samples]],
                text=True, capture_output=True, timeout=30)
            output = replay.stdout + replay.stderr
            self.assertEqual(replay.returncode, 0, output)
            self.assertNotIn("[update error]", output)
            decoded = re.findall(
                r"received update-write (Remote[12]) ZeitstatusBedienteil[12]: (.*)", output)
            self.assertEqual(decoded, [(remote, values) for _, remote, values in samples], output)


if __name__ == "__main__":
    unittest.main()
