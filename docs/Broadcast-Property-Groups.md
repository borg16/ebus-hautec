# Gemeinsame Eigenschaften in Broadcast-Nachrichten

Mehrere Broadcasts liefern dieselbe oder sehr wahrscheinlich dieselbe fachliche
Eigenschaft unter unterschiedlichen Feldnamen. Die folgenden kanonischen Namen
eignen sich als gemeinsame Namen in Home Assistant, Grafana oder einer anderen
Auswertung. Sie sind zunächst **Auswertungs-Aliase**; die bestehenden
Telegramm- und Feldnamen bleiben für ebusd und MQTT unverändert.

Die Schreibweise ist kleingeschriebenes `snake_case`. Bei Heizkreisdaten bleibt
`hk1` beziehungsweise `hk2` Teil der Kennung: gleiche Bedeutung heißt dort
nicht gleicher Messwert.

## Gut belegte Gruppen

| Kanonischer Name | Broadcast-Feld(er) | Einordnung |
| --- | --- | --- |
| `outside_temperature` | `DateTimeBroadcast.ta`, `Status0a.ta`, `Status1a.ta` | Außentemperatur in drei Telegrammen; für eine gemeinsame Verlaufsreihe jeweils denselben Alias verwenden. |
| `dhw_loading_status` | `Status0a.BWR_Ventil`, `Status1a.BWR_Aktiv` | Die Kommentare ordnen beide Bits demselben Warmwasser-Lade-/Nachlauf-Kandidaten zu. Das Signal belegt keinen tatsächlichen Pumpen- oder Verdichterlauf. |
| `fa2_stage_active` | `Status0a.Bit10`, `Status1a.Bit2` | Die Kommentare vergleichen beide Felder mit der FA2-Stufe. Die Übereinstimmung ist sehr hoch, aber Übergangssamples können abweichen; physischer Ausgang nicht bestätigt. |
| `system_stage1_enable` | `Status0a.Bit1`, `OperationalData.Kessel2InBetrieb` | In `Status0a` ausdrücklich als identisch mit `Kessel2InBetrieb` kommentiert. „Enable“ beschreibt den logischen Statuskandidaten, keinen nachgewiesenen Verdichterlauf. |
| `hk1_minutes` | `Status2a.Mins` | Minutenwert für HK1. |
| `hk2_minutes` | `Status3a.Mins` | Entsprechender Minutenwert für HK2; gleicher Feldname und Typ wie HK1, aber eigener Heizkreis. |
| `hk1_operating_state` | `Status2a.b3` | HK1: `01` Heizen/Tag, `00` Absenken/Nacht, `04` Aus. |
| `hk2_operating_state` | `Status3a.b5` | HK2 mit derselben dokumentierten Codierung wie `Status2a.b3`. |
| `hk1_operating_mode` | `Status2a.b4` | HK1-Modus, Codierung `03` bis `50` laut Feldkommentar. |
| `hk2_operating_mode` | `Status3a.b6` | HK2-Modus mit derselben dokumentierten Codierung wie `Status2a.b4`. |
| `hk1_time_program` | `Status2a.b6` | HK1-Programmkennung: `01`, `03`, `05` für Programm 1, 2, 3. |
| `hk2_time_program` | `Status3a.b4` | HK2-Programmkennung mit derselben dokumentierten Codierung wie `Status2a.b6`. |

`hk1_minutes` und `hk2_minutes` sollten getrennte Sensoren bleiben. Für eine
Ansicht, die den jeweils aktiven Heizkreis auswählt, kann Home Assistant beide
unter einem übergeordneten Anzeigenamen „Heizkreis-Minuten“ darstellen.

## Plausible Zuordnungen, noch nicht als identisch behandeln

| Vorgeschlagener Alias | Broadcast-Feld(er) | Warum noch unsicher |
| --- | --- | --- |
| `heat_pump_flow_temperature` | `Status0b.tf_hp`, möglicherweise `Status1b.tf_hp` | `Status0b.tf_hp` ist durch direkte `00-07`-Vergleiche gut als TWV gestützt. `Status1b.tf_hp` ist nur als derselbe TWV-Kandidat bezeichnet; ein direkter Vergleich fehlt. |
| `heat_pump_return_temperature` | `OperationalData.tr_hp`, möglicherweise `Status0b.tr_hp` | Beide heißen `tr_hp`; `Status0b.tr_hp` ist als Wärmepumpen-Rücklauftemperatur beschrieben. Ein zeitgleicher Vergleich der beiden Broadcastwerte ist hier nicht dokumentiert. |
| `dhw_target_temperature` | `ControlCommands.hotWaterTargetTemperature`, möglicherweise `Status3b.TB_target` | Beide Feldbeschreibungen nennen den Warmwasser-Sollwert. Ein Vergleich beider Telegramme oder eine Bestätigung der Firmware-Zuordnung fehlt. |

Diese Kandidaten erst dann auf einen einzigen Datenpunkt abbilden, wenn ein
zeitgleicher Mitschnitt die Wertezuordnung bestätigt. Bis dahin getrennte
Entitäten behalten oder die Kandidaten in der Auswertung sichtbar kennzeichnen.

## Umsetzung in einer Auswertung

Für eindeutig gleiche Eigenschaften kann man die Quellen in Home Assistant
unter einem gemeinsamen Anzeigenamen zusammenführen oder eine Template-Entität
mit dem Alias als `unique_id` anlegen. Bei zeitlich leicht versetzten
Broadcasts sollte die Auswertung den zuletzt verfügbaren gültigen Wert
übernehmen. Mehrere Quellen derselben Temperatur dürfen nicht addiert oder
gemittelt werden, solange keine zeitliche Synchronität sichergestellt ist.

Eine Umbenennung direkt in `broadcast.tsp` würde die von ebusd erzeugten
Nachricht-/Feldpfade ändern. Sie sollte deshalb erst zusammen mit einer
Migration der MQTT-Abonnenten und Dashboards erfolgen.
