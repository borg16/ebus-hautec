#!/usr/bin/env python3
"""Show operating-mode changes of both heating circuits in an ebusd raw log.

Sources (see docs/Heating-Mode-2026-10-11-test3.md):
  - controller broadcasts 10 FE 10 0A 11 02 (HK1) / 11 03 (HK2): state bytes
  - FB1/FB2 change answers (40 <block>) and the block 20 answer: mode byte
Usage: analyze_operating_mode.py ebusd.test3.log
"""
import sys

BROADCAST = {"1102": "HK1", "1103": "HK2"}
FB = {"90": "HK1/FB1", "91": "HK2/FB2"}


def frames(path):
    for line in open(path):
        parts = line.split()
        if len(parts) >= 3 and parts[2][:1] == "<":
            yield parts[1][:8], parts[2][1:]


def main(path):
    last = {}
    for t, h in frames(path):
        try:
            qq, zz, pb_sb, ln = h[0:2], h[2:4], h[4:8], int(h[8:10], 16)
        except ValueError:
            continue
        data = h[10:10 + 2 * ln]
        if qq == "10" and zz == "fe" and pb_sb == "100a" and data[:4] in BROADCAST:
            name = BROADCAST[data[:4]]
            state = data[12:20]  # phase, mode, 00, program coding
            if last.get(name) != state:
                print(f"{t} broadcast {name}: state bytes {state}")
                last[name] = state

    # Block 20 answers follow the master part (data, CRC, ACK) in the same raw line.
    for t, h in frames(path):
        if h[0:2] == "10" and h[2:4] in FB and h[4:8] == "100a" and h[8:10] == "02" and h[10:12] == "20":
            body = h[18:]  # len, 30 blk, day, night, water, mode, ...
            if body[2:4] == "30" and len(body) >= 20:
                mode = body[18:22]  # Betriebsart, Uhrenprogramm
                key = (h[2:4], "mode")
                if last.get(key) != mode:
                    print(f"{t} FB block 20 {body[4:6]} {FB[h[2:4]]}: mode/program {mode}")
                    last[key] = mode


if __name__ == "__main__":
    main(sys.argv[1])
