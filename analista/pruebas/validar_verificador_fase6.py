#!/usr/bin/env python3
"""Valida Fase 6 sobre productos reales y fallos mecánicos inducidos."""
from __future__ import annotations
import json,shutil,subprocess,sys,tempfile
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2];SCHEMA=ROOT/'analista/esquema/contratos-v1.0.0.schema.json';FUENTES=ROOT/'analista/generado/fuentes.jsonl';UNIDADES=ROOT/'analista/generado/unidades.jsonl';INPUT=ROOT/'analista/generado/normalizados';OUTPUT=ROOT/'analista/generado/verificados';MOTOR=ROOT/'analista/motores/verificador_evidencia.py'
FILES={'apariciones-conceptuales.jsonl':'aparicion_conceptual','conceptos.jsonl':'concepto','definiciones.jsonl':'definicion','afirmaciones-candidatas.jsonl':'afirmacion','formulas-candidatas.jsonl':'formula','relaciones-explicitas.jsonl':'relacion_explicita','distinciones.jsonl':'distincion','negaciones.jsonl':'negacion','excepciones.jsonl':'excepcion','restricciones-alcance.jsonl':'restriccion_alcance'}
COUNTS={'apariciones-conceptuales.jsonl':2575,'conceptos.jsonl':21,'definiciones.jsonl':60,'afirmaciones-candidatas.jsonl':333,'formulas-candidatas.jsonl':21,'relaciones-explicitas.jsonl':83,'distinciones.jsonl':233,'negaciones.jsonl':1346,'excepciones.jsonl':1,'restricciones-alcance.jsonl':16};TOTAL=sum(COUNTS.values())
def load(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def dump(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
def val(schema,name):return Draft202012Validator({'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':f'#/$defs/{name}'})
def run(*,input_root=INPUT,output_root=OUTPUT,fuentes=FUENTES,unidades=UNIDADES,code=0):
 r=subprocess.run([sys.executable,str(MOTOR),'--repo-root',str(ROOT),'--fuentes',str(fuentes),'--unidades',str(unidades),'--input-root',str(input_root),'--output-root',str(output_root)],cwd=ROOT,text=True,capture_output=True);assert r.returncode==code,(r.returncode,r.stdout,r.stderr);return r
def status(root,fn,rid):return next(r['estado_verificacion'] for r in load(root/fn) if r['id']==rid)
def copy_inputs(dst):dst.mkdir(parents=True,exist_ok=True);[shutil.copy2(INPUT/fn,dst/fn) for fn in FILES]
def main():
 schema=json.loads(SCHEMA.read_text(encoding='utf-8'));validators={fn:val(schema,k) for fn,k in FILES.items()};result=run();assert '"fallidos": 0' in result.stdout and f'"verificados": {TOTAL}' in result.stdout
 snap={};total=0
 for fn,count in COUNTS.items():
  before=load(INPUT/fn);after=load(OUTPUT/fn);assert len(before)==len(after)==count;total+=count;snap[fn]=(OUTPUT/fn).read_bytes()
  for a,b in zip(before,after):
   errors=list(validators[fn].iter_errors(b));assert not errors,f"{b['id']}: {errors[0].message}";changed={k for k in set(a)|set(b) if a.get(k)!=b.get(k)};assert changed=={'estado_verificacion'};assert (a['estado_verificacion'],b['estado_verificacion'])==('pendiente','verificado')
 assert total==TOTAL==4689;run();
 for fn,b in snap.items():assert (OUTPUT/fn).read_bytes()==b,f'No reproducible: {fn}'
 with tempfile.TemporaryDirectory() as td:
  td=Path(td);src=load(FUENTES)
  for r in src:
   if r['id']=='AA-SP-V1':r['sha256']='0'*64;r['version_fuente']='sha256:'+'0'*64
  bad=td/'fuentes.jsonl';dump(bad,src);out=td/'hash';run(output_root=out,fuentes=bad,code=2);assert all(r['estado_verificacion']=='fallido' for fn in FILES for r in load(out/fn))
  formula=load(INPUT/'formulas-candidatas.jsonl')[0];units=load(UNIDADES)
  for r in units:
   if r['id']==formula['unidad_id']:r['sha256_texto']='0'*64
  badu=td/'unidades.jsonl';dump(badu,units);out=td/'unit';run(output_root=out,unidades=badu,code=2);assert status(out,'formulas-candidatas.jsonl',formula['id'])=='fallido'
  mut=td/'text';copy_inputs(mut);rows=load(mut/'formulas-candidatas.jsonl');rid=rows[0]['id'];rows[0]['formula_literal']+=' X';rows[0]['texto_literal']=rows[0]['formula_literal'];dump(mut/'formulas-candidatas.jsonl',rows);out=td/'textout';run(input_root=mut,output_root=out,code=2);assert status(out,'formulas-candidatas.jsonl',rid)=='fallido'
  mut=td/'range';copy_inputs(mut);rows=load(mut/'definiciones.jsonl');rid=rows[0]['id'];rows[0]['localizacion']['linea_fin']=999999;dump(mut/'definiciones.jsonl',rows);out=td/'rangeout';run(input_root=mut,output_root=out,code=2);assert status(out,'definiciones.jsonl',rid)=='fallido'
  mut=td/'ref';copy_inputs(mut);rows=load(mut/'relaciones-explicitas.jsonl');rid=rows[0]['id'];rows[0]['objeto_ref']='CON-INEXISTENTE';dump(mut/'relaciones-explicitas.jsonl',rows);out=td/'refout';run(input_root=mut,output_root=out,code=2);assert status(out,'relaciones-explicitas.jsonl',rid)=='fallido'
  mut=td/'version';copy_inputs(mut);rows=load(mut/'negaciones.jsonl');rid=rows[0]['id'];rows[0]['producido_por']['version']='9.9.9';dump(mut/'negaciones.jsonl',rows);out=td/'verout';run(input_root=mut,output_root=out,code=2);assert status(out,'negaciones.jsonl',rid)=='fallido'
 run();print('OK Fase 6: 4689 registros verificados; 0 fallidos; solo cambia estado_verificacion; hash, unidad, literal, rango, referencias y versiones corruptas fallan expresamente.');return 0
if __name__=='__main__':raise SystemExit(main())
