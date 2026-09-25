#!/usr/bin/env python3
"""TEM-Livewerte nach Parameter-Code, aus einer Textdatei oder einzelnen Menüs lesen."""

import argparse
import hashlib
from collections import defaultdict
from datetime import date, timedelta
import json
import math
from pathlib import Path
import re
import shutil
import sys
import time

from analyze_master_log import ROOT, input_names, tem_id, value_model
from discover_parameters import Reader, context_bytes, discover, hex_byte


UNITS = {0: "", 2: "°C", 4: "K", 8: "%", 10: "h", 12: "min",
         14: "s", 16: "kW"}


def display_context(menu, context):
    """Interpret the observed menu groups; HK labels remain inferred."""
    if 0x63 <= menu <= 0x72:
        menu += 0x40
    if context != "base":
        if context == "1000" and menu in HK_MENUS:
            return "HK2"
        return f"Unbekannt ({context})"
    if menu == 0xa9:
        return "WP"
    if menu == 0xaa:
        return "EH"
    if 0xab <= menu <= 0xb2:
        return f"WE{menu - 0xab + 1}"
    if menu in HK_MENUS:
        return "HK1"
    if menu in (0x00, 0x02, 0x0a, 0x0d, 0x0e, 0x10, 0xa4, 0xa5, 0xa6, 0xa8):
        return "Global"
    return f"Menü {menu:02x}"


# Menus with observed base/1000 contexts in commands.txt; lower aliases above.
HK_MENUS = {0x01, 0x03, 0x08, 0x09, 0x0b, 0x0c, 0x0f, 0x21, 0x23, 0xa3, 0xa7}


class Descriptions:
    def __init__(self):
        self.names = input_names()
        self.ste = defaultdict(list)
        archive = json.loads((ROOT / "ste-output/parameter.json").read_text(encoding="utf-8"))
        for record in archive["records"]:
            self.ste[record["tem_id"]].append(record)

    def lookup(self, ident, menu):
        candidates = self.names.get(ident, [])
        # The lower menu aliases refer to the same WE groups.
        if 0x6b <= menu <= 0x72:
            menu += 0x40
        if 0xab <= menu <= 0xb2:
            level = str(menu - 0xab + 11)
            candidates = [c for c in candidates if c[2] in (None, level)]
        if ident == "04-43":
            return "Expert-Modus"
        if candidates:
            return " / ".join(dict.fromkeys(c[0] for c in candidates))
        names = list(dict.fromkeys(r["name"] for r in self.ste[ident] if r["name"]))
        return " / ".join(names) or "Beschreibung unbekannt"


    def assignment(self, ident, context):
        """Use table columns, not TEM group numbers, to identify Soll/Ist."""
        candidates = [c for c in self.names.get(ident, []) if c[1] == "soll_und_istwerte.md"]
        if re.fullmatch(r"WE[1-8]", context):
            candidates = [c for c in candidates if c[2] == str(int(context[2:]) + 10)]
        if context in ("HK1", "HK2"):
            # Only the explicitly numbered room/flow-temperature pairs distinguish HKs.
            candidates = [c for c in candidates if not (
                (match := re.match(r"(?:Raumtemperatur|Vorlauftemperatur)\s*([12])\b", c[0]))
                and match[1] != context[-1])]
        roles = list(dict.fromkeys(re.search(r"\((Soll|Ist);", c[0])[1] for c in candidates))
        labels = " / ".join(dict.fromkeys(c[0] for c in candidates))
        return "/".join(roles) or "—", labels


def parameter_catalog(before, contexts):
    """Select one established selector per TEM/context, with no invented accesses."""
    archive = json.loads((ROOT / "master-output/requests.json").read_text())
    if archive["scan_sha256"] != hashlib.sha256((ROOT / "commands.txt").read_bytes()).hexdigest():
        raise ValueError("Parameterkatalog veraltet; zuerst python3 scripts/analyze_master_log.py ausführen")
    if any(context != b"\x10\x00" for context in contexts):
        raise ValueError("Der Parameterkatalog kennt nur Zusatzkontext 1000; andere Kontexte mit --menu lesen")
    entries = []
    for entry in archive["requests"]:
        if entry["service"] != "0621" or not entry["tem_id"]:
            continue
        group = int(entry["tem_id"].split("-")[0])
        if before is not None and (group < 3) != before:
            continue
        selector = bytes.fromhex(entry["request"])
        if len(selector) == 4 and selector[2:] not in contexts:
            continue
        entries.append(entry)
    return sorted(entries, key=lambda e: (tuple(map(int, e["tem_id"].split("-"))),
                                          e["context"], e["request"]))


def parameter_collection(path, entries):
    """Resolve a complete UTF-8 collection before making any bus accesses."""
    catalog = defaultdict(list)
    for entry in entries:
        catalog[entry["tem_id"]].append(entry)
    selected, seen = [], set()
    for number, line in enumerate(Path(path).read_text(encoding="utf-8-sig").splitlines(), 1):
        line = line.partition("#")[0].strip()
        if not line:
            continue
        fields = line.split(maxsplit=1)
        if not re.fullmatch(r"[0-9]{1,2}-[0-9]{1,3}", fields[0]):
            raise ValueError(f"{path}:{number}: erwartet TEM-Code [Kontext], z.B. 03-00 HK1")
        group, index = map(int, fields[0].split("-"))
        if group > 31 or index > 127:
            raise ValueError(f"{path}:{number}: TEM-Code außerhalb von 00-00 bis 31-127")
        ident = f"{group:02d}-{index:02d}"
        matches = catalog.get(ident, [])
        if len(fields) == 2:
            context = " ".join(fields[1].split()).casefold()
            matches = [entry for entry in matches if entry["context"].casefold() == context]
        if not matches:
            raise ValueError(f"{path}:{number}: kein bekannter Zugriff für {line!r} "
                             "mit den gewählten Kontextoptionen")
        for entry in matches:
            key = (entry["tem_id"], entry["context"])
            if key not in seen:
                selected.append(entry)
                seen.add(key)
    if not selected:
        raise ValueError(f"{path}: Parametersammlung ist leer")
    return selected


def read_parameters(reader, entries, descriptions, before, raw):
    """Read in the supplied order and stream results, retaining unavailable/error rows."""
    counts = {"accessible": 0, "unavailable": 0, "errors": 0}
    print("TEM    Kontext  Art   Beschreibung | Aktueller Wert" if before else
          "TEM    Kontext  Beschreibung | Aktueller Wert", flush=True)
    refreshed = None
    for entry in entries:
        if refreshed is None or time.monotonic() - refreshed >= 60:
            # The captured operating panel renews expert access about once a minute.
            reader.enable_expert()
            refreshed = time.monotonic()
        ident, context = entry["tem_id"], entry["context"]
        selector = bytes.fromhex(entry["request"])
        role, label = descriptions.assignment(ident, context) if before else ("", "")
        label = " ".join((label or descriptions.lookup(ident, selector[0])).split())
        response = None
        try:
            response = reader.read("0621", selector)
            if len(response) < 2:
                raise ValueError("fehlende TEM-Kennung")
            if response[:2] == b"\xff\x1f":
                value = "nicht verfügbar (ff1f)"
                counts["unavailable"] += 1
            else:
                if len(response) < 4:
                    raise ValueError("fehlender Typ-/Einheitenkopf")
                if tem_id(response.hex()) != ident:
                    raise ValueError(f"erwartet {ident}, Antwort enthält {tem_id(response.hex())}")
                value = display_value(ident, response)
                counts["accessible"] += 1
        except ValueError as exc:
            value = f"Fehler: {exc}"
            counts["errors"] += 1
            print(f"{ident}/{context}: {exc}", file=sys.stderr)
        prefix = f"{ident:<6} {context:<7} "
        if before:
            prefix += f"{role:<5} "
        print(f"{prefix}{label} | {value}", flush=True)
        if raw and response is not None:
            print(f"    Antwort: {response.hex()}", flush=True)
    return counts


def display_value(ident, data):
    """Use the same encoding decisions as controller.tsp; preserve special replies."""
    if len(data) not in (6, 10):
        return f"Unbekanntes Antwortformat; roh: {data.hex(' ')}"
    model, _ = value_model(ident, data)
    if model in ("Kurzantwort", "Sonderantwort"):
        return f"Sonderformat; roh: {data.hex(' ')}"
    raw = data[8:10]
    unit = UNITS.get(data[3], f"[Einheit 0x{data[3]:02x}]")
    if model.startswith("Zahlenantwort"):
        value = int.from_bytes(raw, "little", signed=True)
        if value == -32768:
            return "nicht verfügbar"
        if "Steilheit100" in model:
            return f"{value / 100:g}"
        if "Faktor10" in model:
            return f"{value / 10:g}"
        return f"{value / 10:g} {unit}".strip()
    if "ByteMitVorzeichen" in model:
        value = int.from_bytes(raw[:1], "little", signed=True)
        if value == -128:
            return "nicht verfügbar"
    else:
        value = int.from_bytes(raw, "little")
        if value == 65535:
            return "nicht verfügbar"
    if "<DAY>" in model:
        return (date(1900, 1, 1) + timedelta(days=value)).isoformat()
    if "Wochenminuten" in model:
        return f"{value} min (Wochenminuten)"
    if "Schalter" in model:
        return {0: "Aus (0)", 1: "Ein (1)"}.get(value, str(value))
    return f"{value} {unit}".strip()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("block", nargs="?", type=hex_byte,
                        help="Verzeichnisblock in Hex, z.B. 14 für Menüs a0..a7")
    parser.add_argument("--menu", type=hex_byte,
                        help="statt eines ganzen Blocks nur dieses Menü lesen, z.B. a7")
    parser.add_argument("--server", default="localhost")
    parser.add_argument("--port", type=int, default=8888)
    parser.add_argument("--destination", type=hex_byte, default=0x15,
                        help="Leseziel in Hex (Standard: 15)")
    parser.add_argument("--expert-destination", type=hex_byte, default=0x10,
                        help="Ziel der Expert-Freischaltung in Hex (Standard: 10)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--base-only", action="store_true", help="nur Grundkontext lesen")
    group.add_argument("--context", type=context_bytes, action="append",
                       help="Zusatzkontext in Hex; wiederholbar (Standard: 1000)")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--from-03-00", action="store_true",
                       help="alle bekannten Parameter ab 03-00 sortiert lesen; mit Menüangabe: Anzeigefilter")
    modes.add_argument("--before-03-00", action="store_true",
                       help="alle bekannten Werte 00..02 mit Soll/Ist sortiert lesen; mit Menüangabe: Anzeigefilter")
    modes.add_argument("--parameters-file", type=Path, metavar="DATEI",
                       help="Parametersammlung lesen: pro Zeile TEM-Code [Kontext], # für Kommentare")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout in Sekunden")
    parser.add_argument("--delay", type=float, default=0.1, help="Pause zwischen Abfragen in Sekunden")
    parser.add_argument("--raw", action="store_true", help="vollständige Rohantwort zusätzlich anzeigen")
    args = parser.parse_args(argv)
    parameter_mode = args.block is None and args.menu is None
    if args.block is not None and args.menu is not None:
        parser.error("Block und --menu schließen einander aus")
    if args.parameters_file is not None and not parameter_mode:
        parser.error("--parameters-file kann nicht mit Block oder --menu kombiniert werden")
    if parameter_mode and not (args.before_03_00 or args.from_03_00 or args.parameters_file is not None):
        parser.error("Block, --menu, --before-03-00, --from-03-00 oder --parameters-file angeben")
    if args.block is not None and args.block > 0x1f:
        parser.error("Verzeichnisblock muss zwischen 00 und 1f liegen")
    if not 1 <= args.port <= 65535 or args.timeout <= 0 or not math.isfinite(args.delay) or args.delay < 0:
        parser.error("ungültiger Port, Timeout oder Abstand")
    if shutil.which("ebusctl") is None:
        parser.error("ebusctl wurde nicht im PATH gefunden")
    block = args.block
    if args.menu is not None:
        block = args.menu // 8
    contexts = [] if args.base_only else list(dict.fromkeys(args.context or [b"\x10\x00"]))
    menus = None if args.menu is None else {args.menu}

    try:
        descriptions = Descriptions()
        if not parameter_mode:
            print("Menü  Kontext  TEM    Beschreibung | Aktueller Wert", flush=True)

        displayed = 0

        def emit(row):
            nonlocal displayed
            ident = tuple(map(int, row["tem"].split("-")))
            if args.from_03_00 and ident < (3, 0):
                return
            if args.before_03_00 and ident >= (3, 0):
                return
            description = descriptions.lookup(row["tem"], int(row["menu"], 16))
            description = " ".join(description.split())
            value = display_value(row["tem"], bytes.fromhex(row["response"]))
            context = display_context(int(row["menu"], 16), row["context"])
            print(f"{row['menu']}    {context:<7}  {row['tem']}  {description} | {value}", flush=True)
            if args.raw:
                print(f"    Antwort: {row['response']}", flush=True)
            displayed += 1

        if parameter_mode:
            if args.parameters_file is not None:
                entries = parameter_collection(args.parameters_file, parameter_catalog(None, contexts))
            else:
                entries = parameter_catalog(args.before_03_00, contexts)
            print(f"Lese {len(entries)} Parameterzugriffe nach TEM-Code; Expert-Freischaltung "
                  "zu Beginn und nach jeweils 60 Sekunden.", file=sys.stderr)
            counts = read_parameters(Reader(args), entries, descriptions,
                                     args.before_03_00, args.raw)
        else:
            print(f"Lese Block {block:02x}; Expert-Freischaltung einmal vor den Parameterabfragen.",
                  file=sys.stderr)
            counts = discover(Reader(args), [block], contexts, emit,
                              lambda message: print(message, file=sys.stderr), menus=menus)
    except KeyboardInterrupt:
        print("Abgebrochen; bereits ausgegebene Werte bleiben erhalten.", file=sys.stderr)
        return 130
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        return 1
    if not parameter_mode and (args.from_03_00 or args.before_03_00):
        print(f"{displayed} angezeigt, {counts['accessible'] - displayed} ausgefiltert.", file=sys.stderr)
    print(f"{counts['accessible']} Parameter, {counts['unavailable']} unbelegte Plätze, "
          f"{counts['errors']} Fehler.", file=sys.stderr)
    return 1 if counts["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
