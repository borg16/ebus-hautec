# Zugriff auf die ebus-Daten in VictoriaMetrics

Alle ebusd-Nachrichten (per MQTT und Telegraf) liegen in VictoriaMetrics unter
`http://raspi:8428`. Die Prometheus-kompatible API genügt für Analysen.

## Hilfsskript

[scripts/vm_query.py](../scripts/vm_query.py) gibt Zeitreihen als Liste der
Wertänderungen aus (`--all` zeigt jeden Wert):

```sh
python3 scripts/vm_query.py 'ebus_tf_hp_value{topic="ebusd/Broadcast/Status0b"}' -- -6h now 1m
python3 scripts/vm_query.py ebus_startcounter_value 2026-10-11T09:00 2026-10-11T10:30 1s
```

Zeiten: `now`, relativ (`-6h`, `-8d`, dann `--` davor setzen) oder lokale ISO-Zeit.

## Rohabfragen mit curl

```sh
# Metrikliste
curl -s 'http://raspi:8428/api/v1/label/__name__/values'
# Serien (Topics) einer Metrik der letzten Stunde
curl -s 'http://raspi:8428/api/v1/series' -d 'match[]=ebus_startcounter_value' -d start=-1h
# Zeitreihe
curl -s 'http://raspi:8428/api/v1/query_range' --data-urlencode 'query=ebus_tf_hp_value' \
  -d start=-6h -d end=now -d step=1m
```

Zeitstempel in den Antworten sind Unix-Sekunden. `step` bestimmt die
Auflösung: Zu groß gewählte Schritte verschlucken kurze Ereignisse, für
einzelne Starts also `1s`–`10s` verwenden.

## Namensschema

- **Metrik:** `ebus_<feldname_klein>_value`, zum Beispiel `ebus_tf_hp_value`.
  Teils existieren zusätzlich Varianten mit Großbuchstaben, `ebus2_*` und
  `mqtt_consumer_*` aus älteren Konfigurationen. Für aktuelle Daten
  `ebus_<klein>_value` nehmen.
- **Label `topic`:** `ebusd/<Circuit>/<Nachricht>`. Gleiche Feldnamen kommen in
  mehreren Nachrichten vor, deshalb immer mit `topic` filtern, zum Beispiel
  `{topic="ebusd/Broadcast/Status0b"}` oder `{topic=~".*Feuerungsautomat1.*"}`.
- **Weitere Quellen:** Die Hausleistung steht in `senec_ENERGY_GUI_HOUSE_POW`
  (Watt, Wärmepumpe läuft ab etwa 2 kW zusätzlich zur Grundlast von etwa 0,6–0,9 kW).

## Wichtige Metriken

| Zweck | Metrik / Topic |
|---|---|
| Vorlauf/Rücklauf Wärmepumpe | `ebus_tf_hp_value`, `ebus_tr_hp_value` mit `topic="ebusd/Broadcast/Status0b"` |
| Zieltemperatur Heizkreis | `ebus_tf_hc_target_value` (`Broadcast/Status3b`) |
| Warmwasser Ist/Soll | `ebus_tb_value`, `ebus_tb_target_value` |
| Stufenanforderung | `ebus_n1_value`, `ebus_n2_value`, `ebus_n3_value` (`Broadcast/Status3b`) |
| Verdichterstufen 1/2 | `Burner1/…Feuerungsautomat1AnRegler`, `Burner2/…`: `flame`, `settinglevel`, `boilertemperature`, `returnwatertemperature`; `Burner1/Betriebsdaten1`: `kesselsollt`, `stellgrad` |
| Anlaufzähler | `ebus_startcounter_value` (`Remote1/StartCounterUnit1`, `Remote2/StartCounterUnit2`) |
| Betriebsstunden | `ebus_hours_value`, `ebus_minutes_value` (`Remote*/OperatingHoursUnit*`) |
| Raumtemperatur | `ebus_t_room_value` (`Remote*/Statusblock0*Bedienteil*`) |
| Fehler | `ebus_errorcode_value`, `ebus_alarm_value` |

## Interpretationshinweise

- **`flame`/`stellgrad` bedeuten Anforderung, nicht Verdichterlauf.** Der
  Verdichter läuft nur, wenn zusätzlich die Hausleistung um etwa 2 kW steigt
  und Vorlauf/Rücklauf reagieren.
- **Anlaufzähler:** `StartCounterUnit*` springt alle 10 Minuten kurz auf 99
  und zurück. Das sind Lesefehler und keine Starts; ignorieren oder
  per `step`/Filter entfernen. Der Zähler zählt erst bei der nächsten
  Abfrage und hinkt dem echten Start deshalb um Minuten hinterher.
- **Heizkreis im Standby:** Dann bleibt `ebus_tf_hc_target_value` auf 0. Die
  Regelung fordert beide Stufen an (Sollwert 33–34 °C, Stellgrad 100 %), der
  Verdichter läuft aber nicht. Beobachtet am 11.10.2026: Mit Uhrenprogramm 1
  stieg das Ziel auf 24,1 °C, die Hausleistung auf etwa 2,35 kW und der
  Vorlauf von 25,6 auf 31,9 °C.
- **Zusatzheizung:** In den ebus-Daten gibt es kein eigenes Signal dafür.
  `Burner2` ist die zweite Wärmepumpenstufe.
- **Zeitzone:** Das Hilfsskript gibt lokale Zeit aus (CEST).
