# eBUS standard coverage audit

Audit date: 2026-09-27. Scope: the TypeSpec files imported by `main.tsp`,
their generated CSV definitions, and CRC-valid master telegrams in four local
captures. This is a coverage and decoding review; it does not establish which
additional commands the TEM controller supports.

References:

- [eBUS Application Layer V1.6.1, March 2007](https://www.stroimdom.com.ua/applications/core/interface/file/attachment.php?id=418507), page numbers below.
- [ebusd standard operational-data definitions](https://github.com/john30/ebusd-configuration/blob/master/src/opdata_inc.tsp).
- [ebusd standard broadcasts](https://github.com/john30/ebusd-configuration/blob/master/src/broadcast.tsp).
- Installed `@ebusd/ebus-typespec/lib/models.tsp`, `Ebus.Id` models.

## Highest-priority findings in existing messages

### 07 04: identification corrected

`Broadcast.Identification` and the former `Signals.Geraeteidentifikation` originally
defined only `manufacturer: UCH` and `id: UCH`. The documented payload has ten bytes:
manufacturer, five ASCII ID characters, two software-version bytes and two
hardware-version bytes (p. 39). The installed `Ebus.Id` models already implement
these fields.

The broadcast recorded at 2026-09-27 14:53:28.645 contains:

```text
10 fe 07 04 0a  10 31 37 33 38 35 01 06 01 00
                |  \----17385---/ \SW/ \HW/
               TEM
```

The initial replay produced `TEM;49` (49 is the ASCII code of the first ID
character). Both definitions now share `IdentificationData` in `hautec.tsp`,
with fields `manufacturer`, `id` (`STR:5`), `softwareVersion` and
`hardwareVersion` (`PIN`). Replay now produces `TEM;17385;0106;0100`, matching
ebusd's built-in identification handling. Leading version zeroes are preserved.
The English slave-reply name is now `Signals.Identification`; update consumers
of `Signals.Geraeteidentifikation`. The broadcast name remains unchanged.
CSV field names are lowercase, e.g. `softwareversion`.

There are 3,080 CRC-valid 07 04 master telegrams in `ebusd.log`: one ten-byte
identification broadcast and 3,079 empty requests to `08`/`18`. Those requests
must not be counted as 3,079 successful identification responses. The specific
`Signals` model currently covers target `08` only.

### 05 01 / 05 03: outside-temperature decoding corrected

`BetriebsdatenAutomat.OutsideTemperature` originally used `UCH`. The standard
uses a signed byte and the special replacement value `3F` (p. 19).
All 15,231 captured 05 03 messages use `3F` in that field. The initial replay of
`031005030a010048643117ff3f4000` displayed `63`, a spurious temperature.

Both this field and the 05 01 `TAussenIst` field now use the shared
`OutsideTemperature1Byte` scalar. Normal reads return signed temperature values
or the explicit state `unavailable` for `3F`. The ordinary `SCH` replacement
`80` remains `-` (JSON null). The unused legacy `Aussentemperatur` alias also
inherits the corrected scalar. Field names are retained for existing consumers.

The installed ebusd/TypeSpec combination cannot configure a custom numeric
replacement byte. The implementation therefore uses `SCH` with a value list.
An explicit mapping of negative wire bytes is necessary because ebusd's
value-list fallback prints unsigned codes. Tests cover all 256 byte values
for both services on both burners, plus observed extended TEM payloads.

**Consumer behavior:** default text reads give values such as `-30`, `15`, or
`unavailable`. JSON encodes mapped negatives and `unavailable` as strings;
unmapped positive values remain numeric. Treat `unavailable` as missing and
convert numeric strings when required. With `ebusctl read -n`, mapped values
are raw enum codes (e.g. 226 for -30 and 63 for unavailable), not decoded
temperatures. This mapping is an explicit state, not a custom JSON-null
replacement. See [ebusd's value-list decoding](https://github.com/john30/ebusd/blob/master/src/lib/ebus/data.cpp).

### 05 0D: documented flag hidden among raw bytes

`RaumtemperaturdatenReglerAnFeuerungsautomat` now accounts for all ten payload
bytes. After the room target and actual temperatures, payload byte 3 bit 0
denotes active domestic-hot-water preparation; six reserved bytes follow
(p. 34). The status byte remains exposed as `b`. The reserved tail is now
explicitly ignored with `@maxLength(6) reserved: IGN`, including the previously
omitted last byte. The former output fields `b_1` through `b_5` are removed.

The complete reserved tail is `00 80 00 80 FF FF` in every CRC-valid 05 0D
telegram checked: 761 in `ebusd.log`, 170 in `input/complete.log`, and 170 in
`input/ebusd-rawdata.log`. The historical files overlap; these are per-file
counts. `input/master.log` contains no 05 0D messages. This is an observation
of the available captures, not a guarantee for other firmware or future traffic.

A useful English field would be `hotWaterPreparationActive`. The status byte
is zero in all 761 samples, so this capture supplies no switching event with
which to verify the TEM-specific functional meaning. No physical terminal
assignment follows from the documented flag.

### 08 01: standard semantics are clearer than the current names

The standard layout is already present. The upstream `RcOperation` model names
the first temperature as boiler temperature and the last as return temperature;
it also enumerates emission-test values. Here those fields are `tr_hp` and
`tr_hp2`, and `Emissionstest` has no enumeration. English standard names would
reduce ambiguity, while the actual TEM sensor mapping still requires evidence.

## Missing standard definitions

All codes below are PB/SB service bytes, not TEM menu selectors. The absence
check covers the active imports, not unused type declarations or `obsolete/`.

| Service | Standard function / proposed English model | Reference |
| --- | --- | --- |
| `08 00` | Controller demands / `ControllerTargetValues` | p. 44; upstream `RcTarget` |
| `08 03` | Boiler parameters / `BoilerParameters` | p. 47 |
| `08 04` | Operating modes and targets / `SystemRemoteControl` | p. 48 |
| `05 0B` | Configuration response / `BurnerConfiguration` | p. 32 |
| `05 03`, block `02` | Additional measurements / `BurnerOperatingData2` | p. 20 |
| `07 01`, `07 02` | Set date/time, outside temperature | pp. 36–37 |
| `07 03`, `07 05` | Discover supported commands | pp. 38, 41 |
| `03 06`, `03 07`, `03 08`, `03 10` | Further counters | pp. 11–15 |
| `05 00`, `05 04`, `05 06`–`05 09`, `05 0C` | Further burner requests/data | pp. 16, 21, 23–30, 33 |
| `09 00`–`09 03` | RAM/EEPROM access | pp. 49–52 |
| `0F 01`–`0F 03` | Test services | pp. 53–61 |
| `FF 03`–`FF 06` | Network-management queries | pp. 66–70 |

05 0A is present, but its separate 05 0B response is missing. Existing 05 03
models match block 01 only. Service 05 05 is explicitly barred, not a missing
implementation candidate.

None of the missing services above except 07 01 occurs among CRC-valid master
telegrams in the four examined captures. Documentation alone is insufficient
to conclude that the installed devices implement them.

The 07 05 table contains an apparent editorial inconsistency: its heading
identifies 07 05, but its SB row says 03h. Resolve this before implementation.

## Observed deviations that require care

- **07 01:** six messages in `ebusd.log`, all `10 → 18`, with eight payload
  bytes instead of the standard nine. Example: `66 17 cd 31 00 08 66 17`.
  This looks like the eight-byte 08 01 payload, not a valid standard BCD
  date/time layout. The reason is unknown; decoding it as `SetDateTime`
  solely from PB/SB would be misleading.
- **03 04 / 03 05:** both occur 408 times, carrying four/five master payload
  bytes to the remote controls. The current `@out` fields therefore describe
  an observed TEM transfer, not a normal empty standard query. 03 04 includes
  an extra `number`; 03 05 leaves its fifth byte undecoded. Do not blindly
  reverse their field directions when comparing against the standard.
- **05 01 / 05 03:** the actual payloads have ten bytes instead of the
  standard five/eight. The additional five/two bytes have no definition in
  the compared standard tables.
- **08 02:** the already corrected seven-byte standard prefix is followed
  by an unknown eighth byte in this installation.
- **10 0A:** the application-layer standard does not define the TEM block
  payloads used by this project. Its standard heating flags cannot simply
  be transplanted to `OperatingStatus_1100` or `OperatingStatus_1101`.

The selected `@id(0x06, 0x21, 0x08, 0x03)` in `controller.tsp` means service
`06 21` plus selector `08 03`, currently `P00_04_HK1`. It is unrelated to the
standard boiler-parameter service `08 03`.

## Capture accounting and validation

| File | CRC-valid master telegrams | Excluded lines |
| --- | ---: | ---: |
| `ebusd.log` | 52,793 | 277 |
| `input/complete.log` | 10,709 | 148 |
| `input/master.log` | 4,953 | 0 |
| `input/ebusd-rawdata.log` | 16,199 | 148 |

Counts are per file; the historical files overlap and must not be summed as
independent observations. Initial NUL padding in `ebusd.log` was skipped.
Wire escapes were decoded and master CRC/length checked. Counts do not imply
successful slave replies. The built CSV inventory was compared with the
standard command families; three representative real telegrams were replayed
using ebusd, `/dev/null`, read-only mode and `--inject=stop`.

Identification and outside-temperature decoding have now been corrected.
Remaining work: expose the documented 05 0D flag, clarify 08 01 names, then
investigate missing services and vendor extensions based on observed traffic
or supported-command queries. In 05 0D, the reserved tail is now ignored;
its all-zero status flag cannot establish whether hot-water preparation actually
stopped or whether TEM simply does not populate this indication.

Regression checks:

```sh
python3 -m unittest discover -s scripts -p test_standard_messages.py
python3 -m unittest discover -s scripts -p test_broadcast.py
```
