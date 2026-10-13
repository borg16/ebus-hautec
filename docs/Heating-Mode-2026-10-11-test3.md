# Betriebsart der Heizkreise (Versuch test3, 2026-10-11)

Rohdaten: `ebusd.test3.log`. Auswertung: `scripts/analyze_operating_mode.py ebusd.test3.log`.

Ablauf: Start HK1 Standby / HK2 Uhrenprogramm 1; 22:03 HK2 → Standby; 22:18 HK1 → Programm 1;
22:22 HK2 → Programm 1. Der Controller fragt jede Bedieneinheit alle 80 s ab.

## Lesen

| Quelle | Feld | Standby | Automatik |
|---|---|---|---|
| FB-Antwort `10 0A / 20 <Block>` (FB1 Block `01`, FB2 Block `0B`) | `Betriebsart`, `Uhrenprogramm` | `00` | `01` (Programm 1 = `00`) |
| Broadcast `10 0A 11 02` (HK1) | `Status2a.b4` (Betriebsart) | `00` | `01` |
| Broadcast `10 0A 11 03` (HK2) | `Status3a.b6` (Betriebsart) | `00` | `01` |

Alle Betriebsarten: Abschnitt Test5.

Die FB meldet eine Änderung mit `40 <Block>` auf `D0 14` (FB1) bzw. `D0 15` (FB2); der
Controller liest dann Block `21` und `20`. Die Broadcast-Zustände folgen innerhalb eines
80-s-Zyklus.

| Wechsel | FB-Änderung | Broadcast |
|---|---|---|
| HK2 → Standby | 22:03:54 | 22:04:13 |
| HK1 → Programm 1 | 22:19:44 | 22:20:03 |
| HK2 → Programm 1 | 22:23:54 | 22:24:13 |

Abgeleitete Größen (Vorlauf-Sollwerte in `10 02`/`10 03`, Pumpenbits `11 00`/`11 01`)
laufen nach (Pumpennachlauf 15 min) und taugen nicht als Modusanzeige.

## Nachtrag test4 (HK1 Standby, `ebusd.test4.log`)

- 23:12:51 `31 → 10 / 06 23 04 01 00 00 00` (ACK `00`): ebusd schreibt `P03_50_HK1_set` = 0.
- 23:13:04 FB1 antwortet auf `D0 14` mit `50 01`; der Controller schreibt `10 → 90 / 10 0A 0E 31 01 …`
  und `… 30 01 …` (Betriebsart `00`, neuer Schlüssel `ca 03`). Danach `C0 00`; FB1 setzt nichts zurück.
- Der Schreibweg `06 23` für 03-50 wird also zur FB durchgereicht und bleibt bestehen
  (bisher nur Wert 0 bei HK1 belegt).

## Test5 (HK2 über die FB durchgeschaltet, `ebusd.test5.log`, 2026-10-12)

Je Wechsel meldet FB2 `40 0B`; der Controller liest `20 0B`, der 80-s-Broadcast `11 03`
folgt 18–19 s später.

| Einstellung | FB `20 0B`: Betriebsart / Programm | `11 03`: Phase / Betriebsart / – / Programmcode |
|---|---|---|
| Standby (test3/4) | 0 / 0 | 04 / 00 / 00 / 01 |
| Automatik, Programm 1 | 1 / 0 | 01 oder 00 / 01 / 00 / 01 |
| Automatik, Programm 2 | 1 / 1 | 01 / 01 / 00 / 03 |
| Automatik, Programm 3 | 1 / 2 | 00 / 01 / 00 / 05 |
| Heizbetrieb (Sonne) | 2 / 0 | 01 / 02 / 00 / 01 |
| Absenkbetrieb (Mond) | 3 / 0 | 00 / 03 / 00 / 01 |
| Sommerbetrieb | 4 / 0 | 04 / 04 / 00 / 01 |
| Hand-/Notbetrieb | 5 / 0 | 04 / 05 / 00 / 01 |

Ergebnis:

- **Betriebsart** = 03-50 (0 Standby, 1 Automatik, 2 Heizen, 3 Absenken, 4 Sommer, 5 Hand), gelesen aus
  `20 0B` Byte 1 oder `11 03` Byte 2 (HK1: `11 02`).
- **Uhrenprogramm** (0-basiert) steht in `20 0B` Byte 2; im Broadcast als Code 1 + 2·Programm
  (Byte 4). Nur bei Automatik relevant.
- **Phase** (Broadcast Byte 1) ist der wirksame Zustand: 01 = Heizen/Tag, 00 = Absenken/Nacht,
  04 = aus (Standby, Sommer, Hand). In Automatik wechselt sie mit dem Zeitprogramm
  (Korrektur der test4-Hypothese: keine Modusanzeige).
- Der Vorlauf-Sollwert (`10 03`, Wort 3) stand in Heizen, Absenken, Sommer und Hand auf 0
  (vermutlich Heizgrenze, nicht geprüft); als Modusanzeige ungeeignet.
- **Behaglichkeit** −1,5 K → +1,0 K (ca. 18:01:25): `21 0B` Wort 1 wechselt von `f1 ff` auf `0a 00`
  (vorzeichenbehaftet, 0,1 K). `11 03` bleibt gleich; in `10 03` steigt Wort 3 auf 27,5 °C,
  Wort 6 von 20,5 auf 23,0 °C.
- Alle Wechsel kamen von der FB; kein Schreibtelegramm `06 23` im Log (`06 21 02 09 01` um :00
  sind Lesezugriffe).
- Der Schlüssel in `D0 15` (FB2) läuft pro Änderung um 1 hoch; nach dem Zurückstellen springt der
  Controller auf `a2`.

## Offen / Testplan

Nicht belegt: Schreiben der Modi 1–5 und der Uhrenprogramme 2/3 per `06 23` (nur Wert 0 bei HK1
getestet); Verhalten von HK1 in den Modi 2–5 (nur HK2 gemessen).

1. `03-50` je Modus per Controller schreiben (`P03_50_HK1_set` / `P03_50_HK2_set`), 3 Zyklen
   beobachten: übernimmt `11 02`/`11 03` den Wert, und zeigt FB Block `20` ihn an?
2. Uhrenprogramm 2/3 per Schreiben: kein Parameter bekannt; per `20 0B`-Byte 2 beobachten,
   ob ein separater Selektor existiert (FB-Änderung mit Log vergleichen).
3. Erst danach Home-Assistant-`select`-Entitäten mit Lesepfad `Status2a`/`Status3a`
   und Schreibpfad `P03_50_*_set` anlegen.
