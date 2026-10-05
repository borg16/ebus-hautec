import "@ebusd/ebus-typespec";
using Ebus;
using Ebus.Num;
using Ebus.Str;

namespace hautec;

/** Standard identification payload (07 04), shared by replies and broadcasts. */
model IdentificationData {
  /** Device manufacturer. */
  manufacturer: Ebus.Id.manufacturer;
  /** Five-character device identifier. */
  @maxLength(5)
  id: STR;
  /** Software version and revision, four BCD digits in wire order. */
  softwareVersion: PIN;
  /** Hardware version and revision, four BCD digits in wire order. */
  hardwareVersion: PIN;
}

// 05 01 / 05 03 use 0x3f for unavailable outside temperature (OSI 7 pp. 17, 19).
// ebusd cannot override SCH's replacement byte in CSV. Its value-list fallback
// returns unsigned wire values, so explicitly map every valid negative SCH byte.
// Normal reads show signed temperatures or "unavailable"; numeric enum reads (-n)
// expose wire codes. JSON encodes mapped values as strings. See the coverage audit.
enum OutsideTemperatureSpecialValues {
  unavailable: 0x3f,
  "-127": 0x81,
  "-126": 0x82,
  "-125": 0x83,
  "-124": 0x84,
  "-123": 0x85,
  "-122": 0x86,
  "-121": 0x87,
  "-120": 0x88,
  "-119": 0x89,
  "-118": 0x8a,
  "-117": 0x8b,
  "-116": 0x8c,
  "-115": 0x8d,
  "-114": 0x8e,
  "-113": 0x8f,
  "-112": 0x90,
  "-111": 0x91,
  "-110": 0x92,
  "-109": 0x93,
  "-108": 0x94,
  "-107": 0x95,
  "-106": 0x96,
  "-105": 0x97,
  "-104": 0x98,
  "-103": 0x99,
  "-102": 0x9a,
  "-101": 0x9b,
  "-100": 0x9c,
  "-99": 0x9d,
  "-98": 0x9e,
  "-97": 0x9f,
  "-96": 0xa0,
  "-95": 0xa1,
  "-94": 0xa2,
  "-93": 0xa3,
  "-92": 0xa4,
  "-91": 0xa5,
  "-90": 0xa6,
  "-89": 0xa7,
  "-88": 0xa8,
  "-87": 0xa9,
  "-86": 0xaa,
  "-85": 0xab,
  "-84": 0xac,
  "-83": 0xad,
  "-82": 0xae,
  "-81": 0xaf,
  "-80": 0xb0,
  "-79": 0xb1,
  "-78": 0xb2,
  "-77": 0xb3,
  "-76": 0xb4,
  "-75": 0xb5,
  "-74": 0xb6,
  "-73": 0xb7,
  "-72": 0xb8,
  "-71": 0xb9,
  "-70": 0xba,
  "-69": 0xbb,
  "-68": 0xbc,
  "-67": 0xbd,
  "-66": 0xbe,
  "-65": 0xbf,
  "-64": 0xc0,
  "-63": 0xc1,
  "-62": 0xc2,
  "-61": 0xc3,
  "-60": 0xc4,
  "-59": 0xc5,
  "-58": 0xc6,
  "-57": 0xc7,
  "-56": 0xc8,
  "-55": 0xc9,
  "-54": 0xca,
  "-53": 0xcb,
  "-52": 0xcc,
  "-51": 0xcd,
  "-50": 0xce,
  "-49": 0xcf,
  "-48": 0xd0,
  "-47": 0xd1,
  "-46": 0xd2,
  "-45": 0xd3,
  "-44": 0xd4,
  "-43": 0xd5,
  "-42": 0xd6,
  "-41": 0xd7,
  "-40": 0xd8,
  "-39": 0xd9,
  "-38": 0xda,
  "-37": 0xdb,
  "-36": 0xdc,
  "-35": 0xdd,
  "-34": 0xde,
  "-33": 0xdf,
  "-32": 0xe0,
  "-31": 0xe1,
  "-30": 0xe2,
  "-29": 0xe3,
  "-28": 0xe4,
  "-27": 0xe5,
  "-26": 0xe6,
  "-25": 0xe7,
  "-24": 0xe8,
  "-23": 0xe9,
  "-22": 0xea,
  "-21": 0xeb,
  "-20": 0xec,
  "-19": 0xed,
  "-18": 0xee,
  "-17": 0xef,
  "-16": 0xf0,
  "-15": 0xf1,
  "-14": 0xf2,
  "-13": 0xf3,
  "-12": 0xf4,
  "-11": 0xf5,
  "-10": 0xf6,
  "-9": 0xf7,
  "-8": 0xf8,
  "-7": 0xf9,
  "-6": 0xfa,
  "-5": 0xfb,
  "-4": 0xfc,
  "-3": 0xfd,
  "-2": 0xfe,
  "-1": 0xff,
}

/** Signed outside temperature; 0x3f unavailable, 0x80 SCH replacement. */
@values(OutsideTemperatureSpecialValues)
@unit("°C")
scalar OutsideTemperature1Byte extends SCH;

scalar TwoDigits extends UCH;

scalar Byte extends UCH;

@unit("°C")
scalar Temp1Byte extends D1C;
// 0304

model StartCounter {
  digits: TwoDigits;
  digits_1: TwoDigits;
  digits_2: TwoDigits;
  digits_3: TwoDigits;
}

@unit("min")
scalar Minutes extends UCH;

@unit("h")
scalar Hours extends HCD3;

@values(Values_HeatingType)
scalar HeatingType extends UCH;
// 0305

model OperatingHours {
  @out
  minutes: Minutes;

  @out
  hours: Hours;

  @out
  heatingId: UCH;
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
scalar Aussentemperatur extends OutsideTemperature1Byte;

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
scalar TAussenIst extends OutsideTemperature1Byte;
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
  /** Controller performance demand, not a measured terminal or M17 command.
   * Do not equate this with the returned SettingLevel in 05 03. */
  Stellgrad: Stellgrad;
}
// 0503

model BetriebsdatenAutomat {
  Statusanzeige: UCH;
  ldw: BI0;
  gdw: BI1;
  ws: BI2;
  /** Standard burner label. On this heat-pump controller it is not an
   * independently validated compressor-current or M17 fan indication. */
  flame: BI3;
  valve1: BI4;
  valve2: BI5;
  /** Standard pump-status bit. For FA1 (03 -> 10), correlates with
   * Broadcast.Status0a.Bit3 (1250/1257 next-message pairs on 2026-10-03).
   * Candidate for source/heat-pump pump enable, possibly TEM 3; physical
   * output unverified. Not the long-run-on heating pump candidate Running.
   * M17 additionally requires closed K1 contact 31-34, behind K4/K7 interlocks.
   * uwp alone proves neither fan voltage/current nor a direct fan command.
   * This shared model also serves FA2; the FA1 evidence does not map FA2. */
  uwp: BI6;
  Alarm: BI7;
  /** FA1 reports 0/50/100 stage levels; 50% does not prove a running air-source
   * compressor (it was reported while that compressor was off during cooling).
   * 100% can persist during an inferred ground-source compressor pause in DHW.
   * Not a measured fan speed, M17 state, or one-to-one physical compressor ID.
   * See docs/Heating-Terminal-Analysis-2026-10-03.md. */
  @unit("%") SettingLevel: UCH;
  @unit("°C") BoilerTemperature: D1C;
  @unit("°C") ReturnWaterTemperature: UCH;
  @unit("°C") BoilerTemperature2: UCH;
  OutsideTemperature: OutsideTemperature1Byte;
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
  /** Status byte: bit 0 indicates hot-water preparation in the standard; observed as zero. */
  hotWaterPreparationActive: BI0;
  /** Reserved payload bytes 4..9, including the final byte; observed as 00 80 00 80 FF FF. */
  @maxLength(6)
  reserved: IGN;
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

/** Controller time synchronization payload after the 30 00 selector (12 bytes).
 * See docs/FB-Initialization.md for capture evidence and the unresolved date epoch.
 */
model RemoteTimeSyncData {
  /** Minutes since Monday 00:00, inferred from Tuesday, Wednesday and Sunday captures. */
  @unit("min")
  minutesSinceMonday: UIN;

  /** Raw TEM day counter; interpreting it as days since 1900-01-01 is one day ahead. */
  @unit("days")
  dayCounter: UIN;

  /** Unknown bytes, observed as EF EF EF EF EF EF; retained for analysis. */
  @maxLength(6)
  unknownData: HEX;

  /** Opaque synchronization key, also seen in the D0 14 payload; semantics unconfirmed. */
  @maxLength(2)
  syncKey: HEX;
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

enum Values_HeatingType {
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
