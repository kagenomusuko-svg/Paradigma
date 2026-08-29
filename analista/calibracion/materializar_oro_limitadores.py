#!/usr/bin/env python3
from __future__ import annotations
import base64,hashlib,json,re,zlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
CAL=ROOT/'analista/calibracion'; POLICY=CAL/'politica-oro-limitadores-v1.0.0.json'; LOCK=CAL/'muestra-fase8.lock.json'; UNITS=ROOT/'analista/generado/unidades.jsonl'; OUT=CAL/'patron-oro-limitadores.jsonl'; PILOTO='AA-SP-V1'
NO_RE=re.compile(r'(?<![\w-])no(?![\w-])',re.I); END_RE=re.compile(r'[.;?!:](?=\s|$)')

def load_jsonl(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def lr(u,t,a,b):
 base=u['localizacion']['linea_inicio']; return base+t[:a].count('\n'),base+t[:b].count('\n')
def blank(k,lit,li,lf,c):
 return {'tipo_registro':k,'texto_literal':lit,'linea_inicio':li,'linea_fin':lf,'clasificacion':c,'estatus_enunciativo':None,'concepto_designacion':None,'sujeto_designacion':None,'objeto_designacion':None,'termino_a_literal':None,'termino_b_literal':None,'objeto_negado_literal':None,'fragmento_literal':None}
def negs(u):
 t=u['texto_literal']; spans=[]; s=0
 for m in END_RE.finditer(t): spans.append((s,m.end(),True)); s=m.end()
 if s<len(t): spans.append((s,len(t),False))
 out=[]
 for a,b,complete in spans:
  clause=t[a:b]; ms=[m for m in NO_RE.finditer(clause) if not re.match(r'(?i)no\s+s[oó]lo\b',clause[m.start():])]
  if not ms: continue
  start=a+ms[0].start(); tail=t[start:b]; sm=re.search(r'(?i)\s+sino\b',tail)
  if sm: tail=tail[:sm.start()]
  lit=tail.strip(' \n\t.,;:!?'); lit=re.sub(r'\n[IVXLCDM]+\s*$','',lit).rstrip()
  if not lit: continue
  li,lf=lr(u,t,start,start+len(lit)); row=blank('negacion',lit,li,lf,'negacion_explicita' if complete else 'negacion_candidata'); row['objeto_negado_literal']=lit; out.append(row)
 return out
def anchors(policy):
 raw=zlib.decompress(base64.b64decode(policy['anclajes_zlib_base64'])); return json.loads(raw.decode('utf-8'))
def anchored(a,u):
 uid,kind,s,e,li,lf,classification,digest,*rest=a; lit=u['texto_literal'][s:e]
 if hashlib.sha256(lit.encode()).hexdigest()!=digest: raise AssertionError(f'Literal manual cambió: {uid}:{li}-{lf}')
 if lr(u,u['texto_literal'],s,e)!=(li,lf): raise AssertionError(f'Rango manual cambió: {uid}:{li}-{lf}')
 row=blank(kind,lit,li,lf,classification)
 if kind=='distincion':
  ai,ae,bi,be=rest; row['termino_a_literal']=lit[ai:ae]; row['termino_b_literal']=lit[bi:be]
  assert row['termino_a_literal'] in lit and row['termino_b_literal'] in lit
 elif kind in {'restriccion_alcance','excepcion'}: row['fragmento_literal']=lit
 return row
def materialize():
 policy=json.loads(POLICY.read_text(encoding='utf-8')); lock=json.loads(LOCK.read_text(encoding='utf-8')); units={r['id']:r for r in load_jsonl(UNITS) if r.get('fuente_id')==PILOTO}
 challenge=lock['desafios']['limitadores']; general=lock['desafios']['general']; ids=[]
 for uid in general+challenge:
  if uid not in ids: ids.append(uid)
 by={uid:[] for uid in ids}
 for a in anchors(policy):
  if a[0] not in by: raise AssertionError(f'Anclaje fuera del lock: {a[0]}')
  by[a[0]].append(a)
 rows=[]; seen=set()
 for uid in ids:
  items=negs(units[uid])+[anchored(a,units[uid]) for a in by[uid]]; items.sort(key=lambda x:(x['linea_inicio'],x['linea_fin'],x['tipo_registro'],x['texto_literal']))
  for i in items:
   key=(i['tipo_registro'],uid,i['texto_literal'],i['linea_inicio'],i['linea_fin'],i.get('termino_a_literal'),i.get('termino_b_literal'),i.get('objeto_negado_literal'),i.get('fragmento_literal'))
   if key in seen: raise AssertionError(f'Ítem duplicado: {key[:5]}')
   seen.add(key)
  rows.append({'version':'1.0.0','obra_id':PILOTO,'unidad_id':uid,'motor':'limitadores','estratos':(['general'] if uid in general else [])+(['desafio'] if uid in challenge else []),'revision_manual':True,'items_esperados':items,'observacion':'Revisión manual 4F: negaciones por cláusula con marcador no (se excluye el correlativo no solo); distinciones y restricciones por anclajes explícitos revisados; excepción literal. Sin inferir alcance hacia afirmaciones previas.'})
 payload=''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode(); exp=policy['producto']
 if len(rows)!=exp['revisiones'] or sum(len(r['items_esperados']) for r in rows)!=exp['items']: raise AssertionError('Conteos 4F divergentes')
 h=hashlib.sha256(payload).hexdigest()
 if h!=exp['sha256_jsonl']: raise AssertionError(f'Hash 4F divergente: {h}')
 return payload
def main(): OUT.write_bytes(materialize()); print('OK gold 4F: 56 revisiones/218 ítems; 31 general/96 y 27 desafío/132; hash congelado reproducido.'); return 0
if __name__=='__main__': raise SystemExit(main())
