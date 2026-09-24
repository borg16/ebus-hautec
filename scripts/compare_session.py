#!/usr/bin/env python3
"""Compare the last CRC-valid session observations with the STE parameter table.

No bus access. The mapping of the two request contexts to STE HK 1/2 is
explicitly an inference. Later, known FB fields are kept as separate evidence.
"""

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from analyze_master_log import ROOT, crc, parse_line, tem_id, unescape


UNITS = {0: "", 2: "°C", 4: "K", 8: "%", 10: "h", 12: "min", 14: "s", 16: "kW", 34: "Passwortanzeige"}
# Offsets refer to bytes after the two-byte block header. Only selected,
# understood fields are used, not the unknown remainder of each FB block.
FB_FIELDS = {
    0x3001: [("03-51", 0, 10), ("03-53", 2, 10), ("05-51", 4, 10)],
    0x3101: [("03-58", 0, 10), ("03-43", 2, 10), ("03-35", 6, 10)],
    0x3002: [("03-10", 0, 100), ("03-01", 8, 10)],
    0x3003: [("03-21", 2, 10), ("03-02", 4, 10)],
    0x3103: [("03-00", 0, 10)],
}


def verify_markdown(records, text):
    """Ensure the machine-readable baseline still matches the user's table."""
    values = {}
    for line in text.splitlines():
        if not line.startswith("| "):
            continue
        cells = [s.strip() for s in line.strip("|").split("|")]
        if len(cells) == 8 and (m := re.fullmatch(r"\[(\d+)\]\(#datensatz-\d+\)", cells[7])):
            values[int(m[1])] = float(cells[3])
    if values != {r["index"]: r["stored_value"] for r in records}:
        raise ValueError("Parameter.md differs from parameter.json; reconcile the baseline first")


def select_baseline(ident, request, by_id):
    candidates = by_id.get(ident, [])
    if not candidates:
        return None
    page = int(request[:2], 16)
    if page in (0xA9, 0xAA, 0xAB):
        level = {0xA9: 9, 0xAA: 10, 0xAB: 11}[page]
        candidates = [r for r in candidates if r["group_text"].startswith(f"Einstellebene {level},")]
    elif candidates[0]["variant_flag_raw"] == 1:
        if len(request) == 4:
            variant = 0
        elif len(request) == 8 and request.endswith("1000"):
            variant = 1
        else:
            raise ValueError(f"Unmapped request context: {request}")
        candidates = [r for r in candidates if r["variant_index"] == variant]
    if len(candidates) != 1:
        raise ValueError(f"Ambiguous baseline for {ident}/{request}")
    return candidates[0]


def decode_value(ident, data):
    typ, unit = data[2:4]
    if typ in (0x0D, 0x4D, 0x8D):
        value = int.from_bytes(data[8:10], "little", signed=True)
        return (None if value == -32768 else value / 10), UNITS[unit]
    value = int.from_bytes(data[8:10], "little")
    if ident == "03-10":
        return value / 100, ""
    if typ not in (0, 2, 4, 9):
        raise ValueError(f"Unsupported setting type: {ident}/{typ}")
    return (None if value == 65535 else value), UNITS[unit]


def compare(log_path, baseline):
    by_id = defaultdict(list)
    by_index = {r["index"]: r for r in baseline}
    for record in baseline:
        if record["tem_id"]:
            by_id[record["tem_id"]].append(record)
    direct, blocks, writes, invalid = {}, {}, [], []
    lines = log_path.read_text().splitlines()
    for number, line in enumerate(lines, 1):
        if "<01100623" in line:
            data = unescape(bytes.fromhex(line.split("<")[1]))
            end = 5 + data[4]
            if len(data) > end and crc(data[:end]) == data[end] and data[end + 1:] == b"\x00":
                writes.append({"line": number, "time": line[:23], "request": data[5:end - 2].hex(),
                               "value_hex": data[end - 2:end].hex()})
        if not any(prefix in line for prefix in ("<01150621", "<1090100a", "<1091100a")):
            continue
        try:
            parsed = parse_line(line, number)
        except ValueError as exc:
            invalid.append({"line": number, "error": str(exc)})
            continue
        if parsed["status"] != "complete":
            continue
        request = bytes.fromhex(parsed["request"])
        response = bytes.fromhex(parsed["response"])
        if parsed["service"] == "0621":
            ident = tem_id(parsed["response"])
            if len(response) != 10 or ident not in by_id:
                continue
            reference = select_baseline(ident, parsed["request"], by_id)
            value, unit = decode_value(ident, response)
            direct[parsed["request"]] = {
                "ste_index": reference["index"], "source": "Master", "selector": parsed["request"],
                "line": number, "time": parsed["time"], "value": value, "unit": unit,
                "value_hex": response[8:10].hex(), "payload": parsed["response"],
            }
        elif parsed["service"] == "100a":
            data = response if request[0] in (0x20, 0x21) else request
            if len(data) != 14:
                continue
            code = int.from_bytes(data[:2], "big")
            # FB 1: 01/02/03; FB 2: 0b/0c/0d. Do not use FB 2's extra mirror of 01.
            if parsed["destination"] == "91":
                if data[1] not in (0x0B, 0x0C, 0x0D):
                    continue
                code -= 10
            if code in FB_FIELDS:
                blocks[parsed["destination"], code] = (parsed, data)

    observations = list(direct.values())
    # A later acknowledged write must never silently be replaced with an earlier read.
    pending = [w for w in writes if w["request"] in direct and w["line"] > direct[w["request"]]["line"]]
    if pending:
        raise ValueError(f"Settings written after their final read: {pending}")
    for (destination, code), (parsed, data) in blocks.items():
        variant = int(destination == "91")
        for ident, offset, divisor in FB_FIELDS[code]:
            reference = next(r for r in by_id[ident] if r["variant_index"] == variant)
            raw = data[2 + offset:4 + offset]
            integer = int.from_bytes(raw, "little", signed=True)
            value = None if integer == -32768 else integer / divisor
            observations.append({
                "ste_index": reference["index"], "source": f"FB {destination}", "selector": data[:2].hex(),
                "line": parsed["line"], "time": parsed["time"], "value": value,
                "unit": "" if ident == "03-10" else "K" if ident in ("03-35", "03-58") else "°C",
                "value_hex": raw.hex(), "payload": data.hex(),
            })

    grouped = defaultdict(list)
    for observation in observations:
        grouped[observation["ste_index"]].append(observation)
    results = []
    for index, evidence in sorted(grouped.items()):
        reference = by_index[index]
        evidence.sort(key=lambda e: e["line"])
        latest = evidence[-1]
        status = "gleich" if latest["value"] == reference["stored_value"] else "abweichend"
        if reference["tem_id"] == "04-40":
            status = "Passwortanzeige; nicht als geaendertes Passwort bewiesen"
        if latest["value"] is None:
            status = "Ersatzwert; nicht vergleichbar"
        results.append({"ste_index": index, "tem_id": reference["tem_id"], "name": reference["name"],
                        "context": reference["context"], "baseline": reference["stored_value"],
                        "baseline_unit": reference["unit_inferred"], "latest": latest,
                        "status": status, "evidence": evidence})
    return {"log_end": lines[-1][:23], "invalid": invalid,
            "direct_request_count": len(direct), "fb_block_count": len(blocks),
            "status_counts": dict(Counter(r["status"] for r in results)),
            "results": results,
            "unobserved_ste_indices": sorted(set(by_index) - set(grouped))}


def fmt(value):
    if value is None:
        return "—"
    return f"{value:g}".replace(".", ",")


def write_outputs(report, output):
    output.mkdir(exist_ok=True)
    (output / "comparison.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    with (output / "comparison.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        fields = ["tem_id", "context", "name", "baseline", "latest_value", "unit", "status",
                  "source", "selector", "time", "log_line", "ste_index"]
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=";")
        writer.writeheader()
        for r in sorted(report["results"], key=lambda r: (r["tem_id"], r["ste_index"])):
            last = r["latest"]
            writer.writerow({"tem_id": r["tem_id"], "context": r["context"], "name": r["name"],
                             "baseline": fmt(r["baseline"]), "latest_value": fmt(last["value"]),
                             "unit": last["unit"], "status": r["status"], "source": last["source"],
                             "selector": last["selector"], "time": last["time"], "log_line": last["line"],
                             "ste_index": r["ste_index"]})
    lines = ["# Einzelbelege zum Vergleich", "",
             "Basis: [ste-output/Parameter.md](../ste-output/Parameter.md). "
             "Einordnung und Unsicherheiten: [Session-Comparison.md](../Session-Comparison.md).", "",
             "HK 1/2 sind die abgeleiteten Zuordnungen zu den STE-Varianten. "
             "Alle zuletzt vorhandenen Quellen werden einzeln gezeigt; unterschiedliche "
             "Zeitpunkte und widersprüchliche Werte bleiben sichtbar.", "",
             "| TEM | STE-Nr. | Bezeichnung / Kontext | STE | Quelle / Anfrage | Letzter Wert | Zeitpunkt | Logzeile |",
             "|---|---:|---|---:|---|---:|---|---:|"]
    for r in sorted(report["results"], key=lambda r: (r["tem_id"], r["ste_index"])):
        for e in r["evidence"]:
            lines.append(f"| {r['tem_id']} | {r['ste_index']} | {r['name']} / {r['context']} | "
                         f"{fmt(r['baseline'])} {r['baseline_unit']} | {e['source']} `{e['selector']}` | "
                         f"{fmt(e['value'])} {e['unit']} | {e['time'][11:]} | {e['line']} |")
    (output / "Evidence.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    baseline = json.loads((ROOT / "ste-output/parameter.json").read_text())["records"]
    verify_markdown(baseline, (ROOT / "ste-output/Parameter.md").read_text())
    report = compare(ROOT / "complete.log", baseline)
    write_outputs(report, ROOT / "comparison-output")
    print(json.dumps({k: v for k, v in report.items() if k not in ("results", "unobserved_ste_indices")}, indent=2))
