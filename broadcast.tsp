import "@ebusd/ebus-typespec";
import "./_templates.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec;

namespace Broadcast {

/** default *r */
model r {
}

/** default *b */
@passive 
@zz(BROADCAST)
model b {
}

/** default *w */
@write 
@zz(BROADCAST)
model w {
}

/** date/time */
@passive 
@id(0x7, 0)
model Datetime {
/** Outside temperature */
@unit("°C")

ta: D2B,


time: BTI,


date: BDA,
}
// r;b,id,identification,0704,manufacturer,UCH,0x06=Dungs;0x0f=FH Ostfalia;0x10=TEM;0x11=Lamberti;0x14=CEB;0x15=Landis-Staefa;0x16=FERRO;0x17=MONDIAL;0x18=Wikon;0x19=Wolf;0x20=RAWE;0x30=Satronic;0x40=ENCON;0x50=Kromschröder;0x60=Eberle;0x65=EBV;0x75=Grässlin;0x85=ebm-papst;0x95=SIG;0xa5=Theben;0xa7=Thermowatt;0xb5=Vaillant;0xc0=Toby;0xc5=Weishaupt;0xfd=ebusd.eu,device manufacturer,id,STR:5,device id,software,PIN,software version,hardware,PIN,hardware versionr

/** identification */
@inherit(r, b)
@ext(0x7, 0x4)
model Id {
/** device manufacturer */
@values(Values_manufacturer)

manufacturer: UCH,
/** device id */

id: UCH,
}

/** identification */
@write 
@zz(BROADCAST)
@id(0x7, 0x4)
model IdWrite {
}

/** Inquiry of existence */
@write 
@zz(BROADCAST)
@id(0x7, 0xfe)
model Queryexistence {
}

/** sign of life */
@passive 
@id(0x7, 0xff)
model Signoflife {
}

/** error message */
@passive 
@id(0xfe, 1)
model Error {

@maxLength(10) 

error: STR,
}

/** reset network start */
@passive 
@id(0xff, 0)
model Netresetstate {
}

/** reset network configuration */
@passive 
@id(0xff, 1)
model Netresetcfg {
}

/** network loss */
@passive 
@id(0xff, 0x2)
model Netloss {
}

/** Betriebsdaten des Reglers an den Feuerungsautomaten 1 */
@passive 
@id(0x5, 0xd)
model ToFAxSub {


daten: ReglerToFA,
}

/** Betriebsdaten des Reglers an andere Regler */
@passive 
@id(0x8, 1)
model ToCtrl {

@unit("°C")

tr_hp: D2B,

@unit("°C")

tb: D2B,


Emissionstest: UCH,


BWR_Aktiv: BI0,


PumpenFreigabeSperre: BI1,


Kessel1InBetrieb: BI2,


Kessel2InBetrieb: BI3,


Ladepumpe: BI4,


BW_Ladung: BI5,


TBF_Connect: BI6,

@unit("°C")

tr_hp2: D2B,
}

/** Master-Regler an Slave-Regler */
@passive 
@id(0x8, 0x2)
model ToSlaveCtrl {


Bit0: BI0,


Bit1: BI1,


Bit2: BI2,


Bit3: BI3,


Bit4: BI4,


Bit5: BI5,


Bit6: BI6,


Bit7: BI7,


Bit8: BI0,


Bit9: BI1,


Bit10: BI2,


Bit11: BI3,


Bit12: BI4,


Bit13: BI5,


Bit14: BI6,


Bit15: BI7,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x11, 0)
model Status0a {


ta: Temp,


Bit0: BI0,


Bit1: BI1,


Bit2: BI2,


Bit3: BI3,


Bit4: BI4,


Bit5: BI5,


Bit6: BI6,


Bit7: BI7,


Bit8: BI0,


Bit9: BI1,


Bit10: BI2,


Bit11: BI3,


Bit12: BI4,


Bit13: BI5,


Bit14: BI6,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x10, 0)
model Status0b {
/** Heat pump flow temperature */
@unit("°C")

tf_hp: Temp,
/** Heat pump return temperature */
@unit("°C")

tr_hp: Temp,
/** Heating circuit flow temperature */
@unit("°C")

tf_hc: Temp,


b1: Byte,


b2: Byte,


tb: Temp,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x11, 1)
model Status1a {


ta: Temp,


Flag0: BI0,
Flag1: BI1,
Flag2: BI2,
Flag3: BI3,
Flag4: BI4,
Flag5: BI5,
Flag6: BI6,
Flag7: BI7,


Bit0: BI0,


Bit1: BI1,


Bit2: BI2,


Bit3: BI3,


Bit4: BI4,


Bit5: BI5,


Bit6: BI6,

Bit7: BI7,

b2: Byte,

b3: Byte,

b4: Byte,

b5: Byte,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x10, 1)
model Status1b {
/** Heat pump flow temperature */
@unit("°C")

tf_hp: Temp,


n1: Zehntel,


tr: Temp,


n2: Zehntel,
/** software water temperature */
@unit("°C")

tb: Temp,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x11, 0x2)
model Status2a {


b1: Byte,


b2: Byte,


Mins: UIN,


b3: Byte,


b4: Byte,


b5: Byte,


b6: Byte,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x10, 0x2)
model Status2b {


Bit0: BI0,


Bit1: BI1,


Bit2: BI2,


Bit3: BI3,


Bit4: BI4,


Bit5: BI5,


Bit6: BI6,


Bit7: BI7,


Bit8: BI0,


Bit9: BI1,


Bit10: BI2,


Bit11: BI3,


Bit12: BI4,


Bit13: BI5,


Bit14: BI6,


Bit15: BI7,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x11, 0x3)
model Status3a {


b1: Byte,


b2: Byte,
/** Minutes since Tuesday 00:00 */

Mins: UIN,


b5: Byte,


b6: Byte,


qB3: Byte,


b4: Byte,
}

/** xxx */
@passive 
@id(0x10, 0xa, 0x10, 0x3)
model Status3b {


n1: Zehntel,


n2: Zehntel,


TF_HC_target: Temp,


n3: Zehntel,
/** Service water target temperature */
@unit("°C")

TB_target: Temp,
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

