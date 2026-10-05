#!/usr/bin/env python3
"""Offline extraction of the 2026-10-03 heating experiment; no bus access."""
import json,csv
from bisect import bisect_left
from datetime import datetime
from pathlib import Path
from collections import defaultdict,Counter
ROOT = Path(__file__).resolve().parents[1]
import os
os.chdir(ROOT)
from analyze_master_log import unescape,crc,tem_id
from analyze_status_frequency import LINE,analyze
catalog={e['request']:e for e in json.load(open('master-output/requests.json'))['requests'] if e['service']=='0621'}
rows=[];params=[];telegrams=[];bad=[]
def dec(p,i,div=10):return int.from_bytes(p[i:i+2],'little',signed=True)/div
for n,line in enumerate(Path('ebusd.test1.log').read_text().splitlines(),1):
 m=LINE.fullmatch(line)
 if not m:continue
 try:
  d=unescape(bytes.fromhex(m[2].replace('<','').replace('>','')));end=5+d[4]
  if len(d)<=end or crc(d[:end])!=d[end]:continue
 except (ValueError,IndexError):continue
 t=m[1];key=d[:4].hex();p=d[5:end];tail=d[end+1:];resp=None
 if len(tail)>=4 and tail[0]==0 and len(tail)==tail[1]+4 and tail[-1]==0 and crc(tail[1:-2])==tail[-2]:resp=tail[2:-2]
 rec=dict(line=n,time=t,telegram=key,payload=p.hex(),response=resp.hex() if resp is not None else None,tail=tail.hex())
 telegrams.append(rec)
 def add(f,v):rows.append(dict(line=n,time=t,telegram=key,field=f,value=v,payload=p.hex()))
 if key in ['03100503','13100503']:
  fa='FA1' if key[:2]=='03' else 'FA2'
  for f,v in [('level',p[3]),('flow_coarse',p[4]/2),('status',p[1]),('status_bits',p[2]),('flame',(p[2]>>3)&1),('uwp',(p[2]>>6)&1)]:add(fa+'_'+f,v)
 elif key in ['10030501','10130501']:
  fa='FA1' if key[2:4]=='03' else 'FA2'
  for f,v in [('request',p[4]),('extra_byte5',p[5]),('extra_byte5_signed',int.from_bytes(p[5:6],'little',signed=True)),('command',p[0])]:add(fa+'_'+f,v)
 elif key=='10fe0801':
  add('return_0801',dec(p,0,256));add('tank_0801',dec(p,2,256));add('status_0801',p[5])
 elif key=='10fe0802':
  for i,f in [(0,'target_0802'),(2,'tank_target_0802')]:add(f,dec(p,i,256))
  add('expected_0802',int.from_bytes(p[4:5],'little',signed=True));add('error_device',p[5]);add('error_code',p[6])
 elif key=='10fe100a':
  selector=p[:2].hex()
  if selector=='1000':
   for i,f in [(2,'flow_1000'),(4,'return_1000'),(6,'hc_flow_1000'),(10,'tank_1000')]:add(f,dec(p,i))
  elif selector=='1001':add('HK2_candidate_1001',dec(p,6))
  elif selector in ['1002','1003']:
   for i in range(2,len(p),2):add('word'+str((i-2)//2)+'_'+selector,dec(p,i))
   add('target_'+selector,dec(p,6));add('tank_target_'+selector,dec(p,10))
  elif selector in ['1100','1101']:
   add('outside_'+selector,dec(p,2))
   for i,f in [(4,'a'),(5,'b')]:add('status_'+selector+'_'+f,p[i])
   for bit in range(8):add('bit'+str(bit)+'_'+selector,(p[4]>>bit)&1)
   add('dhw_'+selector,p[5]&1)
 elif key.endswith('0621'):
  if resp is None:bad.append({**rec,'reason':'invalid/incomplete transport'})
  elif resp[:2]==bytes.fromhex('ff1f'):bad.append({**rec,'reason':'ff1f'})
  elif len(resp)==10:
   ident=tem_id(resp.hex());typ,unit=resp[2:4]
   if typ in (13,77,141):v=dec(resp,8)
   elif typ in (1,193):v=int.from_bytes(resp[8:9],'little',signed=True)
   elif typ in (0,2,4,9):v=int.from_bytes(resp[8:10],'little')/(100 if ident=='03-10' else 1)
   else:continue
   e=catalog.get(p.hex(),{});ctx=e.get('context','unknown')
   params.append(dict(line=n,time=t,parameter=ident,context=ctx,value=v,selector=p.hex(),response=resp.hex()))
   add('TEM_'+ident+'_'+ctx,v)
out=Path('heating-test1-output');out.mkdir(exist_ok=True)
for name,data in [('bus-values',rows),('parameter-values',params)]:
 with (out/(name+'.csv')).open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
summary=analyze(Path('ebusd.test1.log'))[0];summary.update(invalid_reads=bad)
(out/'bus-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
# Retain only configuration/clock evidence, not a duplicate of the whole log.
evidence=[r for r in telegrams if r['telegram']=='10fe0700' or r['telegram'].endswith('0623') or (r['telegram'][4:]=='100a' and r['telegram'][2:4] in ('90','91'))]
(out/'telegram-evidence.json').write_text(json.dumps(evidence,indent=2)+'\n')
print('Wrote',len(rows),'bus values and',len(params),'parameter values to',out)

# Keep the quantitative comparisons and state edges reproducible alongside
# the full measurements. These comparisons do not establish physical outputs.
series = defaultdict(list)
for row in rows:
 series[row['field']].append({**row, 'dt': datetime.fromisoformat(row['time'])})
comparisons = []
for field,target,mask,active_level in [
 ('bit1_1100','FA1_level',1,None),
 ('bit2_1100','FA1_level',1,100),
 ('status_1100_b','FA2_level',4,100),
 ('status_1101_b','FA2_level',4,100),
]:
 values = series[target]
 times = [r['dt'] for r in values]
 matches = 0
 gaps = []
 mismatches = []
 for row in series[field]:
  i = bisect_left(times,row['dt'])
  if i == len(values):continue
  following = values[i]
  gap = (following['dt']-row['dt']).total_seconds()
  if gap > 10:continue
  observed = bool(int(row['value']) & mask)
  expected = following['value'] > 0 if active_level is None else following['value'] == active_level
  gaps.append(gap)
  matches += observed == expected
  if observed != expected:mismatches.append({'status_line':row['line'],'stage_line':following['line']})
 comparisons.append(dict(field=field,target=target,mask=mask,active_level=active_level,
                         pairs=len(gaps),matches=matches,max_gap_s=max(gaps),mismatches=mismatches))
mixer_pairs = Counter()
mixer_mismatches = []
direct = series['TEM_01-21_HK2']
times = [r['dt'] for r in direct]
for row in series['status_1101_a']:
 i = bisect_left(times,row['dt'])
 choices = direct[max(0,i-1):min(len(direct),i+1)]
 nearest = min(choices,key=lambda v:abs((v['dt']-row['dt']).total_seconds()))
 gap = abs((nearest['dt']-row['dt']).total_seconds())
 if gap > 10:continue
 mask = int(row['value']) & 0x60
 mixer_pairs[(mask,nearest['value'])] += 1
 if {0:0,0x20:100,0x40:-100}.get(mask) != nearest['value']:
  mixer_mismatches.append(dict(status_line=row['line'],direct_line=nearest['line'],gap_s=gap))
edges = {}
for field in ['FA1_level','FA2_level','FA1_uwp','status_1100_a','status_1100_b',
              'status_1101_a','status_1101_b','TEM_01-21_HK2','TEM_01-96_HK1']:
 changes = []
 previous = None
 for row in series[field]:
  if row['value'] != previous:
   changes.append({k:row[k] for k in ('time','line','value')})
   previous = row['value']
 edges[field] = changes
observations = dict(stage_comparisons=comparisons,
                    mixer_pairs=[dict(mask=mask,direct=value,count=count)
                                 for (mask,value),count in sorted(mixer_pairs.items())],
                    mixer_mismatches=mixer_mismatches,state_edges=edges)
(out/'observations.json').write_text(json.dumps(observations,indent=2)+'\n')
