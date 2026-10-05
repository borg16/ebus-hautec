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
    // M17 observation candidates: betriebsdaten.uwp, Broadcast.Status0a.Bit3
    // (possible TEM 3 enable), and Status0a.Bit1 (possible TEM 24 request).
    // Schematic: M17 is supplied by TEM 3 through K1 contact 31-34; K1 itself
    // depends on the K4/K7 interlock chain. No confirmed bus field for K1's
    // physical contact or M17 current, and no validated direct M17 write command.
    // 05 03 normally arrives about every 8 s versus 80 s for Status0a.
    // These are observation candidates, not a verified fan-control boolean.
    // test1: uwp stays 1 even while SettingLevel is 0 (12:33-12:45).
    // An inferred sole-WP start at controller noon has no FA1 level edge;
    // use direct HK2 mixer readings to observe that short standby command.
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
