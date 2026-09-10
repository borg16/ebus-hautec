# eBUS-Protokoll-Referenz: Hautec Wärmepumpe (2007)
**Controller:** TEM SE 6000 WPC (TEM ID: 17385 | SW: 0106 | HW: 0100)
**Bedienteil:** TEM HFB 5811 W Split (2 Einheiten vorhanden)

## 1. Physikalische eBUS-Topologie
Der Controller nutzt eine proprietäre Master-Slave-Architektur, bei der die Datenpunkte vorrangig blockweise (als Byte-Arrays) zwischen dem Controller und den Fernbedienungen (HFB 5811) ausgetauscht werden. Der Hauptregler fungiert als aktiver eBUS-Master, holt Konfigurationsblöcke zyklisch ab und spiegelt geänderte Werte zurück.

| eBUS-Adresse (Hex) | Komponente / Funktion | TEM-Interne ID / Typ |
| :--- | :--- | :--- |
| **`10`** | Hauptregler TEM SE 6000 WPC (Master) | Master #2 |
| **`15`** | Hauptregler TEM SE 6000 WPC (Slave) | Speicheradresse (EEPROM) |
| **`03`** | Burner 1 (Master-Logik) | Master #11 (Zonenzuordnung HK1) |
| **`90`** | Fernbedienung FB 1 (Slave-Logik) | Spiegelregister für HK1 (Blöcke 04–09) |
| **`13`** | Burner 2 (Master-Logik) | Master #12 (Zonenzuordnung HK2/WW) |
| **`91`** | Fernbedienung FB 2 (Slave-Logik) | Spiegelregister für WP (Blöcke 0A–13) |
| **`31`** / **`36`** | eBUS-Adapter (Shield C6) | Master #8 / Slave #8 |

---

## 2. Telegramm-Struktur (TEM Proprietary)
TEM verwendet herstellerspezifische Service-IDs und verarbeitet Daten vorzugsweise in Blöcken (`20 xx` für Abfragen, `30 xx` für Datensätze/Antworten).

### Aufbau eines Standard-Telegramms:
`[Quell-ADR] [Ziel-ADR] [TEM-Service] [Länge] [Befehls-Code] [Payload...] / [Antwort-Länge] [Antwort-Payload...]`

* **TEM-Service-ID:** **`10 0A`**

---

## 3. Aufgeschlüsselte Datenblöcke & Menüebenen

### Ebene 01/03: Heizkreis- & Komfortparameter (Adresse `90`)
Der Controller ruft zyklisch den Zustand der Fernbedienung FB 1 ab.
`10 90 10 0A 0E D0 14 27 03 9F 90 1F 90 28 90 03 FF EF EF`
Diese antworten in der selben Nachricht mit `02 C0 00` falls keine neuen Daten vorliegen. FB 2 wird mit `10 91 10 0A 0E D0 15 06 03 09 91 1d 91 2e 91 03 FF EF EF` abgefragt und antwortet entsprechend. Die Befehlscodes sind also [`D0 14`](signals.tsp#L163)  und [`D0 15`](signals.tsp#L177).

Im Fall einer beispielhaften Datenänderung werden mehrere Blockpaare abgefragt. Die genaue Zuordnung zu einem einzelnen Menüparameter ist aus diesem Mitschnitt allein noch nicht gesichert:

```text
10 90 10 0a 0e **d1 14** 03 ff 04 90 03 ff 03 ff 03 ff 03 ff / 00
10 90 10 0a 0e **d0 14**  27 03 a0 90 1f 90 29 90 03 ff ef ef / 02  **40 01**
10 90 10 0a 02 **21 01** / 0e 31 01 00 00 dc 00 00 00 3c 00 00 00 00 00
10 90 10 0a 02 **20 01** / 0e 30 01 c8 00 b4 00 f4 01 01 00 00 00 a2 90
10 90 10 0a 0e **d1 14** 03 ff 04 90 03 ff 03 ff 03 ff 03 ff / 00
10 90 10 0a 0e **d0 14** 27 03 a2 90 1f 90 29 90 03 ff ef ef / 02 40 03
10 90 10 0a 02 **21 03** / 0e 31 03 64 00 14 00 00 00 00 00 00 00 c0 01
10 90 10 0a 02 **20 03** / 0e 30 03 00 ff 96 00 **a3** 00 00 00 00 00 2b 90
10 90 10 0a 0e **d1 14** 03 ff 04 90 03 ff 03 ff 03 ff 03 ff / 00
10 90 10 0a 0e **d0 14** 27 03 a2 90 1f 90 29 90 03 ff ef ef / 02 c0 00
```

Die gleiche Änderung sieht bei FB 2 so aus:

```text
10 91 10 0a 0e **d1 15** 03 ff 03 ff 03 ff 03 ff 03 ff 03 ff / 00
10 91 10 0a 0e **d0 15** 06 03 0b 91 1d 91 2f 91 03 ff ef ef / 02 40 0b
10 91 10 0a 02 **21 0b** / 0e 31 0b 00 00 dc 00 03 00 64 00 00 00 00 00
10 91 10 0a 02 **20 0b** / 0e 30 0b c8 00 af 00 f4 01 01 00 00 00 14 91
10 91 10 0a 0e **d1 15** 03 ff 03 ff 03 ff 03 ff 03 ff 03 ff / 00
10 91 10 0a 0e **d0 15** 06 03 14 91 1d 91 2f 91 03 ff ef ef / 02 40 0d
10 91 10 0a 02 **21 0d** / 0e 31 0d 32 00 14 00 00 00 00 00 00 00 c0 01
10 91 10 0a 02 **20 0d** / 0e 30 0d 00 ff a0 00 **a3** 00 b0 04 00 00 30 91
10 91 10 0a 0e **d1 15** 03 ff 03 ff 03 ff 03 ff 03 ff 03 ff / 00
10 91 10 0a 0e **d0 15** 06 03 14 91 1d 91 2f 91 03 ff ef ef / 02 c0 00
```

`signals.tsp` bildet die beobachteten Paare wie folgt ab:

| Telegrammpaar | Definition in `signals.tsp` | Status |
| :--- | :--- | :--- |
| `20 01` / `30 01` | [`BasisTemperaturen01Bedienteil1`](signals.tsp#L514) | Raum-Soll Tag/Nacht und Warmwasser-Soll, FB 1 (`90`) |
| `20 03` / `30 03` | [`Heizgrenzen03Bedienteil1`](signals.tsp#L528) | Heizgrenze und Heizgrenze-Absenkung, FB 1 (`90`) |
| `21 01` / `31 01` | [`Kuehlgrenzen2101Bedienteil1`](signals.tsp#L602) / [`Parameterblock3101Bedienteil1`](signals.tsp#L338) | weiterer Parameterblock, teilweise dekodiert |
| `21 03` / `31 03` | [`Raumschutz2103Bedienteil1`](signals.tsp#L618) / [`Parameterblock3103Bedienteil1`](signals.tsp#L410) | weiterer Parameterblock, teilweise dekodiert |

Damit sind `20 xx` und `21 xx` Abfragen; die im Mitschnitt sichtbaren Antworten tragen jeweils dieselbe Blocknummer als `30 xx` bzw. `31 xx`. Eine Zuordnung zu `30 04` bis `30 06` ist durch `signals.tsp` nicht belegt.

#### Block `20 01` (Basis-Temperaturen)
* **Hex-Muster:** `0e 30 01 c8 00 b4 00 f4 01 01 00 00 00 31 90`
* **Byte-Bedeutung:**
  * Byte 3–4: `c8 00` $\rightarrow$ `00c8` hex = 200 dezimal $\rightarrow$ **20.0 °C** (Raum-Soll Tag)
  * Byte 5–6: `b4 00` $\rightarrow$ `00b4` hex = 180 dezimal $\rightarrow$ **18.0 °C** (Raum-Soll Nacht)
  * Byte 7–8: `f4 01` $\rightarrow$ `01f4` hex = 500 dezimal $\rightarrow$ **50.0 °C** (Warmwasser-Soll)
  * Die letzten zwei Bytes bilden ein eigenes, persistent gespeichertes
    Schlüsselwort; siehe Abschnitt „Änderungsschlüssel“ weiter unten. Sie
    sind nicht als Prüfsumme der vorherigen sichtbaren Werte zu behandeln.

#### Block `20 03` (Heizgrenze / Heizgrenze-Absenkung)
* **Hex-Muster:** `0e 30 03 00 ff a0 00 a8 00 00 00 00 00 18 90`
* **Byte-Bedeutung:**
  * Nach [`Heizgrenzen03Bedienteil1`](signals.tsp#L528) sind die ersten zwei Bytes nach `30 03` reserviert; danach folgen zwei `Temp10`-Werte: **Heizgrenze** und **Heizgrenze-Absenkung**.
  * Eine Bedeutung als Heizkurven-Offset oder Fußpunkt ist in `signals.tsp` nicht definiert und bleibt daher offen.

---

### Ebene 09: Fachmann-Konfiguration (Adresse `90`)
Dieser Block bestimmt das grundlegende hydraulische Verhalten und die Freigabe von Zusatz-Erzeugern.

#### Block `20 09` / `30 09` (Konfigurationsmatrix)
* **Hex-Muster:** `0e 30 09 00 01 00 00 00 00 00 00 00 00 03 ff`
* **Dekodierung in `signals.tsp`:** [`FachmannKonfiguration09Bedienteil1`](signals.tsp#L483) (FB 1, `90`) und [`FachmannKonfiguration09Bedienteil2`](signals.tsp#L493) (FB 2, `91`) verwenden `Konfigurationsmatrix`.
  * `Anlagenschema`: `00` ist als Standard-Heizkreis/WW, `04` als Kühlbetrieb hinterlegt.
  * `ZusatzerzeugerFreigabe`: im Mitschnitt `01`; die fachliche Wirkung ist bisher eine Arbeitshypothese.
  * Die restlichen Bytes werden überwiegend als reserviert geführt; `Kaskadenwert` und ein abschließendes Byte werden separat ausgegeben.

---

### Ebene 11 bis 19: Wärmepumpen- & Kältekreis-Parameter (Adresse `91`)
Diese Blöcke werden über die zweite Fernbedienung (Adresse `91`) gespiegelt. Ihre fachliche Bedeutung ist überwiegend noch nicht entschlüsselt.
* `signals.tsp` enthält generische Lesedefinitionen für Menü `0f` sowie `11` bis `13` ([`WaermepumpenStufenKonfiguration15Bedienteil2`](signals.tsp#L563), [`FachmannKonfiguration17Bedienteil2`](signals.tsp#L573), [`FachmannKonfiguration18Bedienteil2`](signals.tsp#L583), [`FachmannKonfiguration19Bedienteil2`](signals.tsp#L593)). Nur `0f` ist dort als „Kerndaten der Wärmepumpen-Stufen“ bezeichnet.
* Die Blöcke `0b` und `0d` sind im Mitschnitt vorhanden, aber nur teilweise dekodiert. Wo die Bedeutung offen ist, heißen die Modelle absichtlich `Parameterblock…`. Eine Zuordnung zu Mindestlaufzeit, Hysterese oder Abtauung ist folglich noch nicht validiert.

---

## 4. Sichere Abfrage mit der ebusctl-Konsole

### Passiver Lese-Test (Block 09 von FB 90 anfordern)
```bash
ebusctl hex 90100a022009
```
*Antwortet mit der aktuellen Konfigurations-Matrix des Fachmann-Menüs.*

`signals.tsp` definiert die betrachteten Signale als eingehende/passive Lesedaten; auch die Projektbeschreibung nennt keine Unterstützung zum Senden von Steuerbefehlen. Daher sind Schreibtelegramme für Menü 09 derzeit **nicht verifiziert** und werden hier bewusst nicht angegeben. Insbesondere lassen sich die angenommene Freigabewirkung und ein Wechsel des Anlagenschemas nicht sicher aus der vorhandenen Definition ableiten.

---

## 5. Hinweise für den ebusd-CSV-Syntax-Entwurf
Wenn du hieraus eine feste Konfigurationsdatei (z.B. `tem_se6000.csv`) erstellst, beachte folgende Zuordnungen:
* Die vorhandenen TypeSpec-Modelle emittieren Lesetelegramme (`r`) für die Zieladressen `90` und `91`; nur die passiv beobachteten Anfragen an die Feuerungsautomaten sind als `@write @passive` markiert.
* Für bestätigte Felder werden `Temp10`, `UCH`, `BCD` und begrenzte `HEX`-Felder verwendet. Nicht entschlüsselte Daten bleiben als `HEX` erhalten, statt ihnen eine Steuerfunktion zuzuschreiben.

---

## 6. Start-Synchronisation, Parameterspiegel und Schreibhypothese

Der in [`FB-Initialization.md`](FB-Initialization.md) protokollierte
Systemstart zeigt eine andere Richtung als der zyklische Änderungsabgleich:

| Phase | Beobachtete Folge | Interpretation |
|---|---|---|
| Start, Gruppe `nn` | `10 -> 90: d1 14`, `d0 14`; Antwort `02 50 nn`; danach `10 -> 90: 31 nn` und `30 nn` | Der Hauptregler überträgt seinen vollständigen Parameterspiegel an FB 1. Bei großen Gruppen folgen mehrere Teilblöcke, z. B. `37` bis `30`. |
| Bedienänderung an FB 1 | `d0 14` meldet `40 nn`; danach liest der Regler `21 nn`/`20 nn`, FB antwortet mit `31 nn`/`30 nn` | Die FB meldet geänderte lokale Blöcke, die der Regler anschließend abholt. |

Damit ist die naheliegende, aber noch unbewiesene Architektur: Die FB hält
einen lokalen Parameter-Cache. Ein vom Adapter als Master `31` direkt an
Slave `90` gesendeter `30`-/`31`-Block könnte diesen Cache ändern, aber der
Regler könnte ihn beim nächsten Start oder Synchronisationszyklus wieder
überschreiben. Dies ist daher **kein Nachweis eines dauerhaften Schreibwegs
zum Controller**.

Für die eigentliche Ermittlung eines Schreibtelegramms ist ein kontrollierter
Mitschnitt am aussagekräftigsten: Original-ServiceTool eine Einstellung
ändern lassen, während der vorhandene Adapter nur passiv mitschneidet. Dabei
pro Versuch genau einen Wert ändern, vorher/nachher alle vollständigen Blöcke
lesen und die unbekannten Bytes unverändert lassen. Der Adapter darf nicht
die Adresse `10` verwenden, da dies die Master-Identität des Hauptreglers
duplizieren würde.

### Bestätigte Felder in den Startblöcken

| Block | Feldposition nach `30 xx` / `31 xx` | Dekodierung | Wert beim Start |
|---|---:|---|---:|
| `30 01` | 0–1 | Raum-Soll Heizbetrieb, `Temp10` LE | 20,0 °C |
| `30 01` | 2–3 | Raum-Soll Absenkbetrieb, `Temp10` LE | 18,0 °C |
| `30 01` | 4–5 | Wasser-Soll, `Temp10` LE | 50,0 °C |
| `31 01` | 2–3 | Kühltemperatur, `Temp10` LE | 22,0 °C |
| `31 01` | 6–7 | Kühlgrenzabstand, `Temp10` LE | 6,0 K |
| `30 02` | 0 | Steilheit Heizkurve | 30 |
| `30 02` | 8–9 | Fußpunkttemperatur, `Temp10` LE | 22,0 °C |
| `31 03` | 0–1 | Raumschutztemperatur, `Temp10` LE | 10,0 °C |
| `30 03` | 2–3 | Heizgrenze, `Temp10` LE | 16,5 °C |
| `30 03` | 4–5 | Heizgrenze Absenkbetrieb, `Temp10` LE | 16,3 °C |

### Änderungsschlüssel in `30 01`

Die Antwort auf `90100a022001` enthält nach der Längenangabe `0e` den
14-Byte-Block `30 01`. Die letzten zwei Bytes sind damit Anwendungsdaten,
nicht die eBUS-Transport-Prüfsumme. Ein Einzelfeldversuch ergab:

| Zustand | Ende des Blockes |
|---|---|
| 20,0 / 18,0 / 50,0 vor Änderungen | `ad 90` |
| 19,5 / 18,0 / 50,0 | `b6 90` |
| 20,0 / 18,5 / 50,0 | `ba 90` |
| auf 20,0 / 18,0 / 50,0 zurückgestellt | `c7 90` |
| ohne Änderung erneut gelesen | `c7 90` |

Dass beim Zurückstellen auf exakt dieselben Nutzdaten `ad 90` nicht wieder
hergestellt wurde, schließt eine reine Prüfsumme über den sichtbaren
Blockinhalt aus. Hypothese: 16-Bit-Änderungs-, Commit- oder Versionsschlüssel
der FB. Das High-Byte ist in allen bisherigen Beobachtungen `90`, das
Low-Byte verändert sich bei einer gespeicherten Änderung und bleibt ohne
weitere Änderung konstant. Seine Vergabe ist derzeit nicht herleitbar.

## 7. TEM ServiceTool V0.53 und ZIF280

Für die Entschlüsselung eines **dauerhaften** Schreibwegs ist das
Originalwerkzeug besonders interessant:

* Ein historischer Katalog beschreibt das `ZIF 280` als USB-eBUS-Interface
  samt Service-Software für Inbetriebnahme, Wartung, Datenaufzeichnung sowie
  Up-/Download von Reglerdaten; ausdrücklich genannt werden R25, R35 und
  R40. Die Kompatibilität zum älteren SE 6000 WPC ist daraus nicht ableitbar.
  [Katalogeintrag](https://www.simesystems.de/?media_dl=600)
* Ein TEM-Anwender dokumentierte 2014 ein ZIF280 mit ServiceTool V0.53 und
  berichtet, dass die Originalsoftware das Interface als Dongle abfragt.
  Software und Interface müssen deshalb zusammen getestet werden.
  [HaustechnikDialog](https://www.haustechnikdialog.de/forum/t/95477/PC-Ueberwachung-eBus-fuer-Regelung-TEM-PM-2975-OGZ?PostSort=1&page=2)
* Im selben Forum wurde 2025 ein PL2303TA-Treiberproblem unter Windows 11
  berichtet. Ein älterer Windows-Rechner oder eine VM mit USB-Durchreichung
  ist für einen Test daher sinnvoll.
* Das ZIF280 ist voraussichtlich nicht als `ebusd`-Adapter verwendbar. Ein
  Anwender erhielt damit „No Signal“; der Autor von `ebusd` bezeichnete das
  verwendete Host-Protokoll als OpenTherm statt eBUS.
  [FHEM-Diskussion](https://forum.fhem.de/index.php?topic=61017.15)

Es wurde kein aktueller, verifizierter Vermieter für ein ZIF280 gefunden. Die
passendste Leihanfrage ist im oben verlinkten HaustechnikDialog-Thread; dort
sind ZIF280-Besitzer nachweisbar und der Thread hatte 2025 noch Aktivität.
Für den Mitschnitt muss das ZIF280 nicht mit `ebusd` funktionieren: Es würde
die Änderung mit dem ServiceTool ausführen, während der vorhandene Adapter
den eBUS parallel passiv aufzeichnet.
