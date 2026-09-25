import "@ebusd/ebus-typespec";
import "./hautec.tsp";
using Ebus;
namespace hautec;

@zz(0x03)
namespace Burner1 {
    /** Betriebsdaten des Reglers an den Feuerungsautomaten */
    @write
    @passive
    @zz(0x3)
    @id(0x5, 1)
    model Betriebsdaten1 {
        betriebsdaten: BetriebsdatenRegler;
    }

    /** Betriebsdatenanforderung des Reglers an den Feuerungsautomaten 1 */
    @write
    @passive
    @qq(0x10)
    @zz(0x3)
    @id(0x5, 0x2)
    model BetriebsdatenAnforderungReglerAnFeuerungsautomat1 {
        blocknummer: Blocknummer;
    }

    /** Betriebsdaten des Feuerungsautomaten 1 an den Regler */
    @write
    @passive
    @qq(0x3)
    @zz(0x10)
    @id(0x5, 0x3, 1)
    model BetriebsdatenFeuerungsautomat1AnRegler {
        betriebsdaten: BetriebsdatenAutomat;
    }

    /** Konfigurationsdatenanforderung des Reglers an den Feuerungsautomaten 1 */
    @write
    @passive
    @qq(0x10)
    @zz(0x3)
    @id(0x5, 0xa)
    model KonfigurationsAnforderungReglerAnFeuerungsautomat1 {}
}
