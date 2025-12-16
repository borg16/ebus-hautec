import "@ebusd/ebus-typespec";
import "./_templates.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec.tem;

// @zz(0x03)
namespace Burner1 {

/** Betriebsdaten des Reglers an den Feuerungsautomaten */
@write @passive 
@zz(0x3)
@id(0x5, 1)
model Betriebsdaten1 {


betriebsdaten: BetriebsdatenRegler,
}
}

