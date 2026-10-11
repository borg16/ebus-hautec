# Betriebsart der Heizkreise (Versuch test3, 2026-10-11)

Rohdaten: `ebusd.test3.log`. Auswertung: `scripts/analyze_operating_mode.py ebusd.test3.log`.

Ablauf: Start HK1 Standby / HK2 Uhrenprogramm 1; 22:03 HK2 → Standby; 22:18 HK1 → Programm 1;
22:22 HK2 → Programm 1. Der Controller fragt jede Bedieneinheit alle 80 s ab.

## Lesen

| Quelle | Feld | Standby | Uhrenprogramm 1 |
|---|---|---|---|
| FB-Antwort `10 0A / 20 <Block>` (FB1 Block `01`, FB2 Block `0B`) | Byte nach Tag/Nacht/WW-Soll (`Betriebsart`) | `00` | `01` |
| Broadcast `10 0A 11 02` (HK1) | `Status2a.b3` / `b4` | `04` / `00` | `01` / `01` |
| Broadcast `10 0A 11 03` (HK2) | `Status3a.b5` / `b6` | `04` / `00` | `01` / `01` |

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

- **23:12:51.742** `31 → 10 / 06 23 04 01 00 00 00` (ACK `00`): Schreibtelegramm von ebusd
  (Quelle `31`) = `P03_50_HK1_set` mit Wert 0 (Standby). Im Log ist es der einzige Schreibzugriff;
  die Änderung kam also über ebusd, nicht (nur) über die Bedieneinheit.
- **23:13:04** Beim nächsten 80-s-Poll antwortet FB1 auf `D0 14` mit `50 01` (statt `C0 00` oder
  `40 01`). Der Controller sendet daraufhin `10 → 90 / 10 0A 0E 31 01 …` und `… 0E 30 01 …`
  (Controller → FB, Schreibrichtung). Der Block `30 01` enthält Tag 22 °C, Nacht 18 °C,
  WW 50 °C, **Betriebsart `00`** und den neuen Schlüssel `ca 03`. Beim erneuten `D0 14` folgt `C0 00`.
- Die Einstellung bleibt danach bis 23:24 stabil, FB1 setzt sie nicht zurück.
  Der Schreibweg `06 23` für 03-50 funktioniert somit und wird zur FB durchgereicht.
- Broadcast `11 02`: `04 00 00 01` (Standby), erstmals sichtbar 23:13:23. Das Log beginnt erst
  um 23:12:43, der Zustand davor ist nicht erfasst; die Verzögerung der Übernahme ist offen.
- Korrektur zu test3: HK2 (ohne Eingriff, FB2 unverändert) zeigt in `11 03` jetzt `00 01 00 01`
  statt `01 01 00 01`, Soll in `10 03` 19,8 statt 24,9 °C. `b3`/`b5` ist daher
  nicht nur der Modus, sondern wahrscheinlich die aktuelle Programmphase (04 = Standby,
  01 = Tag, 00 = Absenkung; Hypothese, Uhrzeit Sonntag 23:12). `b4`/`b6` (00/01) trennt
  Standby von Programm.

## Offen / Testplan für Schreiben und weitere Modi

Nicht belegt: Werte für Normal (2), Reduziert (3), Sommer (4), Hand (5) sowie ob `b3` den
wirksamen Modus oder die Zeitprogrammphase anzeigt (`04` bei Standby weicht vom 03-50-Wert 0 ab).

Test (je Heizkreis, Wechsel mit ≥ 3 min Abstand, `ebusd.log` mitschneiden):

1. Modi 2–5 an der FB einstellen; `Betriebsart` und `11 02`/`11 03` je Modus notieren.
2. `03-50` per Controller schreiben (`P03_50_HK1_set` / `P03_50_HK2_set`, `06 23`),
   z. B. `ebusctl write -c controller P03_50_HK1_set 0`. Danach 3 Zyklen beobachten:
   übernimmt `11 02`/`11 03` den Wert, bleibt er, und zeigt die FB (Block `20`) ihn an?
3. Falls die FB den Wert zurücksetzt (`40 <Block>` nach dem Schreiben), ist Schreiben nur über
   die FB-Seite möglich und für Home Assistant nicht nutzbar.
4. Erst nach positivem Ergebnis Home-Assistant-`select`-Entitäten mit Lesepfad
   `Status2a`/`Status3a` und Schreibpfad `P03_50_*_set` anlegen.
