import "@ebusd/ebus-typespec";
import "./_templates.tsp";

using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;

namespace Tem;

/**
 * Direkte Parameterabfragen des SE 6000 WPC an dessen Slave-Adresse 15.
 *
 * Die IDs entsprechen den am Gerät funktionierenden Einträgen aus
 * input/15.csv: Service 06 21 mit TEM-Parameterkennung. Das ist ein
 * eigenständiger Zugriffspfad und nicht der 10 0a-Blockabgleich mit den
 * Bedienteilen. Der Schreibdatensatz für Raumtemp_soll ist als separates
 * Modell Raumtemp_soll_set enthalten.
 *
 * ID-Aufbau (6 Bytes je @id): pbsb ist immer 06 21. Die restlichen 4 Bytes
 * setzen sich für die meisten hier genutzten Parameter aus
 * <Parametergruppe><Parameternummer><00><Familienkennung> zusammen, z.B.
 * 63/8f/00/0a für Parameter 03-051 (Gruppe 0x63 = "03"+0x60, Nummer 0x8f,
 * Familienkennung 0x0a = Heizkreis-Parameter). Dieses Schema deckt sich mit
 * dem öffentlichen Referenzprojekt john30/ebusd-configuration (Ordner
 * src/tem, Datei 15.tsp: https://github.com/john30/ebusd-configuration/
 * blob/master/src/tem/15.tsp), das dieselben Parameternummern über
 * @base(0x6, 0x21, <Gruppe>) + @ext(<Nummer>, 0, <Familienkennung>)
 * beschreibt. Achtung: dort sind viele 03-xxx-Parameter zusätzlich hinter
 * @condition(Parameter_level, 'Expert Level'/'User Level') gestaffelt und
 * mit UNTERSCHIEDLICHEN Nummern für dieselbe Einstellung doppelt vorhanden
 * (z.B. Temp_raum_spar = 0x85 im User-Level-Zweig, aber 0x90 im
 * Expert-Level-Zweig) - welche Nummer am eigenen Gerät tatsächlich
 * antwortet, ist nur durch Ausprobieren zu klären; die Referenz dient nur
 * als Kandidatenliste, nicht als Garantie.
 *
 * Abgleich mit FB-Initialization.md: die dortigen "Einsteller"-Kürzel wie
 * "3-2" entsprechen (soweit bisher geprüft) direkt der TEM-Parameternummer
 * "03-002", siehe Kommentare an den einzelnen Modellen unten. Für die als
 * "Kühltemperatur" (3-4), "Kühlgrenzabstand" (3-5) und "Heizgr gem
 * Vorl.Soll" (3-8) bezeichneten Einsteller enthält die Referenz keine
 * Einträge (dort scheinbar nur für Geräte ohne Kühlfunktion erfasst) - für
 * 03-004, 03-005 und 03-008 müssten die Familienkennung 0x0a und
 * unbekannte Nummern-Bytes experimentell gesucht werden.
 * Im ebusctl-grab-Format steht nach PBSB zusätzlich NN, die Anzahl der
 * folgenden Datenbytes. NN gehört nicht in @id; z.B. wird
 * 011506210400800046 als ebusctl hex -n 15062100800046 gesendet. Die
 * Masterquelle wird dabei nicht mit -s 01 erzwungen; ebusd verwendet seine
 * konfigurierte Standardquelle.
 *
 * Abfragetest 2026-09-10 über ebusd 26.1.26.1 an diesem SE 6000 WPC
 * (ausschließlich `read -c 15`, kein Schreibtelegramm): Alle folgenden
 * Werte sind eine Momentaufnahme und keine fest einzubrennenden Sollwerte.
 * Nicht-triviale, fachlich plausible Antworten:
 *   Parameter_level=User_Level; Vl_temp_ist=22.2 °C;
 *   Rl_temp_ist=20.7 °C; Wq_temp_out=36.1 °C; At=At_46=14.7 °C;
 *   Raumtemp_46=Raumtemp_48=22.9 °C;
 *   Hk_vl_temp_46=Hk_vl_temp_48=22.2 °C; Ww_temp_4a=47.5 °C;
 *   Status=Abgeschaltet; Betriebswahl=Aus; Wd=Mon;
 *   Raumtemp_soll=20.0 °C.
 * Wq_temp_in antwortete mit 120.0 °C. Das ist zwar nicht trivial, als
 * Eintrittstemperatur der Wärmequelle aber nicht plausibel und muss vor einer
 * fachlichen Zuordnung mit der Anzeige bzw. einem Rohtelegramm abgeglichen
 * werden.
 * Time antwortete mit 00:00, Sz_1 und Bs_1 mit 0 bzw. 0.00. Die Modelle
 * At_mittel, Temp_raum_spar, Temp_raumschutz, Temp_vl_fusspunkt,
 * Heizgrenze_spar, Startopt_vorhaltezeit, Temp_raum_kompensation,
 * Temp_vl_auslegung, Temp_heizgrenze_normal, Temp_raum_normal, Version_sw,
 * Version_hw und Ww_temp_soll antworteten ebenfalls mit 0/0.0/0.00. Diese
 * Antworten belegen nur, dass die Anfrage angenommen wurde; sie validieren
 * noch nicht die Parametermapping-Hypothese (insbesondere bei User_Level).
 */
@zz(0x15)
namespace _15 {

model Parameterkopf {
  command: command;
  max: SIN;
  min: SIN;
}

/** Sechs Byte Metadaten für Zählerparameter. */
@maxLength(6)
scalar Zaehlerkopf extends HEX;

@unit("h")
@divisor(100)
scalar Betriebsstunden extends HCD;

@divisor(100)
scalar Versionsnummer extends UIN;

@unit("min")
@divisor(10)
scalar Minuten10 extends UIN;

@divisor(10)
scalar Faktor10 extends UIN;

enum Values_Waermepumpenstatus {
  Abgeschaltet: 0,
  Heizbetrieb: 1,
  Vorlauf_Heizbetrieb: 2,
  Extern_gesperrt: 3,
  Kuehlbetrieb: 4,
  Vorlaufzeit_Kuehlbetrieb: 5,
  Vorlaufzeit_Abtaubetrieb: 6,
  Abtaubetrieb: 7,
  Stoerung: 8,
  Abtropfen: 9,
  DT_UEberwachung: 10,
  Abtau_Vorheizung: 11,
  Abtauen_1: 12,
}

@values(Values_Waermepumpenstatus)
scalar Waermepumpenstatus extends UIN;

enum Values_Betriebswahl {
  Standby: 0,
  Uhrenprogramm1: 1,
  Uhrenprogramm2: 2,
  Uhrenprogramm3: 3,
  Normalbetrieb: 4,
  Sparbetrieb: 5,
  HandbetriebHeizen: 7,
  HandbetriebKuehlen: 8,
  Gemaess_Führungskreis: 10,
}

@values(Values_Betriebswahl)
scalar BetriebswahlWert extends UIN;

enum Values_AusEin {
  Aus: 0,
  Ein: 1,
}

@values(Values_AusEin)
scalar AusEin extends UIN;

enum Values_Parameterlevel {
  User_Level: 0,
  Expert_Level: 2,
}

@values(Values_Parameterlevel)
scalar Parameterlevel extends UIN;

model ParameterTemp10 {
  parameterkopf: Parameterkopf,
  temp: temp10,
}

model ParameterTemp2 {
  parameterkopf: Parameterkopf,
  temp: temp2,
}

model ParameterStatus {
  parameterkopf: Parameterkopf,
  status: Waermepumpenstatus,
}

model ParameterBetriebswahl {
  parameterkopf: Parameterkopf,
  status: BetriebswahlWert,
}

/** TEM-Parameter mit Datentyp 0x02 (on_off) und einem 16-Bit-0/1-Wert. */
model ParameterAusEin {
  parameterkopf: Parameterkopf,
  status: AusEin,
}

model ParameterZeit {
  parameterkopf: Parameterkopf,
  time: MIN,
}

model ParameterWochentag {
  parameterkopf: Parameterkopf,
  day: BDY,
}

model ParameterZaehler {
  zaehlerkopf: Zaehlerkopf,
  count: HCD,
}

model ParameterBetriebsstunden {
  zaehlerkopf: Zaehlerkopf,
  hours: Betriebsstunden,
}

model ParameterVersion {
  parameterkopf: Parameterkopf,
  value: Versionsnummer,
}

/** Zugangslevel der TEM-Einsteller, Parameter 04-043. */
@id(0x6, 0x21, 0x04, 0xab, 0x00, 0x4a)
model Parameter_level {
  data: {
    parameterkopf: Parameterkopf,
    status: Parameterlevel,
  },
}

@write
@zz(0x10)
@id(0x6, 0x23, 0x04, 0xaa, 0x00, 0x40)
model Global_passwort {
    /** 256 */
    password: UIN;
}

model ParameterMinuten10 {
  parameterkopf: Parameterkopf,
  time: Minuten10,
}

model ParameterFaktor10 {
  parameterkopf: Parameterkopf,
  value: Faktor10,
}

/** Vorlauftemperatur Wärmeerzeuger, Parameter 00-007. */
@id(0x6, 0x21, 0x00, 0x87, 0x00, 0x42)
model Vl_temp_ist {
  data: ParameterTemp10,
}

/** Rücklauftemperatur Wärmeerzeuger, Parameter 00-008. */
@id(0x6, 0x21, 0x00, 0x88, 0x00, 0x42)
model Rl_temp_ist {
  data: ParameterTemp10,
}

/** Wärmequelle Austrittstemperatur, Parameter 00-070. */
@id(0x6, 0x21, 0x00, 0xc6, 0x00, 0x42)
model Wq_temp_out {
  data: ParameterTemp10,
}

/** Wärmequelle Eintrittstemperatur, Parameter 00-071. */
@id(0x6, 0x21, 0x00, 0xc7, 0x00, 0x42)
model Wq_temp_in {
  data: ParameterTemp10,
}

/** Wärmepumpenstatus, Parameter 02-053. */
@id(0x6, 0x21, 0x02, 0xb5, 0x00, 0x42)
model Status {
  data: ParameterStatus,
}


enum Values_status_2 {
  Aus: 0,
  Automatik: 1,
  Handbetrieb_Heizen: 2,
  Handbetrieb_Kuehlen: 3,
  Waermequellenpumpe: 6,
}

/** Betriebswahl Wärmeerzeuger, Parameter 09-075. */
@id(0x6, 0x21, 0x09, 0xcb, 0x00, 0x42)
model Betriebswahl {
  data: parameter1,
  @values(Values_status_2)
  status: status;
}

/** Uhrzeit, Parameter 02-072. */
@id(0x6, 0x21, 0x02, 0xc8, 0x00, 0x42)
model Time {
  data: ParameterZeit,
}

/** Außentemperatur, Parameter 00-000. */
@id(0x6, 0x21, 0x00, 0x80, 0x00, 0x42)
model At {
  data: ParameterTemp10,
}

/** Außentemperatur, Parameter 00-000, Familienkennung 46. */
@id(0x6, 0x21, 0x00, 0x80, 0x00, 0x46)
model At_46 {
  data: ParameterTemp10,
}

/** Raumtemperatur, Parameter 00-001, Familienkennung 46. */
@id(0x6, 0x21, 0x00, 0x81, 0x00, 0x46)
model Raumtemp_46 {
  data: ParameterTemp10,
}

/** Raumtemperatur, Parameter 00-001, Familienkennung 48. */
@id(0x6, 0x21, 0x00, 0x81, 0x00, 0x48)
model Raumtemp_48 {
  data: ParameterTemp10,
}

/** Vorlauftemperatur Heizkreis, Parameter 00-002, Familienkennung 46. */
@id(0x6, 0x21, 0x00, 0x82, 0x00, 0x46)
model Hk_vl_temp_46 {
  data: ParameterTemp10,
}

/** Vorlauftemperatur Heizkreis, Parameter 00-002, Familienkennung 48. */
@id(0x6, 0x21, 0x00, 0x82, 0x00, 0x48)
model Hk_vl_temp_48 {
  data: ParameterTemp10,
}

/** Warmwassertemperatur, Parameter 00-004, Familienkennung 4a. */
@id(0x6, 0x21, 0x00, 0x84, 0x00, 0x4a)
model Ww_temp_4a {
  data: ParameterTemp10,
}

/** Wochentag, Parameter 02-073. */
@id(0x6, 0x21, 0x02, 0xc9, 0x00, 0x42)
model Wd {
  data: ParameterWochentag,
}

/** Einschaltzyklen des Kompressors, Parameter 02-080. */
@id(0x6, 0x21, 0x7d, 0x87, 0x00, 0x02)
model Sz_1 {
  data: ParameterZaehler,
}

/** Betriebsstunden des Kompressors, Parameter 02-081. */
@id(0x6, 0x21, 0x7d, 0x88, 0x00, 0x02)
model Bs_1 {
  data: ParameterBetriebsstunden,
}

/** Berechneter Raumtemperatur-Sollwert, Parameter 01-001. */
@id(0x6, 0x21, 0x03, 0xb3, 0x00, 0x46)
model Raumtemp_soll {
  parameterkopf: Parameterkopf,
  temp: temp10,
}

/** Schreibbarer Raumtemperatur-Sollwert, Parameter 01-001. */
@write
@zz(0x10)
@id(0x6, 0x23, 0x03, 0xb3, 0x00, 0x46)
model Raumtemp_soll_set {
  temp: temp10,
}

/** Berechneter Außentemperatur-Mittelwert, Parameter 02-020. */
@id(0x6, 0x21, 0x77, 0x84, 0x00, 0x0a)
model At_mittel {
  data: ParameterTemp10,
}

/**
 * Spar-Raumtemperatur Heizbetrieb, Parameter 03-053.
 * Entspricht vermutlich FB-Initialization.md "T Raum Absenkbetrieb".
 */
@id(0x6, 0x21, 0x63, 0x85, 0x00, 0x0a)
model Temp_raum_spar {
  data: ParameterTemp10,
}

/**
 * Raumschutztemperatur, Parameter 03-000.
 * Entspricht FB-Initialization.md Einsteller "3-0" (Raumschutztemperatur).
 */
@id(0x6, 0x21, 0x63, 0x80, 0x00, 0x0a)
model Temp_raumschutz {
  data: ParameterTemp10,
}

/**
 * Fusspunkt-Vorlauftemperatur Heizbetrieb, Parameter 03-001.
 * Entspricht FB-Initialization.md Einsteller "3-1" (Fusspunkttemperatur).
 */
@id(0x6, 0x21, 0x63, 0x81, 0x00, 0x0a)
model Temp_vl_fusspunkt {
  data: ParameterTemp10,
}

/**
 * Heizgrenze Sparbetrieb, Parameter 03-002.
 * Entspricht FB-Initialization.md Einsteller "3-2" (Heizgrenze Absenk).
 */
@id(0x6, 0x21, 0x63, 0x82, 0x00, 0x0a)
model Heizgrenze_spar {
  data: ParameterTemp10,
}

/**
 * Startoptimierung Vorhaltezeit, Parameter 03-006.
 * Entspricht FB-Initialization.md Einsteller "3-6" (Startoptimierung Vor.).
 */
@id(0x6, 0x21, 0x63, 0x83, 0x00, 0x0a)
model Startopt_vorhaltezeit {
  parameterkopf: Parameterkopf,
  time: Minuten10,
}

/**
 * Raumtemperatur-Kompensation (verstärkter Raumeinfluss), Parameter 03-007.
 * Entspricht FB-Initialization.md Einsteller "3-7" (Verst. Raumeinfluss).
 */
@id(0x6, 0x21, 0x63, 0x84, 0x00, 0x0a)
model Temp_raum_kompensation {
  parameterkopf: Parameterkopf,
  value: Faktor10,
}

/** Auslegungs-Vorlauftemperatur, Parameter 03-013. */
@id(0x6, 0x21, 0x63, 0x86, 0x00, 0x0a)
model Temp_vl_auslegung {
  data: ParameterTemp2,
}

/** Heizgrenze Normalbetrieb, Parameter 03-021. */
@id(0x6, 0x21, 0x63, 0x88, 0x00, 0x0a)
model Temp_heizgrenze_normal {
  data: ParameterTemp10,
}

/**
 * Normal-Raumtemperatur Heizbetrieb, Parameter 03-051.
 * Entspricht vermutlich FB-Initialization.md "T Raum Heizbetrieb" (dort ohne
 * Einsteller-Kürzel gelistet, aber mit "1-1" bezeichnet).
 */
@id(0x6, 0x21, 0x63, 0x8f, 0x00, 0x0a)
model Temp_raum_normal {
  data: ParameterTemp10,
}

/** Softwareversion, Parameter 04-092. */
@id(0x6, 0x21, 0x64, 0x91, 0x00, 0x00)
model Version_sw {
  data: ParameterVersion,
}

/** Hardwareversion, Parameter 04-093. */
@id(0x6, 0x21, 0x64, 0x92, 0x00, 0x00)
model Version_hw {
  data: ParameterVersion,
}

/**
 * DEFEKT
 * Normale Warmwassertemperatur, Parameter 05-051. Ungetestete Vermutung für
 * FB-Initialization.md "T Wasser" (Einsteller "1-4") - anders als die
 * 03-xxx-Heizkreisparameter oben liess sich diese Zuordnung nicht über
 * einen übereinstimmenden Nummern-Kürzel bestätigen, sondern nur über den
 * Parameternamen im Referenzprojekt (Ww_param1.userlevel.Temp_soll, Basis
 * 0x65, Familienkennung 0x0e). Bitte per ebusctl testen, bevor darauf
 * verlassen wird.
 */
//@id(0x6, 0x21, 0x65, 0x81, 0x00, 0x0e)
//model Ww_temp_soll {
//  data: ParameterTemp10,
//}

/**
 * Noch nicht fachlich benannter binärer Parameter (Abfrage `01 c2 00 4c`).
 *
 * Mitschnitt 2026-09-10:
 * `1506210401c2004c / 0ac2000200010000000000`
 * Der 10-Byte-Parameterkopf dekodiert zu: Kennung `c2 00`, Typ `0x02`
 * (on/off), Einheit `0x00`, Maximum 1, Minimum 0 und Wert 0 (`Aus`).
 * Die Kennung ist nicht im öffentlich verfügbaren TEM-15.tsp enthalten;
 * die fachliche Funktion bleibt daher offen.
 */
@id(0x6, 0x21, 0x01, 0xc2, 0x00, 0x4c)
model Parameter_01c2_4c {
  data: ParameterAusEin,
}

/**
 * Warmwasser-Sollwert
 * (Abfrage `05 b3 00 4c`).
 *
 * Mitschnitt 2026-09-10:
 * `1506210405b3004c / 0ab3428d02bc026400f401`
 * ergibt Kennung `b3 42`, Typ `0x8d` (Temperatur-Sollwert), Einheit °C,
 * Maximum 70,0 °C (`bc 02`), Minimum 10,0 °C (`64 00`) und Wert 50,0 °C
 * (`f4 01`). Der Wert stimmt mit „T Wasser“ in FB-Initialization.md überein.
 * Diese Zuordnung ist damit hoch plausibel; die interne Bedeutung der
 * Kennung `05 b3 00 4c` ist jedoch noch nicht dokumentiert.
 */
@id(0x6, 0x21, 0x05, 0xb3, 0x00, 0x4c)
model Ww_temp_soll {
  data: ParameterTemp10,
}

@write
@zz(0x10)
@id(0x6, 0x23, 0x05, 0xb3, 0x00, 0x4c)
model Ww_temp_soll_set {
  temp: temp10,
}

@id(0x6, 0x21, 0x01, 0x00, 0x00, 0x00)
model Betriebswahl1 {
  data: ParameterBetriebswahl,
}

@id(0x6, 0x21, 0x01, 0x00, 0x10, 0x00)
model Betriebswahl2 {
  data: ParameterBetriebswahl,
}

@write
@zz(0x10)
@id(0x6, 0x23, 0x01, 0x00, 0x00, 0x00)
model Betriebswahl1_set {
  data: BetriebswahlWert,
}

@write
@zz(0x10)
@id(0x6, 0x23, 0x01, 0x00, 0x10, 0x00)
model Betriebswahl2_set {
  data: BetriebswahlWert,
}
}