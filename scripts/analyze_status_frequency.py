#!/usr/bin/env python3
"""Offline frequency statistics for ebusd raw logs; never contacts a device."""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from statistics import mean, median, pstdev

from analyze_master_log import crc, unescape

ROOT = Path(__file__).resolve().parents[1]
LINE = re.compile(r'(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d\.\d{3}) ([<>0-9a-fA-F]+)')


def definitions():
    result = []
    for filename in ('broadcast.tsp', 'remote1.tsp', 'remote2.tsp', 'burner1.tsp', 'burner2.tsp'):
        source = (ROOT / filename).read_text()
        source = re.sub(r'/\*.*?\*/|//[^\n]*', '', source, flags=re.S)
        for match in re.finditer(r'@zz\(([^)]+)\)\s*@id\(([^)]+)\)\s*model\s+(\w+)', source):
            destination = 0xfe if match[1] == 'BROADCAST' else int(match[1], 0)
            ident = bytes(int(part.strip(), 0) for part in match[2].split(','))
            result.append((filename, destination, ident, match[3]))
    return result


def label(key, defs):
    direction, src, dst, service, selector = key
    matches = []
    for filename, destination, ident, name in defs:
        if destination != int(dst, 16) or ident[:2].hex() != service:
            continue
        # Both burner files share destination 10: disambiguate using the sender.
        if service == '0503' and filename != {'03': 'burner1.tsp', '13': 'burner2.tsp'}.get(src):
            continue
        if service == '100a' and not bytes.fromhex(selector).startswith(ident[2:]):
            continue
        matches.append(name)
    return ' / '.join(matches) or f'{service} {selector}'.strip()


def percentile(values, fraction):
    ordered = sorted(values)
    pos = (len(ordered) - 1) * fraction
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    return ordered[lo] + (ordered[hi] - ordered[lo]) * (pos - lo)


def analyze(path):
    raw = path.read_bytes()
    clean = raw.lstrip(b'\0')
    if b'\0' in clean:
        raise ValueError('Embedded NUL bytes: inspect before parsing')
    groups, errors, transport = defaultdict(list), [], Counter()
    times = []
    for number, line in enumerate(clean.decode('utf-8').splitlines(), 1):
        try:
            match = LINE.fullmatch(line)
            if not match:
                raise ValueError('unsupported line format')
            time = datetime.fromisoformat(match[1])
            times.append(time)
            data = unescape(bytes.fromhex(match[2].replace('<', '').replace('>', '')))
            if len(data) < 6:
                raise ValueError('short fragment, no complete master header')
            end = 5 + data[4]
            if len(data) <= end:
                raise ValueError('incomplete master payload/CRC')
            if crc(data[:end]) != data[end]:
                raise ValueError('master CRC mismatch')
            tail = data[end + 1:]
            if data[1] == 0xfe:
                state = 'broadcast' if not tail else 'broadcast with trailing bytes'
            elif tail == b'\x00':
                state = 'master ACK'
            elif len(tail) >= 4 and tail[0] == 0 and len(tail) == tail[1] + 4 and tail[-1] == 0 and crc(tail[1:-2]) == tail[-2]:
                state = 'slave response CRC and ACK valid'
            else:
                state = 'master valid, response/ACK incomplete or unusual'
            transport[state] += 1
            service = data[2:4].hex()
            selector = data[5:7].hex() if service == '100a' else ''
            key = (match[2][0], data[:1].hex(), data[1:2].hex(), service, selector)
            groups[key].append((time, number))
        except ValueError as exc:
            errors.append({'line': number, 'reason': str(exc), 'text': line})
    if len(times) < 2 or any(b < a for a, b in zip(times, times[1:])):
        raise ValueError('insufficient or non-monotonic timestamps')
    duration = (times[-1] - times[0]).total_seconds()
    defs, rows, intervals = definitions(), [], []
    for key, samples in sorted(groups.items()):
        deltas = [(b[0] - a[0]).total_seconds() for a, b in zip(samples, samples[1:])]
        row = dict(zip(('direction', 'source', 'destination', 'service', 'selector'), key))
        row.update(name=label(key, defs), count=len(samples), per_hour=len(samples)*3600/duration,
                   first=samples[0][0].isoformat(' ', timespec='milliseconds'),
                   last=samples[-1][0].isoformat(' ', timespec='milliseconds'))
        stats = dict(min_s=min(deltas), median_s=median(deltas), mean_s=mean(deltas),
                     stddev_s=pstdev(deltas), p95_s=percentile(deltas, .95), max_s=max(deltas)) if deltas else {}
        row.update({name: stats.get(name) for name in ('min_s', 'median_s', 'mean_s', 'stddev_s', 'p95_s', 'max_s')})
        row['within_1s_of_median_pct'] = 100*sum(abs(d-stats["median_s"]) <= 1 for d in deltas)/len(deltas) if deltas else None
        rows.append(row)
        if key[2:4] == ('fe', '100a'):
            for (a, line_a), (b, line_b), delta in zip(samples, samples[1:], deltas):
                intervals.append(dict(name=row['name'], start=a.isoformat(' ', timespec='milliseconds'),
                                      end=b.isoformat(' ', timespec='milliseconds'), seconds=delta,
                                      start_line=line_a, end_line=line_b))
    summary = dict(input=str(path), sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw),
                   leading_nul_bytes=len(raw)-len(clean), lines=len(clean.decode().splitlines()),
                   first=str(times[0]), last=str(times[-1]), duration_s=duration,
                   valid_master_telegrams=sum(r['count'] for r in rows), excluded_lines=len(errors),
                   errors=dict(Counter(e['reason'] for e in errors)), transport=dict(transport),
                   longest_log_gap=max(((b-a).total_seconds(), str(a), str(b)) for a,b in zip(times,times[1:])))
    assert summary['valid_master_telegrams'] + len(errors) == summary['lines']
    return summary, rows, intervals, errors


def write_csv(path, rows):
    if not rows:
        return
    with path.open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def table(rows):
    lines = ['| Nachricht | Quelle → Ziel | Anzahl | Median s | Mittel s | P95 s | Maximum s | ±1 s um Median |',
             '|---|---|---:|---:|---:|---:|---:|---:|']
    for row in rows:
        numbers = ['—' if row[k] is None else f'{row[k]:.3f}' for k in ('median_s','mean_s','p95_s','max_s')]
        share = '—' if row['within_1s_of_median_pct'] is None else f"{row['within_1s_of_median_pct']:.2f} %"
        lines.append(f"| {row['name']} | `{row['source']} → {row['destination']}` | {row['count']} | " + ' | '.join(numbers + [share]) + ' |')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('log', nargs='?', type=Path, default=ROOT/'ebusd.log')
    parser.add_argument('--output', type=Path, default=ROOT/'status-output')
    args = parser.parse_args()
    summary, rows, intervals, errors = analyze(args.log)
    args.output.mkdir(parents=True, exist_ok=True)
    write_csv(args.output/'frequency.csv', rows)
    write_csv(args.output/'broadcast-intervals.csv', intervals)
    write_csv(args.output/'excluded-lines.csv', errors)
    (args.output/'summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n')
    status = sorted([r for r in rows if r['destination']=='fe' and r['service']=='100a'], key=lambda r:r['selector'])
    other = [r for r in rows if r['destination']=='fe' and r['service']!='100a']
    remote = [r for r in rows if r['source']=='10' and r['destination'] in ('90','91') and r['service']=='100a' and r['selector'] in ('0004','0005','d014','d015','d114','d115')]
    polling = [r for r in rows if r['source']=='31' and r['service']=='100a' and r['selector'] in ('0004','0005')]
    burner = [r for r in rows if r['service'] in ('0501','0503')]
    gap = summary['longest_log_gap']
    report = f'''# Häufigkeit und Regelmäßigkeit der Statusnachrichten

Datei: `{args.log.name}` · SHA-256: `{summary['sha256']}`

Zeitraum: **{summary['first']} bis {summary['last']}**, entsprechend **{summary['duration_s']/3600:.4f} Stunden**. Zeitangaben entsprechen unverändert der Log-Uhrzeit.

{summary['lines']} Raw-Zeilen, **{summary['valid_master_telegrams']} Telegramme mit gültiger Master-CRC**, {summary['excluded_lines']} ausgeschlossene Zeilen. Am Dateianfang stehen {summary['leading_nul_bytes']} Nullbytes ohne Zeitinformation; sie werden übersprungen. Die Quelldatei wird nicht verändert.

## Broadcast-Status aus broadcast.tsp

{table(status)}

Alle acht Statusblöcke haben einen Median von rund **80 Sekunden**. Die Selektorfamilien `10 xx` und `11 xx` sind getrennte Telegramme; die Namenssuffixe geben die beiden Selektorbytes hexadezimal wieder. Die CSV enthält die exakten Minima, Standardabweichungen, Zeitgrenzen und Raten pro Stunde. Die Quote ±1 s bezieht sich auf aufeinanderfolgende Abstände innerhalb der jeweiligen Nachrichtengruppe.

## Weitere Broadcasts

{table(other)}

## Status- und Änderungsabfragen des Reglers an die Bedienteile

{table(remote)}

## Durch ebusd gesendete Statusabfragen (Quelle 31)

{table(polling)}

Diese Abfragen werden getrennt von den durch Quelle 10 ausgelösten Reglertelegrammen gezählt. Ein Anfrage-/Antwortaustausch zählt einmal, nicht zweimal. Die Antwortdaten werden nicht als zusätzliche Broadcast-Nachricht gezählt.

## Betriebsdaten der Wärmeerzeuger

{table(burner)}

## Lücken

Die längste Lücke zwischen beliebigen aufeinanderfolgenden Raw-Zeilen beträgt **{gap[0]:.3f} s**, von **{gap[1]} bis {gap[2]}**. Ob währenddessen der Bus oder nur die Aufzeichnung unterbrochen war, lässt sich aus dem Mitschnitt allein nicht entscheiden. Die Abstände in den Tabellen enthalten diese Lücke; es werden keine vermeintlich fehlenden Telegramme ergänzt.

Die 16 längsten Abstände der acht Broadcast-Statusblöcke:

| Nachricht | Von | Bis | Abstand s | Logzeilen |
|---|---|---|---:|---|
'''
    for item in sorted(intervals, key=lambda i:i['seconds'], reverse=True)[:16]:
        report += f"| {item['name']} | {item['start']} | {item['end']} | {item['seconds']:.3f} | {item['start_line']} → {item['end_line']} |\n"
    report += '''
## Methode und Dateien

Gruppiert wird nach Richtung (`<` empfangen, `>` von ebusd gesendet), Quelle, Ziel und Dienst; bei `10 0a` zusätzlich nach den ersten beiden Nutzdatenbytes. Namen stammen aus den aktuellen TypeSpec-Dateien. Andere Dienste, etwa Parameterabfragen `06 21`, werden in der vollständigen CSV nach Dienst zusammengefasst. Alle Telegramme müssen vollständige Masterdaten und eine gültige Master-CRC enthalten. ACK-/Antwortprüfung ist separat in `summary.json` ausgewiesen und kein zusätzlicher Filter der Häufigkeit. Unvollständige Fragmente sind in `excluded-lines.csv` aufgelistet. Wiederholungen zählen als eigene beobachtete Übertragungen.

Intervalle sind Differenzen aufeinanderfolgender Log-Zeitstempel derselben Gruppe. P95 ist das linear interpolierte 95. Perzentil: 95 % der Abstände liegen höchstens ungefähr dort. Randzeiten vor dem ersten bzw. nach dem letzten Auftreten werden nicht als Intervalle behandelt. Die Statistik beschreibt diesen Mitschnitt, keine garantierten Protokollfristen. Aussagekräftig für den üblichen Takt sind Median und P95; Mittelwert und Maximum enthalten auch Unterbrechungen.

- [frequency.csv](frequency.csv): sämtliche beobachteten Nachrichtengruppen.
- [broadcast-intervals.csv](broadcast-intervals.csv): jeder Abstand der acht Broadcast-Statusblöcke mit Logzeilen.
- [summary.json](summary.json): Zeitraum, Prüfsumme, Parser- und Transportbilanz.
- [excluded-lines.csv](excluded-lines.csv): ausgeschlossene Fragmente/Fehler.

Reproduzieren: `python3 scripts/analyze_status_frequency.py ebusd.log`
'''
    (args.output/'Status-Statistik.md').write_text(report)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(table(status))


if __name__ == '__main__':
    main()
