#!/usr/bin/env python3
"""Validate TEM raw telegrams and generate controller.tsp from observed requests.

Offline only. Does not infer writes from changing response values or invent
request addresses for parameters absent from the capture. The complete session
log also contains 06 23 writes; those are ignored by the read catalog here.
"""

import argparse
import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def unescape(raw):
    result = bytearray()
    i = 0
    while i < len(raw):
        value = raw[i]
        i += 1
        if value == 0xA9:
            if i == len(raw) or raw[i] not in (0, 1):
                raise ValueError("invalid escape sequence")
            value += raw[i]
            i += 1
        elif value == 0xAA:
            raise ValueError("unescaped SYN inside telegram")
        result.append(value)
    return bytes(result)


def crc(data):
    """eBUS CRC: polynomial 0x9b, update = table[crc] XOR symbol.

    CRC covers escaped wire symbols, excluding the CRC symbol itself.
    Reference: john30/ebusd src/lib/ebus/symbol.cpp, updateCrc/calcCrc.
    """
    result = 0
    for value in data:
        wire = (0xA9, value - 0xA9) if value in (0xA9, 0xAA) else (value,)
        for symbol in wire:
            for _ in range(8):
                result = ((result << 1) ^ (0x9B if result & 0x80 else 0)) & 0xFF
            result ^= symbol
    return result


def parse_line(line, line_number):
    match = re.fullmatch(r"(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d\.\d{3}) <([0-9a-fA-F]+)", line)
    if not match:
        raise ValueError("unsupported raw log line")
    data = unescape(bytes.fromhex(match[2]))
    if len(data) < 6:
        raise ValueError("truncated master header")
    end = 5 + data[4]
    if len(data) <= end:
        raise ValueError("truncated master payload/CRC")
    if crc(data[:end]) != data[end]:
        raise ValueError("master CRC mismatch")
    result = {
        "line": line_number, "time": match[1], "source": f"{data[0]:02x}",
        "destination": f"{data[1]:02x}", "service": data[2:4].hex(),
        "request": data[5:end].hex(), "master": data[:end].hex(),
    }
    if len(data) == end + 1:
        return {**result, "status": "request_only"}
    if len(data) < end + 5 or len(data) != end + 5 + data[end + 2]:
        raise ValueError("slave length mismatch")
    if data[end + 1] != 0 or data[-1] != 0:
        raise ValueError("transaction not acknowledged")
    if crc(data[end + 2:-2]) != data[-2]:
        raise ValueError("slave CRC mismatch")
    return {**result, "status": "complete", "response": data[end + 3:-2].hex(),
            "slave": data[end + 2:-2].hex()}


def read_log(path):
    records, errors = [], []
    for number, line in enumerate(path.read_text().splitlines(), 1):
        try:
            records.append(parse_line(line, number))
        except ValueError as exc:
            errors.append({"line": number, "error": str(exc)})
    return records, errors


def tem_id(response):
    word = int.from_bytes(bytes.fromhex(response)[:2], "little")
    return f"{(word >> 7) & 31:02d}-{word & 127:02d}"


def value_model(ident, data):
    typ, unit = data[2:4]
    if len(data) == 6:
        return "Kurzantwort", "6-Byte-Sonderantwort; keine normale Wertstruktur"
    if len(data) != 10:
        raise ValueError(f"unhandled parameter response length: {len(data)}")
    if typ == 0x1D:
        return "Sonderantwort", "Typ 1d: sechs Byte Nutzdaten roh (keine erfundenen Min/Max/Wert-Felder)"
    if typ in (0x0D, 0x4D, 0x8D):
        names = {2: "Celsius10", 4: "Kelvin10", 8: "Prozent10", 10: "Stunden10",
                 12: "Minuten10", 14: "Sekunden10", 16: "Kilowatt10"}
        if unit in names:
            return f"Zahlenantwort<{names[unit]}>", "SIN / 10; Einheit aus Antwort"
    if ident == "03-10" and (typ, unit) == (4, 8):
        return "Zahlenantwort<Steilheit100>", "SIN / 100, aus Antwortgrenze 500 und STE-Grenze 5 abgeleitet"
    if ident == "02-70" and (typ, unit) == (4, 40):
        return "RohgrenzenAntwort<DAY>", "DAY: Tage seit 1900; Datum des Reglers, nicht Log-Zeitstempel"
    if (typ, unit) == (4, 42):
        return "RohgrenzenAntwort<Wochenminuten>", "UIN, Minutenwert bis 10080; keine MIN-Uhrzeit bis 24 h"
    if typ in (1, 0xC1):
        return "RohgrenzenAntwort<ByteMitVorzeichen>", "SCH plus ein Byte Padding; kein vorzeichenbehaftetes 16-Bit-Wort"
    if typ == 2 and unit == 0:
        return "RohgrenzenAntwort<Schalter>", "UIN: 0=Aus, 1=Ein"
    if typ in (0, 4, 9):
        return "RohgrenzenAntwort<UIN>", "UIN; Auswahl/Integer, Grenzen als Rohbytes (Typ 09: Masken möglich)"
    return "Sonderantwort", "unbekannte Spezialkodierung; sechs Byte Nutzdaten vollständig roh"


def build_catalog(records, ste):
    grouped = defaultdict(list)
    for record in records:
        if (record["status"] == "complete" and
                (record["source"], record["destination"]) == ("01", "15") and
                record["service"] in {"0620", "0621", "0622"}):
            grouped[(record["service"], record["request"])].append(record)
    ste_by_id = defaultdict(list)
    for record in ste["records"]:
        if record["tem_id"]:
            ste_by_id[record["tem_id"]].append(record)
    catalog = []
    for (service, request), samples in sorted(grouped.items()):
        data = bytes.fromhex(samples[0]["response"])
        ident, label, ste_indices = None, "", []
        if service == "0621":
            if {r["response"][:8] for r in samples} != {samples[0]["response"][:8]}:
                raise ValueError(f"unstable identity/type/unit for {request}")
            if tem_id(samples[0]["response"]) == "31-127":
                name = f"NichtVorhanden_{request.upper()}"
                model, encoding = "Roh10", "FF1F: in dieser Sitzung nicht vorhanden"
            else:
                ident = tem_id(samples[0]["response"])
                group, parameter = map(int, ident.split("-"))
                name = f"P{group:02d}_{parameter:03d}_{request.upper()}"
                model, encoding = value_model(ident, data)
                matches = ste_by_id.get(ident, [])
                # The request's page gives two explicitly distinguishable WE contexts.
                if request.startswith("a9"):
                    matches = [r for r in matches if r["group_text"].startswith("Einstellebene 9,")]
                elif request.startswith("aa"):
                    matches = [r for r in matches if r["group_text"].startswith("Einstellebene 10,")]
                label = " / ".join(dict.fromkeys(r["name"] for r in matches))
                ste_indices = [r["index"] for r in matches]
        elif service == "0620":
            name, model = f"Menueblock_{request.upper()}", "Roh8"
            encoding = "8 Byte Menue-/Strukturmetadaten roh"
        elif service == "0622":
            name, model = f"Liste_{request.upper()}", f"Roh{len(data)}"
            encoding = "Listenblock roh; keine Schreiboperation"
        else:
            raise ValueError(f"unhandled service {service}; do not classify it as read automatically")
        catalog.append({
            "name": name, "service": service, "request": request, "tem_id": ident,
            "label": label or (f"TEM {ident}; Bezeichnung nicht im STE-Katalog" if ident else encoding),
            "response_model": model, "encoding": encoding, "response_length": len(data),
            "sample_response": samples[0]["response"], "first_line": samples[0]["line"],
            "last_line": samples[-1]["line"], "observations": len(samples),
            "ste_name_candidates": ste_indices,
            "ste_records": matches if service == "0621" and ident else [],
        })
    return catalog


def write_model(response_model):
    """Return the 2-byte value type when the read response exposes one."""
    match = re.fullmatch(r"(?:Zahlenantwort|RohgrenzenAntwort)<(.+)>", response_model)
    return match[1] if match else None


TSP_HEADER = '''// Generated by scripts/analyze_master_log.py from CRC-checked input/complete.log.
// Evidence and limits: Master-Analysis.md and master-output/Parameter.md.
// Requests are menu/index bytes, NOT TEM IDs. TEM IDs come from the slave response.
// Source 01 was observed; no @qq forces ebusd to impersonate that master.
// 10 00 in the extended read variant is a selector, NOT a value to write.
// Write models are generated for observed numeric parameter selectors.

import "@ebusd/ebus-typespec";
using Ebus;
using Ebus.Num;
using Ebus.Str;
using Ebus.Dtm;
using Ebus.Contrib;
namespace Tem;

model Antwortkopf {
  /** TEM-Kennung aus der Antwort, inklusive korrekter Slave-Dekodierung. */
  parameter: TEM_P;
  typ: U1L;
  einheit: U1L;
}

@maxLength(1) scalar Roh1 extends HEX;
@maxLength(2) scalar Roh2 extends HEX;
@maxLength(4) scalar Roh4 extends HEX;
@maxLength(6) scalar Roh6 extends HEX;
@maxLength(8) scalar Roh8 extends HEX;
@maxLength(10) scalar Roh10 extends HEX;

@unit("°C") @divisor(10) scalar Celsius10 extends SIN;
@unit("K") @divisor(10) scalar Kelvin10 extends SIN;
@unit("%") @divisor(10) scalar Prozent10 extends SIN;
@unit("h") @divisor(10) scalar Stunden10 extends SIN;
@unit("min") @divisor(10) scalar Minuten10 extends SIN;
@unit("s") @divisor(10) scalar Sekunden10 extends SIN;
@unit("kW") @divisor(10) scalar Kilowatt10 extends SIN;
/** Aus Log-Grenze 500 und STE-Grenze 5 abgeleitete Skalierung. */
@divisor(100) scalar Steilheit100 extends SIN;
/** Minuten innerhalb einer Woche; nicht als 24-Stunden-Uhrzeit dekodieren. */
@unit("min") scalar Wochenminuten extends UIN;

enum Values_Schalter { Aus: 0, Ein: 1 }
@values(Values_Schalter) scalar Schalter extends UIN;

model ByteMitVorzeichen {
  wert: SCH;
  padding: Roh1;
}

model Zahlenantwort<T> {
  kopf: Antwortkopf;
  maximum: T;
  minimum: T;
  wert: T;
}

model RohgrenzenAntwort<T> {
  kopf: Antwortkopf;
  /** Je nach Typ Grenzen, Masken oder andere Metadaten; unveraendert. */
  grenzen_roh: Roh4;
  wert: T;
}

model Sonderantwort {
  kopf: Antwortkopf;
  nutzdaten_roh: Roh6;
}

model Kurzantwort {
  kopf: Antwortkopf;
  metadaten_roh: Roh2;
}

// Circuit "15" differs from filename "controller", keeping the CSV circuit explicit.
@zz(0x15)
namespace _15 {
'''


def render_tsp(catalog):
    result = [TSP_HEADER]
    for entry in catalog:
        service = bytes.fromhex(entry["service"])
        request = bytes.fromhex(entry["request"])
        details = []
        for ste_record in entry.get("ste_records", []):
            details.append(
                f"STE {ste_record['index']}: {ste_record['group_text']} "
                f"Grenzen {ste_record['minimum']}..{ste_record['maximum']}, "
                f"gespeichert {ste_record['stored_value']}. {ste_record['help_text']}"
            )
        comment = (f"{entry['tem_id'] or entry['service']}: {entry['label']}. "
                   f"master.log:{entry['first_line']}; {entry['observations']} gueltige Antworten. "
                   f"{entry['encoding']}. " + " ".join(details)).replace("*/", "* /").replace("\r", " ").replace("\n", " ")
        result += [f"  /** {comment} */",
                   "  @id(" + ", ".join(f"0x{b:02x}" for b in service + request) + ")",
                   f"  model {entry['name']} {{",
                   f"    antwort: {entry['response_model']};", "  }", ""]
        value_type = write_model(entry["response_model"])
        if entry["service"] == "0621" and value_type:
            result += [f"  /** {comment} Schreibwert; derselbe Selektor wird als 06 23 an 10 verwendet. */",
                       "  @write",
                       "  @zz(0x10)",
                       "  @id(0x06, 0x23, " + ", ".join(f"0x{b:02x}" for b in request) + ")",
                       f"  model {entry['name']}_set {{",
                       f"    wert: {value_type};", "  }", ""]
    result.append("}\n")
    return "\n".join(result)


def write_report(source, records, errors, catalog, ste, output):
    output.mkdir(parents=True, exist_ok=True)
    ids = {r["tem_id"] for r in catalog if r["tem_id"]}
    ste_ids = {r["tem_id"] for r in ste["records"] if r["tem_id"]}
    summary = {
        "source": source.name, "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "valid_complete": sum(r["status"] == "complete" for r in records),
        "request_only": sum(r["status"] == "request_only" for r in records),
        "errors": errors, "unique_requests": len(catalog), "unique_tem_ids": len(ids),
        "ste_ids_observed": sorted(ids & ste_ids), "ste_ids_not_observed": sorted(ste_ids - ids),
        "write_requests_observed": 0, "requests": catalog,
    }
    (output / "requests.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    columns = ["name", "service", "request", "tem_id", "label", "response_model", "encoding",
               "response_length", "first_line", "last_line", "observations", "sample_response"]
    with (output / "requests.tsv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(catalog)
    lines = ["# Zugriffe aus input/complete.log", "",
             "Generiert durch `scripts/analyze_master_log.py`. Die Namen entsprechen "
             "[controller.tsp](../controller.tsp), Circuit `15`.", "",
             "Alle Anfragen sind im Mitschnitt beobachtet und CRC-geprüft. "
             "TEM-Kennungen stammen aus den Antworten. Bezeichnungen stammen, soweit "
             "vorhanden, aus dem STE-Katalog; dessen Werte und Auswahltexte werden nicht übernommen.", "",
             "Der Suffix im Modellnamen ist die vollständige Anfrage in Hex. "
             "Verschiedene Zugriffe auf dieselbe TEM-Kennung bleiben getrennt. "
             "Die zusätzliche Instanz mit `10 00` wird nicht ohne Nachweis als HK 2 bezeichnet.", "",
             "| Modell | TEM | Bezeichnung | Service / Anfrage | Antworttyp | Erste Logzeile | Anzahl |",
             "|---|---|---|---|---|---:|---:|"]
    for r in sorted(catalog, key=lambda r: (r["tem_id"] or "99-999", r["name"])):
        values = [f"`{r['name']}`", r["tem_id"] or "—", r["label"],
                  f"`{r['service']} / {r['request']}`", f"`{r['response_model']}`",
                  r["first_line"], r["observations"]]
        lines.append("| " + " | ".join(str(v).replace("|", "&#124;") for v in values) + " |")
    lines += ["", "## STE-Kennungen ohne beobachtete Antwort", "",
              ", ".join(f"`{ident}`" for ident in sorted(ste_ids - ids)), "",
              "Diese Kennungen erhalten keine geratenen Anfragen. Das Fehlen in diesem "
              "Mitschnitt belegt nicht, dass der Regler sie nicht unterstützt.", ""]
    (output / "Parameter.md").write_text("\n".join(lines), encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, nargs="?", default=ROOT / "input/complete.log")
    parser.add_argument("--ste", type=Path, default=ROOT / "ste-output/parameter.json")
    parser.add_argument("--controller", type=Path, default=ROOT / "controller.tsp")
    parser.add_argument("--output", type=Path, default=ROOT / "master-output")
    args = parser.parse_args()
    records, errors = read_log(args.source)
    ste = json.loads(args.ste.read_text(encoding="utf-8"))
    catalog = build_catalog(records, ste)
    args.controller.write_text(render_tsp(catalog), encoding="utf-8")
    summary = write_report(args.source, records, errors, catalog, ste, args.output)
    print(json.dumps({k: v for k, v in summary.items() if k not in
                      ("requests", "ste_ids_observed", "ste_ids_not_observed")}, indent=2))


if __name__ == "__main__":
    main()
