import "@ebusd/ebus-typespec";
import "./_templates.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;

namespace hautec;



scalar Zweistellen extends UCH;



scalar Byte extends UCH;


@unit("°C")

scalar Temp1Byte extends D1C;
// 0304


model Anlaufzaehler {
  Zweistellen: Zweistellen,
  Zweistellen_1: Zweistellen,
  Zweistellen_2: Zweistellen,
  Zweistellen_3: Zweistellen,
}


@unit("min")

scalar Minuten extends UCH;


@unit("h")

scalar Stunden extends HCD3;


@values(Values_HeizungsTyp)

scalar HeizungsTyp extends UCH;
// 0305


model Betriebsstunden {
  Minuten: Minuten,
  Stunden: Stunden,
  HeizungsTyp: HeizungsTyp,
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
  Status: StatusWaermeAnforderung,
  KesselSollT: KesselSollT,
  BrauchSollT: BrauchSollT,
  TAussenIst: TAussenIst,
  Stellgrad: Stellgrad,
}
// 0503


model BetriebsdatenAutomat {
  Statusanzeige: Statusanzeige,
  ldw: LDW,
  gdw: GDW,
  ws: WS,
  Flamme: Flamme,
  Ventil: Ventil1,
  Ventil_1: Ventil2,
  uwp: UWP,
  Alarm: Alarm,
  tf_hp: Temp1Byte,
  Kesseltemperatur: Temp1Byte,
  Ruecklauftemperatur: Ruecklauftemperatur,
  Boilertemperatur: Boilertemperatur,
  Aussentemperatur: Aussentemperatur,
}
// 050d

/** Raumtemperatur Soll */
@unit("°C")

scalar T_Room_target extends D1C;

/** Raumtemperatur Soll */
@unit("°C")

scalar T_Room extends D2C;


model ReglerToFA {
  T_Room_target: T_Room_target,
  T_Room: T_Room,
  b: Byte,
  b_1: Byte,
  b_2: Byte,
  b_3: Byte,
  b_4: Byte,
  b_5: Byte,
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


model ReadDateTime {
  CommandCode: CommandCode,
  MinutenSeit: MinutenSeit,
  DaysInEpoch: DaysInEpoch,
  WaterTemp: Temp,
  Four: Four,
  Key: Key,
}


model ReadMiscData {
  CommandCode: CommandCode,
  DayTemp: Temp,
  NightTemp: Temp,
  WaterTemp: Temp,
  Four: Four,
  Key: Key,
}


model TimeStatus {
  CommandCode: CommandCode,
  MinutenSeit: MinutenSeit,
  DaysInEpoch: DaysInEpoch,
  Six: Six,
  Key: Key,
}


model DataQuery {
  hex: HEX,
  Key: Key,
  Key_1: Key1,
  Key_2: Key2,
  Key_3: Key3,
  Val: Val1,
  Val_1: Val2,
  Val_2: Val3,
}

/** Is the previous data still valid */

scalar DataUnchanged extends BI7;



scalar Unknown4 extends HEX;


model DQAnswer {
  DataUnchanged: DataUnchanged,
  Unknown: Unknown4,
}


@divisor(10)

scalar Zehntel extends UIN;


@maxLength(2) 

scalar Zwei extends HEX;
// 100a 210c



scalar Steilheit extends UIN;


@unit("K")
@divisor(10)

scalar Hgr extends SIN;


model ReadMoreData {
  CommandCode: CommandCode,
  x: Temp,
  Hgr: Hgr,
  a: Zehntel,
  b: Zehntel,
  c: Zehntel,
  Key: Key,
}
// 100a 200d



scalar ChangeCounter extends UCH;


model ReadE3 {
  CommandCode: CommandCode,
  Zwei: Zwei,
  Heizgrenze: Zehntel,
  HeizGrAbs: Zehntel,
  StartVorhaltezeit: Zehntel,
  VerstRaumeinfluss: Zehntel,
  Key: Key,
}


@maxLength(10) 

scalar Zehn extends HEX;


model ReadE3X {
  CommandCode: CommandCode,
  RaumSchutz: Temp,
  Zehn: Zehn,
}



scalar Steil extends UCH;


@maxLength(7) 

scalar Sieben extends HEX;


model ReadE3Y {
  CommandCode: CommandCode,
  Steil: Steil,
  Sieben: Sieben,
  Fusspunkt: Temp,
  Key: Key,
}


model ReadE3Z {
  CommandCode: CommandCode,
  VorhaltX: Zehntel,
  Kuehl: Zehntel,
  a: Zwei,
  b: Zehntel,
  c: Zehntel,
  d: Zehntel,
}


model statx {
  CommandCode: CommandCode,
  T_Room: Zehntel,
  b: Byte,
  b_1: Byte,
}



model unknownx {
  hex_0: HEX,
  hex_1: HEX,
  hex_2: HEX,
  hex_3: HEX,
  hex_4: HEX,
  hex_5: HEX,
  hex_6: HEX,
  hex_7: HEX,
  hex_8: HEX,
  hex_9: HEX,
  hex_10: HEX,
  hex_11: HEX,
}
// 100a 3101


model Read3101 {
  Zwei: Zwei,
  Temp: Temp,
  Four: Four,
  Four_1: Four,
}
// 100a 3001


model CheckData {
  DayTemp: Temp,
  NightTemp: Temp,
  WaterTemp: Temp,
  Four: Four,
  Key: Key,
}
// 100a 3102


model Read3102 {
  Temp: Temp,
  sin: SIN,
  Zehntel: Zehntel,
  Zwei: Zwei,
  Zehntel_1: Zehntel,
  Zehntel_2: Zehntel,
}
// 100a 3002


model Read3002 {
  Four: Four,
  Temp: Temp,
  Zwei: Zwei,
  Temp_1: Temp,
  Key: Key,
}
// 100a 3103 0e


model Read3103 {
  Zehntel: Zehntel,
  Zehn: Zehn,
}
// 100a 3003


model Read3003 {
  Zehn: Zehn,
  Key: Key,
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

