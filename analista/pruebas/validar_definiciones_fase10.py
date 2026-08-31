#!/usr/bin/env python3
"""Regresión sintética de 4B de Fase 10.

Una forma definicional fuerte solo asciende a definición explícita cuando el
contexto es inequívocamente asertivo. Preguntas, condicionales, negaciones,
citas y discurso referido permanecen candidatos.
"""
from __future__ import annotations
import importlib.util, json, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; MOTORS=ROOT/'analista/motores'

def mod(name,file):
    s=importlib.util.spec_from_file_location(name,MOTORS/file); assert s and s.loader
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def unit(uid,text,line):
    return {'id':uid,'fuente_id':'O','archivo':'cuerpo.md','tipo_estructural':'parrafo','texto_literal':text,
            'localizacion':{'linea_inicio':line,'linea_fin':line},'orden_textual':line}

def main()->int:
    d=mod('d','definiciones_compuesto_fase10.py')
    with tempfile.TemporaryDirectory() as td:
        p=Path(td); src=p/'s'; uni=p/'u'; con=p/'c'; out=p/'o'; cov=p/'cov'
        units=[
            unit('U1','Definimos voluntad operativa como una orientación del acto.',1),
            unit('U2','Si definimos voluntad operativa como una orientación, cambia la hipótesis.',2),
            unit('U3','¿Definimos voluntad operativa como una orientación?',3),
            unit('U4','No definimos voluntad operativa como una orientación.',4),
            unit('U5','«Definimos voluntad operativa como una orientación.»',5),
            unit('U6','Según Elena, definimos voluntad operativa como una orientación.',6),
            unit('U7','Voluntad operativa no significa obediencia.',7),
        ]
        concepts=[{'id':'C1','designacion_operativa':'voluntad operativa','estado_identidad_conceptual':'establecida_por_evidencia'}]
        src.write_text(json.dumps({'id':'O','rutas_derivadas':[]},ensure_ascii=False)+'\n',encoding='utf-8')
        uni.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units),encoding='utf-8')
        original=''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in concepts)
        con.write_text(original,encoding='utf-8')
        result=d.run(obra_id='O',fuentes=src,unidades=uni,conceptos=con,salida=out,cobertura=cov)
        rows=[json.loads(x) for x in out.read_text(encoding='utf-8').splitlines() if x]
        assert result['version']=='1.3.0'
        assert con.read_text(encoding='utf-8')==original, '4B no debe mutar identidad conceptual'
        by_unit={r['unidad_id']:r for r in rows}
        positive=by_unit['U1']
        assert positive['clasificacion_definicion']=='definicion_explicita'
        assert positive['estado_extraccion']=='extraido' and positive['estatus_enunciativo']=='definicion'
        assert positive['criterio_deteccion']=='estructura_definicional_fuerte_prenominal'
        expected={
            'U2':'formulacion_condicional',
            'U3':'pregunta',
            'U4':'negacion_autoral',
            'U5':'cita',
            'U6':'discurso_referido',
            'U7':'negacion_autoral',
        }
        for uid,status in expected.items():
            row=by_unit[uid]
            assert row['clasificacion_definicion']=='definicion_candidata',(uid,row)
            assert row['estado_extraccion']=='candidato'
            assert row['estatus_enunciativo']==status,(uid,row['estatus_enunciativo'])
            assert f'contexto_no_autoriza_definicion_explicita:{status}' in row['criterio_deteccion']
            source=next(x for x in units if x['id']==uid)
            assert row['fuente_id']=='O' and row['unidad_id']==uid
            assert row['texto_literal']==source['texto_literal']
            assert row['localizacion']['ruta']=='cuerpo.md'
            assert row['concepto_id']=='C1'
        assert all(r['producido_por']=={'motor':'definiciones','version':'1.3.0'} for r in rows)
    print('OK Fase 10 4B: forma definicional fuerte solo asciende en contexto asertivo inequívoco')
    return 0
if __name__=='__main__': raise SystemExit(main())
