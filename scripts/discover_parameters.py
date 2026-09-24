#!/usr/bin/env python3
"""Discover TEM parameters, enabling expert mode once per directory block."""

import argparse
import csv
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time


def hex_byte(text):
    value = int(text, 16)
    if not 0 <= value <= 255:
        raise argparse.ArgumentTypeError("expected a hexadecimal byte")
    return value


def context_bytes(text):
    if not re.fullmatch(r"[0-9a-fA-F]{4}", text):
        raise argparse.ArgumentTypeError("expected two bytes, e.g. 1000")
    return bytes.fromhex(text)


def parse_response(text):
    """ebusctl hex returns NN followed by unescaped slave data, no CRC."""
    compact = "".join(text.split())
    if not re.fullmatch(r"(?:[0-9a-fA-F]{2})+", compact):
        raise ValueError(f"not a hex response: {text.strip()}")
    data = bytes.fromhex(compact)
    if len(data) != data[0] + 1:
        raise ValueError("slave response length mismatch")
    return data[1:]


class Reader:
    def __init__(self, args):
        self.args = args
        self.base = ["ebusctl", "-s", args.server, "-p", str(args.port),
                     "-t", str(args.timeout), "-e", "hex"]

    def command(self, service, selector):
        if service not in ("0620", "0621"):
            raise ValueError("discovery only supports read services 0620 and 0621")
        telegram = bytes([self.args.destination]) + bytes.fromhex(service)
        telegram += bytes([len(selector)]) + selector
        return self.base + [telegram.hex()]

    def read(self, service, selector):
        return parse_response(self.execute(self.command(service, selector)))

    def enable_expert(self):
        # Master-directed write: ebusd reports 'done', not a slave payload.
        result = self.execute(self.base + [f"{self.args.expert_destination:02x}06230400005100"])
        if result.strip().lower() != "done":
            raise ValueError(f"unexpected expert-enable response: {result!r}")

    def execute(self, command):
        try:
            result = subprocess.run(command, text=True,
                                    capture_output=True, timeout=self.args.timeout + 2)
            if "not enabled" in (result.stdout + result.stderr).lower():
                raise RuntimeError("ebusd hex command is disabled. Start ebusd with --enablehex "
                                   "and restart this script; no scan was completed.")
            if result.returncode or result.stdout.strip().startswith("ERR:"):
                raise ValueError(result.stderr.strip() or result.stdout.strip()
                                 or f"ebusctl exited with {result.returncode}")
            return result.stdout
        except subprocess.TimeoutExpired as exc:
            raise ValueError("ebusctl timeout") from exc
        finally:
            time.sleep(self.args.delay)


def discover(reader, blocks, contexts, emit, error):
    """Keep each selector separately, including duplicate TEM identifiers."""
    counts = {"accessible": 0, "unavailable": 0, "errors": 0}
    for block in blocks:
        try:
            directory = reader.read("0620", bytes([block]))
            if len(directory) != 8:
                raise ValueError(f"directory has {len(directory)} bytes, expected 8")
        except ValueError as exc:
            counts["errors"] += 1
            error(f"directory {block:02x}: {exc}")
            continue
        try:
            reader.enable_expert()
        except ValueError as exc:
            counts["errors"] += 1
            error(f"expert mode for block {block:02x}: {exc}; skipping parameters")
            continue
        for position, descriptor in enumerate(directory):
            menu = block * 8 + position
            variants = [None] + (contexts if descriptor & 128 else [])
            for context in variants:
                for index in range(descriptor & 127):
                    selector = bytes([menu, index]) if context is None else (
                        bytes([menu, index | 128]) + context)
                    try:
                        response = reader.read("0621", selector)
                        if len(response) < 2:
                            raise ValueError("missing TEM identifier")
                        if response[:2] == b"\xff\x1f":
                            counts["unavailable"] += 1
                            continue
                        if len(response) < 4:
                            raise ValueError("missing type/unit header")
                        word = int.from_bytes(response[:2], "little")
                        ident = f"{(word >> 7) & 31:02d}-{word & 127:02d}"
                        emit({"tem": ident, "menu": f"{menu:02x}", "index": f"{index:02x}",
                              "context": "base" if context is None else context.hex(),
                              "selector": selector.hex(), "type": f"{response[2]:02x}",
                              "unit": f"{response[3]:02x}", "response": response.hex()})
                        counts["accessible"] += 1
                    except ValueError as exc:
                        counts["errors"] += 1
                        error(f"selector {selector.hex()}: {exc}")
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", default="localhost")
    parser.add_argument("--port", type=int, default=8888)
    parser.add_argument("--destination", type=hex_byte, default=0x15, help="hex address (default: 15)")
    parser.add_argument("--expert-destination", type=hex_byte, default=0x10,
                        help="expert-mode write target in hex (default: 10)")
    parser.add_argument("--first-block", type=hex_byte, default=0, help="hex, inclusive (default: 00)")
    parser.add_argument("--last-block", type=hex_byte, default=0x1b, help="hex, inclusive (default: 1b)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--base-only", action="store_true", help="skip extended contexts")
    group.add_argument("--context", type=context_bytes, action="append",
                       help="extended selector bytes; repeatable (default: observed 1000)")
    parser.add_argument("--timeout", type=int, default=5)
    parser.add_argument("--delay", type=float, default=0.1, help="seconds between reads")
    parser.add_argument("--format", choices=("tsv", "jsonl"), default="tsv")
    args = parser.parse_args(argv)
    if not 0 <= args.first_block <= args.last_block <= 0x1f:
        parser.error("require 00 <= first-block <= last-block <= 1f")
    if not 1 <= args.port <= 65535 or args.timeout <= 0 or not math.isfinite(args.delay) or args.delay < 0:
        parser.error("invalid port, timeout or delay")
    if shutil.which("ebusctl") is None:
        parser.error("ebusctl is not installed or not on PATH")
    contexts = [] if args.base_only else list(dict.fromkeys(args.context or [b"\x10\x00"]))
    fields = ["tem", "menu", "index", "context", "selector", "type", "unit", "response"]
    writer = csv.DictWriter(sys.stdout, fields, delimiter="\t", lineterminator="\n")
    if args.format == "tsv":
        writer.writeheader()

    def emit(row):
        if args.format == "tsv":
            writer.writerow(row)
        else:
            print(json.dumps(row))
        sys.stdout.flush()

    print("Reading menu directory; enabling expert mode once per block before parameter reads.",
          file=sys.stderr)
    try:
        counts = discover(Reader(args), range(args.first_block, args.last_block + 1), contexts,
                          emit, lambda message: print(message, file=sys.stderr))
    except KeyboardInterrupt:
        print("Interrupted; already printed results remain usable.", file=sys.stderr)
        return 130
    except (OSError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(", ".join(f"{key}={value}" for key, value in counts.items()), file=sys.stderr)
    return 1 if counts["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
