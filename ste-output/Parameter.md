# TEM-Parameter aus der STE-Datei

Quelle: `Datapacks v 1.1  über V 52  9.02.09.ste` · 64974 Bytes · Controllerkennung: 17385

**217 Datensätze, davon 206 mit 119 unterschiedlichen TEM-Kennungen und 11 ohne TEM-Kennung.**

Die Tabelle ist nach der TEM-Kennung sortiert. Mehrfach vorkommende Kennungen bleiben getrennt. Die Datensatznummer (#) verweist auf die ursprüngliche Dateireihenfolge.

**Wert** bezeichnet das gespeicherte Zahlenfeld, keinen bestätigten aktuellen Anlagenwert. Ob die Datei eine Anlagenaufnahme oder eine bearbeitete Vorlage ist, lässt sich daraus nicht entscheiden. HK 1/2 sind aus den Datensatzpaaren abgeleitet. Einheiten sind aus den Metadaten erschlossen; `s?` bleibt eine Vermutung. `—` bedeutet, dass kein Einheitenname hinterlegt ist, nicht zwingend dimensionslos.

**TEM-Kennung, Einstellebene und FB-Menüposition sind getrennte Nummerierungen.** Die Datei nennt Kühltemperatur `03-43` und Kühlgrenzenabstand `03-35`. Kaskadeneinträge behalten auch für WE 2–8 ihre im Titel gespeicherten Kennungen `04-22` bzw. `11-01` bis `11-05`.

Format, Unsicherheiten und Auffälligkeiten: [STE-Format.md](../STE-Format.md). Alle Zahlenfelder und exakten Originaltexte: [parameter.json](parameter.json). Tabellenexport: [parameter.csv](parameter.csv).

## Parameterübersicht

| TEM | Bezeichnung | Kontext | Wert | Einheit¹ | Min. | Max. | # |
|---|---|---|---:|---|---:|---:|---:|
| 03-00 | Raumschutztemperatur | HK 1¹ | 10 | °C | 3 | 15 | [32](#datensatz-32) |
| 03-00 | Raumschutztemperatur | HK 2¹ | 10 | °C | 3 | 15 | [33](#datensatz-33) |
| 03-01 | Fusspunkttemperatur | HK 1¹ | 20 | °C | 10 | 40 | [34](#datensatz-34) |
| 03-01 | Fusspunkttemperatur | HK 2¹ | 20 | °C | 10 | 40 | [35](#datensatz-35) |
| 03-02 | Heizgrenze Absenkbetrieb | HK 1¹ | 17 | °C | -10 | 20 | [36](#datensatz-36) |
| 03-02 | Heizgrenze Absenkbetrieb | HK 2¹ | 17 | °C | -10 | 20 | [37](#datensatz-37) |
| 03-06 | Startoptimierung Vorhaltezeit | HK 1¹ | 0 | min | 0 | 900 | [38](#datensatz-38) |
| 03-06 | Startoptimierung Vorhaltezeit | HK 2¹ | 0 | min | 0 | 900 | [39](#datensatz-39) |
| 03-07 | Raumtemperatur - Kompensation | HK 1¹ | 0 | — | 0 | 10 | [40](#datensatz-40) |
| 03-07 | Raumtemperatur - Kompensation | HK 2¹ | 0 | — | 0 | 10 | [41](#datensatz-41) |
| 03-08 | Vorlauf Sollwert  Heizgrenze | HK 1¹ | -10 | K | -10 | 10 | [42](#datensatz-42) |
| 03-08 | Vorlauf Sollwert  Heizgrenze | HK 2¹ | -10 | K | -10 | 10 | [43](#datensatz-43) |
| 03-10 | Steilheit Kennlinie | HK 1¹ | 0.3 | — | 0 | 5 | [15](#datensatz-15) |
| 03-10 | Steilheit Kennlinie | HK 2¹ | 0.3 | — | 0 | 5 | [16](#datensatz-16) |
| 03-11 | Fusspunkt Vorlaufkennlinie: TA | HK 1¹ | 20 | °C | -10 | 30 | [44](#datensatz-44) |
| 03-11 | Fusspunkt Vorlaufkennlinie: TA | HK 2¹ | 20 | °C | -10 | 30 | [45](#datensatz-45) |
| 03-20 | Zeitkonstante für Aussentemperaturmittelung | Einstellebene 3, Raumtemperaturregelung | 10 | h | 0 | 20 | [46](#datensatz-46) |
| 03-21 | Heizgrenze bei Tagbetrieb | HK 1¹ | 16 | °C | 0 | 40 | [19](#datensatz-19) |
| 03-21 | Heizgrenze bei Tagbetrieb | HK 2¹ | 16 | °C | 0 | 40 | [20](#datensatz-20) |
| 03-23 | Frostgrenze | HK 1¹ | 2 | °C | -10 | 20 | [47](#datensatz-47) |
| 03-23 | Frostgrenze | HK 2¹ | 2 | °C | -10 | 20 | [48](#datensatz-48) |
| 03-30 | Nachstellzeit Raumregler | HK 1¹ | 0 | min | 0 | 200 | [49](#datensatz-49) |
| 03-30 | Nachstellzeit Raumregler | HK 2¹ | 0 | min | 0 | 200 | [50](#datensatz-50) |
| 03-35 | Kühlgrenzenabstand | HK 1¹ | 10 | °C | 2 | 10 | [51](#datensatz-51) |
| 03-35 | Kühlgrenzenabstand | HK 2¹ | 5 | °C | 2 | 10 | [52](#datensatz-52) |
| 03-43 | Kühltemperatur | HK 1¹ | 22 | °C | 10 | 30 | [53](#datensatz-53) |
| 03-43 | Kühltemperatur | HK 2¹ | 22 | °C | 10 | 30 | [54](#datensatz-54) |
| 03-50 | Betriebswahl Heizung und Brauchwasser | HK 1¹ | 1 | — | 0 | 5 | [1](#datensatz-1) |
| 03-50 | Betriebswahl Heizung und Brauchwasser | HK 2¹ | 1 | — | 0 | 5 | [2](#datensatz-2) |
| 03-51 | Sollwert Raumtemperatur Heizen Tag normal | HK 1¹ | 20.5 | °C | 10 | 30 | [9](#datensatz-9) |
| 03-51 | Sollwert Raumtemperatur Heizen Tag normal | HK 2¹ | 20.5 | °C | 10 | 30 | [10](#datensatz-10) |
| 03-53 | Sollwert Raumteperatur Heizen Nacht | HK 1¹ | 18 | °C | 5 | 20 | [11](#datensatz-11) |
| 03-53 | Sollwert Raumteperatur Heizen Nacht | HK 2¹ | 18 | °C | 5 | 20 | [12](#datensatz-12) |
| 03-58 | Behaglichkeit | HK 1¹ | 0 | K | -3 | 3 | [5](#datensatz-5) |
| 03-58 | Behaglichkeit | HK 2¹ | -1 | K | -3 | 3 | [6](#datensatz-6) |
| 03-60 | Partydauer HB | HK 1¹ | 0 | min | 0 | 600 | [7](#datensatz-7) |
| 03-60 | Partydauer HB | HK 2¹ | 0 | min | 0 | 600 | [8](#datensatz-8) |
| 04-00 | Fühlerkonfiguration speichern | Einstellebene 4, Globale Einstellungen | 0 | — | 0 | 1 | [59](#datensatz-59) |
| 04-02 | Funktion Sollwerteingang | Einstellebene 4, Globale Einstellungen | 0 | — | 0 | 4 | [60](#datensatz-60) |
| 04-08 | Handbetrieb Konfiguration | Einstellebene 4, Globale Einstellungen | 2 | — | 1 | 2 | [61](#datensatz-61) |
| 04-20 | Anlage-Hauptregler / Folgeregler | Einstellebene 4, Globale Einstellungen | 2 | — | 0 | 25 | [62](#datensatz-62) |
| 04-22 | WE 1 Zieladresse | Einstellebene 11, WE 1 Kaskadenfunktionen | 11 | — | 0 | 24 | [170](#datensatz-170) |
| 04-22 | WE 1 Zieladresse | Einstellebene 12, WE 2 Kaskadenfunktionen | 12 | — | 0 | 24 | [176](#datensatz-176) |
| 04-22 | WE 1 Zieladresse | Einstellebene 13, WE 3 Kaskadenfunktionen | 0 | — | 0 | 24 | [182](#datensatz-182) |
| 04-22 | WE 1 Zieladresse | Einstellebene 14, WE 4 Kaskadenfunktionen | 0 | — | 0 | 24 | [188](#datensatz-188) |
| 04-22 | WE 1 Zieladresse | Einstellebene 15, WE 5 Kaskadenfunktionen | 0 | — | 0 | 24 | [194](#datensatz-194) |
| 04-22 | WE 1 Zieladresse | Einstellebene 16, WE 6 Kaskadenfunktionen | 0 | — | 0 | 24 | [200](#datensatz-200) |
| 04-22 | WE 1 Zieladresse | Einstellebene 17, WE 7 Kaskadenfunktionen | 0 | — | 0 | 24 | [206](#datensatz-206) |
| 04-22 | WE 1 Zieladresse | Einstellebene 18, WE 8 Kaskadenfunktionen | 0 | — | 0 | 24 | [212](#datensatz-212) |
| 04-27 | eBUS Adresse WEZ | Einstellebene 9, WE Einstellungen Wärmepumpe | 11 | — | 0 | 25 | [115](#datensatz-115) |
| 04-27 | eBUS Adresse WEZ | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 12 | — | 0 | 25 | [155](#datensatz-155) |
| 04-30 | Multifunktionsusgang 1 | Einstellebene 4, Globale Einstellungen | 1 | — | 0 | 1 | [63](#datensatz-63) |
| 04-31 | Multifunktionsusgang 2 | Einstellebene 4, Globale Einstellungen | 0 | — | 0 | 1 | [64](#datensatz-64) |
| 04-36 | eBUS Speisung Abschaltung | Einstellebene 4, Globale Einstellungen | 1 | — | 0 | 1 | [65](#datensatz-65) |
| 04-40 | Service Passwort | Einstellebene 4, Globale Einstellungen | 161 | — | 0 | 255 | [66](#datensatz-66) |
| 04-45 | Kommandobefehle | Einstellebene 2 | 0 | — | 0 | 29 | [21](#datensatz-21) |
| 04-60 | Mode Austrocknungsprogramm | Einstellebene 4, Globale Einstellungen | 0 | — | 0 | 2 | [67](#datensatz-67) |
| 04-61 | Vorlaufsollwert-Steigung in der Aufheizphase | Einstellebene 4, Globale Einstellungen | 5 | K | 0.5 | 20 | [68](#datensatz-68) |
| 04-62 | Vorlaufsollwert-Abfall in der Abkühlphase | Einstellebene 4, Globale Einstellungen | -5 | K | -20 | -0.5 | [69](#datensatz-69) |
| 04-63 | Vorlaufsollwert in der Beharrungsphase | Einstellebene 4, Globale Einstellungen | 47 | °C | 20 | 70 | [70](#datensatz-70) |
| 04-64 | Dauer der Beharrungsphase | Einstellebene 4, Globale Einstellungen | 30 | — | 1 | 250 | [71](#datensatz-71) |
| 05-00 | Schaltdifferenz Brauchwasserbereitung | Einstellebene 5, Brauchwasserbereitung | 5 | °C | 2 | 20 | [72](#datensatz-72) |
| 05-01 | Temperaturüberhoehung Brauchwasserbereitung | Einstellebene 5, Brauchwasserbereitung | 6 | °C | 2 | 30 | [73](#datensatz-73) |
| 05-02 | Brauchwasser-Vorrang | Einstellebene 5, Brauchwasserbereitung | 0.1 | — | 0 | 20 | [74](#datensatz-74) |
| 05-03 | Nachlaufzeit Brauchwasserbereitung | Einstellebene 5, Brauchwasserbereitung | 3 | min | 0 | 30 | [75](#datensatz-75) |
| 05-04 | Legionellenschutztemperatur | Einstellebene 5, Brauchwasserbereitung | 60 | °C | 60 | 80 | [76](#datensatz-76) |
| 05-05 | Funktionsweise Ladepumpennachlauf | Einstellebene 5, Brauchwasserbereitung | 0 | — | 0 | 2 | [77](#datensatz-77) |
| 05-06 | Zirkulationspumpe aktiv | Einstellebene 5, Brauchwasserbereitung | 1 | — | 0 | 1 | [78](#datensatz-78) |
| 05-07 | Stellglied Brauchwasserbereitung | Einstellebene 5, Brauchwasserbereitung | 1 | — | 0 | 1 | [79](#datensatz-79) |
| 05-13 | Reduktion Sollwert TBO | Einstellebene 5, Brauchwasserbereitung | 15 | K | 0 | 20 | [80](#datensatz-80) |
| 05-14 | Legionellenschutzfunktion | Einstellebene 3, Raumtemperaturregelung | 0 | — | 0 | 8 | [55](#datensatz-55) |
| 05-40 | Min. Fehlerdauer fuer Brauchwasser Störmeldung | Einstellebene 5, Brauchwasserbereitung | 0 | h | 0 | 20 | [81](#datensatz-81) |
| 05-51 | Sollwert Warmwassertemperatur | HK 1¹ | 50 | °C | 10 | 70 | [13](#datensatz-13) |
| 05-51 | Sollwert Warmwassertemperatur | HK 2¹ | 10 | °C | 10 | 70 | [14](#datensatz-14) |
| 05-60 | Partydauer WWB | HK 1¹ | 0 | min | 0 | 600 | [22](#datensatz-22) |
| 05-60 | Partydauer WWB | HK 2¹ | 0 | min | 0 | 600 | [23](#datensatz-23) |
| 06-00 | Brauchwasser Ladeleistung | Einstellebene 6, WM-Einstellungen | 100 | kW | 0 | 999 | [83](#datensatz-83) |
| 06-01 | Puffer, Heiz-  Ladeleistung | Einstellebene 6, WM-Einstellungen | 100 | kW | 0 | 999 | [84](#datensatz-84) |
| 06-02 | Kühlleistung | Einstellebene 6, WM-Einstellungen | 100 | kW | 0 | 999 | [85](#datensatz-85) |
| 06-04 | WEZ Überhöhung | Einstellebene 6, WM-Einstellungen | 10 | K | 0 | 20 | [86](#datensatz-86) |
| 06-05 | Puffer Offset TPM aus | Einstellebene 6, WM-Einstellungen | 0 | K | -10 | 30 | [87](#datensatz-87) |
| 06-08 | TBVsoll Überhöhung | Einstellebene 6, WM-Einstellungen | 10 | K | 0 | 20 | [88](#datensatz-88) |
| 06-10 | Xp WEZ Manager | Einstellebene 6, WM-Einstellungen | 3 | K | 2 | 100 | [89](#datensatz-89) |
| 06-11 | Tn WEZ Manager | Einstellebene 6, WM-Einstellungen | 20 | min | 0 | 100 | [90](#datensatz-90) |
| 06-12 | Tv WEZ Manager | Einstellebene 6, WM-Einstellungen | 0 | s? | 0 | 100 | [91](#datensatz-91) |
| 06-13 | Reduktion Sollwert TKX | Einstellebene 6, WM-Einstellungen | 5 | K | 0 | 25 | [92](#datensatz-92) |
| 06-20 | Sequenzwechsel Flag | Einstellebene 6, WM-Einstellungen | 0 | — | 0 | 8 | [93](#datensatz-93) |
| 07-00 | Proportional-Bereich Mischer | HK 1¹ | 15 | K | 5 | 30 | [94](#datensatz-94) |
| 07-00 | Proportional-Bereich Mischer | HK 2¹ | 15 | K | 5 | 30 | [95](#datensatz-95) |
| 07-01 | Überhöhung WE-Temperatur | HK 1¹ | 0 | K | 0 | 30 | [96](#datensatz-96) |
| 07-01 | Überhöhung WE-Temperatur | HK 2¹ | 3 | K | 0 | 30 | [97](#datensatz-97) |
| 07-02 | Minimale Vorlauftemperatur | HK 1¹ | 0 | °C | 0 | 40 | [98](#datensatz-98) |
| 07-02 | Minimale Vorlauftemperatur | HK 2¹ | 0 | °C | 0 | 40 | [99](#datensatz-99) |
| 07-03 | Pumpennachlauf Heizkreis | HK 1¹ | 15 | min | 0 | 30 | [100](#datensatz-100) |
| 07-03 | Pumpennachlauf Heizkreis | HK 2¹ | 15 | min | 0 | 30 | [101](#datensatz-101) |
| 07-05 | Heizkreistyp | HK 1¹ | 2 | — | 0 | 3 | [102](#datensatz-102) |
| 07-05 | Heizkreistyp | HK 2¹ | 0 | — | 0 | 3 | [103](#datensatz-103) |
| 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung | HK 1¹ | 0 | h | 0 | 20 | [104](#datensatz-104) |
| 07-06 | Min. Fehlerdauer fuer Vorlauf-Störmeldung | HK 2¹ | 0 | h | 0 | 20 | [105](#datensatz-105) |
| 07-08 | Vorlauf Maximaltemperatur TV | HK 1¹ | 55 | °C | 10 | 90 | [17](#datensatz-17) |
| 07-08 | Vorlauf Maximaltemperatur TV | HK 2¹ | 45 | °C | 10 | 90 | [18](#datensatz-18) |
| 07-14 | Heizkreisfunktion im Kühlbetrieb | HK 1¹ | 0 | — | 0 | 3 | [106](#datensatz-106) |
| 07-14 | Heizkreisfunktion im Kühlbetrieb | HK 2¹ | 0 | — | 0 | 3 | [107](#datensatz-107) |
| 07-31 | Heizkreisüberhöhung Niedertarif | HK 1¹ | 0 | K | 0 | 30 | [108](#datensatz-108) |
| 07-31 | Heizkreisüberhöhung Niedertarif | HK 2¹ | 0 | K | 0 | 30 | [109](#datensatz-109) |
| 08-55 | Puffer aktiv | Einstellebene 8, Solar- und Speicherfunktionen | 0 | — | 0 | 3 | [110](#datensatz-110) |
| 08-58 | Puffer Minimaltemperatur | Einstellebene 8, Solar- und Speicherfunktionen | 0 | °C | 0 | 80 | [111](#datensatz-111) |
| 08-59 | Puffer Maximaltemperatur | Einstellebene 8, Solar- und Speicherfunktionen | 90 | °C | 60 | 100 | [112](#datensatz-112) |
| 08-72 | Delta Puffer bei Solar aktiv | Einstellebene 8, Solar- und Speicherfunktionen | 40 | K | 0 | 40 | [113](#datensatz-113) |
| 08-79 | WW Minimaltemperatur bei Solar aktiv | Einstellebene 8, Solar- und Speicherfunktionen | 10 | K | 0 | 60 | [114](#datensatz-114) |
| 09-00 | Nachlaufzeit Schutzfunktion | Einstellebene 9, WE Einstellungen Wärmepumpe | 1 | min | 0 | 40 | [116](#datensatz-116) |
| 09-00 | Nachlaufzeit Schutzfunktion | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 1 | min | 0 | 40 | [156](#datensatz-156) |
| 09-04 | Vorlaufzeit Quellenpumpe | Einstellebene 9, WE Einstellungen Wärmepumpe | 0.5 | min | 0 | 300 | [117](#datensatz-117) |
| 09-04 | Einschaltverzögerung | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 0.5 | min | 0 | 300 | [157](#datensatz-157) |
| 09-07 | WEZ Typ | Einstellebene 9, WE Einstellungen Wärmepumpe | 5 | — | 0 | 6 | [118](#datensatz-118) |
| 09-07 | WEZ Typ | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 1 | — | 0 | 6 | [158](#datensatz-158) |
| 09-08 | Wärmeerzeuger Sperre | Einstellebene 3, Raumtemperaturregelung | 0 | — | 0 | 3 | [56](#datensatz-56) |
| 09-11 | Bedingte WEZ Freigabe | Einstellebene 9, WE Einstellungen Wärmepumpe | 0 | — | 0 | 13 | [119](#datensatz-119) |
| 09-11 | Bedingte WEZ Freigabe | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 10 | — | 0 | 13 | [159](#datensatz-159) |
| 09-12 | Aussentemperatursperre TAW | Einstellebene 9, WE Einstellungen Wärmepumpe | -50 | °C | -50 | 50 | [120](#datensatz-120) |
| 09-12 | Aussentemperatursperre TAW | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | -5 | °C | -50 | 50 | [160](#datensatz-160) |
| 09-13 | Energiezwang Funktion | Einstellebene 9, WE Einstellungen Wärmepumpe | 2 | — | 0 | 3 | [121](#datensatz-121) |
| 09-13 | Energiezwang Funktion | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 2 | — | 0 | 3 | [161](#datensatz-161) |
| 09-14 | Diff. Leistungszwang Tkmax | Einstellebene 9, WE Einstellungen Wärmepumpe | 0 | K | -30 | 30 | [122](#datensatz-122) |
| 09-14 | Diff. Leistungszwang Tkmax | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 0 | K | -30 | 30 | [162](#datensatz-162) |
| 09-20 | Solltemperatur Handbetrieb | HK 1¹ | 48 | °C | 0 | 90 | [57](#datensatz-57) |
| 09-20 | Solltemperatur Handbetrieb | HK 2¹ | 48 | °C | 0 | 90 | [58](#datensatz-58) |
| 09-21 | WE Abschaltdifferenz | Einstellebene 9, WE Einstellungen Wärmepumpe | 5 | K | 2 | 30 | [123](#datensatz-123) |
| 09-21 | WE Abschaltdifferenz | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 3 | K | 2 | 30 | [163](#datensatz-163) |
| 09-23 | Minimale Stillstandszeit | Einstellebene 9, WE Einstellungen Wärmepumpe | 12 | min | 0 | 100 | [124](#datensatz-124) |
| 09-23 | Minimale Stillstandszeit | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 60 | min | 0 | 100 | [164](#datensatz-164) |
| 09-26 | Vorhaltezeit 2. Stufe | Einstellebene 9, WE Einstellungen Wärmepumpe | 10 | s? | 0 | 100 | [125](#datensatz-125) |
| 09-26 | Vorhaltezeit 2. Stufe | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 0 | s? | 0 | 100 | [165](#datensatz-165) |
| 09-31 | Minimale WE Laufzeit | Einstellebene 9, WE Einstellungen Wärmepumpe | 9 | min | 0 | 40 | [126](#datensatz-126) |
| 09-31 | Minimale WE Laufzeit | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 0 | min | 0 | 40 | [166](#datensatz-166) |
| 09-32 | TWVmin Kühlbetrieb | Einstellebene 9, WE Einstellungen Wärmepumpe | 14 | °C | 0 | 30 | [127](#datensatz-127) |
| 09-34 | Einschaltverzögerung 2. Stufe | Einstellebene 9, WE Einstellungen Wärmepumpe | 9 | min | 0 | 40 | [128](#datensatz-128) |
| 09-34 | Einschaltverzögerung 2. Stufe | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 0 | min | 0 | 40 | [167](#datensatz-167) |
| 09-35 | Schaltdifferenz 2. Stufe | Einstellebene 9, WE Einstellungen Wärmepumpe | -3 | K | -20 | 0 | [129](#datensatz-129) |
| 09-35 | Schaltdifferenz 2. Stufe | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 0 | K | -20 | 0 | [168](#datensatz-168) |
| 10-31 | WE Maximaltemperatur | Einstellebene 9, WE Einstellungen Wärmepumpe | 70 | °C | 30 | 80 | [130](#datensatz-130) |
| 10-31 | WE Maximaltemperatur | Einstellebene 10, WE Einstellungen Elektro Zusatzheizung | 70 | °C | 30 | 80 | [169](#datensatz-169) |
| 11-01 | WE Steuerbefehl | Einstellebene 11, WE 1 Kaskadenfunktionen | 2 | — | 1 | 4 | [171](#datensatz-171) |
| 11-01 | WE Steuerbefehl | Einstellebene 12, WE 2 Kaskadenfunktionen | 2 | — | 1 | 4 | [177](#datensatz-177) |
| 11-01 | WE Steuerbefehl | Einstellebene 13, WE 3 Kaskadenfunktionen | 2 | — | 1 | 4 | [183](#datensatz-183) |
| 11-01 | WE Steuerbefehl | Einstellebene 14, WE 4 Kaskadenfunktionen | 2 | — | 1 | 4 | [189](#datensatz-189) |
| 11-01 | WE Steuerbefehl | Einstellebene 15, WE 5 Kaskadenfunktionen | 2 | — | 1 | 4 | [195](#datensatz-195) |
| 11-01 | WE Steuerbefehl | Einstellebene 16, WE 6 Kaskadenfunktionen | 2 | — | 1 | 4 | [201](#datensatz-201) |
| 11-01 | WE Steuerbefehl | Einstellebene 17, WE 7 Kaskadenfunktionen | 2 | — | 1 | 4 | [207](#datensatz-207) |
| 11-01 | WE Steuerbefehl | Einstellebene 18, WE 8 Kaskadenfunktionen | 2 | — | 1 | 4 | [213](#datensatz-213) |
| 11-02 | WE Nennleistung | Einstellebene 11, WE 1 Kaskadenfunktionen | 100 | kW | 0 | 999 | [172](#datensatz-172) |
| 11-02 | WE Nennleistung | Einstellebene 12, WE 2 Kaskadenfunktionen | 100 | kW | 0 | 999 | [178](#datensatz-178) |
| 11-02 | WE Nennleistung | Einstellebene 13, WE 3 Kaskadenfunktionen | 100 | kW | 0 | 999 | [184](#datensatz-184) |
| 11-02 | WE Nennleistung | Einstellebene 14, WE 4 Kaskadenfunktionen | 100 | kW | 0 | 999 | [190](#datensatz-190) |
| 11-02 | WE Nennleistung | Einstellebene 15, WE 5 Kaskadenfunktionen | 100 | kW | 0 | 999 | [196](#datensatz-196) |
| 11-02 | WE Nennleistung | Einstellebene 16, WE 6 Kaskadenfunktionen | 100 | kW | 0 | 999 | [202](#datensatz-202) |
| 11-02 | WE Nennleistung | Einstellebene 17, WE 7 Kaskadenfunktionen | 100 | kW | 0 | 999 | [208](#datensatz-208) |
| 11-02 | WE Nennleistung | Einstellebene 18, WE 8 Kaskadenfunktionen | 100 | kW | 0 | 999 | [214](#datensatz-214) |
| 11-03 | minimale WE-Leistung | Einstellebene 11, WE 1 Kaskadenfunktionen | 70 | % | 0 | 100 | [173](#datensatz-173) |
| 11-03 | minimale WE-Leistung | Einstellebene 12, WE 2 Kaskadenfunktionen | 100 | % | 0 | 100 | [179](#datensatz-179) |
| 11-03 | minimale WE-Leistung | Einstellebene 13, WE 3 Kaskadenfunktionen | 100 | % | 0 | 100 | [185](#datensatz-185) |
| 11-03 | minimale WE-Leistung | Einstellebene 14, WE 4 Kaskadenfunktionen | 100 | % | 0 | 100 | [191](#datensatz-191) |
| 11-03 | minimale WE-Leistung | Einstellebene 15, WE 5 Kaskadenfunktionen | 100 | % | 0 | 100 | [197](#datensatz-197) |
| 11-03 | minimale WE-Leistung | Einstellebene 16, WE 6 Kaskadenfunktionen | 100 | % | 0 | 100 | [203](#datensatz-203) |
| 11-03 | minimale WE-Leistung | Einstellebene 17, WE 7 Kaskadenfunktionen | 100 | % | 0 | 100 | [209](#datensatz-209) |
| 11-03 | minimale WE-Leistung | Einstellebene 18, WE 8 Kaskadenfunktionen | 100 | % | 0 | 100 | [215](#datensatz-215) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 11, WE 1 Kaskadenfunktionen | 80 | % | 0 | 100 | [174](#datensatz-174) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 12, WE 2 Kaskadenfunktionen | 80 | % | 0 | 100 | [180](#datensatz-180) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 13, WE 3 Kaskadenfunktionen | 80 | % | 0 | 100 | [186](#datensatz-186) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 14, WE 4 Kaskadenfunktionen | 80 | % | 0 | 100 | [192](#datensatz-192) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 15, WE 5 Kaskadenfunktionen | 80 | % | 0 | 100 | [198](#datensatz-198) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 16, WE 6 Kaskadenfunktionen | 80 | % | 0 | 100 | [204](#datensatz-204) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 17, WE 7 Kaskadenfunktionen | 80 | % | 0 | 100 | [210](#datensatz-210) |
| 11-04 | Einschaltleistung Folge WE | Einstellebene 18, WE 8 Kaskadenfunktionen | 80 | % | 0 | 100 | [216](#datensatz-216) |
| 11-05 | WE Folgewechsel | Einstellebene 11, WE 1 Kaskadenfunktionen | 0 | — | 0 | 1 | [175](#datensatz-175) |
| 11-05 | WE Folgewechsel | Einstellebene 12, WE 2 Kaskadenfunktionen | 0 | — | 0 | 1 | [181](#datensatz-181) |
| 11-05 | WE Folgewechsel | Einstellebene 13, WE 3 Kaskadenfunktionen | 0 | — | 0 | 1 | [187](#datensatz-187) |
| 11-05 | WE Folgewechsel | Einstellebene 14, WE 4 Kaskadenfunktionen | 0 | — | 0 | 1 | [193](#datensatz-193) |
| 11-05 | WE Folgewechsel | Einstellebene 15, WE 5 Kaskadenfunktionen | 0 | — | 0 | 1 | [199](#datensatz-199) |
| 11-05 | WE Folgewechsel | Einstellebene 16, WE 6 Kaskadenfunktionen | 0 | — | 0 | 1 | [205](#datensatz-205) |
| 11-05 | WE Folgewechsel | Einstellebene 17, WE 7 Kaskadenfunktionen | 0 | — | 0 | 1 | [211](#datensatz-211) |
| 11-05 | WE Folgewechsel | Einstellebene 18, WE 8 Kaskadenfunktionen | 0 | — | 0 | 1 | [217](#datensatz-217) |
| 15-10 | Heissgas Maximaltemperatur | Einstellebene 9, WE Einstellungen Wärmepumpe | 125 | °C | 0 | 140 | [131](#datensatz-131) |
| 15-11 | TWVmax Abschalthysterese | Einstellebene 9, WE Einstellungen Wärmepumpe | 7 | K | 2 | 30 | [132](#datensatz-132) |
| 15-12 | Kondensator Austritt Störung | Einstellebene 9, WE Einstellungen Wärmepumpe | -5 | °C | -20 | 70 | [133](#datensatz-133) |
| 15-13 | Kondensator Austritt Abschaltoffset | Einstellebene 9, WE Einstellungen Wärmepumpe | 2 | K | 0 | 10 | [134](#datensatz-134) |
| 15-21 | Nachlaufzeit Quellenpumpe | Einstellebene 9, WE Einstellungen Wärmepumpe | 0.5 | min | 0 | 15 | [135](#datensatz-135) |
| 15-22 | Wärmequelle Frostschutztemperatur | Einstellebene 9, WE Einstellungen Wärmepumpe | -12 | °C | -50 | 10 | [136](#datensatz-136) |
| 15-23 | Frostschutztemperatur TVD | Einstellebene 5, Brauchwasserbereitung | 4 | — | -20 | 20 | [82](#datensatz-82) |
| 15-24 | Wärmequelle Eintrittsschutztemperatur | Einstellebene 9, WE Einstellungen Wärmepumpe | 40 | °C | 0 | 50 | [137](#datensatz-137) |
| 15-25 | Abschaltoffset Frostschutz | Einstellebene 9, WE Einstellungen Wärmepumpe | 2 | K | 0 | 20 | [138](#datensatz-138) |
| 15-26 | TWE-Temperaturpunkt TWVmax Reduktion | Einstellebene 9, WE Einstellungen Wärmepumpe | -20 | °C | -20 | 10 | [139](#datensatz-139) |
| 15-27 | TWVmax bei TWE Grenztemperatur | Einstellebene 9, WE Einstellungen Wärmepumpe | 60 | °C | 20 | 60 | [140](#datensatz-140) |
| 15-28 | TWE Grenztemperatur | Einstellebene 9, WE Einstellungen Wärmepumpe | -30 | °C | -30 | 10 | [141](#datensatz-141) |
| 15-40 | Abtautyp | Einstellebene 9, WE Einstellungen Wärmepumpe | 0 | — | 0 | 2 | [142](#datensatz-142) |
| 15-41 | Abtaudifferenz (TWE - TVD) | Einstellebene 9, WE Einstellungen Wärmepumpe | 10 | °C | 3 | 30 | [143](#datensatz-143) |
| 15-42 | Freigabe Abtauung (TVD) | Einstellebene 9, WE Einstellungen Wärmepumpe | -6 | °C | -20 | 20 | [144](#datensatz-144) |
| 15-43 | Abtauendetemperatur (TVD) | Einstellebene 9, WE Einstellungen Wärmepumpe | 9 | °C | 0 | 40 | [145](#datensatz-145) |
| 15-44 | Abtaudauer | Einstellebene 9, WE Einstellungen Wärmepumpe | 10 | min | 0 | 30 | [146](#datensatz-146) |
| 15-45 | Abtausperrzeit | Einstellebene 9, WE Einstellungen Wärmepumpe | 45 | min | 0 | 60 | [147](#datensatz-147) |
| 15-46 | Verzögerung Niederdruck | Einstellebene 9, WE Einstellungen Wärmepumpe | 10 | s? | 0 | 250 | [148](#datensatz-148) |
| 15-47 | Abtropfzeit | Einstellebene 9, WE Einstellungen Wärmepumpe | 0 | — | 0 | 100 | [149](#datensatz-149) |
| 15-48 | Verzögerung Druckdifferenzeingang | Einstellebene 9, WE Einstellungen Wärmepumpe | 120 | — | 0 | 250 | [150](#datensatz-150) |
| 15-49 | Abtau Frostschutzstörung | Einstellebene 9, WE Einstellungen Wärmepumpe | 12 | °C | 3 | 20 | [151](#datensatz-151) |
| 15-50 | Abtau Frostschutz Offset Zusatzheizung | Einstellebene 9, WE Einstellungen Wärmepumpe | 2 | K | 2 | 10 | [152](#datensatz-152) |
| 15-60 | Anpassen TWA Messwert | Einstellebene 9, WE Einstellungen Wärmepumpe | 0 | K | 0 | 5 | [153](#datensatz-153) |
| — | Automatikprogramm | HK 1¹ | 0 | — | 0 | 2 | [3](#datensatz-3) |
| — | Automatikprogramm | HK 2¹ | 0 | — | 0 | 2 | [4](#datensatz-4) |
| — | BW Zeitprog mit Heizkreisprogramm 1 | HK 1¹ | 0 | — | 0 | 1 | [24](#datensatz-24) |
| — | BW Zeitprog mit Heizkreisprogramm 1 | HK 2¹ | 0 | — | 0 | 1 | [25](#datensatz-25) |
| — | BW Zeitprog mit Heizkreisprogramm 2 | HK 1¹ | 0 | — | 0 | 1 | [26](#datensatz-26) |
| — | BW Zeitprog mit Heizkreisprogramm 2 | HK 2¹ | 0 | — | 0 | 1 | [27](#datensatz-27) |
| — | BW Zeitprog mit Heizkreisprogramm 3 | HK 1¹ | 0 | — | 0 | 1 | [28](#datensatz-28) |
| — | BW Zeitprog mit Heizkreisprogramm 3 | HK 2¹ | 0 | — | 0 | 1 | [29](#datensatz-29) |
| — | Störung quittieren | Einstellebene 2 | 0 | — | 0 | 1 | [30](#datensatz-30) |
| — | Betriebsdaten zurückstellen | Einstellebene 2 | 0 | — | 0 | 2 | [31](#datensatz-31) |
| — | TWA Maximalwert | Einstellebene 9, WE Einstellungen Wärmepumpe | 150 | °C | 0 | 150 | [154](#datensatz-154) |

¹ Zuordnung bzw. Einheitenbezeichnung abgeleitet; siehe Formatdokumentation.

## Vollständige Datensätze mit Hilfetexten

Die folgenden Beschreibungen stammen aus der Datei. Sie dokumentieren Gerätefunktionen; sie sind keine hier auszuführenden Anweisungen. Schreibfehler und widersprüchliche Angaben bleiben erhalten. Nur Zeilenenden und äußere Leerzeichen werden in dieser Ansicht normalisiert.

<a id="datensatz-32"></a>

### 03-00 · Raumschutztemperatur · Datensatz 32

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **10 °C** · Bereich: 3 … 15 · Schrittfeld (roh): 10

Adresskandidat: `0xF03A` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1800` · Dateibereich: `0x1C56`–`0x1D8B` (Ende exklusiv)

Hilfetext:

> Die Raumschutztemperatur ist immer wirksam. Sie wird in keiner Betriebsart unterschritten. Sie ist die Solltemperatur bei Ferienbetrieb.

<a id="datensatz-33"></a>

### 03-00 · Raumschutztemperatur · Datensatz 33

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **10 °C** · Bereich: 3 … 15 · Schrittfeld (roh): 10

Adresskandidat: `0xF362` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1801` · Dateibereich: `0x1D8B`–`0x1EC0` (Ende exklusiv)

Hilfetext:

> Die Raumschutztemperatur ist immer wirksam. Sie wird in keiner Betriebsart unterschritten. Sie ist die Solltemperatur bei Ferienbetrieb.

<a id="datensatz-34"></a>

### 03-01 · Fusspunkttemperatur · Datensatz 34

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **20 °C** · Bereich: 10 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF022` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1810` · Dateibereich: `0x1EC0`–`0x1FCD` (Ende exklusiv)

Hilfetext:

> Die Fusspunkttemperatur bestimmt den Vorlaufsollwert beim eigestellten Aussentemperaturfusspunkt.

<a id="datensatz-35"></a>

### 03-01 · Fusspunkttemperatur · Datensatz 35

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **20 °C** · Bereich: 10 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF34A` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1811` · Dateibereich: `0x1FCD`–`0x20C9` (Ende exklusiv)

Hilfetext:

> Die Fusspunkttemperatur bestimmt den Vorlaufsollwert bei 20 °C Aussentemperatur.

<a id="datensatz-36"></a>

### 03-02 · Heizgrenze Absenkbetrieb · Datensatz 36

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **17 °C** · Bereich: -10 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF034` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1820` · Dateibereich: `0x20C9`–`0x2256` (Ende exklusiv)

Hilfetext:

> Wenn die gemittelte Aussentemperatur den eingestellten Wert im Absenkbetrieb überschreitet, schaltet der Heizkreis auf Sommerbetrieb. Bei Unterschreiten des Einstellwertes um 2 K wird der Heizbetrieb wieder eingeschaltet

<a id="datensatz-37"></a>

### 03-02 · Heizgrenze Absenkbetrieb · Datensatz 37

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **17 °C** · Bereich: -10 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF35C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1821` · Dateibereich: `0x2256`–`0x23E3` (Ende exklusiv)

Hilfetext:

> Wenn die gemittelte Aussentemperatur den eingestellten Wert im Absenkbetrieb überschreitet, schaltet der Heizkreis auf Sommerbetrieb. Bei Unterschreiten des Einstellwertes um 2 K wird der Heizbetrieb wieder eingeschaltet

<a id="datensatz-38"></a>

### 03-06 · Startoptimierung Vorhaltezeit · Datensatz 38

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 min** · Bereich: 0 … 900 · Schrittfeld (roh): 10

Adresskandidat: `0xF036` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x1830` · Dateibereich: `0x23E3`–`0x2576` (Ende exklusiv)

Hilfetext:

> Damit wird erreicht, dass die Raumtemperatur zum Belegungsbeginn nahezu dem Raumtemperatur-Sollwert entspricht. Der Einstellwert (in Minuten) legt die Zeitdifferenz für den vorzeitigen Heizbeginn zum Belegungsbeginn fest.

<a id="datensatz-39"></a>

### 03-06 · Startoptimierung Vorhaltezeit · Datensatz 39

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 min** · Bereich: 0 … 900 · Schrittfeld (roh): 10

Adresskandidat: `0xF35E` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x1831` · Dateibereich: `0x2576`–`0x2709` (Ende exklusiv)

Hilfetext:

> Damit wird erreicht, dass die Raumtemperatur zum Belegungsbeginn nahezu dem Raumtemperatur-Sollwert entspricht. Der Einstellwert (in Minuten) legt die Zeitdifferenz für den vorzeitigen Heizbeginn zum Belegungsbeginn fest.

<a id="datensatz-40"></a>

### 03-07 · Raumtemperatur - Kompensation · Datensatz 40

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 ** · Bereich: 0 … 10 · Schrittfeld (roh): 1

Adresskandidat: `0xF038` · Typcode: `13` · Einheitencode: `0` · Schlüssel: `0x1840` · Dateibereich: `0x2709`–`0x288D` (Ende exklusiv)

Hilfetext:

> Weicht die mit einer Fernbedienung gemessene Raumtemperatur vom Sollwert ab (z. B. durch Fremdwärme wie Sonneneinstrahlung), korrigiert der Regler die Vorlauftemperatur entsprechend dem eingestellten Wert.

<a id="datensatz-41"></a>

### 03-07 · Raumtemperatur - Kompensation · Datensatz 41

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 ** · Bereich: 0 … 10 · Schrittfeld (roh): 1

Adresskandidat: `0xF360` · Typcode: `13` · Einheitencode: `0` · Schlüssel: `0x1841` · Dateibereich: `0x288D`–`0x2A11` (Ende exklusiv)

Hilfetext:

> Weicht die mit einer Fernbedienung gemessene Raumtemperatur vom Sollwert ab (z. B. durch Fremdwärme wie Sonneneinstrahlung), korrigiert der Regler die Vorlauftemperatur entsprechend dem eingestellten Wert.

<a id="datensatz-42"></a>

### 03-08 · Vorlauf Sollwert  Heizgrenze · Datensatz 42

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **-10 K** · Bereich: -10 … 10 · Schrittfeld (roh): 5

Adresskandidat: `0xF026` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x1850` · Dateibereich: `0x2A11`–`0x2B6A` (Ende exklusiv)

Hilfetext:

> Der Sommerbetrieb ist aktiv wenn die Differenz zwischen dem errechneten Vorlauftemperatur-Sollwert und dem Raumtemperatur-Sollwert kleiner als der Einstellwert ist.

<a id="datensatz-43"></a>

### 03-08 · Vorlauf Sollwert  Heizgrenze · Datensatz 43

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **-10 K** · Bereich: -10 … 10 · Schrittfeld (roh): 5

Adresskandidat: `0xF34E` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x1851` · Dateibereich: `0x2B6A`–`0x2CC3` (Ende exklusiv)

Hilfetext:

> Der Sommerbetrieb ist aktiv wenn die Differenz zwischen dem errechneten Vorlauftemperatur-Sollwert und dem Raumtemperatur-Sollwert kleiner als der Einstellwert ist.

<a id="datensatz-15"></a>

### 03-10 · Steilheit Kennlinie · Datensatz 15

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **0.3 ** · Bereich: 0 … 5 · Schrittfeld (roh): 1

Adresskandidat: `0xF01A` · Typcode: `14` · Einheitencode: `0` · Schlüssel: `0x1030` · Dateibereich: `0x0BF7`–`0x0CE3` (Ende exklusiv)

Hilfetext:

> Die Steilheit bestimmt die Steigung der Kennlinie in Abhängigkeit der Aussentemperatur

<a id="datensatz-16"></a>

### 03-10 · Steilheit Kennlinie · Datensatz 16

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **0.3 ** · Bereich: 0 … 5 · Schrittfeld (roh): 1

Adresskandidat: `0xF342` · Typcode: `14` · Einheitencode: `0` · Schlüssel: `0x1031` · Dateibereich: `0x0CE3`–`0x0DCF` (Ende exklusiv)

Hilfetext:

> Die Steilheit bestimmt die Steigung der Kennlinie in Abhängigkeit der Aussentemperatur

<a id="datensatz-44"></a>

### 03-11 · Fusspunkt Vorlaufkennlinie: TA · Datensatz 44

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **20 °C** · Bereich: -10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF024` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1860` · Dateibereich: `0x2CC3`–`0x2DD1` (Ende exklusiv)

Hilfetext:

> Der eingestellte Wert bestimmt die Lage der eingeastellten Vorlauf Fusspunkttemperatur.

<a id="datensatz-45"></a>

### 03-11 · Fusspunkt Vorlaufkennlinie: TA · Datensatz 45

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **20 °C** · Bereich: -10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF34C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1861` · Dateibereich: `0x2DD1`–`0x2EDF` (Ende exklusiv)

Hilfetext:

> Der eingestellte Wert bestimmt die Lage der eingeastellten Vorlauf Fusspunkttemperatur.

<a id="datensatz-46"></a>

### 03-20 · Zeitkonstante für Aussentemperaturmittelung · Datensatz 46

**Einstellebene 3, Raumtemperaturregelung** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **10 h** · Bereich: 0 … 20 · Schrittfeld (roh): 10

Adresskandidat: `0xF2D8` · Typcode: `13` · Einheitencode: `5` · Schlüssel: `0x1870` · Dateibereich: `0x2EDF`–`0x307C` (Ende exklusiv)

Hilfetext:

> Für die Sommer-/Winterumschaltung wird mit einer gemittelten Aussentemperatur gerechnet, welche die Trägheit des Gebäudes berücksichtigt.
> 0=keine
> 5h=leichte Bauweise
> 10h=mittelschwere Bauweise
> 20h=schwere Bauweise

<a id="datensatz-19"></a>

### 03-21 · Heizgrenze bei Tagbetrieb · Datensatz 19

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **16 °C** · Bereich: 0 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF032` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1050` · Dateibereich: `0x0F6F`–`0x10B6` (Ende exklusiv)

Hilfetext:

> Ist der Aussentemperatur Mittelwert grösser als der Einstelwert, schaltet der Heizbetrieb aus. Der Heizbetrieb schaltet wieder ein, wenn der Mittelwert um 2 K kleiner ist.

<a id="datensatz-20"></a>

### 03-21 · Heizgrenze bei Tagbetrieb · Datensatz 20

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **16 °C** · Bereich: 0 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF35A` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1051` · Dateibereich: `0x10B6`–`0x11FD` (Ende exklusiv)

Hilfetext:

> Ist der Aussentemperatur Mittelwert grösser als der Einstelwert, schaltet der Heizbetrieb aus. Der Heizbetrieb schaltet wieder ein, wenn der Mittelwert um 2 K kleiner ist.

<a id="datensatz-47"></a>

### 03-23 · Frostgrenze · Datensatz 47

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **2 °C** · Bereich: -10 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF03C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1880` · Dateibereich: `0x307C`–`0x31E3` (Ende exklusiv)

Hilfetext:

> Sinkt die Aussentemperatur unter den eingestellten Wert, wird die Frostschutzfunktion aktiv. Steigt die Aussentemperatur über den eingestellten Wert + 2K wird die Frostschutzfunktion deaktiviert.

<a id="datensatz-48"></a>

### 03-23 · Frostgrenze · Datensatz 48

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **2 °C** · Bereich: -10 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF364` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1881` · Dateibereich: `0x31E3`–`0x32E3` (Ende exklusiv)

Hilfetext:

> Liegt die Aussentemperatur unterhalb des Einstellwertes sind die Frostschutzfunktionen frei.

<a id="datensatz-49"></a>

### 03-30 · Nachstellzeit Raumregler · Datensatz 49

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 min** · Bereich: 0 … 200 · Schrittfeld (roh): 10

Adresskandidat: `0xF03E` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x1890` · Dateibereich: `0x32E3`–`0x3465` (Ende exklusiv)

Hilfetext:

> Mit der Nachstellzeit wird die Geschwindigkeit beeinflusst, mit der die Heizungseinrichtung eine Soll-/Istwertabweichung der Raumtemperatur ausregelt. Sie wirkt ergänzend zum eingestellten Raumeinfluss (3-7).

<a id="datensatz-50"></a>

### 03-30 · Nachstellzeit Raumregler · Datensatz 50

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 min** · Bereich: 0 … 200 · Schrittfeld (roh): 10

Adresskandidat: `0xF366` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x1891` · Dateibereich: `0x3465`–`0x35E7` (Ende exklusiv)

Hilfetext:

> Mit der Nachstellzeit wird die Geschwindigkeit beeinflusst, mit der die Heizungseinrichtung eine Soll-/Istwertabweichung der Raumtemperatur ausregelt. Sie wirkt ergänzend zum eingestellten Raumeinfluss (3-7).

<a id="datensatz-51"></a>

### 03-35 · Kühlgrenzenabstand · Datensatz 51

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **10 °C** · Bereich: 2 … 10 · Schrittfeld (roh): 5

Adresskandidat: `0xF014` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x18A0` · Dateibereich: `0x35E7`–`0x376A` (Ende exklusiv)

Hilfetext:

> Der Kühlgrenzenabstand plus die aktuelle Heizgrenze ergibt die Kühlgrenze. Der Kühlbetrieb wird gestartet,
> sobald die gemittelte Aussentemperatur die Kühlgrenze überschritten hat und 1K unter der Kühlgrenze beendet.

<a id="datensatz-52"></a>

### 03-35 · Kühlgrenzenabstand · Datensatz 52

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **5 °C** · Bereich: 2 … 10 · Schrittfeld (roh): 5

Adresskandidat: `0xF33C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x18A1` · Dateibereich: `0x376A`–`0x38ED` (Ende exklusiv)

Hilfetext:

> Der Kühlgrenzenabstand plus die aktuelle Heizgrenze ergibt die Kühlgrenze. Der Kühlbetrieb wird gestartet,
> sobald die gemittelte Aussentemperatur die Kühlgrenze überschritten hat und 1K unter der Kühlgrenze beendet.

<a id="datensatz-53"></a>

### 03-43 · Kühltemperatur · Datensatz 53

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **22 °C** · Bereich: 10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF010` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x18B0` · Dateibereich: `0x38ED`–`0x39E2` (Ende exklusiv)

Hilfetext:

> Die Kühltemperatur ist der Sollwert für die Heizkreistemperatur im Kühlbetrieb

<a id="datensatz-54"></a>

### 03-43 · Kühltemperatur · Datensatz 54

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **22 °C** · Bereich: 10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF338` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x18B1` · Dateibereich: `0x39E2`–`0x3AD7` (Ende exklusiv)

Hilfetext:

> Die Kühltemperatur ist der Sollwert für die Heizkreistemperatur im Kühlbetrieb

<a id="datensatz-1"></a>

### 03-50 · Betriebswahl Heizung und Brauchwasser · Datensatz 1

**Heizkreis 1 (abgeleitet)** · Einstellebene 1

Gespeichert: **1 ** · Bereich: 0 … 5 · Schrittfeld (roh): 1

Adresskandidat: `0xF00A` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x0800` · Dateibereich: `0x0002`–`0x0164` (Ende exklusiv)

Hilfetext:

> 0 = Standbybetrieb
> 1 = Automatik 1
> 2 = Normalbetrieb
> 3 = Reduziertbetrieb
> 4 = Sommerbetrieb
> 5 = Handbetrieb

<a id="datensatz-2"></a>

### 03-50 · Betriebswahl Heizung und Brauchwasser · Datensatz 2

**Heizkreis 2 (abgeleitet)** · Einstellebene 1

Gespeichert: **1 ** · Bereich: 0 … 5 · Schrittfeld (roh): 1

Adresskandidat: `0xF332` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x0801` · Dateibereich: `0x0164`–`0x02B9` (Ende exklusiv)

Hilfetext:

> 0 = Standbybetrieb
> 1 = Automatik 1
> 2 = Normalbetrieb
> 3 = Reduziertbetrieb
> 4 = Sommerbetrieb
> 5 = Handbetrieb

<a id="datensatz-9"></a>

### 03-51 · Sollwert Raumtemperatur Heizen Tag normal · Datensatz 9

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **20.5 °C** · Bereich: 10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF004` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1000` · Dateibereich: `0x071B`–`0x07F0` (Ende exklusiv)

Hilfetext:

> Raumtemperatur Sollwert für Normalbetrieb

<a id="datensatz-10"></a>

### 03-51 · Sollwert Raumtemperatur Heizen Tag normal · Datensatz 10

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **20.5 °C** · Bereich: 10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF32C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1001` · Dateibereich: `0x07F0`–`0x08C5` (Ende exklusiv)

Hilfetext:

> Raumtemperatur Sollwert für Normalbetrieb

<a id="datensatz-11"></a>

### 03-53 · Sollwert Raumteperatur Heizen Nacht · Datensatz 11

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **18 °C** · Bereich: 5 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF006` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1010` · Dateibereich: `0x08C5`–`0x099A` (Ende exklusiv)

Hilfetext:

> Raumtemperatur Sollwert für reduzierten Betrieb

<a id="datensatz-12"></a>

### 03-53 · Sollwert Raumteperatur Heizen Nacht · Datensatz 12

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **18 °C** · Bereich: 5 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF32E` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1011` · Dateibereich: `0x099A`–`0x0A6F` (Ende exklusiv)

Hilfetext:

> Raumtemperatur Sollwert für reduzierten Betrieb

<a id="datensatz-5"></a>

### 03-58 · Behaglichkeit · Datensatz 5

**Heizkreis 1 (abgeleitet)** · Einstellebene 1

Gespeichert: **0 K** · Bereich: -3 … 3 · Schrittfeld (roh): 5

Adresskandidat: `0xF00E` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x0820` · Dateibereich: `0x044F`–`0x0500` (Ende exklusiv)

Hilfetext:

> Anpassung der Raum Solltemperatur

<a id="datensatz-6"></a>

### 03-58 · Behaglichkeit · Datensatz 6

**Heizkreis 2 (abgeleitet)** · Einstellebene 1

Gespeichert: **-1 K** · Bereich: -3 … 3 · Schrittfeld (roh): 5

Adresskandidat: `0xF336` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x0821` · Dateibereich: `0x0500`–`0x05B1` (Ende exklusiv)

Hilfetext:

> Anpassung der Raum Solltemperatur

<a id="datensatz-7"></a>

### 03-60 · Partydauer HB · Datensatz 7

**Heizkreis 1 (abgeleitet)** · Einstellebene 1

Gespeichert: **0 min** · Bereich: 0 … 600 · Schrittfeld (roh): 5

Adresskandidat: `0xF00C` · Typcode: `0` · Einheitencode: `6` · Schlüssel: `0x0830` · Dateibereich: `0x05B1`–`0x0666` (Ende exklusiv)

Hilfetext:

> Zeitdauer für Partybetrieb in Minuten

<a id="datensatz-8"></a>

### 03-60 · Partydauer HB · Datensatz 8

**Heizkreis 2 (abgeleitet)** · Einstellebene 1

Gespeichert: **0 min** · Bereich: 0 … 600 · Schrittfeld (roh): 5

Adresskandidat: `0xF334` · Typcode: `0` · Einheitencode: `6` · Schlüssel: `0x0831` · Dateibereich: `0x0666`–`0x071B` (Ende exklusiv)

Hilfetext:

> Zeitdauer für Partybetrieb in Minuten

<a id="datensatz-59"></a>

### 04-00 · Fühlerkonfiguration speichern · Datensatz 59

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2DA` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2000` · Dateibereich: `0x3EDD`–`0x4072` (Ende exklusiv)

Hilfetext:

> Sind alle benötigten Fühler angeschlossen muss der Einsteller auf &quot;on&quot; gesetzt werden. Damit wird die Anlagenkonfiguration
> gespeichert und es werden Fehler generiert, sollte ein Fühlerwert nicht im definierten Bereich sein.

<a id="datensatz-60"></a>

### 04-02 · Funktion Sollwerteingang · Datensatz 60

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **0 ** · Bereich: 0 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF2D6` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2010` · Dateibereich: `0x4072`–`0x421E` (Ende exklusiv)

Hilfetext:

> Hier wird die Funktion Sollwerteingang einem Heizkreis oder der ganzen Anlage zugeordnet:
> 0 = Wärmeerzeuger
> 1 = Wärmeerzeuger (0 V = Standby, 1-8.5 V = 10-85 °C, 10 V = Kühlbetrieb)
> 2 = Heizkreis
> 3 = Keine Funktion
> 4 = Heizkreis (10 V = Standby)

<a id="datensatz-61"></a>

### 04-08 · Handbetrieb Konfiguration · Datensatz 61

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **2 ** · Bereich: 1 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0xF2DC` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2020` · Dateibereich: `0x421E`–`0x43A5` (Ende exklusiv)

Hilfetext:

> Welcher Wärmeerzeuger im Handbetrieb aktiviert werden soll, kann konfiguriert werden.
> 1 = Lokal (es wird nur der angewählte, reglerinterne WEZ aktiviert).
> 2 = Es werden alle über eBUS eingebundenen WEZ aktiviert.

<a id="datensatz-62"></a>

### 04-20 · Anlage-Hauptregler / Folgeregler · Datensatz 62

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **2 ** · Bereich: 0 … 25 · Schrittfeld (roh): 1

Adresskandidat: `0xF2E2` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2030` · Dateibereich: `0x43A5`–`0x454D` (Ende exklusiv)

Hilfetext:

> 0=kein Wärmemanagement
> 2=Masterregler
> 3=Folgeregler 1
> 4=Folgeregler 2
> 5=Folgeregler 3
> 17=Folgeregler 4
> 18=Folgeregler 5
> 19=Folgeregler 6
> 20=Folgeregler 7

<a id="datensatz-170"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 170

**Einstellebene 11, WE 1 Kaskadenfunktionen** · Einstellebene 11, WE 1 Kaskadenfunktionen

Gespeichert: **11 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF2EA` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5800` · Dateibereich: `0xC74E`–`0xC8BE` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-176"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 176

**Einstellebene 12, WE 2 Kaskadenfunktionen** · Einstellebene 12, WE 2 Kaskadenfunktionen

Gespeichert: **12 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF2F2` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x58A0` · Dateibereich: `0xCE1E`–`0xCF8E` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-182"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 182

**Einstellebene 13, WE 3 Kaskadenfunktionen** · Einstellebene 13, WE 3 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF2FA` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5940` · Dateibereich: `0xD4EE`–`0xD65E` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-188"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 188

**Einstellebene 14, WE 4 Kaskadenfunktionen** · Einstellebene 14, WE 4 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF302` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x59E0` · Dateibereich: `0xDBBE`–`0xDD2E` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-194"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 194

**Einstellebene 15, WE 5 Kaskadenfunktionen** · Einstellebene 15, WE 5 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF30A` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5A80` · Dateibereich: `0xE28E`–`0xE3FE` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-200"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 200

**Einstellebene 16, WE 6 Kaskadenfunktionen** · Einstellebene 16, WE 6 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF312` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5B20` · Dateibereich: `0xE95E`–`0xEACE` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-206"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 206

**Einstellebene 17, WE 7 Kaskadenfunktionen** · Einstellebene 17, WE 7 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF31A` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5BC0` · Dateibereich: `0xF02E`–`0xF19E` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-212"></a>

### 04-22 · WE 1 Zieladresse · Datensatz 212

**Einstellebene 18, WE 8 Kaskadenfunktionen** · Einstellebene 18, WE 8 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 24 · Schrittfeld (roh): 1

Adresskandidat: `0xF322` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5C60` · Dateibereich: `0xF6FE`–`0xF86E` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-115"></a>

### 04-27 · eBUS Adresse WEZ · Datensatz 115

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **11 ** · Bereich: 0 … 25 · Schrittfeld (roh): 1

Adresskandidat: `0xF252` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x4800` · Dateibereich: `0x8148`–`0x82BB` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-155"></a>

### 04-27 · eBUS Adresse WEZ · Datensatz 155

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **12 ** · Bereich: 0 … 25 · Schrittfeld (roh): 1

Adresskandidat: `0xF57A` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x5000` · Dateibereich: `0xB4DA`–`0xB659` (Ende exklusiv)

Hilfetext:

> 0 = kein WE
> 11 = Wärmeerzeuger 1
> 12 = Wärmeerzeuger 2
> 13 = Wärmeerzeuger 3
> 14 = Wärmeerzeuger 4
> 15 = Wärmeerzeuger 5
> 22 = Wärmeerzeuger 6
> 23 = Wärmeerzeuger 7
> 24 = Wärmeerzeuger 8

<a id="datensatz-63"></a>

### 04-30 · Multifunktionsusgang 1 · Datensatz 63

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **1 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2DE` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2040` · Dateibereich: `0x454D`–`0x466B` (Ende exklusiv)

Hilfetext:

> Heizkreispumpe 1
> 0 = Normale Funktion
> 1 = Heizkreipumpe läuft zusätzlich wenn Wärmeerzeugerpumpe läuft

<a id="datensatz-64"></a>

### 04-31 · Multifunktionsusgang 2 · Datensatz 64

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2E4` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2050` · Dateibereich: `0x466B`–`0x4789` (Ende exklusiv)

Hilfetext:

> Heizkreispumpe 2
> 0 = Normale Funktion
> 1 = Heizkreipumpe läuft zusätzlich wenn Wärmeerzeugerpumpe läuft

<a id="datensatz-65"></a>

### 04-36 · eBUS Speisung Abschaltung · Datensatz 65

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **1 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xFEAE` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x2060` · Dateibereich: `0x4789`–`0x4881` (Ende exklusiv)

Hilfetext:

> eBUS Speisung:
> 0 = abgeschaltet
> 1 = eBUS Speisung 50 mA aktiv

<a id="datensatz-66"></a>

### 04-40 · Service Passwort · Datensatz 66

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **161 ** · Bereich: 0 … 255 · Schrittfeld (roh): 1

Adresskandidat: `0xF2E6` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x2070` · Dateibereich: `0x4881`–`0x4971` (Ende exklusiv)

Hilfetext:

> Als Service Passwort kann ein Wert zwischen 0 und 255 eingestellt werden

<a id="datensatz-21"></a>

### 04-45 · Kommandobefehle · Datensatz 21

**Einstellebene 2** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 29 · Schrittfeld (roh): 1

Adresskandidat: `0x0A9D` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x1060` · Dateibereich: `0x11FD`–`0x12EC` (Ende exklusiv)

Hilfetext:

> Kommandobefehle:
> 0 = keine Funktion
> 9 = Geräte Reset
> 21 = Entriegelung
> 29 = Factory Reset

<a id="datensatz-67"></a>

### 04-60 · Mode Austrocknungsprogramm · Datensatz 67

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **0 ** · Bereich: 0 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0xFFC6` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x2080` · Dateibereich: `0x4971`–`0x4AAA` (Ende exklusiv)

Hilfetext:

> 0 = Austrocknungsprogramm beenden
> 1 = Austrocknungsprogramm für Heizkreis 1 starten
> 2 = Austrocknungsprogramm für Heizkreis 2 starten

<a id="datensatz-68"></a>

### 04-61 · Vorlaufsollwert-Steigung in der Aufheizphase · Datensatz 68

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **5 K** · Bereich: 0.5 … 20 · Schrittfeld (roh): 1

Adresskandidat: `0xFFC7` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x2090` · Dateibereich: `0x4AAA`–`0x4BB7` (Ende exklusiv)

Hilfetext:

> Vorlauf Sollwertsteigung für die Aufheizphase Austrocknungsprogramm [K/d]

<a id="datensatz-69"></a>

### 04-62 · Vorlaufsollwert-Abfall in der Abkühlphase · Datensatz 69

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **-5 K** · Bereich: -20 … -0.5 · Schrittfeld (roh): 1

Adresskandidat: `0xFFC9` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x20A0` · Dateibereich: `0x4BB7`–`0x4CC5` (Ende exklusiv)

Hilfetext:

> Vorlauf Sollwertabsenkung für die Auskühlphase im Austrocknungsprogramm [K/d]

<a id="datensatz-70"></a>

### 04-63 · Vorlaufsollwert in der Beharrungsphase · Datensatz 70

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **47 °C** · Bereich: 20 … 70 · Schrittfeld (roh): 1

Adresskandidat: `0xFFCB` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x20B0` · Dateibereich: `0x4CC5`–`0x4DC3` (Ende exklusiv)

Hilfetext:

> Vorlaufsollwert für die Beharrungsphase im Austrocknungsprogramm

<a id="datensatz-71"></a>

### 04-64 · Dauer der Beharrungsphase · Datensatz 71

**Einstellebene 4, Globale Einstellungen** · Einstellebene 4, Globale Einstellungen

Gespeichert: **30 ** · Bereich: 1 … 250 · Schrittfeld (roh): 1

Adresskandidat: `0xFFCD` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x20C0` · Dateibereich: `0x4DC3`–`0x4E9D` (Ende exklusiv)

Hilfetext:

> Zeitdauer für die Beharrungsphase [0.1 d]

<a id="datensatz-72"></a>

### 05-00 · Schaltdifferenz Brauchwasserbereitung · Datensatz 72

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **5 °C** · Bereich: 2 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF294` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x2800` · Dateibereich: `0x4E9D`–`0x4FD1` (Ende exklusiv)

Hilfetext:

> Unterschreitet die Warmwassertemperatur am Fühler TB den Sollwert um den Einstellwert wird die WW-Erwärmung
> aktiviert.

<a id="datensatz-73"></a>

### 05-01 · Temperaturüberhoehung Brauchwasserbereitung · Datensatz 73

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **6 °C** · Bereich: 2 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF296` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x2810` · Dateibereich: `0x4FD1`–`0x511B` (Ende exklusiv)

Hilfetext:

> Damit das Warmwasser effektiv und schnell erwärmt werden kann, ist eine Wärmeerzeuger-Überhöhung zum
> Warmwasser-Sollwert einzustellen.

<a id="datensatz-74"></a>

### 05-02 · Brauchwasser-Vorrang · Datensatz 74

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **0.1 ** · Bereich: 0 … 20 · Schrittfeld (roh): 1

Adresskandidat: `0xF292` · Typcode: `13` · Einheitencode: `0` · Schlüssel: `0x2820` · Dateibereich: `0x511B`–`0x529D` (Ende exklusiv)

Hilfetext:

> Das Warmwasser kann parallel, im Vorrang oder lastabhängig - parallel zu den Heizkreisen erwärmt werden.
> 0 = absoluter Vorrangbetrieb
> 0.1 = absoluter Parallelbetrieb
> 0.2 - 20.0 h = lastabhängiger Parallelbetrieb

<a id="datensatz-75"></a>

### 05-03 · Nachlaufzeit Brauchwasserbereitung · Datensatz 75

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **3 min** · Bereich: 0 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF298` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x2830` · Dateibereich: `0x529D`–`0x53B0` (Ende exklusiv)

Hilfetext:

> Die Ladepumpe läuft nach Beendigung einer Warmwasserladung um die eingestellte Zeit nach.

<a id="datensatz-76"></a>

### 05-04 · Legionellenschutztemperatur · Datensatz 76

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **60 °C** · Bereich: 60 … 80 · Schrittfeld (roh): 10

Adresskandidat: `0xF29A` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x2840` · Dateibereich: `0x53B0`–`0x54F3` (Ende exklusiv)

Hilfetext:

> Sollwert für die thermische Desinfektion (Legionellenschutz). Gilt während einer freigegeben thermischen Desinfektion
> für die Warmwasserladung.

<a id="datensatz-77"></a>

### 05-05 · Funktionsweise Ladepumpennachlauf · Datensatz 77

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **0 ** · Bereich: 0 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0xF2A0` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x2850` · Dateibereich: `0x54F3`–`0x5684` (Ende exklusiv)

Hilfetext:

> Konfiguration der Warmwasserbereitung.
> 0 = zeitabhängiger Pumpennachlauf gemäss Einstellwert 5-03
> 1 = Zeit- und Temperaturabhängiger Pumpennachlauf
> 2 = Warmwasserbereitung über eine separate Wärmepumpe an Klemme .

<a id="datensatz-78"></a>

### 05-06 · Zirkulationspumpe aktiv · Datensatz 78

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **1 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2A2` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x2860` · Dateibereich: `0x5684`–`0x578F` (Ende exklusiv)

Hilfetext:

> 0 = Funktion nicht aktiv
> 1 = Zirkulationspumpe aktiv gemäss eingestelltem Automatikprogramm

<a id="datensatz-79"></a>

### 05-07 · Stellglied Brauchwasserbereitung · Datensatz 79

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **1 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2A3` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x2870` · Dateibereich: `0x578F`–`0x588F` (Ende exklusiv)

Hilfetext:

> 0 = Warmwasserbereitung über Ladepumpe
> 1 = Warmwasserbereitung über ULV

<a id="datensatz-80"></a>

### 05-13 · Reduktion Sollwert TBO · Datensatz 80

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **15 K** · Bereich: 0 … 20 · Schrittfeld (roh): 10

Adresskandidat: `0xF2C2` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x2880` · Dateibereich: `0x588F`–`0x599C` (Ende exklusiv)

Hilfetext:

> Während einer Störung der Wärmepumpe wird der Sollwert TBO um den eingestellten Wert reduziert.

<a id="datensatz-55"></a>

### 05-14 · Legionellenschutzfunktion · Datensatz 55

**Einstellebene 3, Raumtemperaturregelung** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 ** · Bereich: 0 … 8 · Schrittfeld (roh): 1

Adresskandidat: `0xF29C` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x18C0` · Dateibereich: `0x3AD7`–`0x3C18` (Ende exklusiv)

Hilfetext:

> 0 = keine Legionellenschutzfunktion
> 1 = Montag
> 2 = Dienstag
> 3 = Mittwoch
> 4 = Donnerstag
> 5 = Freitag
> 6 = Samstag
> 7 = Sonntag
> 8 = täglich

<a id="datensatz-81"></a>

### 05-40 · Min. Fehlerdauer fuer Brauchwasser Störmeldung · Datensatz 81

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **0 h** · Bereich: 0 … 20 · Schrittfeld (roh): 10

Adresskandidat: `0xF2A4` · Typcode: `13` · Einheitencode: `5` · Schlüssel: `0x2890` · Dateibereich: `0x599C`–`0x5B17` (Ende exklusiv)

Hilfetext:

> Weicht die Brauchwassertemperatur während der Ladung innerhalb der eingestellten Zeit um mehr als 10 K vom Sollwert ab, wird eine Störung generiert. Einstellung 0=Funktion unwirksam

<a id="datensatz-13"></a>

### 05-51 · Sollwert Warmwassertemperatur · Datensatz 13

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **50 °C** · Bereich: 10 … 70 · Schrittfeld (roh): 10

Adresskandidat: `0xF008` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1020` · Dateibereich: `0x0A6F`–`0x0B33` (Ende exklusiv)

Hilfetext:

> Sollwert für Brauchwasser Temperatur

<a id="datensatz-14"></a>

### 05-51 · Sollwert Warmwassertemperatur · Datensatz 14

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **10 °C** · Bereich: 10 … 70 · Schrittfeld (roh): 10

Adresskandidat: `0xF330` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1021` · Dateibereich: `0x0B33`–`0x0BF7` (Ende exklusiv)

Hilfetext:

> Sollwert für Brauchwasser Temperatur

<a id="datensatz-22"></a>

### 05-60 · Partydauer WWB · Datensatz 22

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 min** · Bereich: 0 … 600 · Schrittfeld (roh): 5

Adresskandidat: `0xF00D` · Typcode: `0` · Einheitencode: `6` · Schlüssel: `0x1070` · Dateibereich: `0x12EC`–`0x13A2` (Ende exklusiv)

Hilfetext:

> Zeitdauer für Partybetrieb in Minuten

<a id="datensatz-23"></a>

### 05-60 · Partydauer WWB · Datensatz 23

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 min** · Bereich: 0 … 600 · Schrittfeld (roh): 5

Adresskandidat: `0xF335` · Typcode: `0` · Einheitencode: `6` · Schlüssel: `0x1071` · Dateibereich: `0x13A2`–`0x1458` (Ende exklusiv)

Hilfetext:

> Zeitdauer für Partybetrieb in Minuten

<a id="datensatz-83"></a>

### 06-00 · Brauchwasser Ladeleistung · Datensatz 83

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF2A8` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x3000` · Dateibereich: `0x5CA4`–`0x5E06` (Ende exklusiv)

Hilfetext:

> Ladeleistung die bei einer Warmwasserbereitung vom Wärmemanager angefordert wird.
> Anteil der gesamten Wärmeerzeuger-/Anlageleistung (Summe der Einstellebene 11 ÷ 18 Einsteller 11-02)

<a id="datensatz-84"></a>

### 06-01 · Puffer, Heiz-  Ladeleistung · Datensatz 84

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF2AA` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x3010` · Dateibereich: `0x5E06`–`0x5F18` (Ende exklusiv)

Hilfetext:

> Anteil der gesamten Wärmeerzeuger-/Anlageleistung (Summe der Einstellebene 11 ÷ 18 Einsteller 11-02)

<a id="datensatz-85"></a>

### 06-02 · Kühlleistung · Datensatz 85

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 5

Adresskandidat: `0xF2CA` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x3020` · Dateibereich: `0x5F18`–`0x6025` (Ende exklusiv)

Hilfetext:

> Die Kühlleistung dient dem Wärmemanager zur Berechnung der benötigten Leistung für die weiteren Wärmeerzeuger.

<a id="datensatz-86"></a>

### 06-04 · WEZ Überhöhung · Datensatz 86

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **10 K** · Bereich: 0 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF2AC` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3030` · Dateibereich: `0x6025`–`0x6147` (Ende exklusiv)

Hilfetext:

> Hier wird die Überhöhung Wärmeerzeugersollwert zum Puffer Oben TPO oder Hauptvorlauffühler TKx eingestellt. (TWV zu TPO oder TKx)

<a id="datensatz-87"></a>

### 06-05 · Puffer Offset TPM aus · Datensatz 87

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **0 K** · Bereich: -10 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF2AE` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3040` · Dateibereich: `0x6147`–`0x6233` (Ende exklusiv)

Hilfetext:

> Sollwertreduktion für das Beenden der Pufferladung am Abschaltfühler

<a id="datensatz-88"></a>

### 06-08 · TBVsoll Überhöhung · Datensatz 88

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **10 K** · Bereich: 0 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF2B2` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3050` · Dateibereich: `0x6233`–`0x631A` (Ende exklusiv)

Hilfetext:

> Notwendige Wärmeerzeuger Temperaturerhöhung bei Brauchwasserladung

<a id="datensatz-89"></a>

### 06-10 · Xp WEZ Manager · Datensatz 89

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **3 K** · Bereich: 2 … 100 · Schrittfeld (roh): 5

Adresskandidat: `0xF2B4` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3060` · Dateibereich: `0x631A`–`0x63FC` (Ende exklusiv)

Hilfetext:

> Gibt an, bei welcher Soll-Ist Abweichung der Stellbefehl 100% ist

<a id="datensatz-90"></a>

### 06-11 · Tn WEZ Manager · Datensatz 90

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **20 min** · Bereich: 0 … 100 · Schrittfeld (roh): 10

Adresskandidat: `0xF2B6` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x3070` · Dateibereich: `0x63FC`–`0x6507` (Ende exklusiv)

Hilfetext:

> Die Stellgrösse wird innerhalb der eingestellten Zeit verdoppelt, wenn die Regelabweichung kostant bleibt.

<a id="datensatz-91"></a>

### 06-12 · Tv WEZ Manager · Datensatz 91

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **0 s?** · Bereich: 0 … 100 · Schrittfeld (roh): 10

Adresskandidat: `0xF2B8` · Typcode: `13` · Einheitencode: `7` · Schlüssel: `0x3080` · Dateibereich: `0x6507`–`0x668D` (Ende exklusiv)

Hilfetext:

> Mit der Vorhaltezeit kann dem Wärmemanager ein Differential Anteil zugeordnet werden. Die aktuelle Steigung der Puffer- oder Hauptvorlauftemperatur mit der Vorhaltezeit multipliziert ergibt eine theoretische Sollwertverschiebung.

<a id="datensatz-92"></a>

### 06-13 · Reduktion Sollwert TKX · Datensatz 92

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **5 K** · Bereich: 0 … 25 · Schrittfeld (roh): 10

Adresskandidat: `0xF2C0` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3090` · Dateibereich: `0x668D`–`0x679E` (Ende exklusiv)

Hilfetext:

> Während einer Störung der Wärmepumpe wird der Sollwert TWR oder TKX um den eingestellten Wert reduziert.

<a id="datensatz-93"></a>

### 06-20 · Sequenzwechsel Flag · Datensatz 93

**Einstellebene 6, WM-Einstellungen** · Einstellebene 6, WM-Einstellungen

Gespeichert: **0 ** · Bereich: 0 … 8 · Schrittfeld (roh): 1

Adresskandidat: `0xF2E0` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x30A0` · Dateibereich: `0x679E`–`0x693F` (Ende exklusiv)

Hilfetext:

> 0=kein Folgewechsel
> 1=Folgewechsel nach 1 Woche
> 2=Folgewechsel nach 2 Wochen
> 3=Folgewechsel nach 3 Wochen
> 4=Folgewechsel nach 4 Wochen
> 5=Folgewechsel nach 5 Wochen
> 6=Folgewechsel nach 6 Wochen
> 7=Folgewechsel nach 7 Wochen
> 8=Folgewechsel sofort

<a id="datensatz-94"></a>

### 07-00 · Proportional-Bereich Mischer · Datensatz 94

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **15 K** · Bereich: 5 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF028` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3800` · Dateibereich: `0x693F`–`0x6A2F` (Ende exklusiv)

Hilfetext:

> Gibt an, bei welcher Soll-Ist Abweichung der Stellbefehl 100% ist

<a id="datensatz-95"></a>

### 07-00 · Proportional-Bereich Mischer · Datensatz 95

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **15 K** · Bereich: 5 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF350` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3801` · Dateibereich: `0x6A2F`–`0x6B1F` (Ende exklusiv)

Hilfetext:

> Gibt an, bei welcher Soll-Ist Abweichung der Stellbefehl 100% ist

<a id="datensatz-96"></a>

### 07-01 · Überhöhung WE-Temperatur · Datensatz 96

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 K** · Bereich: 0 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF020` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3810` · Dateibereich: `0x6B1F`–`0x6C03` (Ende exklusiv)

Hilfetext:

> Überhöhung der Sollwertanforderung an den Wärmeverteiler.

<a id="datensatz-97"></a>

### 07-01 · Überhöhung WE-Temperatur · Datensatz 97

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **3 K** · Bereich: 0 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF348` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3811` · Dateibereich: `0x6C03`–`0x6CE7` (Ende exklusiv)

Hilfetext:

> Überhöhung der Sollwertanforderung an den Wärmeverteiler.

<a id="datensatz-98"></a>

### 07-02 · Minimale Vorlauftemperatur · Datensatz 98

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 °C** · Bereich: 0 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF01C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x3820` · Dateibereich: `0x6CE7`–`0x6DD9` (Ende exklusiv)

Hilfetext:

> Vorlauf Minimaltemperatur (ist wirksam, wenn Heizgrenzen nicht aktiv)

<a id="datensatz-99"></a>

### 07-02 · Minimale Vorlauftemperatur · Datensatz 99

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 °C** · Bereich: 0 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF344` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x3821` · Dateibereich: `0x6DD9`–`0x6ECB` (Ende exklusiv)

Hilfetext:

> Vorlauf Minimaltemperatur (ist wirksam, wenn Heizgrenzen nicht aktiv)

<a id="datensatz-100"></a>

### 07-03 · Pumpennachlauf Heizkreis · Datensatz 100

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **15 min** · Bereich: 0 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF02C` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x3830` · Dateibereich: `0x6ECB`–`0x6FCB` (Ende exklusiv)

Hilfetext:

> Nach Abschaltung des Heizkreises läuft die Umwälzpumpe um die eingestellte Zeit nach.

<a id="datensatz-101"></a>

### 07-03 · Pumpennachlauf Heizkreis · Datensatz 101

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **15 min** · Bereich: 0 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF354` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x3831` · Dateibereich: `0x6FCB`–`0x70CB` (Ende exklusiv)

Hilfetext:

> Nach Abschaltung des Heizkreises läuft die Umwälzpumpe um die eingestellte Zeit nach.

<a id="datensatz-102"></a>

### 07-05 · Heizkreistyp · Datensatz 102

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **2 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF02A` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x3840` · Dateibereich: `0x70CB`–`0x71DF` (Ende exklusiv)

Hilfetext:

> 0 = 3 Punkt Mischer
> 1 = 2 Punkt Mischer
> 2 = Pumpenkreis
> 3 = Kein Heizkreis
> 4 = Taktbetrieb, wenn WE abgeschaltet

<a id="datensatz-103"></a>

### 07-05 · Heizkreistyp · Datensatz 103

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF352` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x3841` · Dateibereich: `0x71DF`–`0x72F3` (Ende exklusiv)

Hilfetext:

> 0 = 3 Punkt Mischer
> 1 = 2 Punkt Mischer
> 2 = Pumpenkreis
> 3 = Kein Heizkreis
> 4 = Taktbetrieb, wenn WE abgeschaltet

<a id="datensatz-104"></a>

### 07-06 · Min. Fehlerdauer fuer Vorlauf-Störmeldung · Datensatz 104

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 h** · Bereich: 0 … 20 · Schrittfeld (roh): 10

Adresskandidat: `0xF040` · Typcode: `13` · Einheitencode: `5` · Schlüssel: `0x3850` · Dateibereich: `0x72F3`–`0x742B` (Ende exklusiv)

Hilfetext:

> Weicht die Isttemperatur über die eingestellte Zeit um mehr als 5 K vom Sollwert ab, wird eine eBUS Fehlermeldung generiert.

<a id="datensatz-105"></a>

### 07-06 · Min. Fehlerdauer fuer Vorlauf-Störmeldung · Datensatz 105

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 h** · Bereich: 0 … 20 · Schrittfeld (roh): 10

Adresskandidat: `0xF368` · Typcode: `13` · Einheitencode: `5` · Schlüssel: `0x3851` · Dateibereich: `0x742B`–`0x75AA` (Ende exklusiv)

Hilfetext:

> Sinkt die Aussentemperatur unter den eingestellten Wert, wird die Frostschutzfunktion aktiv. Steigt die Aussentemperatur über den eingestellten Wert + 2K wird die Frostschutzfunktion deaktiviert.

<a id="datensatz-17"></a>

### 07-08 · Vorlauf Maximaltemperatur TV · Datensatz 17

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **55 °C** · Bereich: 10 … 90 · Schrittfeld (roh): 10

Adresskandidat: `0xF01E` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1040` · Dateibereich: `0x0DCF`–`0x0E9F` (Ende exklusiv)

Hilfetext:

> Maximal möglicher Sollwert für Vorlauftemperatur.

<a id="datensatz-18"></a>

### 07-08 · Vorlauf Maximaltemperatur TV · Datensatz 18

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **45 °C** · Bereich: 10 … 90 · Schrittfeld (roh): 10

Adresskandidat: `0xF346` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x1041` · Dateibereich: `0x0E9F`–`0x0F6F` (Ende exklusiv)

Hilfetext:

> Maximal möglicher Sollwert für Vorlauftemperatur.

<a id="datensatz-106"></a>

### 07-14 · Heizkreisfunktion im Kühlbetrieb · Datensatz 106

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF012` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x3860` · Dateibereich: `0x75AA`–`0x76ED` (Ende exklusiv)

Hilfetext:

> 0 = Mischer für Heizbetrieb ohne Kühlbetrieb
> 1 = Mischer zu im Kühlbetrieb
> 2 = Mischer auf im Kühlbetrieb
> 3 = Mischer geregelt im Kühlbetrieb

<a id="datensatz-107"></a>

### 07-14 · Heizkreisfunktion im Kühlbetrieb · Datensatz 107

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF33A` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x3861` · Dateibereich: `0x76ED`–`0x7830` (Ende exklusiv)

Hilfetext:

> 0 = Mischer für Heizbetrieb ohne Kühlbetrieb
> 1 = Mischer zu im Kühlbetrieb
> 2 = Mischer auf im Kühlbetrieb
> 3 = Mischer geregelt im Kühlbetrieb

<a id="datensatz-108"></a>

### 07-31 · Heizkreisüberhöhung Niedertarif · Datensatz 108

**Heizkreis 1 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 K** · Bereich: 0 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF042` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3870` · Dateibereich: `0x7830`–`0x7A74` (Ende exklusiv)

Hilfetext:

> Ist die Zirkulationspumpe inaktiv, kann die Heizkreistemperatur, im günstigen Niedertarif, um den hier eingestellten Wert erhöht werden.
> Dadurch kann bei einer Fussbodenheizung ohne Pufferspeicher zusätzliche Energie in den Fussboden gebracht werden.
> Als Niedertarifzeit gilt das eingestellte Zirkulationspumpen Zeitprogramm.
> Bei einem Pufferspeicher wird der Sollwert TPO um diesen Wert erhöht.

<a id="datensatz-109"></a>

### 07-31 · Heizkreisüberhöhung Niedertarif · Datensatz 109

**Heizkreis 2 (abgeleitet)** · Einstellebene 7 Heizkreisregelung

Gespeichert: **0 K** · Bereich: 0 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF36A` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x3871` · Dateibereich: `0x7A74`–`0x7B73` (Ende exklusiv)

Hilfetext:

> Die Temperaturabweichung für für die Fehlermeldung kann hier verändert werden

<a id="datensatz-110"></a>

### 08-55 · Puffer aktiv · Datensatz 110

**Einstellebene 8, Solar- und Speicherfunktionen** · Einstellebene 8, Solar- und Speicherfunktionen

Gespeichert: **0 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF2C6` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x4000` · Dateibereich: `0x7B73`–`0x7CE1` (Ende exklusiv)

Hilfetext:

> 0 = kein Pufferspeicher
> 1 = Pufferspeicher ohne Warmwassereinsatz (kein TB)
> 2 = Pufferspeicher mit integriertem Warmwassereinsatz oder externem WW-Speicher der über den Puffer erwärmt wird

<a id="datensatz-111"></a>

### 08-58 · Puffer Minimaltemperatur · Datensatz 111

**Einstellebene 8, Solar- und Speicherfunktionen** · Einstellebene 8, Solar- und Speicherfunktionen

Gespeichert: **0 °C** · Bereich: 0 … 80 · Schrittfeld (roh): 10

Adresskandidat: `0xF2BE` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4010` · Dateibereich: `0x7CE1`–`0x7DF3` (Ende exklusiv)

Hilfetext:

> Die minimale Puffer Solltemperatur ist immer im Heiz- oder Brauchwasser Ladebetrieb aktiv.

<a id="datensatz-112"></a>

### 08-59 · Puffer Maximaltemperatur · Datensatz 112

**Einstellebene 8, Solar- und Speicherfunktionen** · Einstellebene 8, Solar- und Speicherfunktionen

Gespeichert: **90 °C** · Bereich: 60 … 100 · Schrittfeld (roh): 10

Adresskandidat: `0xF2D0` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4020` · Dateibereich: `0x7DF3`–`0x7ED5` (Ende exklusiv)

Hilfetext:

> Maximal mögliche Puffer Abschalttemperatur

<a id="datensatz-113"></a>

### 08-72 · Delta Puffer bei Solar aktiv · Datensatz 113

**Einstellebene 8, Solar- und Speicherfunktionen** · Einstellebene 8, Solar- und Speicherfunktionen

Gespeichert: **40 K** · Bereich: 0 … 40 · Schrittfeld (roh): 10

Adresskandidat: `0xF2CE` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4030` · Dateibereich: `0x7ED5`–`0x8007` (Ende exklusiv)

Hilfetext:

> Der Puffer-Sollwert wird, wenn der solare Ertrag auf über 50 % Solarleistung ist, um den eingestellten Wert reduziert.

<a id="datensatz-114"></a>

### 08-79 · WW Minimaltemperatur bei Solar aktiv · Datensatz 114

**Einstellebene 8, Solar- und Speicherfunktionen** · Einstellebene 8, Solar- und Speicherfunktionen

Gespeichert: **10 K** · Bereich: 0 … 60 · Schrittfeld (roh): 10

Adresskandidat: `0xF2CC` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4040` · Dateibereich: `0x8007`–`0x8148` (Ende exklusiv)

Hilfetext:

> Der Warmwasser - Sollwert wird, wenn der solare Ertrag auf über 50 % Solarleistung ist, auf den eingestellten Wert reduziert.

<a id="datensatz-116"></a>

### 09-00 · Nachlaufzeit Schutzfunktion · Datensatz 116

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **1 min** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF258` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x4810` · Dateibereich: `0x82BB`–`0x83C6` (Ende exklusiv)

Hilfetext:

> Die Wärmeerzeugerpumpe und wenn vorhanden der Mischer laufen um diese Zeit weiter.

<a id="datensatz-156"></a>

### 09-00 · Nachlaufzeit Schutzfunktion · Datensatz 156

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **1 min** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF580` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x5010` · Dateibereich: `0xB659`–`0xB770` (Ende exklusiv)

Hilfetext:

> Die Wärmeerzeugerpumpe und wenn vorhanden der Mischer laufen um diese Zeit weiter.

<a id="datensatz-117"></a>

### 09-04 · Vorlaufzeit Quellenpumpe · Datensatz 117

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0.5 min** · Bereich: 0 … 300 · Schrittfeld (roh): 5

Adresskandidat: `0xF254` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x4820` · Dateibereich: `0x83C6`–`0x852F` (Ende exklusiv)

Hilfetext:

> Einschaltverzögerung des Wärmeerzeugers nach einer Wärmeanforderung. Dies entspricht auch der Vorlaufzeit Quellenpumpe oder Gebläse, da diese mit der Wärmeanforderung einschalten.

<a id="datensatz-157"></a>

### 09-04 · Einschaltverzögerung · Datensatz 157

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **0.5 min** · Bereich: 0 … 300 · Schrittfeld (roh): 5

Adresskandidat: `0xF57C` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x5020` · Dateibereich: `0xB770`–`0xB8E1` (Ende exklusiv)

Hilfetext:

> Einschaltverzögerung des Wärmeerzeugers nach einer Wärmeanforderung. Dies entspricht auch der Vorlaufzeit Quellenpumpe oder Gebläse, da diese mit der Wärmeanforderung einschalten.

<a id="datensatz-118"></a>

### 09-07 · WEZ Typ · Datensatz 118

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **5 ** · Bereich: 0 … 6 · Schrittfeld (roh): 1

Adresskandidat: `0xF250` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x4830` · Dateibereich: `0x852F`–`0x86C2` (Ende exklusiv)

Hilfetext:

> 0 = kein Wärmeerzeuger aktiv
> 1 = Zusatzwärmeerzeuger 1-stufig (Elektroheizung)
> 2 = Funktion nicht verfügbar
> 3 = Funktion nicht verfügbar
> 4 = Funktion nicht verfügbar
> 5 = Wärmepumpe ohne Kühlfunktion
> 6 = Wärmepumpe mit Kühlfunktion

<a id="datensatz-158"></a>

### 09-07 · WEZ Typ · Datensatz 158

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **1 ** · Bereich: 0 … 6 · Schrittfeld (roh): 1

Adresskandidat: `0xF578` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x5030` · Dateibereich: `0xB8E1`–`0xBA80` (Ende exklusiv)

Hilfetext:

> 0 = kein Wärmeerzeuger aktiv
> 1 = Zusatzwärmeerzeuger 1-stufig (Elektroheizung)
> 2 = Funktion nicht verfügbar
> 3 = Funktion nicht verfügbar
> 4 = Funktion nicht verfügbar
> 5 = Wärmepumpe ohne Kühlfunktion
> 6 = Wärmepumpe mit Kühlfunktion

<a id="datensatz-56"></a>

### 09-08 · Wärmeerzeuger Sperre · Datensatz 56

**Einstellebene 3, Raumtemperaturregelung** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **0 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF2D4` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x18D0` · Dateibereich: `0x3C18`–`0x3D25` (Ende exklusiv)

Hilfetext:

> 0=keine Sperre
> 1=WE1 (WP) gesperrt
> 2=WE2 (E-Heizung) gesperrt
> 3=WE1 und WE2 gesperrt

<a id="datensatz-119"></a>

### 09-11 · Bedingte WEZ Freigabe · Datensatz 119

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0 ** · Bereich: 0 … 13 · Schrittfeld (roh): 1

Adresskandidat: `0xF27C` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x4840` · Dateibereich: `0x86C2`–`0x882B` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sperre.
> 1 = Wärmeerzeuger gesperrt.
> 2 = gesperrt wenn die Aussentemp. unter den Wert in 11-1 - 2K sinkt.
> 3 = gesperrt wenn die Aussentemp. über den Wert in 11-1 steigt.

<a id="datensatz-159"></a>

### 09-11 · Bedingte WEZ Freigabe · Datensatz 159

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **10 ** · Bereich: 0 … 13 · Schrittfeld (roh): 1

Adresskandidat: `0xF5A4` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x5040` · Dateibereich: `0xBA80`–`0xBB47` (Ende exklusiv)

Hilfetext:

> 0 = frei

<a id="datensatz-120"></a>

### 09-12 · Aussentemperatursperre TAW · Datensatz 120

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-50 °C** · Bereich: -50 … 50 · Schrittfeld (roh): 5

Adresskandidat: `0xF27E` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4850` · Dateibereich: `0x882B`–`0x8985` (Ende exklusiv)

Hilfetext:

> Aussentemperatur bei der die Sperrung des Wärmeerzeugers erfolgt.Die Sperrung erfolgt abhängig dem Wert im Einsteller 11-0 über oder unter dem eingestellten Wert.

<a id="datensatz-160"></a>

### 09-12 · Aussentemperatursperre TAW · Datensatz 160

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **-5 °C** · Bereich: -50 … 50 · Schrittfeld (roh): 5

Adresskandidat: `0xF5A6` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x5050` · Dateibereich: `0xBB47`–`0xBCAD` (Ende exklusiv)

Hilfetext:

> Aussentemperatur bei der die Sperrung des Wärmeerzeugers erfolgt.Die Sperrung erfolgt abhängig dem Wert im Einsteller 11-0 über oder unter dem eingestellten Wert.

<a id="datensatz-121"></a>

### 09-13 · Energiezwang Funktion · Datensatz 121

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **2 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF280` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x4860` · Dateibereich: `0x8985`–`0x8AD9` (Ende exklusiv)

Hilfetext:

> 0 = Kein Energiezwang
> 1 = Energiezwang auf Schutztemperatur
> 2 = Energiezwang auf Maximaltemperatur
> 3 = Energiezwang auf Schutztemperatur und Maximaltemperatur

<a id="datensatz-161"></a>

### 09-13 · Energiezwang Funktion · Datensatz 161

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **2 ** · Bereich: 0 … 3 · Schrittfeld (roh): 1

Adresskandidat: `0xF5A8` · Typcode: `4` · Einheitencode: `0` · Schlüssel: `0x5060` · Dateibereich: `0xBCAD`–`0xBE0D` (Ende exklusiv)

Hilfetext:

> 0 = Kein Energiezwang
> 1 = Energiezwang auf Schutztemperatur
> 2 = Energiezwang auf Maximaltemperatur
> 3 = Energiezwang auf Schutztemperatur und Maximaltemperatur

<a id="datensatz-122"></a>

### 09-14 · Diff. Leistungszwang Tkmax · Datensatz 122

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0 K** · Bereich: -30 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF282` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4870` · Dateibereich: `0x8AD9`–`0x8BF4` (Ende exklusiv)

Hilfetext:

> Die Ansprechtemperatur für positiven Leistungszwang wird gegenüber TKmax um diesen Wert verschoben.

<a id="datensatz-162"></a>

### 09-14 · Diff. Leistungszwang Tkmax · Datensatz 162

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **0 K** · Bereich: -30 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF5AA` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x5070` · Dateibereich: `0xBE0D`–`0xBF34` (Ende exklusiv)

Hilfetext:

> Die Ansprechtemperatur für positiven Leistungszwang wird gegenüber TKmax um diesen Wert verschoben.

<a id="datensatz-57"></a>

### 09-20 · Solltemperatur Handbetrieb · Datensatz 57

**Heizkreis 1 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **48 °C** · Bereich: 0 … 90 · Schrittfeld (roh): 10

Adresskandidat: `0xFE9C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x18E0` · Dateibereich: `0x3D25`–`0x3E01` (Ende exklusiv)

Hilfetext:

> Sollwert Vorlauftemperatur im Handbetrieb

<a id="datensatz-58"></a>

### 09-20 · Solltemperatur Handbetrieb · Datensatz 58

**Heizkreis 2 (abgeleitet)** · Einstellebene 3, Raumtemperaturregelung

Gespeichert: **48 °C** · Bereich: 0 … 90 · Schrittfeld (roh): 10

Adresskandidat: `0xFE9E` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x18E1` · Dateibereich: `0x3E01`–`0x3EDD` (Ende exklusiv)

Hilfetext:

> Sollwert Vorlauftemperatur im Handbetrieb

<a id="datensatz-123"></a>

### 09-21 · WE Abschaltdifferenz · Datensatz 123

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **5 K** · Bereich: 2 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF268` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4880` · Dateibereich: `0x8BF4`–`0x8D0D` (Ende exklusiv)

Hilfetext:

> Wird am Fühler TWV die Temperatur TWVSoll + Einstellwert überschritten, schaltet der Wärmeerzeuger aus.

<a id="datensatz-163"></a>

### 09-21 · WE Abschaltdifferenz · Datensatz 163

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **3 K** · Bereich: 2 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF590` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x5080` · Dateibereich: `0xBF34`–`0xC059` (Ende exklusiv)

Hilfetext:

> Wird am Fühler TWV die Temperatur TWVSoll + Einstellwert überschritten, schaltet der Wärmeerzeuger aus.

<a id="datensatz-124"></a>

### 09-23 · Minimale Stillstandszeit · Datensatz 124

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **12 min** · Bereich: 0 … 100 · Schrittfeld (roh): 5

Adresskandidat: `0xF25A` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x4890` · Dateibereich: `0x8D0D`–`0x8E05` (Ende exklusiv)

Hilfetext:

> Minimale Stillstandzeit des Wärmeerzeugers nach einer Abschaltung.

<a id="datensatz-164"></a>

### 09-23 · Minimale Stillstandszeit · Datensatz 164

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **60 min** · Bereich: 0 … 100 · Schrittfeld (roh): 5

Adresskandidat: `0xF582` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x5090` · Dateibereich: `0xC059`–`0xC15D` (Ende exklusiv)

Hilfetext:

> Minimale Stillstandzeit des Wärmeerzeugers nach einer Abschaltung.

<a id="datensatz-125"></a>

### 09-26 · Vorhaltezeit 2. Stufe · Datensatz 125

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **10 s?** · Bereich: 0 … 100 · Schrittfeld (roh): 10

Adresskandidat: `0xF25E` · Typcode: `13` · Einheitencode: `7` · Schlüssel: `0x48A0` · Dateibereich: `0x8E05`–`0x8F58` (Ende exklusiv)

Hilfetext:

> Bei Modulations- und 2-stufigem Betrieb kann eine Vorhaltezeit (D-Anteil) für die Modulation eingestellt
> werden. Optimierung um ein Überschwingen zu vermeiden.

<a id="datensatz-165"></a>

### 09-26 · Vorhaltezeit 2. Stufe · Datensatz 165

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **0 s?** · Bereich: 0 … 100 · Schrittfeld (roh): 10

Adresskandidat: `0xF586` · Typcode: `13` · Einheitencode: `7` · Schlüssel: `0x50A0` · Dateibereich: `0xC15D`–`0xC2BC` (Ende exklusiv)

Hilfetext:

> Bei Modulations- und 2-stufigem Betrieb kann eine Vorhaltezeit (D-Anteil) für die Modulation eingestellt
> werden. Optimierung um ein Überschwingen zu vermeiden.

<a id="datensatz-126"></a>

### 09-31 · Minimale WE Laufzeit · Datensatz 126

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **9 min** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF256` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x48B0` · Dateibereich: `0x8F58`–`0x9043` (Ende exklusiv)

Hilfetext:

> Minimale Laufzeit des Wärmeerzeugers nach einer Freigabe.

<a id="datensatz-166"></a>

### 09-31 · Minimale WE Laufzeit · Datensatz 166

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **0 min** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF57E` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x50B0` · Dateibereich: `0xC2BC`–`0xC3B3` (Ende exklusiv)

Hilfetext:

> Minimale Laufzeit des Wärmeerzeugers nach einer Freigabe.

<a id="datensatz-127"></a>

### 09-32 · TWVmin Kühlbetrieb · Datensatz 127

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **14 °C** · Bereich: 0 … 30 · Schrittfeld (roh): 10

Adresskandidat: `0xF26C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x48C0` · Dateibereich: `0x9043`–`0x9162` (Ende exklusiv)

Hilfetext:

> Unterschreitet der Wärmepumpen Vorlauffühler im Kühlbetrieb diese Temperatur, wird die Wärmepume abgeschaltet.

<a id="datensatz-128"></a>

### 09-34 · Einschaltverzögerung 2. Stufe · Datensatz 128

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **9 min** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF260` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x48D0` · Dateibereich: `0x9162`–`0x92AE` (Ende exklusiv)

Hilfetext:

> Mit der Einschaltverzögerung kann der Einschaltzeitpunkt der zweiten Stufe um die eingestellte Zeit ab Wärmeerzeugeranforderung verzögert werden.

<a id="datensatz-167"></a>

### 09-34 · Einschaltverzögerung 2. Stufe · Datensatz 167

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **0 min** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF588` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x50C0` · Dateibereich: `0xC3B3`–`0xC50B` (Ende exklusiv)

Hilfetext:

> Mit der Einschaltverzögerung kann der Einschaltzeitpunkt der zweiten Stufe um die eingestellte Zeit ab Wärmeerzeugeranforderung verzögert werden.

<a id="datensatz-129"></a>

### 09-35 · Schaltdifferenz 2. Stufe · Datensatz 129

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-3 K** · Bereich: -20 … 0 · Schrittfeld (roh): 5

Adresskandidat: `0xF25C` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x48E0` · Dateibereich: `0x92AE`–`0x93D4` (Ende exklusiv)

Hilfetext:

> Bei 1-stufigem Betrieb ist dieser Einsteller auf 0 zu belassen.
> Schaltdifferenz für die 2. Stufe -1.0 bis -20.0

<a id="datensatz-168"></a>

### 09-35 · Schaltdifferenz 2. Stufe · Datensatz 168

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **0 K** · Bereich: -20 … 0 · Schrittfeld (roh): 5

Adresskandidat: `0xF584` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x50D0` · Dateibereich: `0xC50B`–`0xC63D` (Ende exklusiv)

Hilfetext:

> Bei 1-stufigem Betrieb ist dieser Einsteller auf 0 zu belassen.
> Schaltdifferenz für die 2. Stufe -1.0 bis -20.0

<a id="datensatz-130"></a>

### 10-31 · WE Maximaltemperatur · Datensatz 130

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **70 °C** · Bereich: 30 … 80 · Schrittfeld (roh): 10

Adresskandidat: `0xF266` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x48F0` · Dateibereich: `0x93D4`–`0x94D9` (Ende exklusiv)

Hilfetext:

> Wird die maximale Wärmeerzeugertemperatur überschritten, wird der WEZ abgeschaltet.

<a id="datensatz-169"></a>

### 10-31 · WE Maximaltemperatur · Datensatz 169

**Einstellebene 10, WE Einstellungen Elektro Zusatzheizung** · Einstellebene 10, WE Einstellungen Elektro Zusatzheizung

Gespeichert: **70 °C** · Bereich: 30 … 80 · Schrittfeld (roh): 10

Adresskandidat: `0xF58E` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x50E0` · Dateibereich: `0xC63D`–`0xC74E` (Ende exklusiv)

Hilfetext:

> Wird die maximale Wärmeerzeugertemperatur überschritten, wird der WEZ abgeschaltet.

<a id="datensatz-171"></a>

### 11-01 · WE Steuerbefehl · Datensatz 171

**Einstellebene 11, WE 1 Kaskadenfunktionen** · Einstellebene 11, WE 1 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF2EB` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5810` · Dateibereich: `0xC8BE`–`0xCA22` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-177"></a>

### 11-01 · WE Steuerbefehl · Datensatz 177

**Einstellebene 12, WE 2 Kaskadenfunktionen** · Einstellebene 12, WE 2 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF2F3` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x58B0` · Dateibereich: `0xCF8E`–`0xD0F2` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-183"></a>

### 11-01 · WE Steuerbefehl · Datensatz 183

**Einstellebene 13, WE 3 Kaskadenfunktionen** · Einstellebene 13, WE 3 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF2FB` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5950` · Dateibereich: `0xD65E`–`0xD7C2` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-189"></a>

### 11-01 · WE Steuerbefehl · Datensatz 189

**Einstellebene 14, WE 4 Kaskadenfunktionen** · Einstellebene 14, WE 4 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF303` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x59F0` · Dateibereich: `0xDD2E`–`0xDE92` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-195"></a>

### 11-01 · WE Steuerbefehl · Datensatz 195

**Einstellebene 15, WE 5 Kaskadenfunktionen** · Einstellebene 15, WE 5 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF30B` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5A90` · Dateibereich: `0xE3FE`–`0xE562` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-201"></a>

### 11-01 · WE Steuerbefehl · Datensatz 201

**Einstellebene 16, WE 6 Kaskadenfunktionen** · Einstellebene 16, WE 6 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF313` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5B30` · Dateibereich: `0xEACE`–`0xEC32` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-207"></a>

### 11-01 · WE Steuerbefehl · Datensatz 207

**Einstellebene 17, WE 7 Kaskadenfunktionen** · Einstellebene 17, WE 7 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF31B` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5BD0` · Dateibereich: `0xF19E`–`0xF302` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-213"></a>

### 11-01 · WE Steuerbefehl · Datensatz 213

**Einstellebene 18, WE 8 Kaskadenfunktionen** · Einstellebene 18, WE 8 Kaskadenfunktionen

Gespeichert: **2 ** · Bereich: 1 … 4 · Schrittfeld (roh): 1

Adresskandidat: `0xF323` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5C70` · Dateibereich: `0xF86E`–`0xF9D2` (Ende exklusiv)

Hilfetext:

> 1 = Temperatursteuerung mit BW Funktion am WE
> 2 = Leistungssteuerung mit BW Funktion am WE
> 3 = Temperatursteuerung ohne BW Funktion am WE
> 4 = Leistungssteuerung ohne BW Funktion am WE

<a id="datensatz-172"></a>

### 11-02 · WE Nennleistung · Datensatz 172

**Einstellebene 11, WE 1 Kaskadenfunktionen** · Einstellebene 11, WE 1 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF2EC` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5820` · Dateibereich: `0xCA22`–`0xCB27` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-178"></a>

### 11-02 · WE Nennleistung · Datensatz 178

**Einstellebene 12, WE 2 Kaskadenfunktionen** · Einstellebene 12, WE 2 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF2F4` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x58C0` · Dateibereich: `0xD0F2`–`0xD1F7` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-184"></a>

### 11-02 · WE Nennleistung · Datensatz 184

**Einstellebene 13, WE 3 Kaskadenfunktionen** · Einstellebene 13, WE 3 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF2FC` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5960` · Dateibereich: `0xD7C2`–`0xD8C7` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-190"></a>

### 11-02 · WE Nennleistung · Datensatz 190

**Einstellebene 14, WE 4 Kaskadenfunktionen** · Einstellebene 14, WE 4 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF304` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5A00` · Dateibereich: `0xDE92`–`0xDF97` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-196"></a>

### 11-02 · WE Nennleistung · Datensatz 196

**Einstellebene 15, WE 5 Kaskadenfunktionen** · Einstellebene 15, WE 5 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF30C` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5AA0` · Dateibereich: `0xE562`–`0xE667` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-202"></a>

### 11-02 · WE Nennleistung · Datensatz 202

**Einstellebene 16, WE 6 Kaskadenfunktionen** · Einstellebene 16, WE 6 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF314` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5B40` · Dateibereich: `0xEC32`–`0xED37` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-208"></a>

### 11-02 · WE Nennleistung · Datensatz 208

**Einstellebene 17, WE 7 Kaskadenfunktionen** · Einstellebene 17, WE 7 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF31C` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5BE0` · Dateibereich: `0xF302`–`0xF407` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-214"></a>

### 11-02 · WE Nennleistung · Datensatz 214

**Einstellebene 18, WE 8 Kaskadenfunktionen** · Einstellebene 18, WE 8 Kaskadenfunktionen

Gespeichert: **100 kW** · Bereich: 0 … 999 · Schrittfeld (roh): 10

Adresskandidat: `0xF324` · Typcode: `13` · Einheitencode: `8` · Schlüssel: `0x5C80` · Dateibereich: `0xF9D2`–`0xFAD7` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Maximalleistung des Wärmeerzeugers von 0 bis 999 kW eingestellt

<a id="datensatz-173"></a>

### 11-03 · minimale WE-Leistung · Datensatz 173

**Einstellebene 11, WE 1 Kaskadenfunktionen** · Einstellebene 11, WE 1 Kaskadenfunktionen

Gespeichert: **70 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF2EE` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5830` · Dateibereich: `0xCB27`–`0xCC3A` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-179"></a>

### 11-03 · minimale WE-Leistung · Datensatz 179

**Einstellebene 12, WE 2 Kaskadenfunktionen** · Einstellebene 12, WE 2 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF2F6` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x58D0` · Dateibereich: `0xD1F7`–`0xD30A` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-185"></a>

### 11-03 · minimale WE-Leistung · Datensatz 185

**Einstellebene 13, WE 3 Kaskadenfunktionen** · Einstellebene 13, WE 3 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF2FE` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5970` · Dateibereich: `0xD8C7`–`0xD9DA` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-191"></a>

### 11-03 · minimale WE-Leistung · Datensatz 191

**Einstellebene 14, WE 4 Kaskadenfunktionen** · Einstellebene 14, WE 4 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF306` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5A10` · Dateibereich: `0xDF97`–`0xE0AA` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-197"></a>

### 11-03 · minimale WE-Leistung · Datensatz 197

**Einstellebene 15, WE 5 Kaskadenfunktionen** · Einstellebene 15, WE 5 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF30E` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5AB0` · Dateibereich: `0xE667`–`0xE77A` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-203"></a>

### 11-03 · minimale WE-Leistung · Datensatz 203

**Einstellebene 16, WE 6 Kaskadenfunktionen** · Einstellebene 16, WE 6 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF316` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5B50` · Dateibereich: `0xED37`–`0xEE4A` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-209"></a>

### 11-03 · minimale WE-Leistung · Datensatz 209

**Einstellebene 17, WE 7 Kaskadenfunktionen** · Einstellebene 17, WE 7 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF31E` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5BF0` · Dateibereich: `0xF407`–`0xF51A` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-215"></a>

### 11-03 · minimale WE-Leistung · Datensatz 215

**Einstellebene 18, WE 8 Kaskadenfunktionen** · Einstellebene 18, WE 8 Kaskadenfunktionen

Gespeichert: **100 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF326` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5C90` · Dateibereich: `0xFAD7`–`0xFBEA` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Minimalleistung des Wärmeerzeugers in % der Maximalleistung eingestellt.

<a id="datensatz-174"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 174

**Einstellebene 11, WE 1 Kaskadenfunktionen** · Einstellebene 11, WE 1 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF2EF` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5840` · Dateibereich: `0xCC3A`–`0xCD40` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-180"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 180

**Einstellebene 12, WE 2 Kaskadenfunktionen** · Einstellebene 12, WE 2 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF2F7` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x58E0` · Dateibereich: `0xD30A`–`0xD410` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-186"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 186

**Einstellebene 13, WE 3 Kaskadenfunktionen** · Einstellebene 13, WE 3 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF2FF` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5980` · Dateibereich: `0xD9DA`–`0xDAE0` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-192"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 192

**Einstellebene 14, WE 4 Kaskadenfunktionen** · Einstellebene 14, WE 4 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF307` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5A20` · Dateibereich: `0xE0AA`–`0xE1B0` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-198"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 198

**Einstellebene 15, WE 5 Kaskadenfunktionen** · Einstellebene 15, WE 5 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF30F` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5AC0` · Dateibereich: `0xE77A`–`0xE880` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-204"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 204

**Einstellebene 16, WE 6 Kaskadenfunktionen** · Einstellebene 16, WE 6 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF317` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5B60` · Dateibereich: `0xEE4A`–`0xEF50` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-210"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 210

**Einstellebene 17, WE 7 Kaskadenfunktionen** · Einstellebene 17, WE 7 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF31F` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5C00` · Dateibereich: `0xF51A`–`0xF620` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-216"></a>

### 11-04 · Einschaltleistung Folge WE · Datensatz 216

**Einstellebene 18, WE 8 Kaskadenfunktionen** · Einstellebene 18, WE 8 Kaskadenfunktionen

Gespeichert: **80 %** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xF327` · Typcode: `0` · Einheitencode: `4` · Schlüssel: `0x5CA0` · Dateibereich: `0xFBEA`–`0xFCF0` (Ende exklusiv)

Hilfetext:

> Mit dem Einsteller wird die Freigabe für den Folge Wärmeerzeuger in % eingestellt

<a id="datensatz-175"></a>

### 11-05 · WE Folgewechsel · Datensatz 175

**Einstellebene 11, WE 1 Kaskadenfunktionen** · Einstellebene 11, WE 1 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2F0` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5850` · Dateibereich: `0xCD40`–`0xCE1E` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-181"></a>

### 11-05 · WE Folgewechsel · Datensatz 181

**Einstellebene 12, WE 2 Kaskadenfunktionen** · Einstellebene 12, WE 2 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF2F8` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x58F0` · Dateibereich: `0xD410`–`0xD4EE` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-187"></a>

### 11-05 · WE Folgewechsel · Datensatz 187

**Einstellebene 13, WE 3 Kaskadenfunktionen** · Einstellebene 13, WE 3 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF300` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5990` · Dateibereich: `0xDAE0`–`0xDBBE` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-193"></a>

### 11-05 · WE Folgewechsel · Datensatz 193

**Einstellebene 14, WE 4 Kaskadenfunktionen** · Einstellebene 14, WE 4 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF308` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5A30` · Dateibereich: `0xE1B0`–`0xE28E` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-199"></a>

### 11-05 · WE Folgewechsel · Datensatz 199

**Einstellebene 15, WE 5 Kaskadenfunktionen** · Einstellebene 15, WE 5 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF310` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5AD0` · Dateibereich: `0xE880`–`0xE95E` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-205"></a>

### 11-05 · WE Folgewechsel · Datensatz 205

**Einstellebene 16, WE 6 Kaskadenfunktionen** · Einstellebene 16, WE 6 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF318` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5B70` · Dateibereich: `0xEF50`–`0xF02E` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-211"></a>

### 11-05 · WE Folgewechsel · Datensatz 211

**Einstellebene 17, WE 7 Kaskadenfunktionen** · Einstellebene 17, WE 7 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF320` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5C10` · Dateibereich: `0xF620`–`0xF6FE` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-217"></a>

### 11-05 · WE Folgewechsel · Datensatz 217

**Einstellebene 18, WE 8 Kaskadenfunktionen** · Einstellebene 18, WE 8 Kaskadenfunktionen

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF328` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x5CB0` · Dateibereich: `0xFCF0`–`0xFDCE` (Ende exklusiv)

Hilfetext:

> 0 = Keine Sequenzumschaltung
> 1 = Sequenzumschaltung

<a id="datensatz-131"></a>

### 15-10 · Heissgas Maximaltemperatur · Datensatz 131

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **125 °C** · Bereich: 0 … 140 · Schrittfeld (roh): 10

Adresskandidat: `0xF286` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4900` · Dateibereich: `0x94D9`–`0x9687` (Ende exklusiv)

Hilfetext:

> Überschreitet die Heissgastemperatur (THG) den Einstellwert, wird die Quellenpumpe oder das Gebläse und der Kompressor abgeschaltet. Sinkt die Temperatur THG um 2 K unter den Einstellwert, läuft die Anlage in der eingestellten Betriebsart weiter.

<a id="datensatz-132"></a>

### 15-11 · TWVmax Abschalthysterese · Datensatz 132

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **7 K** · Bereich: 2 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xFF1F` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4910` · Dateibereich: `0x9687`–`0x97A3` (Ende exklusiv)

Hilfetext:

> Bei einer TWVmax Abschaltung ist immer diese eingestellte Hysterese wirksam für die Wiederinschaltung.

<a id="datensatz-133"></a>

### 15-12 · Kondensator Austritt Störung · Datensatz 133

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-5 °C** · Bereich: -20 … 70 · Schrittfeld (roh): 5

Adresskandidat: `0xFF3C` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4920` · Dateibereich: `0x97A3`–`0x98DB` (Ende exklusiv)

Hilfetext:

> Sinkt die Kondensator Austrittstemperatur unter den eingestellten Wert, wird eine Störung 8 generiert und der WE abgeschaltet.

<a id="datensatz-134"></a>

### 15-13 · Kondensator Austritt Abschaltoffset · Datensatz 134

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **2 K** · Bereich: 0 … 10 · Schrittfeld (roh): 1

Adresskandidat: `0xFF3E` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4930` · Dateibereich: `0x98DB`–`0x9A23` (Ende exklusiv)

Hilfetext:

> Sinkt die Kondensator Austrittstemperatur unter den eingestellten an ID 15-11Wert plus diesen Abschaltoffset, wird der WE abgeschaltet.

<a id="datensatz-135"></a>

### 15-21 · Nachlaufzeit Quellenpumpe · Datensatz 135

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0.5 min** · Bereich: 0 … 15 · Schrittfeld (roh): 5

Adresskandidat: `0xF26A` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x4940` · Dateibereich: `0x9A23`–`0x9B50` (Ende exklusiv)

Hilfetext:

> Die Quellenpumpe (QP) oder das Gebläse laufen nach Abschalten des Kompressors noch für die hier festgelegte Zeit nach.

<a id="datensatz-136"></a>

### 15-22 · Wärmequelle Frostschutztemperatur · Datensatz 136

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-12 °C** · Bereich: -50 … 10 · Schrittfeld (roh): 5

Adresskandidat: `0xF288` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4950` · Dateibereich: `0x9B50`–`0x9CCF` (Ende exklusiv)

Hilfetext:

> Unterschreitet die Wärmequellen Austrittstemperatur (TWA) den hier eingestellten Wert, so wird die Quellenpumpe oder das Gebläse und der Kompressor abgeschaltet. Störung Err 02 wird angezeigt.

<a id="datensatz-82"></a>

### 15-23 · Frostschutztemperatur TVD · Datensatz 82

**Einstellebene 5, Brauchwasserbereitung** · Einstellebene 5, Brauchwasserbereitung

Gespeichert: **4 ** · Bereich: -20 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF29E` · Typcode: `13` · Einheitencode: `0` · Schlüssel: `0x28A0` · Dateibereich: `0x5B17`–`0x5CA4` (Ende exklusiv)

Hilfetext:

> Der TVD (Klemme 45) wirkt, in Stellung 2 des Einstellers 5-5, als Frostschutzfühler für die separate WW-Wärmepumpe. Diese Wärmepumpe wird abgeschaltet, sobald die Temperatur TVD den hier eingestellten Wert unterschreitet.

<a id="datensatz-137"></a>

### 15-24 · Wärmequelle Eintrittsschutztemperatur · Datensatz 137

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **40 °C** · Bereich: 0 … 50 · Schrittfeld (roh): 5

Adresskandidat: `0xF28A` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4960` · Dateibereich: `0x9CCF`–`0x9E2F` (Ende exklusiv)

Hilfetext:

> Überschreitet die Wärmequellen-Eintrittstemperatur (TWE) den hier eingestellten Wert, wird die Quellenpumpe oder das Gebläse und der Kompressor abgeschaltet.

<a id="datensatz-138"></a>

### 15-25 · Abschaltoffset Frostschutz · Datensatz 138

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **2 K** · Bereich: 0 … 20 · Schrittfeld (roh): 1

Adresskandidat: `0xF28E` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4970` · Dateibereich: `0x9E2F`–`0x9FCC` (Ende exklusiv)

Hilfetext:

> Dieser Einsteller ermöglicht bei Frostgefahr ein Abschalten des Kompressors bevor eine Störung ausgelöst
> wird. Die Wärmequellen-Frostschutztemperatur (Einsteller 15-22) plus der hier eingestellte Wert ergeben die Abschaltgrenze.

<a id="datensatz-139"></a>

### 15-26 · TWE-Temperaturpunkt TWVmax Reduktion · Datensatz 139

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-20 °C** · Bereich: -20 … 10 · Schrittfeld (roh): 1

Adresskandidat: `0xFF28` · Typcode: `1` · Einheitencode: `1` · Schlüssel: `0x4980` · Dateibereich: `0x9FCC`–`0xA0ED` (Ende exklusiv)

Hilfetext:

> Wärmequellen Eintrittstemperatur für die Absenkung der maximalen Wärmepumpen Vorlauftemperatur.

<a id="datensatz-140"></a>

### 15-27 · TWVmax bei TWE Grenztemperatur · Datensatz 140

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **60 °C** · Bereich: 20 … 60 · Schrittfeld (roh): 1

Adresskandidat: `0xFF2A` · Typcode: `0` · Einheitencode: `1` · Schlüssel: `0x4990` · Dateibereich: `0xA0ED`–`0xA203` (Ende exklusiv)

Hilfetext:

> Maximale Wärmepumpen Vorlauftemperatur bei Wärmequellen Eintritts Grenztemperatur (15-28).

<a id="datensatz-141"></a>

### 15-28 · TWE Grenztemperatur · Datensatz 141

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-30 °C** · Bereich: -30 … 10 · Schrittfeld (roh): 1

Adresskandidat: `0xFF29` · Typcode: `1` · Einheitencode: `1` · Schlüssel: `0x49A0` · Dateibereich: `0xA203`–`0xA2FB` (Ende exklusiv)

Hilfetext:

> Wärmequellen Eintritts Grenzemperatur für Wärmepumpen Vorlaufreduktion

<a id="datensatz-142"></a>

### 15-40 · Abtautyp · Datensatz 142

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0 ** · Bereich: 0 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0xF26E` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x49B0` · Dateibereich: `0xA2FB`–`0xA494` (Ende exklusiv)

Hilfetext:

> Damit wird festgelegt auf welche Art abgetaut wird. Der eingestellte Code hat folgende Bedeutung:
> 0 = Keine Abtauung (Sole / Wasser- oder Wasser / Wasser Wärmepumpe)
> 1 = Temperaturabhängige Abtaueinleitung
> 2 = Druckabhängige Abtaueinleitung

<a id="datensatz-143"></a>

### 15-41 · Abtaudifferenz (TWE - TVD) · Datensatz 143

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **10 °C** · Bereich: 3 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF270` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x49C0` · Dateibereich: `0xA494`–`0xA601` (Ende exklusiv)

Hilfetext:

> Für eine Abtaueinleitung muss die Temperaturdifferenz Wärmequelle-Eintrittstemperatur TWE – Verdampfungstemperatur
> TVD grösser sein, als der in diesem Einsteller eingestellte Wert.

<a id="datensatz-144"></a>

### 15-42 · Freigabe Abtauung (TVD) · Datensatz 144

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **-6 °C** · Bereich: -20 … 20 · Schrittfeld (roh): 5

Adresskandidat: `0xF272` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x49D0` · Dateibereich: `0xA601`–`0xA7CF` (Ende exklusiv)

Hilfetext:

> Bei 15-40 = 1: Für eine Freigabe der Abtauung muss die Verdampfungstemperatur TVD kleiner sein, als der in diesem Parameter eingestellte Wert.
> Bei 15-40 = 2: Für eine Freigabe der Abtauung muss die Aussentemperatur TA kleiner sein, als der in diesem Parameter eingestellte Wert.

<a id="datensatz-145"></a>

### 15-43 · Abtauendetemperatur (TVD) · Datensatz 145

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **9 °C** · Bereich: 0 … 40 · Schrittfeld (roh): 5

Adresskandidat: `0xF274` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x49E0` · Dateibereich: `0xA7CF`–`0xA8FA` (Ende exklusiv)

Hilfetext:

> Überschreitet die Verdampfungstemperatur TVD den in diesem Einsteller eingestellten Wert, wird die Abtauung beendet.

<a id="datensatz-146"></a>

### 15-44 · Abtaudauer · Datensatz 146

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **10 min** · Bereich: 0 … 30 · Schrittfeld (roh): 5

Adresskandidat: `0xF276` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x49F0` · Dateibereich: `0xA8FA`–`0xAA01` (Ende exklusiv)

Hilfetext:

> Die Abtauung wird beendet, spätestens nach Ablauf der in diesem Einsteller eingestellten Dauer.

<a id="datensatz-147"></a>

### 15-45 · Abtausperrzeit · Datensatz 147

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **45 min** · Bereich: 0 … 60 · Schrittfeld (roh): 5

Adresskandidat: `0xF278` · Typcode: `13` · Einheitencode: `6` · Schlüssel: `0x4A00` · Dateibereich: `0xAA01`–`0xAB39` (Ende exklusiv)

Hilfetext:

> Nach Beendigung einer Abtauung, kann eine weitere Abtauung erst erfolgen, nach Ablauf der in diesem Einsteller eingestellten Abtausperrzeit.

<a id="datensatz-148"></a>

### 15-46 · Verzögerung Niederdruck · Datensatz 148

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **10 s?** · Bereich: 0 … 250 · Schrittfeld (roh): 1

Adresskandidat: `0xF26F` · Typcode: `0` · Einheitencode: `7` · Schlüssel: `0x4A10` · Dateibereich: `0xAB39`–`0xAC7C` (Ende exklusiv)

Hilfetext:

> Eine Störung des Niederdruck Pressostaten muss mindestens um die hier eingestellte Zeit anliegen bis die Störung ausgelöst und angezeigt wird.

<a id="datensatz-149"></a>

### 15-47 · Abtropfzeit · Datensatz 149

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0 ** · Bereich: 0 … 100 · Schrittfeld (roh): 1

Adresskandidat: `0xFF26` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x4A20` · Dateibereich: `0xAC7C`–`0xADE9` (Ende exklusiv)

Hilfetext:

> Nach erfolgter Abtauung wird der Verdichter abgeschaltet und das Abtauventil bleib für die Abtropfzeit wahlweise ein oder ausgeschaltet.
> Achtung der Wert ist im 0.1 Minuten Format. (10 = 1.0 Min)

<a id="datensatz-150"></a>

### 15-48 · Verzögerung Druckdifferenzeingang · Datensatz 150

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **120 ** · Bereich: 0 … 250 · Schrittfeld (roh): 1

Adresskandidat: `0xFF27` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x4A30` · Dateibereich: `0xADE9`–`0xAF32` (Ende exklusiv)

Hilfetext:

> Bei Differenzdruck Abtauung muss der Differndruckschalter für die eingestellte Zeit geschlossen sein, damit eine Abtauung gestartet wird.

<a id="datensatz-151"></a>

### 15-49 · Abtau Frostschutzstörung · Datensatz 151

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **12 °C** · Bereich: 3 … 20 · Schrittfeld (roh): 10

Adresskandidat: `0xFF40` · Typcode: `13` · Einheitencode: `1` · Schlüssel: `0x4A40` · Dateibereich: `0xAF32`–`0xB07F` (Ende exklusiv)

Hilfetext:

> Sinkt die Wärmepumpen Vorlauftemperatur im Abtaubetrieb unter den eingestellten Wert, wird eine Frostschutzstörung 9 generiert und der WE abgeschaltet.

<a id="datensatz-152"></a>

### 15-50 · Abtau Frostschutz Offset Zusatzheizung · Datensatz 152

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **2 K** · Bereich: 2 … 10 · Schrittfeld (roh): 1

Adresskandidat: `0xFF42` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4A50` · Dateibereich: `0xB07F`–`0xB1EA` (Ende exklusiv)

Hilfetext:

> Sinkt die Wärmepumpen Vorlauftemperatur im Abtaubetrieb unter den an ID 15-49 eingestellten Wert plus diesen Offset, wird eine Zusatzheizung Abtaubetrieb freigegeben..

<a id="datensatz-153"></a>

### 15-60 · Anpassen TWA Messwert · Datensatz 153

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **0 K** · Bereich: 0 … 5 · Schrittfeld (roh): 1

Adresskandidat: `0xF28C` · Typcode: `13` · Einheitencode: `2` · Schlüssel: `0x4A60` · Dateibereich: `0xB1EA`–`0xB31B` (Ende exklusiv)

Hilfetext:

> Mit diesem Einsteller kann der Messwert des Wärmequellen-Austrittsfühlers TWA, werkseitig, an die Wärmepumpe angepasst werden.

<a id="datensatz-3"></a>

### Ohne TEM-Kennung · Automatikprogramm · Datensatz 3

**Heizkreis 1 (abgeleitet)** · Einstellebene 1

Gespeichert: **0 ** · Bereich: 0 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0xF00B` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x0810` · Dateibereich: `0x02B9`–`0x0384` (Ende exklusiv)

Hilfetext:

> 0 = Uhrprogramm 1
> 1 = Uhrprogramm 2
> 2 = Uhrprogramm 3

<a id="datensatz-4"></a>

### Ohne TEM-Kennung · Automatikprogramm · Datensatz 4

**Heizkreis 2 (abgeleitet)** · Einstellebene 1

Gespeichert: **0 ** · Bereich: 0 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0xF333` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x0811` · Dateibereich: `0x0384`–`0x044F` (Ende exklusiv)

Hilfetext:

> 0 = Uhrprogramm 1
> 1 = Uhrprogramm 2
> 2 = Uhrprogramm 3

<a id="datensatz-24"></a>

### Ohne TEM-Kennung · BW Zeitprog mit Heizkreisprogramm 1 · Datensatz 24

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF06D` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x1080` · Dateibereich: `0x1458`–`0x155B` (Ende exklusiv)

Hilfetext:

> 0 = Freigabe mit separarem Warmwasser Zeitprogramm
> 1 = Freigabe mit Heizkreis Zeitprogramm 1

<a id="datensatz-25"></a>

### Ohne TEM-Kennung · BW Zeitprog mit Heizkreisprogramm 1 · Datensatz 25

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF06D` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x1081` · Dateibereich: `0x155B`–`0x165E` (Ende exklusiv)

Hilfetext:

> 0 = Freigabe mit separarem Warmwasser Zeitprogramm
> 1 = Freigabe mit Heizkreis Zeitprogramm 1

<a id="datensatz-26"></a>

### Ohne TEM-Kennung · BW Zeitprog mit Heizkreisprogramm 2 · Datensatz 26

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF0CB` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x1090` · Dateibereich: `0x165E`–`0x1761` (Ende exklusiv)

Hilfetext:

> 0 = Freigabe mit separarem Warmwasser Zeitprogramm
> 1 = Freigabe mit Heizkreis Zeitprogramm 2

<a id="datensatz-27"></a>

### Ohne TEM-Kennung · BW Zeitprog mit Heizkreisprogramm 2 · Datensatz 27

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF0CB` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x1091` · Dateibereich: `0x1761`–`0x1864` (Ende exklusiv)

Hilfetext:

> 0 = Freigabe mit separarem Warmwasser Zeitprogramm
> 1 = Freigabe mit Heizkreis Zeitprogramm 2

<a id="datensatz-28"></a>

### Ohne TEM-Kennung · BW Zeitprog mit Heizkreisprogramm 3 · Datensatz 28

**Heizkreis 1 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF129` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x10A0` · Dateibereich: `0x1864`–`0x1967` (Ende exklusiv)

Hilfetext:

> 0 = Freigabe mit separarem Warmwasser Zeitprogramm
> 1 = Freigabe mit Heizkreis Zeitprogramm 3

<a id="datensatz-29"></a>

### Ohne TEM-Kennung · BW Zeitprog mit Heizkreisprogramm 3 · Datensatz 29

**Heizkreis 2 (abgeleitet)** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0xF129` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x10A1` · Dateibereich: `0x1967`–`0x1A6A` (Ende exklusiv)

Hilfetext:

> 0 = Freigabe mit separarem Warmwasser Zeitprogramm
> 1 = Freigabe mit Heizkreis Zeitprogramm 3

<a id="datensatz-30"></a>

### Ohne TEM-Kennung · Störung quittieren · Datensatz 30

**Einstellebene 2** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 1 · Schrittfeld (roh): 1

Adresskandidat: `0x0889` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x10B0` · Dateibereich: `0x1A6A`–`0x1B2B` (Ende exklusiv)

Hilfetext:

> Störung quittieren
> 0 = nein
> 1 = quittieren

<a id="datensatz-31"></a>

### Ohne TEM-Kennung · Betriebsdaten zurückstellen · Datensatz 31

**Einstellebene 2** · Einstellebene 2

Gespeichert: **0 ** · Bereich: 0 … 2 · Schrittfeld (roh): 1

Adresskandidat: `0x0B51` · Typcode: `0` · Einheitencode: `0` · Schlüssel: `0x10C0` · Dateibereich: `0x1B2B`–`0x1C56` (Ende exklusiv)

Hilfetext:

> Betriebsdaten zurückstellen:
> 0 = keine Rückstellung
> 1 = Rückstellung Betriebsdaten Wärmepumpe
> 2 = Rückstellung Betriebsdaten Zusatzheizung

<a id="datensatz-154"></a>

### Ohne TEM-Kennung · TWA Maximalwert · Datensatz 154

**Einstellebene 9, WE Einstellungen Wärmepumpe** · Einstellebene 9, WE Einstellungen Wärmepumpe

Gespeichert: **150 °C** · Bereich: 0 … 150 · Schrittfeld (roh): 1

Adresskandidat: `0xFF2B` · Typcode: `0` · Einheitencode: `1` · Schlüssel: `0x4A70` · Dateibereich: `0xB31B`–`0xB4DA` (Ende exklusiv)

Hilfetext:

> Mit diesem Einsteller kann eine Temperaturgrenze für den WQA Fühler gesetzt werden (Kurzschlussüberwachung).
> Eine Überschreitung der Temperatur führt zu einer Störabschaltung (WQA Frostschutzstörung).
> Eine Einstellung &gt;125 °C bewirkt, dass keine Störung generiert wird.
