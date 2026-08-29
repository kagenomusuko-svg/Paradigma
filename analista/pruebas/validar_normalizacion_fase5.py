#!/usr/bin/env python3
"""Valida que Fase 5 solo añada normalización de recuperación a productos reales."""
from __future__ import annotations
import json,re,subprocess,sys,unicodedata
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2];SCHEMA=ROOT/'analista/esquema/contratos-v1.0.0.schema.json';INPUT=ROOT/'analista/generado';OUTPUT=INPUT/'normalizados';MOTOR=ROOT/'analista/motores/normalizacion.py'
FILES={'apariciones-conceptuales.jsonl':('aparicion_conceptual',2575),'conceptos.jsonl':('concepto',21),'definiciones.jsonl':('definicion',60),'afirmaciones-candidatas.jsonl':('afirmacion',333),'formulas-candidatas.jsonl':('formula',21),'relaciones-explicitas.jsonl':('relacion_explicita',83),'distinciones.jsonl':('distincion',233),'negaciones.jsonl':('negacion',1346),'excepciones.jsonl':('excepcion',1),'restricciones-alcance.jsonl':('restriccion_alcance',16)};TOTAL=sum(n for _,n in FILES.values());SPACE=re.compile(r'\s+');DASH=re.compile(r'\s*-\s*');TRANS=str.maketrans({'‐':'-','‑':'-','‒':'-','–':'-','—':'-','−':'-'})
def load(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def formal(t):return SPACE.sub(' ',unicodedata.normalize('NFKC',t)).strip()
def nodiac(t):return ''.join(c for c in unicodedata.normalize('NFD',t) if unicodedata.category(c)!='Mn')
def variants(t):
 b=formal(t).casefold();g=DASH.sub('-',b.translate(TRANS));out=[]
 for v in (b,nodiac(b),g,nodiac(g)):
  v=SPACE.sub(' ',v).strip()
  if v and v not in out:out.append(v)
 return out
def retrieval(r):return r[{'aparicion_conceptual':'forma_literal','concepto':'designacion_operativa','definicion':'texto_literal','afirmacion':'texto_literal','formula':'formula_literal','relacion_explicita':'relacion_literal','distincion':'texto_literal','negacion':'objeto_negado_literal','excepcion':'fragmento_exceptivo_literal','restriccion_alcance':'fragmento_restriccion_literal'}[r['tipo_registro']]]
def val(schema,name):return Draft202012Validator({'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':f'#/$defs/{name}'})
def main():
 schema=json.loads(SCHEMA.read_text(encoding='utf-8'));total=0;snap={};before_by={};after_by={}
 for fn,(kind,count) in FILES.items():
  before=load(INPUT/fn);after=load(OUTPUT/fn);before_by[fn]=before;after_by[fn]=after;assert len(before)==len(after)==count and [r['id'] for r in before]==[r['id'] for r in after];v=val(schema,kind)
  for a,b in zip(before,after):
   errors=list(v.iter_errors(b));assert not errors,f"{b['id']}: {errors[0].message}";assert set(a)==set(b)
   changed={k for k in a if a[k]!=b[k]};assert changed<= {'normalizacion_formal','normalizacion_lexica'},(fn,a['id'],changed)
   text=retrieval(a);assert b['normalizacion_formal']==formal(text) and b['normalizacion_lexica']==variants(text) and b['normalizacion_lexica']
  total+=count;snap[fn]=(OUTPUT/fn).read_bytes()
 assert total==TOTAL==4689
 c0={r['id']:r for r in before_by['conceptos.jsonl']};c1={r['id']:r for r in after_by['conceptos.jsonl']};assert set(c0)==set(c1) and len(c0)==21
 for cid in c0:
  for field in ('aparicion_ids','estado_identidad_conceptual','evidencia_identidad_ids'):assert c0[cid][field]==c1[cid][field]
 assert [r['concepto_id'] for r in before_by['apariciones-conceptuales.jsonl']]==[r['concepto_id'] for r in after_by['apariciones-conceptuales.jsonl']]
 byname={r['designacion_operativa']:r for r in after_by['conceptos.jsonl']};assert 'pasion' in byname['Pasión']['normalizacion_lexica'];assert 'aego' not in byname['Afasia volitiva']['normalizacion_lexica'];assert 'integral' not in byname['Integral del ego — I(t)']['normalizacion_lexica']
 subprocess.run([sys.executable,str(MOTOR)],cwd=ROOT,check=True)
 for fn,b in snap.items():assert (OUTPUT/fn).read_bytes()==b,f'No reproducible: {fn}'
 print('OK Fase 5: 4689 registros normalizados; IDs, referencias y fuerza preservados; solo normalización formal/léxica de recuperación; 0 fusiones conceptuales.')
 return 0
if __name__=='__main__':raise SystemExit(main())
