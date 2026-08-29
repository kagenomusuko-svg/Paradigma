#!/usr/bin/env python3
"""Verificador mecánico de evidencia — Fase 6. No reclasifica contenido."""
from __future__ import annotations
import argparse,collections,copy,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];DF=ROOT/'analista/generado/fuentes.jsonl';DU=ROOT/'analista/generado/unidades.jsonl';DI=ROOT/'analista/generado/normalizados';DO=ROOT/'analista/generado/verificados'
FILES=('apariciones-conceptuales.jsonl','conceptos.jsonl','definiciones.jsonl','afirmaciones-candidatas.jsonl','formulas-candidatas.jsonl','relaciones-explicitas.jsonl','distinciones.jsonl','negaciones.jsonl','excepciones.jsonl','restricciones-alcance.jsonl')
PRODUCER={'aparicion_conceptual':('conceptos_apariciones','1.1.0'),'concepto':('conceptos_apariciones','1.1.0'),'definicion':('definiciones','1.1.0'),'afirmacion':('afirmaciones','1.1.0'),'formula':('formulas','1.1.0'),'relacion_explicita':('relaciones_explicitas','1.1.0'),'distincion':('limitadores','1.1.0'),'negacion':('limitadores','1.1.0'),'excepcion':('limitadores','1.1.0'),'restriccion_alcance':('limitadores','1.1.0')}
def load(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def dump(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
def excerpt(repo,loc,cache):
 route=loc['ruta'];cache.setdefault(route,(repo/route).read_text(encoding='utf-8').splitlines());s,e=loc['linea_inicio'],loc['linea_fin'];lines=cache[route]
 if not isinstance(s,int) or not isinstance(e,int) or not 1<=s<=e<=len(lines):raise ValueError('rango')
 return '\n'.join(lines[s-1:e])
def literal_excerpt(lit,ex):
 if not lit:return False
 p=ex.find(lit)
 return p>=0 and '\n' not in ex[:p] and '\n' not in ex[p+len(lit):]
def occurrences(unit,lit):
 if not lit:return []
 t=unit['texto_literal'];base=unit['localizacion']['linea_inicio'];out=[];start=0
 while True:
  p=t.find(lit,start)
  if p<0:break
  ls=base+t[:p].count('\n');out.append((ls,ls+lit.count('\n')));start=p+1
 return out
def located(unit,lit,loc):return (loc['linea_inicio'],loc['linea_fin']) in occurrences(unit,lit)
def producer(r):
 exp=PRODUCER.get(r.get('tipo_registro'));return bool(exp and r.get('schema_version')=='1.0.0' and r.get('producido_por')=={'motor':exp[0],'version':exp[1]})
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo-root',type=Path,default=ROOT);ap.add_argument('--fuentes',type=Path,default=DF);ap.add_argument('--unidades',type=Path,default=DU);ap.add_argument('--input-root',type=Path,default=DI);ap.add_argument('--output-root',type=Path,default=DO);a=ap.parse_args()
 sources={r['id']:r for r in load(a.fuentes)};units={r['id']:r for r in load(a.unidades)};by={n:load(a.input_root/n) for n in FILES};flat=[r for rows in by.values() for r in rows];counts=collections.Counter(r.get('id') for r in flat);apps={r['id']:r for r in by['apariciones-conceptuales.jsonl']};concepts={r['id']:r for r in by['conceptos.jsonl']};affirm={r['id']:r for r in by['afirmaciones-candidatas.jsonl']};cache={}
 used={r.get('fuente_id') for r in flat if r.get('fuente_id')};source_ok={}
 for sid in used:
  s=sources.get(sid);ok=bool(s)
  try:
   if ok:
    h=hashlib.sha256((a.repo_root/s['ruta_canonica']).read_bytes()).hexdigest();ok=s.get('schema_version')=='1.0.0' and s.get('producido_por')=={'motor':'fuentes','version':'1.0.1'} and s.get('sha256')==h and s.get('version_fuente')==f'sha256:{h}' and set(s.get('rutas_derivadas',[]))==set(s.get('segmentaciones',[]))
  except Exception:ok=False
  source_ok[sid]=bool(ok)
 unit_ok={}
 def verify_unit(uid):
  if uid in unit_ok:return unit_ok[uid]
  u=units.get(uid);ok=bool(u)
  try:
   if ok:
    s=sources.get(u['fuente_id']);loc=u['localizacion'];ok=u.get('schema_version')=='1.0.0' and u.get('producido_por')=={'motor':'unidades','version':'1.0.0'} and source_ok.get(u['fuente_id'],False) and s is not None and u['archivo']==loc['ruta'] and u['archivo'] in s.get('rutas_derivadas',[]) and excerpt(a.repo_root,loc,cache)==u['texto_literal'] and hashlib.sha256(u['texto_literal'].encode()).hexdigest()==u['sha256_texto']
  except Exception:ok=False
  unit_ok[uid]=bool(ok);return bool(ok)
 verdict={};reasons={}
 def fail(rid,why):reasons.setdefault(rid,[]).append(why)
 for name,rows in by.items():
  if name=='conceptos.jsonl':continue
  for r in rows:
   rid=r.get('id','');kind=r['tipo_registro'];ok=True;sid=r.get('fuente_id');uid=r.get('unidad_id');u=units.get(uid)
   if counts[rid]!=1:fail(rid,'id_no_unico');ok=False
   if not producer(r):fail(rid,'version_o_productor');ok=False
   if not source_ok.get(sid,False):fail(rid,'fuente_o_hash');ok=False
   if not verify_unit(uid):fail(rid,'unidad');ok=False
   try:
    loc=r['localizacion'];ex=excerpt(a.repo_root,loc,cache)
    if u is None or u.get('fuente_id')!=sid or loc['ruta']!=u.get('archivo'):fail(rid,'unidad_fuente_ruta');ok=False
    if kind=='aparicion_conceptual':ok=ok and r['texto_literal']==r['forma_literal'] and located(u,r['forma_literal'],loc) and (r.get('concepto_id') is None or r['concepto_id'] in concepts)
    elif kind=='definicion':ok=ok and u['localizacion']['linea_inicio']<=loc['linea_inicio']<=u['localizacion']['linea_fin'] and literal_excerpt(r['texto_literal'],ex) and r.get('concepto_id') in concepts
    elif kind=='afirmacion':ok=ok and u['localizacion']['linea_inicio']<=loc['linea_inicio']<=loc['linea_fin']<=u['localizacion']['linea_fin'] and literal_excerpt(r['texto_literal'],ex) and all(c in concepts for c in r.get('concepto_ids',[]))
    elif kind=='formula':ok=ok and r['texto_literal']==r['formula_literal'] and located(u,r['formula_literal'],loc) and u['id'] in r.get('contexto_unidad_ids',[]) and all(verify_unit(c) and units[c]['fuente_id']==sid and units[c]['archivo']==u['archivo'] for c in r.get('contexto_unidad_ids',[]))
    elif kind=='relacion_explicita':ok=ok and r['texto_literal']==r['relacion_literal'] and literal_excerpt(r['relacion_literal'],ex) and r.get('sujeto_ref') in concepts and r.get('objeto_ref') in concepts
    elif kind=='distincion':ok=ok and located(u,r['texto_literal'],loc) and r['termino_a_literal'] in r['texto_literal'] and r['termino_b_literal'] in r['texto_literal'] and (r.get('marcador_literal') is None or r['marcador_literal'] in ex)
    elif kind=='negacion':ok=ok and located(u,r['texto_literal'],loc) and r['objeto_negado_literal'] in ex and (r.get('alcance_literal') is None or r['alcance_literal'] in ex)
    elif kind=='excepcion':ok=ok and r['texto_literal']==r['fragmento_exceptivo_literal'] and located(u,r['texto_literal'],loc) and (r.get('afirmacion_limitada_id') is None or r['afirmacion_limitada_id'] in affirm)
    elif kind=='restriccion_alcance':ok=ok and r['texto_literal']==r['fragmento_restriccion_literal'] and located(u,r['texto_literal'],loc) and (r.get('afirmacion_limitada_id') is None or r['afirmacion_limitada_id'] in affirm)
   except Exception:ok=False;fail(rid,'excepcion_verificacion')
   if not ok and rid not in reasons:fail(rid,'evidencia_directa')
   verdict[rid]=bool(ok)
 for c in by['conceptos.jsonl']:
  rid=c['id'];ok=counts[rid]==1 and producer(c);aids=c.get('aparicion_ids',[]);evid=c.get('evidencia_identidad_ids',[]);ok=ok and bool(aids) and all(x in apps and verdict.get(x,False) and apps[x].get('concepto_id')==rid for x in aids) and all(x in aids for x in evid)
  if c.get('estado_identidad_conceptual')=='establecida_por_evidencia':ok=ok and bool(evid) and all(verdict.get(x,False) for x in evid)
  verdict[rid]=bool(ok)
 total=failed=0
 for name,rows in by.items():
  out=[]
  for src in rows:
   r=copy.deepcopy(src);good=verdict.get(r['id'],False);r['estado_verificacion']='verificado' if good else 'fallido';total+=1;failed+=int(not good);out.append(r)
  dump(a.output_root/name,out)
 print(json.dumps({'total':total,'verificados':total-failed,'fallidos':failed,'fuentes':source_ok,'unidades_comprobadas':len(unit_ok),'unidades_validas':sum(unit_ok.values())},ensure_ascii=False,sort_keys=True))
 if failed:
  for rid in sorted(reasons):print(f"FALLO {rid}: {','.join(reasons[rid])}")
 return 0 if failed==0 else 2
if __name__=='__main__':raise SystemExit(main())
