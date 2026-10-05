#!/usr/bin/env python3
"""Plot offline test2 extraction; timestamps are unconverted log times."""
import csv
import os
from collections import defaultdict
from datetime import datetime
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', '/tmp/hautec-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

out = Path(__file__).resolve().parents[1] / 'overnight-test2-output'
series = defaultdict(list)
for row in csv.DictReader((out/'bus-values.csv').open()):
    series[row['field']].append((datetime.fromisoformat(row['time']),float(row['value'])))
fig, axes = plt.subplots(3, 1, figsize=(13,9), sharex=True)
groups = [
    [('outside_1100','Außentemperatur','#247ab0'),('TEM_02-20_HK1','Außenmittel 02-20 HK1','#d07515')],
    [('target_1002','HK1-Soll (Zuordnung aus Voranalysen)','#247ab0'),('target_1003','HK2-Soll (Zuordnung aus Voranalysen)','#b1448c'),('target_0802','WE-Soll 08 02','#d07515')],
    [('FA1_level','FA1-Busstufe; kein gemessener Verdichterstrom','#804da1')],
]
start=datetime.fromisoformat('2026-10-03 23:10:05.953')
stop=datetime.fromisoformat('2026-10-04 07:09:55.735')
for ax,fields,label in zip(axes,groups,['Temperatur [°C]','Sollwert [°C]','Busstufe [%]']):
    for key,title,color in fields:
        x,y=zip(*series[key])
        ax.step(x,y,where='post',label=title,color=color,lw=1.2)
    ax.axvspan(start,stop,color='#247ab0',alpha=.07)
    ax.set_ylabel(label);ax.grid(alpha=.2);ax.legend(loc='upper right',fontsize=8)
axes[0].set_title('Nacht 03./04.10.2026: HK2-Kühlanforderung und kurze FA1-Stufenphasen')
axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
axes[-1].set_xlabel('Log-Uhrzeit; Regleruhr etwa 9 min 13 s früher. Blau: aus Sollwerten abgeleitete Kühlphase.')
fig.tight_layout()
fig.savefig(out/'overview.png',dpi=150)
fig.savefig(out/'overview.svg')
