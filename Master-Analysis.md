# Controllerzugriffe aus master.log

Ergänzung: Das später bereitgestellte `complete.log` enthält die zuvor
weggefilterten Schreibtelegramme `01 -> 10`, Dienst `06 23`.
Die Nachweise und Zuordnungen stehen in [Write-Analysis.md](Write-Analysis.md).
Die folgenden Aussagen zur fehlenden Schreibbeobachtung beziehen sich auf
die ursprüngliche Datei `master.log`.

## Ergebnis

[controller.tsp](controller.tsp) enthält **alle 240 unterschiedlichen,
vollständig und mit gültigen Prüfsummen beobachteten Anfragen** aus
`master.log`. [main.tsp](main.tsp) importiert diese neue Datei anstelle von
`tem/controller.tsp`. Die alte Datei bleibt als historische Arbeitsdatei erhalten.

| Kategorie | Anzahl Modelle |
|---|---:|
| Erfolgreiche Parameteranfragen `06 21` | 201 |
| `06 21` mit Antwort `FF 1F` („nicht vorhanden“) | 7 |
| Menü-/Strukturblöcke `06 20` | 28 |
| Listenblöcke `06 22` | 4 |
| **Gesamt** | **240** |

Die 201 erfolgreichen Parameteranfragen liefern **118 unterschiedliche
TEM-Kennungen**. Mehrere Anfragen können dieselbe Kennung liefern, deshalb
werden sie nicht zusammengelegt. Von den 119 Kennungen des STE-Katalogs
kommen **75 im Mitschnitt vor; 44 fehlen**. „Alle“ bedeutet hier also alle
belegten Zugriffe dieses Mitschnitts, nicht sämtliche möglichen Reglerparameter.

Die vollständige Zuordnung einschließlich Belegzeile und Antworttyp steht in
[master-output/Parameter.md](master-output/Parameter.md), maschinenlesbar in
[requests.tsv](master-output/requests.tsv) und [requests.json](master-output/requests.json).

**Schreiben ist durch diese Datei noch nicht belegt.** `master.log` enthält
ausschließlich Anfragen an Slave `15` mit den Diensten `06 20`, `06 21` und
`06 22`. Keine Anfrage trägt einen veränderten Einstellwert. Die Änderungen
stehen in den Antworten. `06 23` kommt überhaupt nicht vor. Deshalb enthält
die neue Datei keine geratenen Schreibmodelle.

Ein auf `01 -> 15` eingeschränkter Filter könnte Schreibtelegramme an die
zugehörige Masteradresse `10` ausgeblendet haben. Das ist eine mögliche
Erklärung, kein Nachweis des Schreibziels. Für bestätigte Schreibmodelle wird
ein ungefilterter Ausschnitt um eine Bedienänderung benötigt, einschließlich
Master-Master-Telegrammen. Ein Passwort-/Freischaltablauf ist hier ebenfalls
nicht nachgewiesen. `04-43` wird nur gelesen, mit Wert 1; die früher vermutete
Enumeration „User=0, Expert=2“ wird nicht übernommen.

## Benutzung

```bash
npm run build:csv

# Beispiele für den ebusd, auf dem die neue CSV geladen wurde:
ebusctl read -f -c 15 P03_051_0B00
ebusctl read -f -c 15 P05_051_0B03
ebusctl read -f -c 15 P09_023_A909
```

Die Ausgabedatei ist `csv-output/@ebusd/ebus-typespec/tem/controller.csv`.
Sie ersetzt die gleichnamige bisherige CSV. Das Circuit bleibt ausdrücklich
`15`, damit die Datei auch ohne automatische Scan-Konfiguration geladen
werden kann.

Die vollständige Antwort enthält bei normalen Zahlenwerten:

```text
TEM-Kennung;Typcode;Einheitencode;Maximum;Minimum;Wert
03-051;77;2;30.0;10.0;22.0
```

Für einen einzelnen Wert kann ebusctl das Feld `wert` auswählen:

```bash
ebusctl read -f -c 15 P03_051_0B00 wert
```

Bei Auswahlwerten bleiben die vier Grenz-/Maskenbytes roh sichtbar. Bei
Sonderantworten wird die vollständige Roh-Nutzlast statt eines erfundenen
Wertfeldes ausgegeben. „NichtVorhanden“-Modelle dienen der Diagnose der im
Mitschnitt mit `FF 1F` beantworteten Anfragen; sie sind keine Einstellparameter.

Die Quelle `01` wird nicht durch `@qq` erzwungen. ebusd verwendet für aktive
Abfragen seine konfigurierte Masteradresse; passiv empfangene Antworten auf
die Quelle `01` können ebenfalls erkannt werden. Dass diese Zugriffe auch
von einer anderen Masteradresse akzeptiert werden, muss am Gerät geprüft
werden. Hier wurde ausschließlich offline getestet.

## Das belegte Anfrageformat

Beispiel aus Zeile 22:

```text
01 15 06 21 02 0B 00 39 00 0A B3 41 4D 02 2C 01 64 00 DC 00 E2 00
|  |  |     |  |     |  |  |  |                             |  |
QQ ZZ PBSB  NN Index CRC ACK NN Slave-Nutzdaten              CRC ACK
```

Die beiden Anwendungsbytes `0B 00` sind die beobachtete Anfrage. Sie sind
**nicht** die TEM-Kennung `03-51`. Diese kommt als `B3 41` in der Antwort
zurück. Für das Anfragenformat enthält TypeSpec daher:

```typespec
@id(0x06, 0x21, 0x0b, 0x00)
```

Länge, CRC, ACK und Quell-/Zieladresse gehören nicht in `@id`.
Die entsprechende rohe Anfrage ohne Transport-CRC wäre für `ebusctl hex`
`150621020b00` (mit Längenbyte); die benannte Lesedefinition ist bequemer.

Die Antwortkennung wird als Little-Endian-Wort dekodiert:

```text
wort   = byte0 | (byte1 << 8)
gruppe = (wort >> 7) & 31
nummer = wort & 127
B3 41 -> 0x41B3 -> 03-051
```

Das obere Bitfeld gehört nicht zur x-y-Kennung. Für die Ausgabe wird der
eingebaute ebusd-Datentyp `TEM_P` verwendet, dessen Slave-Dekodierung im
Offline-Replay mit den berechneten Kennungen abgeglichen wird.

### Kurze und erweiterte Anfragen

Beobachtet werden zwei Varianten:

```text
06 21 / 0B 00
06 21 / 0B 80 10 00
```

Beim erweiterten Zugriff ist Bit 7 des zweiten Bytes gesetzt; danach folgt
in dieser Datei immer `10 00`. Beide Antworten können dieselbe TEM-Kennung
tragen, aber unterschiedliche Kontexte/Werte betreffen. Beispielsweise liefert
`A7 04` für `07-05` die Werte 2 und 0, während `A7 84 10 00` die Werte 3 und 0
liefert. Der Zusammenhang spricht für einen Instanz-/Kontextselektor, erlaubt
aber keine pauschale Gleichsetzung mit physischem Heizkreis 2.

**`10 00` ist kein übertragener Einstellwert:** Es bleibt auch bei völlig
verschiedenen Parametern und Temperaturen unverändert. Die Modelle behalten
deshalb die vollständige Anfrage als Namenssuffix, etwa `P03_051_0B00` und
`P03_051_0B801000`.

Auch `06 22` ist hier keine Schreiboperation. Es folgen auf die kurze
`02-12`-Antwort wiederkehrend die Anfragen `01 89 00 00` / `01 89 01 00`
bzw. `01 89 10 00` / `01 89 11 00`. Die Antworten enthalten zehn bzw. zwei
Bytes Listendaten. Bedeutung und Elementstruktur bleiben roh erhalten.

## Dekodierung und Unterschiede zum STE-Katalog

Namen werden, soweit vorhanden, anhand der **Antwortkennung** aus dem
STE-Katalog übernommen. Anfrageadressen, Werte, Typ- und Einheitencodes stammen
aus dem Mitschnitt. Die STE-Auswahltexte und Grenzwerte werden nicht als
verbindliche Busdefinition übernommen.

| Antworttyp | Behandlung |
|---|---|
| `0D`, `4D`, `8D` | Vorzeichenbehaftetes Little-Endian-Wort, geteilt durch 10; auch Grenzen so dekodiert |
| `02` mit Einheit 0 | 16-Bit-Auswahl Aus/Ein |
| `01`, `C1` | Vorzeichenbehaftetes **erstes Byte**, danach ein Byte Padding; z. B. `9C 00` = −100, nicht +156 |
| `00`, `04`, `09` | Auswahl/Integer als UIN, Grenzen/Masken unverändert roh |
| `03-10`, Typ `04`, Einheit `08` | Steilheit /100, abgeleitet aus Bus-Maximum 500 und STE-Maximum 5 |
| `02-70`, Typ `04`, Einheit `28` | Datum als `DAY`, Tage seit 1.1.1900 |
| Typ `04`, Einheit `2A` | Minutenwert bis 10.080; keine 24-h-Uhrzeit mit `MIN` |
| `1D` | 10-Byte-Antwort mit sechs Byte speziellen Daten nach der Kennung/Typ/Einheit |
| `1E` | **6-Byte-Antwort** mit nur zwei speziellen Datenbytes nach dem Kopf |
| Unbekannte Spezialtypen | vollständige Rohdaten erhalten |

Bei Typ `09` sind die vermeintlichen Grenzen teils Bitmasken: etwa `04-20`
mit den Bytes `3D 00 1E 00`, obwohl der Wert 2 lautet. Diese Felder pauschal
als Minimum und Maximum zu behandeln wäre falsch.

Einheitencodes werden aus der Antwort verwendet: `02=°C`, `04=K`, `08=%`,
`0A=h`, `0C=min`, `0E=s`, `10=kW`. Eine Ausnahme ist die aus dem STE-Katalog
erschlossene dimensionslose Steilheit. Beispiel eines belegten Unterschieds:
`06-12` hat im Mitschnitt `0C` (Minuten); die STE-Datei hatte Einheitencode 7,
der dort nur vorsichtig als Sekunden vermutet wurde. Die neue Definition
verwendet die Antwortdaten.

Die Datenblöcke `1D` enthalten wechselnde Informationen auch vor den letzten
zwei Bytes. Ein generisches Modell „Kopf + Max + Min + Wert“ würde hier
relevante Daten falsch bezeichnen. Der kurze Typ `1E` würde damit sogar die
Antwortlänge überschreiten.

## Validierung

`npm run build:csv` und die ebusd-Konfigurationsprüfung sind erfolgreich.
Die Gesamt-Konfiguration enthält 327 Nachrichten, davon 240 aus der neuen
Controllerdatei. Sechs Tests sind bestanden. Der Test kompiliert die neue
Datei zusätzlich isoliert und spielt alle 4.776 gültigen Transaktionen in
ebusd mit `/dev/null` als Gerät und `--inject=stop` ab: **4.776 korrekt
zugeordnete und dekodierte Antworten, keine unbekannte Nachricht und kein
Dekodierungsfehler**. Die Antwortkennung wird dabei für jede Parameterantwort
mit der erwarteten TEM-Kennung verglichen. Ein Live-Test ist nicht erfolgt.

Quelle: `master.log`, SHA-256
`b6fb33c89d99a122bb3e4f7f34919e0a450ead3a60db31fffafca2e8462d0e9c`.

Die Datei umfasst 4.953 Zeilen:

- 4.776 vollständige, beidseitig quittierte Telegramme mit gültigen CRCs.
- 176 Anfragen mit gültiger Master-CRC, aber ohne Antwort in dieser Zeile.
  Sie werden nicht als vollständige Transaktion gewertet.
- Eine fehlerhafte Slave-CRC in **Zeile 2069**. Dort steht Typ/Einheit `1D 80`
  statt des sonstigen `1D 00`, ohne passend veränderte CRC. Dieser Datensatz
  fließt nicht in die Definitionen ein.

Die Escape-Sequenzen `A9 00` und `A9 01` werden zustandsbehaftet zu `A9` bzw.
`AA` dekodiert. Einfaches wiederholtes Ersetzen wäre falsch: `A9 00 01`
bedeutet `A9 01`, nicht `AA`. Die CRC wird über die **escapten Wire-Bytes**
berechnet. Grundlage dafür ist die Implementierung von
[ebusd, symbol.cpp](https://github.com/john30/ebusd/blob/master/src/lib/ebus/symbol.cpp).

Reproduzieren:

```bash
python3 scripts/analyze_master_log.py
python3 -m unittest discover -s scripts -p 'test_master_log.py'
npm run build:csv
ebusd --checkconfig --scanconfig=off --configpath=csv-output/@ebusd/ebus-typespec
```

Der Generator erzeugt die TypeSpec-Datei und die Belegtabellen aus dem
Mitschnitt. Er prüft konstante Antwortkennung, Typ und Einheit pro Anfrage,
berücksichtigt unterschiedliche Antwortlängen und übernimmt keine Anfrage
aus dem bisherigen geratenen Mapping. Weitere Dienste oder ein anderer
Kommunikationspartner erfordern eine bewusste Erweiterung des Generators.
