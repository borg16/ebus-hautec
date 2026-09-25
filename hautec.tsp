import "@ebusd/ebus-typespec";
using Ebus;
using Ebus.Num;
using Ebus.Str;

namespace hautec;

scalar Zweistellen extends UCH;

scalar Byte extends UCH;

@unit("°C")
scalar Temp1Byte extends D1C;
// 0304

model Anlaufzaehler {
  Zweistellen: Zweistellen;
  Zweistellen_1: Zweistellen;
  Zweistellen_2: Zweistellen;
  Zweistellen_3: Zweistellen;
}

@unit("min")
scalar Minuten extends UCH;

@unit("h")
scalar Stunden extends HCD3;

@values(Values_HeizungsTyp)
scalar HeizungsTyp extends UCH;
// 0305

model Betriebsstunden {
  @out
  Minuten: Minuten;

  @out
  Stunden: Stunden;

  @out
  HeizungsTyp: HeizungsTyp;
}

@values(Values_Blocknummer)
scalar Blocknummer extends UCH;

/** Bei Fehler herstellerspezifischer Melde- oder Störcode */
scalar Statusanzeige extends UCH;

scalar ldw extends BI7;

scalar gdw extends BI6;

scalar ws extends BI5;

scalar Flamme extends BI4;

scalar Ventil1 extends BI3;

scalar Ventil2 extends BI2;

scalar uwp extends BI1;

scalar Alarm extends BI0;

/** Stellgrad zwischen minimaler und maximaler Kesselleistung */
@unit("%")
scalar Stellgrad extends UCH;

@unit("°C")
scalar Ruecklauftemperatur extends UCH;

@unit("°C")
scalar Boilertemperatur extends UCH;

@unit("°C")
scalar Aussentemperatur extends SCH;

@values(Values_StatusWaermeAnforderung)
scalar StatusWaermeAnforderung extends UCH;

/** Kesselsollwert */
@unit("°C")
scalar KesselSollT extends UCH;

/** Brauchwasser Sollwert TK */
@unit("°C")
scalar BrauchSollT extends UCH;

/** Aussentemp. Istwert */
@unit("°C")
scalar TAussenIst extends SCH;
// 0501

scalar LDW extends BI7;

scalar GDW extends BI6;

scalar WS extends BI5;

scalar UWP extends BI1;

model BetriebsdatenRegler {
  Status: StatusWaermeAnforderung;
  KesselSollT: KesselSollT;
  BrauchSollT: BrauchSollT;
  TAussenIst: TAussenIst;
  Stellgrad: Stellgrad;
}
// 0503

model BetriebsdatenAutomat {
  Statusanzeige: UCH;
  ldw: BI0;
  gdw: BI1;
  ws: BI2;
  flame: BI3;
  valve1: BI4;
  valve2: BI5;
  uwp: BI6;
  Alarm: BI7;
  @unit("%") SettingLevel: UCH;
  @unit("°C") BoilerTemperature: D1C;
  @unit("°C") ReturnWaterTemperature: UCH;
  @unit("°C") BoilerTemperature2: UCH;
  @unit("°C") OutsideTemperature: UCH;
}
// 050d

/** Raumtemperatur Soll */
@unit("°C")
scalar T_Room_target extends D1C;

/** Raumtemperatur Soll */
@unit("°C")
scalar T_Room extends D2C;

model RaumtemperaturdatenReglerAnFeuerungsautomat {
  T_Room_target: T_Room_target;
  T_Room: T_Room;
  b: Byte;
  b_1: Byte;
  b_2: Byte;
  b_3: Byte;
  b_4: Byte;
  b_5: Byte;
}

@maxLength(4)
scalar Four extends HEX;

@maxLength(6)
scalar Six extends HEX;
// 100a02

scalar Eins extends HEX;

@maxLength(3)
scalar Three extends HEX;

@unit("°C")
@divisor(10)
scalar Temp extends SIN;

@maxLength(2)
scalar CommandCode extends HEX;

/** Minuten seit ... */
@unit("min")
scalar MinutenSeit extends UIN;

/** Tage seit 1.1.1900 */
@unit("days")
scalar DaysInEpoch extends UIN;

@maxLength(2)
scalar Key extends HEX;

@maxLength(2)
scalar Key1 extends HEX;

@maxLength(2)
scalar Key2 extends HEX;

@maxLength(2)
scalar Key3 extends HEX;

scalar Val1 extends HEX;

scalar Val2 extends HEX;

scalar Val3 extends HEX;

scalar MyAddress extends HEX;

/** Zeitangaben und Warmwassertemperatur aus Menü 0A */
model ZeitUndWarmwassertemperatur {
  CommandCode: CommandCode;
  MinutenSeit: MinutenSeit;
  DaysInEpoch: DaysInEpoch;
  WaterTemp: Temp;
  Four: Four;
  Key: Key;
}

/** Tag-, Nacht- und Warmwasser-Solltemperatur aus Menü 0B */
model TemperaturSollwerte {
  CommandCode: CommandCode;
  DayTemp: Temp;
  NightTemp: Temp;
  WaterTemp: Temp;
  Four: Four;
  Key: Key;
}

/** Zeitstatusdaten */
model Zeitstatusdaten {
  @out
  CommandCode: CommandCode;

  @out
  MinutenSeit: MinutenSeit;

  @out
  DaysInEpoch: DaysInEpoch;

  @out
  Six: Six;

  @out
  Key: Key;
}

/** Abfrage, ob ein Bedienteil geänderte Daten bereitstellt */
model DatenAenderungsabfrage {
  @out
  hex: HEX;

  @out
  @maxLength(3)
  Key: HEX;

  @out
  @maxLength(9)
  Key_1: HEX;
}

/** Is the previous data still valid */
scalar DataUnchanged extends BI7;

scalar Unknown4 extends HEX;

/** Antwort auf eine Datenänderungsabfrage */
model DatenAenderungsantwort {
  @in
  DataUnchanged: DataUnchanged;

  @in
  Block: BCD;
}

@divisor(10)
scalar Zehntel extends UIN;

@divisor(10)
@unit("°C")
scalar Temp10 extends Num.SIN;

@maxLength(2)
scalar Zwei extends HEX;
// 100a 210c

scalar Steilheit extends UIN;

@unit("K")
@divisor(10)
scalar Hgr extends SIN;

/** Teilweise entschlüsselte Parameterdaten aus Block 21 0C */
model Parameterdaten210C {
  CommandCode: CommandCode;
  x: Temp;
  Hgr: Hgr;
  a: Zehntel;
  b: Zehntel;
  c: Zehntel;
  Key: Key;
}
// 100a 200d

scalar ChangeCounter extends UCH;

/** Heizgrenzen- und Raumeinflussparameter aus Block 20 0D */
model HeizgrenzenParameter200D {
  CommandCode: CommandCode;
  Zwei: Zwei;
  Heizgrenze: Zehntel;
  HeizGrAbs: Zehntel;
  StartVorhaltezeit: Zehntel;
  VerstRaumeinfluss: Zehntel;
  Key: Key;
}

@maxLength(10)
scalar Zehn extends HEX;

/** Teilweise entschlüsselte Raumschutzparameter aus Block 21 0D */
model RaumschutzParameter210D {
  CommandCode: CommandCode;
  RaumSchutz: Temp;
  Zehn: Zehn;
}

scalar Steil extends UCH;

@maxLength(7)
scalar Sieben extends HEX;

/** Teilweise entschlüsselte Heizkennlinienparameter aus Block 20 0C */
model HeizkennlinienParameter200C {
  CommandCode: CommandCode;
  Steil: Steil;
  Sieben: Sieben;
  Fusspunkt: Temp;
  Key: Key;
}

/** Teilweise entschlüsselte Kühlparameter aus Block 21 0B */
model KuehlParameter210B {
  CommandCode: CommandCode;
  VorhaltX: Zehntel;
  Kuehl: Zehntel;
  a: Zwei;
  b: Zehntel;
  c: Zehntel;
  d: Zehntel;
}

/** Anlagenschema / Applikationsnummer (Fachmann-Menü 09) */
@values(Values_Anlagenschema)
scalar Anlagenschema extends UCH;

/** Freigabe Zusatzerzeuger / Abluft-Waermepumpe im Heizkreis */
scalar ZusatzerzeugerFreigabe extends UCH;

/** reservierte/inaktive Funktionsbits, z.B. Ebene 09-03 bis 09-10 bei Menü 09 (Byte-Bedeutung je Menü ggf. abweichend) */
@maxLength(16)
scalar Reserviert8 extends HEX;

/** Kaskaden- oder Priorisierungswert */
scalar Kaskadenwert extends UCH;

// 100a 2009, siehe Protocol-Analysis.md Abschnitt 3 "Ebene 09"; letztes Byte bislang unbekannt/nicht dokumentiert
model Konfigurationsmatrix {
  Anlagenschema: Anlagenschema;
  ZusatzerzeugerFreigabe: ZusatzerzeugerFreigabe;
  Reserviert: Reserviert8;
  Kaskadenwert: Kaskadenwert;
  Reserved: Byte;
}

/** generische Fachmann-Konfiguration mit gleichem Byte-Layout wie Menü 09, Bedeutung der einzelnen Bytes je Menü noch nicht dokumentiert (Menüs 07, 08, 15, 17, 18, 19) */
model FachmannMatrix {
  b1: Byte;
  b2: Byte;
  Reserviert: Reserviert8;
  b13: Byte;
  b14: Byte;
}

@maxLength(12)
scalar Reserviert6 extends HEX;

/** Basis-Temperaturen: Raum-Soll Tag/Nacht, Warmwasser-Soll (Menü 01), siehe Protocol-Analysis.md Abschnitt 3 "Ebene 03" */
model BasisTemperaturen {
  RaumSollTag: Temp;
  RaumSollNacht: Temp;
  WarmwasserSoll: Temp;
  Reserviert: Reserviert6;
}

@maxLength(24)
scalar Roh12 extends HEX;

/** Heizkurven-Offset / Fusspunkt (Menü 03), Byte-Bedeutung noch nicht vollständig entschlüsselt, siehe Protocol-Analysis.md Abschnitt 3 */
model Heizgrenzen03Rohdaten {
  Rohdaten: Roh12;
}

/** Teilweise entschlüsselter Statusblock (Kennung 00 04 bzw. 00 05) */
model Statusblock {
  CommandCode: CommandCode;
  T_Room: Zehntel;
  b: Byte;
  b_1: Byte;
}

/** Noch nicht entschlüsselter Steuerblock */
model UnbekannterSteuerblock {
  @out
  hex_0: HEX;

  @out
  hex_1: HEX;

  @out
  hex_2: HEX;

  @out
  hex_3: HEX;

  @out
  hex_4: HEX;

  @out
  hex_5: HEX;

  @out
  hex_6: HEX;

  @out
  hex_7: HEX;

  @out
  hex_8: HEX;

  @out
  hex_9: HEX;

  @out
  hex_10: HEX;

  @out
  hex_11: HEX;
}
// 100a 3101

model Parameterdaten3101 {
  @out
  Zwei: Zwei;

  @out
  Temp: Temp;

  @out
  Four: Four;

  @out
  Four_1: Four;
}
// 100a 3001

/** Tag-, Nacht- und Warmwasser-Solltemperatur aus Block 30 01 */
model TemperaturSollwerte3001 {
  @out
  DayTemp: Temp;

  @out
  NightTemp: Temp;

  @out
  WaterTemp: Temp;

  @out
  Four: Four;

  @out
  Key: Key;
}
// 100a 3102

model Parameterdaten3102 {
  @out
  Temp: Temp;

  @out
  sin: SIN;

  @out
  Zehntel: Zehntel;

  @out
  Zwei: Zwei;

  @out
  Zehntel_1: Zehntel;

  @out
  Zehntel_2: Zehntel;
}
// 100a 3002

model Parameterdaten3002 {
  @out
  Four: Four;

  @out
  Temp: Temp;

  @out
  Zwei: Zwei;

  @out
  Temp_1: Temp;

  @out
  Key: Key;
}
// 100a 3103 0e

model Parameterdaten3103 {
  @out
  Zehntel: Zehntel;

  @out
  Zehn: Zehn;
}
// 100a 3003

model Parameterdaten3003 {
  @out
  Zehn: Zehn;

  @out
  Key: Key;
}

enum Values_HeizungsTyp {
  WP: 0,
  HS: 1,
}

enum Values_Blocknummer {
  UEbertragung_beenden: 0,
  Block_Nr_1_zyklisch_senden: 1,
  Block_Nr_2_einmalig_senden: 2,
}

enum Values_StatusWaermeAnforderung {
  Brennerabschalten: 0x00,
  Brauchwasserbereitung: 0x55,
  Heizbetrieb: 0xaa,
  Emissionskontrolle: 0xcc,
  TUEV_Funktion: 0xdd,
  Reglerstop_Funktion: 0xee,
}

enum Values_Anlagenschema {
  Standard_Heizkreis_WW: 0,
  Kuehlbetrieb: 4,
}
