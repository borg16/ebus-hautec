"""Offline capture, generation, and ebusd replay checks; no connection to a bus."""

import csv
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from analyze_master_log import ROOT, build_catalog, crc, parse_line, read_log, render_tsp, unescape


class RawFormatTests(unittest.TestCase):
    def test_non_recursive_unescaping(self):
        self.assertEqual(unescape(bytes.fromhex("a90001a901")), bytes.fromhex("a901aa"))
        for data in (b"\xa9", b"\xa9\x02", b"\xaa"):
            with self.assertRaises(ValueError):
                unescape(data)

    def test_crc_and_transaction_boundaries(self):
        self.assertEqual(crc(bytes.fromhex("01150621020b00")), 0x39)
        self.assertEqual(crc(bytes.fromhex("0ab3414d022c016400dc00")), 0xE2)
        line = "2026-09-23 08:57:03.403 <01150621020b0039000ab3414d022c016400dc00e200"
        parsed = parse_line(line, 22)
        self.assertEqual(parsed["request"], "0b00")
        self.assertEqual(parsed["response"], "b3414d022c016400dc00")
        with self.assertRaisesRegex(ValueError, "slave CRC"):
            parse_line(line[:-4] + "e300", 22)
        with self.assertRaisesRegex(ValueError, "not acknowledged"):
            parse_line(line[:-2] + "ff", 22)
        with self.assertRaisesRegex(ValueError, "length"):
            parse_line(line[:-2], 22)


class CaptureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        all_records, cls.errors = read_log(ROOT / "input/complete.log")
        cls.records = [
            record for record in all_records
            if (record["source"], record["destination"]) == ("01", "15")
            and record["service"] in {"0620", "0621", "0622"}
        ]
        cls.ste = json.loads((ROOT / "ste-output/parameter.json").read_text())
        cls.catalog = build_catalog(cls.records, cls.ste)

    def test_capture_coverage(self):
        self.assertEqual(sum(r["status"] == "complete" for r in self.records), 4776)
        self.assertEqual(sum(r["status"] == "request_only" for r in self.records), 176)
        self.assertEqual(len(self.catalog), 240)
        self.assertEqual(len([r for r in self.catalog if r["tem_id"]]), 201)
        ids = {r["tem_id"] for r in self.catalog if r["tem_id"]}
        self.assertEqual(len(ids), 118)
        ste_ids = {r["tem_id"] for r in self.ste["records"] if r["tem_id"]}
        self.assertEqual(len(ste_ids - ids), 44)
        self.assertEqual({r["service"] for r in self.records}, {"0620", "0621", "0622"})

    def test_generated_source_matches_capture(self):
        source = (ROOT / "controller.tsp").read_text()
        self.assertEqual(source, render_tsp(self.catalog))
        self.assertEqual(source.count("  @write\n"), 191)
        self.assertNotIn("@qq(", source)
        self.assertEqual(source.count("  @id("), 431)
        self.assertIn('import "./controller.tsp";', (ROOT / "main.tsp").read_text())
        self.assertNotIn('import "./tem/controller.tsp";', (ROOT / "main.tsp").read_text())

    def test_special_encodings_and_correct_escape_page(self):
        by_request = {(r["service"], r["request"]): r for r in self.catalog}
        self.assertEqual(by_request["0621", "a901"]["tem_id"], "09-00")
        self.assertEqual(by_request["0621", "0109"]["response_model"], "Kurzantwort")
        self.assertEqual(by_request["0621", "0104"]["response_model"], "Sonderantwort")
        self.assertEqual(by_request["0621", "0108"]["response_model"],
                         "RohgrenzenAntwort<Wochenminuten>")
        self.assertEqual(by_request["0621", "0b04"]["response_model"], "Zahlenantwort<Steilheit100>")
        self.assertEqual(by_request["0621", "a608"]["response_model"], "Zahlenantwort<Minuten10>")
        self.assertNotEqual(by_request["0621", "0b00"]["name"],
                            by_request["0621", "0b801000"]["name"])

    @unittest.skipUnless(shutil.which("ebusd") and (ROOT / "node_modules/.bin/tsp").exists(),
                         "ebusd and the installed TypeSpec compiler are needed for offline replay")
    def test_compiled_definitions_decode_every_valid_transaction(self):
        with tempfile.TemporaryDirectory(prefix="hautec-master-test-") as temporary:
            compile_result = subprocess.run(
                [str(ROOT / "node_modules/.bin/tsp"), "compile", "controller.tsp", "--emit",
                 "@ebusd/ebus-typespec", "--output-dir", temporary],
                cwd=ROOT, text=True, capture_output=True, timeout=60)
            self.assertEqual(compile_result.returncode, 0, compile_result.stdout + compile_result.stderr)
            config = Path(temporary) / "@ebusd/ebus-typespec"
            with (config / "tem/controller.csv").open(newline="") as handle:
                csv_rows = [r for r in csv.reader(handle) if r and r[0] == "r"]
            self.assertEqual(len(csv_rows), 240)
            self.assertEqual({(r[7], r[8]) for r in csv_rows},
                             {(r["service"], r["request"]) for r in self.catalog})
            self.assertTrue(all(r[1] == "15" and r[5] == "" and r[6] == "15" for r in csv_rows))
            records = [r for r in self.records if r["status"] == "complete"]
            # --inject=stop exits after replay; /dev/null cannot address a heating controller.
            args = ["ebusd", "--foreground", "--device=/dev/null", "--readonly", "--pollinterval=0",
                    "--port=18889", "--localhost", "--updatecheck=off", "--scanconfig=off",
                    f"--configpath={config}", "--log=update:info", "--inject=stop"]
            args += [r["master"] + "/" + r["slave"] for r in records]
            replay = subprocess.run(args, text=True, capture_output=True, timeout=30)
            self.assertEqual(replay.returncode, 0, replay.stdout + replay.stderr)
            decoded = re.findall(r"received read 15 (\S+) QQ=01: (.*)", replay.stdout)
            self.assertEqual(len(decoded), 4776)
            by_request = {(r["service"], r["request"]): r for r in self.catalog}
            for record, (name, value) in zip(records, decoded):
                entry = by_request[record["service"], record["request"]]
                self.assertEqual(name, entry["name"])
                if entry["tem_id"]:
                    group, param = map(int, entry["tem_id"].split("-"))
                    self.assertEqual(value.split(";")[0], f"{group:02d}-{param:03d}")
            values = dict(decoded)
            self.assertEqual(values["P03_051_0B00"], "03-051;77;2;30.0;10.0;22.0")
            self.assertEqual(values["P03_010_0B04"], "03-010;4;8;5.00;0.00;0.40")
            self.assertEqual(values["P09_012_A905"], "09-012;77;2;50.0;-50.0;-50.0")
            self.assertEqual(values["P02_012_0109"], "02-012;30;0;05 00")
            self.assertNotIn("[update error]", replay.stdout)
            self.assertNotIn("unknown", replay.stdout)


if __name__ == "__main__":
    unittest.main()
