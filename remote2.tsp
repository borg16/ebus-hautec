import "@ebusd/ebus-typespec";
import "./hautec.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec;

@zz(0x91)
namespace Remote2 {

/** Gesamt Anlaufzähler 1 lesen WP */
@zz(0x91)
@id(0x3, 0x4)
model Anlaufzaehler_WP2 {

@out

anlaufzaehler: HCD3,

@out

number: UCH,
}
}

