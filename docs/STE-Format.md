# Analyse der TEM-STE-Datei

## Ergebnis und lesbare Ausgaben

Die Datei lässt sich vollständig strukturell dekodieren: **217 Datensätze auf
64.974 Bytes**, ohne übersprungene Bereiche oder Restbytes. 206 Datensätze tragen
eine TEM-Kennung; das sind **119 unterschiedliche Kennungen**. Die übrigen
11 Datensätze sind mit `-----` bezeichnet. Alle Datensätze enthalten die
Controllerkennung `17385` und das zusätzliche Textfeld `ich`.

- [Parameter.md](ste-output/Parameter.md): nach TEM-Kennung sortierte Übersicht
  mit gespeicherten Werten, Grenzen, Kontext und sämtlichen Hilfetexten.
- [parameter.csv](ste-output/parameter.csv): vollständiger Tabellenexport,
  UTF-8 mit BOM, Semikolon als Trennzeichen und Dezimalkomma.
- [parameter.json](ste-output/parameter.json): alle Felder einschließlich
  unbekannter Metadaten, unveränderter Originaltexte und Dateioffsets.
- [decode_ste.py](scripts/decode_ste.py): reproduzierbarer Decoder, nur Python-Standardbibliothek.

```bash
python3 scripts/decode_ste.py 'Datapacks v 1.1  über V 52  9.02.09.ste'
python3 -m unittest discover -s scripts -p 'test_decode_ste.py'
```

Standardausgabe ist `ste-output/`; mit `--output VERZEICHNIS` lässt sie sich
ändern. Vorhandene gleichnamige Exportdateien werden ersetzt. Die Quelldatei
wird nur gelesen. Es werden keine Geräte angesprochen.

Quelle: `Datapacks v 1.1  über V 52  9.02.09.ste`

SHA-256: `1ba1f84ba2f481f9ed235e3231edb4b100484159b44efaaa765124a888deeebe`

**Bedeutung von „gespeicherter Wert“:** Die Datei enthält Parameterdefinitionen
und pro Datensatz ein plausibles Wertefeld. Die Werte sind die Auslieferungswerte
der betrachteten Heizungsanlage. Einige Parameter sind über die angeschlossenen
Fernbedienungen HFB 5811 durch den Endanwender einstellbar. Es gibt auch Parameter,
die nur über eine Master-Bedienung (oder ebusd) verändert werden können und deren
Werte dem Aufbau der Anlage entsprechen sollten. Diese sind insbesondere ab 07-xx.
Es besteht das Ziel sicherzustellen,
dass diese Einstellungen noch dem Auslieferungszustand entsprechen.

## Wichtige Werte aus der Datei

Die beiden Varianten werden hier als HK 1 und HK 2 bezeichnet. Das ist aus den
gepaarten Datensätzen und ihren Metadaten abgeleitet; eine Zuordnung zur realen
Verrohrung oder zu den eBUS-Adressen der Bedienteile ist damit nicht bewiesen.

| TEM | Bedeutung | HK 1 | HK 2 | Einheit aus Metadaten |
|---|---|---:|---:|---|
| 03-50 | Betriebswahl Heizung und Brauchwasser | 1 | 1 | laut Hilfetext: Automatik 1 |
| 03-51 | Raum-Solltemperatur Tag | 20,5 | 20,5 | °C |
| 03-53 | Raum-Solltemperatur Nacht | 18 | 18 | °C |
| 03-58 | Behaglichkeit | 0 | −1 | K |
| 03-10 | Steilheit Kennlinie | 0,3 | 0,3 | — |
| 03-01 | Fußpunkttemperatur | 20 | 20 | °C |
| 03-21 | Heizgrenze Tagbetrieb | 16 | 16 | °C |
| 03-02 | Heizgrenze Absenkbetrieb | 17 | 17 | °C |
| 03-35 | Kühlgrenzenabstand | 10 | 5 | °C¹ |
| 03-43 | Kühltemperatur | 22 | 22 | °C |
| 05-51 | Warmwasser-Solltemperatur | 50 | 10 | °C |
| 07-08 | Maximale Vorlauftemperatur | 55 | 45 | °C |
| 07-05 | Heizkreistyp | 2: Pumpenkreis | 0: 3-Punkt-Mischer | — |

¹ Der Abstand ist fachlich eine Temperaturdifferenz; die Datei verwendet jedoch
denselben Einheitencode wie bei absoluten Temperaturen. Der Export korrigiert
solche Angaben nicht stillschweigend.

| TEM | Kontext | Gespeicherter Wert / Bedeutung laut Datei |
|---|---|---|
| 04-20 | Global | 2: Masterregler |
| 09-07 | Wärmepumpe, Einstellebene 9 | 5: Wärmepumpe ohne Kühlfunktion |
| 09-07 | Elektro-Zusatzheizung, Einstellebene 10 | 1: Zusatzwärmeerzeuger 1-stufig |
| 09-23 | Wärmepumpe | minimale Stillstandszeit 12 min |
| 09-31 | Wärmepumpe | minimale Laufzeit 9 min |
| 15-10 | Wärmepumpe | Heißgas-Maximaltemperatur 125 °C |
| 15-22 | Wärmepumpe | Wärmequellen-Frostschutztemperatur −12 °C |
| 15-40 | Wärmepumpe | 0: keine Abtauung |
| 05-02 | Brauchwasser | 0,1: absoluter Parallelbetrieb |

Die Kaskadenkonfiguration enthält Einträge für WE 1 bis WE 8. Die Zieladressen
sind 11 für WE 1, 12 für WE 2 und 0 für WE 3–8. Laut Hilfetext bedeutet 0 „kein
WE“. Das Vorhandensein von acht Parametersätzen belegt also nicht acht Geräte.

## Drei unterschiedliche Nummerierungen

1. **TEM-Kennung:** steht am Anfang des Namens, etwa `03-51`, `07-08` oder
   `15-22`. Sie wird als Kennung übernommen und für die Sortierung verwendet.
2. **Einstellebene des Programms:** steht in einem separaten Gruppentext.
   Beispiel: `03-51` liegt in „Einstellebene 2“, `15-22` in „Einstellebene 9“.
3. **Bedienteil-Menüposition / Übertragungsblock:** ist eine andere Darstellung.
   In [FB-Initialization.md](FB-Initialization.md) heißt die Kühltemperatur
   beispielsweise `3-4`; in dieser Datei heißt der TEM-Parameter `03-43`.
   Entsprechend steht dort `3-5` für den hier als `03-35` bezeichneten
   Kühlgrenzenabstand. Aus einer Menüposition darf daher nicht allgemein die
   TEM-Kennung abgeleitet werden.

Mehrfach vorkommende TEM-Kennungen dürfen nicht als Duplikate entfernt werden:
`09-07` existiert für Wärmepumpe und Elektro-Zusatzheizung, die Heizkreiswerte
stehen paarweise in der Datei. Bei WE 1–8 bleiben die Titel `04-22` und `11-01`
bis `11-05` sogar unverändert; erst der Gruppentext weist den Wärmeerzeuger aus.
Eine Umbenennung in etwa `12-02` wäre durch diese Datei nicht belegt.

## Binärer Container

Der Dateianfang entspricht einem **Microsoft-MFC-CArchive** mit serialisierten
Objekten der Klasse **`CDatapack`**, Schema **1**. Kennzeichnend sind der Marker
`FFFF`, der Klassenname und die nachfolgenden Klassenreferenzen `8001`.
Das entspricht Microsofts Beschreibung der MFC-Objektserialisierung.
[Microsoft: TN002, Persistent Object Data Format](https://learn.microsoft.com/en-us/cpp/mfc/tn002-persistent-object-data-format?view=msvc-170)

Die äußere Objektanzahl und der Inhalt von `CDatapack` sind aus dieser Datei
rekonstruiert; Microsoft dokumentiert damit nicht das proprietäre TEM-Schema.

| Offset | Bytes | Interpretation |
|---|---|---|
| `0x0000` | `D9 00` | 217 Objekte, UInt16 Little-Endian |
| `0x0002` | `FF FF` | neue MFC-Klasse |
| `0x0004` | `01 00` | Klassenschema 1 |
| `0x0006` | `09 00` | 9 Bytes Klassenname |
| `0x0008` | `43 44 61 74 61 70 61 63 6B` | `CDatapack` |
| `0x0011` | … | erster Objektinhalt |
| `0x0164` | `01 80` | nächstes Objekt derselben Klasse |
| `0x0166` | … | zweiter Objektinhalt |

Alle beobachteten Ganzzahlen sind Little-Endian. Zahlenwerte und Grenzen sind
IEEE-754-Binary64-Werte (`double`), ebenfalls Little-Endian. Texte lassen sich
als Windows-1252 lesen; eine Codepage-Kennung ist nicht vorhanden. Für die hier
vorkommenden Umlaute wäre ISO-8859-1 ebenfalls kompatibel.

Texte haben ein Längenpräfix und keinen abschließenden Nullterminator:

- Normalfall: ein Byte Länge, danach genau so viele Textbytes.
- Lange Texte: `FF` und anschließend UInt16-Länge, dann Textbytes.
  Die Datei enthält drei solche Hilfetexte mit 400, 279 und 271 Bytes.
- Der Decoder unterstützt zusätzlich die MFC-Längenfortsetzung
  `FF FF FF` + UInt32-Länge. Sie kommt in dieser Datei nicht vor.
- Unicode-CStrings, andere Klassen/Schemas, Objektreferenzen und erweiterte
  Objektanzahlen werden ausdrücklich zurückgewiesen, nicht erraten.

## Aufbau eines CDatapack-Objekts

Die Feldnamen sind Arbeitsnamen des Decoders, keine rekonstruierten
C++-Membernamen. „Roh“ bedeutet: Zahlenwert sicher gelesen, Bedeutung offen.

| Reihenfolge | Typ | Exportfeld | Befund |
|---|---|---|---|
| 1 | 4 × UInt32 | `header_raw` | meist `[1,2,21,1]` oder `[1,2,21,2]`; Details unten |
| 2 | CString | `title` | vollständiger Name einschließlich TEM-Kennung |
| 3 | 2 × UInt32 | `address_low_raw`, `address_high_raw` | Werte 0–255, zusammen plausibler Adresskandidat |
| 4 | UInt32 | `type_raw` | numerischer Typcode: 0, 1, 4, 13 oder 14 |
| 5 | double | `maximum` | obere Grenze |
| 6 | double | `minimum` | untere Grenze |
| 7 | double | `step_raw` | mutmaßliches Schrittfeld, unskaliert ausgegeben |
| 8 | double | `stored_value` | gespeicherter Wert |
| 9 | UInt32 | `position_raw` | Position innerhalb der numerischen Seite |
| 10 | UInt32 | `page_raw` | numerische Seite, 1–11 |
| 11 | UInt32 | `entry_key_raw` | zusammengesetzter Eintragsschlüssel |
| 12 | UInt32 | `variant_flag_raw` | bei gepaarten Heizkreisdatensätzen 1, sonst 0 |
| 13 | UInt32 | `unit_raw` | Einheitencode, siehe unten |
| 14 | CString | `help_text` | Hilfetext, oft Auswahlwerte oder Funktionsbeschreibung |
| 15 | CString | `group_text` | Einstellebene und Funktionsgruppe |
| 16 | 3 × UInt32 | `tail_raw` | erstes Feld 0–3; danach immer 0 und 81 |
| 17 | CString | `author_text` | immer `ich`; mutmaßlich Autor/Bearbeiter |
| 18 | CString | `controller_text` | immer `17385` |

### Feste Offsets nach dem Titel

Relativ zum ersten Byte nach dem Titeltext (`fields_offset` im JSON):

```text
+00  UInt32  address_low_raw
+04  UInt32  address_high_raw
+08  UInt32  type_raw
+12  double  maximum
+20  double  minimum
+28  double  step_raw
+36  double  stored_value
+44  UInt32  position_raw
+48  UInt32  page_raw
+52  UInt32  entry_key_raw
+56  UInt32  variant_flag_raw
+60  UInt32  unit_raw
+64  CString help_text
     CString group_text
     UInt32[3] tail_raw
     CString author_text
     CString controller_text
```

Beispiel Datensatz 9 (`03-51`, HK 1): `fields_offset = 0x075E`.
Ab `0x076A` stehen 30,0 als Maximum, 10,0 als Minimum, 5,0 im Schrittfeld und
ab `0x0782` **20,5** als gespeicherter Wert. Die Werte sind bereits als
Dezimalzahlen im Double-Format gespeichert; der Wert 20,5 wird beim Export
nicht nochmals durch 10 geteilt.

### Metadaten und ihre Sicherheit

**Header:** Das dritte Wort ist immer 21 (`0x15`), passend zur bekannten
Controller-Slaveadresse, aber ohne Originalsoftware bleibt die Bedeutung eine
Hypothese. Das vierte Wort ist 1 oder 2 und passt zur vermuteten Bytebreite des
Controllerwerts. Die ersten beiden Wörter sind überwiegend 1/2, bei zwei
Datensätzen 1/3 und bei drei Kommandodatensätzen 0/0. Ihre genaue Funktion ist
offen. Insbesondere ist das zweite Wort keine zuverlässig ableitbare Bytebreite.

**Adresskandidat:** `address_low_raw | (address_high_raw << 8)` ergibt zum
Beispiel `F004` für `03-51` HK 1 und `F32C` für HK 2. Die Abstufungen passen
zu Bytepositionen in Parameterbereichen: `F004`, `F006`, `F008` enthalten
Raumtemperatur Tag, Nacht und Warmwasser; darauf folgen einzelne Bytewerte
ab `F00A`. Ein weiterer Hinweis ist der Kaskadenübergang von `F2FF` zu `F300`.
Das spricht für interne Speicheradressen/Offsets. **Ein EEPROM-Zugriff oder
ein eBUS-Telegrammformat ist dadurch nicht bewiesen.** Es gibt nur 214
unterschiedliche Adresspaare: die drei BW-Zeitprogramm-Paare benutzen jeweils
dieselbe Adresse für beide Varianten. Deshalb bleibt auch hier der gesamte
Datensatz erhalten.

**Typcode:** Die beobachteten Kombinationen aus viertem Headerwort und
`type_raw` sind `(1,0)`, `(1,1)`, `(2,4)`, `(2,13)` und `(2,14)`. Das passt
zu Bytewerten ohne/mit Vorzeichen, ganzzahligen Auswahlwerten und Werten mit
einer bzw. zwei Dezimalstellen. Besonders aussagekräftig: Code 14 steht nur
bei der Steilheit 0,3; Code 13 auch bei negativen Temperaturen. Dies ist eine
Arbeitshypothese für den Controllerdatentyp. Die Double-Werte der STE-Datei
lassen sich unabhängig davon direkt lesen.

**Schrittfeld:** Der dritte Double-Wert passt zu einer Schrittweite in
Controller-Rohwerten. Beispielsweise steht 5 bei Raum-Solltemperatur
(plausibel 0,5 °C), 10 bei vielen Temperaturen (plausibel 1 °C), 1 bei der
Steilheit (plausibel 0,01) und 5 bei Partydauer (plausibel 5 min).
Diese Skalierung ist nicht gegen das Originalprogramm geprüft. Die Exporte
zeigen deshalb `step_raw`, keine als gesichert ausgegebene physikalische Schrittweite.

**Schlüssel:** Für alle 217 Datensätze gilt exakt:

```text
entry_key_raw = (page_raw << 11) + (position_raw << 4) + variant_index
variant_index = entry_key_raw & 0x0F
```

Bei Heizkreispaaren unterscheiden sich nur die niederwertigen Variantenbits
0/1. Für Kaskaden-WE 1–8 bleibt `page_raw = 11`; stattdessen steigt
`position_raw` jeweils um 10. Die Gruppentexte nennen dabei Einstellebene
11 bis 18. Schlüssel und numerische Seite dürfen folglich nicht pauschal
als TEM-Kennung oder angezeigte Einstellebene verwendet werden.

**Nachspann:** Das erste Wort in `tail_raw` könnte eine Zugangs-/Anzeigeebene
angeben; die Zuordnung ist nicht gesichert. Die konstanten 0 und 81 bleiben
ebenfalls unbenannt. Es ist kein separates Prüfsummenfeld identifiziert.

### Einheitencodes

| `unit_raw` | Abgeleitete Einheit | Begründung |
|---:|---|---|
| 0 | keine Einheit hinterlegt | Auswahlen und diverse Sonderformate |
| 1 | °C | Temperaturparameter |
| 2 | K | Offsets und Temperaturdifferenzen |
| 4 | % | ausdrücklich in Leistungs-Hilfetexten genannt |
| 5 | h | Hilfetext `03-20` nennt 5 h, 10 h und 20 h |
| 6 | min | Partydauer-Hilfetexte nennen Minuten |
| 7 | vermutlich s | Zeitparameter, plausibel nach h/min; nicht ausdrücklich belegt |
| 8 | kW | Hilfetext `11-02` nennt kW |

Die Zuordnung wird zusätzlich durch [tem/_templates.tsp](tem/_templates.tsp)
gestützt: Die dortigen eBUS-Einheitencodes sind für die vorhandenen Vergleiche
jeweils doppelt so groß (`°C=2`, `K=4`, `h=10`, `min=12`, `kW=16`). Die
STE-Codes sind somit nicht unverändert als eBUS-Einheitencodes zu behandeln.
Code 7 fehlt in diesem lokalen Vergleich und wird im Export als `s?` geführt.

## Auffälligkeiten der Quelldaten

- `07-06`, zweiter Heizkreis, enthält einen Frostgrenzen-Hilfetext, obwohl der
  Titel eine Fehlerdauer beschreibt. Der Text entspricht dem von `03-23`, HK 1.
- `07-31`, zweiter Heizkreis, beschreibt im Hilfetext eine Temperaturabweichung
  für eine Fehlermeldung; beim ersten Heizkreis wird die Niedertarifüberhöhung
  ausführlich erläutert. Der Widerspruch ist bereits in der STE-Datei vorhanden.
- `09-11`, Elektro-Zusatzheizung: gespeicherter Wert 10, aber der Hilfetext
  erklärt nur `0 = frei`. Bedeutung 10 bleibt offen.
- `07-05`: Hilfetext nennt zusätzlich Auswahl 4, numerisches Maximum ist 3.
- `08-79`: Titel und Hilfetext beschreiben eine Minimal-/Solltemperatur, die
  Metadaten verwenden jedoch Einheitencode 2 (K).
- `04-64`: Einheitencode 0, Hilfetext nennt `[0.1 d]`. Gespeichert ist 30;
  bei Anwendung dieser textlichen Skalierung entspricht das 3 Tagen.
- `15-47`: ebenfalls Einheitencode 0; der Hilfetext erklärt ausdrücklich
  `10 = 1.0 Min`. Gespeichert ist 0. `15-48` hat auch Code 0, aber keine
  ausdrücklich genannte Zeiteinheit; diese wird nicht ergänzt.
- `15-23` steht in Einstellebene 5 „Brauchwasserbereitung“, obwohl die
  TEM-Kennung und der Titel auf eine Frostschutztemperatur verweisen.
- Die Werte weichen teils von [FB-Initialization.md](FB-Initialization.md) ab,
  etwa 20,5 statt 20 °C Raum-Solltemperatur und 20 statt 22 °C Fußpunkt.
  Sie sind getrennte Datenstände. Auch die Darstellung der Steilheit ist
  unterschiedlich: hier 0,3, im dortigen FB-Mitschnitt 30.

## Verifikation und Grenzen

Der Decoder liest alle Felder sequenziell anhand ihrer Größen und
Längenpräfixe, ohne nach lesbaren Zeichenketten oder vermeintlichen
Datensatztrennzeichen zu suchen. Der mitgelieferte Test serialisiert die
dekodierten Rohfelder unabhängig zurück und vergleicht **alle 64.974 Bytes**
mit dem Original. Er prüft zusätzlich bekannte positive und negative Werte,
die langen Hilfetexte, Datensatzanzahl, Kennungen und den Eintragsschlüssel.
Abgeschnittene Dateien, Restbytes und falsche Klassenmarker werden abgewiesen.

Alle gespeicherten Werte liegen innerhalb der jeweils gespeicherten Grenzen.
Damit ist die Rekonstruktion des Dateiaufbaus gut abgesichert. Der Bytevergleich
bestätigt jedoch nicht automatisch die fachliche Bedeutung der unbekannten
Metadaten. Das Originalprogramm, weitere STE-Dateien oder kontrollierte
Vorher-/Nachher-Dateien wären nötig, um diese Bedeutungen weiter zu verifizieren.

Aus den TEM-Namen oder Adresskandidaten werden hier keine `06 21`-/`06 23`-
Telegramme erzeugt. Die STE-Datei liefert einen Parameterkatalog mit Werten
und internen Metadaten, aber keinen bestätigten Buszugriff für diese Felder.
