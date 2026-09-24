"""Offline tests; no connection to ebusd or the heating controller."""

from argparse import Namespace
import subprocess
import unittest
from unittest.mock import patch

from discover_parameters import Reader, discover, parse_response


class DiscoveryTests(unittest.TestCase):
    def reader(self):
        return Reader(Namespace(server="localhost", port=8888, destination=0x15,
                                expert_destination=0x10, timeout=5, delay=0))

    def test_directory_contexts_duplicates_and_commands(self):
        # One flagged menu with two slots; another ordinary menu with one slot.
        replies = {
            "1006230400005100": "done",
            "1506200114": "08 82 01 00 00 00 00 00 00",
            "15062102a000": "0a85430400030000000200",
            "15062102a001": "0aff1f0000000000000000",
            "15062104a0801000": "0a85430400030000000300",
            "15062104a0811000": "06 0c811e000500",
            "15062102a100": "0a85430400030000000000",
        }
        commands, rows, errors = [], [], []

        def run(command, **kwargs):
            commands.append(command)
            self.assertEqual(command[-2], "hex")
            return subprocess.CompletedProcess(command, 0, replies[command[-1]], "")

        with patch("discover_parameters.subprocess.run", side_effect=run):
            counts = discover(self.reader(), [0x14], [b"\x10\x00"], rows.append, errors.append)
        self.assertEqual(counts, {"accessible": 4, "unavailable": 1, "errors": 0})
        self.assertEqual(errors, [])
        self.assertEqual(len(commands), 7)
        self.assertEqual([c[-1] for c in commands[:3]],
                         ["1506200114", "1006230400005100", "15062102a000"])
        self.assertEqual(sum(c[-1] == "1006230400005100" for c in commands), 1)
        self.assertEqual([r["tem"] for r in rows], ["07-05", "07-05", "02-12", "07-05"])
        self.assertEqual(rows[1]["selector"], "a0801000")
        self.assertEqual(rows[1]["context"], "1000")
        self.assertNotIn("read_command", rows[1])

    def test_disabled_hex_aborts_instead_of_scanning_every_slot(self):
        for status in (0, 1):
            with self.subTest(status=status), patch("discover_parameters.subprocess.run", return_value=
                    subprocess.CompletedProcess([], status, "ERR: command not enabled", "")) as run:
                with self.assertRaisesRegex(RuntimeError, "--enablehex"):
                    discover(self.reader(), range(28), [], lambda row: None, lambda error: None)
                self.assertEqual(run.call_count, 1)

    def test_write_services_are_rejected(self):
        with self.assertRaises(ValueError):
            self.reader().command("0623", b"\0\0")

    def test_bad_block_skipped_but_later_block_scanned(self):
        reader = self.reader()
        rows, errors = [], []
        with patch.object(reader, "enable_expert") as enable, \
                patch.object(reader, "read", side_effect=[b"short", b"\0" * 8]) as read:
            counts = discover(reader, [0, 1], [], rows.append, errors.append)
        enable.assert_called_once()
        self.assertEqual(read.call_count, 2)
        self.assertEqual(counts["errors"], 1)
        self.assertEqual(rows, [])

    def test_base_only_and_bad_parameter_does_not_stop_scan(self):
        reader = self.reader()
        rows, errors = [], []
        with patch.object(reader, "enable_expert"), patch.object(reader, "read", side_effect=[b"\x82" + b"\0" * 7,
                                                      ValueError("timeout"),
                                                      bytes.fromhex("0c811e000500")]) as read:
            counts = discover(reader, [0], [], rows.append, errors.append)
        self.assertEqual(read.call_count, 3)
        self.assertEqual(counts["errors"], 1)
        self.assertEqual(rows[0]["tem"], "02-12")
        self.assertEqual(rows[0]["selector"], "0001")

    def test_malformed_response_rejected(self):
        for response in ("", "ERR: timeout", "08abcdef", "1", "0g", "0000"):
            with self.subTest(response=response), self.assertRaises(ValueError):
                parse_response(response)

    def test_enable_failure_skips_block_and_next_block_enables_again(self):
        reader = self.reader()
        events, rows, errors = [], [], []

        def read(service, selector):
            events.append((service, selector.hex()))
            return b"\1" + b"\0" * 7 if service == "0620" else bytes.fromhex("0c811e000500")

        def enable():
            events.append(("enable", ""))
            if len(events) == 2:
                raise ValueError("no ACK")

        with patch.object(reader, "read", side_effect=read), \
                patch.object(reader, "enable_expert", side_effect=enable):
            counts = discover(reader, [0, 1], [], rows.append, errors.append)
        self.assertEqual(events, [("0620", "00"), ("enable", ""),
                                  ("0620", "01"), ("enable", ""), ("0621", "0800")])
        self.assertEqual(counts, {"accessible": 1, "unavailable": 0, "errors": 1})

    def test_expert_requires_done_and_uses_configured_target(self):
        reader = self.reader()
        reader.args.expert_destination = 0x30
        with patch.object(reader, "execute", return_value="done\n") as execute:
            reader.enable_expert()
        self.assertEqual(execute.call_args.args[0][-1], "3006230400005100")
        with patch.object(reader, "execute", return_value="00"):
            with self.assertRaisesRegex(ValueError, "unexpected"):
                reader.enable_expert()

    def test_process_error_and_timeout(self):
        reader = self.reader()
        with patch("discover_parameters.subprocess.run", return_value=
                   subprocess.CompletedProcess([], 1, "ERR: no signal", "")):
            with self.assertRaisesRegex(ValueError, "no signal"):
                reader.read("0620", b"\0")
        with patch("discover_parameters.subprocess.run", side_effect=subprocess.TimeoutExpired([], 5)):
            with self.assertRaisesRegex(ValueError, "timeout"):
                reader.read("0620", b"\0")


if __name__ == "__main__":
    unittest.main()
