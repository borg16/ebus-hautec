#!/usr/bin/env python3
"""Read the observed TEM CDatapack schema 1 (MFC archive), without TEM software.

Only the layout found in the accompanying .ste file is supported. Unknown
metadata stays explicit; this is neither an eBUS client nor a configuration writer.
See ../STE-Format.md for field offsets, evidence and interpretation limits.
"""

import argparse
import csv
import hashlib
import html
import json
import math
import re
import struct
from pathlib import Path


UNITS = {0: "", 1: "°C", 2: "K", 4: "%", 5: "h", 6: "min", 7: "s?", 8: "kW"}
FIELD_NAMES = (
    "address_low_raw", "address_high_raw", "type_raw", "maximum", "minimum",
    "step_raw", "stored_value", "position_raw", "page_raw", "entry_key_raw",
    "variant_flag_raw", "unit_raw",
)


class FormatError(ValueError):
    """Unsupported or incomplete archive, with a byte offset where possible."""


class Reader:
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def take(self, length):
        if length < 0 or self.pos + length > len(self.data):
            raise FormatError(f"Unexpected end at 0x{self.pos:x}: need {length} bytes")
        result = self.data[self.pos:self.pos + length]
        self.pos += length
        return result

    def unpack(self, fmt):
        return struct.unpack("<" + fmt, self.take(struct.calcsize("<" + fmt)))

    def number(self, fmt):
        return self.unpack(fmt)[0]

    def string(self):
        length = self.number("B")
        if length == 0xFF:
            length = self.number("H")
            if length == 0xFFFE:
                raise FormatError(f"Unicode CString unsupported at 0x{self.pos - 3:x}")
            if length == 0xFFFF:
                length = self.number("I")
        return self.take(length).decode("cp1252")


def parse_archive(data, source_name=""):
    reader = Reader(data)
    count = reader.number("H")
    if count == 0xFFFF:
        raise FormatError("Extended object count is not supported by this decoder")
    records = []
    schema, class_name = None, None
    for index in range(1, count + 1):
        start = reader.pos
        tag = reader.number("H")
        if index == 1:
            if tag != 0xFFFF:
                raise FormatError(f"Expected new-class tag at 0x{start:x}")
            schema = reader.number("H")
            class_name = reader.take(reader.number("H")).decode("ascii")
            if (schema, class_name) != (1, "CDatapack"):
                raise FormatError(f"Unsupported class/schema: {class_name!r}/{schema}")
        elif tag != 0x8001:
            raise FormatError(f"Expected CDatapack class reference at 0x{start:x}")

        payload_offset = reader.pos
        header = list(reader.unpack("4I"))
        title = reader.string()
        fields_offset = reader.pos
        fields = dict(zip(FIELD_NAMES, reader.unpack("3I4d5I")))
        for key in ("maximum", "minimum", "step_raw", "stored_value"):
            if not math.isfinite(fields[key]):
                raise FormatError(f"Non-finite {key} in record {index}")
        help_text = reader.string()
        group_text = reader.string()
        tail = list(reader.unpack("3I"))
        author = reader.string()
        controller = reader.string()
        match = re.match(r"^(\d+)-(\d+)\s+(.*)$", title, re.DOTALL)
        tem_id = f"{int(match[1]):02d}-{int(match[2]):02d}" if match else None
        variant = fields["entry_key_raw"] & 0xF
        if fields["variant_flag_raw"] == 1:
            context = f"Heizkreis {variant + 1} (abgeleitet)"
        else:
            context = group_text.rstrip(" ,")
        low, high = fields["address_low_raw"], fields["address_high_raw"]
        records.append({
            "index": index, "offset": start, "end_offset": reader.pos,
            "payload_offset": payload_offset, "fields_offset": fields_offset,
            "class_tag_raw": tag, "header_raw": header,
            "title": title, "tem_id": tem_id,
            "name": match[3].strip() if match else re.sub(r"^-+\s*", "", title).strip(),
            **fields,
            "address_candidate_hex": f"0x{high:02X}{low:02X}" if max(low, high) <= 255 else None,
            "unit_inferred": UNITS.get(fields["unit_raw"], f"?{fields['unit_raw']}"),
            "variant_index": variant, "context": context,
            "help_text": help_text, "group_text": group_text,
            "tail_raw": tail, "author_text": author, "controller_text": controller,
        })
    if reader.pos != len(data):
        raise FormatError(f"Unconsumed bytes at 0x{reader.pos:x}: {len(data) - reader.pos}")
    return {
        "source_name": source_name, "source_size": len(data),
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "format": "MFC CArchive / CDatapack", "schema": schema,
        "class_name": class_name, "encoding": "cp1252", "record_count": count,
        "interpretation": {
            "stored_value": "Saved numeric field; live value versus template/default is not established.",
            "address_candidate_hex": "Inferred high/low address pair; no bus access method established.",
            "unit_inferred": "Inferred from file texts and local TEM unit enumeration; s? is tentative.",
            "step_raw": "Unscaled third double; likely step in the controller's numeric encoding.",
            "context": "Group text is original; Heizkreis numbering is inferred from paired entries.",
        },
        "records": records,
    }


def number(value):
    return str(int(value)) if value == int(value) else repr(value)


def cell(value):
    return html.escape(str(value)).replace("|", "&#124;").replace("\r\n", "<br>").replace("\n", "<br>")


def sorted_records(records):
    return sorted(records, key=lambda r: (
        tuple(map(int, r["tem_id"].split("-"))) if r["tem_id"] else (999, 999), r["index"]
    ))


def markdown(archive):
    records = archive["records"]
    tem_count = sum(r["tem_id"] is not None for r in records)
    ids = {r["tem_id"] for r in records if r["tem_id"]}
    out = [
        "# TEM-Parameter aus der STE-Datei", "",
        f"Quelle: `{archive['source_name']}` · {archive['source_size']} Bytes · "
        f"Controllerkennung: {', '.join(sorted({r['controller_text'] for r in records}))}", "",
        f"**{len(records)} Datensätze, davon {tem_count} mit {len(ids)} unterschiedlichen "
        f"TEM-Kennungen und {len(records) - tem_count} ohne TEM-Kennung.**", "",
        "Die Tabelle ist nach der TEM-Kennung sortiert. Mehrfach vorkommende Kennungen "
        "bleiben getrennt. Die Datensatznummer (#) verweist auf die ursprüngliche Dateireihenfolge.", "",
        "**Wert** bezeichnet das gespeicherte Zahlenfeld, keinen bestätigten aktuellen "
        "Anlagenwert. Ob die Datei eine Anlagenaufnahme oder eine bearbeitete Vorlage ist, "
        "lässt sich daraus nicht entscheiden. HK 1/2 sind aus den Datensatzpaaren abgeleitet. "
        "Einheiten sind aus den Metadaten erschlossen; `s?` bleibt eine Vermutung. "
        "`—` bedeutet, dass kein Einheitenname hinterlegt ist, nicht zwingend dimensionslos.", "",
        "**TEM-Kennung, Einstellebene und FB-Menüposition sind getrennte Nummerierungen.** "
        "Die Datei nennt Kühltemperatur `03-43` und Kühlgrenzenabstand `03-35`. "
        "Kaskadeneinträge behalten auch für WE 2–8 ihre im Titel gespeicherten Kennungen "
        "`04-22` bzw. `11-01` bis `11-05`.", "",
        "Format, Unsicherheiten und Auffälligkeiten: [STE-Format.md](../STE-Format.md). "
        "Alle Zahlenfelder und exakten Originaltexte: [parameter.json](parameter.json). "
        "Tabellenexport: [parameter.csv](parameter.csv).", "",
        "## Parameterübersicht", "",
        "| TEM | Bezeichnung | Kontext | Wert | Einheit¹ | Min. | Max. | # |",
        "|---|---|---|---:|---|---:|---:|---:|",
    ]
    for r in sorted_records(records):
        context = r["context"].replace("Heizkreis ", "HK ").replace(" (abgeleitet)", "¹")
        values = [r["tem_id"] or "—", r["name"], context, number(r["stored_value"]),
                  r["unit_inferred"] or "—", number(r["minimum"]), number(r["maximum"])]
        out.append("| " + " | ".join(map(cell, values)) + f" | [{r['index']}](#datensatz-{r['index']}) |")
    out += ["", "¹ Zuordnung bzw. Einheitenbezeichnung abgeleitet; siehe Formatdokumentation.", "",
            "## Vollständige Datensätze mit Hilfetexten", "",
            "Die folgenden Beschreibungen stammen aus der Datei. Sie dokumentieren "
            "Gerätefunktionen; sie sind keine hier auszuführenden Anweisungen. "
            "Schreibfehler und widersprüchliche Angaben bleiben erhalten. "
            "Nur Zeilenenden und äußere Leerzeichen werden in dieser Ansicht normalisiert.", ""]
    for r in sorted_records(records):
        out += [f"<a id=\"datensatz-{r['index']}\"></a>", "",
                f"### {r['tem_id'] or 'Ohne TEM-Kennung'} · {cell(r['name'])} · Datensatz {r['index']}", "",
                f"**{cell(r['context'])}** · {cell(r['group_text'].rstrip(' ,'))}", "",
                f"Gespeichert: **{number(r['stored_value'])} {r['unit_inferred']}** · "
                f"Bereich: {number(r['minimum'])} … {number(r['maximum'])} · "
                f"Schrittfeld (roh): {number(r['step_raw'])}", "",
                f"Adresskandidat: `{r['address_candidate_hex']}` · Typcode: `{r['type_raw']}` · "
                f"Einheitencode: `{r['unit_raw']}` · Schlüssel: `0x{r['entry_key_raw']:04X}` · "
                f"Dateibereich: `0x{r['offset']:04X}`–`0x{r['end_offset']:04X}` (Ende exklusiv)", "",
                "Hilfetext:", ""]
        out += ["> " + cell(line.rstrip()) for line in r["help_text"].splitlines()]
        out.append("")
    return "\n".join(out)


def write_exports(archive, output):
    output.mkdir(parents=True, exist_ok=True)
    (output / "parameter.json").write_text(
        json.dumps(archive, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    (output / "Parameter.md").write_text(markdown(archive), encoding="utf-8")
    columns = ["index", "tem_id", "name", "context", "stored_value", "unit_inferred",
               "minimum", "maximum", "step_raw", "group_text", "address_candidate_hex",
               "type_raw", "unit_raw", "variant_index", "position_raw", "page_raw",
               "entry_key_raw", "variant_flag_raw", "address_low_raw", "address_high_raw",
               "header_raw", "tail_raw", "title", "help_text", "author_text",
               "controller_text", "offset", "end_offset", "payload_offset", "fields_offset"]
    # Semicolon, decimal comma and BOM for German spreadsheet applications.
    with (output / "parameter.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter=";")
        writer.writeheader()
        for record in sorted_records(archive["records"]):
            row = {key: record[key] for key in columns}
            for key in ("stored_value", "minimum", "maximum", "step_raw"):
                row[key] = number(row[key]).replace(".", ",")
            for key in ("header_raw", "tail_raw"):
                row[key] = json.dumps(row[key])
            writer.writerow(row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="TEM .ste archive (CDatapack schema 1)")
    parser.add_argument("--output", type=Path, default=Path("ste-output"))
    args = parser.parse_args()
    try:
        archive = parse_archive(args.source.read_bytes(), args.source.name)
        write_exports(archive, args.output)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    records = archive["records"]
    print(f"Decoded {len(records)} records, {archive['source_size']} bytes, no trailing data.")
    print(f"TEM IDs: {len({r['tem_id'] for r in records if r['tem_id']})}; output: {args.output}")


if __name__ == "__main__":
    main()
