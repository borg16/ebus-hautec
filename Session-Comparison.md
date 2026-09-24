# Vergleich der zuletzt beobachteten Einstellungen

Basis ist `ste-output/Parameter.md`; Einzelbelege mit Zeitpunkten und Logzeilen stehen in [Evidence.md](comparison-output/Evidence.md). Reproduzierbar mit `python3 scripts/compare_session.py`.

114 STE-Datensätze sind zugeordnet: 28 numerisch abweichend, 85 gleich und eine gesondert zu behandelnde Passwortanzeige. Für 103 weitere STE-Datensätze fehlt eine zugeordnete Beobachtung. „Zuletzt“ bezeichnet den letzten beobachteten Wert je Quelle, keine gemeinsame Momentaufnahme. Das Protokoll endet am 23.09.2026 um 11:50:08.

Die Zuordnung der Kontextvarianten zu Heizkreis 1/2 ist abgeleitet. FB-Werte sind Werte der Kommunikation mit den Bediengeräten und nicht durchgehend spätere direkte Controller-Lesungen.

| TEM | Bezeichnung / Kontext | STE | Zuletzt beobachtet | Quelle |
|---|---|---:|---:|---|
| 03-50 | Betriebswahl Heizung und Brauchwasser / Heizkreis 1 (abgeleitet) | 1  | 4  | Master |
| 03-50 | Betriebswahl Heizung und Brauchwasser / Heizkreis 2 (abgeleitet) | 1  | 4  | Master |
| 03-58 | Behaglichkeit / Heizkreis 2 (abgeleitet) | -1 K | 0 K | FB 91 |
| 03-51 | Sollwert Raumtemperatur Heizen Tag normal / Heizkreis 1 (abgeleitet) | 20.5 °C | 22 °C | FB 90 |
| 03-51 | Sollwert Raumtemperatur Heizen Tag normal / Heizkreis 2 (abgeleitet) | 20.5 °C | 22 °C | FB 91 |
| 03-53 | Sollwert Raumteperatur Heizen Nacht / Heizkreis 2 (abgeleitet) | 18 °C | 10 °C | FB 91 |
| 05-51 | Sollwert Warmwassertemperatur / Heizkreis 2 (abgeleitet) | 10 °C | 48 °C | FB 91 |
| 03-10 | Steilheit Kennlinie / Heizkreis 1 (abgeleitet) | 0.3  | 0.4  | FB 90 |
| 03-10 | Steilheit Kennlinie / Heizkreis 2 (abgeleitet) | 0.3  | 0.4  | FB 91 |
| 07-08 | Vorlauf Maximaltemperatur TV / Heizkreis 2 (abgeleitet) | 45 °C | 55 °C | Master |
| 03-21 | Heizgrenze bei Tagbetrieb / Heizkreis 1 (abgeleitet) | 16 °C | 25 °C | Master |
| 03-21 | Heizgrenze bei Tagbetrieb / Heizkreis 2 (abgeleitet) | 16 °C | 20 °C | Master |
| 03-01 | Fusspunkttemperatur / Heizkreis 1 (abgeleitet) | 20 °C | 22 °C | FB 90 |
| 03-01 | Fusspunkttemperatur / Heizkreis 2 (abgeleitet) | 20 °C | 22 °C | FB 91 |
| 03-35 | Kühlgrenzenabstand / Heizkreis 1 (abgeleitet) | 10 °C | 5 K | FB 90 |
| 04-30 | Multifunktionsusgang 1 / Einstellebene 4, Globale Einstellungen | 1  | 0  | Master |
| 05-03 | Nachlaufzeit Brauchwasserbereitung / Einstellebene 5, Brauchwasserbereitung | 3 min | 1 min | Master |
| 05-13 | Reduktion Sollwert TBO / Einstellebene 5, Brauchwasserbereitung | 15 K | 0 K | Master |
| 07-05 | Heizkreistyp / Heizkreis 1 (abgeleitet) | 2  | 0  | Master |
| 07-05 | Heizkreistyp / Heizkreis 2 (abgeleitet) | 0  | 3  | Master |
| 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung / Heizkreis 1 (abgeleitet) | 0 h | 2 h | Master |
| 07-14 | Heizkreisfunktion im Kühlbetrieb / Heizkreis 1 (abgeleitet) | 0  | 3  | Master |
| 07-14 | Heizkreisfunktion im Kühlbetrieb / Heizkreis 2 (abgeleitet) | 0  | 3  | Master |
| 09-07 | WEZ Typ / Einstellebene 9, WE Einstellungen Wärmepumpe | 5  | 6  | Master |
| 09-21 | WE Abschaltdifferenz / Einstellebene 9, WE Einstellungen Wärmepumpe | 5 K | 3 K | Master |
| 10-31 | WE Maximaltemperatur / Einstellebene 9, WE Einstellungen Wärmepumpe | 70 °C | 60 °C | Master |
| 15-10 | Heissgas Maximaltemperatur / Einstellebene 9, WE Einstellungen Wärmepumpe | 125 °C | 130 °C | Master |
| 10-31 | WE Maximaltemperatur / Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 70 °C | 68 °C | Master |

## Einschränkungen bei einzelnen Werten

- **05-51, HK 2:** Die direkte Master-Lesung zeigt zuletzt 50 °C (11:24:23), die spätere FB-91-Kommunikation 48 °C (zuletzt 11:44:20). Beide weichen vom STE-Wert 10 °C ab. 48 °C ist kein zweifelsfrei bestätigter abschließender Controller-Wert.
- **03-58, HK 2:** Die Master-Lesung zeigt noch −1 K. Die spätere FB-Antwort zeigt 0 K. Die Zuordnung dieses FB-Felds ist aus dem Vergleich der Telegramme abgeleitet.
- **03-50:** Die Codes ändern sich von 1 auf 4. Die STE-Auswahlliste und die beobachteten Bus-Grenzen passen nicht vollständig zusammen; deshalb wird Code 4 hier nicht mit einem Betriebsartnamen gleichgesetzt.
- **04-40:** STE enthält 161, die Busanzeige 0. Ein möglicherweise maskiertes Passwort ist kein Nachweis einer Passwortänderung und wird nicht unter den 28 Abweichungen gezählt.
- Eine Antwort mit ungültiger CRC (Logzeile 5033) wurde verworfen. Für zugeordnete Schreibselektoren liegt kein bestätigter letzter Schreibzugriff nach der letzten zugehörigen Lesung vor.

Zwischenzeitliche Änderungen wurden nicht mit dem Endstand verwechselt: Beispielsweise sind 05-05, 09-26 (WP), 09-34 (WP), 09-35 (WP), 09-11 (EH), 11-03 (WE1) und 05-51 (HK 1) zuletzt wieder bzw. weiterhin gleich dem STE-Wert.
