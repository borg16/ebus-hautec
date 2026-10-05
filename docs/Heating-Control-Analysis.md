# Heizkreise, Warmwasser und Pumpensteuerung der Hautec-HWM-Anlage

**Vor-Ort-Klärung vom 03.10.2026 zu TEM 7/8:** Der Betreiber bestätigt nach
Prüfung, dass die geschalteten Ausgänge 7 und 8 nicht beschaltet sind. Lediglich
der N-Anschluss des Anschlussblocks 8 wird verwendet. Der zuvor anhand des
Fotos entstandene Verdacht zusätzlicher Ausgangsfunktionen ist damit ausgeräumt.
Der Schaltplan bleibt nach Betreiberangabe die Grundlage für die reale Anlage;
die Nutzung des N-Anschlusses ist keine Pumpenansteuerung durch HK2.
Siehe [aktuelle Klemmenanalyse](Heating-Terminal-Analysis-2026-10-03.md).

**Nachbeobachtungen vom 30.09.2026:** Der Betreiber bestätigt nach erneuter
Prüfung beide Zustände: Beim Kühlen ohne Warmwasserbereitung läuft
**M4.1 durchgehend**, auch während der Pausen der Solewärmepumpe. Beim Kühlen
während Warmwasserbereitung laufen **M5 und M4.2**; **M4.2 läuft auch während
der Kühlverdichterpausen weiter**. Damit ist die unterschiedliche Pumpenauswahl
zwischen den Betriebsarten bestätigt. Volumenstrom, genauer Umschaltzeitpunkt
und eine fehlerhafte Pumpenauswahl sind damit nicht nachgewiesen.
Diese Nachbeobachtungen ersetzen keine synchronen Pumpenmessungen der früheren
Mitschnitte. Einordnung in der [Auswertung vom 30.09.](Cooling-Test-2026-09-30.md).

**Nachtrag vom 28.09.2026:** Der Kühlbetrieb wurde inzwischen mit der aktuellen
Konfiguration geprüft. Der Mitschnitt zeigt vier Abschnitte mit 100 % gemeldetem
Stellgrad, dazwischen 50 %, und wiederkehrende Rückschaltungen bei etwa
17–17,5 °C. 07-14 ist im Versuch für beide Heizkreise auf 3 zurückgelesen.
Der Betreiber bestätigt anhand einer Leistungsmessung mit etwa 5 s Auflösung
und 1,25-kW-Stufen den Soleverdichterlauf; der Abluftverdichter war während
des gesamten Versuchs aus. 50 % Bus-Stellgrad belegt hier daher keinen
laufenden Abluftverdichter. M4.1 wird aufgrund einer früheren Prüfung
vermutet, wurde in diesem Versuch aber nicht kontrolliert.
Die [Auswertung des Kühlversuchs](Cooling-Log-Analysis.md) ergänzt die unten
historisch festgehaltene Aussage, dass der erneute Kühltest noch ausstand.

Stand: 26.09.2026. Auswertung der bereitgestellten Anlagenpläne, der
Parameterbeschreibungen und der im Gespräch mitgeteilten Betriebsbeobachtungen.
Es wurden dafür keine Einstellungen an der Anlage verändert.

## Ergebnis und Beleglage

Die Anlage besitzt einen gemeinsamen Fußbodenheizkreis, den eine Abluft- und
eine Erdwärmepumpe versorgen können. Zwei Heizungs-Pumpenwege bedeuten hier
nicht zwei getrennte Heizzonen. Die Hautec-Bezeichnungen „Heizkreispumpe I/II“,
die TEM-Reglerfunktionen HK1/HK2 und die Bediengeräte FB1/FB2 sind zu unterscheiden.

- **Aus dem Schaltplan abgelesen:** TEM-Ausgang 6 versorgt über K11 wahlweise
  M4.1 oder M4.2. Beide Heizkreispumpen teilen sich einen Pumpenausgang.
- **Aus dem Schaltplan abgelesen:** Ausgang 15, beschriftet mit „Heizkreis 2 + /
  Mischer“, führt zum Steuereingang von KT15. Dessen Kontakt wirkt auf K3.
  Ein Mischerausgang wird für die Wärmeerzeugeransteuerung verwendet.
- **Vom Betreiber bestätigt:** Aktuell ist 07-05 für HK1 auf **2**, für HK2 auf
  **0** eingestellt. Das bei der früheren Einstellung **0/3** beobachtete
  Warmwasserproblem tritt mit **2/0** nicht auf.
- **Vom Betreiber beobachtet:** Nach Ende der Warmwasserbereitung und Übernahme
  der Raumheizung durch die Abluft-Wärmepumpe wechselte **01-21 HK2 von 0 % auf
  −100 %**.
- **Vom Betreiber am Gerät abgelesen:** KT15 ist ein ABB CT-MFE mit
  Ausschaltverzögerung von **1000 s (16 min 40 s)** für den Steuereingang Y1.
  Die Versorgung an A1/A2 muss während des Zeitablaufs bestehen bleiben.
- **Vom Betreiber synchron bestätigt (26.09.2026):** Bit 6 in Broadcast
  `10 0A / 11 01` entspricht der Anzeige „Mischventil Heizkreis zu“ auf FB2
  (`OperatingStatus_1101.Mixer_Close`, zuvor `Flag6`).
- **Offen:** Die genaue Firmware-Zuordnung aller HK-/FB-Statusfelder zu den
  Ausgängen und die Ursache des früheren Warmwasserabbruchs.

„Aus dem Schaltplan abgelesen“ bezeichnet die dokumentierte Verdrahtung, nicht
eine durch Messung bestätigte Übereinstimmung mit der heute eingebauten Anlage.

## Herkunft und zeitliche Einordnung der Einstellungen

Der Betreiber hat am 26.09.2026 die Herkunft der Unterlagen klargestellt:

Die Dateien in `ste-output/` wurden aus einer `.ste`-Datei eines ansonsten
unbekannten Konfigurationsprogramms extrahiert. Die Programmiercheckliste
war ursprünglich eine Excel-Datei. Vom Betreiber berichtete gemeinsame
Rechtschreibfehler deuten auf eine gemeinsame Textgrundlage hin; sie belegen
keine identische Firmware oder Konfiguration. Das Beispiel
„Multifunktionsusgang“ ist im STE-Export vorhanden, war in der originalen Excel-Datei genauso geschrieben. Die Herkunft und
Beleggrenzen sind in [STE-Format.md](STE-Format.md#herkunft-und-beziehung-zur-programmiercheckliste)
festgehalten.

- **[Parameter.md](../ste-output/Parameter.md)** enthält die tatsächlichen
  Einstellungen dieser Anlage **vor der Nachrüstung der Kühlfunktion**.
  Darin können spezielle lokale Anpassungen enthalten sein. Die Werte sind
  daher als historischer Anlagenstand und nicht als bloße Standardvorlage zu lesen.
- **[Programmiercheckliste](../input/Checkliste_Regler_Programmierung.CSV)**
  beschreibt die üblichen Einstellungen des Werkskundendienstes. Die letzte
  beschriftete Variantenspalte „Mono heiz-kühl“ enthält die normalerweise dafür
  vorgesehene Konfiguration. Der Werkskundendienst kennt nach Betreiberangabe
  den eventuell besonderen Anlagenaufbau nicht; die Checkliste belegt daher
  weder die individuelle Sollkonfiguration noch die tatsächlich gesetzten Werte.
- Der vollständige Einstellungsstand **nach der Kühlnachrüstung und vor dem
  späteren Konfigurationsverlust ist unbekannt**. Einzelne Mitschnittwerte
  bleiben eigenständige Belege und keine vollständige Momentaufnahme.
- **Aktueller Stand nach Betreiberangabe vom 26.09.2026:** Vor einigen Tagen
  gingen alle Einstellungen verloren; ein Werksreset ist eine vermutete,
  nicht bestätigte Ursache. Der Betreiber hat alle Einstellungen aus
  `Parameter.md` wiederhergestellt und zusätzlich **09-07 im Wärmepumpen-Kontext
  auf 6 (mit Kühlfunktion)** gesetzt. Diese Angabe beschreibt den derzeitigen
  Stand; eine vollständige Rücklesung wurde hier noch nicht ausgewertet.
  Das bisher beobachtete Verhalten erscheint dem Betreiber wie vor dem
  Konfigurationsverlust. Aus dem bisher ähnlichen
  Verhalten folgt keine bewiesene Gleichheit aller früheren und heutigen
  Parameterwerte.

Für die Regelungsanalyse ist insbesondere **09-11 im Wärmepumpen-Kontext**
zu unterscheiden: Vor der Kühlnachrüstung war tatsächlich **0** eingestellt.
Die Checkliste nennt **5 für Mono** und **6 für Mono heiz-kühl**. Diese
Abweichung darf nicht als nachgewiesener Fehler oder als Beleg einer späteren
Umstellung auf 6 gewertet werden. Die Vermutung, dass gerade Modus 5/6 die
besondere Aufteilung von Warmwasser- und Heizbetrieb erklärt, ist damit für
den historischen Anlagenstand nicht belegt. Der genaue Algorithmus bleibt offen.

## Quellen

| Quelle | Verwendung |
|---|---|
| [Hydraulikschema](input/hydraulik.png) | Leitungswege und Betriebsnotizen |
| [Pumpenanordnung](input/pumpenanordnung.png) | Heizkreispumpe I (HWAL), Heizkreispumpe II (HCS), Speicherladepumpe |
| [Steuerschaltplan, gut lesbare Fassung](input/steuerschaltplan.jpg) | TEM-Klemmen, Relais und Motoren |
| [Legende 1](input/schaltplan_legende1.jpg) | Motoren, Schütze und Hilfsrelais |
| [Legende 2](input/schaltplan_legende2.jpg) | Heizstab, Ventile und Schalter |
| [Controllerfoto](input/tem_se_6000_wpc.png) | Anschlussbeschriftungen |
| [KT15-Foto](../input/kt15.jpg) und Betreiberangabe zur Einstellung | ABB CT-MFE; Y1; Ausschaltverzögerung 1000 s |
| [STE-Parameterkatalog](../ste-output/Parameter.md) | Tatsächliche Einstellungen vor der Kühlnachrüstung sowie Parametertexte |
| [Sitzungsvergleich](Session-Comparison.md) | Historische Mitschnittwerte, insbesondere 07-05 = 0/3 |
| Betreiberangaben im Gespräch vom 25.09.2026 | Aktuelle Einstellung 2/0, Warmwasserproblem mit 0/3 und Änderung von 01-21 HK2 |

Die Betriebsbeobachtungen liegen als Gesprächsbericht vor. Ein zeitlich
synchroner Mitschnitt von Temperaturen, Statusanzeigen und realen
Schaltzuständen wurde dazu noch nicht ausgewertet.

## Hydraulische Funktionen

Nach Betreiberangabe bereitet die Abluft-Wärmepumpe vorrangig Warmwasser.
Wenn sie dafür nicht benötigt wird, kann sie die Raumheizung versorgen.
Die Erdwärmepumpe unterstützt bei zusätzlichem Heizbedarf. Beide Wärmeerzeuger
können getrennt oder gleichzeitig laufen.

| Kennzeichen | Bezeichnung | Aus dem Schema abgeleiteter Zweck |
|---|---|---|
| M4.1 | Heizkreispumpe I (HWAL) | Heizungsweg unter Einbeziehung des Abluft-Wärmetauschers |
| M4.2 | Heizkreispumpe II (HCS) | Heizungsweg über die Erdwärmepumpe, unter Umgehung des Abluft-Wärmetauschers |
| M5 | Speicherladepumpe | Umwälzung für die Speicherladung |
| M3 | Wärmequellenpumpe laut Legende | Zusätzliche Quellenpumpe; nicht eine der drei oben dargestellten Pumpen |
| M17 | Lüfter HWAL | Abluftförderung |

Die allgemeinen WP1-/WP2-Bezeichnungen der Legende sind nicht ohne Prüfung
mit den TEM-Menükontexten, eBUS-Geräten oder den Wärmequellen gleichzusetzen.

Der Weg über M4.1 sieht nach einer Reihenschaltung der Heizwasser-Wärmetauscher
aus. Gleichzeitig laufende Verdichter bedeuten daher nicht zwingend eine
hydraulische Parallelschaltung der Wärmetauscher.

Das Rechteck unter der handschriftlichen Bezeichnung „HzV“ lässt sich zusammen
mit der Pumpendarstellung plausibel als elektrischer Durchlaufheizer deuten.
Ein motorisch geregelter Heizkreismischer ist in den vorliegenden Unterlagen
nicht nachgewiesen. E1 ist in der elektrischen Legende ausdrücklich als
Elektroheizstab bezeichnet; Y2 als Magnetventil Heizen/Kühlen.

## Elektrische Zuordnung

| TEM-Klemme | Beschriftung am Controller | Im Steuerschaltplan erkennbarer Anschluss |
|---|---|---|
| 6 | Heizkreispumpe 1 | Gemeinsame Versorgung der Pumpenauswahl über K11 |
| 7 | Kondensatorpumpe | Geschalteter Ausgang unbeschaltet; Plan und Betreiberprüfung vom 03.10.2026 stimmen überein |
| 8 | Heizkreispumpe 2 / Mischer | Geschalteter Ausgang unbeschaltet, vor Ort bestätigt; nur der zugehörige N-Anschluss wird verwendet |
| 9 | Magnetventil Heizen/Kühlen | K4 und Y2 |
| 10 | Beschriftung im Foto teilweise verdeckt | K2, laut Legende Heizstabschütz |
| 11 | Separate Warmwasser-Wärmepumpe | Unter anderem K11; zusätzlich Verknüpfung über einen K4-Kontakt |
| 13 | WW ein / Ladepumpe / Umlenkventil | Speicherladepumpe M5 |
| 15 | Heizkreis 2 + / Mischer | Steuereingang Y1 von KT15 |
| 16 | Heizkreis 2 − / Mischer | Im gezeigten Plan nicht angeschlossen |
| 26 | WE2, geschalteter Anschluss | Versorgung A1 von KT15 |

### Pumpenauswahl über K11

| Ausgang 6 | K11 | Elektrisch versorgte Heizkreispumpe |
|---|---|---|
| Aus | Beliebig | Keine der beiden |
| Ein | Abgefallen | M4.1 über Ruhekontakt 41–42 |
| Ein | Angezogen | M4.2 über Arbeitskontakt 21–24 |

Die Tabelle beschreibt die Kontaktschaltung ohne Störung, keinen nachgewiesenen
Pumpenlauf oder Volumenstrom. M5 wird separat über Ausgang 13 angesteuert.

### Mischerausgang als Wärmeerzeugeransteuerung

Die abgelesene Signalkette lautet:

```text
TEM 15 (Heizkreis 2 +) ──> KT15, Steuereingang Y1
TEM 26 (WE2)           ──> KT15, Versorgung A1
KT15, Kontakt 15–18    ──> K3, Spule
```

Die Kontaktnummern 15–18 am Relais sind nicht mit den TEM-Klemmen zu verwechseln.
KT15 ist laut Foto ein **ABB CT-MFE**. Der Betreiber hat am Gerät eine
**Ausschaltverzögerung von 1000 s (16 min 40 s)** abgelesen. Der Steuereingang
heißt **Y1**; die frühere Bezeichnung B1 war falsch.

Bei vorhandener Versorgung an A1/A2 gilt laut ABB-Funktionsbeschreibung:

| Ereignis | Reaktion von KT15 |
|---|---|
| Steuersignal an Y1 wird aktiv | Relais zieht sofort an; Kontakt 15–18 schließt |
| Steuersignal an Y1 fällt weg | Die Ausschaltverzögerung von 1000 s beginnt; Kontakt bleibt geschlossen |
| Y1 wird vor Ablauf erneut aktiv | Zeitablauf wird zurückgesetzt; Kontakt bleibt geschlossen. Erst der nächste Signalwegfall startet die vollen 1000 s erneut |
| 1000 s ohne erneutes Steuersignal sind abgelaufen | Relais fällt ab; Kontakt 15–18 öffnet |
| Versorgung an A1/A2 fällt weg | Relais fällt ohne die eingestellte Verzögerung ab; Zeitablauf wird zurückgesetzt |

Damit können Auf-Impulse des HK2-Ausgangs über KT15 eine anhaltende
Schützansteuerung erzeugen, sofern die Impulspausen kürzer als 1000 s sind
und TEM 26 die Versorgung aufrechterhält. Dies erklärt eine mögliche Nutzung
der Mischerregelung ohne Mischermotor; die tatsächliche Impulsfolge wurde
noch nicht aufgezeichnet.

Die 1000 s sind **keine garantierte Mindestlaufzeit des Verdichters**: Die
Verzögerung beginnt mit dem Wegfall von Y1, und die Versorgung über TEM 26
kann sie jederzeit beenden. Auch andere Freigaben und Schutzkontakte sind
für den tatsächlichen Verdichterlauf maßgeblich. Ausgang 15 allein beweist
keinen laufenden Verdichter.

Quelle: [ABB CT-MFE, Datenblatt, S. 2, Rückfallverzögerung](https://library.e.abb.com/public/10c49196c23c80a0c12575f400340e36/2CDC111032D0201.pdf).
Die Funktion stammt aus dem Datenblatt, der konkrete Einstellwert aus der
Ablesung des Betreibers.

Die Legende nennt **K15** ein Multifunktionsrelais „bei Ansteuerung über
Mischerkontakt“, während der Plan **KT15** schreibt. Die funktionale
Übereinstimmung stützt die Interpretation; die unterschiedliche Benennung
bleibt als Dokumentationsabweichung bestehen; das Relaismodell ist durch das
Foto geklärt.

**Korrektur früherer Deutungen:** K3 ist laut Legende das Kompressorschütz WP2,
K2 das Heizstabschütz. Der K3-Kontakt 21–22 im E1-Zweig ist ein zusätzlicher
Öffnerkontakt, nicht der Beleg, dass K3 das eigentliche Heizstabschütz wäre.
Die zuerst als „114.1“, „114.2“ und „115“ gelesenen Kennzeichen sind
M4.1, M4.2 und M5.

## Parameter 07-05 und bekannte Einstellungsstände

| Wert | Beschreibung im STE-Hilfetext |
|---|---|
| 0 | 3-Punkt-Mischer |
| 1 | 2-Punkt-Mischer |
| 2 | Pumpenkreis |
| 3 | Kein Heizkreis |
| 4 | Taktbetrieb, wenn WE abgeschaltet |

Die STE-Metadaten begrenzen den Bereich auf 0–3, obwohl der Hilfetext auch 4
nennt. Die Unterstützung von Wert 4 in der konkreten Firmware ist nicht belegt.
WE steht hier für Wärmeerzeuger.

| Herkunft | HK1 | HK2 | Einordnung |
|---|---:|---:|---|
| STE-Datei | 2 | 0 | Tatsächlicher Anlagenstand vor der Kühlnachrüstung, vom Betreiber bestätigt |
| Mitschnitt in `input/complete.log` | 0 | 3 | Vom Betreiber als problematische Versuchseinstellung eingeordnet |
| Aktuelle Betreiberangabe vom 25.09.2026 | 2 | 0 | Das unten beschriebene Warmwasserproblem tritt damit nicht auf |

Die HK-Kontextzuordnung in der Protokollauswertung bleibt abgeleitet. Die
Betreiberangabe ist die maßgebliche Information zum aktuellen Einstellungsstand;
der ältere Mitschnitt darf nicht als aktuelle Sollkonfiguration verwendet werden.

**Arbeitsinterpretation:** HK1 = 2 passt zum gemeinsamen Pumpenausgang 6.
HK2 = 0 passt zur Nutzung des Mischerausgangs für KT15/K3. Dass kein
Mischermotor vorhanden ist, begründet hier keine Umstellung auf Pumpenkreis
oder Deaktivierung. Eine vollständige Hersteller-Sollparametrierung liegt
noch nicht vor.

### Beobachtetes Warmwasserproblem mit 0/3

Der Betreiber berichtet: Bei 07-05 = 0/3 brach die Warmwassererwärmung bei etwa
49 °C ab. Die Ladepumpe lief weiter und kühlte den Speicher unnötig ab.
Mit 2/0 tritt dieses Problem nicht auf.

Das ist mit einer auseinanderlaufenden Freigabe von Wärmeerzeugung und
Speicherumwälzung vereinbar. **Nicht belegt** sind die konkrete Abschaltursache
bei 49 °C sowie die Frage, ob M5 wegen einer fortbestehenden Ladeanforderung
oder einer Nachlauffunktion weiterlief. Da sich beide Heizkreistypen
unterscheiden, kann die Ursache nicht allein HK2 zugeschrieben werden.

## Zusammenspiel mit der Warmwasserfunktion

Die Warmwasserfunktion hat einen eigenen Speicher-Sollwert und eine
Schaltdifferenz. Die Heizkreisfunktionen bilden ihren Bedarf anhand ihrer
Heizungs-Sollwerte. Vorrang und Wärmeerzeugerzuordnung verbinden die Funktionen.

Wenn Ausgang 11 während der Warmwasserbereitung aktiv wird, zieht K11 an.
Bei gleichzeitig aktivem Ausgang 6 wird dann M4.2 statt M4.1 versorgt.
Das ermöglicht den Heizungsweg unter Umgehung des für Warmwasser genutzten
Abluft-Wärmetauschers. Ob Ausgang 11 genau so von der Firmware gesetzt wird,
muss noch anhand eines synchronen Mitschnitts bestätigt werden.

Folgende Betriebszuordnung ist mit Betreiberbeschreibung und Schaltung vereinbar;
sie ist keine gemessene Wahrheitstabelle der Firmware:

| Bedarf | Vorgesehene Wärmeerzeugung | Plausibler Pumpenbetrieb während der Wärmezufuhr |
|---|---|---|
| Nur Warmwasser | Abluft-Wärmepumpe für Speicher | M5 |
| Raumheizung, Abluft reicht | Abluft-Wärmepumpe | M4.1 |
| Raumheizung, zusätzliche Leistung erforderlich | Abluft- und Erdwärmepumpe | M4.1 |
| Warmwasser und Raumheizung gleichzeitig | Abluft für Speicher, Erdwärme für Raumheizung | M5 und M4.2 |

Nachlauf, Sperren, Kühlbetrieb und Schutzfunktionen sind damit nicht beschrieben.

Relevante Parameter aus dem [STE-Katalog](ste-output/Parameter.md):

| TEM | Bedeutung und Beleggrenze |
|---|---|
| 05-00 | Schaltdifferenz: Speicherladung wird bei Unterschreitung des Sollwerts um diesen Betrag aktiviert |
| 05-02 | Warmwasservorrang: 0 = absoluter Vorrang; 0,1 = absoluter Parallelbetrieb; 0,2–20 h = lastabhängiger Parallelbetrieb |
| 05-03 | Nachlaufzeit der Speicherladepumpe |
| 05-05 | Trotz des Namens „Funktionsweise Ladepumpennachlauf“ nennt Wert 2 eine separate Warmwasser-Wärmepumpe; die Klemmennummer fehlt im Hilfetext |
| 05-07 | Stellglied: 0 = Ladepumpe; 1 = Umlenkventil; Übertragung auf diese Sonderbeschaltung nicht abschließend geklärt |

Vor der Kühlnachrüstung war 05-02 laut STE-Datei auf 0,1 eingestellt.
Nach der berichteten Wiederherstellung gilt dieser Wert auch aktuell;
eine unabhängige Rücklesung wurde hier noch nicht ausgewertet. „Parallel“ bei 05-02 meint Warmwasser gleichzeitig mit Raumheizung;
gleichzeitiger Betrieb beider Wärmeerzeuger für die Raumheizung ist ein anderer Fall.

## Kühlproblem und wiederhergestellte Konfiguration

**Betreiberbericht vom 26.09.2026:** Schon vor dem Konfigurationsverlust
funktionierte Kühlen bei gleichzeitiger Warmwasserbereitung. Ohne
Warmwasserbedarf floss das Kühlwasser dagegen durch beide Wärmepumpen;
nach etwa einer Minute wurde der Kühlbetrieb abgeschaltet. Unerwartete
Sensorwerte als Ursache sind eine Vermutung. Ob dabei der HWAL-Verdichter
lief oder nur dessen Wärmetauscher durchströmt wurde, ist noch offen.
Auch der konkrete Abschaltstatus bzw. Fehlercode fehlt. Seit der
Wiederherstellung wurde Kühlen laut ausdrücklicher Klarstellung des Betreibers
noch nicht getestet. Diese historischen Beobachtungen sind daher kein Befund
über das Kühlverhalten der aktuellen Konfiguration.

Die Wiederherstellung von `Parameter.md` mit alleiniger Änderung von 09-07
auf 6 ergibt nach Betreiberangabe folgende für Kühlen relevante Kombination:

| Parameter | Wiederhergestellter Stand | Vergleich mit Werkscheckliste |
|---|---|---|
| 09-07, Wärmepumpe | 6, ausdrücklich zusätzlich eingestellt | Wärmepumpe mit Kühlfunktion |
| 07-14, HK1/HK2 | 0/0 aus dem historischen Anlagenstand | Fußnote der Checkliste fordert für Mono heizen-kühlen beide Kreise auf 3 |
| 09-11, Wärmepumpe | 0 aus dem historischen Anlagenstand | Checkliste nennt für Mono heiz-kühl 6; genaue Bedeutung dieses Sonderwertes fehlt im STE-Hilfetext |

Diese Abweichungen sind Diagnosehinweise, keine bestätigte Sollkonfiguration
für die individuell beschaltete Anlage. Insbesondere beeinflusst eine Änderung
von 07-14 bei HK2 den für KT15 genutzten Mischerausgang. 09-07 allein beschreibt
den Wärmeerzeugertyp und belegt keine vollständige Kühlkonfiguration.

**Präzisierung der Pumpenauswahl:** Im bereitgestellten Steuerschaltplan ist
zusätzlich zum direkten Zweig zur K11-Spule ein Kontakt **K4, 21–24** zu
sehen. K4 ist laut Legende ein Hilfsrelais für Kühlbetrieb und wird im Plan
zusammen mit Y2 über TEM 9 angesteuert. Deshalb ist nicht belegt, dass K11
und damit die Auswahl M4.1/M4.2 ausschließlich dem Warmwasserstatus folgen
müssen. Der zusätzliche Kontakt kann einen weiteren Ansteuerweg bereitstellen;
seine Einspeisung, die Ausgangszustände im Kühlbetrieb und die tatsächliche
Verdrahtung nach der Nachrüstung sind noch abzugleichen. Die bisherige
Interpretation eines unvermeidlichen Wegs durch beide Wärmepumpen ohne
Warmwasserbedarf wäre zu weitgehend.

Ein abgeschalteter HWAL-Verdichter verändert für sich allein keinen
hydraulischen Leitungsweg. Ob sein Abschalten genügt, hängt unter anderem
davon ab, ob er während des fehlerhaften Kühlbetriebs tatsächlich Wärme
zuführt und was die Abschaltung auslöst. Das ist noch nicht nachgewiesen.

Die Untersuchung des Kühlbetriebs ist zurückgestellt: Der Betreiber möchte
zunächst die Heizlogik vollständig verstehen. Für einen späteren Vergleich
der beiden Kühlzustände wären Pumpenlauf M4.1/M4.2/M5,
HWAL-Verdichterbetrieb, K4-/K11-Zustand, HK2-Stellbefehl und KT15 sowie die
Temperaturen und der Status unmittelbar vor und bei der Abschaltung relevant.
Schutzgrenzen werden zur Diagnose nicht verändert.

## Beobachtung von 01-21 HK2

Der Betreiber meldete bei der aktuellen Einstellung 2/0: Seit Ende der
Warmwasserbereitung übernimmt die Abluft-Wärmepumpe die Raumheizung;
01-21 HK2 wechselte dabei von **0 % auf −100 %**.

| Wert | Bedeutung der Mischer-Stellgröße |
|---|---|
| +100 % | Auf-Befehl |
| 0 % | Kein Stellbefehl |
| −100 % | Zu-Befehl |

Es handelt sich um einen Stellbefehl, nicht um eine gemessene Ventilposition.
0 % bedeutet deshalb weder „Ventil geschlossen“ noch „Wärmeerzeuger aus“.

**Plausible Erklärung:** Mit der wieder verfügbaren Abluftwärme fordert HK2
eine Verringerung der zusätzlichen Wärmezufuhr. Das passt zur Verwendung des
Auf-Ausgangs für KT15/K3. −100 % schaltet jedoch nicht unmittelbar über den
unbeschalteten Ausgang 16 einen Verdichter aus. Bleiben weitere Auf-Impulse
aus, öffnet KT15 nach 1000 s ab dem letzten Wegfall des Y1-Signals, sofern
die Versorgung bestehen bleibt. Fällt die Versorgung vorher weg, öffnet es
bereits dann. Der zeitliche Zusammenhang
zwischen Auf-Befehl, Versorgung von KT15, dessen Kontakt und dem tatsächlichen
Verdichterlauf ist noch nicht aufgezeichnet.

## Bediengeräte FB1/FB2 und ihre Ausgangssymbole

Nach Betreiberangabe sind zwei Bediengeräte als FB1 und FB2 mit den
Slave-Adressen **0x90 und 0x91** angemeldet. Der Controller überträgt die
anzuzeigenden Daten per Broadcast oder direkter Nachricht.

| Anzeige laut Bedienungsanleitung des Betreibers | Bedeutungskandidat für diese Anlage |
|---|---|
| Mischventil Heizkreis auf | Wenn das Symbol Ausgang 15 abbildet: Ansteuerung von KT15, kein tatsächlicher Mischermotor |
| Mischventil Heizkreis zu | Anzeige auf FB2 synchron zu `OperatingStatus_1101.Mixer_Close` bestätigt; Zuordnung zum physischen Ausgang 16 weiterhin ungemessen |
| Umwälzpumpe Heizkreis oder Wärmepumpenkreis | Bei Abbildung von Ausgang 6 gemeinsame Heizungs-Pumpenfreigabe; M4.1/M4.2 erst durch K11 ausgewählt |
| Funktion Warmwasserbereitung | Warmwasserstatus; noch nicht geklärt, ob Anforderung, aktive Ladung oder konkreter Ausgang gemeldet wird |
| Wärmeerzeuger | Zugeordneter oder gemeinsamer Wärmeerzeugerstatus; genaue Zuordnung und Aussage über tatsächlichen Verdichterlauf offen |

Busadresse, Reglerfunktion, Ausgabesymbol und reales Bauteil sind unterschiedliche
Ebenen. Insbesondere gilt nicht automatisch „FB2-Pumpensymbol = M4.2“.
Ein gemeinsamer Warmwasserstatus könnte auf beiden FB erscheinen, ohne zwei
Warmwasserkreise zu bedeuten. Das ist noch keine beobachtete Zuordnung.

Die vorhandenen Statusdefinitionen in [broadcast.tsp](broadcast.tsp) und
[hautec.tsp](hautec.tsp) enthalten noch unbenannte Felder. Eine vollständige
Zuordnung der fünf Symbole zu Telegrammbits ist nicht belegt. Aus der
Symbolreihenfolge wird keine Bitnummer abgeleitet.

### Mitschnitt vom 26.09.2026: Symbol „Mischventil zu“ auf FB2

**Betreiberbeobachtung:** Das Symbol war spätestens seit 11:40 sichtbar und
verschwand um 11:42. Der Betreiber bestätigt, dass beide Angaben die Uhrzeit
außerhalb der Bedieneinheit bzw. die Log-Zeit meinen.

Quelle: [`ebusd.log`](../ebusd.log), 11:31:00.563–11:44:40.569. Die Datei
enthält 699 vollständige Telegramme mit gültiger Master-CRC: 174 Broadcasts,
370 quittierte Master-Master-Telegramme und 155 Master-Slave-Transaktionen
mit gültiger Antwort-CRC und Quittierungen. Drei zusätzliche Zeilen enthalten
nur das einzelne Byte `20` (Zeilen 171, 373 und 476); sie wurden nicht als
Telegramme interpretiert.

Die im Broadcast `07 00` übertragene Reglerzeit liegt etwa zwei Minuten hinter
der Log-Zeit: Um 11:42:06.138 wird beispielsweise 11:40:03 übertragen.
Für den folgenden Abgleich wird ausschließlich die bestätigte Log-Zeit verwendet.

**Ergebnis der ersten Mitschnittauswertung, vor der späteren Bestätigung:**
In `10 FE 10 0A`, Nutzdatenkennung
`11 01`, wechselt Bit 6 des ersten Statusbytes. Das ist das fünfte Nutzdatenbyte
(Index 4, einschließlich der Kennung `11 01`) und entspricht
dem damaligen Feld `Broadcast.Status1a.Flag6`, inzwischen
`Broadcast.OperatingStatus_1101.Mixer_Close` in `broadcast.tsp`.

| Log-Zeit | Zeile | Erstes Statusbyte | Flag6 |
|---|---:|---|---:|
| 11:31:40.423 | 36 | `80` | 0 |
| 11:33:00.533 | 104 | `C0` | 1 |
| 11:34:20.550 | 170 | `80` | 0 |
| 11:35:40.426 | 238 | `80` | 0 |
| 11:37:00.428 | 306 | `80` | 0 |
| 11:38:20.538 | 372 | `80` | 0 |
| 11:39:40.555 | 440 | `C0` | 1 |
| 11:41:00.431 | 513 | `80` | 0 |
| 11:42:20.573 | 583 | `80` | 0 |
| 11:43:40.449 | 650 | `80` | 0 |

Die beiden relevanten Telegramme einschließlich CRC lauten:

```text
11:39:40.555  10 fe 10 0a 0c  11 01 dc 00 c0 07 06 00 00 00 74 00  b4
11:41:00.431  10 fe 10 0a 0c  11 01 dc 00 80 07 06 00 00 00 74 00  38
```

Der Statusblock kommt etwa alle 80 Sekunden. Zwischen diesen beiden
Nutzdatenfolgen ändert sich ausschließlich die Maske `0x40`. Der gesetzte
Wert um 11:39:40 passt zeitlich zum sichtbaren Symbol um 11:40; der bereits
um 11:41:00 gelöschte Wert passt jedoch nicht unmittelbar zum berichteten
Verschwinden um 11:42. Diese erste Beobachtung ließ die Zuordnung zunächst
offen. Die unten dokumentierte spätere synchrone Beobachtung bestätigt das
Anzeigebit; die frühere Zeitabweichung belegt keine Anzeigeverzögerung.
Die 80 Sekunden sind das Abtastintervall dieses Blocks im Mitschnitt, keine
nachgewiesene Dauer eines Stellbefehls. Die Zuordnung des gesamten Blocks zu
HK2 und seiner übrigen Felder folgt daraus nicht.

Weitere Befunde über den gesamten Mitschnitt:

- Beide `05 03`-Rückmeldungen behalten Statusnummer `00`, Statusbits `48`
  (`flame=1`, `uwp=1` nach aktuellem Modell) und Stellgrad `64` = 100 %.
  Nur das Kesseltemperaturbyte wechselt um 11:37 von `59` auf `5A`
  (44,5 auf 45,0 °C nach aktueller Dekodierung).
- In `05 01` bleiben die Anforderungen an `03` bei 100 % und an `13` bei
  0 %, beide mit Status `EE`. Die Zusatzbytes bleiben ebenfalls konstant.
  Das Verschwinden des Symbols fällt somit mit keinem beobachteten Wechsel
  dieser Wärmeerzeuger-Statusbits oder Stellgrade zusammen.
- Die direkten Statusantworten von `91` auf `00 04` und `00 05` sowie die
  Änderungsabfragen `D0 15` liefern keinen passenden Wechsel.
- Im Broadcast `08 01` bleibt das Statusbyte bei `08`. Bei `08 02` wechselt
  das letzte, bisher nicht modellierte Byte mehrfach zwischen `00`, `90`,
  `3F` und `27`; daraus ergibt sich keine eindeutige Symbolzuordnung.

### Nachbeobachtung: Anzeigebit bestätigt, wiederkehrende Zu-Impulse

Der Betreiber hat anschließend das synchrone Erscheinen der Anzeige
„Mischventil Heizkreis zu“ auf FB2 mit `Flag6` bestätigt. Das Feld heißt nun
`Broadcast.OperatingStatus_1101.Mixer_Close` (`BI6`, unveränderte Bitposition).
Damit ist die Zuordnung **Bit → Anzeige** durch Betriebsbeobachtung bestätigt;
eine Messung des physischen Ausgangs 16 oder eine Ventilpositionsmeldung ist
damit nicht verbunden.

Der zusätzlich berichtete Ablauf lautet:

| Beobachteter Abschnitt | Verhalten von Bit und Anzeige |
|---|---|
| Anfangs beobachteter Betriebsmodus, nicht näher bestimmt | Ungefähr alle 6,5 Minuten für etwa 1 Minute aktiv |
| Erdwärmepumpe wird eingeschaltet | Wiederkehrende Folge setzt aus |
| Danach Raumheizung nur durch Abluft-Wärmepumpe | Bit/Anzeige bleiben aus |
| Anschließend Warmwasserbereitung aktiviert | Wiederkehrende Folge setzt wieder ein |

Diese Angaben stammen aus der weiteren Betreiberbeobachtung, nicht aus einer
zusätzlichen Auswertung von `ebusd.log`. Die erste Phase wird nicht rückwirkend
als nachgewiesene Warmwasserphase bezeichnet. Im älteren Mitschnitt liegen die
beiden gesetzten Stichproben um 11:33:00.533 und 11:39:40.555 rund 6 Minuten
40 Sekunden auseinander; das ist mit der ungefähren Periodenangabe vereinbar.
Die Einschaltdauer von etwa einer Minute lässt sich bei 80 Sekunden
Abtastintervall aus diesem Mitschnitt allein nicht bestätigen.

**Arbeitsinterpretation:** Das Muster passt zu einem betriebszustandsabhängig
wiederholten Zu-Befehl der Mischerfunktion. Denkbar ist ein wiederholtes
Anfahren bzw. Halten der logischen Zu-Endlage; der konkrete Firmwarezweck
und ein dafür verantwortlicher Zeitparameter sind nicht belegt. Die
Wiederaufnahme bei Warmwasserbeginn deutet auf eine Kopplung an die
Warmwasser-/Heizungsumschaltung hin, belegt aber weder eine allgemeine
Warmwasservorrangsperre noch eine direkte Erdwärmepumpen-Abschaltung.

Das Bit ist insbesondere kein allgemeines Gegenstück zu „Erdwärmepumpe ein“:
Es bleibt auch in der anschließenden Phase mit alleiniger Abluftheizung aus.
`Mixer_Close=0` bedeutet zunächst nur, dass dieses Zu-Symbol nicht aktiv ist;
ein Auf-Befehl oder eine Wärmeanforderung folgt daraus nicht.

Nach dokumentierter Verdrahtung ist Ausgang 16 unbeschaltet; KT15 wird über
den Auf-Ausgang 15 und die Versorgung an 26 beeinflusst. Selbst wenn das
Anzeigebit Ausgang 16 abbildet, würden die Zu-Impulse KT15 daher nicht direkt
ansteuern oder dessen Ausschaltverzögerung neu starten. Dafür sind die
Auf-Impulse und der Versorgungszustand maßgeblich, deren zeitlicher Verlauf
noch nicht aufgezeichnet ist.

**Weiter offen:** Der synchrone Zusammenhang mit `01-21 HK2`, dem Auf-Symbol,
KT15/K3 und dem tatsächlichen Verdichterlauf. Die frühere Einzelbeobachtung
von `01-21 HK2 = −100 %` wird nicht nachträglich mit diesen neuen Symbolfolgen
gleichgesetzt. Auch die Zuordnung von `03`/`13` zu realen Wärmeerzeugern oder
HK1/HK2 bleibt offen.

## Nächste belegbare Abgleiche

**Aktueller Untersuchungsfokus:** Heizlogik einschließlich paralleler
Warmwasserbereitung. Zu klären ist die Kette von HK1-/HK2-Sollwerten über
Anlagensollwert und Wärmeerzeugeranforderung bis zu den Ausgängen 15/26,
KT15 und K3 sowie die Änderung dieser Kette bei Beginn und Ende der
Warmwasserbereitung. Die Maximalwertbildung des verwandten Reglers bleibt
bis zum Abgleich ein Vergleichsmodell. Kühlversuche und Änderungen der
Kühlparameter sind derzeit nicht Gegenstand der Untersuchung.

1. Bei einem normalen Warmwasser-/Heizungswechsel zeitgleich 01-21 HK2,
   die Pumpenbefehle, die Symbole beider FB und den tatsächlichen Betrieb der
   Pumpen und Wärmeerzeuger protokollieren.
2. Prüfen, ob +100 % bei 01-21 HK2 dem Zuschalten der Erdwärmepumpe vorausgeht.
   Dazu Vorlauf-Soll/Ist und Wärmeerzeugerstatus erfassen.
3. Aktuelle Werte von 05-02, 05-03, 05-05 und 05-07 zusammen mit 07-05 sichern;
   historische STE-/Mitschnittwerte nicht als aktuelle Werte behandeln.
4. Die tatsächliche Verdrahtung von KT15 mit dem Plan abgleichen und den
   Ablauf von Y1, Versorgung und Relaiskontakt zeitlich erfassen; Modell und
   eingestellte Zeitfunktion sind identifiziert. Arbeiten an Netzspannungsklemmen sind
   davon getrennte Facharbeiten; zur Protokollbeobachtung sind keine Eingriffe nötig.

Ein erneuter Versuch mit der problematischen Einstellung 0/3 ist für diese
Abgleiche nicht erforderlich.

## Ergänzende Recherchequellen

- [Hautec HSC 6001 WPC, Anleitung von 2008](https://www.manualslib.de/manual/804180/Hautec-Hsc-6001-Wpc.html):
  getrennte Funktionen für Heizkreise, Warmwasser und Wärmeerzeuger; vergleichbare
  Reglergeneration, kein Beweis für jede Besonderheit des SE 6000 WPC.
- [Hautec SE 6024 WPC, Anleitung von 2015](https://www.manualslib.de/manual/111332/Hautec-Se-6024-Wpc.html), S. 57:
  Ausgangsanzeige Mischer mit 0 % = kein Befehl, +100 % = Auf, −100 % = Zu.
- [Walter Meier 61X2 / SE 6024 WPC](https://www.manualslib.de/manual/118188/Walter-Meier-61X2.html),
  S. 26–27: 07-005 mit Werten 0–3 sowie Pumpentaktbetrieb über 07-060/07-061.
  Dies belegt nicht die Unterstützung von 07-05 = 4 bei dieser Anlage.
- [IT 5711 Fachmannanleitung](https://www.scheer-heizsysteme.de/media/produkt_pdf/Anleitungen/IT_5711_Regler_Fachmannanleitung.pdf),
  S. 39: Erklärung von 3-Punkt-Antrieb, 2-Punkt-Antrieb mit Rückstellung und
  direktem Pumpenkreis. Die Parameternummerierung unterscheidet sich.
