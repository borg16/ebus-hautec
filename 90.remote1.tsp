import "@ebusd/ebus-typespec";
import "./_templates.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec.tem;

// @zz(0x90)
namespace Remote1 {

/** Gesamt Anlaufzähler 1 lesen WP */
@zz(0x90)
@id(0x3, 0x4)
model Anlaufzaehler_WP1 {

@out

anlaufzaehler: HCD3,

@out

number: UCH,
}
}

