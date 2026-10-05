# Parameter-Vergleichsversuche nach cool8

Stand: 02.10.2026. Vorschlag zur Diagnose, keine ausgeführten Anlagenänderungen
und keine festgelegte Daueroptimierung. Grundlage sind die lokalen
Parameterbeschreibungen und die [cool8-Auswertung](Cooling-Test-2026-10-02-cool8.md).

## Bestätigte Ausgangswerte

Die am 02.10.2026 vom Betreiber neu gespeicherten
[aktuellen Einstellungen](../aktuelle_einstellungen.txt) enthalten:

| Parameter | Kontext | Ausgangswert |
| --- | --- | --- |
| 09-35 Schaltdifferenz 2. Stufe | WP | −3 K |
| 06-10 Xp WEZ Manager | Global | 3 K |
| 06-11 Tn WEZ Manager | Global | 20 min |
| 07-14 Heizkreisfunktion im Kühlbetrieb | HK1 / HK2 | 2 / 2 |
| 03-43 Kühltemperatur | HK1 / HK2 | 21 / 21 °C |
| 03-35 Kühlgrenzenabstand | HK1 / HK2 | 2 / 2 K |
| 11-03 minimale WE-Leistung | WE1 | 70 % |

Der Betreiber hatte 07-14 bereits vor einer Weile versuchsweise von 3 auf 2
geändert und keinen Unterschied beobachtet. **07-14 bleibt für alle folgenden
Vergleiche in beiden Heizkreisen auf 2.** Eine Rückstellung nach einem Versuch
betrifft nur den jeweils untersuchten Parameter, nicht 07-14.
Der genaue frühere Änderungszeitpunkt ist nicht dokumentiert; die neue Datei
belegt daher nicht rückwirkend die Einstellung während jedes alten Mitschnitts.

Laut Parameterbeschreibung bedeutet 2 „Mischer auf“, 3 „geregelt“.
Ein dauerhaftes 01-21 HK2 = +100 ist mit Stellung 2 vereinbar und dann kein
eigenständiger Nachweis einer temperaturabhängig berechneten HK2-Kühlanforderung.
Die Beobachtung ohne erkennbare Veränderung beweist nicht, dass 07-14 wirkungslos
ist. Sie spricht aber dafür, die nächste Untersuchung bei unveränderter
HK2-Funktion auf WE1-Anforderung und Stufenfreigabe zu konzentrieren.

Vor dem jeweiligen Versuch Ausgangswerte nochmals lesen und zusammen mit dem
Änderungszeitpunkt dokumentieren, damit spätere Bedienungen erkennbar bleiben.

Die Wertebereiche unten stammen aus dem STE-Export und den lokalen Definitionen,
nicht aus einer neuen Abfrage der gerade geladenen Firmware. Änderungen nur
über den bekannten angebotenen Einsteller vornehmen und zurücklesen.

## Versuch A: Schaltdifferenz der zweiten Stufe

**09-35 im WP-Kontext: −3 K → −2 K**, anschließend zurück auf den vorher
bestätigten Ausgangswert. EH-Kontext unverändert lassen. Der lokale Hilfetext
nennt für zweistufigen Betrieb negative Werte; hier weder 0 noch einen positiven
Wert als Vergleich verwenden. Der frühere positive Wert verhinderte die Kühlung.

Ziel ist die Unterscheidung der ersten Abschaltung nahe 17,5–17,6 °C von den
späteren Rücknahmen bei WE1 = 73–76 %. Besonders interessant ist eine erste
längere Phase mit noch hoher WE1-Anforderung, wie in cool8.

- Verschiebt sich die temperaturabhängige Schaltregion bei ähnlicher hoher
  WE1-Anforderung reproduzierbar, spricht das für einen Einfluss von 09-35.
- Bleibt die WE1-Kurve ähnlich, während sich nur Stufenwechsel verändern,
  liegt der Einfluss eher hinter der gemeinsamen Anforderungsbildung.
- Bleibt der Effekt aus oder startet die zusätzliche Stufe nicht mehr, ist
  das ebenfalls festzuhalten. Es beweist weder einen bestimmten Fühlerbezug
  noch automatisch eine Begrenzung durch 09-32.

Die genaue Kühlgleichung und ihre Wirkrichtung sind nicht dokumentiert.
Insbesondere wird keine Abschaltverschiebung um exakt +1 K vorausgesagt.
Die Änderung −3 → −2 ist ein begrenzter Vergleich im bekannten negativen
Bereich, kein Versuch, eine untere Schutzgrenze abzusenken.

Quelle: [09-35, Beschreibung](../ste-output/Parameter.md#datensatz-129).

## Versuch B: Empfindlichkeit des gemeinsamen Leistungsreglers

Zunächst 09-35 wieder auf den bestätigten Ausgangswert zurückstellen.
Dann **06-10 „Xp WEZ Manager“: 3 K → 6 K**; 06-11 unverändert lassen.
Nach dem Vergleich 06-10 wieder auf den Ausgangswert zurückstellen.

Der Hilfetext beschreibt Xp als die Soll-Ist-Abweichung, bei der der Stellbefehl
100 % beträgt. Ein größerer Proportionalbereich bedeutet nach der üblichen
PI-Interpretation eine geringere proportionale Reaktion auf dieselbe
Temperaturänderung. Das ist eine aus der Beschreibung abgeleitete Erwartung;
die vollständige TEM-Reglergleichung und ihr Kühlbetrieb sind nicht bekannt.
Die Gesamtanforderung halbiert sich nicht zwangsläufig, da Reglerzustand,
Integralanteil, Begrenzungen und Stufenlogik mitwirken.

Zu vergleichen sind vor allem **01-09 WE1 relativ zur Änderung von 00-08**
und danach die Schaltphasen, nicht allein die Anzahl der Verdichterstarts.
Werden die schnellen Anforderungsänderungen bei ähnlichen Temperaturverläufen
kleiner, stützt das die Beteiligung des gemeinsamen Reglers. Bleiben die
Rückschaltungen dagegen an einer Temperaturregion trotz hoher Anforderung,
ist eine zusätzliche Begrenzung weiter plausibel.

Längere Laufzeiten oder Stabilität sind nicht garantiert; auch längere
Startverzögerungen bzw. geringere Kühlanforderung sind mögliche Ergebnisse.
06-10 ist ein globaler Managerparameter und kann auch Heizen und Warmwasser
beeinflussen, daher als begrenzten Diagnoseversuch behandeln.

Quelle: [06-10, Beschreibung](../ste-output/Parameter.md#datensatz-89).

## Versuch C: Nachstellzeit, optional nach A und B

Bei wiederhergestelltem Ausgangswert von 06-10 und 09-35:
**06-11 „Tn WEZ Manager“: 20 min → 40 min**.

Der Hilfetext beschreibt die zeitliche Verstärkung bei konstanter
Regelabweichung. Eine größere Nachstellzeit lässt einen Integralanteil
langsamer auf- und abbauen. Die Rücknahme einer zuvor hohen Anforderung kann
also ebenfalls langsamer werden; die Änderung garantiert keine Verbesserung.

Interessant sind die Erholung der WE1-Anforderung zwischen den Läufen und
das längerfristige Wandern der Schaltpunkte. Ein einzelner 40-Sekunden-Lauf
reicht nicht, um eine 20-/40-Minuten-Nachstellzeit zu bewerten. Diesen Versuch
erst dann ergänzen, wenn die ersten beiden Vergleiche noch eine offene Frage
zum Reglerzustand lassen. Auch dieser Parameter gilt global. Nicht auf 0
setzen, solange die Bedeutung dieses Sonderwerts in der Firmware ungeklärt ist.

Quelle: [06-11, Beschreibung](../ste-output/Parameter.md#datensatz-90).

## Einheitlicher Ablauf und Messraster

1. Ausgangseinstellungen lesen und Rohlog vor der Änderung beginnen.
2. Pro Vergleich ausschließlich den genannten Parameter ändern, zurücklesen
   und Zeitpunkt notieren. Für den nächsten Versuch vorher den Ausgangswert
   wiederherstellen; Werte nicht aufeinander stapeln.
3. Kühltemperaturen, Kühlgrenzenabstände, Pumpen-/Heizkreisfunktionen und
   hydraulische Bedingungen möglichst gleich halten. Warmwasserwechsel oder
   weitere Bedienungen im Versuch ausdrücklich markieren.
4. Wie in cool8 ungefähr alle fünf Sekunden 00-07 WP, 00-08, 00-02 HK2,
   01-09 WE1, 01-21 HK2 sowie 01-96 und 01-07 aufzeichnen. Passive Telegramme
   und nach Möglichkeit elektrische Leistung weiter erfassen. Gleiche
   Messwerte müssen nicht in beiden Kontexten doppelt abgefragt werden.
5. Für A/B den Anlauf und möglichst zwei bis drei vergleichbare folgende
   Schaltphasen erfassen. Bei ausbleibendem Start dieses Ergebnis dokumentieren,
   statt durch weitere gleichzeitige Änderungen eine Reaktion zu erzwingen.
   Nicht dauerhaft im Kurzzyklus laufen lassen, nur um mehr Wiederholungen
   zu sammeln.
6. Nach Rückstellung bei ähnlichen Temperaturen prüfen, ob das ursprüngliche
   Verhalten wiederkehrt. Wärmerer Startzustand und gespeicherter Reglerzustand
   können den ersten Lauf erheblich verändern. Keine zusätzliche Netzunterbrechung
   als vermeintlichen Regler-Reset in den Vergleich einführen.

Ein einziger Vorher/Nachher-Vergleich beweist keine interne Gleichung.
Die aufgezeichneten Sollwerte und die Kurve von 01-09 sind wichtiger als eine
bloße Aussage „läuft länger“.

## Für diese erste Versuchsfolge unverändert lassen

- **11-03 minimale WE-Leistung:** Der bekannte Wert 70 % passt zur beobachteten
  Normierung. Eine Änderung würde zugleich die Zuordnung zwischen direkter
  und normierter Anforderung verändern und den Vergleich erschweren. Sie ist
  nicht als einfache Verdichter-Leistungsreduzierung nachgewiesen.
- **07-14 Heizkreisfunktion: HK1 = 2, HK2 = 2 beibehalten.** Der HK2-Ausgang
  wirkt laut Plan auf KT15/K3; der Einsteller ist hier kein nachgewiesener
  mechanischer Mischer-Test. Der frühere Vergleich 3 → 2 brachte laut Betreiber
  keine erkennbare Änderung.
- **09-23 / 09-31 Mindeststillstands-/Mindestlaufzeit:** Die bisher beobachteten
  kurzen Phasen sind ohnehin kürzer als die zuletzt gelesenen Werte. Ihre
  tatsächliche Zuordnung zur Soleverdichter-Freigabekette ist offen; Verstellen
  würde diese Frage nicht gezielt klären. Zeiten nicht verkürzen.
- **09-21 Abschaltdifferenz:** Der verfügbare Text beschreibt das Überschreiten
  von TWV-Soll plus Differenz, also keine bestätigte Kühlgleichung.
- **09-32:** Kein bestätigter Einsteller/Anfrageselektor am vorliegenden Regler.
  Nicht über eine aus der STE-Datei erratene Adresse verändern.

Vorläufige Reihenfolge: **09-35 WP allein**, danach **06-10 allein**;
06-11 nur bei verbleibendem Bedarf. Diese Auswahl soll Regelpfade unterscheiden,
nicht eine Fühlerverlegung oder eine endgültige Anlagenkonfiguration vorwegnehmen.

## Ergebnis von Versuch A: cool9, −2 K

Die [cool9-Auswertung](Cooling-Test-2026-10-02-cool9.md) zeigt sechs
100-%-Busphasen von jeweils etwa 40 s, Zuschaltung bei WE1 = 93 % und
Rücknahme bei WE1 = 73 %. Der Vorlauf liegt bei den Rücknahmen noch bei
21,8–22,9 °C. −2 K beseitigt das Takten somit nicht.

Die Ausgangstemperaturen und die anfängliche WE1-Anforderung unterscheiden
sich von cool8; eine kausale Verschlechterung durch 09-35 ist daraus nicht
bewiesen. Zunächst den Rückvergleich bei −3 K und ähnlichen Bedingungen
abschließen. Danach bleibt 06-10 = 3 → 6 K der nächste einzelne Vergleich.
07-14 bleibt für beide Heizkreise auf 2.

## Ergänzender Vergleich: cool10, −4 K

Auch [cool10 mit −4 K](Cooling-Test-2026-10-02-cool10.md) zeigt acht kurze
100-%-Busphasen von etwa 40–64 s. Sechs liegen vor dem Beginn der zusätzlichen
Abfragen, zwei danach. In den beiden direkt erfassten Phasen erfolgt die
Rücknahme bei WE1 = 73 bzw. 70 % und Vorlauf 21,8 bzw. 21,6 °C.

Eine erkennbare Beruhigung gegenüber −2 K ist nicht zu sehen. Eine Wirkung
von 09-35 auf die frühere lange Phase nahe 17,5 °C kann damit nicht beurteilt
werden, weil diese Betriebsbedingung nicht wieder erreicht wird. Die nächsten
Schritte bleiben Rückstellung auf −3 K und anschließend der einzelne Vergleich
06-10 = 3 → 6 K. 07-14 bleibt in beiden Heizkreisen auf 2.
