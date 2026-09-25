# Heizkreise, Warmwasser und Pumpensteuerung der Hautec-HWM-Anlage

Stand: 25.09.2026. Auswertung der bereitgestellten Anlagenpläne, der
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
- **Offen:** Die genaue Firmware-Zuordnung aller HK-/FB-Statusfelder zu den
  Ausgängen und die Ursache des früheren Warmwasserabbruchs.

„Aus dem Schaltplan abgelesen“ bezeichnet die dokumentierte Verdrahtung, nicht
eine durch Messung bestätigte Übereinstimmung mit der heute eingebauten Anlage.

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
| [STE-Parameterkatalog](ste-output/Parameter.md) | Parametertexte und gespeicherte Dateifelder |
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
| 7 | Kondensatorpumpe | Im gezeigten Plan nicht angeschlossen |
| 8 | Heizkreispumpe 2 / Mischer | Im gezeigten Plan nicht angeschlossen |
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
| STE-Datei | 2 | 0 | Gespeicherte Dateifelder; für sich allein kein aktueller Anlagenzustand |
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

Die STE-Datei enthält für 05-02 den Wert 0,1. Das ist kein bestätigter aktueller
Anlagenwert. „Parallel“ bei 05-02 meint Warmwasser gleichzeitig mit Raumheizung;
gleichzeitiger Betrieb beider Wärmeerzeuger für die Raumheizung ist ein anderer Fall.

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
| Mischventil Heizkreis zu | Wenn Ausgang 16 gemeint ist: logischer Schließbefehl ohne angeschlossenen Aktor |
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

## Nächste belegbare Abgleiche

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
