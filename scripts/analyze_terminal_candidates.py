#!/usr/bin/env python3
"""Compare terminal-state candidates offline; never contacts the controller."""
import bisect
import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from analyze_master_log import crc, unescape
from analyze_status_frequency import LINE

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "heating-output"


def read_log(path):
    groups = defaultdict(list)
    errors = Counter()
    raw = path.read_bytes()
    for number, line in enumerate(raw.lstrip(b"\0").decode().splitlines(), 1):
        match = LINE.fullmatch(line)
        try:
            if not match:
                raise ValueError("line format")
            data = unescape(bytes.fromhex(match[2].replace("<", "").replace(">", "")))
            if len(data) < 6:
                raise ValueError("short header")
            end = 5 + data[4]
            if len(data) <= end or crc(data[:end]) != data[end]:
                raise ValueError("incomplete master or invalid CRC")
        except ValueError as error:
            errors[str(error)] += 1
            continue
        payload = data[5:end]
        key = data[:4].hex()
        value = None
        if key == "10fe100a":
            key += "_" + payload[:2].hex()
        elif data[1:4] == bytes.fromhex("150621") and payload == bytes.fromhex("21811000"):
            tail = data[end + 1:]
            if not (len(tail) >= 4 and tail[0] == 0 and len(tail) == tail[1] + 4
                    and tail[-1] == 0 and crc(tail[1:-2]) == tail[-2]):
                errors["invalid HK2 answer"] += 1
                continue
            answer = tail[2:-2]
            if len(answer) != 10 or answer[:2] != bytes.fromhex("9500"):
                errors["unexpected HK2 answer"] += 1
                continue
            key = "P01_21_HK2"
            value = int.from_bytes(answer[8:9], "little", signed=True)
        if key not in {"10fe100a_1100", "10fe100a_1101", "03100503", "P01_21_HK2"}:
            continue
        groups[key].append(dict(time=datetime.fromisoformat(match[1]), line=number,
                                payload=payload, value=value))
    return groups, dict(sha256=hashlib.sha256(raw).hexdigest(), errors=dict(errors))


def write_csv(name, rows):
    if rows:
        with (OUTPUT / name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)


def main():
    OUTPUT.mkdir(exist_ok=True)
    stage_pairs, mixer_pairs, summary = [], [], {}
    for path in sorted(ROOT.glob("ebusd*.log")):
        groups, metadata = read_log(path)
        fa = groups["03100503"]
        times = [r["time"] for r in fa]
        counters = Counter()
        for row in groups["10fe100a_1100"]:
            i = bisect.bisect_left(times, row["time"])
            if i == len(times):
                continue
            delta = (times[i] - row["time"]).total_seconds()
            if delta > 10:
                continue
            status, reply = row["payload"][4], fa[i]["payload"]
            pair = dict(log=path.name, time=str(row["time"]), line=row["line"],
                        status_a=f"{status:02x}", next_fa_time=str(times[i]),
                        next_fa_line=fa[i]["line"], gap_s=delta, fa_level=reply[3],
                        bit1=int(bool(status & 2)), bit2=int(bool(status & 4)),
                        bit3=int(bool(status & 8)), bit7=int(bool(status & 128)),
                        fa_uwp=int(bool(reply[2] & 64)))
            stage_pairs.append(pair)
            counters["pairs"] += 1
            counters["bit2_vs_level100_mismatch"] += pair["bit2"] != (reply[3] == 100)
            counters["bit1_vs_positive_level_mismatch"] += pair["bit1"] != (reply[3] > 0)
            counters["bit3_vs_uwp_mismatch"] += pair["bit3"] != pair["fa_uwp"]
            counters["bit7_vs_uwp_mismatch"] += pair["bit7"] != pair["fa_uwp"]
        direct = groups["P01_21_HK2"]
        times = [r["time"] for r in direct]
        mixer_counts = Counter()
        for row in groups["10fe100a_1101"]:
            i = bisect.bisect_left(times, row["time"])
            choices = [j for j in (i - 1, i) if 0 <= j < len(times)]
            if not choices:
                continue
            j = min(choices, key=lambda j: abs((times[j] - row["time"]).total_seconds()))
            delta = (times[j] - row["time"]).total_seconds()
            if abs(delta) > 10:
                continue
            status, value = row["payload"][4], direct[j]["value"]
            match = bool(status & 32) == (value > 0) and bool(status & 64) == (value < 0)
            mixer_counts["pairs"] += 1
            mixer_counts["mismatches"] += not match
            mixer_counts[f"mask_{status & 96:02x}_value_{value}"] += 1
            mixer_pairs.append(dict(log=path.name, time=str(row["time"]), line=row["line"],
                                    status_a=f"{status:02x}", flag5=int(bool(status & 32)),
                                    mixer_close=int(bool(status & 64)),
                                    direct_time=str(times[j]), direct_line=direct[j]["line"],
                                    signed_gap_s=delta, p01_21_hk2=value, match=match))
        metadata.update(stage_comparison=dict(counters), mixer_comparison=dict(mixer_counts))
        summary[path.name] = metadata
    write_csv("stage-candidates.csv", stage_pairs)
    write_csv("mixer-candidates.csv", mixer_pairs)
    (OUTPUT / "candidate-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({name: {k: v for k, v in data.items() if k.endswith("comparison")}
                      for name, data in summary.items()}, indent=2))


if __name__ == "__main__":
    main()
