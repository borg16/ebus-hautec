import "@ebusd/ebus-typespec";
import "./_templates.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec.tem;

// @zz(0x13)
namespace Burner2 {

/** Betriebsdaten des Reglers an den Feuerungsautomaten */
@write @passive 
@zz(0x13)
@id(0x5, 1)
model Betriebsdaten2 {


betriebsdaten: BetriebsdatenRegler,
}
}

