# Schreibbefehle in complete.log

## Generierte Schreibdefinitionen ab 03-00

Der Generator `scripts/analyze_master_log.py` erzeugt `_set`-Modelle für alle
205 numerisch dekodierbaren Parameter-/Kontextpaare ab 03-00, einschließlich
der nur im Scan belegten Zugriffe. Zusammen mit den 56 bisherigen Schreibmodellen
unterhalb 03-00 ergeben sich 261 Definitionen. Ziel ist `10`, Dienst `06 23`;
der vollständige Leseselektor und die jeweilige Wertkodierung bleiben erhalten.
Die Definition allein belegt noch keine Annahme durch den Regler.

Für 03-07 wird `SIN / 10` ohne Einheit verwendet: Die Antwort nennt die Grenze
100, der STE-Katalog die Grenze 10. Diese Skalierung ist abgeleitet.
Acht Kurzantwort-Zugriffe bleiben ohne Schreibdefinition: 03-61, 03-62 und
03-63 jeweils in HK1/HK2 sowie 05-61 und 05-64. Die sechs Antwortbytes enthalten
keinen normalen Zwei-Byte-Wert; ihr Schreibformat ist bisher unbekannt.
Die vollständige Ausnahmeliste steht in
[master-output/Parameter.md](master-output/Parameter.md#schreibdefinitionen-ab-03-00).

Die Erweiterung wurde durch TypeSpec-Kompilierung, Prüfung der erzeugten
CSV-Zieladressen/Selektoren/Werttypen und Offline-Wiedergabe der Leseantworten
geprüft. Es wurden dafür keine Werte am Regler geschrieben.

## Ergebnis

In `complete.log` sind **131 Übertragungen mit Dienst `06 23` von Quelle `01`
an Ziel `10`** enthalten. Alle 131 haben eine gültige Master-CRC. Bei 128
steht anschließend ACK `00`; drei Zeilen enden nach der CRC und werden kurz
darauf mit demselben Inhalt vollständig wiederholt (Zeilen 7792/7793,
9837/9839 und 10270/10272). Es sind daher nicht 131 verschiedene Änderungen.

Es gibt **26 unterschiedliche Selektoren**. Davon lassen sich 24 über die
entsprechenden Leseantworten 19 unterschiedlichen TEM-Kennungen zuordnen.
Bei 23 Selektoren bzw. 18 TEM-Kennungen ist mindestens einmal auch der
geschriebene Wert in einer folgenden Leseantwort bestätigt, ohne dass vorher
ein weiterer Schreibauftrag für denselben Selektor auftaucht: insgesamt
48 solche Schreiben/Lesen-Paare.

Damit ist die zuvor in [Master-Analysis.md](Master-Analysis.md) offene Frage
geklärt: **Lesen erfolgt hier an Slave `15`, Schreiben an Master `10`.** Ein
Filter auf Telegramme `01 -> 15` entfernt die Schreibaufträge.

## Nachgewiesenes Format

Kurze Variante:

```text
Lesen:    01 15 06 21 02 [Menü Index]                 CRC ACK [Antwort] CRC ACK
Schreiben:01 10 06 23 04 [Menü Index] [Wert-Lo Wert-Hi] CRC ACK
```

Erweiterte, ebenfalls beobachtete Variante:

```text
Lesen:    01 15 06 21 04 [Menü Index|80 10 00]                 CRC ACK [Antwort] CRC ACK
Schreiben:01 10 06 23 06 [Menü Index|80 10 00] [Wert-Lo Wert-Hi] CRC ACK
```

Der Lese-Selektor wird beim Schreiben unverändert übernommen und um zwei
Wertbytes ergänzt. Der Zusatz `10 00` ist weiterhin ein Kontext-/Instanzselektor;
er ist nicht der geschriebene Wert. Die Zuordnung dieses Kontexts zur physischen
Anlage bleibt offen.

### Expert-Modus

Die Sitzung wurde zusätzlich mit `ebusctl` nachvollzogen. Die Schreibsequenz

```text
(01) 10 06 23 04 00 00 51 00
```

versetzt den Controller in den Expert-Modus. `00 00` ist damit in dieser
Controller-Version kein bloßer Keepalive-Selektor. Erst nach diesem Schreiben
werden Expert-Einsteller wie `05-05` (Funktionsweise Ladepumpennachlauf) sichtbar.
Im Mitschnitt erscheint die vollständige quittierte Übertragung beispielsweise
in [complete.log:2468](input/complete.log#L2468):

```text
01 10 06 23 04 00 00 51 00 13 00
```

Die wiederkehrenden Schreibungen mit `00 00 51 00` halten den Expert-Zugang
offen. Die Varianten mit `00 00 E8 03` gehören zum selben Sitzungsmechanismus;
ihre genaue Zeit-/Statusbedeutung ist noch nicht getrennt bestimmt.

Der einzelne Befehl mit Selektor `04 AD 00 40` bleibt davon unabhängig. Er ist
weiterhin als separater, nicht vollständig zugeordneter Adressierungsweg geführt.

### Beispiel: Warmwasser-Solltemperatur 05-51 auf 30 °C

[complete.log:3512](complete.log#L3512), 09:35:45.310:

```text
01 10 06 23 04 0B 03 2C 01 4A 00
```

| Bytes | Bedeutung |
|---|---|
| `01 10` | Quelle 01, Ziel 10 |
| `06 23` | Schreibdienst |
| `04` | vier Nutzdatenbytes |
| `0B 03` | derselbe Selektor wie beim Lesezugriff auf 05-51 |
| `2C 01` | Little-Endian 300, bei diesem Parameter 30,0 °C |
| `4A` | gültige Master-CRC |
| `00` | ACK |

297 ms später liefert die Leseantwort in
[complete.log:3514](complete.log#L3514) die Nutzdaten:

```text
B3 42 8D 02 BC 02 64 00 2C 01
```

Das ist TEM `05-051`, Typ `8D`, Einheit `02`, Maximum 70 °C, Minimum 10 °C,
Wert **30 °C**. Später wird derselbe Parameter mehrfach zwischen 30 und 50 °C
umgestellt und jeweils passend zurückgelesen.

### Weitere eindeutige Beispiele

| Schreibzeile → Lesezeile | TEM | Selektor | Wertbytes | Dekodierter Wert |
|---|---|---|---|---|
| 1949 → 1952 | 03-58 Behaglichkeit | `01 02` | `05 00` | +0,5 K |
| 1963 → 1964 | 03-58 Behaglichkeit | `01 02` | `FB FF` | −0,5 K |
| 4458 → 4459 | 03-51 Raum-Solltemperatur Tag | `0B 00` | `2C 01` | 30 °C |
| 8189 → 8190 | 03-21 Heizgrenze Tag | `0B 06` | `FA 00` | 25 °C |
| 7750 → 7751 | 09-35 Schaltdifferenz zweite Stufe | `A9 0D` | `E2 FF` | −3 K |
| 10301 → 10302 | 03-51, erweiterter Kontext | `0B 80 10 00` | `DC 00` | 22 °C |

Das letzte Beispiel lautet vollständig:

```text
01 10 06 23 06 0B 80 10 00 DC 00 46 00
```

## Alle beobachteten Schreibselektoren

Die Zahlen in der Wertspalte sind **unskalierte** Little-Endian-Werte; bei
negativen Parametern als vorzeichenbehaftetes 16-Bit-Wort interpretiert.
„Anzahl“ zählt Zeilen einschließlich Wiederholungen und der drei Zeilen ohne ACK.

| Selektor | TEM | Anzahl | Beobachtete Rohwerte | Erste Schreibzeile |
|---|---|---:|---|---:|
| `01 02` | 03-58 | 8 | 5, 10, 0, −5 | 1949 |
| `00 00` | Expert-Modus-Freischaltung und Sitzungserhaltung | 56 | 81, 1000 | 2468 |
| `A3 00` | 03-11 | 1 | 200 | 2522 |
| `A5 05` | 05-05 | 1 | 0 | 2671 |
| `0B 03` | 05-51 | 6 | 300, 500 | 3512 |
| `01 80 10 00` | 03-50 | 13 | 2, 3, 4, 5, 6, 1 | 3927 |
| `AA 04` | 09-11, Elektro-Zusatzheizung | 1 | 10 | 4313 |
| `0B 04` | 03-10 | 2 | 100, 40 | 4446 |
| `0B 00` | 03-51 | 3 | 300, 220 | 4458 |
| `21 03` | 01-40 | 2 | 1, 0 | 5518 |
| `21 05` | 01-54 | 13 | 1, 0 | 5572 |
| `04 AD 00 40` | offen; separater Adressierungsweg | 1 | 11 | 5609 |
| `21 80 10 00` | 01-20, erweiterter Kontext | 2 | 0, 1 | 7287 |
| `A9 03` | 09-07, Wärmepumpe | 1 | 6 | 7638 |
| `A9 0A` | 09-26, Wärmepumpe | 1 | 100 | 7699 |
| `A9 0C` | 09-34, Wärmepumpe | 1 | 90 | 7743 |
| `A9 0D` | 09-35, Wärmepumpe | 1 | −30 | 7750 |
| `AB 05` | 11-03 | 1 | 70 | 7906 |
| `01 00` | 03-50 | 9 | 2, 4, 3, 1 | 8059 |
| `0B 06` | 03-21 | 1 | 250 | 8189 |
| `A7 04` | 07-05 | 1 | 0 | 8723 |
| `A7 06` | 07-14 | 1 | 3 | 8735 |
| `A7 84 10 00` | 07-05, erweiterter Kontext | 2 | 0, 3 | 9218 |
| `A7 86 10 00` | 07-14, erweiterter Kontext | 1 | 3 | 9246 |
| `0B 84 10 00` | 03-10, erweiterter Kontext | 1 | 40 | 10292 |
| `0B 80 10 00` | 03-51, erweiterter Kontext | 1 | 220 | 10301 |

Für `21 80 10 00` sind die Schreibbefehle quittiert und die TEM-Kennung aus
früheren Leseantworten bekannt; nach den beiden Schreibbefehlen gibt es hier
keine erneute Leseantwort für genau diesen Selektor. Bei schnellen Folgen von
Betriebswahl-Änderungen wird teilweise nur der zuletzt geschriebene Wert
zurückgelesen. Das ist kein Nachweis, dass zwischenzeitliche Befehle fehlschlagen.

## Konsequenz für TypeSpec

Ein belegtes Schreibmodell für 05-51 hat beispielsweise diese Form:

```typespec
@write
@zz(0x10)
@id(0x06, 0x23, 0x0b, 0x03)
model P05_051_0B03_set {
  wert: Celsius10;
}
```

Es gibt keine zusätzliche Slave-Nutzlast beim quittierten Master-Master-
Schreiben. Länge, Transport-CRC und ACK gehören daher auch hier nicht in
`@id` oder ein Antwortmodell. Die beobachtete Quelle 01 muss nicht als
`@qq(0x01)` festgeschrieben werden.

Die unmittelbar passende Rücklesung belegt die Übernahme während der Sitzung.
Sie belegt noch nicht die Speicherung über einen Neustart hinweg. Ebenso
ist die Übertragbarkeit des Schreibschemas auf bisher nur gelesene Parameter
noch kein Nachweis ihrer Schreibbarkeit. Die 56 Aufträge an `00 00` haben
ein auffälliges Muster mit Wert 81 oft etwa einmal pro Minute; eine genaue
Passwort-/Freischaltfunktion oder deren Notwendigkeit ist damit noch nicht
entschlüsselt.
