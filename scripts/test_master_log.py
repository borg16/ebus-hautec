"""Offline capture, generation, and ebusd replay checks; no connection to a bus."""

import csv
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from analyze_master_log import ROOT, build_catalog, build_controller_catalog, crc, parse_line, read_log, render_tsp, unescape


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
        cls.historical = build_catalog(cls.records, cls.ste)
        cls.catalog = build_controller_catalog(cls.records, cls.ste)

    def test_capture_coverage(self):
        self.assertEqual(sum(r["status"] == "complete" for r in self.records), 4776)
        self.assertEqual(sum(r["status"] == "request_only" for r in self.records), 176)
        self.assertEqual(len(self.historical), 240)
        self.assertEqual(len([r for r in self.historical if r["tem_id"]]), 201)
        ids = {r["tem_id"] for r in self.historical if r["tem_id"]}
        self.assertEqual(len(ids), 118)
        ste_ids = {r["tem_id"] for r in self.ste["records"] if r["tem_id"]}
        self.assertEqual(len(ste_ids - ids), 44)
        self.assertEqual({r["service"] for r in self.records}, {"0620", "0621", "0622"})

    def test_generated_source_matches_capture(self):
        source = (ROOT / "controller.tsp").read_text()
        self.assertEqual(source, render_tsp(self.catalog))
        self.assertEqual(source.count("  @write\n"), 165)
        self.assertNotIn("@qq(", source)
        self.assertEqual(source.count("  @id("), 494)
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

    def test_scan_preferences_and_input_names(self):
        parameters = {e["request"]: e for e in self.catalog if e["tem_id"]}
        self.assertEqual(len(parameters), 328)
        with (ROOT / "commands.txt").open() as handle:
            scan_selectors = {r["selector"] for r in csv.DictReader(handle, delimiter="\t")}
        self.assertTrue(all(e["service"] == "0620" or
                            (e["service"] == "0621" and e["request"] in scan_selectors)
                            for e in self.catalog))
        self.assertFalse(any(0x63 <= int(s[:2], 16) <= 0x72 for s in parameters))
        self.assertEqual(parameters["a704"]["tem_id"], "07-05")
        self.assertEqual(parameters["a7841000"]["tem_id"], "07-05")
        self.assertIn("Heizkreistyp", parameters["a704"]["label"])
        self.assertEqual(parameters["a704"]["label_source"], "Checkliste_Regler_Programmierung.CSV")
        self.assertIn("Aussentemperatur", parameters["0800"]["label"])
        self.assertEqual(parameters["0800"]["label_source"], "soll_und_istwerte.md")
        self.assertIn("WE 2", parameters["ac01"]["label"])
        self.assertNotIn("WE 1", parameters["ac01"]["label"])
        self.assertTrue(parameters["a925"]["scan_only"])
        self.assertFalse(parameters["a925"]["generate_write"])
        self.assertEqual(sum(e.get("scan_only", False) for e in parameters.values()), 153)

    def test_one_command_per_parameter_context_and_tem_names(self):
        entries = [e for e in self.catalog if e["tem_id"]]
        self.assertEqual(len({(e["tem_id"], e["context"]) for e in entries}), len(entries))
        self.assertEqual(sum(len(e["aliases"]) for e in entries), 378)
        by_id_context = {(e["tem_id"], e["context"]): e for e in entries}
        self.assertEqual(by_id_context["00-00", "HK1"]["name"], "P00_00_HK1")
        self.assertEqual(by_id_context["01-01", "HK2"]["name"], "P01_01_HK2")
        self.assertEqual(by_id_context["07-05", "HK1"]["name"], "P07_05_HK1")
        self.assertEqual({a["selector"] for a in by_id_context["00-00", "HK1"]["aliases"]},
                         {"0002", "0101", "0800", "0900"})
        for context in ("WP", "EH"):
            self.assertIn(("10-31", context), by_id_context)
        for i in range(1, 9):
            self.assertIn(("11-05", f"WE{i}"), by_id_context)

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
            self.assertEqual(len(csv_rows), 329)
            self.assertEqual({(r[7], r[8]) for r in csv_rows},
                             {(r["service"], "" if r["service"] == "0620" else r["request"])
                              for r in self.catalog})
            self.assertTrue(all(r[1] == "15" and r[5] == "" and r[6] == "15" for r in csv_rows))
            selected = {(e["service"], e["request"]) for e in self.catalog}
            records = [r for r in self.records if r["status"] == "complete"
                       and (r["service"], r["request"]) in selected]
            for entry in self.catalog:
                if entry.get("scan_only"):
                    selector = bytes.fromhex(entry["request"])
                    data = bytes.fromhex(entry["sample_response"])
                    records.append({"service": "0621", "request": entry["request"],
                                    "response": data.hex(),
                                    "master": (bytes.fromhex("01150621") + bytes([len(selector)]) + selector).hex(),
                                    "slave": (bytes([len(data)]) + data).hex()})
            # --inject=stop exits after replay; /dev/null cannot address a heating controller.
            args = ["ebusd", "--foreground", "--device=/dev/null", "--readonly", "--pollinterval=0",
                    "--port=18889", "--localhost", "--updatecheck=off", "--scanconfig=off",
                    f"--configpath={config}", "--log=update:info", "--inject=stop"]
            args += [r["master"] + "/" + r["slave"] for r in records]
            replay = subprocess.run(args, text=True, capture_output=True, timeout=30)
            self.assertEqual(replay.returncode, 0, replay.stdout + replay.stderr)
            decoded = re.findall(r"received read 15 (\S+) QQ=01: (.*)", replay.stdout)
            self.assertEqual(len(decoded), len(records))
            by_request = {(r["service"], r["request"]): r for r in self.catalog}
            for record, (name, value) in zip(records, decoded):
                entry = by_request[record["service"], record["request"]]
                self.assertEqual(name, entry["name"])
                if record["service"] == "0620":
                    expected = [str(int(record["request"], 16))]
                    for descriptor in bytes.fromhex(record["response"]):
                        expected.extend([str(descriptor & 127), str(descriptor >> 7)])
                    self.assertEqual(value.split(";"), expected)
                if entry["tem_id"]:
                    group, param = map(int, entry["tem_id"].split("-"))
                    self.assertEqual(value.split(";")[0], f"{group:02d}-{param:03d}")
            values = dict(decoded)
            self.assertEqual(values[by_request["0621", "0b00"]["name"]], "03-051;77;2;30.0;10.0;22.0")
            self.assertEqual(values[by_request["0621", "0b04"]["name"]], "03-010;4;8;5.00;0.00;0.40")
            self.assertEqual(values[by_request["0621", "a905"]["name"]], "09-012;77;2;50.0;-50.0;-50.0")
            self.assertEqual(values[by_request["0621", "0109"]["name"]], "02-012;30;0;05 00")
            self.assertNotIn("[update error]", replay.stdout)
            self.assertNotIn("unknown", replay.stdout)


if __name__ == "__main__":
    unittest.main()
