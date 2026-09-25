# EBUSD Configuration for Reading Hautec Carno (~2006) Data

This is a configuration to read and write observed numeric parameters of the TEM SE 6000 WPC controller.

The preliminary analysis of the protocol is documented in [Protocol-Analysis.md](Protocol-Analysis.md).

Die Zuordnung von Heizkreisen, Pumpen, Warmwasser und Relais sowie die aktuellen
Betreiberbeobachtungen sind in [Heating-Control-Analysis.md](Heating-Control-Analysis.md)
dokumentiert. Dort ist auch die funktionierende Einstellung 07-05 = 2/0 gegenüber
der problematischen Versuchseinstellung 0/3 aus dem älteren Mitschnitt eingeordnet.

The active [controller.tsp](controller.tsp) combines the scan in `commands.txt`
with the CRC-checked requests in `input/complete.log`. It contains 328 parameter
read selectors, one per TEM identifier and context, plus `Menueblock`.
Expanded menus `a3..b2` replace matching aliases in `63..72`; duplicate views
within each context are consolidated. WP, EH and WE1..WE8 stay separate.
261 write commands cover the selected selectors: 205 numeric parameter/context
pairs from `03-00` upward, including scan-only accesses, plus the 56 existing
writes below `03-00`. Device acceptance has not been verified for every command.
Eight short-response accesses (`03-61`, `03-62`, `03-63` in HK1/HK2,
`05-61` and `05-64`) remain read-only because their write format is unknown.
The inferred encoding of `03-07` is dimensionless SIN / 10, matching its scan
and STE limits. See [write definitions](master-output/Parameter.md#schreibdefinitionen-ab-03-00).

Command names use TEM numbers (`Pxx_xx`), with `_HK1`, `_HK2`,
`_WP`, `_EH` or `_WE1` etc. where needed. HK labels follow the inferred context
mapping, not proof of separate physical sensors. Old names have been removed;
see [the migration table](master-output/Umbenennung.md) for their replacements.
Only parameter selectors present in `commands.txt` are generated, plus the
generic `Menueblock` directory command with its `index` argument. Unavailable
slots and `06 22` list commands are omitted. The discovery script also supports
reading the directory directly via `ebusctl hex`.

Parameter descriptions come first from `input/Checkliste_Regler_Programmierung.CSV`
and `input/soll_und_istwerte.md`, with the STE catalog as fallback. The leading
TEM identifier in the checklist is used, not its second-column display code.
Ambiguous names remain explicit alternatives, and missing names stay marked
unknown. Each definition records its data and name sources. Regenerate with:

```sh
python3 scripts/analyze_master_log.py
npm run build:csv
```

It replaces the previously imported `tem/controller.tsp`.
See [Master-Analysis.md](Master-Analysis.md) for read coverage and remaining
gaps, [Write-Analysis.md](Write-Analysis.md) for write evidence, and [the
parameter index](master-output/Parameter.md) for model names by TEM parameter.
Parameters without an observed selector in `parameter.json` are not guessed.

Für Expert-Einsteller muss vor dem Lesen oder Schreiben zunächst die quittierte
Freischaltung `01 10 06 23 04 00 00 51 00` gesendet werden. Danach werden auch
Parameter wie `05-05` sichtbar; wiederholte `00 00`-Schreibungen halten die
Sitzung aktiv.

## Parameter live nach Code auslesen

```sh
python3 scripts/read_menu_block.py --before-03-00  # Gruppen 00–02, mit Soll/Ist
python3 scripts/read_menu_block.py --from-03-00    # Parameter ab 03-00
```

Liest die bekannten Parameter nach TEM-Code sortiert, jeweils in ihren
relevanten Kontexten. Die Soll-/Ist-Zuordnung folgt `input/soll_und_istwerte.md`.
Mit `--server HOST` lässt sich ein entfernter ebusd ansprechen.

Eine eigene Parametersammlung lässt sich als Textdatei übergeben:

```sh
python3 scripts/read_menu_block.py --parameters-file scripts/parameters.example.txt
```

Pro Zeile steht ein TEM-Code und optional ein Kontext, z. B. `00-01 HK1`.
Ohne Kontext werden alle bekannten Kontexte gelesen. Leerzeilen und
Kommentare mit `#` sind erlaubt. Details stehen in [scripts/README.md](scripts/README.md).

## Menüblock live auslesen

```sh
python3 scripts/read_menu_block.py 14          # Block 14 hex: Menüs a0..a7
python3 scripts/read_menu_block.py --menu a7   # nur Menü a7
```

Zeigt Beschreibungen und aktuelle Werte aller angebotenen Parameter, auch im
beobachteten Zusatzkontext. Benötigt `ebusctl` und ebusd mit `--enablehex`;
der Expert-Zugang wird einmal freigeschaltet.
Weitere Optionen und Details stehen in [scripts/README.md](scripts/README.md).

## Building the ebusd CSV configuration

The message definitions are written in [TypeSpec](https://typespec.io/) (`.tsp` files) using the [`@ebusd/ebus-typespec`](https://www.npmjs.com/package/@ebusd/ebus-typespec) library, with `main.tsp` as the entry point importing all circuit files. To compile them into the ebusd CSV configuration:

```bash
npm install
npm run build:csv
```

This emits one CSV file per circuit (e.g. `broadcast.csv`, `burner1.csv`, `remote1.csv`, ...) into `csv-output/@ebusd/ebus-typespec/hautec/`, ready to be placed in ebusd's configuration directory.

Note: circuit-specific `.tsp` source files intentionally do **not** use a `ZZ.` numeric filename prefix (e.g. `burner1.tsp`, not `03.burner1.tsp`). The circuit address is instead set via `@zz(...)` on the namespace. This is required because the emitter blanks the CSV `circuit` column whenever the source filename (minus a leading 2-hex-digit prefix) matches the circuit name — a convention meant for ebusd's `--scanconfig` auto-detection. Since this configuration is loaded as plain static CSV files (no `--scanconfig`), a blank circuit column causes ebusd to fail with `ERR: missing argument, circuit`.
