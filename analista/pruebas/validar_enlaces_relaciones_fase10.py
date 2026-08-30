#!/usr/bin/env python3
"""Regresión sintética de 4C/4E de Fase 10."""
from __future__ import annotations
import importlib.util,json,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; MOTORS=ROOT/'analista/motores'

def mod(name,file):
 s=importlib.util.spec_from_file_location(name,MOTORS/file);assert s and s.loader
 m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main()->int:
 a=mod('a','afirmaciones_compuesto_fase10.py');r=mod('r','relaciones_compuesto_fase10.py')
 with tempfile.TemporaryDirectory() as td:
  p=Path(td);u=p/'u';c=p/'c';ao=p/'ao';ac=p/'ac';ro=p/'ro';rc=p/'rc'
  units=[{'id':'U','fuente_id':'O','archivo':'x.md','tipo_estructural':'parrafo','texto_literal':'La voluntad produce el acto. Si la voluntad produce el acto, cambia la orientación. La voluntad no produce el acto. ¿La voluntad produce el acto?','localizacion':{'linea_inicio':1,'linea_fin':1}}]
  concepts=[
   {'id':'C1','designacion_operativa':'voluntad','estado_identidad_conceptual':'establecida_por_evidencia'},
   {'id':'C2','designacion_operativa':'acto','estado_identidad_conceptual':'establecida_por_evidencia'},
   {'id':'C3','designacion_operativa':'orientación','estado_identidad_conceptual':'no_determinada'}]
  u.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units),encoding='utf-8');c.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in concepts),encoding='utf-8')
  a.run(obra_id='O',unidades=u,conceptos=c,salida=ao,cobertura=ac);ars=[json.loads(x) for x in ao.read_text().splitlines()]
  assert ars and all(x['estado_extraccion']=='candidato' for x in ars)
  assert any(x['estatus_enunciativo']=='formulacion_condicional' for x in ars)
  r.run(obra_id='O',unidades=u,conceptos=c,salida=ro,cobertura=rc);rr=[json.loads(x) for x in ro.read_text().splitlines()]
  assert any(x['clasificacion_relacion']=='relacion_explicita' and x['texto_literal']=='La voluntad produce el acto.' for x in rr)
  conditional=[x for x in rr if x['texto_literal'].startswith('Si la voluntad produce')]; assert conditional and all(x['clasificacion_relacion']=='relacion_candidata' for x in conditional)
  negated=[x for x in rr if 'no produce' in x['texto_literal']]; assert negated and all(x['clasificacion_relacion']=='relacion_candidata' for x in negated)
  questioned=[x for x in rr if '?' in x['texto_literal']]; assert questioned and all(x['clasificacion_relacion']=='relacion_candidata' for x in questioned)
  assert all(x['producido_por']=={'motor':'relaciones_explicitas','version':'1.3.0'} for x in rr)
 print('OK Fase 10 4C/4E: relación explícita exige contexto asertivo; condicional, negación y pregunta quedan candidatas');return 0
if __name__=='__main__':raise SystemExit(main())
