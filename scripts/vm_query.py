"""Kleine Hilfe für Abfragen der ebus-Daten in VictoriaMetrics (nur Standardbibliothek).

Beispiel:
    python3 scripts/vm_query.py 'ebus_tf_hp_value{topic="ebusd/Broadcast/Status0b"}' -- -6h now 1m
    python3 scripts/vm_query.py --all ebus_startcounter_value -- -8d now 1h
"""
import argparse
import datetime as dt
import json
import time
import urllib.parse
import urllib.request

BASE = "http://raspi:8428"


def _ts(value):
    """Akzeptiert 'now', relative Werte wie '-6h' oder 'YYYY-MM-DDTHH:MM' (lokale Zeit)."""
    if value == "now":
        return int(time.time())
    if value[0] == "-":
        factor = {"s": 1, "m": 60, "h": 3600, "d": 86400}[value[-1]]
        return int(time.time()) - int(value[1:-1]) * factor
    return int(dt.datetime.fromisoformat(value).timestamp())


def query_range(expr, start, end, step):
    params = urllib.parse.urlencode(
        {"query": expr, "start": _ts(start), "end": _ts(end), "step": step}
    )
    with urllib.request.urlopen(f"{BASE}/api/v1/query_range?{params}") as r:
        return json.load(r)["data"]["result"]


def print_changes(result, show_all=False):
    for series in result:
        metric = series["metric"]
        print("#", metric.get("topic"), metric["__name__"])
        previous = None
        for t, value in series["values"]:
            if show_all or value != previous:
                stamp = dt.datetime.fromtimestamp(t).strftime("%m-%d %H:%M:%S")
                print(" ", stamp, value)
                previous = value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("expr")
    parser.add_argument("start")
    parser.add_argument("end")
    parser.add_argument("step")
    parser.add_argument("--all", action="store_true", help="alle Werte statt nur Änderungen")
    args = parser.parse_args()
    print_changes(query_range(args.expr, args.start, args.end, args.step), args.all)
