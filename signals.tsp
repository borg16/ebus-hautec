import "@ebusd/ebus-typespec";
import "./hautec.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec;

namespace Signals {
// [anlauftyp2=1]r,ehp,anlaufzaehler_HS2,Gesamt Anlaufzähler 2 lesen HS,10,91,0304,anlaufzaehler,m,HCD:3,number,m,UCH

/** Gesamt Betriebsstunden 1 Stufe 1 lesen */
@qq(0x10)
@zz(0x90)
@id(0x3, 0x5)
model BetriebsstundenBedienteil1 {

@out

betriebsstunden: Betriebsstunden,
}

/** Gesamt Betriebsstunden 2 Stufe 1 lesen */
@qq(0x10)
@zz(0x91)
@id(0x3, 0x5)
model BetriebsstundenBedienteil2 {

@out

betriebsstunden: Betriebsstunden,
}

/** Betriebsdatenanforderung des Reglers an den Feuerungsautomaten 1 */
@write @passive 
@qq(0x10)
@zz(0x3)
@id(0x5, 0x2)
model BetriebsdatenAnforderungReglerAnFeuerungsautomat1 {


blocknummer: Blocknummer,
}

/** Betriebsdatenanforderung des Reglers an den Feuerungsautomaten 2 */
@write @passive 
@qq(0x10)
@zz(0x13)
@id(0x5, 0x2)
model BetriebsdatenAnforderungReglerAnFeuerungsautomat2 {


blocknummer: Blocknummer,
}

/** Betriebsdaten des Feuerungsautomaten 1 an den Regler */
@write @passive 
@qq(0x3)
@zz(0x10)
@id(0x5, 0x3, 1)
model BetriebsdatenFeuerungsautomat1AnRegler {


betriebsdaten: BetriebsdatenAutomat,
}

/** Betriebsdaten des Feuerungsautomaten 2 an den Regler */
@write @passive 
@qq(0x13)
@zz(0x10)
@id(0x5, 0x3, 1)
model BetriebsdatenFeuerungsautomat2AnRegler {


betriebsdaten: BetriebsdatenAutomat,
}

/** Konfigurationsdatenanforderung des Reglers an den Feuerungsautomaten 1 */
@write @passive 
@qq(0x10)
@zz(0x3)
@id(0x5, 0xa)
model KonfigurationsAnforderungReglerAnFeuerungsautomat1 {
}

/** Konfigurationsdatenanforderung des Reglers an den Feuerungsautomaten 2 */
@write @passive 
@qq(0x10)
@zz(0x13)
@id(0x5, 0xa)
model KonfigurationsAnforderungReglerAnFeuerungsautomat2 {
}

/** Konfigurationsdatenanforderung des Reglers an Slave 1 */
@write @passive 
@qq(0x10)
@zz(0x90)
@id(0x5, 0xa)
model KonfigurationsAnforderungReglerAnBedienteil1 {
}

/** Konfigurationsdatenanforderung des Reglers an Slave 2 */
@write @passive 
@qq(0x10)
@zz(0x91)
@id(0x5, 0xa)
model KonfigurationsAnforderungReglerAnBedienteil2 {
}

/** Geräteidentifikation */
@qq(0x10)
@zz(0x8)
@id(0x7, 0x4)
model Geraeteidentifikation {
/** device manufacturer */
@values(Values_manufacturer)

manufacturer: UCH,
/** device id */

id: UCH,
}

@zz(0x90)
@id(0x10, 0xa, 0, 0x4)
model Statusblock04Bedienteil1 {

@in

data: Statusblock,
}

@zz(0x91)
@id(0x10, 0xa, 0, 0x4)
model Statusblock04Bedienteil2 {

@in

data: Statusblock,
}

@zz(0x90)
@id(0x10, 0xa, 0, 0x5)
model Statusblock05Bedienteil1 {

@in

data: Statusblock,
}

@zz(0x91)
@id(0x10, 0xa, 0, 0x5)
model Statusblock05Bedienteil2 {

@in

data: Statusblock,
}

/** Änderungsabfrage an Bedienteil 1 */
@zz(0x90)
@id(0x10, 0xa, 0xd0)
model DatenAenderungsabfrageBedienteil1 {

@out

DataQ: DatenAenderungsabfrage,

@in

Answer: DatenAenderungsantwort,
}

/** Änderungsabfrage an Bedienteil 2 */
@zz(0x91)
@id(0x10, 0xa, 0xd0)
model DatenAenderungsabfrageBedienteil2 {

@out

DataQ: DatenAenderungsabfrage,

@in

Answer: DatenAenderungsantwort,
}

/** Datum und Uhrzeit aus Bedienteil 1 */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0xa)
model DatumUhrzeitBedienteil1 {

@in

data1: ZeitUndWarmwassertemperatur,
}

/** Datum und Uhrzeit aus Bedienteil 2 */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xa)
model DatumUhrzeitBedienteil2 {

@in

data2: ZeitUndWarmwassertemperatur,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0xb)
model Parameterblock210BBedienteil1 {

@in

data: KuehlParameter210B,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xb)
model Parameterblock210BBedienteil2 {

@in

data: KuehlParameter210B,
}

/** Temperatur-Sollwerte aus Bedienteil 1 */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0xb)
model TemperaturSollwerte200BBedienteil1 {

@in

data: TemperaturSollwerte,
}

/** Temperatur-Sollwerte aus Bedienteil 2 */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xb)
model TemperaturSollwerte200BBedienteil2 {

@in

data: TemperaturSollwerte,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0xc)
model Parameterblock210CBedienteil1 {

@in

data: Parameterdaten210C,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xc)
model Parameterblock210CBedienteil2 {

@in

data: Parameterdaten210C,
}

@zz(0x90)
@id(0x10, 0xa, 0x20, 0xc)
model Heizkennlinie200CBedienteil1 {

@in

data: HeizkennlinienParameter200C,
}

@zz(0x91)
@id(0x10, 0xa, 0x20, 0xc)
model Heizkennlinie200CBedienteil2 {

@in

data: HeizkennlinienParameter200C,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0xd)
model Parameterblock210DBedienteil1 {

@in

data: RaumschutzParameter210D,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xd)
model Parameterblock210DBedienteil2 {

@in

data: RaumschutzParameter210D,
}

@zz(0x90)
@id(0x10, 0xa, 0x20, 0xd)
model Heizgrenzen200DBedienteil1 {

@in

data: HeizgrenzenParameter200D,
}

@zz(0x91)
@id(0x10, 0xa, 0x20, 0xd)
model Heizgrenzen200DBedienteil2 {

@in

data: HeizgrenzenParameter200D,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 0)
model ZeitstatusBedienteil1 {

@out

data: Zeitstatusdaten,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0)
model ZeitstatusBedienteil2 {

@out

data: Zeitstatusdaten,
}

@zz(0x90)
@id(0x10, 0xa, 0x31, 1)
model Parameterblock3101Bedienteil1 {

@out

data: Parameterdaten3101,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 1)
model Parameterblock3101Bedienteil2 {

@out

data: Parameterdaten3101,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 1)
model TemperaturSollwerte3001Bedienteil1 {

@out

data: TemperaturSollwerte3001,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 1)
model TemperaturSollwerte3001Bedienteil2 {

@out

data: TemperaturSollwerte3001,
}

@zz(0x90)
@id(0x10, 0xa, 0x31, 0x2)
model Parameterblock3102Bedienteil1 {

@out

data: Parameterdaten3102,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 0x2)
model Parameterblock3102Bedienteil2 {

@out

data: Parameterdaten3102,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 0x2)
model Parameterblock3002Bedienteil1 {

@out

data: Parameterdaten3002,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0x2)
model Parameterblock3002Bedienteil2 {

@out

data: Parameterdaten3002,
}

@zz(0x90)
@id(0x10, 0xa, 0x31, 0x3)
model Parameterblock3103Bedienteil1 {

@out

data: Parameterdaten3103,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 0x3)
model Parameterblock3103Bedienteil2 {

@out

data: Parameterdaten3103,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 0x3)
model Parameterblock3003Bedienteil1 {

@out

data: Parameterdaten3003,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0x3)
model Parameterblock3003Bedienteil2 {

@out

data: Parameterdaten3003,
}

@zz(0x90)
@id(0x10, 0xa, 0xd1, 0x14)
model SteuerblockD114Bedienteil1 {

@out

data: UnbekannterSteuerblock,
}

@zz(0x91)
@id(0x10, 0xa, 0xd1, 0x14)
model SteuerblockD114Bedienteil2 {

@out

data: UnbekannterSteuerblock,
}

@zz(0x90)
@id(0x10, 0xa, 0xd1, 0x15)
model SteuerblockD115Bedienteil1 {

@out

data: UnbekannterSteuerblock,
}

@zz(0x91)
@id(0x10, 0xa, 0xd1, 0x15)
model SteuerblockD115Bedienteil2 {

@out

data: UnbekannterSteuerblock,
}

/** Fachmann-Konfigurationsmatrix (Anlagenschema, Zusatzerzeuger-Freigabe, Kaskadenwert), Menü 09, aus 1. Bedienteil */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0x9)
model FachmannKonfiguration09Bedienteil1 {

@in

data: Konfigurationsmatrix,
}

/** Fachmann-Konfigurationsmatrix (Anlagenschema, Zusatzerzeuger-Freigabe, Kaskadenwert), Menü 09, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x9)
model FachmannKonfiguration09Bedienteil2 {

@in

data: Konfigurationsmatrix,
}

@zz(0x90)
@id(0x10, 0xa, 0x20, 0x0)
model Menueblock00Bedienteil1 {
  Ebene: BCD;
  Block: BCD;
  @maxLength(10)
  Data: HEX;
  @maxLength(2)
  Data2: HEX;
}

/** Basis-Temperaturen (Raum-Soll Tag/Nacht, Warmwasser-Soll), Menü 01, aus 1. Bedienteil */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0x1)
model BasisTemperaturen01Bedienteil1 {

Ebene: BCD,
Block: BCD,
T_Room_target_Day: Temp10,
T_Room_target_Night: Temp10,
T_Water_target: Temp10,
@maxLength(6)
Reserviert2: HEX
}

/** Heizgrenzen, Menü 03, aus Bedienteil 1 */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0x3)
model Heizgrenzen03Bedienteil1 {
Ebene: BCD;
Block: BCD;

@maxLength(2)
Reserved: HEX;
Heizgrenze: Temp10;
HeizgrenzeAbsenk: Temp10;
@maxLength(6)
Reserved2: HEX;
}

/** Fachmann-Konfiguration, Menü 07, aus 1. Bedienteil */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0x7)
model FachmannKonfiguration07Bedienteil1 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 08, aus 1. Bedienteil */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0x8)
model FachmannKonfiguration08Bedienteil1 {

@in

data: FachmannMatrix,
}

/** Kerndaten der Wärmepumpen-Stufen, Menü 15, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xf)
model WaermepumpenStufenKonfiguration15Bedienteil2 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 17, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x11)
model FachmannKonfiguration17Bedienteil2 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 18, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x12)
model FachmannKonfiguration18Bedienteil2 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 19, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x13)
model FachmannKonfiguration19Bedienteil2 {

@in

data: FachmannMatrix,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0x01)
model Kuehlgrenzen2101Bedienteil1 {

Ebene: BCD;
Block: BCD;
@maxLength(2)
Null1: HEX;
Base_temp: Temp10;
Null2: HEX;
@divisor(10) @unit("K")
CoolingLimitDistance: SIN;
@maxLength(4)
Null3: HEX;
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0x03)
model Raumschutz2103Bedienteil1 {

Ebene: BCD;
Block: BCD;
Room_protection_temp: Temp10;
Data: UCH;
@maxLength(7)
Nulls: HEX;
@maxLength(2)
Data2: HEX;
}

enum Values_manufacturer {
  Dungs: 0x06,
  FH_Ostfalia: 0x0f,
  TEM: 0x10,
  Lamberti: 0x11,
  CEB: 0x14,
  Landis_Staefa: 0x15,
  FERRO: 0x16,
  MONDIAL: 0x17,
  Wikon: 0x18,
  Wolf: 0x19,
  RAWE: 0x20,
  Satronic: 0x30,
  ENCON: 0x40,
  Kromschroeder: 0x50,
  Eberle: 0x60,
  EBV: 0x65,
  Graesslin: 0x75,
  ebm_papst: 0x85,
  SIG: 0x95,
  Theben: 0xa5,
  Thermowatt: 0xa7,
  Vaillant: 0xb5,
  Toby: 0xc0,
  Weishaupt: 0xc5,
  ebusd_eu: 0xfd,
}
}
