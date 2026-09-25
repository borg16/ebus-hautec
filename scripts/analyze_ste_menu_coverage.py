#!/usr/bin/env python3
"""Offline: prove a minimum menu cover for the reachable STE records."""

from collections import defaultdict
import csv
import json
import re

from analyze_master_log import ROOT, tem_id


def matches(record, row):
    if not record["tem_id"] or record["tem_id"] != row["tem"]:
        return False
    menu = int(row["menu"], 16)
    # Observed reduced/expanded aliases; see Menu-Structure.md.
    if 0x63 <= menu <= 0x72:
        menu += 0x40
    level = int(re.match(r"Einstellebene (\d+)", record["group_text"])[1])
    if level >= 9:
        return menu == 0xa0 + level and row["context"] == "base"
    if menu >= 0xa9 or int(row["menu"], 16) in (0x29, 0x2a):
        return False
    context = "1000" if record["context"] == "Heizkreis 2 (abgeleitet)" else "base"
    return row["context"] == context


def preference(menu):
    # Prefer expanded menus, then the observed overview 01 over its alternative 03.
    number = int(menu, 16)
    return (number < 0xa0, number)


def analyze(records, rows):
    for row in rows:
        if tem_id(row["response"]) != row["tem"]:
            raise ValueError(f"Scan identity mismatch: {row['selector']}")
        if not row["selector"].startswith(row["menu"]):
            raise ValueError(f"Scan menu mismatch: {row['selector']}")
    options = {r["index"]: [s for s in rows if matches(r, s)] for r in records}
    coverage = defaultdict(set)
    for index, candidates in options.items():
        for row in candidates:
            coverage[row["menu"]].add(index)
    # A subset can always be replaced by its superset at equal menu cost.
    selected = {
        m: entries for m, entries in coverage.items()
        if not any(entries < other or (entries == other and preference(n) < preference(m))
                   for n, other in coverage.items() if n != m)
    }
    reachable = {i for i, candidates in options.items() if candidates}
    if set().union(*selected.values()) != reachable:
        raise ValueError("Incomplete cover")

    # Prove the lower bound against ALL original menus, not only the reduced set.
    # Each witness needs one menu from its candidate set. Disjoint candidate sets
    # force distinct menus, hence as many menus as there are witnesses.
    witnesses, used = {}, set()
    for menu, indices in sorted(selected.items()):
        private = indices - set().union(*(s for m, s in selected.items() if m != menu))
        candidates = sorted(private, key=lambda i: (len({r["menu"] for r in options[i]}), i))
        for index in candidates:
            menus = {r["menu"] for r in options[index]}
            if not menus & used:
                witnesses[menu] = (index, menus)
                used.update(menus)
                break
        else:
            raise ValueError("Data changed: a minimum cover needs a more general search")
    return options, selected, witnesses


def main():
    records = json.loads((ROOT / "ste-output/parameter.json").read_text())["records"]
    with (ROOT / "commands.txt").open() as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    options, selected, witnesses = analyze(records, rows)
    by_index = {r["index"]: r for r in records}
    reachable = {i for i, candidates in options.items() if candidates}
    missing_ids = sorted({r["tem_id"] for r in records if r["tem_id"] and not options[r["index"]]})
    named = sum(bool(r["tem_id"]) for r in records)
    menus = sorted(selected)
    out = ROOT / "menu-output"
    out.mkdir(exist_ok=True)
    with (out / "STE-Menuezuordnung.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["ste_index", "tem", "name", "context", "menu", "selector", "status"])
        for record in records:
            candidates = [r for r in options[record["index"]] if r["menu"] in selected]
            chosen = min(candidates, key=lambda r: r["selector"]) if candidates else None
            writer.writerow([record["index"], record["tem_id"] or "", record["name"], record["context"],
                             chosen["menu"] if chosen else "", chosen["selector"] if chosen else "",
                             "zugeordnet" if chosen else "kein Selektor belegt" if record["tem_id"]
                             else "keine TEM-Kennung"])

    lines = ["# Menüauswahl für den STE-Parameterkatalog", "",
             "Generiert mit `python3 scripts/analyze_ste_menu_coverage.py` aus "
             "[commands.txt](../commands.txt) und [STE-Parameterdaten](../ste-output/parameter.json). "
             "Ziel ist [ste-output/Parameter.md](../ste-output/Parameter.md). Keine Live-Abfragen.", "",
             "## Ergebnis", "",
             f"Eine vollständige Abdeckung aller {len(records)} STE-Datensätze ist mit den bekannten "
             f"Selektoren nicht belegt. **{len(menus)} Menüs decken alle {len(reachable)} zuordenbaren "
             f"Datensätze ab**: {named} Einträge haben eine TEM-Kennung, davon fehlen "
             f"{named - len(reachable)} Einträge mit {len(missing_ids)} unterschiedlichen Kennungen. "
             f"Weitere {len(records) - named} Einträge besitzen keine TEM-Kennung.", "",
             "```text", " ".join(menus), "```", "",
             "Alle Menüadressen sind hexadezimal. Grundkontext und Zusatzkontext `1000` "
             "werden bei den entsprechenden Menüs gemeinsam berücksichtigt. Die Zuordnung "
             "zu HK 1/2 bleibt aus STE und Mitschnitt abgeleitet. WP/EH und WE 1–8 bleiben "
             "getrennte Instanzen. Bei nicht gepaarten STE-Einträgen der Ebenen 1–8 wird der "
             "Grundkontext verwendet; damit ist keine globale Speicheridentität bewiesen.", "",
             "## Menüabdeckung und Minimalitätsbeleg", "",
             "Die Anzahl zählt STE-Datensätze, nicht alle im Menü vorhandenen Busparameter. "
             "Jede Tabellenzeile enthält einen notwendigen Beispielparameter samt **allen** "
             "Menüalternativen aus dem Scan. Diese Alternativmengen sind paarweise disjunkt. "
             f"Daher werden mindestens {len(menus)} Menüs benötigt; die Auswahl erreicht diese "
             "Untergrenze unter der dokumentierten Kontextzuordnung. Erweiterte Menüs werden "
             "bevorzugt. Menü `03` kann `01` für diesen STE-Ausschnitt ersetzen.", "",
             "| Menü | Kontexte | STE-Einträge | Notwendiges Beispiel (STE #) | Alle Menüalternativen |",
             "|---|---|---:|---|---|"]
    for menu in menus:
        index, alternatives = witnesses[menu]
        contexts = sorted({r["context"] for i in selected[menu] for r in options[i] if r["menu"] == menu},
                          key=lambda c: (c != "base", c))
        lines.append(f"| `{menu}` | {', '.join(contexts)} | {len(selected[menu])} | "
                     f"{by_index[index]['tem_id']} (#{index}) | {', '.join(sorted(alternatives))} |")
    lines += ["", "Die vollständige Zuordnung jedes STE-Eintrags zu einem konkreten Selektor steht in "
              "[STE-Menuezuordnung.tsv](STE-Menuezuordnung.tsv). "
              "Gleiche TEM-Kennungen allein werden nicht über WP/EH/WE-Kontexte hinweg gleichgesetzt.", "",
              "## Fehlende TEM-Kennungen", "",
              "Diese Kennungen kommen im gesamten Scan nicht vor. Das beweist nicht, dass der "
              "Regler sie grundsätzlich nicht unterstützt; es gibt dafür derzeit keine belegten Selektoren.", "",
              "| TEM | Bezeichnung | STE-Datensätze |", "|---|---|---|"]
    for ident in missing_ids:
        missing = [r for r in records if r["tem_id"] == ident and not options[r["index"]]]
        lines.append(f"| {ident} | {missing[0]['name']} | {', '.join(str(r['index']) for r in missing)} |")
    lines += ["", "## Einträge ohne TEM-Kennung", "",
              "Keine gesicherte Zuordnung zu `06 21`; insbesondere werden Zeitprogramme oder "
              "Kommandos nicht anhand ihrer Namen auf unbekannte Selektoren abgebildet.", "",
              "| Bezeichnung | STE-Datensätze |", "|---|---|"]
    unnamed = defaultdict(list)
    for record in records:
        if not record["tem_id"]:
            unnamed[record["name"]].append(str(record["index"]))
    for name, indices in unnamed.items():
        lines.append(f"| {name} | {', '.join(indices)} |")
    lines += ["", "## Auslesen", "", "```sh", f"for menu in {' '.join(menus)}; do",
              '  python3 scripts/read_menu_block.py --menu "$menu" --server 192.168.87.46 || break',
              "done", "```", "",
              "Serveradresse anpassen. Nicht `--base-only` verwenden: Die STE-Heizkreispaare "
              "benötigen auch `1000`. Das Skript liest alle angebotenen Plätze dieser Menüs, "
              "also gegebenenfalls zusätzliche Parameter außerhalb des STE-Katalogs. "
              "Voraussetzung sind `ebusctl`, ebusd mit `--enablehex` und die vom Skript "
              "durchgeführte Expert-Freischaltung. Die Aufrufe oben wurden nicht live ausgeführt.", "",
              "Wer stattdessen ganze Verzeichnisblöcke lesen möchte, benötigt für diese Auswahl "
              "`00 01 04 14 15 16`; dabei werden weitere Menüs mitgelesen.", ""]
    (out / "STE-Menueabdeckung.md").write_text("\n".join(lines))
    print(f"{len(menus)} menus; {len(reachable)}/{len(records)} STE records; minimum proven")
    print(" ".join(menus))


if __name__ == "__main__":
    main()
