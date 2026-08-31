#!/usr/bin/env python3
"""Regresión sintética de 4C/4E de Fase 10."""
from __future__ import annotations
import importlib.util,json,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; MOTORS=ROOT/'analista/motores'

def mod(name,file):
 s=importlib.util.spec_from_file_location(name,MOTORS/file);assert s and s.loader
 m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def unit(uid,text,line):
 return {'id':uid,'fuente_id':'O','archivo':'x.md','tipo_estructural':'parrafo','texto_literal':text,'localizacion':{'linea_inicio':line,'linea_fin':line}}

def main()->int:
 a=mod('a','afirmaciones_compuesto_fase10.py');r=mod('r','relaciones_compuesto_fase10.py');refs=mod('refs_regresion','referencias_conceptuales_fase10.py')

 # Dos designaciones distintas que colapsan a la misma firma mecánica no se
 # fusionan ni se elige una. Permanecen en el expediente conceptual, pero esa
 # firma ambigua queda fuera del índice usado para enlaces downstream.
 ambiguous=[
  {'id':'A1','designacion_operativa':'Colección','estado_identidad_conceptual':'no_determinada'},
  {'id':'A2','designacion_operativa':'Colección:','estado_identidad_conceptual':'no_determinada'},
 ]
 idx,by=refs.build_index(ambiguous)
 assert set(by)=={'A1','A2'}
 assert refs.occurrences('Colección: ejemplo.',idx)==[]

 with tempfile.TemporaryDirectory() as td:
  p=Path(td);u=p/'u';c=p/'c';ao=p/'ao';ac=p/'ac';ro=p/'ro';rc=p/'rc'
  units=[
   unit('U1','La voluntad produce el acto.',1),
   unit('U2','Si la voluntad produce el acto, cambia la orientación.',2),
   unit('U3','La voluntad no produce el acto.',3),
   unit('U4','¿La voluntad produce el acto?',4),
   unit('U5','«La voluntad produce el acto.»',5),
   unit('U6','Según Elena, la voluntad produce el acto.',6),
  ]
  concepts=[
   {'id':'C1','designacion_operativa':'voluntad','estado_identidad_conceptual':'establecida_por_evidencia'},
   {'id':'C2','designacion_operativa':'acto','estado_identidad_conceptual':'establecida_por_evidencia'},
   {'id':'C3','designacion_operativa':'orientación','estado_identidad_conceptual':'no_determinada'}]
  u.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units),encoding='utf-8');c.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in concepts),encoding='utf-8')
  a.run(obra_id='O',unidades=u,conceptos=c,salida=ao,cobertura=ac);ars=[json.loads(x) for x in ao.read_text().splitlines()]
  assert ars and all(x['estado_extraccion']=='candidato' for x in ars)
  by_unit={x['unidad_id']:x for x in ars}
  assert by_unit['U2']['estatus_enunciativo']=='formulacion_condicional'
  assert by_unit['U4']['estatus_enunciativo']=='pregunta'
  assert by_unit['U5']['estatus_enunciativo']=='cita'
  assert by_unit['U6']['estatus_enunciativo']=='discurso_referido'
  r.run(obra_id='O',unidades=u,conceptos=c,salida=ro,cobertura=rc);rr=[json.loads(x) for x in ro.read_text().splitlines()]
  rel_by_unit={x['unidad_id']:x for x in rr if x['sujeto_ref']=='C1' and x['objeto_ref']=='C2'}
  assert rel_by_unit['U1']['clasificacion_relacion']=='relacion_explicita'
  for uid in ('U2','U3','U4','U5','U6'):
   assert rel_by_unit[uid]['clasificacion_relacion']=='relacion_candidata',(uid,rel_by_unit[uid])
   assert rel_by_unit[uid]['estado_extraccion']=='candidato'
   assert rel_by_unit[uid]['fuente_id']=='O' and rel_by_unit[uid]['unidad_id']==uid
   assert rel_by_unit[uid]['texto_literal']==next(x['texto_literal'] for x in units if x['id']==uid)
  assert all(x['producido_por']=={'motor':'relaciones_explicitas','version':'1.2.0'} for x in rr)
 print('OK Fase 10 4C/4E: aserción explícita; firmas ambiguas no se resuelven; contextos no asertivos quedan candidatos');return 0
if __name__=='__main__':raise SystemExit(main())
