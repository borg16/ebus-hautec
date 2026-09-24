# EBUSD Configuration for Reading Hautec Carno (~2006) Data

This is a configuration to read and write observed numeric parameters of the TEM SE 6000 WPC controller.

The preliminary analysis of the protocol is documented in [Protocol-Analysis.md](Protocol-Analysis.md).

The active [controller.tsp](controller.tsp) uses the CRC-checked TEM requests
captured in `input/complete.log` and adds `06 23` write models for observed numeric
parameter selectors. It replaces the previously imported `tem/controller.tsp`.
See [Master-Analysis.md](Master-Analysis.md) for read coverage and remaining
gaps, [Write-Analysis.md](Write-Analysis.md) for write evidence, and [the
parameter index](master-output/Parameter.md) for model names by TEM parameter.
Parameters without an observed selector in `parameter.json` are not guessed.

Für Expert-Einsteller muss vor dem Lesen oder Schreiben zunächst die quittierte
Freischaltung `01 10 06 23 04 00 00 51 00` gesendet werden. Danach werden auch
Parameter wie `05-05` sichtbar; wiederholte `00 00`-Schreibungen halten die
Sitzung aktiv.

## Building the ebusd CSV configuration

The message definitions are written in [TypeSpec](https://typespec.io/) (`.tsp` files) using the [`@ebusd/ebus-typespec`](https://www.npmjs.com/package/@ebusd/ebus-typespec) library, with `main.tsp` as the entry point importing all circuit files. To compile them into the ebusd CSV configuration:

```bash
npm install
npm run build:csv
```

This emits one CSV file per circuit (e.g. `broadcast.csv`, `burner1.csv`, `remote1.csv`, ...) into `csv-output/@ebusd/ebus-typespec/hautec/`, ready to be placed in ebusd's configuration directory.

Note: circuit-specific `.tsp` source files intentionally do **not** use a `ZZ.` numeric filename prefix (e.g. `burner1.tsp`, not `03.burner1.tsp`). The circuit address is instead set via `@zz(...)` on the namespace. This is required because the emitter blanks the CSV `circuit` column whenever the source filename (minus a leading 2-hex-digit prefix) matches the circuit name — a convention meant for ebusd's `--scanconfig` auto-detection. Since this configuration is loaded as plain static CSV files (no `--scanconfig`), a blank circuit column causes ebusd to fail with `ERR: missing argument, circuit`.
