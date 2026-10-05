#!/usr/bin/env python3
"""Plot extracted test1 observations without accessing the heating bus."""
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

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'heating-test1-output'
series = defaultdict(list)
for row in csv.DictReader((OUT / 'bus-values.csv').open()):
    series[row['field']].append((datetime.fromisoformat(row['time']), float(row['value'])))

def moment(value):
    return datetime.fromisoformat('2026-10-03 ' + value)

def draw(ax, field, label, color, style='-', points=False, window=None):
    values = series[field]
    if window:
        values = [(t,v) for t,v in values if window[0] <= t <= window[1]]
    if not values:
        return
    times, values = zip(*values)
    if points:
        ax.plot(times, values, '.', ms=3.5, color=color, label=label)
    else:
        # Do not imply uninterrupted direct observations across the initial
        # parameter polling gap (roughly 10:55-11:16).
        if field.startswith('TEM_') and field != 'TEM_02-20_HK1':
            expanded = []
            for i, (t, value) in enumerate(zip(times, values)):
                if i and (t - times[i-1]).total_seconds() > 30:
                    expanded.append((times[i-1], float('nan')))
                expanded.append((t, value))
            times, values = zip(*expanded)
        ax.step(times, values, where='post', lw=1.3, color=color, ls=style, label=label)

fig, axes = plt.subplots(4, 1, figsize=(14, 12), sharex=True,
                         gridspec_kw={'height_ratios':[2,1.3,1,1.2]})
for f,label,c,style in [
    ('TEM_00-07_HK1','TWV / Eingang 47, direkt','#ba9200','-'),
    ('TEM_00-08_HK1','Ruecklauf / Eingang 48, direkt','#dd6528','-'),
    ('TEM_00-02_HK2','HK2-Ist / Eingang 43, direkt','#3670b4','-'),
    ('tank_1000','Speicher TB, Broadcast','#39854e','-'),
    ('TEM_01-96_HK1','Anlagensoll 01-96','#ad44a1','--')]:
    draw(axes[0],f,label,c,style)
draw(axes[1],'target_1002','Sollkandidat 10 02 / HK1','#3670b4')
draw(axes[1],'target_1003','Sollkandidat 10 03 / HK2','#ad44a1')
draw(axes[1],'TEM_02-20_HK1','Gemittelte Aussentemperatur','#39854e')
axes[1].axhline(17,color='#777777',ls=':',label='HK2 Heizgrenze: 17 C')
draw(axes[2],'FA1_level','FA1 gemeldete Stufe','#8250a0')
draw(axes[2],'FA2_level','FA2 gemeldete Stufe; physische Zuordnung offen','#ca7523','--')
draw(axes[3],'TEM_01-21_HK2','HK2 Stellbefehl, direkte Stichproben','#3670b4',points=True)
for field,label,c in [('bit5_1101','Auf-Bit: gesetzte 80-s-Stichproben','#258744'),('bit6_1101','Zu-Bit: gesetzte 80-s-Stichproben','#c24643')]:
    vals=[(t,100 if field.startswith('bit5') else -100) for t,v in series[field] if v]
    if vals: axes[3].plot(*zip(*vals),'x',color=c,ms=5,label=label)
for ax,label in zip(axes,['Temperatur [C]','Temperatur [C]','Busstufe [%]','Stellbefehl [%]']):
    ax.set_ylabel(label);ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=8,ncol=2)
    for t in ['12:09:12','12:33:33','13:30:37','14:20:51','15:09:42']:
        ax.axvline(moment(t),color='#888888',lw=.7,alpha=.55)
axes[-1].set_xlim(moment('10:53:24'),moment('15:29:45'))
axes[-1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
axes[-1].set_xlabel('03.10.2026, Log-Zeit (Europe/Berlin); Regleruhr etwa 9 min 12 s zurueck')
fig.suptitle('Heizversuch test1: Standby-Impuls, Warmwasserende und Aktivierung von HK2')
fig.text(.02,.015,'Busstufen sind keine Strommessung. Mischerwerte als Stichproben; kurze Impulse koennen fehlen.\nElektrische Leistung aus dem Screenshot wird nicht als numerische Messreihe rekonstruiert.',fontsize=9)
fig.tight_layout(rect=(0,.06,1,.96))
for ext in ['png','svg']:fig.savefig(OUT/f'overview.{ext}',dpi=160)
plt.close(fig)

for name,start,end,title in [
    ('noon','12:08:45','12:10:05','Kurzer HK2-Befehl bei Standby: Beginn um Reglerzeit 12:00'),
    ('mixer-detail','15:06:00','15:26:00','HK2: letzte Auf-Impulse, anschliessend 15 Minuten Zu-Befehl')]:
    window=(moment(start),moment(end))
    fig,axes=plt.subplots(2,1,figsize=(12,6),sharex=True)
    draw(axes[0],'TEM_01-21_HK2','01-21 HK2 (Punkte: direkte Messungen)','#3670b4',points=True,window=window)
    for field,factor,label,c in [('bit5_1101',100,'Auf-Bit 5','#258744'),('bit6_1101',-100,'Zu-Bit 6','#c24643')]:
        a=[(t,v*factor) for t,v in series[field] if window[0]<=t<=window[1]]
        if a:axes[0].plot(*zip(*a),'x',color=c,ms=7,label=label)
    draw(axes[1],'FA1_level','FA1-Stufenmeldung','#8250a0',window=window)
    draw(axes[1],'FA2_level','FA2-Stufenmeldung','#ca7523','--',window=window)
    if name=='noon':
        for ax in axes:ax.axvline(moment('12:09:12'),color='#555555',ls=':',label='Regler 12:00 (ca.)')
    for ax in axes:
        ax.grid(alpha=.2);ax.legend(fontsize=8,loc='upper right');ax.set_ylim(-110,115)
    axes[0].set_ylabel('Stellbefehl [%]');axes[1].set_ylabel('Busstufe [%]')
    axes[1].set_xlim(*window);axes[1].xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    axes[1].set_xlabel('Log-Zeit am 03.10.2026 (Europe/Berlin)')
    fig.suptitle(title);fig.tight_layout(rect=(0,0,1,.94))
    for ext in ['png','svg']:fig.savefig(OUT/f'{name}.{ext}',dpi=160)
    plt.close(fig)
print('Wrote overview, noon and mixer-detail figures to',OUT)
