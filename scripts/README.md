# Eigene Parametersammlung lesen

```sh
python3 scripts/read_menu_block.py --parameters-file scripts/parameters.example.txt
python3 scripts/read_menu_block.py --parameters-file meine-parameter.txt --server 192.168.87.46 --raw
```

Die Sammlung ist eine UTF-8-Textdatei mit einem TEM-Code pro Zeile und einem
optionalen Kontext, getrennt durch Leerzeichen oder Tabulatoren:

```text
# Meine Parameter
00-01 HK1  # Raumtemperatur Heizkreis 1
00-01 HK2
03-00      # Alle bekannten Kontexte
07-05 HK1
```

Leerzeilen und Kommentare ab `#` werden ignoriert. TEM-Codes sind dezimal;
`3-0` und `03-00` sind gleichwertig. Kontexte entsprechen der Kontextspalte
der Live-Ausgabe, etwa `HK1`, `HK2`, `WP`,
`EH`, `WE1` bis `WE8` oder `Global`; Groß-/Kleinschreibung ist beliebig.
Ohne Kontext werden alle für diesen TEM-Code bekannten, durch die
Kontextoptionen zugelassenen Zugriffe gelesen. Die Dateireihenfolge bleibt
erhalten, mehrere Kontexte eines Eintrags werden nach Kontext sortiert.
Doppelte TEM-/Kontext-Paare werden nur bei ihrem ersten Auftreten gelesen.

Die Datei wird vollständig geprüft, bevor die Expert-Freischaltung oder ein
Lesezugriff erfolgt. Ungültige Codes, unbekannte Parameter/Kontexte und durch
`--base-only` ausgeschlossene explizite Kontexte führen mit Dateiname und
Zeilennummer zum Abbruch. Eine leere Sammlung wird ebenfalls abgelehnt.
Es werden nur die ausgewählten Zugriffe aus `master-output/requests.json`
verwendet, auch über die Grenze `03-00` hinweg. Ausgabe und Fehlerbehandlung
entsprechen dem Parametermodus ohne die Spalte `Art`.

`--parameters-file` ist nicht mit Block, `--menu`, `--before-03-00` oder
`--from-03-00` kombinierbar. Verbindungsoptionen, `--raw`, `--base-only` und
`--context` gelten weiterhin. Relative Dateipfade beziehen sich auf das
aktuelle Arbeitsverzeichnis. Eine anpassbare Vorlage liegt in
[parameters.example.txt](parameters.example.txt).

# Parameter nach Code mit aktuellen Werten lesen

```sh
# Alle bekannten Werte der Gruppen 00, 01 und 02 mit Soll-/Ist-Zuordnung
python3 scripts/read_menu_block.py --before-03-00 --server 192.168.87.46

# Alle bekannten Parameter ab 03-00
python3 scripts/read_menu_block.py --from-03-00 --server 192.168.87.46
```

Ohne Block oder `--menu` wählen diese Optionen zwei eigenständige Betriebsarten.
Die Ausgabe ist numerisch nach TEM-Code und danach nach Kontext sortiert.
Pro TEM-Code und Kontext wird genau ein bevorzugter Selektor aus
`master-output/requests.json` direkt mit `06 21` gelesen; Verzeichnisblöcke
werden dabei nicht abgefragt. HK1/HK2, WP/EH und WE1–WE8 bleiben getrennt.
Aktuell sind dies 115 Zugriffe für 00–02 und 213 Zugriffe ab 03-00.
`--base-only` lässt die Zusatzkontexte aus; standardmäßig ist `1000` enthalten.
Andere Zusatzkontexte sind im Parameterkatalog nicht belegt und können
weiterhin gezielt mit `--menu` untersucht werden.

Der erste Modus zeigt die Spalten `TEM`, `Kontext`, `Art`, `Beschreibung` und
`Aktueller Wert`. `Art` ist `Soll` oder `Ist` gemäß der jeweiligen Spalte in
[input/soll_und_istwerte.md](../input/soll_und_istwerte.md), nicht allein anhand
der TEM-Gruppe. Beispielsweise ist `02-20` dort als Soll eingetragen.
Tabellenzeilen für WE1–WE8 und ausdrücklich nummerierte Raum-/Vorlauftemperaturen
werden dem jeweiligen Kontext zugeordnet. Andere mehrdeutige Bezeichnungen
bleiben als Alternativen erhalten; etwa beweisen WP-/EH-Namen in der Tabelle
keine neue Zuordnung der HK-Selektoren. Ohne passende Tabellenzuordnung steht
`—` in der Spalte `Art`; der Parameter wird trotzdem gelesen und angezeigt.
Der zweite Modus zeigt dieselben Spalten ohne `Art`.

Die Katalogdatei liefert nur Adressen und Kontextzuordnungen, keine aktuellen
Werte: Jeder angezeigte Wert stammt aus einer neuen Busantwort. Nicht verfügbare
Parameter (`ff1f`) und Lesefehler bleiben als Zeilen sichtbar. Bei einer
abweichenden TEM-Kennung wird ein Fehler ausgegeben und nicht unter der
ursprünglichen Kennung dekodiert. Fehler einzelner Werte unterbrechen die
übrigen Abfragen nicht und führen zu Exitcode 1.

Vor dem ersten Zugriff und nach jeweils mindestens 60 Sekunden wird die
Expert-Freischaltung erneuert, entsprechend dem beobachteten Minutenrhythmus.
Schlägt sie fehl, endet der Lauf. Es werden keine Parameterwerte geschrieben.
Die Sitzung wird am Ende nicht deaktiviert. Für die Parametermodi einschließlich der Parametersammlung wird
`commands.txt` gegen den gespeicherten Katalog-Hash geprüft. Nach Änderungen
am Scan zunächst `python3 scripts/analyze_master_log.py` ausführen.
Unbekannte oder bislang nicht belegte Selektoren werden nicht ergänzt;
insbesondere bleiben die dokumentierten Lücken des STE-Katalogs bestehen.

# Menüblock mit Beschreibungen und aktuellen Werten lesen

```sh
# Verzeichnisblock 14 (hex): alle angebotenen Parameter der Menüs a0..a7
python3 scripts/read_menu_block.py 14

# Nur das Menü a7, auf einem entfernten ebusd
python3 scripts/read_menu_block.py --menu a7 --server 192.168.87.46

# Nur Grundkontext; vollständige Rohantwort zusätzlich ausgeben
python3 scripts/read_menu_block.py --menu a7 --base-only --raw
```

Zwei optionale Darstellungsmodi filtern nach der numerischen TEM-Kennung:

```sh
# Alle Werte ab TEM 03-00 einschließlich im ausgewählten Block
python3 scripts/read_menu_block.py 00 --from-03-00

# Alle Werte vor TEM 03-00 im ausgewählten Block
python3 scripts/read_menu_block.py 00 --before-03-00
```

Die Optionen schließen einander aus und funktionieren auch mit `--menu`.
Ohne diese Optionen werden alle gelesenen Werte angezeigt. Die Filter beziehen
sich auf TEM-Kennungen aus den Antworten, nicht auf Menüadressen. Alle Plätze
der ausgewählten Menüs werden weiterhin gelesen; auch die zusätzliche
Rohdatenausgabe mit `--raw` wird gefiltert. Bei aktivem Filter zeigt die
Abschlussmeldung zusätzlich die Anzahl angezeigter und ausgefilterter Werte.

Benötigt Python 3, `ebusctl` im PATH und `--enablehex` am ebusd-Daemon.
Das Skript kann aus jedem Arbeitsverzeichnis aufgerufen werden; die
Beschreibungsdateien werden relativ zum Projektverzeichnis gefunden.
Verzeichnisblock und Menüadresse sind unterschiedliche Angaben und werden
immer hexadezimal interpretiert (auch `10` bedeutet hexadezimal 10).
Ein Block enthält acht Menüs; alternativ wählt `--menu` genau eines aus.

Das Skript liest die Platzanzahl live mit `06 20` und anschließend jeden
angebotenen Platz mit `06 21`. Wie beim Discovery-Scanner wird nach der
Verzeichnisantwort einmal der Expert-Zugang über `10 06 23 04 00 00 51 00`
freigeschaltet. Schlägt die Freischaltung fehl, werden keine Parameter gelesen.
Es werden keine Parameterwerte geschrieben. Die Sitzung wird nicht periodisch
verlängert oder anschließend deaktiviert; bei langen Abfragen kann sie ablaufen.

Die Ausgabe enthält Menü, interpretierten Kontext, TEM-Kennung, Beschreibung
und aktuellen Wert mit Einheit. Die Kontextspalte zeigt `HK1`/`HK2` für die
bekannten Heizkreismenüs, `WP`/`EH` für Wärmepumpe/Zusatzheizung und `WE1` bis
`WE8` für die Wärmeerzeugerinstanzen, auch bei den unteren Menüaliasen.
Ungepaarte allgemeine Menüs erscheinen als `Global`, nicht zugeordnete Menüs
mit ihrer Menüadresse und unbekannte Zusatzkontexte als `Unbekannt (XXXX)`.
Die HK-Zuordnung bleibt abgeleitet; `Global` bezeichnet hier die allgemeine
Menügruppe, keine bewiesene gemeinsame Speicherinstanz.
Beschreibungen stammen vorrangig
aus den Eingabetabellen unter `input/`, ersatzweise aus
`ste-output/parameter.json`; fehlende Namen bleiben ausdrücklich unbekannt.
Werte werden ausschließlich aus den neuen Busantworten übernommen. Die
Dekodierung folgt den bestehenden Regeln für `controller.tsp`, einschließlich
03-10 mit Skalierung 1/100, vorzeichenbehafteten Byte-Werten und Wochenminuten.
Auswahlwerte erscheinen numerisch, Schalter als Aus/Ein. Sonderantworten und
unbekannte Formate bleiben als Rohdaten sichtbar; ergänzende `06 22`-Inhalte
werden nicht abgefragt.

Bei gesetztem Zusatzflag wird auch der beobachtete Kontext `1000` gelesen.
`--base-only` unterdrückt ihn; wiederholbares `--context XXXX` ersetzt die
Standardauswahl. Gleiche TEM-Kennungen an verschiedenen Selektoren bleiben
getrennte Zeilen. Nicht verfügbare Plätze (`ff1f`) werden gezählt und ausgelassen.
Fehler einzelner Plätze verhindern die übrigen Abfragen nicht.

Weitere Optionen: `--port 8888`, `--timeout 5`, `--delay 0.1`,
`--destination 15` und `--expert-destination 10`. Ergebnisse erscheinen sofort
auf stdout, Fehler und Abschlusszähler auf stderr. Exitcode: 0 bei erfolgreicher
Abfrage, 1 bei Fehlern/Teilergebnissen, 2 bei ungültigem Aufruf, 130 bei Abbruch.

Offline-Test: `python3 -m unittest discover -s scripts -p test_read_menu_block.py`.

# Menu-based parameter discovery

Use `discover_parameters.py` to read the menu directory (`06 20`) and query
only its advertised slots (`06 21`):

```sh
python3 scripts/discover_parameters.py
python3 scripts/discover_parameters.py --server 192.168.87.46 > accessible-parameters.tsv
```

Requires Python 3 and `ebusctl`, with **`--enablehex` enabled on the ebusd daemon**.
It uses `ebusctl hex` with the read services `06 20` and `06 21`, so generated
CSV definitions are not required. CRC and escaping
are handled by ebusd. After each valid directory-block reply, it enables expert
mode **once before reading that block's parameters**, including its extended
contexts, by sending `10 06 23 04 00 00 51 00`. No parameter settings are written.
The master-directed write must return `done`; otherwise the block's parameters
are skipped and an error is reported. An invalid directory reply skips the
block without a write. Valid empty blocks also receive one enable command.
There is no additional timed refresh within a block or automatic disable at
the end. Long blocks can therefore still exceed the controller's session timeout.
Accessible means that the controller returned a parameter in the current
access state; it does not establish writability.

`read -f -h` still requires a matching loaded message definition in ebusd.
The earlier script version incorrectly used that command, causing
`ERR: element not found` for unknown selectors before they reached the bus.
This error did not establish that those controller parameters were unavailable.
With the corrected script, disabled `hex` support aborts the scan immediately
with an explanation. Add `--enablehex` to your existing ebusd startup options
and restart the daemon if necessary; no daemon settings are changed by the script.

The default block range is hexadecimal `00..1b`, as observed in the capture.
For menus with the extra flag, the script also queries the observed context
`1000`. This is kept as a context label rather than assumed to mean HK 2.
Every selector is retained separately even if its TEM number appears elsewhere.
Unoccupied slots (`ff1f`) are skipped; short and unknown parameter types are
retained with their raw response. Type and unit columns are raw hex codes;
no speculative value scaling is performed.

Examples:

```sh
# Only base context, directory block 14 (menus a0..a7)
python3 scripts/discover_parameters.py --first-block 14 --last-block 14 --base-only

# JSON Lines output; choose an explicit extended context
python3 scripts/discover_parameters.py --context 1000 --format jsonl > parameters.jsonl
```

`--context` can be repeated for known additional contexts; it replaces the
default list. `--destination` takes a hexadecimal read address (default `15`);
`--expert-destination` sets the expert-write address (default `10`). All calls
use the same ebusd connection options and its configured bus source address.
`--port`, `--timeout` and `--delay` configure the connection and pacing
(defaults: 8888, 5 seconds, 0.1 seconds). Blocks and contexts are hexadecimal.

Each output row includes TEM number, menu, slot, context, full selector,
raw type/unit and reply. Commands are not included in the output.
To query a selector manually, for example:

```sh
ebusctl -s localhost -p 8888 -t 5 -e hex 15062102a704
```

This reads 07-05 using selector `a7 04`. `hex` sends the request directly.
Results stream to stdout; errors and counts go to stderr. Failed reads do
not stop later slots, but make the final exit code 1 (partial scan).
Exit code 0 means all attempted reads succeeded; Ctrl+C returns 130 and
leaves previously printed rows usable. Discovery beyond the selected blocks
and contexts is not implied. The script does not read supplemental `06 22`
contents or guess write commands.

Offline verification: `python3 -m unittest discover -s scripts -p test_discover_parameters.py`.

# 06-21-Parameterscan

Mit Python 3 und `ebusctl` auf dem Rechner mit ebusd starten:

```bash
python3 scripts/scan_0621.py
```

Für einen entfernten ebusd oder einen begrenzten Bereich:

```bash
python3 scripts/scan_0621.py --server 192.168.87.46 --start 0000 --end 00ff --output scan-test
```

Standardziel ist `15` (`--destination` ändert die Hexadresse). Der Scanner
sendet `ebusctl ... hex 15062104XXYY0000`. Dabei läuft `YY` von `00` bis `ff`,
danach wird `XX` erhöht: insgesamt 65.536 Kombinationen. ebusd muss `hex`
erlauben (`--enablehex`). CRC und Bus-Escaping übernimmt ebusd.

Mit `--suffix` lassen sich ohne `--code` die letzten beiden Bytes festlegen
(Hex in Übertragungsreihenfolge, Standard: `0000`):

```bash
python3 scripts/scan_0621.py --suffix 004c --start 0000 --end ffff
```

Dies sendet `150621040000004c` bis `15062104ffff004c`. `--suffix` und
`--code` können nicht zusammen verwendet werden. Beim Fortsetzen denselben
Suffix angeben; auch in diesem Modus gilt `--step`.

Mit `--code` bleiben die ersten beiden Payload-Bytes fest, während `--start`
und `--end` die letzten beiden Bytes durchlaufen (Hex, Grenzen inklusive):

```bash
python3 scripts/scan_0621.py --server 192.168.87.46 --code 04ab --start 0000 --end ffff
```

Dies sendet `1506210404ab0000` bis `1506210404abffff`. `--code` gibt die
rohen Bytes in Übertragungsreihenfolge an, keinen TEM-Code im Format `xx-yyy`.
Auch `--code 0000` aktiviert diesen Modus. Ohne `--code` bleibt der bisherige
Modus mit festem Ende (`--suffix`, Standard `0000`) aktiv. Filter und Antwortdekodierung sind in
beiden Modi identisch.

`--step N` probiert in beiden Modi nur jede N-te Kombination, beginnend bei
`--start` (positive Dezimalzahl, Standard: `1`). Beispielsweise:

```bash
python3 scripts/scan_0621.py --code 04ab --start 0000 --end 00ff --step 16
```

Dies prüft die Payloads `04ab0000`, `04ab0010`, …, `04ab00f0`. Die Endgrenze
wird nur abgefragt, wenn sie mit der Schrittweite erreicht wird. Beim
Fortsetzen dieselbe Schrittweite angeben.

Ein Treffer hat das Längenbyte `0a`, genau zehn folgende Payload-Bytes und
beginnt in der Payload nicht mit `ff1f`. Der TEM-Einstellungscode wird aus den
ersten zwei **Antwort**-Payload-Bytes dekodiert, nicht aus der Anfrage:
`value = byte0 | (byte1 << 8)`, Gruppe `(value >> 7) & 31`, Nummer `value & 127`.
Beispiel: `ab02` ergibt `05-043`. Dies entspricht der Slave-Dekodierung von
[ebusd TEM_P](https://github.com/john30/ebusd/blob/master/src/lib/ebus/contrib/tem.cpp).

Treffer erscheinen sofort im Terminal und in `hits.tsv`. `all.tsv` enthält
zusätzlich alle übrigen Antworten und Fehler. Beide Dateien werden in einem
neuen Ausgabeverzeichnis erstellt (Standard: `scan-0621-DATUM-UHRZEIT`).
Vorhandene Verzeichnisse werden nicht überschrieben. Die TSV-Dateien enthalten
Zeitstempel, Server, Zieladresse, Anfrage, Status, Parameterbytes, TEM-Code,
Datentyp (`type`), Einheit (`unit`), `max`, `min`, Antwort und Fehlermeldung.

Bei Treffern werden die Payload-Bytes 3 und 4 entsprechend `command` aus
`tem/_templates.tsp` als `Values_type` und `Values_unit` angezeigt (Enum-Namen,
z.B. `TemperaturSoll` und `_C`). Unbekannte Werte erscheinen als `unknown(0xNN)`,
der UCH-Ersatzwert `ff` als `-`. Die Bytes 5–6 und 7–8 werden entsprechend
`Parameterkopf` aus `tem/controller.tsp` als `max` und `min` dekodiert:
vorzeichenbehaftete 16-Bit-Werte in Little-Endian, Ersatzwert `0080` als `-`.
Es erfolgt keine Skalierung, da beide Felder dort direkt als `SIN` definiert
sind.

Die letzten zwei Payload-Bytes werden zusätzlich als `value_bytes`,
`value_unsigned` und `value_signed` ausgegeben (Little-Endian, unskaliert).
`value` zeigt bei `on_off` den UIN-Wert als `Aus`/`Ein` (Ersatzwert `ffff`: `-`).
Für die Temperaturtypen `0d`, `4d`, `8d` mit Einheit `_C` oder `K` wird
zusätzlich SIN / 10 angenommen, wie bei den meisten Temperaturmodellen in
`controller.tsp` (Ersatzwert `0080`: `-`). `value_encoding` kennzeichnet diese
Annahme ausdrücklich: Es gibt auch abweichende Skalierungen wie `temp2`.
Bei anderen Typen bleibt `value` leer; im Terminal steht `unbekannt`, und die
Rohwerte bleiben sichtbar. Typ und Einheit allein reichen beispielsweise für
Versions-, Zeit- und Zählerwerte nicht zur eindeutigen Dekodierung aus.
Die Interpretation der letzten zwei Bytes als Wert setzt den Aufbau
`Parameterkopf` plus Zwei-Byte-Wert voraus; etwa Zähler mit Sechs-Byte-Kopf
und Vier-Byte-Wert brauchen eine eigene Zuordnung.

Beispiel aus `controller.tsp`: `0ab3428d02bc026400f401` enthält am Ende
`f401`, also den Rohwert 500 und unter der Annahme SIN / 10 den Wert `50 °C`.

Beispiel: `0aab028d02fa009cff0000` ergibt `05-043`,
`type=TemperaturSoll unit=_C max=250 min=-100`.

`--delay` steuert die Pause zwischen Abfragen (Standard: 0,1 Sekunden),
`--timeout` das ebusctl-Timeout (Standard: 5 Sekunden). Ein vollständiger Scan
dauert allein durch die Pausen mindestens ca. 1 Stunde 49 Minuten, zusätzlich
zur Telegrammlaufzeit und eventuellen Timeouts. Fehler werden protokolliert;
der Scan läuft weiter und endet bei Fehlern mit Exitcode 1.

Strg+C beendet den Scan mit Exitcode 130 und zeigt eine Startkombination zum
Fortsetzen an. Mit `--start XXXX` und einem neuen Ausgabeverzeichnis fortsetzen;
im Modus mit festem Anfang auch denselben `--code` angeben. Die zuletzt
begonnene Anfrage wird dabei gegebenenfalls wiederholt.
