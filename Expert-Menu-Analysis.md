# Expert-Modus und Menüzugriffe in complete.log

Die zeitliche Zuordnung stützt eine **periodisch erneuerte Expert-Sitzung während
der Bedienung höherer Einstellmenüs**. Sie belegt nicht, dass das Lesen eines
anderen Menüs die Sitzung beendet. Die Verbindung von `0000 / 5100` zur
Freischaltung stammt aus der separat nachvollzogenen Bedienung, siehe
[Write-Analysis.md](Write-Analysis.md); hier wird ihre zeitliche Korrelation
im Mitschnitt untersucht.

## Schaltungen und Rückmeldung

Gezählt wurden CRC-geprüfte `01 → 10 / 06 23`-Telegramme mit Selektor `0000`:

- 50 quittierte Schreibungen des Wertes `51 00` (81).
- Zwei weitere Übertragungen desselben Wertes ohne aufgezeichnetetes ACK,
  jeweils unmittelbar wiederholt (7792/7793 und 9837/9839).
- Vier quittierte Schreibungen von `e8 03` (1000).

Nach zehn ausgewählten `5100`-Schreibungen folgt eine Abfrage `06 21 / 0001`.
Diese liefert TEM **04-43** mit Wert **1**. Nach allen vier `e803`-Schreibungen
liefert dieselbe Abfrage **0**. Die Antwort folgt jeweils etwa 250 ms später.
Der Benutzer hat anschließend bestätigt, dass **04-43 den Expert-Modus anzeigt**.
Die Zuordnung 0 = aus und 1 = ein ist damit bestätigt.

| Schreibzeile | Uhrzeit | Wert | Rückmeldezeile | 04-43 |
|---:|---|---|---:|---:|
| 4216 | 09:46:44.847 | e803 | 4217 | 0 |
| 4223 | 09:46:56.270 | 5100 | 4224 | 1 |
| 7545 | 10:38:40.990 | e803 | 7546 | 0 |
| 7555 | 10:38:49.710 | 5100 | 7556 | 1 |
| 8509 | 10:55:44.921 | e803 | 8510 | 0 |
| 8518 | 10:56:00.655 | 5100 | 8519 | 1 |
| 8688 | 11:00:26.267 | e803 | 8689 | 0 |
| 8695 | 11:00:34.626 | 5100 | 8696 | 1 |

Das beweist nicht, dass `e803` einen zuvor aktiven Expert-Zugang abschaltet:
unmittelbare Statusmessungen vor diesen Schreibungen fehlen. Auch ein anderer
Zugangsversuch oder eine andere Sitzungsfunktion ist damit vereinbar.

## Zusammenhang mit den Einstellmenüs

| Expert-Bedienphase, ungefähr | Danach bzw. dabei gelesene Menüs |
|---|---|
| 09:16–09:28 | a3 → a4 → a5 → a6 → a7 |
| 09:47–09:52 | aa → ab |
| 10:38–10:43 | a9 |
| 10:44–10:47 | aa → ab |
| 10:56–10:59 | a5 → a7 |
| 11:00–11:01 | a7 |
| 11:08–11:10 | a7, Grund- und Zusatzkontext |
| 11:17–11:18 | a3 → a7 |

Während längerer Phasen wird `5100` im Minutenrhythmus gesendet: 24 Abstände
zwischen aufeinanderfolgenden quittierten `5100`-Schreibungen liegen zwischen
58,924 und 61,001 Sekunden. Die übrigen Abstände umfassen kurze Startsequenzen,
Phasenwechsel und lange Pausen; der Takt gilt also nicht für die ganze Sitzung.

Besonders deutlich ist der Anfang:

- 09:16:00.991 Freischaltung (2468), danach Status 1 (2469).
- 09:16:02.194 erneute Freischaltung (2470), dann Menü a3 (2473/2474).
- 09:16:55.617 und 09:17:55.617 weitere Freischaltungen (2493/2516),
  **ohne irgendeine vollständige Parameter-Leseantwort 01 → 15 dazwischen**.
- Danach wiederholte Erneuerungen während a3, a4, a5, a6 und a7.

Damit ist die Wiederholung nicht allein durch das Betreten eines Menüblocks
erklärbar. Sie passt zu einem Timer der Bedienung. Ob und nach welcher Zeit
der Controller die Freigabe ohne Erneuerung löscht, lässt sich daraus noch
nicht bestimmen. Insbesondere ist der Erneuerungsabstand nicht automatisch
die Timeoutdauer.

Zwischen höheren Menüs ist keine eigene Freischaltung zwingend beobachtet:
Zum Beispiel erfolgt der Wechsel a4 → a5 um 09:20:44.728 (2596), zwischen
den Freischaltungen um 09:19:56.711 und 09:20:55.635.

Nach dem Verlassen dieser Phasen werden überwiegend die unteren Menüs gelesen
und die Minuten-Erneuerungen hören auf. Dadurch sind zwei Erklärungen im
Mitschnitt nicht trennbar: expliziter Verlust durch einen Zugriff auf ein
anderes Menü oder Ablauf nach ausbleibender Erneuerung. Eine unmittelbar
um einen solchen Zugriff herum gemessene Statusänderung 1 → 0 fehlt.

## Verzeichnisblöcke sind keine nachgewiesenen Zugangsschalter

Alle 28 `06 20`-Blöcke werden siebenmal gelesen. Jeder Block liefert über
alle sieben Runden dieselben acht Bytes. Die erste Runde beginnt bereits
um 08:56:56.780 (1208), also vor der ersten im Mitschnitt beobachteten
`5100`-Freischaltung um 09:16:00.991.

Block `14` enthält unverändert `00 00 00 84 08 0b 0b 88`: Für Menü a7
werden acht Plätze angekündigt. Das Verzeichnis kann folglich Einstellmenüs
ankündigen, ohne damit deren aktuelle Lesefreigabe zu beweisen. Der Zugangszustand
vor Mitschnittbeginn ist unbekannt; aus der frühen Runde allein folgt keine
sichere Aussage über eine bereits zuvor erteilte Freischaltung.

Die Freischaltungen werden nicht vor jeder `06 20`-Abfrage gesendet. Es zeigt
sich auch keine Änderung der Verzeichnisantworten an den beobachteten
Freischaltzeitpunkten. Zu unterscheiden sind daher der **Verzeichnisblock**
(acht Menüdeskriptoren) und das **Einstellmenü** (erstes Byte bei `06 21`).

## Konsequenz für die nächste Messung

Am aussagekräftigsten ist nun: frisch freischalten, **04-43 über `0001` lesen**,
genau eine verdächtige Menüabfrage ausführen und sofort 04-43 sowie a7/04
erneut lesen. Gegenprobe mit identischer Wartezeit ohne die Menüabfrage.
Dabei denselben Bus-Absender verwenden. Ein zusätzlicher Versuch ohne
Minuten-Erneuerung bestimmt den tatsächlichen Timeout.

Die vollständige Liste der 56 Übertragungen samt benachbarten Lesezugriffen
steht in [menu-output/Expert-Events.md](menu-output/Expert-Events.md).
