# Tatsächlich genutzte Menüs

Vergleich von `commands.txt` (aktueller Scan) mit vollständigen, CRC-geprüften Parameterantworten von 01 → 15 in `input/complete.log`. Alle Adressen sind hexadezimal. Ein Selektor umfasst Menü, Index und Kontext; gleiche TEM-Kennungen werden nicht zusammengelegt.

Der Scan enthält 503 Selektoren. Alle 201 im Mitschnitt gültig gelesenen Selektoren sind enthalten und liefern dieselbe TEM-Kennung. 302 Scan-Selektoren wurden dort nicht gültig gelesen. Die 3841 Leseantworten schließen Wiederholungen ein; ff1f-Antworten sind nicht als erfolgreiche Parameterzugriffe gezählt.

| Menü | Verzeichnisblock | Selektoren im Scan | Davon im Mitschnitt gelesen | Leseantworten |
|---|---|---:|---:|---:|
| 00 | 00 | 3 | 1 | 14 |
| 01 | 00 | 17 | 17 | 2662 |
| 02 | 00 | 1 | 0 | 0 |
| 03 | 00 | 18 | 0 | 0 |
| 08 | 01 | 30 | 27 | 439 |
| 09 | 01 | 48 | 38 | 207 |
| 0a | 01 | 2 | 2 | 29 |
| 0b | 01 | 12 | 12 | 144 |
| 0c | 01 | 6 | 0 | 0 |
| 0d | 01 | 1 | 0 | 0 |
| 0e | 01 | 1 | 0 | 0 |
| 0f | 01 | 2 | 2 | 11 |
| 10 | 02 | 1 | 0 | 0 |
| 21 | 04 | 32 | 10 | 77 |
| 23 | 04 | 24 | 2 | 2 |
| 29 | 05 | 2 | 0 | 0 |
| 2a | 05 | 2 | 0 | 0 |
| 63 | 0c | 4 | 0 | 0 |
| 64 | 0c | 7 | 0 | 0 |
| 65 | 0c | 9 | 0 | 0 |
| 66 | 0c | 9 | 0 | 0 |
| 67 | 0c | 14 | 0 | 0 |
| 69 | 0d | 11 | 0 | 0 |
| 6a | 0d | 7 | 0 | 0 |
| 6b | 0d | 8 | 0 | 0 |
| 6c | 0d | 8 | 0 | 0 |
| 6d | 0d | 8 | 0 | 0 |
| 6e | 0d | 8 | 0 | 0 |
| 6f | 0d | 8 | 0 | 0 |
| 70 | 0e | 8 | 0 | 0 |
| 71 | 0e | 8 | 0 | 0 |
| 72 | 0e | 8 | 0 | 0 |
| a3 | 14 | 8 | 4 | 8 |
| a4 | 14 | 8 | 8 | 9 |
| a5 | 14 | 11 | 11 | 25 |
| a6 | 14 | 11 | 11 | 23 |
| a7 | 14 | 16 | 16 | 68 |
| a8 | 15 | 5 | 0 | 0 |
| a9 | 15 | 38 | 17 | 33 |
| aa | 15 | 15 | 15 | 39 |
| ab | 15 | 8 | 8 | 51 |
| ac | 15 | 8 | 0 | 0 |
| ad | 15 | 8 | 0 | 0 |
| ae | 15 | 8 | 0 | 0 |
| af | 15 | 8 | 0 | 0 |
| b0 | 16 | 8 | 0 | 0 |
| b1 | 16 | 8 | 0 | 0 |
| b2 | 16 | 8 | 0 | 0 |

## Paare mit Menüversatz +40 hex

Alle Positionen des unteren Menüs existieren im oberen Gegenstück. In diesem Scan sind ihre TEM-Kennungen und vollständigen Antwortbytes jeweils identisch. Das ist eine starke Stütze für alternative Ansichten, aber kein allgemeiner Beweis identischer interner Speicherung oder Zugriffsrechte.

| Unteres Menü | Oberes Menü | Gemeinsame Selektoren, einschließlich Kontexte | Zusätzliche Selektoren oben |
|---|---|---:|---:|
| 63 | a3 | 4 | 4 |
| 64 | a4 | 7 | 1 |
| 65 | a5 | 9 | 2 |
| 66 | a6 | 9 | 2 |
| 67 | a7 | 14 | 2 |
| 69 | a9 | 11 | 27 |
| 6a | aa | 7 | 8 |
| 6b | ab | 8 | 0 |
| 6c | ac | 8 | 0 |
| 6d | ad | 8 | 0 |
| 6e | ae | 8 | 0 |
| 6f | af | 8 | 0 |
| 70 | b0 | 8 | 0 |
| 71 | b1 | 8 | 0 |
| 72 | b2 | 8 | 0 |
