import "@ebusd/ebus-typespec";
import "./hautec.tsp";
using Ebus;
namespace hautec;

@zz(0x13)
namespace Burner2 {

/** Betriebsdaten des Reglers an den Feuerungsautomaten */
@write @passive 
@zz(0x13)
@id(0x5, 1)
model Betriebsdaten2 {


betriebsdaten: BetriebsdatenRegler,
}

/** Betriebsdatenanforderung des Reglers an den Feuerungsautomaten 2 */
@write @passive 
@qq(0x10)
@zz(0x13)
@id(0x5, 0x2)
model BetriebsdatenAnforderungReglerAnFeuerungsautomat2 {


blocknummer: Blocknummer,
}

/** Betriebsdaten des Feuerungsautomaten 2 an den Regler */
@write @passive 
@qq(0x13)
@zz(0x10)
@id(0x5, 0x3, 1)
model BetriebsdatenFeuerungsautomat2AnRegler {


betriebsdaten: BetriebsdatenAutomat,
}

/** Konfigurationsdatenanforderung des Reglers an den Feuerungsautomaten 2 */
@write @passive 
@qq(0x10)
@zz(0x13)
@id(0x5, 0xa)
model KonfigurationsAnforderungReglerAnFeuerungsautomat2 {
}

}

