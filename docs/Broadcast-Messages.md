# TEM broadcast names (service 10 0A)

The active names remain `Status0a` through `Status3b` for existing MQTT consumers.
The English names are retained in the model comments as proposals for a later
coordinated migration. Their four hexadecimal suffix digits are the payload
selector bytes in wire order, not heating-circuit numbers. All eight definitions
are passive broadcasts to `FE`.

| Active name | Planned name (deferred) | Selector | Naming evidence |
| --- | --- | --- | --- |
| `Status0a` | `OperatingStatus_1100` | `11 00` | Outside temperature followed by partly understood status bytes. |
| `Status0b` | `TemperatureValues_1000` | `10 00` | Several temperature values in the existing decoder; exact sensor assignments remain provisional. |
| `Status1a` | `OperatingStatus_1101` | `11 01` | Outside temperature and status bytes, including the operator-confirmed FB2 mixer-close indication. |
| `Status1b` | `TemperatureValues_1001` | `10 01` | Temperature values and unknown words; distinct from `10 00`, without an established circuit-wide assignment. |
| `Status2a` | `TimeAndStatus_1102` | `11 02` | Minute counter and partly unknown bytes. |
| `Status2b` | `ControllerData_1002` | `10 02` | Meaning not sufficiently established for a functional name; see below. |
| `Status3a` | `TimeAndStatus_1103` | `11 03` | Minute counter and partly unknown bytes, similar to `11 02`. |
| `Status3b` | `TemperatureTargets_1003` | `10 03` | Heating/water temperature targets in the existing decoder; remaining values and circuit assignments are provisional. |

The planned names are project names inferred from the current decoding and local evidence,
not official TEM command names. Evidence comes from
[broadcast.tsp](../broadcast.tsp), the CRC-checked `ebusd.log` capture of
2026-09-27, and the [confirmed display observation](Heating-Control-Analysis.md#nachbeobachtung-anzeigebit-bestätigt-wiederkehrende-zu-impulse).
The last source confirms one indication bit in `11 01`, not the meaning of the
whole block or a physical terminal state.

In the capture, blocks `10 00` and `10 01` contain 12 bytes after the selector.
Several words decoded as tenths of a degree vary between plausible temperature
values. Both time blocks contain a word increasing from 8692 to 9707 over
roughly 17 hours. The name `TimeAndStatus` does not establish the counter's
calendar origin or the semantics of the remaining bytes.

For `10 02`, the first word takes values `00 00`, `be 00`, and `f4 01`
(little-endian 0, 190, 500). These suggest numeric data, potentially temperature
targets, rather than independent flags. This remains a decoding question;
`ControllerData_1002` deliberately does not promote the old bit labels to
confirmed semantics. Several existing models also decode only part of their
payload. Restoring the active names preserves all field layouts and data types.

Existing ebusd reads, MQTT subscriptions, and dashboards should continue using
`Status0a` through `Status3b`, for example `Broadcast.Status1a.Mixer_Close`.
A later migration will coordinate message names and consumers together.
Archived logs retain the names originally recorded. Older generated reports
may contain the temporarily used English names; the table above maps them to
the active names. Regenerated [frequency reports](../status-output/Status-Statistik.md)
use the active definitions.

Cross-message properties that can share a name in Home Assistant or another
evaluation are collected in [Broadcast-Property-Groups.md](Broadcast-Property-Groups.md).
That mapping distinguishes well-supported aliases from still-unverified
temperature correspondences and does not rename the active ebusd fields.

Rebuild and regenerate the report with:

```sh
npm run build:csv
python3 scripts/analyze_status_frequency.py ebusd.log
```

## Shared input candidate for tf_hp and tf_hc (2026-09-30)

The legacy `Status0b.tf_hp` and `Status0b.tf_hc` fields are separate words
in selector `10 00`, not two proven independent sensors. The local
[sensor list](../input/soll_und_istwerte.md) assigns TWV (00-07) and THV1
(00-02 HK1) to input 47. In `ebusd.cool3.log`, 60 of 72 CRC-valid frames
contain identical values; the remaining differences are at most 0.3 K.
Across all three cooling logs, 309 of 339 frames are identical, with a
maximum difference of 0.3 K. Internal update timing or processing could
explain differences; neither mechanism has been established.

The operator's proposed location near handwritten R3 at the HWAL heat
exchanger in `input/hydraulik.png` fits the warm values during simultaneous
DHW preparation and cooling. Physical sensor placement is not confirmed.
In particular, neither legacy name proves a cooling-flow temperature or an
independent floor-heating supply measurement during DHW preparation.
Keep both decoded values and existing names for consumers; only comments
were clarified. See the [cooling analysis](Cooling-Test-2026-09-30.md)
for the per-log comparison and limits of the R3 hypothesis.

## Status1b.tr compared with direct HK2 reads (cool4, 2026-09-30)

The third temperature word after selector `10 01`, currently named
`Status1b.tr`, matches direct `00-02 HK2` reads in all 20 nearest-time pairs
in `ebusd.cool4.log`. Maximum separation is 6.634 s; each pair is exactly
equal at 0.1 °C resolution. This supports the THV2/input-43 assignment.
The operator places input 43 at the ground-source heat-pump inlet; the exact
pipe/medium still needs clarification. It is distinct from the input-48
return value. All 47 direct HK2 reads between 23:40:00 and 23:51:32 are 22.0 °C
while input-48 return and WE1 demand vary. This validates the observed value
mapping, not the complete sensor calibration or firmware control role.

Only the source comment was updated; field names, offsets and types remain
unchanged. See the [cool4 analysis](Cooling-Test-2026-09-30-cool4.md) and
[comparison CSV](../cooling4-output/HK2_candidate_1001-comparison.csv).

## Status0a.Bit2: second-stage status candidate (cool5, 2026-10-01)

`Status0a.Bit2` is mask 0x04 of the first status byte after the outside
temperature in selector `11 00` (payload offset 4, including selector).
In all 376 CRC-valid status samples across `cool`, `cooltest`, `cool3`,
`cool4`, and `cool5`, it is set exactly when the following FA1 `05 03`
reply reports 100 %. Maximum separation: 4.797 s. At nine samples near
edges, it already reflects the next level rather than the preceding one.
This strongly supports a second-stage active/enable status interpretation;
the official firmware meaning and physical output mapping are not established.

The roughly 80 s sampling interval misses entire 40 s phases in `cool5`.
Do not infer pulse lengths from a held-last-value plot. In the earlier
DHW/cooling pause around 15:21–15:33 in `cool3`, all nine status samples
still have this bit set, matching FA1=100 despite the electrical evidence
for a stopped cooling compressor. It is not a compressor-run measurement.
The field name and wire definition remain unchanged; only a comment is added.
See the [comparison and evidence](Cooling-Test-2026-10-01-cool5.md).

### Timing qualification from cool6 (2026-10-01)

The next-FA1 comparison matches 66 of 67 new Status0a samples. At 20:00:07.153
(line 14843), Bit2 is still 1; the next FA1 update at 20:00:12.820 is already
50 %. That sample matches the preceding 100-% phase. The exact next-message
rule observed in the earlier five logs is therefore not universal and does
not establish a guaranteed advance indication. The stage-status interpretation
remains plausible. See the [cool6 analysis](Cooling-Test-2026-10-01-cool6.md).

## Direct confirmation of Status0b.tf_hp by 00-07 (cool8, 2026-10-02)

All 24 nearest-time pairs of `Status0b.tf_hp` and direct `00-07 WP`
(selector `08 04`) differ by at most 0.1 K; 18 are exactly equal, maximum
time separation 0.770 s. This directly supports the TWV assignment.
There are 386 valid direct 00-07 reads, median interval 4.984 s. The value
can reach its minimum tens of seconds after a stage reduction, so a later
minimum must not be treated as the instantaneous switch-off temperature.
Field names and wire decoding remain unchanged. See the
[cool8 analysis](Cooling-Test-2026-10-02-cool8.md).
