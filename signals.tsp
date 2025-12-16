import "@ebusd/ebus-typespec";
import "./_templates.tsp";
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
model Betriebsstunden_1 {

@out

betriebsstunden: Betriebsstunden,
}

/** Gesamt Betriebsstunden 2 Stufe 1 lesen */
@qq(0x10)
@zz(0x91)
@id(0x3, 0x5)
model Betriebsstunden_2 {

@out

betriebsstunden: Betriebsstunden,
}

/** Betriebsdatenanforderung des Reglers an den Feuerungsautomaten 1 */
@write @passive 
@qq(0x10)
@zz(0x3)
@id(0x5, 0x2)
model AnfRegler2FA1 {


blocknummer: Blocknummer,
}

/** Betriebsdatenanforderung des Reglers an den Feuerungsautomaten 2 */
@write @passive 
@qq(0x10)
@zz(0x13)
@id(0x5, 0x2)
model AnfRegler2FA2 {


blocknummer: Blocknummer,
}

/** Betriebsdaten des Feuerungsautomaten 1 an den Regler */
@write @passive 
@qq(0x3)
@zz(0x10)
@id(0x5, 0x3, 1)
model ToRegler1 {


betriebsdaten: BetriebsdatenAutomat,
}

/** Betriebsdaten des Feuerungsautomaten 2 an den Regler */
@write @passive 
@qq(0x13)
@zz(0x10)
@id(0x5, 0x3, 1)
model ToRegler2 {


betriebsdaten: BetriebsdatenAutomat,
}

/** Konfigurationsdatenanforderung des Reglers an den Feuerungsautomaten 1 */
@write @passive 
@qq(0x10)
@zz(0x3)
@id(0x5, 0xa)
model ConfAnfToFA1 {
}

/** Konfigurationsdatenanforderung des Reglers an den Feuerungsautomaten 2 */
@write @passive 
@qq(0x10)
@zz(0x13)
@id(0x5, 0xa)
model ConfAnfToFA2 {
}

/** Konfigurationsdatenanforderung des Reglers an Slave 1 */
@write @passive 
@qq(0x10)
@zz(0x90)
@id(0x5, 0xa)
model ConfAnfToS1 {
}

/** Konfigurationsdatenanforderung des Reglers an Slave 2 */
@write @passive 
@qq(0x10)
@zz(0x91)
@id(0x5, 0xa)
model ConfAnfToS2 {
}

/** identification */
@qq(0x10)
@zz(0x8)
@id(0x7, 0x4)
model Idx {
/** device manufacturer */
@values(Values_manufacturer)

manufacturer: UCH,
/** device id */

id: UCH,
}

@zz(0x90)
@id(0x10, 0xa, 0, 0x4)
model Statx1 {

@in

data: statx,
}

@zz(0x91)
@id(0x10, 0xa, 0, 0x4)
model Statx2 {

@in

data: statx,
}

@zz(0x90)
@id(0x10, 0xa, 0, 0x5)
model Staty1 {

@in

data: statx,
}

@zz(0x91)
@id(0x10, 0xa, 0, 0x5)
model Staty2 {

@in

data: statx,
}

/** Have Data Q1 */
@zz(0x90)
@id(0x10, 0xa, 0xd0)
model HaveDataQuery1 {

@out

DataQ: DataQuery,

@in

Answer: DQAnswer,
}

/** Have Data Q2 */
@zz(0x91)
@id(0x10, 0xa, 0xd0)
model HaveDataQuery2 {

@out

DataQ: DataQuery,

@in

Answer: DQAnswer,
}

/** aus 1. Bedienteil */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0xa)
model Read0a_1 {

@in

data1: ReadDateTime,
}

/** aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xa)
model Read0a_2 {

@in

data2: ReadDateTime,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0xb)
model Read0b1_1 {

@in

data: ReadE3Z,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xb)
model Read0b1_2 {

@in

data: ReadE3Z,
}

/** aus 1. Bedienteil */
@zz(0x90)
@id(0x10, 0xa, 0x20, 0xb)
model Read0b2_1 {

@in

data: ReadMiscData,
}

/** aus 1. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xb)
model Read0b2_2 {

@in

data: ReadMiscData,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0xc)
model Read0c1_1 {

@in

data: ReadMoreData,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xc)
model Read0c1_2 {

@in

data: ReadMoreData,
}

@zz(0x90)
@id(0x10, 0xa, 0x20, 0xc)
model Read0c2_1 {

@in

data: ReadE3Y,
}

@zz(0x91)
@id(0x10, 0xa, 0x20, 0xc)
model Read0c2_2 {

@in

data: ReadE3Y,
}

@zz(0x90)
@id(0x10, 0xa, 0x21, 0xd)
model Read0D1_1 {

@in

data: ReadE3X,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xd)
model Read0D1_2 {

@in

data: ReadE3X,
}

@zz(0x90)
@id(0x10, 0xa, 0x20, 0xd)
model Read0D2_1 {

@in

data: ReadE3,
}

@zz(0x91)
@id(0x10, 0xa, 0x20, 0xd)
model Read0D2_2 {

@in

data: ReadE3,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 0)
model TimeStatus1 {

@out

data: TimeStatus,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0)
model TimeStatus2 {

@out

data: TimeStatus,
}

@zz(0x90)
@id(0x10, 0xa, 0x31, 1)
model Read3101_1 {

@out

data: Read3101,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 1)
model Read3101_2 {

@out

data: Read3101,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 1)
model CheckData1 {

@out

data: CheckData,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 1)
model CheckData2 {

@out

data: CheckData,
}

@zz(0x90)
@id(0x10, 0xa, 0x31, 0x2)
model Read3102_1 {

@out

data: Read3102,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 0x2)
model Read3102_2 {

@out

data: Read3102,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 0x2)
model Read3002_1 {

@out

data: Read3002,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0x2)
model Read3002_2 {

@out

data: Read3002,
}

@zz(0x90)
@id(0x10, 0xa, 0x31, 0x3)
model Read3103_1 {

@out

data: Read3103,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 0x3)
model Read3103_2 {

@out

data: Read3103,
}

@zz(0x90)
@id(0x10, 0xa, 0x30, 0x3)
model Read3003_1 {

@out

data: Read3003,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0x3)
model Read3003_2 {

@out

data: Read3003,
}

@zz(0x90)
@id(0x10, 0xa, 0xd1, 0x14)
model Read_d114_1 {

@out

data: unknownx,
}

@zz(0x91)
@id(0x10, 0xa, 0xd1, 0x14)
model Read_d114_2 {

@out

data: unknownx,
}

@zz(0x90)
@id(0x10, 0xa, 0xd1, 0x15)
model Read_d115_1 {

@out

data: unknownx,
}

@zz(0x91)
@id(0x10, 0xa, 0xd1, 0x15)
model Read_d115_2 {

@out

data: unknownx,
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

