import "@ebusd/ebus-typespec";
import "./hautec.tsp";
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

/** Date/Time Broadcast (eBUS service 07 00) */
@passive 
@zz(BROADCAST)
@id(0x7, 0)
model DateTimeBroadcast {
/** Outside temperature */
@unit("°C")
ta: D2B,
time: BTI,
date: BDA,
}
/** Identification (eBUS service 07 04). */
@inherit(r, b)
@ext(0x7, 0x4)
model Identification {
  data: IdentificationData;
}

/** Identification, write direction (eBUS service 07 04) */
@write 
@zz(BROADCAST)
@id(0x7, 0x4)
model IdentificationWrite {
}

/** Inquiry of Existence (eBUS service 07 FE) */
@write 
@zz(BROADCAST)
@id(0x7, 0xfe)
model InquiryOfExistence {
}

/** Sign of Life (eBUS service 07 FF) */
@passive 
@zz(BROADCAST)
@id(0x7, 0xff)
model SignOfLife {
}

/** Error Message (eBUS service FE 01) */
@passive 
@zz(BROADCAST)
@id(0xfe, 1)
model ErrorMessage {

@maxLength(10) 
error: STR,
}

/** Reset Status NM (eBUS service FF 00) */
@passive 
@zz(BROADCAST)
@id(0xff, 0)
model ResetStatusNM {
}

/** Reset Target Configuration NM (eBUS service FF 01) */
@passive 
@zz(BROADCAST)
@id(0xff, 1)
model ResetTargetConfigurationNM {
}

/** Failure Message NM (eBUS service FF 02) */
@passive 
@zz(BROADCAST)
@id(0xff, 0x2)
model FailureMessageNM {
}

/** Betriebsdaten des Reglers an den Feuerungsautomaten 1 */
@passive 
@zz(BROADCAST)
@id(0x5, 0xd)
model ToFAxSub {
  daten: RaumtemperaturdatenReglerAnFeuerungsautomat,
}

/** Operational Data: Betriebsdaten des Reglers an andere Regler (eBUS service 08 01) */
@passive 
@zz(BROADCAST)
@id(0x8, 1)
model OperationalData {
@unit("°C") tr_hp: D2B,
@unit("°C") tb: D2B,
Emissionstest: UCH,
BWR_Aktiv: BI0,
PumpenFreigabeSperre: BI1,
Kessel1InBetrieb: BI2,
/** Standard label only: status byte is 00 or 08 in the eleven ebusd*.log
 * captures examined on 2026-10-03. No physical compressor/terminal assignment. */
Kessel2InBetrieb: BI3,
/** Standard label; remains clear in those captures, including DHW phases.
 * Use Status0a.BWR_Ventil / Status1a.BWR_Aktiv as DHW output candidates. */
Ladepumpe: BI4,
/** Standard label; not a validated TEM 13 / M5 indication. */
BW_Ladung: BI5,
TBF_Connect: BI6,
@unit("°C") tr_hp2: D2B,
}

/** Control commands from the master controller to other controllers (eBUS service 08 02). */
// eBUS Application Layer V1.6.1, section 3.4.3, p. 46 (seven payload bytes):
// https://www.stroimdom.com.ua/applications/core/interface/file/attachment.php?id=418507
// TEM/Hautec adds an eighth byte in ebusd.log; its meaning is not established.
// Leave it undecoded so both standard seven-byte and observed eight-byte frames work.
@passive
@zz(BROADCAST)
@id(0x8, 0x2)
model ControlCommands {
  /** Boiler target temperature (TK_target). */
  @unit("°C")
  boilerTargetTemperature: D2B,
  /** Domestic hot water target temperature (TB_target). */
  @unit("°C")
  hotWaterTargetTemperature: D2B,
  /** Expected performance demand (L_exp): -100 = no deficiency; 0 = no target; 100 = maximum. */
  @unit("%")
  expectedPerformance: D1B,
  /** Number of the first burner control unit with an error (FA_no). */
  errorDevice: UCH,
  /** Manufacturer-specific error code (ERR). */
  errorCode: UCH,
}

// TEM-specific service 10 0A. Keep Status0a..Status3b for existing MQTT consumers.
// Planned names in the comments include the two hexadecimal selector bytes,
// not heating-circuit numbers. See docs/Broadcast-Messages.md for the deferred migration.
// Terminal hypotheses below: docs/Heating-Terminal-Analysis-2026-10-03.md.
// For selectors 11 00/11 01, payload indices include the two selector bytes:
// p2..3 = outside temperature, p4 = status A, p5 = status B; bit numbers are zero-based.
// These broadcasts normally arrive every 80 s, so short pulses can be missed.
// Operator verified: switched TEM outputs 7/8 unused; only N on block 8 is used.
// Existing field names remain stable; none of these hypotheses adds a write command.
// Additional heating experiment: docs/Heating-Test-2026-10-03-test1.md.
// Log timestamps and controller time differ by about 9 min 12 s in test1.
/** Operating status and outside temperature; TEM selector 11 00. Flag meanings are only partly established. Planned name: OperatingStatus_1100 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x11, 0)
model Status0a {
ta: Temp,
Bit0: BI0,
/** Candidate: first-stage enable, possibly TEM 24 ("Verdichter 1").
 * Matches next FA1 05 03 SettingLevel > 0 in 1252/1257 pairs across eleven logs
 * (next response within 10 s). All five exceptions are in cooltest: bit already
 * set while FA1 reports 0%. Not a measured K1 contact or compressor current.
 * M17 relevance: TEM 24 reaches K1 through K4/K7; this bit cannot establish
 * that K1 is energized, especially when the cooling interlock inhibits K1. */
// test1: 207/207 next-FA1 pairs agree; still no physical contact measurement.
Bit1: BI1,
/** Candidate: second-stage enable, possibly TEM 26 ("WEZ 1-2", contact 25-26).
 * Matches next FA1 05 03 SettingLevel == 100 in 1255/1257 pairs across eleven
 * logs; one timing mismatch each in ebusd.log and cool6. Earlier five-log
 * comparison was 376/376. See heating-output/stage-candidates.csv.
 * Per schematic, TEM 26 supplies KT15 and its contact feed; HK2+ / TEM 15
 * controls Y1. KT15 then switches K3 and, through K3, source pump M3.
 * Loss of TEM 26 can stop K3 before the 1000 s off-delay expires.
 * Remains set during the inferred DHW cooling pause in cool3: not a K3/current
 * measurement, not a direct M17 status, and not proof of physical TEM 26 state. */
// test1: 207/207 next-FA1 pairs agree. Remains set before, during and after
// the inferred 12:09-12:19 sole-WP run; cannot by itself report that run.
Bit2: BI2,
/** Candidate: source/heat-pump pump enable, possibly TEM 3 (source pump/fan).
 * Matches next FA1 05 03 uwp in 1250/1257 pairs. The approximately one-minute
 * run-on differs from Running's approximately 15-minute heating-pump run-on.
 * M17 relevance: schematic supply is TEM 3 AND closed K1 contact 31-34.
 * Bit3 alone does not report M17. Bit1 AND Bit3 is also unvalidated: it omits
 * K4/K7 interlocks, actual K1 contact state and asynchronous/stale bus samples.
 * Need synchronized TEM 3, K1 and fan-current observations before using a
 * derived M17 state for software control. M3 is instead switched by K3. */
// test1: this bit and all 2073 FA1 uwp samples stay set, including the
// 12:33-12:45 FA1 level-0 pause. This capture cannot identify M17 current.
Bit3: BI3,
Bit4: BI4,
Bit5: BI5,
Bit6: BI6,
/** Candidate: heating-circuit pump enable, possibly TEM 6 (not compressor run).
 * On 2026-09-27, FA1 level falls to 0 at 07:02:53 and uwp clears at 07:03:49;
 * this bit stays set through 07:16:11 and clears by 07:17:31, consistent with
 * 07-03 = 15 min. Per schematic, TEM 6 feeds M4.1/M4.2 through K11 selection.
 * Does not distinguish those pumps, prove flow, or describe M17. Compare
 * P01_20_HK1 and physical TEM 6; terminal assignment remains unmeasured. */
Running: BI7,
/** Candidate: DHW loading actuator/run-on status, possibly TEM 13 (M5).
 * Also compare Status1a.BWR_Aktiv. In cool3, first cleared samples follow DHW
 * target reduction by about 3 min, consistent with configured run-on and
 * 80 s sampling. TEM 13 (M5) versus TEM 11 (K11 selection) remains unresolved;
 * neither actual pump current nor a safe K11/M17 state follows from this bit. */
BWR_Ventil: BI0,
/** Legacy name; not established as a second DHW valve or another terminal. */
BWR_Ventil2: BI1,
/** New candidate: FA2 stage-active indication, NOT the physical sole-WP.
 * test1: B & 0x04 agrees with next FA2 05 03 SettingLevel == 100 in 207/207
 * pairs within 10 s (maximum separation 7.844 s). FA2 rises at 12:04 and
 * 13:33, whereas inferred sole-WP starts are about 12:09 and 14:20.
 * Physical actuator assignment remains open; not an M17 indication. */
Bit10: BI2,
Bit11: BI3,
Bit12: BI4,
Bit13: BI5,
Bit14: BI6,
}

/** Temperature values; TEM selector 10 00. Individual sensor assignments remain provisional. Planned name: TemperatureValues_1000 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x10, 0)
model Status0b {
/** Legacy name: TWV, supported by direct 00-07 WP reads in cool8:
 * all 24 nearest-time pairs agree within 0.1 K (max separation 0.770 s).
 * The local sensor list assigns TWV and THV1 to input 47;
 * this is not a proven cooling-flow temperature during DHW.
 * Nearly equal to tf_hc, but the two transmitted words can differ. */
@unit("°C") tf_hp: Temp,
/** Heat pump return temperature */
@unit("°C") tr_hp: Temp,
/** Legacy name: THV1 candidate, sharing input 47 with TWV in the local
 * sensor list. Not an independent measured floor-heating flow by name alone.
 * Keep the separate wire value; differences up to 0.3 K occur in the logs. */
@unit("°C") tf_hc: Temp,
b1: Byte,
b2: Byte,
@unit("°C") tb: Temp,
}

/** Operating status and outside temperature; TEM selector 11 01. Includes the confirmed FB2 mixer-close indication. Planned name: OperatingStatus_1101 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x11, 1)
model Status1a {
@unit("°C") ta: Temp,
Flag0: BI0,
Flag1: BI1,
Flag2: BI2,
Flag3: BI3,
Flag4: BI4,
/** Candidate: HK2 mixer-open indication, possibly TEM 15 / KT15 input Y1.
 * Joint comparison of bits 5/6 with P01_21_HK2 (+100/0/-100) matches 105/105
 * pairs in cool6/8/9/10 (max time gap 1.819 s); mostly steady +100 states.
 * In pulsed cool4/5, 11/34 pairs disagree at gaps up to 6.649 s; timing is a
 * possible explanation, not proven. See heating-output/mixer-candidates.csv.
 * No physical mixer is documented: KT15 holds K3 with a 1000 s off-delay
 * only while supplied by TEM 26. This is not a K3 or M17 running indication. */
// test1: nearest direct comparisons within 10 s match 178/191; short pulses
// produce 13 disagreements even at about 1.7 s separation. An entire
// standby open/close cycle at 12:09 (controller noon) is missed by the 80 s
// broadcasts. An open command is not necessarily a space-heating request:
// anti-seizure operation is a strong explanation for that standby cycle.
Flag5: BI5,
/** Operator-confirmed FB2 "mixer close" indication; not a valve-position
 * measurement or an electrically verified TEM 16 state. TEM 16 is unused
 * in the schematic: this bit neither directly stops K3 nor retriggers KT15.
 * A clear bit does not imply mixer-open; compare Flag5 and P01_21_HK2. */
Mixer_Close: BI6,
/** Candidate: logical HK2 pump/activity including run-on. test1: set from
 * 14:21:04 through 15:23:44; first clear at 15:25:04, after approximately
 * 15 min of direct mixer-close readings. Physical TEM 8 is unconnected;
 * this is not M4.2 current, a confirmed terminal state, or M17 status. */
Flag7: BI7,
/** DHW loading/run-on candidate corresponding to Status0a.BWR_Ventil.
 * Physical TEM 13 (M5) versus TEM 11 (K11) not distinguished; not proof that
 * the air-source compressor or M17 is running. */
BWR_Aktiv: BI0,
Bit1: BI1,
/** Candidate corresponding to Status0a.Bit10 / FA2 stage activity.
 * test1: 205/207 next-FA2 pairs agree within 10 s; two transition samples
 * agree with the preceding FA2 state instead. No physical output proven. */
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

/** Temperature values; TEM selector 10 01. Individual sensor assignments remain provisional. Planned name: TemperatureValues_1001 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x10, 1)
model Status1b {
/** Legacy name: TWV candidate; same physical-assignment caveats as Status0b.tf_hp. */
@unit("°C") tf_hp: Temp,
n1: Zehntel,
/** Legacy name: matches 00-02 HK2 (THV2, input 43) in all 20 nearest-time
 * pairs in ebusd.cool4.log (max separation 6.634 s). Operator locates this
 * sensor at the ground-source heat-pump inlet; do not equate it with input 48. */
tr: Temp,
n2: Zehntel,
/** software water temperature */
@unit("°C") tb: Temp,
}

/** Minute counter and partly unknown status data; TEM selector 11 02. Planned name: TimeAndStatus_1102 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x11, 0x2)
model Status2a {
b1: Byte,
b2: Byte,
Mins: UIN,
/** HK1 operating state in the controller (2026-10-11 test3): 04 = standby, 01 = clock program 1.
 * Updated within one 80 s cycle after the FB1 change; other modes not yet measured. */
b3: Byte,
/** HK1 companion byte: 00 = standby, 01 = clock program 1. Matches the mode byte of FB1 block 20 01. */
b4: Byte,
b5: Byte,
b6: Byte,
}

/** Partly unknown controller data; TEM selector 10 02. The legacy bit-field interpretation is unverified. Planned name: ControllerData_1002 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x10, 0x2)
model Status2b {
Bit0: BI0,
Bit1: BI1,
Bit2: BI2,
Bit3: BI3,
Bit4: BI4,
Bit5: BI5,
Bit6: BI6,
/** Legacy bit interpretation: 10 02 appears to contain numeric words.
 * Not a validated DHW flag; use the 11 00/11 01 candidates for comparison. */
BWR_Aktiv: BI7,
Bit8: BI0,
/** Legacy name only; no established DHW/cooling/terminal semantics. */
BWR_Aktiv_not_Cooling: BI1,
Bit10: BI2,
Bit11: BI3,
Bit12: BI4,
Bit13: BI5,
Bit14: BI6,
Bit15: BI7,
}

/** Minute counter and partly unknown status data; TEM selector 11 03. Planned name: TimeAndStatus_1103 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x11, 0x3)
model Status3a {
b1: Byte,
b2: Byte,
/** Minutes since Monday 00:00; checked against 07 00 and 30 00 captures (docs/FB-Initialization.md). */
Mins: UIN,
/** HK2 operating state in the controller (2026-10-11 test3): 04 = standby, 01 = clock program 1.
 * Same layout as Status2a.b3; other modes not yet measured. */
b5: Byte,
/** HK2 companion byte: 00 = standby, 01 = clock program 1. Matches the mode byte of FB2 block 20 0B. */
b6: Byte,
qB3: Byte,
b4: Byte,
}

/** Temperature targets and partly unknown values; TEM selector 10 03. Circuit assignments remain provisional. Planned name: TemperatureTargets_1003 (deferred until coordinated migration). */
@passive 
@zz(BROADCAST)
@id(0x10, 0xa, 0x10, 0x3)
model Status3b {
n1: Zehntel,
n2: Zehntel,
TF_HC_target: Temp,
n3: Zehntel,
/** Service water target temperature */
@unit("°C")TB_target: Temp,
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
