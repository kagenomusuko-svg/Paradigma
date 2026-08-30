#!/usr/bin/env python3
"""Regresión sintética de 4C/4E genéricos de Fase 10."""
from __future__ import annotations
import importlib.util,json,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent

def mod(name,file):
 s=importlib.util.spec_from_file_location(name,HERE/file);assert s and s.loader
 m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main()->int:
 a=mod('a','afirmaciones_compuesto_fase10.py');r=mod('r','relaciones_compuesto_fase10.py')
 with tempfile.TemporaryDirectory() as td:
  p=Path(td);u=p/'u';c=p/'c';ao=p/'ao';ac=p/'ac';ro=p/'ro';rc=p/'rc'
  units=[{'id':'U','fuente_id':'O','archivo':'x.md','tipo_estructural':'parrafo','texto_literal':'La voluntad produce el acto. Si la autonomía condiciona el acto, cambia la orientación.','localizacion':{'linea_inicio':1,'linea_fin':1}}]
  concepts=[
   {'id':'C1','designacion_operativa':'voluntad','estado_identidad_conceptual':'establecida_por_evidencia'},
   {'id':'C2','designacion_operativa':'acto','estado_identidad_conceptual':'establecida_por_evidencia'},
   {'id':'C3','designacion_operativa':'autonomía','estado_identidad_conceptual':'no_determinada'},
   {'id':'C4','designacion_operativa':'orientación','estado_identidad_conceptual':'no_determinada'},]
  u.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units),encoding='utf-8');c.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in concepts),encoding='utf-8')
  a.run(obra_id='O',unidades=u,conceptos=c,salida=ao,cobertura=ac);ars=[json.loads(x) for x in ao.read_text().splitlines()]
  assert len(ars)==2;assert {'C1','C2'}==set(ars[0]['concepto_ids']);assert ars[1]['estatus_enunciativo']=='formulacion_condicional';assert all(x['estado_extraccion']=='candidato' for x in ars)
  r.run(obra_id='O',unidades=u,conceptos=c,salida=ro,cobertura=rc);rr=[json.loads(x) for x in ro.read_text().splitlines()]
  assert any(x['clasificacion_relacion']=='relacion_explicita' and x['sujeto_ref']=='C1' and x['objeto_ref']=='C2' for x in rr)
  assert any(x['clasificacion_relacion']=='relacion_candidata' and x['sujeto_ref']=='C3' and x['objeto_ref']=='C2' for x in rr)
 print('OK Fase 10 4C/4E: referencias literales y relaciones sin coaparición inferida');return 0
if __name__=='__main__':raise SystemExit(main())
