# Häufigkeit und Regelmäßigkeit der Statusnachrichten

Datei: `ebusd.log` · SHA-256: `c75b682075b05290c306ff51d34909c51ddb8cd26bac1c0995e9fc972bbfaffb`

Zeitraum: **2026-09-27 00:54:44.942000 bis 2026-09-27 17:51:26.799000**, entsprechend **16.9450 Stunden**. Zeitangaben entsprechen unverändert der Log-Uhrzeit.

53070 Raw-Zeilen, **52793 Telegramme mit gültiger Master-CRC**, 277 ausgeschlossene Zeilen. Am Dateianfang stehen 2474361 Nullbytes ohne Zeitinformation; sie werden übersprungen. Die Quelldatei wird nicht verändert.

## Broadcast-Status aus broadcast.tsp

| Nachricht | Quelle → Ziel | Anzahl | Median s | Mittel s | P95 s | Maximum s | ±1 s um Median |
|---|---|---:|---:|---:|---:|---:|---:|
| TemperatureValues_1000 | `10 → fe` | 759 | 80.001 | 80.393 | 80.157 | 246.715 | 99.08 % |
| TemperatureValues_1001 | `10 → fe` | 759 | 80.001 | 80.393 | 80.157 | 246.995 | 99.08 % |
| ControllerData_1002 | `10 → fe` | 760 | 80.001 | 80.287 | 80.142 | 166.979 | 98.95 % |
| TemperatureTargets_1003 | `10 → fe` | 760 | 80.001 | 80.286 | 80.142 | 166.713 | 99.08 % |
| OperatingStatus_1100 | `10 → fe` | 759 | 80.001 | 80.393 | 80.157 | 246.715 | 99.08 % |
| OperatingStatus_1101 | `10 → fe` | 759 | 80.001 | 80.393 | 80.157 | 246.995 | 99.08 % |
| TimeAndStatus_1102 | `10 → fe` | 760 | 80.001 | 80.287 | 80.142 | 166.979 | 98.95 % |
| TimeAndStatus_1103 | `10 → fe` | 760 | 80.001 | 80.286 | 80.142 | 166.713 | 99.08 % |

Alle acht Statusblöcke haben einen Median von rund **80 Sekunden**. Die Selektorfamilien `10 xx` und `11 xx` sind getrennte Telegramme; die Namenssuffixe geben die beiden Selektorbytes hexadezimal wieder. Die CSV enthält die exakten Minima, Standardabweichungen, Zeitgrenzen und Raten pro Stunde. Die Quote ±1 s bezieht sich auf aufeinanderfolgende Abstände innerhalb der jeweiligen Nachrichtengruppe.

## Weitere Broadcasts

| Nachricht | Quelle → Ziel | Anzahl | Median s | Mittel s | P95 s | Maximum s | ±1 s um Median |
|---|---|---:|---:|---:|---:|---:|---:|
| ToFAxSub | `10 → fe` | 761 | 80.001 | 80.181 | 80.111 | 216.838 | 99.21 % |
| DateTimeBroadcast | `10 → fe` | 2030 | 29.985 | 30.053 | 31.119 | 106.759 | 77.28 % |
| IdentificationWrite | `10 → fe` | 1 | — | — | — | — | — |
| OperationalData | `10 → fe` | 2030 | 29.969 | 30.053 | 31.094 | 109.869 | 75.16 % |
| ControlCommands | `10 → fe` | 2030 | 30.063 | 30.053 | 31.094 | 109.447 | 79.20 % |
| ErrorMessage | `10 → fe` | 2 | 8.954 | 8.954 | 8.954 | 8.954 | 100.00 % |

## Status- und Änderungsabfragen des Reglers an die Bedienteile

| Nachricht | Quelle → Ziel | Anzahl | Median s | Mittel s | P95 s | Maximum s | ±1 s um Median |
|---|---|---:|---:|---:|---:|---:|---:|
| Statusblock04Bedienteil1 | `10 → 90` | 760 | 80.001 | 80.287 | 80.157 | 166.839 | 99.08 % |
| DatenAenderungsabfrageBedienteil1 | `10 → 90` | 789 | 80.001 | 77.230 | 80.142 | 146.708 | 93.65 % |
| SteuerblockD114Bedienteil1 | `10 → 90` | 789 | 80.001 | 77.230 | 80.142 | 146.713 | 93.65 % |
| Statusblock05Bedienteil2 | `10 → 91` | 760 | 80.001 | 80.286 | 80.142 | 166.838 | 99.08 % |
| DatenAenderungsabfrageBedienteil2 | `10 → 91` | 784 | 80.001 | 77.724 | 80.142 | 146.990 | 94.76 % |
| SteuerblockD115Bedienteil2 | `10 → 91` | 784 | 80.001 | 77.724 | 80.142 | 146.994 | 94.76 % |

## Durch ebusd gesendete Statusabfragen (Quelle 31)

| Nachricht | Quelle → Ziel | Anzahl | Median s | Mittel s | P95 s | Maximum s | ±1 s um Median |
|---|---|---:|---:|---:|---:|---:|---:|
| Statusblock05Bedienteil1 | `31 → 90` | 1015 | 60.001 | 60.070 | 60.033 | 130.987 | 99.90 % |
| Statusblock04Bedienteil2 | `31 → 91` | 1016 | 60.001 | 60.070 | 60.032 | 130.994 | 99.90 % |
| Statusblock05Bedienteil2 | `31 → 91` | 994 | 60.001 | 61.340 | 60.042 | 130.994 | 97.78 % |

Diese Abfragen werden getrennt von den durch Quelle 10 ausgelösten Reglertelegrammen gezählt. Ein Anfrage-/Antwortaustausch zählt einmal, nicht zweimal. Die Antwortdaten werden nicht als zusätzliche Broadcast-Nachricht gezählt.

## Betriebsdaten der Wärmeerzeuger

| Nachricht | Quelle → Ziel | Anzahl | Median s | Mittel s | P95 s | Maximum s | ±1 s um Median |
|---|---|---:|---:|---:|---:|---:|---:|
| BetriebsdatenFeuerungsautomat1AnRegler | `03 → 10` | 7617 | 8.000 | 8.010 | 9.234 | 80.712 | 55.63 % |
| Betriebsdaten1 | `10 → 03` | 3047 | 20.000 | 20.025 | 20.094 | 98.806 | 99.21 % |
| Betriebsdaten2 | `10 → 13` | 3047 | 20.000 | 20.025 | 20.094 | 98.806 | 99.21 % |
| BetriebsdatenFeuerungsautomat2AnRegler | `13 → 10` | 7614 | 8.000 | 8.012 | 9.203 | 81.306 | 59.67 % |

## Lücken

Die längste Lücke zwischen beliebigen aufeinanderfolgenden Raw-Zeilen beträgt **79.338 s**, von **2026-09-27 14:52:07.937000 bis 2026-09-27 14:53:27.275000**. Ob währenddessen der Bus oder nur die Aufzeichnung unterbrochen war, lässt sich aus dem Mitschnitt allein nicht entscheiden. Die Abstände in den Tabellen enthalten diese Lücke; es werden keine vermeintlich fehlenden Telegramme ergänzt.

Die 16 längsten Abstände der acht Broadcast-Statusblöcke:

| Nachricht | Von | Bis | Abstand s | Logzeilen |
|---|---|---|---:|---|
| TemperatureValues_1001 | 2026-09-27 14:51:02.262 | 2026-09-27 14:55:09.257 | 246.995 | 43706 → 43883 |
| OperatingStatus_1101 | 2026-09-27 14:51:01.644 | 2026-09-27 14:55:08.639 | 246.995 | 43705 → 43882 |
| TemperatureValues_1000 | 2026-09-27 14:50:52.402 | 2026-09-27 14:54:59.117 | 246.715 | 43698 → 43874 |
| OperatingStatus_1100 | 2026-09-27 14:50:51.784 | 2026-09-27 14:54:58.499 | 246.715 | 43697 → 43873 |
| ControllerData_1002 | 2026-09-27 14:51:32.262 | 2026-09-27 14:54:19.241 | 166.979 | 43735 → 43843 |
| TimeAndStatus_1102 | 2026-09-27 14:51:31.644 | 2026-09-27 14:54:18.623 | 166.979 | 43734 → 43842 |
| TemperatureTargets_1003 | 2026-09-27 14:51:42.419 | 2026-09-27 14:54:29.132 | 166.713 | 43743 → 43851 |
| TimeAndStatus_1103 | 2026-09-27 14:51:41.801 | 2026-09-27 14:54:28.514 | 166.713 | 43742 → 43850 |
| TemperatureValues_1000 | 2026-09-27 14:54:59.117 | 2026-09-27 14:56:59.227 | 120.110 | 43874 → 44023 |
| OperatingStatus_1100 | 2026-09-27 14:54:58.499 | 2026-09-27 14:56:58.609 | 120.110 | 43873 → 44022 |
| TemperatureTargets_1003 | 2026-09-27 14:54:29.132 | 2026-09-27 14:56:29.227 | 120.095 | 43851 → 43997 |
| TimeAndStatus_1103 | 2026-09-27 14:54:28.514 | 2026-09-27 14:56:28.609 | 120.095 | 43850 → 43996 |
| TemperatureValues_1001 | 2026-09-27 14:55:09.257 | 2026-09-27 14:57:09.227 | 119.970 | 43883 → 44032 |
| OperatingStatus_1101 | 2026-09-27 14:55:08.639 | 2026-09-27 14:57:08.609 | 119.970 | 43882 → 44031 |
| ControllerData_1002 | 2026-09-27 14:54:19.241 | 2026-09-27 14:56:19.102 | 119.861 | 43843 → 43989 |
| TimeAndStatus_1102 | 2026-09-27 14:54:18.623 | 2026-09-27 14:56:18.484 | 119.861 | 43842 → 43988 |

## Methode und Dateien

Gruppiert wird nach Richtung (`<` empfangen, `>` von ebusd gesendet), Quelle, Ziel und Dienst; bei `10 0a` zusätzlich nach den ersten beiden Nutzdatenbytes. Namen stammen aus den aktuellen TypeSpec-Dateien. Andere Dienste, etwa Parameterabfragen `06 21`, werden in der vollständigen CSV nach Dienst zusammengefasst. Alle Telegramme müssen vollständige Masterdaten und eine gültige Master-CRC enthalten. ACK-/Antwortprüfung ist separat in `summary.json` ausgewiesen und kein zusätzlicher Filter der Häufigkeit. Unvollständige Fragmente sind in `excluded-lines.csv` aufgelistet. Wiederholungen zählen als eigene beobachtete Übertragungen.

Intervalle sind Differenzen aufeinanderfolgender Log-Zeitstempel derselben Gruppe. P95 ist das linear interpolierte 95. Perzentil: 95 % der Abstände liegen höchstens ungefähr dort. Randzeiten vor dem ersten bzw. nach dem letzten Auftreten werden nicht als Intervalle behandelt. Die Statistik beschreibt diesen Mitschnitt, keine garantierten Protokollfristen. Aussagekräftig für den üblichen Takt sind Median und P95; Mittelwert und Maximum enthalten auch Unterbrechungen.

- [frequency.csv](frequency.csv): sämtliche beobachteten Nachrichtengruppen.
- [broadcast-intervals.csv](broadcast-intervals.csv): jeder Abstand der acht Broadcast-Statusblöcke mit Logzeilen.
- [summary.json](summary.json): Zeitraum, Prüfsumme, Parser- und Transportbilanz.
- [excluded-lines.csv](excluded-lines.csv): ausgeschlossene Fragmente/Fehler.

Reproduzieren: `python3 scripts/analyze_status_frequency.py ebusd.log`
