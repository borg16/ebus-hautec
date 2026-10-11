# Gezieltes Polling mit Home Assistant

Der Mitschnitt vom 09.10.2026 zeigt erfolgreiche Abfragen mit ebusd als Master
`31`, aber auch fehlgeschlagene Vorbereitungen und eine leere Antwort auf
`90 10 0a 02 20 0b`. Mit `--pollinterval=0` verschwinden laut Betreiber die Fehler.

## Einstellungen

1. `filter-seen=1` in der MQTT-Integration verwenden. Der Standardwert `5`
   aktiviert automatisches Polling für alle Nachrichten, die durch die übrigen
   Discovery-Filter kommen. Bei `1` veröffentlicht Discovery nur bereits
   beobachtete Nachrichten und vergibt keine zusätzlichen Poll-Prioritäten.
2. Aktuell sind keine Lesemodelle für Polling markiert. Remote1 und Remote2
   werden ausschließlich durch Mithören aktualisiert, sofern keine expliziten
   Lesezugriffe ausgelöst werden. Für künftig gewünschte andere Werte gezielt
   `@poll(5)` ergänzen. Der CSV-Compiler erzeugt dafür `r5`; die Zahl ist eine
   relative Priorität, kein Sekundenintervall.
3. `--pollinterval=5` beibehalten: Die Polling-Funktion steht für spätere Werte
   bereit, sendet ohne Poll-Prioritäten aber keine automatischen Abfragen.
   Künftig markierte Nachrichten teilen sich das globale Intervall; jede einzelne
   wird nicht alle fünf Sekunden abgefragt. Kürzlich mitgehörte Daten können
   eine Abfrage ersetzen.

Im Repository-Verzeichnis neu kompilieren:

```bash
npm run build:csv
```

Den bisherigen ebusd-Prozess beenden und mit diesem angepassten Aufruf neu
starten; keinen zweiten Prozess für denselben Adapter starten:

```bash
sudo ebusd --pidfile /var/run/ebusd.pid \
  -d ens:/dev/ttyACM0 \
  --mqttport 1883 --mqttjson \
  -l /var/log/ebusd/ebusd.log \
  --log=all:debug --log=update:notice --log=other:debug \
  -c "$HOME/Repos/ebus-hautec/csv-output/@ebusd/ebus-typespec" \
  --pollinterval=5 \
  --mqttvar='filter-name=status|temp|humidity|yield|count|energy|power|runtime|hours|starts|mode|curve|^load$|^party$|sensor|timer|stunden|anlaufzaehler,filter-seen=1' \
  --mqttint=/etc/ebusd/mqtt-hassio.cfg
```

Alternativ in `/etc/ebusd/mqtt-hassio.cfg` den Wert `filter-seen = 5` auf
`filter-seen = 1` ändern; dann ist der zusätzliche Kommandozeilenwert unnötig.
Die Datei unter `/etc` wird durch dieses Repository nicht verändert.

`--log=update:notice` macht erfolgreiche Lese- und mitgehörte Telegramme sichtbar.
Nach dem Neustart sollten null Poll-Nachrichten geladen sein. Keine zusätzlichen
Poll-Prioritäten über MQTT `/get`, `ebusctl read -p` oder HTTP setzen, solange
die jeweilige Abfrage nicht geprüft ist. Alte dynamische Prioritäten werden
durch den Neustart verworfen.

## Grenzen der bestehenden Lesedefinitionen

- `StartCounterUnit1/2`, `OperatingHoursUnit1/2` und
  `TemperaturSollwerte3001Bedienteil1/2` enthalten variable Masterdaten
  (`@out`, CSV-Part `m`). Diese Daten müssen beim Senden vorliegen. Ein
  automatischer Poll ohne Eingabewerte endet mit `end of input reached`.
  Die mitgeschnittenen TEM-Zählerübertragungen sind keine leeren
  Standard-Leseabfragen; die Felder dürfen nicht pauschal auf `@in` gedreht
  oder mit Nullwerten gefüllt werden.
- `TemperaturSollwerte200BBedienteil1` erhält im aktuellen Log eine gültige
  Antwort mit null Nutzdatenbytes (`00`), während die Definition Temperaturdaten
  erwartet. Ursache der leeren Antwort beziehungsweise Unterstützung dieses
  Selektors ist noch ungeklärt. Die funktionierende Abfrage `2001` liefert die
  Basis-Solltemperaturen von Bedienteil 1.
- Alle Remote-Leseabfragen und der generische TEM-Menüblock bleiben ohne
  Poll-Priorität. Auch die erfolgreich geprüften Remote-Abfragen werden auf
  Betreiberwunsch nicht automatisch gepollt.

Die bestehenden Definitionen bleiben zum Dekodieren und für explizite Zugriffe
erhalten. Mitgehörte Zähler, Sollwerte und Broadcasts werden weiterhin verarbeitet;
deren Aktualisierung hängt von den Telegrammen des Reglers ab. Die historischen
Nachrichtentypen werden hier nicht grundsätzlich überarbeitet.

Für weitere Poll-Nachrichten zunächst eine eigenständige Leseabfrage ohne
variable Masterdaten und mit passender Antwort nachweisen, dann `@poll(5)`
ergänzen und die CSV-Dateien neu erzeugen. Änderungen an generierten
`controller.tsp`-Definitionen müssen im Generator berücksichtigt werden.

Referenz: [ebusd MQTT-Integration](https://github.com/john30/ebusd/blob/master/contrib/etc/ebusd/mqtt-hassio.cfg),
Kommentare zu `filter-seen`.
