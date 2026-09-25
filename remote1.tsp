import "@ebusd/ebus-typespec";
import "./hautec.tsp";
using Ebus;
using Ebus.Num;
using Ebus.Dtm;
using Ebus.Str;
namespace hautec;

@zz(0x90)
namespace Remote1 {
  /** Gesamt Anlaufzähler 1 lesen WP */
  @zz(0x90)
  @id(0x3, 0x4)
  model Anlaufzaehler_WP1 {
    @out anlaufzaehler: HCD3;
    @out number: UCH;
  }

  // [anlauftyp2=1]r,ehp,anlaufzaehler_HS2,Gesamt Anlaufzähler 2 lesen HS,10,91,0304,anlaufzaehler,m,HCD:3,number,m,UCH

  /** Gesamt Betriebsstunden 1 Stufe 1 lesen */
  @qq(0x10)
  @zz(0x90)
  @id(0x3, 0x5)
  model BetriebsstundenBedienteil1 {
    @out betriebsstunden: Betriebsstunden;
  }

  /** Konfigurationsdatenanforderung des Reglers an Slave 1 */
  @write
  @passive
  @qq(0x10)
  @zz(0x90)
  @id(0x5, 0xa)
  model KonfigurationsAnforderungReglerAnBedienteil1 {}

  @zz(0x90)
  @id(0x10, 0xa, 0, 0x4)
  model Statusblock04Bedienteil1 {
    @in data: Statusblock;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0, 0x5)
  model Statusblock05Bedienteil1 {
    @in data: Statusblock;
  }

  /** Änderungsabfrage an Bedienteil 1 */
  @zz(0x90)
  @id(0x10, 0xa, 0xd0)
  model DatenAenderungsabfrageBedienteil1 {
    @out DataQ: DatenAenderungsabfrage;

    @in Answer: DatenAenderungsantwort;
  }

  /** Datum und Uhrzeit aus Bedienteil 1 */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0xa)
  model DatumUhrzeitBedienteil1 {
    @in data1: ZeitUndWarmwassertemperatur;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x21, 0xb)
  model Parameterblock210BBedienteil1 {
    @in data: KuehlParameter210B;
  }

  /** Temperatur-Sollwerte aus Bedienteil 1 */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0xb)
  model TemperaturSollwerte200BBedienteil1 {
    @in data: TemperaturSollwerte;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x21, 0xc)
  model Parameterblock210CBedienteil1 {
    @in data: Parameterdaten210C;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0xc)
  model Heizkennlinie200CBedienteil1 {
    @in data: HeizkennlinienParameter200C;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x21, 0xd)
  model Parameterblock210DBedienteil1 {
    @in data: RaumschutzParameter210D;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0xd)
  model Heizgrenzen200DBedienteil1 {
    @in data: HeizgrenzenParameter200D;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x30, 0)
  model ZeitstatusBedienteil1 {
    @out data: Zeitstatusdaten;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x31, 1)
  model Parameterblock3101Bedienteil1 {
    @out data: Parameterdaten3101;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x30, 1)
  model TemperaturSollwerte3001Bedienteil1 {
    @out data: TemperaturSollwerte3001;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x31, 0x2)
  model Parameterblock3102Bedienteil1 {
    @out data: Parameterdaten3102;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x30, 0x2)
  model Parameterblock3002Bedienteil1 {
    @out  data: Parameterdaten3002;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x31, 0x3)
  model Parameterblock3103Bedienteil1 {
    @out data: Parameterdaten3103;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x30, 0x3)
  model Parameterblock3003Bedienteil1 {
    @out data: Parameterdaten3003;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0xd1, 0x14)
  model SteuerblockD114Bedienteil1 {
    @out data: UnbekannterSteuerblock;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0xd1, 0x15)
  model SteuerblockD115Bedienteil1 {
    @out data: UnbekannterSteuerblock;
  }

  /** Fachmann-Konfigurationsmatrix (Anlagenschema, Zusatzerzeuger-Freigabe, Kaskadenwert), Menü 09, aus 1. Bedienteil */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0x9)
  model FachmannKonfiguration09Bedienteil1 {
    @in data: Konfigurationsmatrix;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0x0)
  model Menueblock00Bedienteil1 {
    Ebene: BCD;
    Block: BCD;
    @maxLength(10) Data: HEX;
    @maxLength(2) Data2: HEX;
  }

  /** Basis-Temperaturen (Raum-Soll Tag/Nacht, Warmwasser-Soll), Menü 01, aus 1. Bedienteil */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0x1)
  model BasisTemperaturen01Bedienteil1 {
    Ebene: BCD;
    Block: BCD;
    T_Room_target_Day: Temp10;
    T_Room_target_Night: Temp10;
    T_Water_target: Temp10;
    @maxLength(6) Reserviert2: HEX;
  }

  /** Heizgrenzen, Menü 03, aus Bedienteil 1 */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0x3)
  model Heizgrenzen03Bedienteil1 {
    Ebene: BCD;
    Block: BCD;
    @maxLength(2) Reserved: HEX;
    Heizgrenze: Temp10;
    HeizgrenzeAbsenk: Temp10;
    @maxLength(6) Reserved2: HEX;
  }

  /** Fachmann-Konfiguration, Menü 07, aus 1. Bedienteil */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0x7)
  model FachmannKonfiguration07Bedienteil1 {
    @in data: FachmannMatrix;
  }

  /** Fachmann-Konfiguration, Menü 08, aus 1. Bedienteil */
  @zz(0x90)
  @id(0x10, 0xa, 0x20, 0x8)
  model FachmannKonfiguration08Bedienteil1 {
    @in data: FachmannMatrix;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x21, 0x01)
  model Kuehlgrenzen2101Bedienteil1 {
    Ebene: BCD;
    Block: BCD;
    @maxLength(2) Null1: HEX;
    Base_temp: Temp10;
    Null2: HEX;
    @divisor(10) @unit("K") CoolingLimitDistance: SIN;
    @maxLength(4) Null3: HEX;
  }

  @zz(0x90)
  @id(0x10, 0xa, 0x21, 0x03)
  model Raumschutz2103Bedienteil1 {
    Ebene: BCD;
    Block: BCD;
    Room_protection_temp: Temp10;
    Data: UCH;
    @maxLength(7) Nulls: HEX;
    @maxLength(2) Data2: HEX;
  }
}
