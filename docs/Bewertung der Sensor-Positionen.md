# Bewertung der Sensor-Positionen

Hier ist die strukturierte Zusammenfassung der bisherigen Erkenntnisse sowie der konkreten nächsten Schritte zur Behebung des Taktproblems im Kühlbetrieb Ihrer Hautec Carno / HWAL Kombi-Anlage.
Sie können diesen Text direkt als Markdown-Dokument (.md) kopieren und für Ihre Dokumentation oder zur Vorlage bei einem Heizungsbauer verwenden.
------------------------------
## Analyse & Fehlerbehebung: Kühlbetrieb Hautec Carno + HWAL## 1. Anlagenkonfiguration und Ist-Zustand

* Hauptaggregat: Hautec Carno (Sole-Wasser-Wärmepumpe, Baujahr 2006, Kältemittel R 407C).
* Zusatzaggregat: Hautec HWAL (Abluft-Wärmepumpe).
* Nachrüstung: Aktive Kühlfunktion (nachgerüstet im Jahr 2010).
* Hydraulische Wege im System:
1. Weg 1 (Direktweg): Sole-Wärmepumpe liefert Kälte/Wärme direkt in die Flächenheizung (z. B. bei aktiver Brauchwassererwärmung).
   2. Weg 2 (Kombianlauf): Der Fluss wird durch das Gehäuse der Abluft-Wärmepumpe (HWAL) zur Flächenheizung geleitet. Dieser Weg wird automatisch gewählt, wenn kein Brauchwasser erwärmt wird.

------------------------------
## 2. Das Fehlerbild

* Heizbetrieb: Läuft auf beiden Wegen seit Jahren absolut problemlos.
* Kühlbetrieb über Weg 1 (Direkt): Funktioniert einwandfrei (Einschaltdauer des Verdichters > 20 Minuten).
* Kühlbetrieb über Weg 2 (über HWAL): Der Kühlvorgang bricht nach ca. 2 Minuten ab. Nach Ablauf der softwareseitigen Taktsperre (erneut ca. 2 Minuten) startet der Verdichter wieder neu. Es liegt ein extremes, materialschädigendes Takten vor.

------------------------------
## 3. Bisherige Erkenntnisse & Ursachenanalyse
Da die Anlage auf Weg 1 stabil kühlt, ist die Kältemaschine (Verdichter, Kältemittel, Umschaltventil) technisch intakt. Der Fehler ist rein hydraulischer Natur oder resultiert aus einem Konfigurationskonflikt der Sensorik auf Weg 2.
## Ursache A: Hydraulischer Totpunkt (Mangelnder Durchfluss)
Die Abluft-Wärmepumpe (HWAL) ist im Sommerbetrieb ausgeschaltet. In ihrem Inneren befinden sich Umschaltventile oder Rückschlagklappen. Da das Gerät im Kühlmodus elektrisch nicht aktiv angesteuert wird, verbleiben diese Ventile möglicherweise in einer geschlossenen oder blockierenden Position.

* Die Folge: Die Haupt-Wärmepumpe pumpt das eiskalte Wasser gegen einen massiven Widerstand. Das Wasser im internen Wärmetauscher steht.

## Ursache B: Frostschutz-Abschaltung durch Sensor-Schock
Der interne Fühler „WP Vorlauf“ sitzt direkt am heizungsseitigen Ausgang des internen Plattenwärmetauschers. Durch den mangelnden Durchfluss (Ursache A) stürzt die Temperatur an diesem Fühler innerhalb kürzester Zeit extrem ab.

* Die Folge: Sobald der Fühler einen kritischen Wert (z. B. < 14 °C oder < 12 °C) registriert, greift der softwareseitige Frostschutz der Hautec-Steuerung. Der Verdichter wird nach genau 2 Minuten hart abgeschaltet, um ein Einfrieren und Zerstören des Wärmetauschers zu verhindern.

## Ursache C: Reglerschwingung am Mischerkreisfühler
Der externe Fühler „Vorlauf HK2 Mischer“ sitzt hinter der Abluft-Wärmepumpe. Die HWAL besitzt im Sommer eine warme thermische Eigenmasse. Beim Start misst dieser Fühler Wärme und fordert Kühlung an. Sobald die Kälte der Hauptpumpe verzögert und schlagartig durch die HWAL bricht, stürzt der Fühlerwert ab. Die Software gerät durch die Trägheit des Zwischenaggregats in eine mathematische Regelschwingung und wirft den Verdichter ab.
------------------------------
## 4. Konkrete nächste Schritte zur Fehlerbehebung
Die Behebung sollte stufenweise erfolgen – beginnend mit einer Diagnose am Gerät bis hin zur endgültigen hydraulischen/elektronischen Anpassung.
## Schritt 1: Live-Diagnose am Display (Eigenleistung)
Starten Sie den Kühlbetrieb über den fehlerhaften Weg 2 und beobachten Sie die Fühlerwerte im Display der Steuerung im Sekundentakt bis zum Abbruch:

* Fokus auf Fühler „WP Vorlauf“: Fällt der Wert innerhalb der 2 Minuten rapide ab und löst bei einem bestimmten Tiefpunkt (z. B. 12–15 °C) die Abschaltung aus?
* Fokus auf Fühler „Vorlauf HK2 Mischer“: Ändert sich der Wert an diesem externen Fühler vor dem Abbruch überhaupt, oder bleibt er warm? (Ein Indiz dafür, ob überhaupt kaltes Wasser durch die HWAL fließt).

## Schritt 2: Manueller „Fühltest“ an den Rohren
Tasten Sie während der 2 Minuten Laufzeit die Rohre direkt vor und hinter der Abluft-Wärmepumpe (HWAL) ab:

* Wird das Rohr vor der HWAL eiskalt, aber das Rohr danach bleibt warm? $\rightarrow$ Beweis für fehlenden Durchfluss (Ventil in HWAL geschlossen).

## Schritt 3: Prüfung der elektrischen Verriegelung / Konfiguration
Prüfen Sie in den Parametern der Fachhandwerkerebene:

* Ist die HWAL im Sommer komplett stromlos (z. B. über eine Sicherung/Schalter)? Wenn ja: Testweise einschalten. Oft benötigen die internen Ventile Strom, um auf „Durchgang“ zu fahren.
* Gibt es im Regler eine Option, den Kühlbetrieb für die HWAL explizit freizugeben oder zu sperren, sodass die Ventile zwangsgeöffnet werden?

## Schritt 4: Die nachhaltige Lösung – Einbau eines Kühl-Bypasses (Fachhandwerker)
Energetisch und regelungstechnisch ist das Durchschleusen von kaltem Kühlwasser durch eine warme, inaktive Abluft-Wärmepumpe im Sommer nicht sinnvoll.

* Empfehlung: Installation eines motorisierten 3-Wege-Umschaltventils vor der HWAL. Sobald die Anlage in den Kühlbetrieb schaltet, muss dieses Ventil die HWAL komplett umgehen (Bypass) und das kalte Wasser direkt auf den funktionierenden Weg 1 in den Heizkreis leiten.

------------------------------
Um die Diagnose weiter zu verfeinern, lassen Sie mich wissen:

* Welche konkreten Temperaturen Sie bei Schritt 1 kurz vor dem Abschalten ablesen konnten.
* Welcher Regler-Typ genau in Ihrer Hautec verbaut ist (z. B. ein SC 6021).


---

Hier ist die finale, vollständige Zusammenfassung aller Erkenntnisse zu Ihrer Hautec Carno / HWAL-Kombianlage (Baujahr 2006, Kühl-Nachrüstung 2010) mit dem Regler TEM SE 6000 WPC.
Diese Zusammenfassung verknüpft Ihre Grafana-Messwerte und die gefundenen Parameter zu einer eindeutigen Fehlerursache und zeigt Ihnen den Weg zur Lösung.
------------------------------
## Abschluss-Analyse: Taktproblem im Kühlbetrieb (Hautec & TEM SE 6000)## 1. Das Fehlerbild

* Normalzustand: Der Heizbetrieb läuft auf allen Wegen fehlerfrei. Auch der Kühlbetrieb über Weg 1 (Direktweg zur Flächenheizung) funktioniert stabil mit Laufzeiten von über 20 Minuten.
* Problemzustand: Sobald kein Brauchwasser erwärmt wird, schaltet die Anlage automatisch auf Weg 2 (durch die inaktive Abluft-Wärmepumpe HWAL) um. In diesem Modus taktet die Kühlung exakt im 2-Minuten-Raster: Der Verdichter springt an, kühlt kurz und bricht nach ca. 120 Sekunden ab, um nach einer kurzen Pause wieder von vorn zu beginnen.

------------------------------
## 2. Die messtechnischen Fakten (Grafana-Auswertung)

* Der Temperatursturz (Gelbe Linie): Beim Start des Verdichters (erkennbar an der Magenta-Leistungsspitze) sinkt die Temperatur hinter der Abluft-Wärmepumpe rasant ab und pendelt sich bei 17,3 °C ein.
* Keine Kühlung im Haus (Orange Linie): Der Rücklauf aus der Wohnung bleibt währenddessen konstant warm bei knapp 21 °C. Es findet in diesen 2 Minuten also kein nennenswerter Energietransfer in die Räume statt.

------------------------------
## 3. Die exakte Fehlerursache: Warum schaltet die Anlage ab?
Das Problem ist ein Zusammenspiel aus hydraulischer Trägheit und der Sicherheitslogik des TEM-Reglers:

   1. Die blockierte 18°C-Schutzgrenze (Taupunktschutz):
   Obwohl im Steuerungs-Parameter 09-32 (TWVmin Kühlbetrieb) theoretisch 14 °C als Abschaltgrenze hinterlegt sind, wird dieser Wert im Alltag ignoriert. Da kein aktiver Raumfeuchtefühler verbaut ist, schaltet der TEM-Regler auf einen festen, internen Not-Taupunktschutz von exakt 18,0 °C um. Sobald der Vorlauffühler diesen Wert unterschreitet, wird der Verdichter zum Schutz vor feuchten Fußböden abgeschaltet. Ihre gemessenen 17,3 °C lösen genau diesen Schutzmechanismus aus.
   2. Die Ursache für die 17,3 °C (Parameter 07-14 = 3):
   Der Parameter für die Heizkreisfunktion steht im Kühlbetrieb auf 3 (Mischer geregelt). Nach dem Start des Kühlbetriebs reagiert der mechanische Heizungsmischer viel zu träge. Da das eiskalte Wasser zusätzlich durch das träge Volumen der ausgeschalteten HWAL fließen muss, staut sich die Kälte im Gerät. Bevor der Mischer weit genug geöffnet hat, um das kalte Wasser mit dem warmen Wasser aus dem Haus zu vermischen, ist die Temperatur am Sensor bereits unter 18 °C gefallen – die Anlage würgt sich selbst ab.

------------------------------
## 4. Konkrete Schritte zur Behebung## Schritt 1: Der Sofort-Test am Regler (Fehler verifizieren)
Stellen Sie den Parameter 07-14 (Heizkreisfunktion im Kühlbetrieb) testweise von 3 (geregelt) auf 2 (Mischer auf im Kühlbetrieb).

* Effekt: Der Mischer wird gezwungen, bei Kühlanforderung sofort zu 100 % zu öffnen. Das kalte Wasser wird ohne Verzögerung direkt in den Fußboden gespült.
* Ergebnis-Erwartung: Die Temperatur hinter der HWAL sollte durch das warme Wasser aus dem Haus sofort über 18 °C gepuffert werden. Läuft der Kühlbetrieb nun länger als 20 Minuten durch, ist die Ursache (Mischerträgheit/Durchflussproblem) zweifelsfrei bewiesen.

## Schritt 2: Die dauerhafte Lösung wählen
Falls der Test in Schritt 1 erfolgreich ist, haben Sie zwei Optionen für den Dauerbetrieb:

* Option A (Reine Einstellungssache): Belassen Sie den Parameter 07-14 dauerhaft auf dem Wert 2. Das ist die einfachste und kostengünstigste Lösung, sofern die Fußböden im Sommer dadurch nicht unangenehm kalt werden.
* Option B (Die saubere hydraulische Lösung): Beauftragen Sie einen Heizungsbauer mit dem Einbau eines motorisierten 3-Wege-Umschaltventils (Kühl-Bypass) vor der HWAL. Das Ventil sorgt dafür, dass das kalte Wasser im Sommer die Abluft-Wärmepumpe komplett umgeht und direkt auf dem funktionierenden Weg 1 in das Haus geleitet wird. Dadurch kann der Mischer wie gewünscht auf Wert 3 (geregelt) verbleiben, ohne dass es zu einem Kältestau kommt.

Geben Sie mir gern Bescheid, ob Sie den Parameter-Test (Wert 2) am Regler durchführen konnten und ob die Anlage damit die 2-Minuten-Grenze durchbrochen hat. Falls Sie Unterstützung beim Navigieren durch das TEM-Menü benötigen, helfe ich Ihnen gerne weiter!

