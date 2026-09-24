# Zugriffe aus master.log

Generiert durch `scripts/analyze_master_log.py`. Die Namen entsprechen [controller.tsp](../controller.tsp), Circuit `15`.

Alle Anfragen sind im Mitschnitt beobachtet und CRC-geprüft. TEM-Kennungen stammen aus den Antworten. Bezeichnungen stammen, soweit vorhanden, aus dem STE-Katalog; dessen Werte und Auswahltexte werden nicht übernommen.

Der Suffix im Modellnamen ist die vollständige Anfrage in Hex. Verschiedene Zugriffe auf dieselbe TEM-Kennung bleiben getrennt. Die zusätzliche Instanz mit `10 00` wird nicht ohne Nachweis als HK 2 bezeichnet.

| Modell | TEM | Bezeichnung | Service / Anfrage | Antworttyp | Erste Logzeile | Anzahl |
|---|---|---|---|---|---:|---:|
| `P00_000_0101` | 00-00 | TEM 00-00; Bezeichnung nicht im STE-Katalog | `0621 / 0101` | `Zahlenantwort<Celsius10>` | 3 | 256 |
| `P00_000_0800` | 00-00 | TEM 00-00; Bezeichnung nicht im STE-Katalog | `0621 / 0800` | `Zahlenantwort<Celsius10>` | 108 | 45 |
| `P00_000_08801000` | 00-00 | TEM 00-00; Bezeichnung nicht im STE-Katalog | `0621 / 08801000` | `Zahlenantwort<Celsius10>` | 538 | 15 |
| `P00_000_0900` | 00-00 | TEM 00-00; Bezeichnung nicht im STE-Katalog | `0621 / 0900` | `Zahlenantwort<Celsius10>` | 948 | 4 |
| `P00_001_0801` | 00-01 | TEM 00-01; Bezeichnung nicht im STE-Katalog | `0621 / 0801` | `Zahlenantwort<Celsius10>` | 109 | 46 |
| `P00_001_08811000` | 00-01 | TEM 00-01; Bezeichnung nicht im STE-Katalog | `0621 / 08811000` | `Zahlenantwort<Celsius10>` | 541 | 11 |
| `P00_001_0902` | 00-01 | TEM 00-01; Bezeichnung nicht im STE-Katalog | `0621 / 0902` | `Zahlenantwort<Celsius10>` | 949 | 4 |
| `P00_001_09821000` | 00-01 | TEM 00-01; Bezeichnung nicht im STE-Katalog | `0621 / 09821000` | `Zahlenantwort<Celsius10>` | 1775 | 1 |
| `P00_002_0802` | 00-02 | TEM 00-02; Bezeichnung nicht im STE-Katalog | `0621 / 0802` | `Zahlenantwort<Celsius10>` | 112 | 18 |
| `P00_002_08821000` | 00-02 | TEM 00-02; Bezeichnung nicht im STE-Katalog | `0621 / 08821000` | `Zahlenantwort<Celsius10>` | 542 | 6 |
| `P00_002_0904` | 00-02 | TEM 00-02; Bezeichnung nicht im STE-Katalog | `0621 / 0904` | `Zahlenantwort<Celsius10>` | 951 | 9 |
| `P00_002_09841000` | 00-02 | TEM 00-02; Bezeichnung nicht im STE-Katalog | `0621 / 09841000` | `Zahlenantwort<Celsius10>` | 1777 | 2 |
| `P00_004_0803` | 00-04 | TEM 00-04; Bezeichnung nicht im STE-Katalog | `0621 / 0803` | `Zahlenantwort<Celsius10>` | 116 | 17 |
| `P00_004_08831000` | 00-04 | TEM 00-04; Bezeichnung nicht im STE-Katalog | `0621 / 08831000` | `Zahlenantwort<Celsius10>` | 543 | 5 |
| `P00_004_0906` | 00-04 | TEM 00-04; Bezeichnung nicht im STE-Katalog | `0621 / 0906` | `Zahlenantwort<Celsius10>` | 955 | 13 |
| `P00_004_09861000` | 00-04 | TEM 00-04; Bezeichnung nicht im STE-Katalog | `0621 / 09861000` | `Zahlenantwort<Celsius10>` | 1779 | 4 |
| `P00_007_0804` | 00-07 | TEM 00-07; Bezeichnung nicht im STE-Katalog | `0621 / 0804` | `Zahlenantwort<Celsius10>` | 123 | 9 |
| `P00_007_08841000` | 00-07 | TEM 00-07; Bezeichnung nicht im STE-Katalog | `0621 / 08841000` | `Zahlenantwort<Celsius10>` | 544 | 6 |
| `P00_007_0908` | 00-07 | TEM 00-07; Bezeichnung nicht im STE-Katalog | `0621 / 0908` | `Zahlenantwort<Celsius10>` | 968 | 9 |
| `P00_007_09881000` | 00-07 | TEM 00-07; Bezeichnung nicht im STE-Katalog | `0621 / 09881000` | `Zahlenantwort<Celsius10>` | 1782 | 4 |
| `P00_008_0805` | 00-08 | TEM 00-08; Bezeichnung nicht im STE-Katalog | `0621 / 0805` | `Zahlenantwort<Celsius10>` | 131 | 22 |
| `P00_008_08851000` | 00-08 | TEM 00-08; Bezeichnung nicht im STE-Katalog | `0621 / 08851000` | `Zahlenantwort<Celsius10>` | 545 | 4 |
| `P00_008_090A` | 00-08 | TEM 00-08; Bezeichnung nicht im STE-Katalog | `0621 / 090a` | `Zahlenantwort<Celsius10>` | 984 | 25 |
| `P00_008_098A1000` | 00-08 | TEM 00-08; Bezeichnung nicht im STE-Katalog | `0621 / 098a1000` | `Zahlenantwort<Celsius10>` | 1784 | 2 |
| `P00_009_AB00` | 00-09 | TEM 00-09; Bezeichnung nicht im STE-Katalog | `0621 / ab00` | `RohgrenzenAntwort<ByteMitVorzeichen>` | 1688 | 19 |
| `P00_070_0806` | 00-70 | TEM 00-70; Bezeichnung nicht im STE-Katalog | `0621 / 0806` | `Zahlenantwort<Celsius10>` | 135 | 71 |
| `P00_070_08861000` | 00-70 | TEM 00-70; Bezeichnung nicht im STE-Katalog | `0621 / 08861000` | `Zahlenantwort<Celsius10>` | 550 | 2 |
| `P00_070_090B` | 00-70 | TEM 00-70; Bezeichnung nicht im STE-Katalog | `0621 / 090b` | `Zahlenantwort<Celsius10>` | 985 | 23 |
| `P00_070_098B1000` | 00-70 | TEM 00-70; Bezeichnung nicht im STE-Katalog | `0621 / 098b1000` | `Zahlenantwort<Celsius10>` | 2529 | 1 |
| `P00_071_0807` | 00-71 | TEM 00-71; Bezeichnung nicht im STE-Katalog | `0621 / 0807` | `Zahlenantwort<Celsius10>` | 142 | 69 |
| `P00_071_08871000` | 00-71 | TEM 00-71; Bezeichnung nicht im STE-Katalog | `0621 / 08871000` | `Zahlenantwort<Celsius10>` | 551 | 1 |
| `P00_071_090C` | 00-71 | TEM 00-71; Bezeichnung nicht im STE-Katalog | `0621 / 090c` | `Zahlenantwort<Celsius10>` | 986 | 22 |
| `P00_071_098C1000` | 00-71 | TEM 00-71; Bezeichnung nicht im STE-Katalog | `0621 / 098c1000` | `Zahlenantwort<Celsius10>` | 2530 | 2 |
| `P00_072_0808` | 00-72 | TEM 00-72; Bezeichnung nicht im STE-Katalog | `0621 / 0808` | `Zahlenantwort<Celsius10>` | 156 | 57 |
| `P00_072_08881000` | 00-72 | TEM 00-72; Bezeichnung nicht im STE-Katalog | `0621 / 08881000` | `Zahlenantwort<Celsius10>` | 552 | 1 |
| `P00_072_090D` | 00-72 | TEM 00-72; Bezeichnung nicht im STE-Katalog | `0621 / 090d` | `Zahlenantwort<Celsius10>` | 1011 | 3 |
| `P00_072_098D1000` | 00-72 | TEM 00-72; Bezeichnung nicht im STE-Katalog | `0621 / 098d1000` | `Zahlenantwort<Celsius10>` | 2531 | 2 |
| `P00_073_0809` | 00-73 | TEM 00-73; Bezeichnung nicht im STE-Katalog | `0621 / 0809` | `Zahlenantwort<Celsius10>` | 182 | 7 |
| `P00_073_08891000` | 00-73 | TEM 00-73; Bezeichnung nicht im STE-Katalog | `0621 / 08891000` | `Zahlenantwort<Celsius10>` | 553 | 2 |
| `P00_073_090E` | 00-73 | TEM 00-73; Bezeichnung nicht im STE-Katalog | `0621 / 090e` | `Zahlenantwort<Celsius10>` | 2447 | 3 |
| `P00_073_098E1000` | 00-73 | TEM 00-73; Bezeichnung nicht im STE-Katalog | `0621 / 098e1000` | `Zahlenantwort<Celsius10>` | 2532 | 2 |
| `P00_074_080A` | 00-74 | TEM 00-74; Bezeichnung nicht im STE-Katalog | `0621 / 080a` | `Zahlenantwort<Celsius10>` | 187 | 6 |
| `P00_074_088A1000` | 00-74 | TEM 00-74; Bezeichnung nicht im STE-Katalog | `0621 / 088a1000` | `Zahlenantwort<Celsius10>` | 556 | 1 |
| `P00_074_090F` | 00-74 | TEM 00-74; Bezeichnung nicht im STE-Katalog | `0621 / 090f` | `Zahlenantwort<Celsius10>` | 2448 | 3 |
| `P00_075_080B` | 00-75 | TEM 00-75; Bezeichnung nicht im STE-Katalog | `0621 / 080b` | `Zahlenantwort<Celsius10>` | 191 | 6 |
| `P00_075_0910` | 00-75 | TEM 00-75; Bezeichnung nicht im STE-Katalog | `0621 / 0910` | `Zahlenantwort<Celsius10>` | 2451 | 4 |
| `P00_081_080C` | 00-81 | TEM 00-81; Bezeichnung nicht im STE-Katalog | `0621 / 080c` | `Zahlenantwort<Celsius10>` | 204 | 3 |
| `P00_081_0911` | 00-81 | TEM 00-81; Bezeichnung nicht im STE-Katalog | `0621 / 0911` | `Zahlenantwort<Celsius10>` | 2452 | 4 |
| `P00_095_080D` | 00-95 | TEM 00-95; Bezeichnung nicht im STE-Katalog | `0621 / 080d` | `RohgrenzenAntwort<UIN>` | 205 | 4 |
| `P00_095_0912` | 00-95 | TEM 00-95; Bezeichnung nicht im STE-Katalog | `0621 / 0912` | `RohgrenzenAntwort<UIN>` | 2453 | 4 |
| `P00_096_080E` | 00-96 | TEM 00-96; Bezeichnung nicht im STE-Katalog | `0621 / 080e` | `Zahlenantwort<Celsius10>` | 210 | 4 |
| `P00_096_088E1000` | 00-96 | TEM 00-96; Bezeichnung nicht im STE-Katalog | `0621 / 088e1000` | `Zahlenantwort<Celsius10>` | 4940 | 1 |
| `P00_096_0913` | 00-96 | TEM 00-96; Bezeichnung nicht im STE-Katalog | `0621 / 0913` | `Zahlenantwort<Celsius10>` | 2460 | 2 |
| `P01_001_0903` | 01-01 | TEM 01-01; Bezeichnung nicht im STE-Katalog | `0621 / 0903` | `Zahlenantwort<Celsius10>` | 950 | 8 |
| `P01_001_09831000` | 01-01 | TEM 01-01; Bezeichnung nicht im STE-Katalog | `0621 / 09831000` | `Zahlenantwort<Celsius10>` | 1776 | 2 |
| `P01_002_0905` | 01-02 | TEM 01-02; Bezeichnung nicht im STE-Katalog | `0621 / 0905` | `Zahlenantwort<Celsius10>` | 952 | 11 |
| `P01_002_09851000` | 01-02 | TEM 01-02; Bezeichnung nicht im STE-Katalog | `0621 / 09851000` | `Zahlenantwort<Celsius10>` | 1778 | 2 |
| `P01_004_0907` | 01-04 | TEM 01-04; Bezeichnung nicht im STE-Katalog | `0621 / 0907` | `Zahlenantwort<Celsius10>` | 967 | 8 |
| `P01_004_09871000` | 01-04 | TEM 01-04; Bezeichnung nicht im STE-Katalog | `0621 / 09871000` | `Zahlenantwort<Celsius10>` | 1780 | 4 |
| `P01_007_0909` | 01-07 | TEM 01-07; Bezeichnung nicht im STE-Katalog | `0621 / 0909` | `Zahlenantwort<Celsius10>` | 978 | 8 |
| `P01_007_09891000` | 01-07 | TEM 01-07; Bezeichnung nicht im STE-Katalog | `0621 / 09891000` | `Zahlenantwort<Celsius10>` | 1783 | 3 |
| `P01_009_AB01` | 01-09 | TEM 01-09; Bezeichnung nicht im STE-Katalog | `0621 / ab01` | `Zahlenantwort<Prozent10>` | 1690 | 17 |
| `P01_020_2100` | 01-20 | TEM 01-20; Bezeichnung nicht im STE-Katalog | `0621 / 2100` | `RohgrenzenAntwort<Schalter>` | 2282 | 6 |
| `P01_020_21801000` | 01-20 | TEM 01-20; Bezeichnung nicht im STE-Katalog | `0621 / 21801000` | `RohgrenzenAntwort<Schalter>` | 3347 | 6 |
| `P01_021_2101` | 01-21 | TEM 01-21; Bezeichnung nicht im STE-Katalog | `0621 / 2101` | `RohgrenzenAntwort<ByteMitVorzeichen>` | 2283 | 7 |
| `P01_022_2102` | 01-22 | TEM 01-22; Bezeichnung nicht im STE-Katalog | `0621 / 2102` | `RohgrenzenAntwort<Schalter>` | 2313 | 5 |
| `P01_040_2103` | 01-40 | TEM 01-40; Bezeichnung nicht im STE-Katalog | `0621 / 2103` | `RohgrenzenAntwort<Schalter>` | 2314 | 9 |
| `P01_053_2104` | 01-53 | TEM 01-53; Bezeichnung nicht im STE-Katalog | `0621 / 2104` | `RohgrenzenAntwort<Schalter>` | 2321 | 14 |
| `P01_054_2105` | 01-54 | TEM 01-54; Bezeichnung nicht im STE-Katalog | `0621 / 2105` | `RohgrenzenAntwort<Schalter>` | 2325 | 13 |
| `P01_063_2106` | 01-63 | TEM 01-63; Bezeichnung nicht im STE-Katalog | `0621 / 2106` | `RohgrenzenAntwort<Schalter>` | 2335 | 9 |
| `P01_096_0914` | 01-96 | TEM 01-96; Bezeichnung nicht im STE-Katalog | `0621 / 0914` | `Zahlenantwort<Celsius10>` | 2461 | 2 |
| `P01_097_0915` | 01-97 | TEM 01-97; Bezeichnung nicht im STE-Katalog | `0621 / 0915` | `RohgrenzenAntwort<ByteMitVorzeichen>` | 2462 | 2 |
| `P01_099_210F` | 01-99 | TEM 01-99; Bezeichnung nicht im STE-Katalog | `0621 / 210f` | `RohgrenzenAntwort<Schalter>` | 2368 | 2 |
| `P01_099_218F1000` | 01-99 | TEM 01-99; Bezeichnung nicht im STE-Katalog | `0621 / 218f1000` | `RohgrenzenAntwort<Schalter>` | 3348 | 6 |
| `P02_000_0105` | 02-00 | TEM 02-00; Bezeichnung nicht im STE-Katalog | `0621 / 0105` | `Sonderantwort` | 8 | 243 |
| `P02_000_01851000` | 02-00 | TEM 02-00; Bezeichnung nicht im STE-Katalog | `0621 / 01851000` | `Sonderantwort` | 516 | 33 |
| `P02_002_0104` | 02-02 | TEM 02-02; Bezeichnung nicht im STE-Katalog | `0621 / 0104` | `Sonderantwort` | 6 | 247 |
| `P02_002_01841000` | 02-02 | TEM 02-02; Bezeichnung nicht im STE-Katalog | `0621 / 01841000` | `Sonderantwort` | 515 | 35 |
| `P02_003_0103` | 02-03 | TEM 02-03; Bezeichnung nicht im STE-Katalog | `0621 / 0103` | `Sonderantwort` | 5 | 250 |
| `P02_003_01831000` | 02-03 | TEM 02-03; Bezeichnung nicht im STE-Katalog | `0621 / 01831000` | `Sonderantwort` | 514 | 36 |
| `P02_010_0106` | 02-10 | TEM 02-10; Bezeichnung nicht im STE-Katalog | `0621 / 0106` | `Sonderantwort` | 10 | 240 |
| `P02_010_01861000` | 02-10 | TEM 02-10; Bezeichnung nicht im STE-Katalog | `0621 / 01861000` | `Sonderantwort` | 517 | 32 |
| `P02_012_0109` | 02-12 | TEM 02-12; Bezeichnung nicht im STE-Katalog | `0621 / 0109` | `Kurzantwort` | 13 | 274 |
| `P02_012_01891000` | 02-12 | TEM 02-12; Bezeichnung nicht im STE-Katalog | `0621 / 01891000` | `Kurzantwort` | 522 | 52 |
| `P02_020_0901` | 02-20 | TEM 02-20; Bezeichnung nicht im STE-Katalog | `0621 / 0901` | `Zahlenantwort<Celsius10>` | 2466 | 1 |
| `P02_020_09811000` | 02-20 | TEM 02-20; Bezeichnung nicht im STE-Katalog | `0621 / 09811000` | `Zahlenantwort<Celsius10>` | 1774 | 1 |
| `P02_040_0916` | 02-40 | TEM 02-40; Bezeichnung nicht im STE-Katalog | `0621 / 0916` | `Zahlenantwort<Kilowatt10>` | 2463 | 2 |
| `P02_041_0917` | 02-41 | TEM 02-41; Bezeichnung nicht im STE-Katalog | `0621 / 0917` | `Zahlenantwort<Kilowatt10>` | 2464 | 1 |
| `P02_070_0A01` | 02-70 | TEM 02-70; Bezeichnung nicht im STE-Katalog | `0621 / 0a01` | `RohgrenzenAntwort<DAY>` | 21 | 14 |
| `P02_071_0108` | 02-71 | TEM 02-71; Bezeichnung nicht im STE-Katalog | `0621 / 0108` | `RohgrenzenAntwort<Wochenminuten>` | 12 | 288 |
| `P02_071_01881000` | 02-71 | TEM 02-71; Bezeichnung nicht im STE-Katalog | `0621 / 01881000` | `RohgrenzenAntwort<Wochenminuten>` | 520 | 63 |
| `P02_071_0A00` | 02-71 | TEM 02-71; Bezeichnung nicht im STE-Katalog | `0621 / 0a00` | `RohgrenzenAntwort<Wochenminuten>` | 20 | 15 |
| `P03_000_2300` | 03-00 | Raumschutztemperatur | `0621 / 2300` | `Zahlenantwort<Celsius10>` | 2369 | 1 |
| `P03_001_2301` | 03-01 | Fusspunkttemperatur | `0621 / 2301` | `Zahlenantwort<Celsius10>` | 2370 | 1 |
| `P03_010_0B04` | 03-10 | Steilheit Kennlinie | `0621 / 0b04` | `Zahlenantwort<Steilheit100>` | 27 | 23 |
| `P03_010_0B841000` | 03-10 | Steilheit Kennlinie | `0621 / 0b841000` | `Zahlenantwort<Steilheit100>` | 575 | 6 |
| `P03_011_A300` | 03-11 | Fusspunkt Vorlaufkennlinie: TA | `0621 / a300` | `Zahlenantwort<Celsius10>` | 811 | 4 |
| `P03_020_A301` | 03-20 | Zeitkonstante für Aussentemperaturmittelung | `0621 / a301` | `Zahlenantwort<Stunden10>` | 812 | 2 |
| `P03_021_0B06` | 03-21 | Heizgrenze bei Tagbetrieb | `0621 / 0b06` | `Zahlenantwort<Celsius10>` | 29 | 22 |
| `P03_021_0B861000` | 03-21 | Heizgrenze bei Tagbetrieb | `0621 / 0b861000` | `Zahlenantwort<Celsius10>` | 573 | 4 |
| `P03_023_A302` | 03-23 | Frostgrenze | `0621 / a302` | `Zahlenantwort<Celsius10>` | 814 | 1 |
| `P03_030_A303` | 03-30 | Nachstellzeit Raumregler | `0621 / a303` | `Zahlenantwort<Minuten10>` | 815 | 1 |
| `P03_050_0100` | 03-50 | Betriebswahl Heizung und Brauchwasser | `0621 / 0100` | `RohgrenzenAntwort<UIN>` | 2 | 262 |
| `P03_050_01801000` | 03-50 | Betriebswahl Heizung und Brauchwasser | `0621 / 01801000` | `RohgrenzenAntwort<UIN>` | 511 | 49 |
| `P03_051_0B00` | 03-51 | Sollwert Raumtemperatur Heizen Tag normal | `0621 / 0b00` | `Zahlenantwort<Celsius10>` | 22 | 16 |
| `P03_051_0B801000` | 03-51 | Sollwert Raumtemperatur Heizen Tag normal | `0621 / 0b801000` | `Zahlenantwort<Celsius10>` | 4950 | 2 |
| `P03_053_0B02` | 03-53 | Sollwert Raumteperatur Heizen Nacht | `0621 / 0b02` | `Zahlenantwort<Celsius10>` | 25 | 18 |
| `P03_053_0B821000` | 03-53 | Sollwert Raumteperatur Heizen Nacht | `0621 / 0b821000` | `Zahlenantwort<Celsius10>` | 577 | 3 |
| `P03_058_0102` | 03-58 | Behaglichkeit | `0621 / 0102` | `Zahlenantwort<Kelvin10>` | 4 | 260 |
| `P03_058_01821000` | 03-58 | Behaglichkeit | `0621 / 01821000` | `Zahlenantwort<Kelvin10>` | 513 | 42 |
| `P03_078_0F00` | 03-78 | TEM 03-78; Bezeichnung nicht im STE-Katalog | `0621 / 0f00` | `RohgrenzenAntwort<UIN>` | 809 | 10 |
| `P03_078_0F801000` | 03-78 | TEM 03-78; Bezeichnung nicht im STE-Katalog | `0621 / 0f801000` | `RohgrenzenAntwort<UIN>` | 4325 | 1 |
| `P04_000_A400` | 04-00 | Fühlerkonfiguration speichern | `0621 / a400` | `RohgrenzenAntwort<Schalter>` | 817 | 2 |
| `P04_002_A401` | 04-02 | Funktion Sollwerteingang | `0621 / a401` | `RohgrenzenAntwort<UIN>` | 819 | 1 |
| `P04_008_A402` | 04-08 | Handbetrieb Konfiguration | `0621 / a402` | `RohgrenzenAntwort<UIN>` | 820 | 1 |
| `P04_020_A403` | 04-20 | Anlage-Hauptregler / Folgeregler | `0621 / a403` | `RohgrenzenAntwort<UIN>` | 821 | 1 |
| `P04_022_AB02` | 04-22 | WE 1 Zieladresse | `0621 / ab02` | `RohgrenzenAntwort<UIN>` | 1697 | 3 |
| `P04_027_A900` | 04-27 | eBUS Adresse WEZ | `0621 / a900` | `RohgrenzenAntwort<UIN>` | 3493 | 1 |
| `P04_027_AA00` | 04-27 | eBUS Adresse WEZ | `0621 / aa00` | `RohgrenzenAntwort<UIN>` | 1665 | 4 |
| `P04_030_A404` | 04-30 | Multifunktionsusgang 1 | `0621 / a404` | `RohgrenzenAntwort<Schalter>` | 822 | 1 |
| `P04_031_A405` | 04-31 | Multifunktionsusgang 2 | `0621 / a405` | `RohgrenzenAntwort<Schalter>` | 823 | 1 |
| `P04_036_A406` | 04-36 | eBUS Speisung Abschaltung | `0621 / a406` | `RohgrenzenAntwort<Schalter>` | 824 | 1 |
| `P04_040_A407` | 04-40 | Service Passwort | `0621 / a407` | `RohgrenzenAntwort<UIN>` | 825 | 1 |
| `P04_043_0001` | 04-43 | TEM 04-43; Bezeichnung nicht im STE-Katalog | `0621 / 0001` | `RohgrenzenAntwort<UIN>` | 810 | 14 |
| `P05_000_A500` | 05-00 | Schaltdifferenz Brauchwasserbereitung | `0621 / a500` | `Zahlenantwort<Kelvin10>` | 827 | 4 |
| `P05_001_A501` | 05-01 | Temperaturüberhoehung Brauchwasserbereitung | `0621 / a501` | `Zahlenantwort<Kelvin10>` | 828 | 2 |
| `P05_002_A502` | 05-02 | Brauchwasser-Vorrang | `0621 / a502` | `Zahlenantwort<Stunden10>` | 829 | 2 |
| `P05_003_A503` | 05-03 | Nachlaufzeit Brauchwasserbereitung | `0621 / a503` | `Zahlenantwort<Minuten10>` | 830 | 2 |
| `P05_004_A504` | 05-04 | Legionellenschutztemperatur | `0621 / a504` | `Zahlenantwort<Celsius10>` | 831 | 2 |
| `P05_005_A505` | 05-05 | Funktionsweise Ladepumpennachlauf | `0621 / a505` | `RohgrenzenAntwort<UIN>` | 832 | 3 |
| `P05_006_A506` | 05-06 | Zirkulationspumpe aktiv | `0621 / a506` | `RohgrenzenAntwort<Schalter>` | 833 | 2 |
| `P05_007_A507` | 05-07 | Stellglied Brauchwasserbereitung | `0621 / a507` | `RohgrenzenAntwort<Schalter>` | 835 | 2 |
| `P05_013_A508` | 05-13 | Reduktion Sollwert TBO | `0621 / a508` | `Zahlenantwort<Kelvin10>` | 836 | 2 |
| `P05_040_A509` | 05-40 | Min. Fehlerdauer fuer Brauchwasser Störmeldung | `0621 / a509` | `Zahlenantwort<Stunden10>` | 837 | 2 |
| `P05_051_0B03` | 05-51 | Sollwert Warmwassertemperatur | `0621 / 0b03` | `Zahlenantwort<Celsius10>` | 26 | 27 |
| `P05_051_0B831000` | 05-51 | Sollwert Warmwassertemperatur | `0621 / 0b831000` | `Zahlenantwort<Celsius10>` | 576 | 4 |
| `P06_000_A600` | 06-00 | Brauchwasser Ladeleistung | `0621 / a600` | `Zahlenantwort<Kilowatt10>` | 841 | 3 |
| `P06_001_A601` | 06-01 | Puffer, Heiz-  Ladeleistung | `0621 / a601` | `Zahlenantwort<Kilowatt10>` | 842 | 2 |
| `P06_002_A602` | 06-02 | Kühlleistung | `0621 / a602` | `Zahlenantwort<Kilowatt10>` | 843 | 2 |
| `P06_004_A603` | 06-04 | WEZ Überhöhung | `0621 / a603` | `Zahlenantwort<Kelvin10>` | 844 | 2 |
| `P06_005_A604` | 06-05 | Puffer Offset TPM aus | `0621 / a604` | `Zahlenantwort<Kelvin10>` | 845 | 2 |
| `P06_008_A605` | 06-08 | TBVsoll Überhöhung | `0621 / a605` | `Zahlenantwort<Kelvin10>` | 846 | 2 |
| `P06_010_A606` | 06-10 | Xp WEZ Manager | `0621 / a606` | `Zahlenantwort<Kelvin10>` | 847 | 2 |
| `P06_011_A607` | 06-11 | Tn WEZ Manager | `0621 / a607` | `Zahlenantwort<Minuten10>` | 848 | 2 |
| `P06_012_A608` | 06-12 | Tv WEZ Manager | `0621 / a608` | `Zahlenantwort<Minuten10>` | 849 | 2 |
| `P06_013_A609` | 06-13 | Reduktion Sollwert TKX | `0621 / a609` | `Zahlenantwort<Kelvin10>` | 850 | 2 |
| `P06_020_A60A` | 06-20 | Sequenzwechsel Flag | `0621 / a60a` | `RohgrenzenAntwort<UIN>` | 851 | 2 |
| `P07_000_A700` | 07-00 | Proportional-Bereich Mischer | `0621 / a700` | `Zahlenantwort<Kelvin10>` | 864 | 6 |
| `P07_000_A7801000` | 07-00 | Proportional-Bereich Mischer | `0621 / a7801000` | `Zahlenantwort<Kelvin10>` | 4328 | 2 |
| `P07_001_A701` | 07-01 | Überhöhung WE-Temperatur | `0621 / a701` | `Zahlenantwort<Kelvin10>` | 865 | 4 |
| `P07_001_A7811000` | 07-01 | Überhöhung WE-Temperatur | `0621 / a7811000` | `Zahlenantwort<Kelvin10>` | 4329 | 2 |
| `P07_002_A702` | 07-02 | Minimale Vorlauftemperatur | `0621 / a702` | `Zahlenantwort<Celsius10>` | 866 | 4 |
| `P07_002_A7821000` | 07-02 | Minimale Vorlauftemperatur | `0621 / a7821000` | `Zahlenantwort<Celsius10>` | 4330 | 2 |
| `P07_003_A703` | 07-03 | Pumpennachlauf Heizkreis | `0621 / a703` | `Zahlenantwort<Minuten10>` | 867 | 6 |
| `P07_003_A7831000` | 07-03 | Pumpennachlauf Heizkreis | `0621 / a7831000` | `Zahlenantwort<Minuten10>` | 4331 | 5 |
| `P07_005_A704` | 07-05 | Heizkreistyp | `0621 / a704` | `RohgrenzenAntwort<UIN>` | 868 | 7 |
| `P07_005_A7841000` | 07-05 | Heizkreistyp | `0621 / a7841000` | `RohgrenzenAntwort<UIN>` | 4332 | 7 |
| `P07_006_A705` | 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung | `0621 / a705` | `Zahlenantwort<Stunden10>` | 869 | 5 |
| `P07_006_A7851000` | 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung | `0621 / a7851000` | `Zahlenantwort<Stunden10>` | 4333 | 5 |
| `P07_008_0B05` | 07-08 | Vorlauf Maximaltemperatur TV | `0621 / 0b05` | `Zahlenantwort<Celsius10>` | 28 | 15 |
| `P07_008_0B851000` | 07-08 | Vorlauf Maximaltemperatur TV | `0621 / 0b851000` | `Zahlenantwort<Celsius10>` | 574 | 4 |
| `P07_014_A706` | 07-14 | Heizkreisfunktion im Kühlbetrieb | `0621 / a706` | `RohgrenzenAntwort<UIN>` | 870 | 5 |
| `P07_014_A7861000` | 07-14 | Heizkreisfunktion im Kühlbetrieb | `0621 / a7861000` | `RohgrenzenAntwort<UIN>` | 4344 | 4 |
| `P07_031_A707` | 07-31 | Heizkreisüberhöhung Niedertarif | `0621 / a707` | `Zahlenantwort<Kelvin10>` | 871 | 3 |
| `P07_031_A7871000` | 07-31 | Heizkreisüberhöhung Niedertarif | `0621 / a7871000` | `Zahlenantwort<Kelvin10>` | 4345 | 1 |
| `P09_000_A901` | 09-00 | Nachlaufzeit Schutzfunktion | `0621 / a901` | `Zahlenantwort<Minuten10>` | 3494 | 1 |
| `P09_000_AA01` | 09-00 | Nachlaufzeit Schutzfunktion | `0621 / aa01` | `Zahlenantwort<Minuten10>` | 1666 | 2 |
| `P09_004_A902` | 09-04 | Vorlaufzeit Quellenpumpe | `0621 / a902` | `Zahlenantwort<Minuten10>` | 3495 | 2 |
| `P09_004_AA02` | 09-04 | Einschaltverzögerung | `0621 / aa02` | `Zahlenantwort<Minuten10>` | 1667 | 2 |
| `P09_007_A903` | 09-07 | WEZ Typ | `0621 / a903` | `RohgrenzenAntwort<UIN>` | 3496 | 3 |
| `P09_007_AA03` | 09-07 | WEZ Typ | `0621 / aa03` | `RohgrenzenAntwort<UIN>` | 1668 | 3 |
| `P09_011_A904` | 09-11 | Bedingte WEZ Freigabe | `0621 / a904` | `RohgrenzenAntwort<UIN>` | 3498 | 2 |
| `P09_011_AA04` | 09-11 | Bedingte WEZ Freigabe | `0621 / aa04` | `RohgrenzenAntwort<UIN>` | 1669 | 4 |
| `P09_012_A905` | 09-12 | Aussentemperatursperre TAW | `0621 / a905` | `Zahlenantwort<Celsius10>` | 3499 | 2 |
| `P09_012_AA05` | 09-12 | Aussentemperatursperre TAW | `0621 / aa05` | `Zahlenantwort<Celsius10>` | 1670 | 3 |
| `P09_013_A906` | 09-13 | Energiezwang Funktion | `0621 / a906` | `RohgrenzenAntwort<UIN>` | 3500 | 2 |
| `P09_013_AA06` | 09-13 | Energiezwang Funktion | `0621 / aa06` | `RohgrenzenAntwort<UIN>` | 1671 | 3 |
| `P09_014_A907` | 09-14 | Diff. Leistungszwang Tkmax | `0621 / a907` | `Zahlenantwort<Kelvin10>` | 3501 | 2 |
| `P09_014_AA07` | 09-14 | Diff. Leistungszwang Tkmax | `0621 / aa07` | `Zahlenantwort<Kelvin10>` | 1672 | 3 |
| `P09_021_A908` | 09-21 | WE Abschaltdifferenz | `0621 / a908` | `Zahlenantwort<Kelvin10>` | 3510 | 1 |
| `P09_021_AA08` | 09-21 | WE Abschaltdifferenz | `0621 / aa08` | `Zahlenantwort<Kelvin10>` | 1673 | 3 |
| `P09_023_A909` | 09-23 | Minimale Stillstandszeit | `0621 / a909` | `Zahlenantwort<Minuten10>` | 3511 | 2 |
| `P09_023_AA09` | 09-23 | Minimale Stillstandszeit | `0621 / aa09` | `Zahlenantwort<Minuten10>` | 1681 | 2 |
| `P09_026_A90A` | 09-26 | Vorhaltezeit 2. Stufe | `0621 / a90a` | `Zahlenantwort<Sekunden10>` | 3512 | 4 |
| `P09_026_AA0A` | 09-26 | Vorhaltezeit 2. Stufe | `0621 / aa0a` | `Zahlenantwort<Sekunden10>` | 1682 | 2 |
| `P09_031_A90B` | 09-31 | Minimale WE Laufzeit | `0621 / a90b` | `Zahlenantwort<Minuten10>` | 3513 | 1 |
| `P09_031_AA0B` | 09-31 | Minimale WE Laufzeit | `0621 / aa0b` | `Zahlenantwort<Minuten10>` | 1683 | 2 |
| `P09_034_A90C` | 09-34 | Einschaltverzögerung 2. Stufe | `0621 / a90c` | `Zahlenantwort<Minuten10>` | 3515 | 3 |
| `P09_034_AA0C` | 09-34 | Einschaltverzögerung 2. Stufe | `0621 / aa0c` | `Zahlenantwort<Minuten10>` | 1684 | 2 |
| `P09_035_A90D` | 09-35 | Schaltdifferenz 2. Stufe | `0621 / a90d` | `Zahlenantwort<Kelvin10>` | 3516 | 4 |
| `P09_035_AA0D` | 09-35 | Schaltdifferenz 2. Stufe | `0621 / aa0d` | `Zahlenantwort<Kelvin10>` | 1685 | 2 |
| `P10_031_A90E` | 10-31 | WE Maximaltemperatur | `0621 / a90e` | `Zahlenantwort<Celsius10>` | 3524 | 1 |
| `P10_031_AA0E` | 10-31 | WE Maximaltemperatur | `0621 / aa0e` | `Zahlenantwort<Celsius10>` | 1686 | 2 |
| `P11_001_AB03` | 11-01 | WE Steuerbefehl | `0621 / ab03` | `RohgrenzenAntwort<UIN>` | 1698 | 2 |
| `P11_002_AB04` | 11-02 | WE Nennleistung | `0621 / ab04` | `Zahlenantwort<Kilowatt10>` | 1699 | 2 |
| `P11_003_AB05` | 11-03 | minimale WE-Leistung | `0621 / ab05` | `RohgrenzenAntwort<UIN>` | 1700 | 3 |
| `P11_004_AB06` | 11-04 | Einschaltleistung Folge WE | `0621 / ab06` | `RohgrenzenAntwort<UIN>` | 1701 | 2 |
| `P11_005_AB07` | 11-05 | WE Folgewechsel | `0621 / ab07` | `RohgrenzenAntwort<Schalter>` | 1702 | 3 |
| `P15_010_A90F` | 15-10 | Heissgas Maximaltemperatur | `0621 / a90f` | `Zahlenantwort<Celsius10>` | 3526 | 1 |
| `P15_011_A910` | 15-11 | TWVmax Abschalthysterese | `0621 / a910` | `Zahlenantwort<Kelvin10>` | 3527 | 1 |
| `P15_023_A50A` | 15-23 | Frostschutztemperatur TVD | `0621 / a50a` | `Zahlenantwort<Celsius10>` | 838 | 2 |
| `Liste_01890000` | — | Listenblock roh; keine Schreiboperation | `0622 / 01890000` | `Roh10` | 14 | 271 |
| `Liste_01890100` | — | Listenblock roh; keine Schreiboperation | `0622 / 01890100` | `Roh2` | 15 | 270 |
| `Liste_01891000` | — | Listenblock roh; keine Schreiboperation | `0622 / 01891000` | `Roh10` | 523 | 49 |
| `Liste_01891100` | — | Listenblock roh; keine Schreiboperation | `0622 / 01891100` | `Roh2` | 524 | 47 |
| `Menueblock_00` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 00` | `Roh8` | 1 | 7 |
| `Menueblock_01` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 01` | `Roh8` | 17 | 7 |
| `Menueblock_02` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 02` | `Roh8` | 18 | 7 |
| `Menueblock_03` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 03` | `Roh8` | 19 | 7 |
| `Menueblock_04` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 04` | `Roh8` | 30 | 7 |
| `Menueblock_05` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 05` | `Roh8` | 31 | 7 |
| `Menueblock_06` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 06` | `Roh8` | 32 | 7 |
| `Menueblock_07` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 07` | `Roh8` | 33 | 7 |
| `Menueblock_08` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 08` | `Roh8` | 34 | 7 |
| `Menueblock_09` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 09` | `Roh8` | 35 | 7 |
| `Menueblock_0A` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 0a` | `Roh8` | 36 | 7 |
| `Menueblock_0B` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 0b` | `Roh8` | 37 | 7 |
| `Menueblock_0C` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 0c` | `Roh8` | 38 | 7 |
| `Menueblock_0D` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 0d` | `Roh8` | 39 | 7 |
| `Menueblock_0E` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 0e` | `Roh8` | 40 | 7 |
| `Menueblock_0F` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 0f` | `Roh8` | 41 | 7 |
| `Menueblock_10` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 10` | `Roh8` | 42 | 7 |
| `Menueblock_11` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 11` | `Roh8` | 43 | 7 |
| `Menueblock_12` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 12` | `Roh8` | 44 | 7 |
| `Menueblock_13` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 13` | `Roh8` | 45 | 7 |
| `Menueblock_14` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 14` | `Roh8` | 46 | 7 |
| `Menueblock_15` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 15` | `Roh8` | 47 | 7 |
| `Menueblock_16` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 16` | `Roh8` | 48 | 7 |
| `Menueblock_17` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 17` | `Roh8` | 49 | 7 |
| `Menueblock_18` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 18` | `Roh8` | 50 | 7 |
| `Menueblock_19` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 19` | `Roh8` | 51 | 7 |
| `Menueblock_1A` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 1a` | `Roh8` | 52 | 7 |
| `Menueblock_1B` | — | 8 Byte Menue-/Strukturmetadaten roh | `0620 / 1b` | `Roh8` | 54 | 7 |
| `NichtVorhanden_0107` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 0107` | `Roh10` | 11 | 21 |
| `NichtVorhanden_010A` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 010a` | `Roh10` | 16 | 21 |
| `NichtVorhanden_01811000` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 01811000` | `Roh10` | 512 | 15 |
| `NichtVorhanden_01871000` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 01871000` | `Roh10` | 519 | 14 |
| `NichtVorhanden_018A1000` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 018a1000` | `Roh10` | 525 | 14 |
| `NichtVorhanden_0B01` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 0b01` | `Roh10` | 23 | 16 |
| `NichtVorhanden_0B811000` | — | FF1F: in dieser Sitzung nicht vorhanden | `0621 / 0b811000` | `Roh10` | 4951 | 1 |

## STE-Kennungen ohne beobachtete Antwort

`03-02`, `03-06`, `03-07`, `03-08`, `03-35`, `03-43`, `03-60`, `04-45`, `04-60`, `04-61`, `04-62`, `04-63`, `04-64`, `05-14`, `05-60`, `08-55`, `08-58`, `08-59`, `08-72`, `08-79`, `09-08`, `09-20`, `09-32`, `15-12`, `15-13`, `15-21`, `15-22`, `15-24`, `15-25`, `15-26`, `15-27`, `15-28`, `15-40`, `15-41`, `15-42`, `15-43`, `15-44`, `15-45`, `15-46`, `15-47`, `15-48`, `15-49`, `15-50`, `15-60`

Diese Kennungen erhalten keine geratenen Anfragen. Das Fehlen in diesem Mitschnitt belegt nicht, dass der Regler sie nicht unterstützt.
