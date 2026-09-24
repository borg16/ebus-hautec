#!/usr/bin/env python3
"""Scan 06 21 payloads: vary the first two bytes, or the last two with --code."""

import argparse
import csv
from datetime import datetime, timezone
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time


# Values_type / Values_unit in tem/_templates.tsp.
TEM_TYPES = {
    0x00: "none", 0x02: "on_off", 0x04: "Zeit", 0x09: "selection",
    0x0d: "Temperatur", 0x40: "Dauer", 0x4d: "TemperaturSchwelle",
    0x8d: "TemperaturSoll", 0xc0: "range",
}
TEM_UNITS = {
    0x00: "none", 0x02: "_C", 0x04: "K", 0x08: "__0",
    0x0a: "h", 0x0c: "min", 0x10: "kW", 0x2a: "hh_mm",
}


def decode_header(response):
    """Decode Parameterkopf from an already validated hit (no scaling)."""
    payload = bytes.fromhex(response)[1:]

    def uch(value, names):
        if value == 0xff:  # UCH replacement
            return "-"
        return names.get(value, f"unknown(0x{value:02x})")

    def sin(data):
        value = int.from_bytes(data, "little", signed=True)
        return "-" if value == -32768 else value  # SIN replacement 0x8000

    return [uch(payload[2], TEM_TYPES), uch(payload[3], TEM_UNITS),
            sin(payload[4:6]), sin(payload[6:8])]


def hex_number(text):
    return int(text, 16)


def decode_value(response):
    """Show the trailing word; type/unit alone do not guarantee its encoding."""
    payload = bytes.fromhex(response)[1:]
    data = payload[8:10]
    unsigned = int.from_bytes(data, "little")
    signed = int.from_bytes(data, "little", signed=True)
    value = ""
    encoding = "unbekannt; Rohwerte ohne Skalierung"
    if payload[2] == 0x02:
        encoding = "UIN/on_off"
        value = {0: "Aus", 1: "Ein", 0xffff: "-"}.get(unsigned, str(unsigned))
    elif payload[2] in (0x0d, 0x4d, 0x8d) and payload[3] in (0x02, 0x04):
        # Common in controller.tsp (temp10), but ParameterTemp2 also exists.
        encoding = "Annahme: SIN / 10"
        unit = "°C" if payload[3] == 0x02 else "K"
        value = "-" if signed == -32768 else f"{signed / 10:g} {unit}"
    return [data.hex(), unsigned, signed, value, encoding]


def classify(response):
    """ebusctl hex returns NN + unescaped slave payload, without CRC."""
    compact = "".join(response.split()).lower()
    if not re.fullmatch(r"[0-9a-f]+", compact) or len(compact) % 2:
        return "invalid", "", ""
    raw = bytes.fromhex(compact)
    if len(raw) != raw[0] + 1:
        return "invalid", "", ""
    if raw[0] != 10:
        return "length", "", ""
    parameter = raw[1:3]
    if parameter == b"\xff\x1f":
        return "ff1f", parameter.hex(), ""
    # TEM_P slave representation (master encoding differs):
    # https://github.com/john30/ebusd/blob/master/src/lib/ebus/contrib/tem.cpp
    value = int.from_bytes(parameter, "little")
    code = f"{(value >> 7) & 0x1f:02d}-{value & 0x7f:03d}"
    return "hit", parameter.hex(), code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", default="localhost")
    parser.add_argument("--port", type=int, default=8888)
    parser.add_argument("--destination", type=hex_number, default=0x15,
                        help="Zieladresse in Hex (Standard: 15)")
    fixed_bytes = parser.add_mutually_exclusive_group()
    fixed_bytes.add_argument("--code", type=hex_number,
                        help="Feste erste zwei Payload-Bytes in Hex (z.B. 04ab); "
                             "start/end iterieren dann die letzten zwei Bytes")
    fixed_bytes.add_argument("--suffix", type=hex_number, default=0,
                             help="Feste letzte zwei Payload-Bytes in Hex "
                                  "(Standard: 0000); nur ohne --code")
    parser.add_argument("--start", type=hex_number, default=0,
                        help="Erste Bytekombination in Hex, inklusive (Standard: 0000)")
    parser.add_argument("--end", type=hex_number, default=0xffff,
                        help="Letzte Bytekombination in Hex, inklusive (Standard: ffff)")
    parser.add_argument("--step", type=int, default=1,
                        help="Schrittweite als positive Dezimalzahl (Standard: 1)")
    parser.add_argument("--delay", type=float, default=0.1,
                        help="Pause zwischen Anfragen in Sekunden (Standard: 0.1)")
    parser.add_argument("--timeout", type=int, default=5)
    parser.add_argument("--output", type=Path,
                        default=Path(datetime.now().strftime("scan-0621-%Y%m%d-%H%M%S")),
                        help="Neues Ausgabeverzeichnis")
    args = parser.parse_args()
    if not 0 <= args.start <= args.end <= 0xffff:
        parser.error("Erforderlich: 0000 <= start <= end <= ffff")
    if args.step <= 0:
        parser.error("step muss eine positive ganze Zahl sein")
    if args.code is not None and not 0 <= args.code <= 0xffff:
        parser.error("code muss zwischen 0000 und ffff liegen")
    if not 0 <= args.suffix <= 0xffff:
        parser.error("suffix muss zwischen 0000 und ffff liegen")
    if not 0 <= args.destination <= 255 or not 1 <= args.port <= 65535:
        parser.error("Ungültige Zieladresse oder Port")
    if args.timeout <= 0 or not math.isfinite(args.delay) or args.delay < 0:
        parser.error("timeout muss positiv und delay endlich und >= 0 sein")
    executable = shutil.which("ebusctl")
    if executable is None:
        parser.error("ebusctl wurde nicht im PATH gefunden")
    args.output.mkdir(parents=True, exist_ok=False)
    base = [executable, "-s", args.server, "-p", str(args.port),
            "-t", str(args.timeout), "-e", "hex"]
    fields = ["timestamp", "server", "destination", "request", "status",
              "parameter_bytes", "tem_code", "type", "unit", "max", "min",
              "value_bytes", "value_unsigned", "value_signed", "value", "value_encoding",
              "response", "error"]
    count = hits = errors = 0
    current = args.start
    mode = (f"Payload XXXX{args.suffix:04x}" if args.code is None
            else f"Payload {args.code:04x}XXXX")
    print(f"Scan {args.start:04x}..{args.end:04x} ({mode}), Schrittweite {args.step}, "
          f"Ziel {args.destination:02x}; "
          f"Protokolle: {args.output}", file=sys.stderr)
    with (args.output / "all.tsv").open("w", newline="", buffering=1) as all_file, \
            (args.output / "hits.tsv").open("w", newline="", buffering=1) as hit_file:
        all_log = csv.writer(all_file, delimiter="\t")
        hit_log = csv.writer(hit_file, delimiter="\t")
        all_log.writerow(fields)
        hit_log.writerow(fields)
        try:
            for current in range(args.start, args.end + 1, args.step):
                payload = (f"{current:04x}{args.suffix:04x}" if args.code is None
                           else f"{args.code:04x}{current:04x}")
                request = f"{args.destination:02x}062104{payload}"
                response = error = parameter = code = ""
                try:
                    result = subprocess.run(base + [request], capture_output=True,
                                            text=True, timeout=args.timeout + 2)
                    response, error = result.stdout.strip(), result.stderr.strip()
                    if result.returncode or response.startswith(("ERR:", "usage:")):
                        status = "error"
                        error = error or f"ebusctl exit={result.returncode}"
                    else:
                        status, parameter, code = classify(response)
                except subprocess.TimeoutExpired:
                    status, error = "error", "ebusctl timeout"
                header = decode_header(response) if status == "hit" else [""] * 4
                decoded_value = decode_value(response) if status == "hit" else [""] * 5
                row = [datetime.now(timezone.utc).isoformat(),
                       f"{args.server}:{args.port}", f"{args.destination:02x}",
                       request, status, parameter, code, *header, *decoded_value,
                       response, error]
                all_log.writerow(row)
                count += 1
                if status == "hit":
                    hits += 1
                    hit_log.writerow(row)
                    type_name, unit, maximum, minimum = header
                    raw, unsigned, signed, value, encoding = decoded_value
                    print(f"{request} -> {response}  {parameter} = {code}  "
                          f"type={type_name} unit={unit} max={maximum} min={minimum}  "
                          f"value={value or 'unbekannt'} ({encoding}; "
                          f"raw={raw} unsigned={unsigned} signed={signed})",
                          flush=True)
                if status in ("error", "invalid"):
                    errors += 1
                    if errors <= 5:
                        print(f"{request}: {error or response}", file=sys.stderr)
                if count % 256 == 0:
                    print(f"Bis {current:04x}: {count} Anfragen, {hits} Treffer, "
                          f"{errors} Fehler", file=sys.stderr)
                if current + args.step <= args.end:
                    time.sleep(args.delay)
        except KeyboardInterrupt:
            fixed_code = (f"--suffix {args.suffix:04x} " if args.code is None
                          else f"--code {args.code:04x} ")
            print(f"\nAbgebrochen; zum sicheren Fortsetzen {fixed_code}"
                  f"--start {current:04x} --end {args.end:04x} --step {args.step} "
                  "mit neuem Ausgabeverzeichnis verwenden.", file=sys.stderr)
            return 130
        finally:
            print(f"{count} Anfragen, {hits} Treffer, {errors} Fehler", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
