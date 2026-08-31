#!/usr/bin/env python3
"""Regresión del control específico de identidad conceptual de Fase 10."""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def mod():
    p=ROOT/'analista/motores/validador_identidad_fase10.py';s=importlib.util.spec_from_file_location('v',p);assert s and s.loader
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def app(aid,criterion,source='O'):
    return {'id':aid,'concepto_id':'C','fuente_id':source,'unidad_id':'U','texto_literal':'voluntad operativa','forma_literal':'voluntad operativa',
            'estado_extraccion':'extraido','estado_verificacion':'verificado','criterio_deteccion':criterion}

def concept(state='establecida_por_evidencia',evidence=None):
    return {'id':'C','aparicion_ids':['A'],'evidencia_identidad_ids':['A'] if evidence is None else evidence,
            'estado_identidad_conceptual':state,'estado_extraccion':'extraido' if state=='establecida_por_evidencia' else 'candidato','estado_verificacion':'verificado'}

def must_fail(v,c,a,fragment):
    try:v.validate_rows(obra_id='O',conceptos=[c],apariciones=[a])
    except AssertionError as e:assert fragment in str(e),(fragment,str(e))
    else:raise AssertionError(f'Debió fallar: {fragment}')

def main()->int:
    v=mod()
    body=v.validate_rows(obra_id='O',conceptos=[concept()],apariciones=[app('A','declaracion_designativa_explicita_en_cuerpo:definimos_como')])
    assert body['identidades_establecidas']==1
    gloss=v.validate_rows(obra_id='O',conceptos=[concept()],apariciones=[app('A','lema_en_glosario_tecnico_explicito')])
    assert gloss['identidades_establecidas']==1
    candidate=concept(state='no_determinada',evidence=[]);ok=v.validate_rows(obra_id='O',conceptos=[candidate],apariciones=[app('A','recurrencia_literal_intraobra')])
    assert ok['identidades_establecidas']==0
    must_fail(v,concept(),app('A','recurrencia_literal_intraobra; identidad_conceptual_no_determinada'),'no declarativa')
    must_fail(v,concept(),app('A','declaracion_designativa_explicita_en_cuerpo:definimos_como',source='OTRA'),'fuera de obra')
    c=concept(state='no_determinada',evidence=['A']);must_fail(v,c,app('A','recurrencia_literal_intraobra'),'sobreclasificado')
    print('OK Fase 10 identidad: el sellado mecánico no basta; la evidencia debe ser declarativa y de la misma obra')
    return 0
if __name__=='__main__':raise SystemExit(main())
