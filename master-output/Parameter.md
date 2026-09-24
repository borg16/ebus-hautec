# Bevorzugte Zugriffe aus commands.txt und input/complete.log

Generiert durch `scripts/analyze_master_log.py`. Die Namen entsprechen [controller.tsp](../controller.tsp), Circuit `15`.

TEM-Kennungen und Zugriffe stammen aus dem Scan oder den CRC-geprüften Logantworten. Identische untere Menüs 63..72 werden zugunsten ihrer Gegenstücke a3..b2 weggelassen. Namen stammen vorrangig aus input/Checkliste_Regler_Programmierung.CSV und input/soll_und_istwerte.md, ersatzweise aus dem STE-Katalog. Pro TEM-Kennung und Kontext bleibt ein bevorzugter Selektor. Neue Namen und entfallene Aliase stehen in [Umbenennung.md](Umbenennung.md). Neue reine Scan-Zugriffe erhalten keine abgeleiteten Schreibmodelle.

Der Suffix im Modellnamen ist die vollständige Anfrage in Hex. Verschiedene Zugriffe auf dieselbe TEM-Kennung bleiben getrennt. Die zusätzliche Instanz mit `10 00` wird nicht ohne Nachweis als HK 2 bezeichnet.

| Modell | TEM | Bezeichnung | Service / Anfrage | Antworttyp | Beleg | Namensquelle |
|---|---|---|---|---|---|---|
| `P00_00_HK1` | 00-00 | Aussentemperatur (Ist; TA) | `0621 / 0800` | `Zahlenantwort<Celsius10>` | commands.txt:41; input/complete.log:1355 | soll_und_istwerte.md |
| `P00_00_HK2` | 00-00 | Aussentemperatur (Ist; TA) | `0621 / 08801000` | `Zahlenantwort<Celsius10>` | commands.txt:56; input/complete.log:2003 | soll_und_istwerte.md |
| `P00_01_HK1` | 00-01 | Raumtemperatur 1 (Ist; TI1) / Raumtemperatur 2 (Ist; TI2) | `0621 / 0801` | `Zahlenantwort<Celsius10>` | commands.txt:42; input/complete.log:1356 | soll_und_istwerte.md |
| `P00_01_HK2` | 00-01 | Raumtemperatur 1 (Ist; TI1) / Raumtemperatur 2 (Ist; TI2) | `0621 / 08811000` | `Zahlenantwort<Celsius10>` | commands.txt:57; input/complete.log:2007 | soll_und_istwerte.md |
| `P00_02_HK1` | 00-02 | Vorlauftemperatur1 (Ist; THV1) / Vorlauftemperatur2 (Ist; THV2) | `0621 / 0802` | `Zahlenantwort<Celsius10>` | commands.txt:43; input/complete.log:1360 | soll_und_istwerte.md |
| `P00_02_HK2` | 00-02 | Vorlauftemperatur1 (Ist; THV1) / Vorlauftemperatur2 (Ist; THV2) | `0621 / 08821000` | `Zahlenantwort<Celsius10>` | commands.txt:58; input/complete.log:2008 | soll_und_istwerte.md |
| `P00_04_HK1` | 00-04 | Warmwassertemperatur (Ist; TBO) | `0621 / 0803` | `Zahlenantwort<Celsius10>` | commands.txt:44; input/complete.log:1366 | soll_und_istwerte.md |
| `P00_04_HK2` | 00-04 | Warmwassertemperatur (Ist; TBO) | `0621 / 08831000` | `Zahlenantwort<Celsius10>` | commands.txt:59; input/complete.log:2009 | soll_und_istwerte.md |
| `P00_07_HK1` | 00-07 | WP-Vorlauftemperatur (Ist; TWV) / EH-Vorlauftemperatur (Ist; TEV) | `0621 / 0804` | `Zahlenantwort<Celsius10>` | commands.txt:45; input/complete.log:1376 | soll_und_istwerte.md |
| `P00_07_HK2` | 00-07 | WP-Vorlauftemperatur (Ist; TWV) / EH-Vorlauftemperatur (Ist; TEV) | `0621 / 08841000` | `Zahlenantwort<Celsius10>` | commands.txt:60; input/complete.log:2013 | soll_und_istwerte.md |
| `P00_08_HK1` | 00-08 | WP-Rücklauftemperatur (Ist; TWR) | `0621 / 0805` | `Zahlenantwort<Celsius10>` | commands.txt:46; input/complete.log:1391 | soll_und_istwerte.md |
| `P00_08_HK2` | 00-08 | WP-Rücklauftemperatur (Ist; TWR) | `0621 / 08851000` | `Zahlenantwort<Celsius10>` | commands.txt:61; input/complete.log:2016 | soll_und_istwerte.md |
| `P00_09_WE1` | 00-09 | Wärmeleistung WE 1 (Ist; PWE1) | `0621 / ab00` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:441; input/complete.log:4353 | soll_und_istwerte.md |
| `P00_09_WE2` | 00-09 | Wärmeleistung WE 2 (Ist; PWE2) | `0621 / ac00` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:449 | soll_und_istwerte.md |
| `P00_09_WE3` | 00-09 | Wärmeleistung WE 3 (Ist; PWE3) | `0621 / ad00` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:457 | soll_und_istwerte.md |
| `P00_09_WE4` | 00-09 | TEM 00-09; Bezeichnung nicht im STE-Katalog | `0621 / ae00` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:465 | unbekannt |
| `P00_09_WE5` | 00-09 | TEM 00-09; Bezeichnung nicht im STE-Katalog | `0621 / af00` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:473 | unbekannt |
| `P00_09_WE6` | 00-09 | TEM 00-09; Bezeichnung nicht im STE-Katalog | `0621 / b000` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:481 | unbekannt |
| `P00_09_WE7` | 00-09 | TEM 00-09; Bezeichnung nicht im STE-Katalog | `0621 / b100` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:489 | unbekannt |
| `P00_09_WE8` | 00-09 | TEM 00-09; Bezeichnung nicht im STE-Katalog | `0621 / b200` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:497 | unbekannt |
| `P00_70_HK1` | 00-70 | Wärmequelle-Austrittstemperatur (Ist; TWA) | `0621 / 0806` | `Zahlenantwort<Celsius10>` | commands.txt:47; input/complete.log:1397 | soll_und_istwerte.md |
| `P00_70_HK2` | 00-70 | Wärmequelle-Austrittstemperatur (Ist; TWA) | `0621 / 08861000` | `Zahlenantwort<Celsius10>` | commands.txt:62; input/complete.log:2023 | soll_und_istwerte.md |
| `P00_71_HK1` | 00-71 | Wärmequelle-Eintrittstemperatur (Ist; TWE) | `0621 / 0807` | `Zahlenantwort<Celsius10>` | commands.txt:48; input/complete.log:1407 | soll_und_istwerte.md |
| `P00_71_HK2` | 00-71 | Wärmequelle-Eintrittstemperatur (Ist; TWE) | `0621 / 08871000` | `Zahlenantwort<Celsius10>` | commands.txt:63; input/complete.log:2024 | soll_und_istwerte.md |
| `P00_72_HK1` | 00-72 | Heissgastemperatur (Ist; THG) | `0621 / 0808` | `Zahlenantwort<Celsius10>` | commands.txt:49; input/complete.log:1425 | soll_und_istwerte.md |
| `P00_72_HK2` | 00-72 | Heissgastemperatur (Ist; THG) | `0621 / 08881000` | `Zahlenantwort<Celsius10>` | commands.txt:64; input/complete.log:2027 | soll_und_istwerte.md |
| `P00_73_HK1` | 00-73 | Kondensatortemperatur (Ist; TKA) | `0621 / 0809` | `Zahlenantwort<Celsius10>` | commands.txt:50; input/complete.log:1460 | soll_und_istwerte.md |
| `P00_73_HK2` | 00-73 | Kondensatortemperatur (Ist; TKA) | `0621 / 08891000` | `Zahlenantwort<Celsius10>` | commands.txt:65; input/complete.log:2028 | soll_und_istwerte.md |
| `P00_74_HK1` | 00-74 | Verdampfertemperatur (Ist; TVD) | `0621 / 080a` | `Zahlenantwort<Celsius10>` | commands.txt:51; input/complete.log:1466 | soll_und_istwerte.md |
| `P00_74_HK2` | 00-74 | Verdampfertemperatur (Ist; TVD) | `0621 / 088a1000` | `Zahlenantwort<Celsius10>` | commands.txt:66; input/complete.log:2032 | soll_und_istwerte.md |
| `P00_75_HK1` | 00-75 | Sauggastemperatur (Ist; TSG) | `0621 / 080b` | `Zahlenantwort<Celsius10>` | commands.txt:52; input/complete.log:1472 | soll_und_istwerte.md |
| `P00_75_HK2` | 00-75 | Sauggastemperatur (Ist; TSG) | `0621 / 088b1000` | `Zahlenantwort<Celsius10>` | commands.txt:67 | soll_und_istwerte.md |
| `P00_81_HK1` | 00-81 | Warmwasser WP Verdampfertemperatur (Ist; WW-TVD) | `0621 / 080c` | `Zahlenantwort<Celsius10>` | commands.txt:53; input/complete.log:1494 | soll_und_istwerte.md |
| `P00_81_HK2` | 00-81 | Warmwasser WP Verdampfertemperatur (Ist; WW-TVD) | `0621 / 088c1000` | `Zahlenantwort<Celsius10>` | commands.txt:68 | soll_und_istwerte.md |
| `P00_95_HK1` | 00-95 | Externer Sollwert 0-10V (Ist; SWin) | `0621 / 080d` | `RohgrenzenAntwort<UIN>` | commands.txt:54; input/complete.log:1496 | soll_und_istwerte.md |
| `P00_95_HK2` | 00-95 | Externer Sollwert 0-10V (Ist; SWin) | `0621 / 088d1000` | `RohgrenzenAntwort<UIN>` | commands.txt:69 | soll_und_istwerte.md |
| `P00_96_HK1` | 00-96 | Anlage Vorlaufsollwert (Ist; TKx/TWR) | `0621 / 080e` | `Zahlenantwort<Celsius10>` | commands.txt:55; input/complete.log:1503 | soll_und_istwerte.md |
| `P00_96_HK2` | 00-96 | Anlage Vorlaufsollwert (Ist; TKx/TWR) | `0621 / 088e1000` | `Zahlenantwort<Celsius10>` | commands.txt:70; input/complete.log:10281 | soll_und_istwerte.md |
| `P01_01_HK1` | 01-01 | Raumtemperatur 1 (Soll; TI1) / Raumtemperatur 2 (Soll; TI2) | `0621 / 0903` | `Zahlenantwort<Celsius10>` | commands.txt:74; input/complete.log:2934 | soll_und_istwerte.md |
| `P01_01_HK2` | 01-01 | Raumtemperatur 1 (Soll; TI1) / Raumtemperatur 2 (Soll; TI2) | `0621 / 09831000` | `Zahlenantwort<Celsius10>` | commands.txt:98; input/complete.log:4522 | soll_und_istwerte.md |
| `P01_02_HK1` | 01-02 | Vorlauftemperatur1 (Soll; THV1) / Vorlauftemperatur2 (Soll; THV2) | `0621 / 0905` | `Zahlenantwort<Celsius10>` | commands.txt:76; input/complete.log:2939 | soll_und_istwerte.md |
| `P01_02_HK2` | 01-02 | Vorlauftemperatur1 (Soll; THV1) / Vorlauftemperatur2 (Soll; THV2) | `0621 / 09851000` | `Zahlenantwort<Celsius10>` | commands.txt:100; input/complete.log:4526 | soll_und_istwerte.md |
| `P01_04_HK1` | 01-04 | Warmwassertemperatur (Soll; TBO) | `0621 / 0907` | `Zahlenantwort<Celsius10>` | commands.txt:78; input/complete.log:2979 | soll_und_istwerte.md |
| `P01_04_HK2` | 01-04 | Warmwassertemperatur (Soll; TBO) | `0621 / 09871000` | `Zahlenantwort<Celsius10>` | commands.txt:102; input/complete.log:4528 | soll_und_istwerte.md |
| `P01_07_HK1` | 01-07 | WP-Vorlauftemperatur (Soll; TWV) / EH-Vorlauftemperatur (Soll; TEV) | `0621 / 0909` | `Zahlenantwort<Celsius10>` | commands.txt:80; input/complete.log:3007 | soll_und_istwerte.md |
| `P01_07_HK2` | 01-07 | WP-Vorlauftemperatur (Soll; TWV) / EH-Vorlauftemperatur (Soll; TEV) | `0621 / 09891000` | `Zahlenantwort<Celsius10>` | commands.txt:104; input/complete.log:4532 | soll_und_istwerte.md |
| `P01_09_WE1` | 01-09 | Wärmeleistungsanforderung WE 1 (Soll; PSollWE1) | `0621 / ab01` | `Zahlenantwort<Prozent10>` | commands.txt:442; input/complete.log:4356 | soll_und_istwerte.md |
| `P01_09_WE2` | 01-09 | Wärmeleistungsanforderung WE 2 (Soll; PSollWE2) | `0621 / ac01` | `Zahlenantwort<Prozent10>` | commands.txt:450 | soll_und_istwerte.md |
| `P01_09_WE3` | 01-09 | Wärmeleistungsanforderung WE 3 (Soll; PSollWE3) | `0621 / ad01` | `Zahlenantwort<Prozent10>` | commands.txt:458 | soll_und_istwerte.md |
| `P01_09_WE4` | 01-09 | Wärmeleistungsanforderung WE 4 (Soll; PSollWE4) | `0621 / ae01` | `Zahlenantwort<Prozent10>` | commands.txt:466 | soll_und_istwerte.md |
| `P01_09_WE5` | 01-09 | Wärmeleistungsanforderung WE 5 (Soll; PSollWE5) | `0621 / af01` | `Zahlenantwort<Prozent10>` | commands.txt:474 | soll_und_istwerte.md |
| `P01_09_WE6` | 01-09 | Wärmeleistungsanforderung WE 6 (Soll; PSollWE6) | `0621 / b001` | `Zahlenantwort<Prozent10>` | commands.txt:482 | soll_und_istwerte.md |
| `P01_09_WE7` | 01-09 | Wärmeleistungsanforderung WE 7 (Soll; PSollWE7) | `0621 / b101` | `Zahlenantwort<Prozent10>` | commands.txt:490 | soll_und_istwerte.md |
| `P01_09_WE8` | 01-09 | Wärmeleistungsanforderung WE 8 (Soll; PSollWE8) | `0621 / b201` | `Zahlenantwort<Prozent10>` | commands.txt:498 | soll_und_istwerte.md |
| `P01_20_HK1` | 01-20 | TEM 01-20; Bezeichnung nicht im STE-Katalog | `0621 / 2100` | `RohgrenzenAntwort<Schalter>` | commands.txt:144; input/complete.log:5453 | unbekannt |
| `P01_20_HK2` | 01-20 | TEM 01-20; Bezeichnung nicht im STE-Katalog | `0621 / 21801000` | `RohgrenzenAntwort<Schalter>` | commands.txt:160; input/complete.log:7267 | unbekannt |
| `P01_21_HK1` | 01-21 | TEM 01-21; Bezeichnung nicht im STE-Katalog | `0621 / 2101` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:145; input/complete.log:5454 | unbekannt |
| `P01_21_HK2` | 01-21 | TEM 01-21; Bezeichnung nicht im STE-Katalog | `0621 / 21811000` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:161 | unbekannt |
| `P01_22_HK1` | 01-22 | TEM 01-22; Bezeichnung nicht im STE-Katalog | `0621 / 2102` | `RohgrenzenAntwort<Schalter>` | commands.txt:146; input/complete.log:5498 | unbekannt |
| `P01_22_HK2` | 01-22 | TEM 01-22; Bezeichnung nicht im STE-Katalog | `0621 / 21821000` | `RohgrenzenAntwort<Schalter>` | commands.txt:162 | unbekannt |
| `P01_40_HK1` | 01-40 | TEM 01-40; Bezeichnung nicht im STE-Katalog | `0621 / 2103` | `RohgrenzenAntwort<Schalter>` | commands.txt:147; input/complete.log:5499 | unbekannt |
| `P01_40_HK2` | 01-40 | TEM 01-40; Bezeichnung nicht im STE-Katalog | `0621 / 21831000` | `RohgrenzenAntwort<Schalter>` | commands.txt:163 | unbekannt |
| `P01_53_HK1` | 01-53 | TEM 01-53; Bezeichnung nicht im STE-Katalog | `0621 / 2104` | `RohgrenzenAntwort<Schalter>` | commands.txt:148; input/complete.log:5513 | unbekannt |
| `P01_53_HK2` | 01-53 | TEM 01-53; Bezeichnung nicht im STE-Katalog | `0621 / 21841000` | `RohgrenzenAntwort<Schalter>` | commands.txt:164 | unbekannt |
| `P01_54_HK1` | 01-54 | TEM 01-54; Bezeichnung nicht im STE-Katalog | `0621 / 2105` | `RohgrenzenAntwort<Schalter>` | commands.txt:149; input/complete.log:5527 | unbekannt |
| `P01_54_HK2` | 01-54 | TEM 01-54; Bezeichnung nicht im STE-Katalog | `0621 / 21851000` | `RohgrenzenAntwort<Schalter>` | commands.txt:165 | unbekannt |
| `P01_63_HK1` | 01-63 | TEM 01-63; Bezeichnung nicht im STE-Katalog | `0621 / 2106` | `RohgrenzenAntwort<Schalter>` | commands.txt:150; input/complete.log:5539 | unbekannt |
| `P01_63_HK2` | 01-63 | TEM 01-63; Bezeichnung nicht im STE-Katalog | `0621 / 21861000` | `RohgrenzenAntwort<Schalter>` | commands.txt:166 | unbekannt |
| `P01_64_HK1` | 01-64 | TEM 01-64; Bezeichnung nicht im STE-Katalog | `0621 / 2107` | `RohgrenzenAntwort<Schalter>` | commands.txt:151 | unbekannt |
| `P01_64_HK2` | 01-64 | TEM 01-64; Bezeichnung nicht im STE-Katalog | `0621 / 21871000` | `RohgrenzenAntwort<Schalter>` | commands.txt:167 | unbekannt |
| `P01_65_HK1` | 01-65 | TEM 01-65; Bezeichnung nicht im STE-Katalog | `0621 / 2108` | `RohgrenzenAntwort<Schalter>` | commands.txt:152 | unbekannt |
| `P01_65_HK2` | 01-65 | TEM 01-65; Bezeichnung nicht im STE-Katalog | `0621 / 21881000` | `RohgrenzenAntwort<Schalter>` | commands.txt:168 | unbekannt |
| `P01_66_HK1` | 01-66 | TEM 01-66; Bezeichnung nicht im STE-Katalog | `0621 / 2109` | `RohgrenzenAntwort<Schalter>` | commands.txt:153 | unbekannt |
| `P01_66_HK2` | 01-66 | TEM 01-66; Bezeichnung nicht im STE-Katalog | `0621 / 21891000` | `RohgrenzenAntwort<Schalter>` | commands.txt:169 | unbekannt |
| `P01_76_HK1` | 01-76 | TEM 01-76; Bezeichnung nicht im STE-Katalog | `0621 / 210a` | `RohgrenzenAntwort<UIN>` | commands.txt:154 | unbekannt |
| `P01_76_HK2` | 01-76 | TEM 01-76; Bezeichnung nicht im STE-Katalog | `0621 / 218a1000` | `RohgrenzenAntwort<UIN>` | commands.txt:170 | unbekannt |
| `P01_77_HK1` | 01-77 | TEM 01-77; Bezeichnung nicht im STE-Katalog | `0621 / 210b` | `RohgrenzenAntwort<Schalter>` | commands.txt:155 | unbekannt |
| `P01_77_HK2` | 01-77 | TEM 01-77; Bezeichnung nicht im STE-Katalog | `0621 / 218b1000` | `RohgrenzenAntwort<Schalter>` | commands.txt:171 | unbekannt |
| `P01_78_HK1` | 01-78 | TEM 01-78; Bezeichnung nicht im STE-Katalog | `0621 / 210c` | `RohgrenzenAntwort<Schalter>` | commands.txt:156 | unbekannt |
| `P01_78_HK2` | 01-78 | TEM 01-78; Bezeichnung nicht im STE-Katalog | `0621 / 218c1000` | `RohgrenzenAntwort<Schalter>` | commands.txt:172 | unbekannt |
| `P01_82_HK1` | 01-82 | TEM 01-82; Bezeichnung nicht im STE-Katalog | `0621 / 210d` | `RohgrenzenAntwort<Schalter>` | commands.txt:157 | unbekannt |
| `P01_82_HK2` | 01-82 | TEM 01-82; Bezeichnung nicht im STE-Katalog | `0621 / 218d1000` | `RohgrenzenAntwort<Schalter>` | commands.txt:173 | unbekannt |
| `P01_94_HK1` | 01-94 | TEM 01-94; Bezeichnung nicht im STE-Katalog | `0621 / 210e` | `RohgrenzenAntwort<Schalter>` | commands.txt:158 | unbekannt |
| `P01_94_HK2` | 01-94 | TEM 01-94; Bezeichnung nicht im STE-Katalog | `0621 / 218e1000` | `RohgrenzenAntwort<Schalter>` | commands.txt:174 | unbekannt |
| `P01_96_HK1` | 01-96 | Anlage Vorlaufsollwert (Soll; TKx/TWR) | `0621 / 0914` | `Zahlenantwort<Celsius10>` | commands.txt:91; input/complete.log:5742 | soll_und_istwerte.md |
| `P01_96_HK2` | 01-96 | Anlage Vorlaufsollwert (Soll; TKx/TWR) | `0621 / 09941000` | `Zahlenantwort<Celsius10>` | commands.txt:115 | soll_und_istwerte.md |
| `P01_97_HK1` | 01-97 | Anlage Vorlaufsollwert (Soll; TBx) | `0621 / 0915` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:92; input/complete.log:5743 | soll_und_istwerte.md |
| `P01_97_HK2` | 01-97 | Anlage Vorlaufsollwert (Soll; TBx) | `0621 / 09951000` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:116 | soll_und_istwerte.md |
| `P01_99_HK1` | 01-99 | TEM 01-99; Bezeichnung nicht im STE-Katalog | `0621 / 210f` | `RohgrenzenAntwort<Schalter>` | commands.txt:159; input/complete.log:5608 | unbekannt |
| `P01_99_HK2` | 01-99 | TEM 01-99; Bezeichnung nicht im STE-Katalog | `0621 / 218f1000` | `RohgrenzenAntwort<Schalter>` | commands.txt:175; input/complete.log:7269 | unbekannt |
| `P02_00_HK1` | 02-00 | TEM 02-00; Bezeichnung nicht im STE-Katalog | `0621 / 0105` | `Sonderantwort` | commands.txt:10; input/complete.log:1216 | unbekannt |
| `P02_00_HK2` | 02-00 | TEM 02-00; Bezeichnung nicht im STE-Katalog | `0621 / 01851000` | `Sonderantwort` | commands.txt:18; input/complete.log:1974 | unbekannt |
| `P02_02_HK1` | 02-02 | TEM 02-02; Bezeichnung nicht im STE-Katalog | `0621 / 0104` | `Sonderantwort` | commands.txt:9; input/complete.log:1213 | unbekannt |
| `P02_02_HK2` | 02-02 | TEM 02-02; Bezeichnung nicht im STE-Katalog | `0621 / 01841000` | `Sonderantwort` | commands.txt:17; input/complete.log:1972 | unbekannt |
| `P02_03_HK1` | 02-03 | TEM 02-03; Bezeichnung nicht im STE-Katalog | `0621 / 0103` | `Sonderantwort` | commands.txt:8; input/complete.log:1212 | unbekannt |
| `P02_03_HK2` | 02-03 | TEM 02-03; Bezeichnung nicht im STE-Katalog | `0621 / 01831000` | `Sonderantwort` | commands.txt:16; input/complete.log:1971 | unbekannt |
| `P02_10_HK1` | 02-10 | TEM 02-10; Bezeichnung nicht im STE-Katalog | `0621 / 0106` | `Sonderantwort` | commands.txt:11; input/complete.log:1218 | unbekannt |
| `P02_10_HK2` | 02-10 | TEM 02-10; Bezeichnung nicht im STE-Katalog | `0621 / 01861000` | `Sonderantwort` | commands.txt:19; input/complete.log:1975 | unbekannt |
| `P02_12_HK1` | 02-12 | TEM 02-12; Bezeichnung nicht im STE-Katalog | `0621 / 0109` | `Kurzantwort` | commands.txt:13; input/complete.log:1221 | unbekannt |
| `P02_12_HK2` | 02-12 | TEM 02-12; Bezeichnung nicht im STE-Katalog | `0621 / 01891000` | `Kurzantwort` | commands.txt:21; input/complete.log:1981 | unbekannt |
| `P02_20_HK1` | 02-20 | Aussentemperatur Mittelwert (Soll; TAavg) | `0621 / 0901` | `Zahlenantwort<Celsius10>` | commands.txt:72; input/complete.log:5748 | soll_und_istwerte.md |
| `P02_20_HK2` | 02-20 | Aussentemperatur Mittelwert (Soll; TAavg) | `0621 / 09811000` | `Zahlenantwort<Celsius10>` | commands.txt:96; input/complete.log:4520 | soll_und_istwerte.md |
| `P02_40_HK1` | 02-40 | Wärmeleistung (Soll; PH) | `0621 / 0916` | `Zahlenantwort<Kilowatt10>` | commands.txt:93; input/complete.log:5745 | soll_und_istwerte.md |
| `P02_40_HK2` | 02-40 | Wärmeleistung (Soll; PH) | `0621 / 09961000` | `Zahlenantwort<Kilowatt10>` | commands.txt:117 | soll_und_istwerte.md |
| `P02_41_HK1` | 02-41 | Wärmeleistung (Soll; PBW) | `0621 / 0917` | `Zahlenantwort<Kilowatt10>` | commands.txt:94; input/complete.log:5746 | soll_und_istwerte.md |
| `P02_41_HK2` | 02-41 | Wärmeleistung (Soll; PBW) | `0621 / 09971000` | `Zahlenantwort<Kilowatt10>` | commands.txt:118 | soll_und_istwerte.md |
| `P02_50_HK1` | 02-50 | TEM 02-50; Bezeichnung nicht im STE-Katalog | `0621 / 0308` | `Sonderantwort` | commands.txt:30 | unbekannt |
| `P02_50_HK2` | 02-50 | TEM 02-50; Bezeichnung nicht im STE-Katalog | `0621 / 03881000` | `Sonderantwort` | commands.txt:39 | unbekannt |
| `P02_70` | 02-70 | TEM 02-70; Bezeichnung nicht im STE-Katalog | `0621 / 0a01` | `RohgrenzenAntwort<DAY>` | commands.txt:120; input/complete.log:1229 | unbekannt |
| `P02_71_HK1` | 02-71 | TEM 02-71; Bezeichnung nicht im STE-Katalog | `0621 / 0108` | `RohgrenzenAntwort<Wochenminuten>` | commands.txt:12; input/complete.log:1220 | unbekannt |
| `P02_71_HK2` | 02-71 | TEM 02-71; Bezeichnung nicht im STE-Katalog | `0621 / 01881000` | `RohgrenzenAntwort<Wochenminuten>` | commands.txt:20; input/complete.log:1978 | unbekannt |
| `P02_80_Menue29` | 02-80 | TEM 02-80; Bezeichnung nicht im STE-Katalog | `0621 / 2900` | `Sonderantwort` | commands.txt:200 | unbekannt |
| `P02_80_Menue2A` | 02-80 | TEM 02-80; Bezeichnung nicht im STE-Katalog | `0621 / 2a00` | `Sonderantwort` | commands.txt:202 | unbekannt |
| `P02_81_Menue29` | 02-81 | TEM 02-81; Bezeichnung nicht im STE-Katalog | `0621 / 2901` | `Sonderantwort` | commands.txt:201 | unbekannt |
| `P02_81_Menue2A` | 02-81 | TEM 02-81; Bezeichnung nicht im STE-Katalog | `0621 / 2a01` | `Sonderantwort` | commands.txt:203 | unbekannt |
| `P03_00_HK1` | 03-00 | Raumschutztemperatur | `0621 / 2300` | `Zahlenantwort<Celsius10>` | commands.txt:176; input/complete.log:5610 | Checkliste_Regler_Programmierung.CSV |
| `P03_00_HK2` | 03-00 | Raumschutztemperatur | `0621 / 23801000` | `Zahlenantwort<Celsius10>` | commands.txt:188 | Checkliste_Regler_Programmierung.CSV |
| `P03_01_HK1` | 03-01 | Fusspunkttemperatur | `0621 / 2301` | `Zahlenantwort<Celsius10>` | commands.txt:177; input/complete.log:5611 | Checkliste_Regler_Programmierung.CSV |
| `P03_01_HK2` | 03-01 | Fusspunkttemperatur | `0621 / 23811000` | `Zahlenantwort<Celsius10>` | commands.txt:189 | Checkliste_Regler_Programmierung.CSV |
| `P03_02_HK1` | 03-02 | Heizgrenze Absenkbetrieb | `0621 / 2302` | `Zahlenantwort<Celsius10>` | commands.txt:178 | Checkliste_Regler_Programmierung.CSV |
| `P03_02_HK2` | 03-02 | Heizgrenze Absenkbetrieb | `0621 / 23821000` | `Zahlenantwort<Celsius10>` | commands.txt:190 | Checkliste_Regler_Programmierung.CSV |
| `P03_06_HK1` | 03-06 | Startoptimierung Vorhaltezeit | `0621 / 2303` | `Zahlenantwort<Minuten10>` | commands.txt:179 | Checkliste_Regler_Programmierung.CSV |
| `P03_06_HK2` | 03-06 | Startoptimierung Vorhaltezeit | `0621 / 23831000` | `Zahlenantwort<Minuten10>` | commands.txt:191 | Checkliste_Regler_Programmierung.CSV |
| `P03_07_HK1` | 03-07 | Raumtemperatur - Kompensation | `0621 / 2304` | `Sonderantwort` | commands.txt:180 | Checkliste_Regler_Programmierung.CSV |
| `P03_07_HK2` | 03-07 | Raumtemperatur - Kompensation | `0621 / 23841000` | `Sonderantwort` | commands.txt:192 | Checkliste_Regler_Programmierung.CSV |
| `P03_08_HK1` | 03-08 | Vorlauf Sollwert Heizgrenze | `0621 / 2305` | `Zahlenantwort<Kelvin10>` | commands.txt:181 | Checkliste_Regler_Programmierung.CSV |
| `P03_08_HK2` | 03-08 | Vorlauf Sollwert Heizgrenze | `0621 / 23851000` | `Zahlenantwort<Kelvin10>` | commands.txt:193 | Checkliste_Regler_Programmierung.CSV |
| `P03_10_HK1` | 03-10 | Steilheit Kennlinie | `0621 / 0b04` | `Zahlenantwort<Steilheit100>` | commands.txt:124; input/complete.log:1237 | STE-Katalog |
| `P03_10_HK2` | 03-10 | Steilheit Kennlinie | `0621 / 0b841000` | `Zahlenantwort<Steilheit100>` | commands.txt:130; input/complete.log:2061 | STE-Katalog |
| `P03_11_HK1` | 03-11 | Fusspunkt Vorlaufkennlinie TA | `0621 / a300` | `Zahlenantwort<Celsius10>` | commands.txt:329; input/complete.log:2473 | Checkliste_Regler_Programmierung.CSV |
| `P03_11_HK2` | 03-11 | Fusspunkt Vorlaufkennlinie TA | `0621 / a3801000` | `Zahlenantwort<Celsius10>` | commands.txt:333 | Checkliste_Regler_Programmierung.CSV |
| `P03_20_HK1` | 03-20 | Zeitkonst. für Aussentemp.rmittelung | `0621 / a301` | `Zahlenantwort<Stunden10>` | commands.txt:330; input/complete.log:2474 | Checkliste_Regler_Programmierung.CSV |
| `P03_20_HK2` | 03-20 | Zeitkonst. für Aussentemp.rmittelung | `0621 / a3811000` | `Zahlenantwort<Stunden10>` | commands.txt:334 | Checkliste_Regler_Programmierung.CSV |
| `P03_21_HK1` | 03-21 | Heizgrenze bei Tagbetrieb | `0621 / 0b06` | `Zahlenantwort<Celsius10>` | commands.txt:126; input/complete.log:1239 | STE-Katalog |
| `P03_21_HK2` | 03-21 | Heizgrenze bei Tagbetrieb | `0621 / 0b861000` | `Zahlenantwort<Celsius10>` | commands.txt:132; input/complete.log:2059 | STE-Katalog |
| `P03_23_HK1` | 03-23 | Frostgrenze | `0621 / a302` | `Zahlenantwort<Celsius10>` | commands.txt:331; input/complete.log:2532 | Checkliste_Regler_Programmierung.CSV |
| `P03_23_HK2` | 03-23 | Frostgrenze | `0621 / a3821000` | `Zahlenantwort<Celsius10>` | commands.txt:335 | Checkliste_Regler_Programmierung.CSV |
| `P03_30_HK1` | 03-30 | Nachstellzeit Raumregler | `0621 / a303` | `Zahlenantwort<Minuten10>` | commands.txt:332; input/complete.log:2541 | Checkliste_Regler_Programmierung.CSV |
| `P03_30_HK2` | 03-30 | Nachstellzeit Raumregler | `0621 / a3831000` | `Zahlenantwort<Minuten10>` | commands.txt:336 | Checkliste_Regler_Programmierung.CSV |
| `P03_35_HK1` | 03-35 | Kühlgrenzenabstand | `0621 / 2306` | `Zahlenantwort<Kelvin10>` | commands.txt:182 | Checkliste_Regler_Programmierung.CSV |
| `P03_35_HK2` | 03-35 | Kühlgrenzenabstand | `0621 / 23861000` | `Zahlenantwort<Kelvin10>` | commands.txt:194 | Checkliste_Regler_Programmierung.CSV |
| `P03_43_HK1` | 03-43 | Kühltemperatur | `0621 / 2307` | `Zahlenantwort<Celsius10>` | commands.txt:183 | Checkliste_Regler_Programmierung.CSV |
| `P03_43_HK2` | 03-43 | Kühltemperatur | `0621 / 23871000` | `Zahlenantwort<Celsius10>` | commands.txt:195 | Checkliste_Regler_Programmierung.CSV |
| `P03_50_HK1` | 03-50 | Betriebswahl Heizung und Brauchwasser | `0621 / 0100` | `RohgrenzenAntwort<UIN>` | commands.txt:5; input/complete.log:1209 | STE-Katalog |
| `P03_50_HK2` | 03-50 | Betriebswahl Heizung und Brauchwasser | `0621 / 01801000` | `RohgrenzenAntwort<UIN>` | commands.txt:14; input/complete.log:1968 | STE-Katalog |
| `P03_51_HK1` | 03-51 | Sollwert Raumtemperatur Heizen Tag normal | `0621 / 0b00` | `Zahlenantwort<Celsius10>` | commands.txt:121; input/complete.log:1230 | STE-Katalog |
| `P03_51_HK2` | 03-51 | Sollwert Raumtemperatur Heizen Tag normal | `0621 / 0b801000` | `Zahlenantwort<Celsius10>` | commands.txt:127; input/complete.log:10298 | STE-Katalog |
| `P03_53_HK1` | 03-53 | Sollwert Raumteperatur Heizen Nacht | `0621 / 0b02` | `Zahlenantwort<Celsius10>` | commands.txt:122; input/complete.log:1235 | STE-Katalog |
| `P03_53_HK2` | 03-53 | Sollwert Raumteperatur Heizen Nacht | `0621 / 0b821000` | `Zahlenantwort<Celsius10>` | commands.txt:128; input/complete.log:2064 | STE-Katalog |
| `P03_58_HK1` | 03-58 | Behaglichkeit | `0621 / 0102` | `Zahlenantwort<Kelvin10>` | commands.txt:7; input/complete.log:1211 | STE-Katalog |
| `P03_58_HK2` | 03-58 | Behaglichkeit | `0621 / 01821000` | `Zahlenantwort<Kelvin10>` | commands.txt:15; input/complete.log:1970 | STE-Katalog |
| `P03_61_HK1` | 03-61 | TEM 03-61; Bezeichnung nicht im STE-Katalog | `0621 / 0c00` | `Kurzantwort` | commands.txt:133 | unbekannt |
| `P03_61_HK2` | 03-61 | TEM 03-61; Bezeichnung nicht im STE-Katalog | `0621 / 0c801000` | `Kurzantwort` | commands.txt:136 | unbekannt |
| `P03_62_HK1` | 03-62 | TEM 03-62; Bezeichnung nicht im STE-Katalog | `0621 / 0c01` | `Kurzantwort` | commands.txt:134 | unbekannt |
| `P03_62_HK2` | 03-62 | TEM 03-62; Bezeichnung nicht im STE-Katalog | `0621 / 0c811000` | `Kurzantwort` | commands.txt:137 | unbekannt |
| `P03_63_HK1` | 03-63 | TEM 03-63; Bezeichnung nicht im STE-Katalog | `0621 / 0c02` | `Kurzantwort` | commands.txt:135 | unbekannt |
| `P03_63_HK2` | 03-63 | TEM 03-63; Bezeichnung nicht im STE-Katalog | `0621 / 0c821000` | `Kurzantwort` | commands.txt:138 | unbekannt |
| `P03_78_HK1` | 03-78 | TEM 03-78; Bezeichnung nicht im STE-Katalog | `0621 / 0f00` | `RohgrenzenAntwort<UIN>` | commands.txt:141; input/complete.log:2461 | unbekannt |
| `P03_78_HK2` | 03-78 | TEM 03-78; Bezeichnung nicht im STE-Katalog | `0621 / 0f801000` | `RohgrenzenAntwort<UIN>` | commands.txt:142; input/complete.log:9159 | unbekannt |
| `P04_00` | 04-00 | Fühlerkonfiguration speichern | `0621 / a400` | `RohgrenzenAntwort<Schalter>` | commands.txt:337; input/complete.log:2554 | Checkliste_Regler_Programmierung.CSV |
| `P04_02` | 04-02 | Funktion Sollwerteingang | `0621 / a401` | `RohgrenzenAntwort<UIN>` | commands.txt:338; input/complete.log:2556 | Checkliste_Regler_Programmierung.CSV |
| `P04_08` | 04-08 | Handbetrieb Konfiguration | `0621 / a402` | `RohgrenzenAntwort<UIN>` | commands.txt:339; input/complete.log:2565 | Checkliste_Regler_Programmierung.CSV |
| `P04_20` | 04-20 | Anlage-Hauptregler / Folgeregler | `0621 / a403` | `RohgrenzenAntwort<UIN>` | commands.txt:340; input/complete.log:2567 | Checkliste_Regler_Programmierung.CSV |
| `P04_22_WE1` | 04-22 | WE 1 Zieladresse | `0621 / ab02` | `RohgrenzenAntwort<UIN>` | commands.txt:443; input/complete.log:4371 | STE-Katalog |
| `P04_22_WE2` | 04-22 | WE 1 Zieladresse | `0621 / ac02` | `RohgrenzenAntwort<UIN>` | commands.txt:451 | STE-Katalog |
| `P04_22_WE3` | 04-22 | WE 1 Zieladresse | `0621 / ad02` | `RohgrenzenAntwort<UIN>` | commands.txt:459 | STE-Katalog |
| `P04_22_WE4` | 04-22 | WE 1 Zieladresse | `0621 / ae02` | `RohgrenzenAntwort<UIN>` | commands.txt:467 | STE-Katalog |
| `P04_22_WE5` | 04-22 | WE 1 Zieladresse | `0621 / af02` | `RohgrenzenAntwort<UIN>` | commands.txt:475 | STE-Katalog |
| `P04_22_WE6` | 04-22 | WE 1 Zieladresse | `0621 / b002` | `RohgrenzenAntwort<UIN>` | commands.txt:483 | STE-Katalog |
| `P04_22_WE7` | 04-22 | WE 1 Zieladresse | `0621 / b102` | `RohgrenzenAntwort<UIN>` | commands.txt:491 | STE-Katalog |
| `P04_22_WE8` | 04-22 | WE 1 Zieladresse | `0621 / b202` | `RohgrenzenAntwort<UIN>` | commands.txt:499 | STE-Katalog |
| `P04_27_EH` | 04-27 | eBUS Adresse WEZ | `0621 / aa00` | `RohgrenzenAntwort<UIN>` | commands.txt:426; input/complete.log:4235 | Checkliste_Regler_Programmierung.CSV |
| `P04_27_WP` | 04-27 | eBUS Adresse WEZ | `0621 / a900` | `RohgrenzenAntwort<UIN>` | commands.txt:388; input/complete.log:7567 | Checkliste_Regler_Programmierung.CSV |
| `P04_30` | 04-30 | Multifunktionsausgang 1 | `0621 / a404` | `RohgrenzenAntwort<Schalter>` | commands.txt:341; input/complete.log:2570 | Checkliste_Regler_Programmierung.CSV |
| `P04_31` | 04-31 | Multifunktionsausgang 2 | `0621 / a405` | `RohgrenzenAntwort<Schalter>` | commands.txt:342; input/complete.log:2574 | Checkliste_Regler_Programmierung.CSV |
| `P04_36` | 04-36 | eBUS Speisung Abschaltung | `0621 / a406` | `RohgrenzenAntwort<Schalter>` | commands.txt:343; input/complete.log:2576 | Checkliste_Regler_Programmierung.CSV |
| `P04_40` | 04-40 | Service Passwort | `0621 / a407` | `RohgrenzenAntwort<UIN>` | commands.txt:344; input/complete.log:2581 | Checkliste_Regler_Programmierung.CSV |
| `P04_42` | 04-42 | TEM 04-42; Bezeichnung nicht im STE-Katalog | `0621 / 0000` | `RohgrenzenAntwort<UIN>` | commands.txt:2 | unbekannt |
| `P04_43` | 04-43 | Expert-Modus | `0621 / 0001` | `RohgrenzenAntwort<UIN>` | commands.txt:3; input/complete.log:2469 | Benutzerbestaetigung |
| `P04_45_HK1` | 04-45 | Kommandobefehle | `0621 / 1000` | `RohgrenzenAntwort<UIN>` | commands.txt:143 | Checkliste_Regler_Programmierung.CSV |
| `P04_45_HK2` | 04-45 | Kommandobefehle | `0621 / 23881000` | `RohgrenzenAntwort<UIN>` | commands.txt:196 | Checkliste_Regler_Programmierung.CSV |
| `P04_60_HK1` | 04-60 | Mode Austrocknungsprogramm | `0621 / 2309` | `RohgrenzenAntwort<UIN>` | commands.txt:185 | Checkliste_Regler_Programmierung.CSV |
| `P04_60_HK2` | 04-60 | Mode Austrocknungsprogramm | `0621 / 23891000` | `RohgrenzenAntwort<UIN>` | commands.txt:197 | Checkliste_Regler_Programmierung.CSV |
| `P05_00` | 05-00 | Schaltdifferenz Brauchwasserbereitung | `0621 / a500` | `Zahlenantwort<Kelvin10>` | commands.txt:345; input/complete.log:2596 | Checkliste_Regler_Programmierung.CSV |
| `P05_01` | 05-01 | Temperaturüberhoehung Brauchwasserbereitung | `0621 / a501` | `Zahlenantwort<Kelvin10>` | commands.txt:346; input/complete.log:2597 | Checkliste_Regler_Programmierung.CSV |
| `P05_02` | 05-02 | Brauchwasser-Vorrang | `0621 / a502` | `Zahlenantwort<Stunden10>` | commands.txt:347; input/complete.log:2600 | Checkliste_Regler_Programmierung.CSV |
| `P05_03` | 05-03 | Nachlaufzeit Brauchwasserbereitung | `0621 / a503` | `Zahlenantwort<Minuten10>` | commands.txt:348; input/complete.log:2604 | Checkliste_Regler_Programmierung.CSV |
| `P05_04` | 05-04 | Legionellenschutztemperatur | `0621 / a504` | `Zahlenantwort<Celsius10>` | commands.txt:349; input/complete.log:2607 | Checkliste_Regler_Programmierung.CSV |
| `P05_05` | 05-05 | Funktionsweise Ladepumpennachlauf | `0621 / a505` | `RohgrenzenAntwort<UIN>` | commands.txt:350; input/complete.log:2610 | Checkliste_Regler_Programmierung.CSV |
| `P05_06` | 05-06 | Zirkulationspumpe aktiv | `0621 / a506` | `RohgrenzenAntwort<Schalter>` | commands.txt:351; input/complete.log:2613 | Checkliste_Regler_Programmierung.CSV |
| `P05_07` | 05-07 | Stellglied Brauchwasserbereitung | `0621 / a507` | `RohgrenzenAntwort<Schalter>` | commands.txt:352; input/complete.log:2673 | Checkliste_Regler_Programmierung.CSV |
| `P05_13` | 05-13 | Reduktion Sollwert TBO | `0621 / a508` | `Zahlenantwort<Kelvin10>` | commands.txt:353; input/complete.log:2677 | Checkliste_Regler_Programmierung.CSV |
| `P05_14_HK1` | 05-14 | Legionellenschutzfunktion | `0621 / 230a` | `RohgrenzenAntwort<UIN>` | commands.txt:186 | Checkliste_Regler_Programmierung.CSV |
| `P05_14_HK2` | 05-14 | Legionellenschutzfunktion | `0621 / 238a1000` | `RohgrenzenAntwort<UIN>` | commands.txt:198 | Checkliste_Regler_Programmierung.CSV |
| `P05_40` | 05-40 | Min. Fehlerdauer fuer Brauchwasser Störmeldung | `0621 / a509` | `Zahlenantwort<Stunden10>` | commands.txt:354; input/complete.log:2685 | Checkliste_Regler_Programmierung.CSV |
| `P05_51_HK1` | 05-51 | Sollwert Warmwassertemperatur | `0621 / 0b03` | `Zahlenantwort<Celsius10>` | commands.txt:123; input/complete.log:1236 | Checkliste_Regler_Programmierung.CSV |
| `P05_51_HK2` | 05-51 | Sollwert Warmwassertemperatur | `0621 / 0b831000` | `Zahlenantwort<Celsius10>` | commands.txt:129; input/complete.log:2062 | Checkliste_Regler_Programmierung.CSV |
| `P05_61` | 05-61 | TEM 05-61; Bezeichnung nicht im STE-Katalog | `0621 / 0d00` | `Kurzantwort` | commands.txt:139 | unbekannt |
| `P05_64` | 05-64 | TEM 05-64; Bezeichnung nicht im STE-Katalog | `0621 / 0e00` | `Kurzantwort` | commands.txt:140 | unbekannt |
| `P06_00` | 06-00 | Brauchwasser Ladeleistung | `0621 / a600` | `Zahlenantwort<Kilowatt10>` | commands.txt:356; input/complete.log:2714 | Checkliste_Regler_Programmierung.CSV |
| `P06_01` | 06-01 | Puffer, Heiz- Ladeleistung | `0621 / a601` | `Zahlenantwort<Kilowatt10>` | commands.txt:357; input/complete.log:2715 | Checkliste_Regler_Programmierung.CSV |
| `P06_02` | 06-02 | Kühlleistung | `0621 / a602` | `Zahlenantwort<Kilowatt10>` | commands.txt:358; input/complete.log:2719 | Checkliste_Regler_Programmierung.CSV |
| `P06_04` | 06-04 | WEZ Überhöhung | `0621 / a603` | `Zahlenantwort<Kelvin10>` | commands.txt:359; input/complete.log:2721 | Checkliste_Regler_Programmierung.CSV |
| `P06_05` | 06-05 | Puffer Offset TPM aus | `0621 / a604` | `Zahlenantwort<Kelvin10>` | commands.txt:360; input/complete.log:2723 | Checkliste_Regler_Programmierung.CSV |
| `P06_08` | 06-08 | TBVsoll Überhöhung | `0621 / a605` | `Zahlenantwort<Kelvin10>` | commands.txt:361; input/complete.log:2726 | Checkliste_Regler_Programmierung.CSV |
| `P06_10` | 06-10 | Xp WEZ Manager | `0621 / a606` | `Zahlenantwort<Kelvin10>` | commands.txt:362; input/complete.log:2727 | Checkliste_Regler_Programmierung.CSV |
| `P06_11` | 06-11 | Tn WEZ Manager | `0621 / a607` | `Zahlenantwort<Minuten10>` | commands.txt:363; input/complete.log:2731 | Checkliste_Regler_Programmierung.CSV |
| `P06_12` | 06-12 | Tv WEZ Manager | `0621 / a608` | `Zahlenantwort<Minuten10>` | commands.txt:364; input/complete.log:2737 | Checkliste_Regler_Programmierung.CSV |
| `P06_13` | 06-13 | Reduktion Sollwert TKX | `0621 / a609` | `Zahlenantwort<Kelvin10>` | commands.txt:365; input/complete.log:2742 | Checkliste_Regler_Programmierung.CSV |
| `P06_20` | 06-20 | Sequenzwechsel Flag | `0621 / a60a` | `RohgrenzenAntwort<UIN>` | commands.txt:366; input/complete.log:2746 | Checkliste_Regler_Programmierung.CSV |
| `P07_00_HK1` | 07-00 | Proportional-Bereich Mischer | `0621 / a700` | `Zahlenantwort<Kelvin10>` | commands.txt:367; input/complete.log:2773 | Checkliste_Regler_Programmierung.CSV |
| `P07_00_HK2` | 07-00 | Proportional-Bereich Mischer | `0621 / a7801000` | `Zahlenantwort<Kelvin10>` | commands.txt:375; input/complete.log:9170 | Checkliste_Regler_Programmierung.CSV |
| `P07_01_HK1` | 07-01 | Überhöhung WE-Temperatur | `0621 / a701` | `Zahlenantwort<Kelvin10>` | commands.txt:368; input/complete.log:2776 | Checkliste_Regler_Programmierung.CSV |
| `P07_01_HK2` | 07-01 | Überhöhung WE-Temperatur | `0621 / a7811000` | `Zahlenantwort<Kelvin10>` | commands.txt:376; input/complete.log:9171 | Checkliste_Regler_Programmierung.CSV |
| `P07_02_HK1` | 07-02 | Minimale Vorlauftemperatur | `0621 / a702` | `Zahlenantwort<Celsius10>` | commands.txt:369; input/complete.log:2779 | Checkliste_Regler_Programmierung.CSV |
| `P07_02_HK2` | 07-02 | Minimale Vorlauftemperatur | `0621 / a7821000` | `Zahlenantwort<Celsius10>` | commands.txt:377; input/complete.log:9173 | Checkliste_Regler_Programmierung.CSV |
| `P07_03_HK1` | 07-03 | Pumpennachlauf Heizkreis | `0621 / a703` | `Zahlenantwort<Minuten10>` | commands.txt:370; input/complete.log:2787 | Checkliste_Regler_Programmierung.CSV |
| `P07_03_HK2` | 07-03 | Pumpennachlauf Heizkreis | `0621 / a7831000` | `Zahlenantwort<Minuten10>` | commands.txt:378; input/complete.log:9174 | Checkliste_Regler_Programmierung.CSV |
| `P07_05_HK1` | 07-05 | Heizkreistyp | `0621 / a704` | `RohgrenzenAntwort<UIN>` | commands.txt:371; input/complete.log:2788 | Checkliste_Regler_Programmierung.CSV |
| `P07_05_HK2` | 07-05 | Heizkreistyp | `0621 / a7841000` | `RohgrenzenAntwort<UIN>` | commands.txt:379; input/complete.log:9175 | Checkliste_Regler_Programmierung.CSV |
| `P07_06_HK1` | 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung | `0621 / a705` | `Zahlenantwort<Stunden10>` | commands.txt:372; input/complete.log:2798 | Checkliste_Regler_Programmierung.CSV |
| `P07_06_HK2` | 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung | `0621 / a7851000` | `Zahlenantwort<Stunden10>` | commands.txt:380; input/complete.log:9176 | Checkliste_Regler_Programmierung.CSV |
| `P07_08_HK1` | 07-08 | Vorlauf Maximaltemperatur TV | `0621 / 0b05` | `Zahlenantwort<Celsius10>` | commands.txt:125; input/complete.log:1238 | STE-Katalog |
| `P07_08_HK2` | 07-08 | Vorlauf Maximaltemperatur TV | `0621 / 0b851000` | `Zahlenantwort<Celsius10>` | commands.txt:131; input/complete.log:2060 | STE-Katalog |
| `P07_09` | 07-09 | TEM 07-09; Bezeichnung nicht im STE-Katalog | `0621 / 0200` | `Zahlenantwort<Celsius10>` | commands.txt:22 | unbekannt |
| `P07_14_HK1` | 07-14 | Heizkreisfunktion im Kühlbetrieb | `0621 / a706` | `RohgrenzenAntwort<UIN>` | commands.txt:373; input/complete.log:2800 | Checkliste_Regler_Programmierung.CSV |
| `P07_14_HK2` | 07-14 | Heizkreisfunktion im Kühlbetrieb | `0621 / a7861000` | `RohgrenzenAntwort<UIN>` | commands.txt:381; input/complete.log:9221 | Checkliste_Regler_Programmierung.CSV |
| `P07_31_HK1` | 07-31 | Heizkreisüberhöhung Niedertarif | `0621 / a707` | `Zahlenantwort<Kelvin10>` | commands.txt:374; input/complete.log:2807 | Checkliste_Regler_Programmierung.CSV |
| `P07_31_HK2` | 07-31 | Heizkreisüberhöhung Niedertarif | `0621 / a7871000` | `Zahlenantwort<Kelvin10>` | commands.txt:382; input/complete.log:9222 | Checkliste_Regler_Programmierung.CSV |
| `P08_55` | 08-55 | Puffer aktiv | `0621 / a800` | `RohgrenzenAntwort<UIN>` | commands.txt:383 | STE-Katalog |
| `P08_58` | 08-58 | Puffer Minimaltemperatur | `0621 / a801` | `Zahlenantwort<Celsius10>` | commands.txt:384 | STE-Katalog |
| `P08_59` | 08-59 | Puffer Maximaltemperatur | `0621 / a802` | `Zahlenantwort<Celsius10>` | commands.txt:385 | STE-Katalog |
| `P08_72` | 08-72 | Delta Puffer bei Solar aktiv | `0621 / a803` | `Zahlenantwort<Kelvin10>` | commands.txt:386 | STE-Katalog |
| `P08_79` | 08-79 | WW Minimaltemperatur bei Solar aktiv | `0621 / a804` | `Zahlenantwort<Celsius10>` | commands.txt:387 | STE-Katalog |
| `P09_00_EH` | 09-00 | Nachlaufzeit Schutzfunktion | `0621 / aa01` | `Zahlenantwort<Minuten10>` | commands.txt:427; input/complete.log:4237 | Checkliste_Regler_Programmierung.CSV |
| `P09_00_WP` | 09-00 | Nachlaufzeit Schutzfunktion | `0621 / a901` | `Zahlenantwort<Minuten10>` | commands.txt:389; input/complete.log:7569 | Checkliste_Regler_Programmierung.CSV |
| `P09_04_EH` | 09-04 | Vorlaufzeit Quellenpumpe | `0621 / aa02` | `Zahlenantwort<Minuten10>` | commands.txt:428; input/complete.log:4246 | Checkliste_Regler_Programmierung.CSV |
| `P09_04_WP` | 09-04 | Vorlaufzeit Quellenpumpe | `0621 / a902` | `Zahlenantwort<Minuten10>` | commands.txt:390; input/complete.log:7579 | Checkliste_Regler_Programmierung.CSV |
| `P09_07_EH` | 09-07 | WEZ Typ | `0621 / aa03` | `RohgrenzenAntwort<UIN>` | commands.txt:429; input/complete.log:4250 | Checkliste_Regler_Programmierung.CSV |
| `P09_07_WP` | 09-07 | WEZ Typ | `0621 / a903` | `RohgrenzenAntwort<UIN>` | commands.txt:391; input/complete.log:7585 | Checkliste_Regler_Programmierung.CSV |
| `P09_08_HK1` | 09-08 | Wärmeerzeuger Sperre | `0621 / 230b` | `RohgrenzenAntwort<UIN>` | commands.txt:187 | Checkliste_Regler_Programmierung.CSV |
| `P09_08_HK2` | 09-08 | Wärmeerzeuger Sperre | `0621 / 238b1000` | `RohgrenzenAntwort<UIN>` | commands.txt:199 | Checkliste_Regler_Programmierung.CSV |
| `P09_11_EH` | 09-11 | Bedingte WEZ Freigabe | `0621 / aa04` | `RohgrenzenAntwort<UIN>` | commands.txt:430; input/complete.log:4257 | Checkliste_Regler_Programmierung.CSV |
| `P09_11_WP` | 09-11 | Bedingte WEZ Freigabe | `0621 / a904` | `RohgrenzenAntwort<UIN>` | commands.txt:392; input/complete.log:7590 | Checkliste_Regler_Programmierung.CSV |
| `P09_12_EH` | 09-12 | Aussentemperatursperre TAW | `0621 / aa05` | `Zahlenantwort<Celsius10>` | commands.txt:431; input/complete.log:4261 | Checkliste_Regler_Programmierung.CSV |
| `P09_12_WP` | 09-12 | Aussentemperatursperre TAW | `0621 / a905` | `Zahlenantwort<Celsius10>` | commands.txt:393; input/complete.log:7594 | Checkliste_Regler_Programmierung.CSV |
| `P09_13_EH` | 09-13 | Energiezweig Funktion | `0621 / aa06` | `RohgrenzenAntwort<UIN>` | commands.txt:432; input/complete.log:4265 | Checkliste_Regler_Programmierung.CSV |
| `P09_13_WP` | 09-13 | Energiezweig Funktion | `0621 / a906` | `RohgrenzenAntwort<UIN>` | commands.txt:394; input/complete.log:7602 | Checkliste_Regler_Programmierung.CSV |
| `P09_14_EH` | 09-14 | Diff. Leistungszwang Tkmax | `0621 / aa07` | `Zahlenantwort<Kelvin10>` | commands.txt:433; input/complete.log:4266 | Checkliste_Regler_Programmierung.CSV |
| `P09_14_WP` | 09-14 | Diff. Leistungszwang Tkmax | `0621 / a907` | `Zahlenantwort<Kelvin10>` | commands.txt:395; input/complete.log:7609 | Checkliste_Regler_Programmierung.CSV |
| `P09_21_EH` | 09-21 | WE Abschaltdifferenz | `0621 / aa08` | `Zahlenantwort<Kelvin10>` | commands.txt:434; input/complete.log:4269 | Checkliste_Regler_Programmierung.CSV |
| `P09_21_WP` | 09-21 | WE Abschaltdifferenz | `0621 / a908` | `Zahlenantwort<Kelvin10>` | commands.txt:396; input/complete.log:7665 | Checkliste_Regler_Programmierung.CSV |
| `P09_23_EH` | 09-23 | Minimale Stillstandszeit | `0621 / aa09` | `Zahlenantwort<Minuten10>` | commands.txt:435; input/complete.log:4326 | Checkliste_Regler_Programmierung.CSV |
| `P09_23_WP` | 09-23 | Minimale Stillstandszeit | `0621 / a909` | `Zahlenantwort<Minuten10>` | commands.txt:397; input/complete.log:7673 | Checkliste_Regler_Programmierung.CSV |
| `P09_26_EH` | 09-26 | Vorhaltezeit 2. Stufe | `0621 / aa0a` | `Zahlenantwort<Sekunden10>` | commands.txt:436; input/complete.log:4330 | Checkliste_Regler_Programmierung.CSV |
| `P09_26_WP` | 09-26 | Vorhaltezeit 2. Stufe | `0621 / a90a` | `Zahlenantwort<Sekunden10>` | commands.txt:398; input/complete.log:7684 | Checkliste_Regler_Programmierung.CSV |
| `P09_31_EH` | 09-31 | Minimale WE Laufzeit | `0621 / aa0b` | `Zahlenantwort<Minuten10>` | commands.txt:437; input/complete.log:4335 | Checkliste_Regler_Programmierung.CSV |
| `P09_31_WP` | 09-31 | Minimale WE Laufzeit | `0621 / a90b` | `Zahlenantwort<Minuten10>` | commands.txt:399; input/complete.log:7687 | Checkliste_Regler_Programmierung.CSV |
| `P09_34_EH` | 09-34 | Einschaltverzögerung 2. Stufe | `0621 / aa0c` | `Zahlenantwort<Minuten10>` | commands.txt:438; input/complete.log:4337 | Checkliste_Regler_Programmierung.CSV |
| `P09_34_WP` | 09-34 | Einschaltverzögerung 2. Stufe | `0621 / a90c` | `Zahlenantwort<Minuten10>` | commands.txt:400; input/complete.log:7701 | Checkliste_Regler_Programmierung.CSV |
| `P09_35_EH` | 09-35 | Schaltdifferenz 2. Stufe | `0621 / aa0d` | `Zahlenantwort<Kelvin10>` | commands.txt:439; input/complete.log:4342 | Checkliste_Regler_Programmierung.CSV |
| `P09_35_WP` | 09-35 | Schaltdifferenz 2. Stufe | `0621 / a90d` | `Zahlenantwort<Kelvin10>` | commands.txt:401; input/complete.log:7703 | Checkliste_Regler_Programmierung.CSV |
| `P10_31_EH` | 10-31 | WE Maximaltemperatur | `0621 / aa0e` | `Zahlenantwort<Celsius10>` | commands.txt:440; input/complete.log:4345 | Checkliste_Regler_Programmierung.CSV |
| `P10_31_WP` | 10-31 | WE Maximaltemperatur | `0621 / a90e` | `Zahlenantwort<Celsius10>` | commands.txt:402; input/complete.log:7745 | Checkliste_Regler_Programmierung.CSV |
| `P11_01_WE1` | 11-01 | WE Steuerbefehl | `0621 / ab03` | `RohgrenzenAntwort<UIN>` | commands.txt:444; input/complete.log:4372 | STE-Katalog |
| `P11_01_WE2` | 11-01 | WE Steuerbefehl | `0621 / ac03` | `RohgrenzenAntwort<UIN>` | commands.txt:452 | STE-Katalog |
| `P11_01_WE3` | 11-01 | WE Steuerbefehl | `0621 / ad03` | `RohgrenzenAntwort<UIN>` | commands.txt:460 | STE-Katalog |
| `P11_01_WE4` | 11-01 | WE Steuerbefehl | `0621 / ae03` | `RohgrenzenAntwort<UIN>` | commands.txt:468 | STE-Katalog |
| `P11_01_WE5` | 11-01 | WE Steuerbefehl | `0621 / af03` | `RohgrenzenAntwort<UIN>` | commands.txt:476 | STE-Katalog |
| `P11_01_WE6` | 11-01 | WE Steuerbefehl | `0621 / b003` | `RohgrenzenAntwort<UIN>` | commands.txt:484 | STE-Katalog |
| `P11_01_WE7` | 11-01 | WE Steuerbefehl | `0621 / b103` | `RohgrenzenAntwort<UIN>` | commands.txt:492 | STE-Katalog |
| `P11_01_WE8` | 11-01 | WE Steuerbefehl | `0621 / b203` | `RohgrenzenAntwort<UIN>` | commands.txt:500 | STE-Katalog |
| `P11_02_WE1` | 11-02 | WE Nennleistung | `0621 / ab04` | `Zahlenantwort<Kilowatt10>` | commands.txt:445; input/complete.log:4376 | STE-Katalog |
| `P11_02_WE2` | 11-02 | WE Nennleistung | `0621 / ac04` | `Zahlenantwort<Kilowatt10>` | commands.txt:453 | STE-Katalog |
| `P11_02_WE3` | 11-02 | WE Nennleistung | `0621 / ad04` | `Zahlenantwort<Kilowatt10>` | commands.txt:461 | STE-Katalog |
| `P11_02_WE4` | 11-02 | WE Nennleistung | `0621 / ae04` | `Zahlenantwort<Kilowatt10>` | commands.txt:469 | STE-Katalog |
| `P11_02_WE5` | 11-02 | WE Nennleistung | `0621 / af04` | `Zahlenantwort<Kilowatt10>` | commands.txt:477 | STE-Katalog |
| `P11_02_WE6` | 11-02 | WE Nennleistung | `0621 / b004` | `Zahlenantwort<Kilowatt10>` | commands.txt:485 | STE-Katalog |
| `P11_02_WE7` | 11-02 | WE Nennleistung | `0621 / b104` | `Zahlenantwort<Kilowatt10>` | commands.txt:493 | STE-Katalog |
| `P11_02_WE8` | 11-02 | WE Nennleistung | `0621 / b204` | `Zahlenantwort<Kilowatt10>` | commands.txt:501 | STE-Katalog |
| `P11_03_WE1` | 11-03 | minimale WE-Leistung | `0621 / ab05` | `RohgrenzenAntwort<UIN>` | commands.txt:446; input/complete.log:4381 | STE-Katalog |
| `P11_03_WE2` | 11-03 | minimale WE-Leistung | `0621 / ac05` | `RohgrenzenAntwort<UIN>` | commands.txt:454 | STE-Katalog |
| `P11_03_WE3` | 11-03 | minimale WE-Leistung | `0621 / ad05` | `RohgrenzenAntwort<UIN>` | commands.txt:462 | STE-Katalog |
| `P11_03_WE4` | 11-03 | minimale WE-Leistung | `0621 / ae05` | `RohgrenzenAntwort<UIN>` | commands.txt:470 | STE-Katalog |
| `P11_03_WE5` | 11-03 | minimale WE-Leistung | `0621 / af05` | `RohgrenzenAntwort<UIN>` | commands.txt:478 | STE-Katalog |
| `P11_03_WE6` | 11-03 | minimale WE-Leistung | `0621 / b005` | `RohgrenzenAntwort<UIN>` | commands.txt:486 | STE-Katalog |
| `P11_03_WE7` | 11-03 | minimale WE-Leistung | `0621 / b105` | `RohgrenzenAntwort<UIN>` | commands.txt:494 | STE-Katalog |
| `P11_03_WE8` | 11-03 | minimale WE-Leistung | `0621 / b205` | `RohgrenzenAntwort<UIN>` | commands.txt:502 | STE-Katalog |
| `P11_04_WE1` | 11-04 | Einschaltleistung Folge WE | `0621 / ab06` | `RohgrenzenAntwort<UIN>` | commands.txt:447; input/complete.log:4383 | STE-Katalog |
| `P11_04_WE2` | 11-04 | Einschaltleistung Folge WE | `0621 / ac06` | `RohgrenzenAntwort<UIN>` | commands.txt:455 | STE-Katalog |
| `P11_04_WE3` | 11-04 | Einschaltleistung Folge WE | `0621 / ad06` | `RohgrenzenAntwort<UIN>` | commands.txt:463 | STE-Katalog |
| `P11_04_WE4` | 11-04 | Einschaltleistung Folge WE | `0621 / ae06` | `RohgrenzenAntwort<UIN>` | commands.txt:471 | STE-Katalog |
| `P11_04_WE5` | 11-04 | Einschaltleistung Folge WE | `0621 / af06` | `RohgrenzenAntwort<UIN>` | commands.txt:479 | STE-Katalog |
| `P11_04_WE6` | 11-04 | Einschaltleistung Folge WE | `0621 / b006` | `RohgrenzenAntwort<UIN>` | commands.txt:487 | STE-Katalog |
| `P11_04_WE7` | 11-04 | Einschaltleistung Folge WE | `0621 / b106` | `RohgrenzenAntwort<UIN>` | commands.txt:495 | STE-Katalog |
| `P11_04_WE8` | 11-04 | Einschaltleistung Folge WE | `0621 / b206` | `RohgrenzenAntwort<UIN>` | commands.txt:503 | STE-Katalog |
| `P11_05_WE1` | 11-05 | WE Folgewechsel | `0621 / ab07` | `RohgrenzenAntwort<Schalter>` | commands.txt:448; input/complete.log:4385 | STE-Katalog |
| `P11_05_WE2` | 11-05 | WE Folgewechsel | `0621 / ac07` | `RohgrenzenAntwort<Schalter>` | commands.txt:456 | STE-Katalog |
| `P11_05_WE3` | 11-05 | WE Folgewechsel | `0621 / ad07` | `RohgrenzenAntwort<Schalter>` | commands.txt:464 | STE-Katalog |
| `P11_05_WE4` | 11-05 | WE Folgewechsel | `0621 / ae07` | `RohgrenzenAntwort<Schalter>` | commands.txt:472 | STE-Katalog |
| `P11_05_WE5` | 11-05 | WE Folgewechsel | `0621 / af07` | `RohgrenzenAntwort<Schalter>` | commands.txt:480 | STE-Katalog |
| `P11_05_WE6` | 11-05 | WE Folgewechsel | `0621 / b007` | `RohgrenzenAntwort<Schalter>` | commands.txt:488 | STE-Katalog |
| `P11_05_WE7` | 11-05 | WE Folgewechsel | `0621 / b107` | `RohgrenzenAntwort<Schalter>` | commands.txt:496 | STE-Katalog |
| `P11_05_WE8` | 11-05 | WE Folgewechsel | `0621 / b207` | `RohgrenzenAntwort<Schalter>` | commands.txt:504 | STE-Katalog |
| `P15_10_WP` | 15-10 | Heissgas Maximaltemperatur | `0621 / a90f` | `Zahlenantwort<Celsius10>` | commands.txt:403; input/complete.log:7752 | Checkliste_Regler_Programmierung.CSV |
| `P15_11_WP` | 15-11 | TWVmax Abschalthysterese | `0621 / a910` | `Zahlenantwort<Kelvin10>` | commands.txt:404; input/complete.log:7766 | Checkliste_Regler_Programmierung.CSV |
| `P15_12_WP` | 15-12 | Kondensator Austritt Störung | `0621 / a911` | `Zahlenantwort<Celsius10>` | commands.txt:405 | Checkliste_Regler_Programmierung.CSV |
| `P15_13_WP` | 15-13 | Kondensator Austritt Abschaltoffset | `0621 / a912` | `Zahlenantwort<Kelvin10>` | commands.txt:406 | Checkliste_Regler_Programmierung.CSV |
| `P15_21_WP` | 15-21 | Nachlaufzeit Quellenpumpe | `0621 / a913` | `Zahlenantwort<Minuten10>` | commands.txt:407 | Checkliste_Regler_Programmierung.CSV |
| `P15_22_WP` | 15-22 | Wärmequelle Frostschutztemperatur | `0621 / a914` | `Zahlenantwort<Celsius10>` | commands.txt:408 | Checkliste_Regler_Programmierung.CSV |
| `P15_23` | 15-23 | Frostschutztemperatur TVD | `0621 / a50a` | `Zahlenantwort<Celsius10>` | commands.txt:355; input/complete.log:2692 | STE-Katalog |
| `P15_24_WP` | 15-24 | Wärmequelle Eintrittsschutztemperatur | `0621 / a915` | `Zahlenantwort<Celsius10>` | commands.txt:409 | STE-Katalog |
| `P15_25_WP` | 15-25 | Abschaltoffset Frostschutz | `0621 / a916` | `Zahlenantwort<Kelvin10>` | commands.txt:410 | Checkliste_Regler_Programmierung.CSV |
| `P15_26_WP` | 15-26 | TWE-Temp rpunkt TWVmax Reduktion | `0621 / a917` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:411 | Checkliste_Regler_Programmierung.CSV |
| `P15_27_WP` | 15-27 | TWVmax bei TWE Grenztenperatur | `0621 / a918` | `RohgrenzenAntwort<UIN>` | commands.txt:412 | Checkliste_Regler_Programmierung.CSV |
| `P15_28_WP` | 15-28 | TWE Grenztenperatur | `0621 / a919` | `RohgrenzenAntwort<ByteMitVorzeichen>` | commands.txt:413 | Checkliste_Regler_Programmierung.CSV |
| `P15_40_WP` | 15-40 | Abtautyp | `0621 / a91a` | `RohgrenzenAntwort<UIN>` | commands.txt:414 | Checkliste_Regler_Programmierung.CSV |
| `P15_41_WP` | 15-41 | Abtaudifferenz (TWE - TVD) | `0621 / a91b` | `Zahlenantwort<Kelvin10>` | commands.txt:415 | Checkliste_Regler_Programmierung.CSV |
| `P15_42_WP` | 15-42 | Freigabe Abtauung (TVD) | `0621 / a91c` | `Zahlenantwort<Celsius10>` | commands.txt:416 | Checkliste_Regler_Programmierung.CSV |
| `P15_43_WP` | 15-43 | Abtauendetemperatur (TVD) | `0621 / a91d` | `Zahlenantwort<Celsius10>` | commands.txt:417 | Checkliste_Regler_Programmierung.CSV |
| `P15_44_WP` | 15-44 | Abtaudauer | `0621 / a91e` | `Zahlenantwort<Minuten10>` | commands.txt:418 | Checkliste_Regler_Programmierung.CSV |
| `P15_45_WP` | 15-45 | Abtausperrzeit | `0621 / a91f` | `Zahlenantwort<Minuten10>` | commands.txt:419 | STE-Katalog |
| `P15_46_WP` | 15-46 | Verzögerung Niederdruck | `0621 / a920` | `RohgrenzenAntwort<UIN>` | commands.txt:420 | STE-Katalog |
| `P15_47_WP` | 15-47 | Abtropfzeit | `0621 / a921` | `RohgrenzenAntwort<UIN>` | commands.txt:421 | STE-Katalog |
| `P15_48_WP` | 15-48 | Verzögerung Druckdifferenzeingang | `0621 / a922` | `RohgrenzenAntwort<UIN>` | commands.txt:422 | STE-Katalog |
| `P15_49_WP` | 15-49 | Abtau Frostschutzstörung | `0621 / a923` | `Zahlenantwort<Celsius10>` | commands.txt:423 | STE-Katalog |
| `P15_50_WP` | 15-50 | Abtau Frostschutz Offset Zusatzheizung | `0621 / a924` | `Zahlenantwort<Kelvin10>` | commands.txt:424 | STE-Katalog |
| `P15_60_WP` | 15-60 | Anpassen TWA Messwert | `0621 / a925` | `Zahlenantwort<Kelvin10>` | commands.txt:425 | STE-Katalog |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 00` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 01` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 02` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 03` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 04` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 05` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 06` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 07` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 08` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 09` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 0a` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 0b` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 0c` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 0d` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 0e` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 0f` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 10` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 11` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 12` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 13` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 14` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 15` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 16` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 17` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 18` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 19` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 1a` | `MenueAnzahl / MenueZusatzflag` |  | — |
| `Menueblock` | — | 8 Menues: je 7 Bit Eintragsanzahl und 1 Bit Zusatzflag; siehe Menu-Structure.md | `0620 / 1b` | `MenueAnzahl / MenueZusatzflag` |  | — |

## STE-Kennungen ohne beobachtete Antwort

`03-60`, `04-61`, `04-62`, `04-63`, `04-64`, `05-60`, `09-20`, `09-32`

Diese Kennungen erhalten keine geratenen Anfragen. Das Fehlen in diesem Mitschnitt belegt nicht, dass der Regler sie nicht unterstützt.
