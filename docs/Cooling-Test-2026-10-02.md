# Ausbleibender Kühlbetrieb am 02.10.2026

Quelle: `ebusd.2.log`, 17:53:23.895–18:04:46.765, Log-Zeiten Europe/Berlin,
und das vom Betreiber bereitgestellte Leistungsdiagramm. Offline-Auswertung;
keine Anlagenparameter verändert.

## Ergebnis

Die Daten sprechen deutlich für eine **Heizanforderung aus HK1**, die zum
beobachteten Lauf der Abluftwärmepumpe passt. Die auffälligste Einstellung
ist **03-58 Behaglichkeit HK1 = +3 K**, gegenüber 0 K in HK2. Zusätzlich
stehen in beiden übertragenen Heizgrenzenblöcken **17 °C für Tagbetrieb**
und **16 °C für Absenkbetrieb**. Die vom Betreiber genannten 16 °C sind
damit im Mitschnitt nicht die Tag-Heizgrenze.

Die Anleitung des verwandten Hautec HSC 6001 WPC beschreibt, dass sich
die wirksame Heizgrenze mit Änderungen durch Betriebswahl und Behaglichkeit
verschiebt; der Abstand zum Normal-Raumsoll bleibt erhalten.
[Herstelleranleitung, Seite 26](https://www.manualslib.de/manual/804180/Hautec-Hsc-6001-Wpc.html?page=26).
Die lokale STE-Beschreibung zu 03-35 legt die Kühlgrenze als aktuelle
Heizgrenze plus Kühlgrenzenabstand fest.

Übertragen auf den vorliegenden Tagbetrieb ergibt sich für HK1:

- wirksame Heizgrenze: 17 °C + 3 K = **20 °C**;
- Kühlgrenze: 20 °C + 2 K = **22 °C**;
- gemittelter Außenwert: **19,1 °C**, somit unter beiden Grenzen.

Das ist eine durch Daten und verwandte Herstellerdokumentation gestützte
Erklärung, keine direkte Rücklesung einer intern berechneten Kühlgrenze
dieser Firmware. Der genaue Vorrang zwischen Heiz- und Kühlanforderungen
ist im Log nicht als eigener Zustand ausgewiesen.

## Übertragene Einstellungen

Die Zuordnung folgt den bereits dokumentierten FB-Blöcken und
`scripts/compare_session.py`. FB1/HK1 und FB2/HK2 sind die bestehende
logische Projektzuordnung, keine Aussage über getrennte physische Heizkreise.

| Einstellung | HK1 | HK2 | Logzeilen HK1/HK2 |
|---|---:|---:|---|
| 03-58 Behaglichkeit | +3 K | 0 K | 58 / 159 |
| 03-43 Kühltemperatur | 21 °C | 21 °C | 58 / 159 |
| 03-35 Kühlgrenzenabstand | 2 K | 2 K | 58 / 159 |
| 03-51 Raumtemperatur Tag | 22 °C | 22 °C | 59 / 160 |
| 03-53 Raumtemperatur Nacht | 18 °C | 10 °C | 59 / 160 |
| 03-21 Heizgrenze Tag | 17 °C | 17 °C | 494 / 203 |
| 03-02 Heizgrenze Absenkbetrieb | 16 °C | 16 °C | 494 / 203 |

Beispiel HK1: `31 01 1e 00 d2 00 02 00 14 00 00 00 00 00`:
`1e00` = +3,0 K, `d200` = 21,0 °C, `1400` = 2,0 K.
Heizgrenzenblock: `30 03 00 ff aa 00 a0 00 00 00 00 00 18 90`:
`aa00` = 17,0 °C, `a000` = 16,0 °C.

## Betriebswerte und zeitlicher Verlauf

| Befund | Erste relevante Logzeit | Zeile |
|---|---|---:|
| 01-21 HK2 wechselt auf −100 %, bleibt dort | 17:53:32.013 | 35 |
| 01-96 Anlagensoll wechselt von 0 auf 28 °C | 17:53:35.387 | 42 |
| 01-07 WP-Soll wechselt von 0 auf 38 °C | 17:53:45.944 | 89 |
| Broadcast 10 02: HK1-Sollkandidat 28,7 °C | 17:54:36.018 | 291 |
| FA1 meldet 50 % | 17:54:37.005 | 298 |
| Broadcast 10 03: HK2-Soll 21 °C | 17:54:45.924 | 320 |
| 01-09 WE1 direkt 100 % | 17:56:07.321 | 604 |
| 02-20, Selektor 09 01: 19,1 °C | 18:00:00.323 | 1417 |
| FA1 meldet 100 % statt 50 % | 18:03:31.325 | 2097 |

01-96 bleibt bei 28 °C, 01-07 bei 38 °C; die zweite Abfragevariante
bestätigt jeweils denselben Wert. Der HK1-Sollkandidat steigt später auf
28,8 °C; HK2 bleibt bei 21 °C. Die 21-°C-Linie im Screenshot beschreibt
also nicht den gemeinsamen WP-Sollwert. Der Unterschied von 10 K zwischen
01-96 und 01-07 ist beobachtet, seine genaue Ursache hier nicht bestimmt.

Die 102 gültigen WE1-Parameterantworten nach Expert-Freischaltung melden
jeweils 100 %. Davor liefern 31 Antworten `ff1f` (nicht verfügbar), nicht
0 %. Das darf nicht als Anforderungsanstieg erst um 17:56 gelesen werden.

00-07 wird diesmal tatsächlich als Istwert abgefragt: 24,6–25,8 °C.
00-08 liegt bei 23,2–23,3 °C. Der Speicher-Broadcast liegt ab 17:54:12
bei rund 48,6 °C, die Warmwasserbits in 11 00/11 01 bleiben in den
vorliegenden Stichproben aus. Das stützt die Betreiberangabe, dass keine
Warmwasserbereitung läuft. Der steigende Vorlauf und die Heizanforderung
passen zur Raumheizung durch die beobachtete Abluftwärmepumpe.

Zwischen erster FA1-Meldung 50 % und 100 % liegen 8 min 54,3 s, passend
zur früher dokumentierten 9-min-Stufenverzögerung. Das ist keine aktuelle
Rücklesung von 09-34 und kein Beweis für einen zweiten laufenden Verdichter.
HK2 bleibt bei −100 %, während es im vorherigen Kühlversuch cool6 bei
aktiver Kühlanforderung +100 % meldete. Ein logischer Stufenwert ersetzt
keine Messung der elektrischen Freigabekette.

## Gezielt prüfbarer nächster Schritt

Zuerst **03-58 in HK1 auf 0 K zurücknehmen** und die Sollwerte erneut
beobachten. Zusätzlich **03-21 Tag-Heizgrenze** in beiden Kontexten
prüfen; wenn die beabsichtigte Heizgrenze 16 °C ist, muss dieser Parameter
entsprechend stehen, nicht nur 03-02. Bei 16 °C, Behaglichkeit 0 K und
Abstand 2 K ergibt die dokumentierte Logik eine Kühlgrenze von 18 °C.

Als Bestätigung sollte die hohe HK1-/WP-Heizanforderung verschwinden;
01-96, 01-07 und 01-21 HK2 gemeinsam beobachten. Die Umschaltung kann
zusätzlich durch Lauf-/Stillstandszeiten verzögert sein. Eine erfolgreiche
Kühlumschaltung nach der Korrektur liegt in diesem Mitschnitt noch nicht vor.

## Datenqualität und Grenzen

2331 Zeilen; 2260 vollständige Mastertelegramme mit gültiger CRC,
71 kurze Fragmente. 1621 Transaktionen besitzen gültige Antwort-CRC und
ACK; bei 205 weiteren gültigen Mastertelegrammen ist die Antwort/Quittierung
unvollständig oder ungewöhnlich. Parameterwerte stammen nur aus gültigen
Antworten, die aufgeführten FB-Einstellungsblöcke sind quittiert.

Am Beginn stehen zwei FE-01-Texte `5710ERR010` und `5710ERR011`
(Zeilen 3 und 40), anschließend umfangreiche FB-Initialisierungsblöcke.
Die genaue Bedeutung dieser Texte und ein möglicher Neustart sind nicht
geklärt. Spätere Fehlergerät/-code-Felder in 08 02 sind 0/0. Der Beginn
enthält außerdem vorübergehende Nullwerte; er ist nicht durchgehend als
eingeschwungener Betrieb zu lesen.

SHA-256: `864ccc2f280fd2cf51580cec8921a5eb83c0a00d53f8b574683b55bcbaa59e17`.
