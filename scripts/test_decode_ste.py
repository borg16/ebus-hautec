"""Structural regression checks against the supplied TEM archive."""

import csv
import json
import struct
import tempfile
import unittest
from pathlib import Path

from decode_ste import FormatError, Reader, parse_archive, write_exports


SOURCE = Path(__file__).resolve().parents[1] / "Datapacks v 1.1  über V 52  9.02.09.ste"


def encode_string(text):
    data = text.encode("cp1252")
    length = len(data)
    if length < 255:
        prefix = struct.pack("<B", length)
    elif length < 65534:
        prefix = b"\xff" + struct.pack("<H", length)
    else:
        prefix = b"\xff\xff\xff" + struct.pack("<I", length)
    return prefix + data


def rebuild(archive):
    """Independent field-by-field reconstruction, not a raw-byte copy."""
    parts = [struct.pack("<H", archive["record_count"])]
    for index, record in enumerate(archive["records"]):
        parts.append(struct.pack("<H", record["class_tag_raw"]))
        if index == 0:
            name = archive["class_name"].encode("ascii")
            parts.append(struct.pack("<HH", archive["schema"], len(name)) + name)
        parts.append(struct.pack("<4I", *record["header_raw"]))
        parts.append(encode_string(record["title"]))
        for name in ("address_low_raw", "address_high_raw", "type_raw"):
            parts.append(struct.pack("<I", record[name]))
        for name in ("maximum", "minimum", "step_raw", "stored_value"):
            parts.append(struct.pack("<d", record[name]))
        for name in ("position_raw", "page_raw", "entry_key_raw", "variant_flag_raw", "unit_raw"):
            parts.append(struct.pack("<I", record[name]))
        parts += [encode_string(record["help_text"]), encode_string(record["group_text"]),
                  struct.pack("<3I", *record["tail_raw"]),
                  encode_string(record["author_text"]), encode_string(record["controller_text"])]
    return b"".join(parts)


class ArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not SOURCE.exists():
            raise unittest.SkipTest("The original .ste fixture is not available")
        cls.data = SOURCE.read_bytes()
        cls.archive = parse_archive(cls.data, SOURCE.name)

    def test_byte_exact_reconstruction(self):
        self.assertEqual(len(self.data), 64974)
        self.assertEqual(self.archive["source_sha256"],
                         "1ba1f84ba2f481f9ed235e3231edb4b100484159b44efaaa765124a888deeebe")
        self.assertEqual(rebuild(self.archive), self.data)

    def test_records_and_values(self):
        records = self.archive["records"]
        self.assertEqual(len(records), 217)
        self.assertEqual(sum(r["tem_id"] is not None for r in records), 206)
        self.assertEqual(len({r["tem_id"] for r in records if r["tem_id"]}), 119)
        self.assertEqual(records[8]["tem_id"], "03-51")
        self.assertEqual(records[8]["stored_value"], 20.5)
        self.assertEqual(records[8]["fields_offset"] + 36, 0x782)
        self.assertEqual(records[14]["stored_value"], 0.3)
        self.assertEqual(records[135]["tem_id"], "15-22")
        self.assertEqual(records[135]["stored_value"], -12)
        self.assertEqual(sorted(len(r["help_text"]) for r in records if len(r["help_text"]) >= 255),
                         [271, 279, 400])
        self.assertEqual(records[-1]["end_offset"], len(self.data))
        for r in records:
            self.assertLessEqual(r["minimum"], r["stored_value"])
            self.assertLessEqual(r["stored_value"], r["maximum"])
            self.assertEqual(r["entry_key_raw"],
                             (r["page_raw"] << 11) + (r["position_raw"] << 4) + r["variant_index"])

    def test_invalid_archives_fail(self):
        for length in (0, 1, 2, 16, len(self.data) // 2, len(self.data) - 1):
            with self.subTest(length=length), self.assertRaises(FormatError):
                parse_archive(self.data[:length])
        with self.assertRaisesRegex(FormatError, "Unconsumed"):
            parse_archive(self.data + b"\x00")
        wrong_tag = bytearray(self.data)
        second = self.archive["records"][1]["offset"]
        wrong_tag[second:second + 2] = b"\x00\x00"
        with self.assertRaisesRegex(FormatError, "class reference"):
            parse_archive(wrong_tag)
        wrong_schema = bytearray(self.data)
        wrong_schema[4] = 2
        with self.assertRaisesRegex(FormatError, "Unsupported class/schema"):
            parse_archive(wrong_schema)

    def test_exports_preserve_all_records_and_texts(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            write_exports(self.archive, output)
            decoded = json.loads((output / "parameter.json").read_text(encoding="utf-8"))
            self.assertEqual(decoded, self.archive)
            with (output / "parameter.csv").open(encoding="utf-8-sig", newline="") as handle:
                csv_records = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual(len(csv_records), 217)
            indexed = {int(row["index"]): row for row in csv_records}
            for record in self.archive["records"]:
                self.assertEqual(indexed[record["index"]]["help_text"], record["help_text"])
            self.assertEqual(indexed[9]["stored_value"], "20,5")
            markdown = (output / "Parameter.md").read_text(encoding="utf-8")
            self.assertEqual(markdown.count('<a id="datensatz-'), 217)


class StringTests(unittest.TestCase):
    def test_length_prefix_boundaries(self):
        for length in (0, 254, 255, 400, 65534, 65536):
            with self.subTest(length=length):
                text = "ä" * length
                reader = Reader(encode_string(text))
                self.assertEqual(reader.string(), text)
                self.assertEqual(reader.pos, len(reader.data))

    def test_unicode_marker_rejected(self):
        with self.assertRaisesRegex(FormatError, "Unicode"):
            Reader(b"\xff\xfe\xff").string()


if __name__ == "__main__":
    unittest.main()
