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

/** Gesamt Betriebsstunden 2 Stufe 1 lesen */
@qq(0x10)
@zz(0x91)
@id(0x3, 0x5)
model BetriebsstundenBedienteil2 {

@out

betriebsstunden: Betriebsstunden,
}

/** Konfigurationsdatenanforderung des Reglers an Slave 2 */
@write @passive 
@qq(0x10)
@zz(0x91)
@id(0x5, 0xa)
model KonfigurationsAnforderungReglerAnBedienteil2 {
}

@zz(0x91)
@id(0x10, 0xa, 0, 0x4)
model Statusblock04Bedienteil2 {

@in

data: Statusblock,
}

@zz(0x91)
@id(0x10, 0xa, 0, 0x5)
model Statusblock05Bedienteil2 {

@in

data: Statusblock,
}

/** Änderungsabfrage an Bedienteil 2 */
@zz(0x91)
@id(0x10, 0xa, 0xd0)
model DatenAenderungsabfrageBedienteil2 {

@out

DataQ: DatenAenderungsabfrage,

@in

Answer: DatenAenderungsantwort,
}

/** Datum und Uhrzeit aus Bedienteil 2 */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xa)
model DatumUhrzeitBedienteil2 {

@in

data2: ZeitUndWarmwassertemperatur,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xb)
model Parameterblock210BBedienteil2 {

@in

data: KuehlParameter210B,
}

/** Temperatur-Sollwerte aus Bedienteil 2 */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xb)
model TemperaturSollwerte200BBedienteil2 {

@in

data: TemperaturSollwerte,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xc)
model Parameterblock210CBedienteil2 {

@in

data: Parameterdaten210C,
}

@zz(0x91)
@id(0x10, 0xa, 0x20, 0xc)
model Heizkennlinie200CBedienteil2 {

@in

data: HeizkennlinienParameter200C,
}

@zz(0x91)
@id(0x10, 0xa, 0x21, 0xd)
model Parameterblock210DBedienteil2 {

@in

data: RaumschutzParameter210D,
}

@zz(0x91)
@id(0x10, 0xa, 0x20, 0xd)
model Heizgrenzen200DBedienteil2 {

@in

data: HeizgrenzenParameter200D,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0)
model ZeitstatusBedienteil2 {

@out

data: Zeitstatusdaten,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 1)
model Parameterblock3101Bedienteil2 {

@out

data: Parameterdaten3101,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 1)
model TemperaturSollwerte3001Bedienteil2 {

@out

data: TemperaturSollwerte3001,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 0x2)
model Parameterblock3102Bedienteil2 {

@out

data: Parameterdaten3102,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0x2)
model Parameterblock3002Bedienteil2 {

@out

data: Parameterdaten3002,
}

@zz(0x91)
@id(0x10, 0xa, 0x31, 0x3)
model Parameterblock3103Bedienteil2 {

@out

data: Parameterdaten3103,
}

@zz(0x91)
@id(0x10, 0xa, 0x30, 0x3)
model Parameterblock3003Bedienteil2 {

@out

data: Parameterdaten3003,
}

@zz(0x91)
@id(0x10, 0xa, 0xd1, 0x14)
model SteuerblockD114Bedienteil2 {

@out

data: UnbekannterSteuerblock,
}

@zz(0x91)
@id(0x10, 0xa, 0xd1, 0x15)
model SteuerblockD115Bedienteil2 {

@out

data: UnbekannterSteuerblock,
}

/** Fachmann-Konfigurationsmatrix (Anlagenschema, Zusatzerzeuger-Freigabe, Kaskadenwert), Menü 09, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x9)
model FachmannKonfiguration09Bedienteil2 {

@in

data: Konfigurationsmatrix,
}

/** Kerndaten der Wärmepumpen-Stufen, Menü 15, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0xf)
model WaermepumpenStufenKonfiguration15Bedienteil2 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 17, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x11)
model FachmannKonfiguration17Bedienteil2 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 18, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x12)
model FachmannKonfiguration18Bedienteil2 {

@in

data: FachmannMatrix,
}

/** Fachmann-Konfiguration, Menü 19, aus 2. Bedienteil */
@zz(0x91)
@id(0x10, 0xa, 0x20, 0x13)
model FachmannKonfiguration19Bedienteil2 {

@in

data: FachmannMatrix,
}


}

