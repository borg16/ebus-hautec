"""Betriebsphasen der Wärmepumpen aus den ebus-Daten in VictoriaMetrics ableiten.

Die Betriebsstundenzähler zählen die Anforderung der Stufen (flame), nicht den
Verdichterlauf. Dieses Skript trennt deshalb pro Zeitschritt:

* Anforderung Stufe 1/2   (Burner1/Burner2 ``flame``)
* Warmwasser              (``bwr_aktiv`` aus Broadcast/Status1a)
* Verdichter wahrscheinlich aktiv: Spreizung Vorlauf - Rücklauf (Status0b)
  größer als ``--spread`` Kelvin. Die Hausleistung wird nur ausgewiesen
  (Mittelwert, Überschuss über Grundlast), weil andere Verbraucher stören.

Beispiele:
    python3 scripts/analyze_operation.py 2026-10-11T00:00 now
    python3 scripts/analyze_operation.py -- -24h now --spread 3 --segments
"""
import argparse
import datetime as dt

from vm_query import _ts, query_range

STATUS0B = 'topic="ebusd/Broadcast/Status0b"'
QUERIES = {
    "tf": f"ebus_tf_hp_value{{{STATUS0B}}}",
    "tr": f"ebus_tr_hp_value{{{STATUS0B}}}",
    "tb": f"ebus_tb_value{{{STATUS0B}}}",
    "ww": 'ebus_bwr_aktiv_value{topic="ebusd/Broadcast/Status1a"}',
    "f1": 'ebus_flame_value{topic=~"ebusd/Burner1/.*"}',
    "f2": 'ebus_flame_value{topic=~"ebusd/Burner2/.*"}',
    "pow": "senec_ENERGY_GUI_HOUSE_POW",
}


def load(start, end, step):
    series = {}
    for key, expr in QUERIES.items():
        result = query_range(expr, start, end, f"{step}s")
        series[key] = {int(t): float(v) for t, v in result[0]["values"]} if result else {}
    return series


def classify(series, t, spread):
    """Gibt (Modus, Verdichter-Indiz, Stufe 1, Stufe 2) für den Zeitpunkt zurück."""
    g = lambda k: series[k].get(t)
    tf, tr = g("tf"), g("tr")
    active = tf is not None and tr is not None and tf - tr > spread
    mode = "WW" if g("ww") else ("Heizen" if active else "-")
    return mode, active, bool(g("f1")), bool(g("f2"))


def label(mode, active, s1, s2):
    stages = ("S1+S2" if s1 and s2 else "S1" if s1 else "S2" if s2 else "keine")
    return f"{mode:6} Anforderung {stages:5} Verdichter {'ja' if active else 'nein'}"


def fmt(t):
    return dt.datetime.fromtimestamp(t).strftime("%d.%m. %H:%M")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("start")
    parser.add_argument("end")
    parser.add_argument("--step", type=int, default=30, help="Auflösung in Sekunden")
    parser.add_argument("--spread", type=float, default=4.0, help="Vorlauf-Rücklauf-Schwelle in K")
    parser.add_argument("--base", type=float, default=900.0, help="Grundlast in W")
    parser.add_argument("--segments", action="store_true", help="alle Phasen einzeln ausgeben")
    args = parser.parse_args()

    series = load(args.start, args.end, args.step)
    times = sorted(series["tf"])
    if not times:
        raise SystemExit("keine Daten")

    segments = []
    for t in times:
        state = classify(series, t, args.spread)
        power = series["pow"].get(t)
        if segments and segments[-1]["state"] == state:
            segments[-1]["end"] = t + args.step
            segments[-1]["power"].append(power)
        else:
            segments.append({"state": state, "start": t, "end": t + args.step, "power": [power]})

    totals = {}
    for seg in segments:
        totals.setdefault(seg["state"], 0)
        totals[seg["state"]] += seg["end"] - seg["start"]

    if args.segments:
        print("Phasen (Hausleistung = Median, W):")
        for seg in segments:
            if seg["end"] - seg["start"] < 2 * args.step:
                continue
            p = sorted(x for x in seg["power"] if x is not None)
            med = f"{p[len(p) // 2]:6.0f}" if p else "     -"
            print(f"  {fmt(seg['start'])} - {fmt(seg['end'])}  {label(*seg['state'])}  {med} W")
        print()

    print("Summen je Zustand:")
    for state, secs in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"  {label(*state)}  {secs / 3600:6.2f} h")

    def hours(pred):
        return sum(s for st, s in totals.items() if pred(st)) / 3600

    print()
    print("Zusammenfassung:")
    print(f"  Stufe 1 angefordert    {hours(lambda s: s[2]):6.2f} h")
    print(f"  Stufe 2 angefordert    {hours(lambda s: s[3]):6.2f} h")
    print(f"  Verdichter-Indiz       {hours(lambda s: s[1]):6.2f} h")
    print(f"    davon Warmwasser     {hours(lambda s: s[1] and s[0] == 'WW'):6.2f} h")
    print(f"    davon Heizen         {hours(lambda s: s[1] and s[0] == 'Heizen'):6.2f} h")
    print(f"    davon beide Stufen   {hours(lambda s: s[1] and s[2] and s[3]):6.2f} h")
    print(f"  angefordert ohne Lauf  {hours(lambda s: (s[2] or s[3]) and not s[1]):6.2f} h")

    both = [
        (t, series["pow"][t])
        for t in times
        if t in series["pow"] and classify(series, t, args.spread)[1:] == (True, True, True)
    ]
    one = [
        (t, series["pow"][t])
        for t in times
        if t in series["pow"] and classify(series, t, args.spread)[1:] == (True, True, False)
    ]
    for name, rows in (("nur Stufe 1", one), ("beide Stufen", both)):
        values = sorted(v for _, v in rows)
        if values:
            print(f"  Hausleistung bei Verdichter-Indiz, {name}: Median {values[len(values) // 2]:.0f} W "
                  f"(Grundlast {args.base:.0f} W)")


if __name__ == "__main__":
    main()
