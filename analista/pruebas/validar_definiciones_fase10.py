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

    # Marcadores romanos aislados son estructura documental. Si quedan antes de
    # la definición, no la contaminan; si interrumpen una entrada y Fase 3 la
    # divide, ningún fragmento parcial asciende a definición explícita.
    with tempfile.TemporaryDirectory(dir=ROOT/'analista/pruebas') as td:
        gloss=Path(td)/'99-glosario.md'
        gloss.write_text(
            '## Glosario\n\n'
            'Annona\nXXIII\n\nDefinición primera.\nDefinición segunda.\n→ Cap. 1\n'
            'Contrato fiscal\nPrimera parte contractual.\nXXV\n\nSegunda parte contractual.\n→ Cap. 2\n',
            encoding='utf-8',
        )
        rel=gloss.relative_to(ROOT).as_posix()
        gloss_units=[
            {'id':'UG1','fuente_id':'OG','archivo':rel,'tipo_estructural':'parrafo','texto_literal':'Annona\nXXIII','localizacion':{'linea_inicio':3,'linea_fin':4}},
            {'id':'UG2','fuente_id':'OG','archivo':rel,'tipo_estructural':'parrafo','texto_literal':'Definición primera.\nDefinición segunda.\n→ Cap. 1\nContrato fiscal\nPrimera parte contractual.\nXXV','localizacion':{'linea_inicio':6,'linea_fin':11}},
            {'id':'UG3','fuente_id':'OG','archivo':rel,'tipo_estructural':'parrafo','texto_literal':'Segunda parte contractual.\n→ Cap. 2','localizacion':{'linea_inicio':13,'linea_fin':14}},
        ]
        source={'id':'OG','rutas_derivadas':[rel]}
        gloss_concepts=[
            {'id':'CANNONA','designacion_operativa':'Annona','estado_identidad_conceptual':'establecida_por_evidencia'},
            {'id':'CCONTRATO','designacion_operativa':'Contrato fiscal','estado_identidad_conceptual':'establecida_por_evidencia'},
        ]
        gloss_rows=d.glossary_definitions('OG',source,gloss_units,gloss_concepts)
        annona=[r for r in gloss_rows if r['concepto_id']=='CANNONA']
        assert len(annona)==1,annona
        assert annona[0]['unidad_id']=='UG2'
        assert annona[0]['texto_literal']=='Definición primera.\nDefinición segunda.'
        assert annona[0]['clasificacion_definicion']=='definicion_explicita'
        assert annona[0]['localizacion']=={'ruta':rel,'linea_inicio':6,'linea_fin':7}
        assert 'XXIII' not in annona[0]['texto_literal']

        contrato=[r for r in gloss_rows if r['concepto_id']=='CCONTRATO']
        assert len(contrato)==2,contrato
        assert {r['unidad_id'] for r in contrato}=={'UG2','UG3'}
        assert {r['texto_literal'] for r in contrato}=={'Primera parte contractual.','Segunda parte contractual.'}
        assert all(r['clasificacion_definicion']=='definicion_candidata' for r in contrato)
        assert all(r['estado_extraccion']=='candidato' and r['estatus_enunciativo']=='definicion' for r in contrato)
        assert all('entrada_glosario_fragmentada_por_unidades' in r['criterio_deteccion'] for r in contrato)
        assert all('XXV' not in r['texto_literal'] for r in contrato)

    print('OK Fase 10 4B: explícita solo si es inequívoca y mono-unidad; entradas de glosario fragmentadas permanecen candidatas')
    return 0
if __name__=='__main__': raise SystemExit(main())
