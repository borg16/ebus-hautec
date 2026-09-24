"""Offline audit of directory slots, parameter identities and context pairs."""

from collections import defaultdict
from pathlib import Path

from analyze_master_log import ROOT, read_log, tem_id


def analyze():
    records, _ = read_log(ROOT / "input/complete.log")
    records = [r for r in records if (r["source"], r["destination"], r["status"])
               == ("01", "15", "complete")]
    blocks, reads = defaultdict(list), defaultdict(list)
    for r in records:
        if r["service"] == "0620":
            blocks[int(r["request"], 16)].append(r)
        elif r["service"] == "0621":
            reads[r["request"]].append(r)
    descriptors = {}
    for block, samples in blocks.items():
        assert len({r["response"] for r in samples}) == 1, "directory changed"
        payload = bytes.fromhex(samples[0]["response"])
        assert len(payload) == 8
        descriptors.update({8 * block + i: value for i, value in enumerate(payload)})
    identities = {}
    for selector, samples in reads.items():
        ids = {tem_id(r["response"]) for r in samples}
        assert len(ids) == 1, f"identity changed: {selector}"
        identities[selector] = next(iter(ids))
        request = bytes.fromhex(selector)
        assert (request[1] & 127) < (descriptors[request[0]] & 127)
        if len(request) == 4:
            assert request[1] & 128 and request[2:] == b"\x10\x00"
            assert descriptors[request[0]] & 128
        else:
            assert len(request) == 2 and not request[1] & 128
    pairs = []
    for selector in sorted(reads):
        request = bytes.fromhex(selector)
        if len(request) != 4:
            continue
        base = bytes([request[0], request[1] & 127]).hex()
        assert base in reads
        pairs.append((base, selector))
    valid_pairs = sum(identities[a] == identities[b] != "31-127" for a, b in pairs)
    empty_pairs = sum(identities[a] == identities[b] == "31-127" for a, b in pairs)
    lines = ["# Prüfung der Menüadressierung", "",
             "Generiert mit `python3 scripts/analyze_menu_structure.py` aus CRC-geprüften "
             "vollständigen Antworten in `input/complete.log`. Interpretation: "
             "[Menu-Structure.md](../Menu-Structure.md). Alle Selektoren sind hexadezimal.", "",
             f"- {len(blocks)} unveränderte Verzeichnisblöcke; "
             f"{sum(bool(v) for v in descriptors.values())} nichtleere Menüs; "
             f"{sum(v & 127 for v in descriptors.values())} Plätze.",
             f"- {len(reads)} gelesene Selektoren; alle Indizes innerhalb der Verzeichnisgrenzen.",
             "- Pro Selektor bleibt die TEM-Kennung über alle Beobachtungen unverändert.",
             f"- {len(pairs)} Kontextpaare: {valid_pairs} gleiche gültige Kennungen, "
             f"{empty_pairs} beidseitig unbelegt, {len(pairs)-valid_pairs-empty_pairs} unterschiedlich verfügbar.",
             "- Alle erweiterten Selektoren gehören zu Menüs mit gesetztem Zusatzflag.", "",
             "## Kontextpaare", "",
             "`—` bedeutet Antwortkennung `ff 1f`; HK-Zuordnungen werden hier nicht vorausgesetzt.", "",
             "| Grundselektor | Erweiterter Selektor | TEM Grundkontext | TEM Zusatzkontext | Erste Logzeilen |",
             "|---|---|---|---|---|"]
    def label(s):
        return "—" if identities[s] == "31-127" else identities[s]
    for a, b in pairs:
        lines.append(f"| `{a}` | `{b}` | {label(a)} | {label(b)} | "
                     f"{reads[a][0]['line']} / {reads[b][0]['line']} |")
    lines += ["", "## Sämtliche beobachteten Menüplätze", "",
              "Die letzte Antwort ist je Selektor zeitlich separat bestimmt; sie ist roh "
              "angegeben und bildet keine gemeinsame Momentaufnahme.", "",
              "| Selektor | TEM | Erste Logzeile | Letzte Logzeile | Letzte Antwort (hex) |",
              "|---|---|---:|---:|---|"]
    for s, samples in sorted(reads.items()):
        lines.append(f"| `{s}` | {label(s)} | {samples[0]['line']} | "
                     f"{samples[-1]['line']} | `{samples[-1]['response']}` |")
    output = ROOT / "menu-output/Adressierung.md"
    output.parent.mkdir(exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[4:9]))


if __name__ == "__main__":
    analyze()
