# Prüfung der Hypothese: 09-32 und eine feste 18-°C-Kühlgrenze

Stand: 01.10.2026. Quellen: Betreiberbeobachtungen, STE-Parameterbeschreibung,
Reglerverzeichnis und die bisherigen Kühlmitschnitte. Keine Anlagenänderungen.

**Nachtrag cool6:** Die [neue Messung](Cooling-Test-2026-10-01-cool6.md)
liefert direkte Rücklauf- und WE1-Werte etwa alle fünf Sekunden. Die fünf
vollständigen Rückschaltungen erfolgen bei gemeldetem Vorlauf 22 / 21,5 /
20,5 / 20 / 18,5 °C und direkter WE1-Anforderung von 73–76 %. Beim letzten
dieser Zyklen werden Werte unter 18 °C erst nach der Rückschaltung übertragen.
Eine zusätzliche Sollwertabsenkung um 19:54 wurde vom Betreiber bestätigt.
00-07 wurde weiterhin nicht direkt abgefragt; vorhanden ist 01-07 (Soll).

**Nachtrag cool8 vom 02.10.2026:** [00-07 ist nun direkt aufgezeichnet](Cooling-Test-2026-10-02-cool8.md),
386 gültige Messungen ungefähr alle fünf Sekunden. Der erste lange Lauf bleibt
noch 6 min 52,6 s nach der ersten Unterschreitung von 18 °C auf 100 %; 83
Messungen liegen in dieser Laufphase darunter. Drei spätere Rückschaltungen
erfolgen bei 19,6 / 19,2 / 20,8 °C ohne vorherige Messung unter 18 °C in der
jeweiligen Laufphase. Die erste Abschaltung nahe 17,5–17,6 °C erfolgt dagegen
bei noch 90 % direkter WE1-Anforderung und wird getrennt von den späteren
73–76-%-Rückschaltungen betrachtet. Eine zusätzliche Temperaturbegrenzung
bleibt möglich, eine einheitliche feste 18-°C-Abschaltung auf TWV wird nicht gestützt.

## Bewertung

**Eine untere Vorlaufbegrenzung ist ein plausibler zusätzlicher Einfluss.
Eine im vorhandenen Regler fest hinterlegte Grenze von 18 °C ist nicht
nachgewiesen und erklärt die bisherigen Kurzzyklen nicht allein.**

Der Betreiber hat inzwischen geprüft: Eingang 47 misst den WP-Vorlauf,
48 den WP-Rücklauf innerhalb des Geräts. Die entscheidende räumliche
Präzisierung ist, ob damit die HWAL oder die Solewärmepumpe gemeint ist.
Die Zuordnung von 47 zur handschriftlichen Markierung R3 und die Lage
relativ zum M4.2-Weg müssen damit zusammengeführt werden; allein aus den
Bezeichnungen Vorlauf/Rücklauf folgt keine bestimmte Lage im Hydraulikplan.

Falls 47/R3 tatsächlich im HWAL-Zweig sitzt, der bei M4.2 vom Kühlwasser
umgangen wird, ist folgende Erklärung schlüssig:

- Bei M4.1 erreicht das Kühlwasser den Fühler und eine dort überwachte
  Vorlauf-Untergrenze könnte eine Freigabe zurücknehmen.
- Bei M4.2 mit Warmwasserbereitung misst derselbe Fühler einen warmen
  Anlagenteil. Die gleiche Grenze würde dann nicht erreicht, obwohl
  andernorts gekühlt wird.

Die unterschiedlichen Temperaturverläufe während Warmwasser passen dazu.
Die Beobachtung beweist jedoch weder, dass gerade 09-32 die wirksame Grenze
ist, noch ihren Wert. Gleichzeitig ändert Warmwasser die gemeinsame
Leistungsanforderung; der Vergleich variiert also mehr als nur den Pumpenweg.
Längerer Lauf über M4.2 allein bestätigt deshalb nicht die korrekte
Fühlerverwendung für sämtliche Kühlbegrenzungen.

## Was die Parameterbeschreibung belegt

[09-32 im STE-Export](../ste-output/Parameter.md#datensatz-127) beschreibt
eine Abschaltung bei Unterschreiten einer minimalen WP-Vorlauftemperatur.
Der gespeicherte Wert beträgt 14 °C. Auch die lokale Programmiercheckliste
führt 14 °C auf. Das sind **keine aktuellen Rücklesungen dieses Reglers**.
Der STE-Export kennzeichnet gespeicherte Werte ausdrücklich entsprechend.

09-32 fehlt in der Liste beobachteter Parameterantworten und hat keinen
bestätigten Anfrageselektor in `controller.tsp`.
[Verzeichnisbefund](../master-output/Parameter.md#ste-kennungen-ohne-beobachtete-antwort)
Der Betreiber findet den Einsteller ebenfalls nicht am Gerät.

Daraus lässt sich der Wert 18 °C nicht herleiten. Eine andere Firmwarevariante,
konfigurationsabhängige Sichtbarkeit, eine nicht verstellbare Grenze oder
eine abweichende bzw. fehlende Funktion bleiben Möglichkeiten. Keine dieser
Möglichkeiten ist allein durch den fehlenden Menüeintrag bewiesen.
Die im STE-Export genannte Adresse `0xF26C` ist insbesondere kein bestätigter
eBUS-Anfrageselektor.

## Messbefunde gegen eine einfache feste 18-°C-Erklärung

1. Im Versuch vom 29.09. liefert der feinere TWV-Broadcast von
   **22:30:41.677 bis 22:34:41.696 wiederholt 17,9 °C**, während FA1
   durchgehend 100 % meldet. Die Rückschaltung folgt erst um 22:38:33.202.
   Das spricht gegen eine unmittelbar wirksame 18-°C-Grenze auf genau
   diesem Messwert. Eine andere Filterung oder Freigabebedingung ist damit
   nicht vollständig ausgeschlossen.
2. In `cool4` erfolgen die fünf Rückschaltungen bei grob übertragenen
   Vorlaufwerten **20 / 21 / 20,5 / 20,5 / 21 °C**.
3. In `cool5` werden bei allen fünf Rückschaltungen **21,5 °C** übertragen.
   Die gemeinsame WE1-Anforderung fällt jeweils schon davor deutlich ab.
4. In den frühen Versuchen lag die Rückschaltregion eher bei 17,5 °C.
   Dazu passt numerisch auch 20,5 °C minus 3 K; ein Bezug zu 09-35 bleibt
   eine alternative Hypothese, keine bestätigte Firmwaregleichung.

Das grobe FA1-Temperaturfeld hat 0,5-°C-Auflösung, der feinere Broadcast
kommt nur etwa alle 80 s. Einzelne kurzzeitige Minima könnten fehlen.
Die gemessenen Temperaturwerte an Bus-Rückschaltungen sind außerdem keine
synchronen Strom- oder Schützmessungen. Trotzdem stützt die Gesamtheit
keine einheitliche Erklärung aller Versuche durch Unterschreiten von 18 °C.

Belege: [29.09.](Cooling-Test-2026-09-29.md),
[cool4](Cooling-Test-2026-09-30-cool4.md),
[cool5](Cooling-Test-2026-10-01-cool5.md).

## Einordnung der vorhandenen Sensorbewertung

Die Datei [Bewertung der Sensor-Positionen.md](Bewertung%20der%20Sensor-Positionen.md)
enthält weitergehende Aussagen, die durch die bisherigen Unterlagen nicht
belegt sind:

- Ein automatischer Wechsel auf exakt 18 °C wegen eines fehlenden
  Raumfeuchtefühlers ist weder im zitierten 09-32-Hilfetext beschrieben noch
  durch die Logs nachgewiesen. Der Hilfetext allein belegt auch keine
  Taupunktberechnung oder eine spezielle Frostschutzfunktion.
- Ein träger mechanischer Heizkreismischer ist nicht nachgewiesen. Nach dem
  dokumentierten Schaltplan wirkt der HK2-Auf-Ausgang auf KT15/K3.
- Ein blockiertes Ventil, fehlender Durchfluss und eine exakt zweiminütige
  Schutzabschaltung sind keine festgestellten Ursachen. Die beobachteten
  Phasen unterscheiden sich deutlich in ihrer Länge.

Die dort vorgeschlagene Änderung von 07-14 auf 2 ist daher kein belastbar
begründeter Mischer-Test. Die über das Zeitrelais geführte Verdichteransteuerung
muss bei der Interpretation dieser Funktion berücksichtigt werden.

## Gezielt prüfbare nächste Beobachtung

Eine zeitlich dichtere Aufzeichnung von **00-07 (TWV/47), 00-08 (TWR/48)
und 01-09 WE1**, beispielsweise alle 2–5 s während mehrerer Schaltphasen,
würde die bisherigen 80-s-Temperaturstichproben wesentlich ergänzen.
Passive FA1-Rückmeldungen und möglichst reale Verdichterleistung mitführen.
Eine Abfrage garantiert dabei keine ebenso schnelle interne Aktualisierung.

Zu prüfen ist die Reihenfolge: wiederholtes Erreichen einer bestimmten
TWV-Untergrenze vor der Abschaltung oder Rücknahme der WE1-Anforderung bei
noch deutlich wärmerem TWV. Beides kann als getrennte Begrenzung existieren.
Für die konkrete Behauptung „09-32 ist intern fest 18 °C“ wäre zusätzlich
eine gerätespezifische Firmware-/Herstellerauskunft oder ein bestätigter
Lesezugriff erforderlich. Ein geratener Schreibzugriff ist kein Nachweis.
