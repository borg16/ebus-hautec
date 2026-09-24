# Menüverzeichnis des TEM-Controllers

Auswertung von `input/complete.log`: Das Zusammenspiel von `06 20` und
`06 21` erlaubt sehr wahrscheinlich die dynamische Ermittlung der angebotenen
Parameter. Die folgende Interpretation ist aus dem Mitschnitt abgeleitet,
nicht aus einer TEM-Protokollspezifikation.

## Systematik: Menüplatz, TEM-Kennung und Instanz

**Die Bedienung muss die Liste der angebotenen Parameteradressen wahrscheinlich
nicht fest einprogrammiert haben.** Sie kann sie durch Verzeichnisabfragen und
anschließendes Lesen der Menüplätze aufbauen. Das Verzeichnis allein enthält
aber noch keine TEM-Nummern: Erst die jeweilige `06 21`-Antwort liefert die
Zuordnung. Für eine vollständig beschriftete Oberfläche fehlen weiterhin
Klartextnamen und Auswahltexte; auch Sondertypen und Skalierungen verlangen
Protokollwissen.

Folgende Ebenen sind auseinanderzuhalten:

| Ebene | Beispiel | Funktion |
|---|---|---|
| Zielgerät | Lesen an `15`, Schreiben an `10` | Im Mitschnitt verwendete eBUS-Adressen |
| Menü | `a7` | Sammlung von Eintragsplätzen |
| Eintragsindex | `04` | Nullbasierte Position innerhalb des Menüs |
| Vollständiger Selektor | `a7 04` oder `a7 84 10 00` | Tatsächlich übertragene Adresse einschließlich Kontext |
| TEM-Kennung | `07-05` | Identifiziert den Parametertyp in der Antwort |
| Instanz | Grundkontext bzw. zusätzlicher Kontext | Unterscheidet Einstellungen desselben Parametertyps |

**Korrektur zum Beispiel:** `a7 04` liefert **07-05**, nicht 07-04.
Die sieben niedrigen Bits des Antwortwortes sind `05`. Der Index `04` ist
die fünfte Menüposition und keine TEM-Parameternummer. Das vollständige
beobachtete Menü `a7` macht diese Unterscheidung deutlich:

| Index (hex) | TEM-Kennung | Grundselektor | Erweiterter Selektor |
|---|---|---|---|
| 00 | 07-00 | `a7 00` | `a7 80 10 00` |
| 01 | 07-01 | `a7 01` | `a7 81 10 00` |
| 02 | 07-02 | `a7 02` | `a7 82 10 00` |
| 03 | 07-03 | `a7 03` | `a7 83 10 00` |
| 04 | 07-05 | `a7 04` | `a7 84 10 00` |
| 05 | 07-06 | `a7 05` | `a7 85 10 00` |
| 06 | 07-14 | `a7 06` | `a7 86 10 00` |
| 07 | 07-31 | `a7 07` | `a7 87 10 00` |

Die optische Beziehung `a7` → Einstellebene 7 tritt bei mehreren Menüs auf,
ist aber keine allgemeine Umrechnungsregel. Menü `0b` mischt beispielsweise
03-51, 03-53, 05-51, 03-10, 07-08 und 03-21. In `a5` findet sich auch
15-23. Die TEM-Kennung muss deshalb aus der Antwort übernommen werden.

### Drei Ursachen für mehrfach vorkommende TEM-Kennungen

1. **Ein Menüplatz in mehreren Kontexten.** `0b 02` und `0b 82 10 00`
   liefern beide 03-53, zuletzt aber 18 °C bzw. 10 °C. Bei `a7 04` und
   `a7 84 10 00` ist es jeweils 07-05, zuletzt mit Wert 0 bzw. 3.
   Das passt zu getrennten Heizkreiseinstellungen. Die Zuordnung
   Grundkontext → HK 1 und Zusatzkontext → HK 2 ist durch STE-Varianten und
   den Vergleich mit den Fernbedienungsdaten gestützt, bleibt aber abgeleitet.
2. **Unterschiedliche Funktionsgruppen in verschiedenen Menüs.** `a9 0e`
   und `aa 0e` liefern beide 10-31, mit 60 °C bzw. 68 °C. Der STE-Katalog
   ordnet diese Gruppen Wärmepumpe und Zusatzheizung zu. Diese Unterscheidung
   erfolgt bereits durch die Menüadresse, ohne den Zusatz `10 00`.
3. **Mehrere Menüansichten desselben Parametertyps.** Beispielsweise
   erscheint 00-00 unter `01 01`, `08 00` und `09 00`; 02-71 unter `01 08`
   und `0a 00`. Das passt zu Übersichts- und Detailansichten. Die gleiche
   TEM-Kennung allein beweist jedoch nicht, dass zwei Adressen auf denselben
   internen Speicherwert zeigen.

Ein Parameterverzeichnis darf deshalb **nicht nur nach TEM-Kennung indiziert
werden**. Als Zugriffsschlüssel sollte es mindestens Zielgerät, Dienst und
vollständigen Selektor speichern; die TEM-Kennung dient als semantische
Zuordnung. Kontextgleiche oder alternative Zugriffe dürfen erst nach weiterer
Bestätigung zusammengefasst werden.

### Was die Kontextprüfung tatsächlich belegt

Die erneute Prüfung aller vollständigen Antworten ergibt 208 verschiedene
`06 21`-Selektoren, davon 201 mit gültiger TEM-Kennung und sieben mit
`ff 1f`. Bei keinem Selektor wechselt die Kennung im Verlauf des Mitschnitts.
Alle Indizes liegen innerhalb der aus `06 20` abgeleiteten Grenzen.

Es gibt 55 beobachtete Paare aus kurzem und erweitertem Selektor:

- 51 Paare liefern dieselbe gültige TEM-Kennung.
- Drei Paare sind in beiden Kontexten unbelegt.
- Ein Paar ist nur im Grundkontext verfügbar: `01 01` liefert 00-00,
  während `01 81 10 00` mit `ff 1f` antwortet.

Alle erweiterten Abfragen betreffen Menüs mit gesetztem Zusatzflag.
Dies stützt die Kontextinterpretation, beweist aber weder die Zahl der
Instanzen noch, dass jeder Menüplatz in jedem Kontext verfügbar ist.
`10 00` wird daher als beobachteter Kontextselektor behandelt; insbesondere
wird daraus keine ungeprüfte Fortsetzung mit `20 00` für einen HK 3 abgeleitet.
Auch gleiche Werte in beiden Kontexten sind kein Beweis für einen globalen Wert.

Die vollständigen Paare, Menüplätze und Antwortbelege stehen in
[menu-output/Adressierung.md](menu-output/Adressierung.md). Die Auswertung
ist mit `python3 scripts/analyze_menu_structure.py` reproduzierbar und prüft
die genannten Beziehungen direkt gegen CRC-geprüfte Logantworten.

### Ablauf für eine dynamische Bedienoberfläche

1. Die bekannten Verzeichnisblöcke lesen und pro Menü Platzanzahl und Flag merken.
2. Für jedes Menü die Indizes von null bis Anzahl minus eins abfragen.
3. `ff 1f` als nicht verfügbaren Platz behandeln; ansonsten den vollständigen
   Selektor zusammen mit TEM-Kennung, Typ, Einheit und Rohantwort speichern.
4. Für bekannte weitere Kontexte die entsprechenden erweiterten Selektoren
   abfragen. Die vollständige Erkennung möglicher Kontexte ist noch offen.
5. Für verstandene Zahlentypen Grenzen und Wert dekodieren. Sonderantworten
   separat behandeln; bei 02-12 sind etwa zusätzliche `06 22`-Abfragen beobachtet.
6. Namen und Auswahltexte über die TEM-Kennung aus einer passenden Tabelle
   ergänzen. Selbst die Skalierung ist nicht vollständig generisch bewiesen:
   03-10 benötigt in der bisherigen Dekodierung eine besondere Skalierung.

Für bestätigte numerische Schreibzugriffe wird derselbe vollständige Selektor
mit Dienst `06 23` an `10` gesendet und um den kodierten Wert ergänzt; siehe
[Write-Analysis.md](Write-Analysis.md). Die TEM-Kennung wird dabei nicht anstelle
des Selektors übertragen. Aus einem lesbaren Menüplatz folgt noch keine
gesicherte Schreibberechtigung. Der separat dokumentierte Expert-Zugang zeigt
außerdem, dass die angebotene Oberfläche vom Zugangsstatus abhängen kann.

Damit ist eine dynamische Ermittlung der Parameterliste plausibel und durch
die Telegrammfolge gestützt. Eine vollständig selbstbeschreibende Oberfläche
einschließlich Namen, Instanzerkennung und sämtlicher Datentypen ist durch
diesen Mitschnitt hingegen nicht nachgewiesen.

## Verzeichnis lesen: 06 20

### Vergleich mit dem vollständigen Scan in commands.txt

Der aktuelle Scan enthält 503 erreichbare Selektoren. Alle 201 im Mitschnitt
gültig gelesenen Selektoren sind darin vorhanden, jeweils mit derselben
TEM-Kennung. Die Nutzung pro Menü und die Zahlen zu den folgenden Paaren
stehen in [menu-output/Nutzung.md](menu-output/Nutzung.md).

Ein besonders deutliches Muster sind **alternative Menüs mit Versatz +40 hex**:
`63→a3`, `64→a4`, `65→a5`, `66→a6`, `67→a7`, `69→a9`, `6a→aa`
und `6b..72→ab..b2`. Bei allen 125 gemeinsamen Selektoren, einschließlich
Kontextvarianten, stimmen im Scan sowohl die TEM-Kennung als auch die
vollständige Antwort überein. Die oberen Menüs enthalten teilweise weitere
Positionen:

| Menüpaar | Gemeinsam enthalten | Zusätzliche TEM-Kennungen oben |
|---|---|---|
| 63 / a3 | 03-11, 03-20 | 03-23, 03-30 |
| 64 / a4 | sieben Parameter der Ebene 4 | 04-40 |
| 65 / a5 | neun Parameter der Ebene 5 | 05-40, 15-23 |
| 66 / a6 | neun Parameter der Ebene 6 | 06-13, 06-20 |
| 67 / a7 | sieben Parameter der Ebene 7 | 07-31 |
| 69 / a9 | erste elf Positionen | weitere 27 Positionen |
| 6a / aa | erste sieben Positionen | weitere acht Positionen |
| 6b..72 / ab..b2 | je acht Positionen | keine |

**In complete.log werden keine Parameter über die unteren Menüs 63..72
abgerufen.** Die Master-Bedienung verwendet stattdessen a3..a7, a9, aa und ab.
Das stützt die Interpretation als reduzierte und erweiterte Bedienansichten
derselben Funktionsgruppen. Die genaue Benutzerrollen- oder Zugangsbedeutung
der Adressbereiche ist daraus noch nicht eindeutig ableitbar. `+40` ist eine
hier belegte Beziehung, keine allgemeine Umrechnungsregel für beliebige Menüs.

07-05 erscheint deshalb im Scan unter `67 04` und `a7 04` sowie jeweils im
Zusatzkontext. Im Mitschnitt wurden nur `a7 04` und `a7 84 10 00` benutzt,
auch bei den bestätigten Schreibzugriffen auf diesen Parameter.

Daneben bestehen weitere Muster:

- Menü 01 dient als häufig gelesene Übersicht (2662 gültige Parameterantworten).
  Das teilweise ähnliche Menü 03 wird nicht verwendet. Beispielsweise ist
  seine Temperaturposition 01 aber 00-02 statt 00-00: keine identische Kopie.
- Menüs 08 und 09 werden beide verwendet, obwohl sie viele Temperatur- und
  Statuskennungen gemeinsam enthalten. Es gibt also keine globale Regel,
  immer nur eine der mehrfachen Darstellungen zu benutzen.
- a9 und aa werden beide benutzt und entsprechen nach der bisherigen
  Zuordnung verschiedenen Wärmeerzeugergruppen. Eine gemeinsame TEM-Kennung
  bedeutet dort nicht, dass dieselbe Instanz gemeint ist.
- Aus der Folge ab..b2 wird nur ab genutzt. Die Wiederholung der Kennungen
  11-01..11-05 passt zu den im STE-Katalog beschriebenen WE-Instanzen 1..8;
  der Mitschnitt belegt keine Bedienung sämtlicher dieser Instanzen.

Auf Ebene der **Verzeichnisblöcke** liegen die erfolgreichen Parameterzugriffe
somit in 00, 01, 04, 14 und 15. Die Verzeichnisblöcke 0c..0e und 16 werden
zwar mit `06 20` gelesen, ihre Menüplätze aber im Mitschnitt nicht mit `06 21`
verwendet. Die Abfrage eines Verzeichnisblocks ist nicht gleichbedeutend mit
der Nutzung seiner Parameter.

Für aus dem Mitschnitt abgeleitete Definitionen sind daher weiterhin die
tatsächlich beobachteten vollständigen Selektoren maßgeblich. Eine automatische
Zusammenlegung allein anhand der TEM-Kennung würde alternative Ansichten und
getrennte Geräteinstanzen vermischen.

Der Master `01` liest vom Slave `15` die Blöcke `00` bis `1b`.
Die Anfrage enthält ein Byte Blocknummer; jede Antwort enthält acht Bytes.
Für Byteposition `i` (0 bis 7) im Block `b` gilt nach den Beobachtungen:

```
Menüadresse = 8 * b + i
Anzahl der Eintragsplätze = Antwortbyte & 0x7f
Zusatzflag = Antwortbyte & 0x80
```

Beispiel: Block `01` antwortet mit `8f 98 02 87 83 01 01 81`
([Logzeile 1225](input/complete.log#L1225)).

| Menü (hex) | Deskriptor (hex) | Plätze (dezimal) | Zusatzflag |
|---|---|---:|---|
| 08 | 8f | 15 | ja |
| 09 | 98 | 24 | ja |
| 0a | 02 | 2 | nein |
| 0b | 87 | 7 | ja |
| 0c | 83 | 3 | ja |
| 0d | 01 | 1 | nein |
| 0e | 01 | 1 | nein |
| 0f | 81 | 1 | ja |

Alle 28 Blöcke bleiben über sieben Abfragerunden identisch. Sie beschreiben
224 Menüpositionen, davon 48 mit einer Anzahl größer null, insgesamt 393
Eintragsplätze. Bei 13 Menüs ist das Zusatzflag gesetzt. Sämtliche beobachteten
`06 21`-Eintragsindizes liegen innerhalb der so bestimmten Anzahl.
393 Plätze sind **keine Aussage über 393 unterschiedliche TEM-Parameter**.

`controller.tsp` enthält wieder das generische Kommando `Menueblock` mit
`index` als Anfrageargument. Beispiel für Block 1 (Menüs `08..0f`):

```sh
ebusctl read -f -c 15 -i 1 Menueblock
```

Die Ausgabe enthält den Index und acht Paare `position_0_anzahl`,
`position_0_zusatzflag` bis `position_7_anzahl`, `position_7_zusatzflag`.
Beobachtet sind Indizes 0 bis 27 (dezimal). Der Discovery-Scanner fragt
die Blöcke weiterhin direkt per `ebusctl hex` ab:

```sh
ebusctl hex 1506200101
```

Jedes der acht Antwortbytes enthält die Anzahl in Bits 0..6 und das Zusatzflag
in Bit 7; Menüadresse = `8 * Blockindex + Byteposition`.

## Einträge lesen: 06 21

Die normale Nutzlast ist `[Menü, Index]`, wobei der Index bei null beginnt.
Die Antwort liefert die TEM-Kennung und bei normalen Zahlenparametern
Typ, Einheit, Grenzen und aktuellen Wert. Es gibt auch Sonderantworten.
Die TEM-Kennung wird aus den ersten beiden Bytes als Little-Endian-Wort `w`
ermittelt: `x = (w >> 7) & 31`, `y = w & 127`.

Beispiel zum Parameter **07-05**:

```
Dienst:    06 21
Nutzlast:  a7 04
Antwort:   85 43 04 00 03 00 00 00 02 00
           -----
           w = 0x4385 -> 07-05
```

Beleg: [Logzeile 2788](input/complete.log#L2788). Die Menüadresse `a7`
und der Index `04` sind also nicht unmittelbar die TEM-Nummer `07-05`.
Erst die Antwort stellt diese Zuordnung her.

Der Slot `0b 01` liefert dagegen `ff 1f 00 00 00 00 00 00 00 00`
([Logzeile 1232](input/complete.log#L1232)): Ein Platz im Verzeichnis kann
unbelegt bzw. im aktuellen Kontext nicht verfügbar sein. Solche Antworten
muss ein Bedienelement aussortieren.

## Zusätzlicher Kontext

Bei einigen Menüs wird auch die vier Byte lange Anfrage
`[Menü, Index | 0x80, 0x10, 0x00]` verwendet. Beispielsweise liefern
`a7 04` und `a7 84 10 00` jeweils `07-05`, aber unterschiedliche Werte.
Alle im Mitschnitt so angesprochenen Menüs haben das Zusatzflag im
Verzeichnis gesetzt. Das spricht für mehrere Instanzen/Kontexte.

Die genaue Flagbedeutung, die Kodierung aller möglichen Kontexte und deren
Anzahl sind damit noch nicht bewiesen. Insbesondere liefert das Flag allein
keinen sicheren Algorithmus zur Erkennung sämtlicher Heizkreise. Die im
Parametervergleich verwendete Zuordnung zu HK 1/2 ist abgeleitet.

## Was eine Bedienung entdecken kann

Eine Bedienung kann die Verzeichnisblöcke lesen, für jedes Menü alle Indizes
`0 .. Anzahl-1` abfragen und aus gültigen Antworten die TEM-Nummern samt
Werten und den bekannten Metadaten zusammensetzen. Für diese Firmware sind
die Blöcke `00..1b` beobachtet; eine allgemeine Erkennung des Verzeichnisendes
für andere Firmwareversionen ist noch nicht geklärt.

Das Verzeichnis zeigt auch bislang nicht gelesene Kandidaten: Menü `a9`
hat den Deskriptor `26`, also 38 Plätze (`00..25`, hex). Im Mitschnitt wurden
nur `00..10` gelesen. Die übrigen Plätze lassen sich erst nach einer Abfrage
als gültig oder unbelegt einordnen; ihre TEM-Nummern sind bisher unbekannt.

In diesen Metadaten stehen keine Klartextnamen, Hilfetexte oder Bezeichnungen
der Auswahlwerte. Dafür benötigt die Bedienung vermutlich eigene Tabellen;
die STE-Datei ist für uns eine zusätzliche Quelle. Auch Schreibbarkeit und
Zugriffsrechte lassen sich aus dem Verzeichnis noch nicht zuverlässig ableiten.
Die Funktion von `06 22` als ergänzende Listenabfrage ist separat zu betrachten;
sie wird für die hier belegte Zuordnung von Menü/Index zu TEM-Nummer nicht benötigt.

## Ergänzende Daten zu einem Parameter: 06 22

Die Beobachtungen sprechen für das blockweise Lesen eines strukturierten
Parameterinhalts. Konkret betrifft das im Mitschnitt ausschließlich **02-12**,
erreichbar über Menü `01`, Index `09`. Die Bezeichnung dieses Parameters ist
im STE-Katalog nicht enthalten.

Die folgende Sequenz steht beispielsweise in Logzeilen 1221–1223:

| Dienst | Anfrage-Nutzlast | Antwort-Nutzlast |
|---|---|---|
| `06 21` | `01 09` | `0c 81 1e 00 05 00` |
| `06 22` | `01 89 00 00` | `00 00 00 ff ff ff ff ff ff ff` |
| `06 22` | `01 89 01 00` | `ff 00` |

`0c 81` identifiziert 02-12. Auffällig sind der Typ `1e` und die nur sechs
Byte lange Antwort: Sie entspricht nicht der normalen zehn Byte langen
Zahlenantwort. Danach werden die ergänzenden Daten abgeholt. In sämtlichen
271 vollständig beobachteten Abfragen `06 22 / 01890000` ist die vorherige
vollständige Transaktion von Master 01 an Slave 15 `06 21 / 0109`.

Für den zusätzlichen Kontext lautet dieselbe Sequenz
`06 21 / 01891000`, `06 22 / 01891000`, `06 22 / 01891100`
(Logzeilen 1981–1983). Auch bei allen 49 vollständigen Abfragen des ersten
ergänzenden Blocks dieses Kontexts geht die entsprechende `06 21`-Abfrage
unmittelbar voraus, wenn man nur vollständige Transaktionen 01 → 15 betrachtet.

Die wahrscheinlichste Aufteilung der `06 22`-Anfrage ist damit:

```
01       Menü
89       Eintragsindex 09 mit gesetztem Erweiterungsbit
00 / 01  Teilblock im Grundkontext
10 / 11  Teilblock im zusätzlichen Kontext
00       weiteres Adressbyte; Bedeutung offen
```

Die genaue Bitaufteilung von Kontext und Teilblock bleibt eine Hypothese.
Die kurze zweite Antwort passt zu einer Fortsetzung mit insgesamt zwölf
Nutzdatenbytes. Ob die Teilblöcke direkt verkettet werden dürfen oder eigene
Kopffelder besitzen, ist nicht bewiesen. Ebenso ist offen, ob `05 00` in der
`06 21`-Antwort eine Anzahl, eine Kapazität oder andere Metadaten bezeichnet.

Alle 637 vollständigen `06 22`-Antworten enthalten unverändert die beiden
oben gezeigten Nutzlasten, in beiden Kontexten. Es gibt deshalb keinen
Inhaltswechsel, mit dem sich einzelne Felder semantisch identifizieren ließen.

Eine Fehler-/Meldungsliste wäre eine plausible Anwendung: Der Inhalt wird
wiederholt zusammen mit Statusparametern abgefragt, und viele `ff`-Bytes könnten
unbelegte Plätze kennzeichnen. Das ist aber **kein Nachweis eines Fehlerspeichers**.
Auch andere strukturierte Statusdaten sind möglich. Eine Liste von Auswahltexten
oder ein allgemeines Parameterverzeichnis wird durch die beobachteten Antworten
nicht gestützt; lesbarer Text und eine Folge von TEM-Kennungen sind darin nicht
erkennbar.

Für eine weitere Entschlüsselung wäre eine Aufzeichnung hilfreich, in der
02-12 tatsächlich einen anderen Inhalt liefert, etwa zusammen mit einer
bekannten, ohnehin auftretenden Meldung und der zugehörigen Anzeige am Bedienteil.
Bis dahin sollten die Antworten als Rohdaten erhalten bleiben.
