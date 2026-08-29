#!/usr/bin/env python3
"""Valida 7A sobre 4689 registros reales verificados y mutaciones estructurales."""
from __future__ import annotations
import json,shutil,subprocess,sys,tempfile
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2];SCHEMA=ROOT/'analista/esquema/contratos-v1.0.0.schema.json';INPUT=ROOT/'analista/generado/verificados';OUTPUT=ROOT/'analista/generado/auditados';UNITS=ROOT/'analista/generado/unidades.jsonl';MOTOR=ROOT/'analista/motores/auditor_estructural.py'
FILES={'apariciones-conceptuales.jsonl':'aparicion_conceptual','conceptos.jsonl':'concepto','definiciones.jsonl':'definicion','afirmaciones-candidatas.jsonl':'afirmacion','formulas-candidatas.jsonl':'formula','relaciones-explicitas.jsonl':'relacion_explicita','distinciones.jsonl':'distincion','negaciones.jsonl':'negacion','excepciones.jsonl':'excepcion','restricciones-alcance.jsonl':'restriccion_alcance'}
COUNTS={'apariciones-conceptuales.jsonl':2575,'conceptos.jsonl':21,'definiciones.jsonl':60,'afirmaciones-candidatas.jsonl':333,'formulas-candidatas.jsonl':21,'relaciones-explicitas.jsonl':83,'distinciones.jsonl':233,'negaciones.jsonl':1346,'excepciones.jsonl':1,'restricciones-alcance.jsonl':16};TOTAL=sum(COUNTS.values())
def load(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def dump(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
def val(schema,name):return Draft202012Validator({'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':f'#/$defs/{name}'})
def run(inp,out,code=0):
 r=subprocess.run([sys.executable,str(MOTOR),'--input-root',str(inp),'--output-root',str(out),'--unidades',str(UNITS)],cwd=ROOT,text=True,capture_output=True);assert r.returncode==code,(r.returncode,r.stdout,r.stderr);return r
def copy_inputs(dst):dst.mkdir(parents=True,exist_ok=True);[shutil.copy2(INPUT/fn,dst/fn) for fn in FILES]
def status(root,fn,rid):return next(r['estado_auditoria'] for r in load(root/fn) if r['id']==rid)
def main():
 schema=json.loads(SCHEMA.read_text(encoding='utf-8'));validators={fn:val(schema,k) for fn,k in FILES.items()};result=run(INPUT,OUTPUT);assert f'"auditados": {TOTAL}' in result.stdout and '"rechazados": 0' in result.stdout
 snap={};total=0
 for fn,count in COUNTS.items():
  before=load(INPUT/fn);after=load(OUTPUT/fn);assert len(before)==len(after)==count;total+=count;snap[fn]=(OUTPUT/fn).read_bytes()
  for a,b in zip(before,after):
   errors=list(validators[fn].iter_errors(b));assert not errors,f"{b['id']}: {errors[0].message}";changed={k for k in set(a)|set(b) if a.get(k)!=b.get(k)};assert changed=={'estado_auditoria'};assert a['estado_verificacion']==b['estado_verificacion']=='verificado' and b['estado_auditoria']=='auditado'
 assert total==TOTAL==4689;run(INPUT,OUTPUT)
 for fn,b in snap.items():assert (OUTPUT/fn).read_bytes()==b,f'No reproducible: {fn}'
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);mut=td/'unverified';copy_inputs(mut);rows=load(mut/'negaciones.jsonl');rid=rows[0]['id'];rows[0]['estado_verificacion']='pendiente';dump(mut/'negaciones.jsonl',rows);out=td/'r1';run(mut,out,2);assert status(out,'negaciones.jsonl',rid)=='rechazado'
  mut=td/'broken';copy_inputs(mut);rows=load(mut/'relaciones-explicitas.jsonl');rid=rows[0]['id'];rows[0]['objeto_ref']='CON-INEXISTENTE';dump(mut/'relaciones-explicitas.jsonl',rows);out=td/'r2';run(mut,out,2);assert status(out,'relaciones-explicitas.jsonl',rid)=='rechazado'
  mut=td/'force';copy_inputs(mut);rows=load(mut/'negaciones.jsonl');idx=next(i for i,r in enumerate(rows) if r['clasificacion_negacion']=='negacion_candidata');rid=rows[idx]['id'];rows[idx]['estado_extraccion']='extraido';dump(mut/'negaciones.jsonl',rows);out=td/'r3';run(mut,out,2);assert status(out,'negaciones.jsonl',rid)=='rechazado'
  mut=td/'dup';copy_inputs(mut);rows=load(mut/'excepciones.jsonl');rows.append(dict(rows[0]));dump(mut/'excepciones.jsonl',rows);out=td/'r4';run(mut,out,2);assert all(r['estado_auditoria']=='rechazado' for r in load(out/'excepciones.jsonl'))
  mut=td/'formula';copy_inputs(mut);rows=load(mut/'formulas-candidatas.jsonl');rid=rows[0]['id'];rows[0]['contexto_unidad_ids']=[];dump(mut/'formulas-candidatas.jsonl',rows);out=td/'r5';run(mut,out,2);assert status(out,'formulas-candidatas.jsonl',rid)=='rechazado'
 print('OK Fase 7A: 4689 registros auditados; 0 rechazados; solo cambia estado_auditoria; mutaciones de verificación, referencia, fuerza, duplicado y contexto son rechazadas.');return 0
if __name__=='__main__':raise SystemExit(main())
