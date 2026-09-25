"""Offline checks with captured payloads and a simulated ebusctl process."""

from contextlib import redirect_stderr, redirect_stdout
import csv
import io
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from analyze_master_log import ROOT
from read_menu_block import Descriptions, display_context, display_value, main, parameter_catalog, parameter_collection


class MenuBlockTests(unittest.TestCase):
    def run_cli(self, argv, replies):
        stdout, stderr, commands = io.StringIO(), io.StringIO(), []

        def run(command, **kwargs):
            telegram = command[-1]
            commands.append(telegram)
            return subprocess.CompletedProcess(command, 0, replies[telegram], "")

        with patch("read_menu_block.shutil.which", return_value="/usr/bin/ebusctl"), \
                patch("discover_parameters.subprocess.run", side_effect=run), \
                redirect_stdout(stdout), redirect_stderr(stderr):
            status = main([*argv, "--delay", "0"])
        return status, stdout.getvalue(), stderr.getvalue(), commands

    def collection_file(self, content):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "parameters.txt"
        path.write_text(content, encoding="utf-8")
        return path

    def test_collection_reads_only_selected_parameters_in_file_order(self):
        path = self.collection_file("\ufeff# Sammlung\n07-05 HK2 # Heizkreis\n\n00-01 hk1\n07-05\n7-5 HK2\n")
        entries = parameter_catalog(None, [b"\x10\x00"])
        expected = [("07-05", "HK2"), ("00-01", "HK1"), ("07-05", "HK1")]
        selected = [next(e for e in entries if (e["tem_id"], e["context"]) == key)
                    for key in expected]
        replies = {"1006230400005100": "done"}
        telegrams = []
        for entry in selected:
            selector, response = entry["request"], entry["sample_response"]
            telegram = f"150621{len(selector) // 2:02x}{selector}"
            telegrams.append(telegram)
            replies[telegram] = f"{len(response) // 2:02x}{response}"
        status, out, err, commands = self.run_cli(["--parameters-file", str(path), "--raw"], replies)
        self.assertEqual(status, 0)
        self.assertEqual(commands, ["1006230400005100", *telegrams])
        rows = [tuple(line.split()[:2]) for line in out.splitlines() if re.match(r"^\d+-\d+ ", line)]
        self.assertEqual(rows, expected)
        self.assertEqual(out.count("Antwort:"), 3)
        self.assertIn("3 Parameter, 0 unbelegte Plätze, 0 Fehler", err)

    def test_invalid_collections_fail_before_any_bus_access(self):
        for content, error in [
                ("# leer\n\n", "Parametersammlung ist leer"),
                ("07-05 HK1\ninvalid", ":2: erwartet TEM-Code"),
                ("32-00", "außerhalb"), ("03-128", "außerhalb"),
                ("31-127", "kein bekannter Zugriff"),
                ("07-05 WP", "kein bekannter Zugriff"),
                ("07-05 HK1 extra", "kein bekannter Zugriff")]:
            with self.subTest(content=content):
                path = self.collection_file(content)
                status, out, err, commands = self.run_cli(["--parameters-file", str(path)], {})
                self.assertEqual(status, 1)
                self.assertIn(error, err)
                self.assertEqual(commands, [])
        missing = self.collection_file("")
        missing.unlink()
        status, out, err, commands = self.run_cli(["--parameters-file", str(missing)], {})
        self.assertEqual(status, 1)
        self.assertIn(str(missing), err)
        self.assertEqual(commands, [])

    def test_collection_respects_context_options(self):
        path = self.collection_file("07-05")
        selected = parameter_collection(path, parameter_catalog(None, []))
        self.assertEqual([(e["tem_id"], e["context"]) for e in selected], [("07-05", "HK1")])
        path.write_text("07-05 HK2")
        status, out, err, commands = self.run_cli(
            ["--parameters-file", str(path), "--base-only"], {})
        self.assertEqual(status, 1)
        self.assertIn("kein bekannter Zugriff", err)
        self.assertEqual(commands, [])
        status, out, err, commands = self.run_cli(
            ["--parameters-file", str(path), "--context", "2000"], {})
        self.assertEqual(status, 1)
        self.assertIn("nur Zusatzkontext 1000", err)
        self.assertEqual(commands, [])

    def test_example_collection_uses_known_selectors(self):
        selected = parameter_collection(ROOT / "scripts/parameters.example.txt",
                                        parameter_catalog(None, [b"\x10\x00"]))
        self.assertTrue(selected)

    def test_individual_menu_live_values_and_contexts(self):
        replies = {"1506200114": "080100000000000082", "1006230400005100": "done",
                   "15062102a700": "0a85430400030000000300",
                   "15062102a701": "0aff1f0000000000000000",
                   "15062104a7801000": "0a85430400030000000100",
                   "15062104a7811000": "060c811e000500"}
        status, out, err, commands = self.run_cli(["--menu", "a7", "--raw"], replies)
        self.assertEqual(status, 0)
        self.assertEqual(commands[:2], ["1506200114", "1006230400005100"])
        self.assertNotIn("15062102a000", commands)
        self.assertIn("Heizkreistyp", out)
        self.assertIn("| 3", out)
        self.assertIn("| 1", out)
        self.assertIn("a7    HK1", out)
        self.assertIn("a7    HK2", out)
        self.assertEqual(out.splitlines()[0], "Menü  Kontext  TEM    Beschreibung | Aktueller Wert")
        self.assertNotIn("a7801000", out)
        self.assertIn("Sonderformat; roh: 0c 81 1e 00 05 00", out)
        self.assertIn("Antwort: 85430400030000000300", out)
        self.assertIn("3 Parameter, 1 unbelegte Plätze, 0 Fehler", err)

    def test_tem_display_modes(self):
        # Exercise the boundary and a three-digit parameter number numerically.
        replies = {"1506200100": "080300000000000000", "1006230400005100": "done",
                   "150621020000": "0a7f010400030000000100",  # 02-127
                   "150621020001": "0a80410400030000000200",  # 03-00
                   "150621020002": "0a00450400030000000300"}  # 10-00
        for mode, expected, excluded in [
                ([], ["02-127", "03-00", "10-00"], []),
                (["--from-03-00"], ["03-00", "10-00"], ["02-127"]),
                (["--before-03-00"], ["02-127"], ["03-00", "10-00"])]:
            with self.subTest(mode=mode):
                status, out, err, commands = self.run_cli(["00", "--raw", *mode], replies)
                self.assertEqual(status, 0)
                self.assertEqual(len(commands), 5)
                for ident in expected:
                    self.assertIn(ident, out)
                for ident in excluded:
                    self.assertNotIn(ident, out)
                self.assertEqual(out.count("Antwort:"), len(expected))
                if mode:
                    self.assertIn(f"{len(expected)} angezeigt, {len(excluded)} ausgefiltert.", err)

    def test_sorted_parameter_modes_from_full_scan(self):
        with (ROOT / "commands.txt").open() as handle:
            scan = {r["selector"]: r for r in csv.DictReader(handle, delimiter="\t")}
        for before, flag, expected_count in [(True, "--before-03-00", 115),
                                             (False, "--from-03-00", 213)]:
            with self.subTest(flag=flag):
                entries = parameter_catalog(before, [b"\x10\x00"])
                self.assertEqual(len(entries), expected_count)
                self.assertEqual(len({(e["tem_id"], e["context"]) for e in entries}), expected_count)
                replies = {"1006230400005100": "done"}
                for entry in entries:
                    selector = entry["request"]
                    response = scan[selector]["response"]
                    replies[f"150621{len(selector) // 2:02x}{selector}"] = f"{len(response) // 2:02x}{response}"
                status, out, err, commands = self.run_cli([flag], replies)
                self.assertEqual(status, 0)
                self.assertNotIn("150620", " ".join(commands))
                self.assertEqual(len(commands), expected_count + 1)
                lines = [line for line in out.splitlines() if re.match(r"^\d+-\d+ ", line)]
                codes = [tuple(map(int, line.split()[0].split("-"))) for line in lines]
                self.assertEqual(len(codes), expected_count)
                self.assertEqual(codes, sorted(codes))
                self.assertTrue(all((code < (3, 0)) == before for code in codes))
                self.assertIn("HK1", out)
                self.assertIn("HK2", out)
                self.assertIn("WE8", out)
                if before:
                    self.assertRegex(out, r"02-20\s+HK1\s+Soll\s+Aussentemperatur Mittelwert")
                    self.assertRegex(out, r"00-01\s+HK2\s+Ist\s+Raumtemperatur 2")
                    self.assertRegex(out, r"01-01\s+HK1\s+Soll\s+Raumtemperatur 1")
                    self.assertRegex(out, r"01-20\s+HK1\s+—")
                else:
                    self.assertIn("WP", out)
                    self.assertIn("EH", out)

    def test_table_assignment_preserves_missing_and_ambiguous_roles(self):
        descriptions = Descriptions()
        role, label = descriptions.assignment("00-07", "HK1")
        self.assertEqual(role, "Ist")
        self.assertIn("WP-Vorlauftemperatur", label)
        self.assertIn("EH-Vorlauftemperatur", label)
        self.assertEqual(descriptions.assignment("00-09", "WE4"), ("—", ""))
        role, label = descriptions.assignment("01-09", "WE8")
        self.assertEqual(role, "Soll")
        self.assertIn("WE 8", label)
        self.assertNotIn("WE 1", label)
        base = parameter_catalog(True, [])
        self.assertTrue(base)
        self.assertTrue(all(len(e["request"]) == 4 for e in base))
        with self.assertRaisesRegex(ValueError, "nur Zusatzkontext 1000"):
            parameter_catalog(True, [b"\x20\x00"])

    def test_parameter_mode_reports_failures_and_continues(self):
        entries = parameter_catalog(True, [b"\x10\x00"])[:4]
        responses = ["0aff1f0000000000000000", "ERR: timeout",
                     "0a80410400030000000200", "0a00000d02f4010cfe6400"]
        # Last entry is 00-01: provide a valid fresh response with that identifier.
        responses[-1] = "0a01000d02f4010cfe6400"
        replies = {"1006230400005100": "done"}
        for entry, response in zip(entries, responses):
            selector = entry["request"]
            replies[f"150621{len(selector) // 2:02x}{selector}"] = response
        with patch("read_menu_block.parameter_catalog", return_value=entries):
            status, out, err, commands = self.run_cli(["--before-03-00"], replies)
        self.assertEqual(status, 1)
        self.assertIn("nicht verfügbar (ff1f)", out)
        self.assertIn("Fehler: ERR: timeout", out)
        self.assertIn("Antwort enthält 03-00", out)
        self.assertIn("| 10 °C", out)
        self.assertIn("1 Parameter, 1 unbelegte Plätze, 2 Fehler", err)

    def test_parameter_mode_refreshes_expert_and_aborts_on_enable_failure(self):
        entries = parameter_catalog(False, [])[:2]
        replies = {"1006230400005100": "done"}
        for entry in entries:
            selector = entry["request"]
            response = entry["sample_response"]
            replies[f"150621{len(selector) // 2:02x}{selector}"] = f"{len(response) // 2:02x}{response}"
        with patch("read_menu_block.parameter_catalog", return_value=entries), \
                patch("read_menu_block.time.monotonic", side_effect=[0, 61, 61]):
            status, out, err, commands = self.run_cli(["--from-03-00"], replies)
        self.assertEqual(status, 0)
        self.assertEqual(commands.count("1006230400005100"), 2)
        status, out, err, commands = self.run_cli(["--from-03-00"],
                                                {"1006230400005100": "ERR: no ACK"})
        self.assertEqual(status, 1)
        self.assertEqual(commands, ["1006230400005100"])

    def test_interpreted_contexts_and_aliases(self):
        cases = [(0xa7, "base", "HK1"), (0xa7, "1000", "HK2"),
                 (0x67, "1000", "HK2"), (0xa9, "base", "WP"),
                 (0x69, "base", "WP"), (0xaa, "base", "EH"),
                 (0x6a, "base", "EH"), (0xa5, "base", "Global"),
                 (0x29, "base", "Menü 29"), (0xa7, "2000", "Unbekannt (2000)"),
                 (0xa9, "1000", "Unbekannt (1000)")]
        for number in range(1, 9):
            cases.extend([(0xaa + number, "base", f"WE{number}"),
                          (0x6a + number, "base", f"WE{number}")])
        for menu, context, expected in cases:
            with self.subTest(menu=menu, context=context):
                self.assertEqual(display_context(menu, context), expected)

    def test_whole_block_and_partial_failure(self):
        replies = {"1506200114": "080200000000000001", "1006230400005100": "done",
                   "15062102a000": "ERR: timeout", "15062102a001": "03abcd00",
                   "15062102a700": "0a80438d042c0132009600"}
        status, out, err, commands = self.run_cli(["14", "--base-only"], replies)
        self.assertEqual(status, 1)
        self.assertIn("| 15 K", out)
        self.assertIn("2 Fehler", err)
        self.assertEqual(len(commands), 5)

    def test_expert_failure_prevents_parameter_reads(self):
        status, out, err, commands = self.run_cli(["00"], {
            "1506200100": "080100000000000000", "1006230400005100": "ERR: no ACK"})
        self.assertEqual(status, 1)
        self.assertEqual(len(commands), 2)
        self.assertIn("skipping parameters", err)

    def test_invalid_selection_rejected_before_bus_access(self):
        for argv in ([], ["20"], ["14", "--menu", "a7"], ["--menu", "100"],
                     ["14", "--delay", "nan"],
                     ["14", "--from-03-00", "--before-03-00"],
                     ["14", "--parameters-file", "params.txt"],
                     ["--menu", "a7", "--parameters-file", "params.txt"],
                     ["--from-03-00", "--parameters-file", "params.txt"],
                     ["--before-03-00", "--parameters-file", "params.txt"]):
            with self.subTest(argv=argv), redirect_stderr(io.StringIO()), \
                    patch("discover_parameters.subprocess.run") as run:
                with self.assertRaises(SystemExit) as exc:
                    main(argv)
                self.assertEqual(exc.exception.code, 2)
                run.assert_not_called()

    def test_decoding_known_and_special_values(self):
        cases = [
            ("03-07", "87410d06640000000f00", "1.5"),
            ("03-10", "8a410408f40100008200", "1.3"),
            ("09-12", "8c444d02f4010cfeceff", "-5 °C"),
            ("04-30", "1e420200010000000100", "Ein (1)"),
            ("04-30", "1e42020001000000ffff", "nicht verfügbar"),
            ("09-12", "8c444d02f4010cfe0080", "nicht verfügbar"),
            ("15-29", "9c4701020a00e2ffe200", "-30 °C"),
            ("15-29", "9c4701020a00e2ff8000", "nicht verfügbar"),
            ("02-71", "47c1042a602700009f0f", "3999 min (Wochenminuten)"),
            ("02-70", "46c10428000000000000", "1900-01-01"),
        ]
        for ident, payload, expected in cases:
            with self.subTest(ident=ident, payload=payload):
                self.assertEqual(display_value(ident, bytes.fromhex(payload)), expected)
        for payload in ("0c811e000500", "50c11d00010026000000", "8543fe00000000000000"):
            self.assertIn("Sonderformat; roh:", display_value("02-12", bytes.fromhex(payload)))
        self.assertIn("Unbekanntes Antwortformat", display_value("02-12", b"\0" * 8))

    def test_descriptions_and_all_scan_payloads(self):
        descriptions = Descriptions()
        self.assertIn("Heizkreistyp", descriptions.lookup("07-05", 0xa7))
        self.assertIn("WE 2", descriptions.lookup("01-09", 0xac))
        self.assertNotIn("WE 1", descriptions.lookup("01-09", 0x6c))
        self.assertEqual(descriptions.lookup("31-127", 0), "Beschreibung unbekannt")
        with (ROOT / "commands.txt").open() as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                with self.subTest(selector=row["selector"]):
                    self.assertTrue(display_value(row["tem"], bytes.fromhex(row["response"])))
                    self.assertTrue(descriptions.lookup(row["tem"], int(row["menu"], 16)))


if __name__ == "__main__":
    unittest.main()
