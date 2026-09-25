# Menüauswahl für den STE-Parameterkatalog

Generiert mit `python3 scripts/analyze_ste_menu_coverage.py` aus [commands.txt](../commands.txt) und [STE-Parameterdaten](../ste-output/parameter.json). Ziel ist [ste-output/Parameter.md](../ste-output/Parameter.md). Keine Live-Abfragen.

## Ergebnis

Eine vollständige Abdeckung aller 217 STE-Datensätze ist mit den bekannten Selektoren nicht belegt. **19 Menüs decken alle 195 zuordenbaren Datensätze ab**: 206 Einträge haben eine TEM-Kennung, davon fehlen 11 Einträge mit 8 unterschiedlichen Kennungen. Weitere 11 Einträge besitzen keine TEM-Kennung.

```text
01 0b 23 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af b0 b1 b2
```

Alle Menüadressen sind hexadezimal. Grundkontext und Zusatzkontext `1000` werden bei den entsprechenden Menüs gemeinsam berücksichtigt. Die Zuordnung zu HK 1/2 bleibt aus STE und Mitschnitt abgeleitet. WP/EH und WE 1–8 bleiben getrennte Instanzen. Bei nicht gepaarten STE-Einträgen der Ebenen 1–8 wird der Grundkontext verwendet; damit ist keine globale Speicheridentität bewiesen.

## Menüabdeckung und Minimalitätsbeleg

Die Anzahl zählt STE-Datensätze, nicht alle im Menü vorhandenen Busparameter. Jede Tabellenzeile enthält einen notwendigen Beispielparameter samt **allen** Menüalternativen aus dem Scan. Diese Alternativmengen sind paarweise disjunkt. Daher werden mindestens 19 Menüs benötigt; die Auswahl erreicht diese Untergrenze unter der dokumentierten Kontextzuordnung. Erweiterte Menüs werden bevorzugt. Menü `03` kann `01` für diesen STE-Ausschnitt ersetzen.

| Menü | Kontexte | STE-Einträge | Notwendiges Beispiel (STE #) | Alle Menüalternativen |
|---|---|---:|---|---|
| `01` | base, 1000 | 4 | 03-50 (#1) | 01, 03 |
| `0b` | base, 1000 | 12 | 03-51 (#9) | 0b |
| `23` | base, 1000 | 20 | 03-00 (#32) | 23 |
| `a3` | base, 1000 | 7 | 03-23 (#47) | a3 |
| `a4` | base | 8 | 04-40 (#66) | a4 |
| `a5` | base | 11 | 05-40 (#81) | a5 |
| `a6` | base | 11 | 06-13 (#92) | a6 |
| `a7` | base, 1000 | 16 | 07-31 (#108) | a7 |
| `a8` | base | 5 | 08-55 (#110) | a8 |
| `a9` | base | 38 | 09-31 (#126) | a9 |
| `aa` | base | 15 | 09-14 (#162) | aa |
| `ab` | base | 6 | 04-22 (#170) | 6b, ab |
| `ac` | base | 6 | 04-22 (#176) | 6c, ac |
| `ad` | base | 6 | 04-22 (#182) | 6d, ad |
| `ae` | base | 6 | 04-22 (#188) | 6e, ae |
| `af` | base | 6 | 04-22 (#194) | 6f, af |
| `b0` | base | 6 | 04-22 (#200) | 70, b0 |
| `b1` | base | 6 | 04-22 (#206) | 71, b1 |
| `b2` | base | 6 | 04-22 (#212) | 72, b2 |

Die vollständige Zuordnung jedes STE-Eintrags zu einem konkreten Selektor steht in [STE-Menuezuordnung.tsv](STE-Menuezuordnung.tsv). Gleiche TEM-Kennungen allein werden nicht über WP/EH/WE-Kontexte hinweg gleichgesetzt.

## Fehlende TEM-Kennungen

Diese Kennungen kommen im gesamten Scan nicht vor. Das beweist nicht, dass der Regler sie grundsätzlich nicht unterstützt; es gibt dafür derzeit keine belegten Selektoren.

| TEM | Bezeichnung | STE-Datensätze |
|---|---|---|
| 03-60 | Partydauer HB | 7, 8 |
| 04-61 | Vorlaufsollwert-Steigung in der Aufheizphase | 68 |
| 04-62 | Vorlaufsollwert-Abfall in der Abkühlphase | 69 |
| 04-63 | Vorlaufsollwert in der Beharrungsphase | 70 |
| 04-64 | Dauer der Beharrungsphase | 71 |
| 05-60 | Partydauer WWB | 22, 23 |
| 09-20 | Solltemperatur Handbetrieb | 57, 58 |
| 09-32 | TWVmin Kühlbetrieb | 127 |

## Einträge ohne TEM-Kennung

Keine gesicherte Zuordnung zu `06 21`; insbesondere werden Zeitprogramme oder Kommandos nicht anhand ihrer Namen auf unbekannte Selektoren abgebildet.

| Bezeichnung | STE-Datensätze |
|---|---|
| Automatikprogramm | 3, 4 |
| BW Zeitprog mit Heizkreisprogramm 1 | 24, 25 |
| BW Zeitprog mit Heizkreisprogramm 2 | 26, 27 |
| BW Zeitprog mit Heizkreisprogramm 3 | 28, 29 |
| Störung quittieren | 30 |
| Betriebsdaten zurückstellen | 31 |
| TWA Maximalwert | 154 |

## Auslesen

```sh
for menu in 01 0b 23 a3 a4 a5 a6 a7 a8 a9 aa ab ac ad ae af b0 b1 b2; do
  python3 scripts/read_menu_block.py --menu "$menu" --server 192.168.87.46 || break
done
```

Serveradresse anpassen. Nicht `--base-only` verwenden: Die STE-Heizkreispaare benötigen auch `1000`. Das Skript liest alle angebotenen Plätze dieser Menüs, also gegebenenfalls zusätzliche Parameter außerhalb des STE-Katalogs. Voraussetzung sind `ebusctl`, ebusd mit `--enablehex` und die vom Skript durchgeführte Expert-Freischaltung. Die Aufrufe oben wurden nicht live ausgeführt.

Wer stattdessen ganze Verzeichnisblöcke lesen möchte, benötigt für diese Auswahl `00 01 04 14 15 16`; dabei werden weitere Menüs mitgelesen.
