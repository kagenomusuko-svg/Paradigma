#!/usr/bin/env python3
"""Valida 7B sobre los registros calibrados sin resolver doctrina."""
from __future__ import annotations
import importlib.util,json,shutil,subprocess,sys,tempfile
from collections import Counter
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2];SCHEMA=ROOT/'analista/esquema/contratos-v1.0.0.schema.json';INPUT=ROOT/'analista/generado/auditados';OUTPUT=ROOT/'analista/generado/hallazgos-auditoria.jsonl';MOTOR=ROOT/'analista/motores/auditor_descriptivo.py'
FILES=('apariciones-conceptuales.jsonl','conceptos.jsonl','definiciones.jsonl','afirmaciones-candidatas.jsonl','formulas-candidatas.jsonl','relaciones-explicitas.jsonl','distinciones.jsonl','negaciones.jsonl','excepciones.jsonl','restricciones-alcance.jsonl')
EXPECTED={'uso_singular':13,'definiciones_multiples':13,'variacion_de_objeto':11,'relacion_repetida':1,'negacion_explicita':1258,'excepcion_explicita':1,'restriccion_de_alcance':16};TOTAL=sum(EXPECTED.values())
def load(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def run(inp=INPUT,out=OUTPUT,code=0):
 r=subprocess.run([sys.executable,str(MOTOR),'--input-root',str(inp),'--output',str(out)],cwd=ROOT,text=True,capture_output=True);assert r.returncode==code,(r.returncode,r.stdout,r.stderr);return r
def import_motor():
 spec=importlib.util.spec_from_file_location('auditor_descriptivo',MOTOR);assert spec and spec.loader;m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def main():
 schema=json.loads(SCHEMA.read_text(encoding='utf-8'));v=Draft202012Validator({'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':'#/$defs/hallazgo_auditoria'});first=run();assert f'"hallazgos": {TOTAL}' in first.stdout;findings=load(OUTPUT);assert len(findings)==TOTAL and Counter(r['categoria'] for r in findings)==EXPECTED
 by={fn:load(INPUT/fn) for fn in FILES};allr={r['id']:r for rows in by.values() for r in rows};concepts={r['id']:r for r in by['conceptos.jsonl']}
 for f in findings:
  errors=list(v.iter_errors(f));assert not errors,f"{f['id']}: {errors[0].message}";assert f['estado_verificacion']=='verificado' and f['estado_auditoria']=='auditado' and f['resolucion_doctrinal']=='no_realizada' and f['producido_por']=={'motor':'auditor_descriptivo','version':'1.0.0'};assert all(rid in allr for rid in f['registro_ids'])
 mapping={'negacion_explicita':('negacion','clasificacion_negacion','negacion_explicita'),'excepcion_explicita':('excepcion','clasificacion_excepcion','excepcion_explicita'),'restriccion_de_alcance':('restriccion_alcance','clasificacion_restriccion','restriccion_explicita')}
 for cat,(kind,field,label) in mapping.items():
  rows=[f for f in findings if f['categoria']==cat];assert len(rows)==EXPECTED[cat]
  for f in rows:
   assert len(f['registro_ids'])==1;r=allr[f['registro_ids'][0]];assert r['tipo_registro']==kind and r[field]==label;assert r['estatus_enunciativo']=='no_determinado'
 appearances=by['apariciones-conceptuales.jsonl'];sing=[f for f in findings if f['categoria']=='uso_singular'];assert len(sing)==13
 for f in sing:
  app=allr[f['registro_ids'][-1]] if allr[f['registro_ids'][-1]]['tipo_registro']=='aparicion_conceptual' else allr[f['registro_ids'][0]];cid=app['concepto_id'];assert cid in concepts and sum(1 for r in appearances if r.get('concepto_id')==cid)==1
 defs={r['id']:r for r in by['definiciones.jsonl']}
 for f in (x for x in findings if x['categoria']=='definiciones_multiples'):
  rows=[defs[rid] for rid in f['registro_ids']];assert len(rows)>1 and len({r['concepto_id'] for r in rows})==1
 rel={r['id']:r for r in by['relaciones-explicitas.jsonl']};vars=[f for f in findings if f['categoria']=='variacion_de_objeto'];assert len(vars)==11
 for f in vars:
  rows=[rel[rid] for rid in f['registro_ids']];assert len({r['sujeto_ref'] for r in rows})==1 and len({r['objeto_ref'] for r in rows})>1
 repeated=next(f for f in findings if f['categoria']=='relacion_repetida');rr=[rel[rid] for rid in repeated['registro_ids']];assert len(rr)==2 and len({(r['sujeto_ref'],r['objeto_ref'],r['relacion_literal']) for r in rr})==1
 module=import_motor()
 for cid in concepts:
  dossier=module.records_for_concept(cid,by);expected=[r for r in appearances if r.get('concepto_id')==cid]+[r for r in by['definiciones.jsonl'] if r.get('concepto_id')==cid]+[r for r in by['afirmaciones-candidatas.jsonl'] if cid in r.get('concepto_ids',[])]+[r for r in by['relaciones-explicitas.jsonl'] if r.get('sujeto_ref')==cid or r.get('objeto_ref')==cid];assert {r['id'] for r in dossier}=={r['id'] for r in expected}
 snap=OUTPUT.read_bytes();run();assert OUTPUT.read_bytes()==snap
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);mut=td/'auditados';mut.mkdir();[shutil.copy2(INPUT/fn,mut/fn) for fn in FILES];rows=load(mut/'negaciones.jsonl');rows[0]['estado_auditoria']='pendiente';(mut/'negaciones.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8');out=td/'hallazgos.jsonl';run(mut,out,1);assert not out.exists()
 print('OK Fase 7B: 1313 hallazgos reproducibles; 1258 negaciones, 16 restricciones y 1 excepción explícitas se conservan sin atribuir voz ni resolver alcance doctrinal; multiplicidades previas preservadas.');return 0
if __name__=='__main__':raise SystemExit(main())
