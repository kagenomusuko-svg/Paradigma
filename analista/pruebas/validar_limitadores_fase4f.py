#!/usr/bin/env python3
"""Valida 4F v1.1 sobre el producto real completo del piloto."""
from __future__ import annotations
import copy,json,subprocess,sys
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[2]
SCHEMA=ROOT/'analista/esquema/contratos-v1.0.0.schema.json'; UNITS=ROOT/'analista/generado/unidades.jsonl'; MOTOR=ROOT/'analista/motores/limitadores.py'; OUT=ROOT/'analista/generado'
FILES={'distinciones.jsonl':('distincion',233),'negaciones.jsonl':('negacion',1346),'excepciones.jsonl':('excepcion',1),'restricciones-alcance.jsonl':('restriccion_alcance',16)}
COVERAGE=OUT/'cobertura-limitadores.jsonl'; PILOTO='AA-SP-V1'

def load(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def validator(schema,name): return Draft202012Validator({'$schema':schema['$schema'],'$defs':schema['$defs'],'$ref':f'#/$defs/{name}'})
def occurrences(unit,literal):
 t=unit['texto_literal'];base=unit['localizacion']['linea_inicio'];out=[];start=0
 while True:
  pos=t.find(literal,start)
  if pos<0:break
  ls=base+t[:pos].count('\n');out.append((ls,ls+literal.count('\n')));start=pos+1
 return out
def main():
 schema=json.loads(SCHEMA.read_text(encoding='utf-8'));units={u['id']:u for u in load(UNITS) if u.get('fuente_id')==PILOTO};assert len(units)==836
 snapshots={};seen=set();total=0
 for fn,(kind,count) in FILES.items():
  rows=load(OUT/fn);assert len(rows)==count,(fn,len(rows),count);snapshots[fn]=(OUT/fn).read_bytes();v=validator(schema,kind)
  for r in rows:
   errors=list(v.iter_errors(r));assert not errors,f"{r.get('id')}: {errors[0].message}"
   assert r['id'] not in seen;seen.add(r['id']);total+=1;assert r['producido_por']=={'motor':'limitadores','version':'1.1.1'}
   assert r['unidad_id'] in units and r['fuente_id']==PILOTO;u=units[r['unidad_id']];loc=r['localizacion'];assert loc['ruta']==u['archivo'];assert (loc['linea_inicio'],loc['linea_fin']) in occurrences(u,r['texto_literal'])
   assert r['estatus_enunciativo']=='no_determinado' and r['estado_verificacion']=='pendiente' and r['estado_auditoria']=='pendiente'
   cls=r.get('clasificacion_distincion') or r.get('clasificacion_negacion') or r.get('clasificacion_excepcion') or r.get('clasificacion_restriccion');assert cls
   if cls.endswith('_explicita'):assert r['estado_extraccion']=='extraido'
   else:assert cls.endswith('_candidata') and r['estado_extraccion']=='candidato'
   if kind=='distincion':
    assert r['marcador_literal']=='sino' and r['termino_a_literal'] in r['texto_literal'] and r['termino_b_literal'] in r['texto_literal']
   elif kind=='negacion':
    assert r['objeto_negado_literal']==r['texto_literal'];assert not r['texto_literal'].casefold().startswith(('no solo ','no sólo '))
   elif kind=='excepcion':
    assert r['fragmento_exceptivo_literal']==r['texto_literal'] and r['afirmacion_limitada_id'] is None
   else:
    assert r['fragmento_restriccion_literal']==r['texto_literal'] and r['afirmacion_limitada_id'] is None and r['tipo_restriccion']=='no_determinada'
  forbidden=copy.deepcopy(rows[0]);forbidden['solucion_doctrinal']='X';assert not v.is_valid(forbidden)
 assert total==1596 and len(seen)==1596
 coverage=load(COVERAGE);assert len(coverage)==1;cv=validator(schema,'reporte_cobertura');assert cv.is_valid(coverage[0]);c=coverage[0];assert c['version_motor']=='1.1.1' and c['unidades_totales']==c['unidades_procesadas']==836 and c['unidades_omitidas']==[] and c['errores']==[]
 snapshots[COVERAGE.name]=COVERAGE.read_bytes();subprocess.run([sys.executable,str(MOTOR)],cwd=ROOT,check=True)
 for fn,content in snapshots.items():assert (OUT/fn).read_bytes()==content,f'Salida no reproducible: {fn}'
 print('OK Fase 4F v1.1: 233 distinciones, 1346 negaciones, 1 excepción y 16 restricciones; 836/836 unidades; 1596 IDs únicos; literalidad, fuerza y reproducibilidad verificadas; 0 vínculos de afirmación inferidos.')
 return 0
if __name__=='__main__':raise SystemExit(main())
