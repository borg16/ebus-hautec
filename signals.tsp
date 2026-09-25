import "@ebusd/ebus-typespec";
import "./hautec.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec;

namespace Signals {
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
