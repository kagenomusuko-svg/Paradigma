#!/usr/bin/env python3
"""Regresión sintética de identidad conceptual intraobra de Fase 10.

Fija la frontera epistemológica de 4A: una declaración inequívoca del cuerpo o
un lema del glosario propio puede aportar evidencia; recurrencia, semejanza y
estructuras ambiguas solo producen candidatos no determinados.
"""
from __future__ import annotations
import importlib.util, json, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MOTORS=ROOT/'analista/motores'


def module(name,path):
    s=importlib.util.spec_from_file_location(name,path); assert s and s.loader
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def rows(path:Path)->list[dict]:
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x]


def unit(uid:str,text:str,order:int,archivo:str='cuerpo.md',line:int=1)->dict:
    return {'id':uid,'fuente_id':'O','archivo':archivo,'tipo_estructural':'parrafo','texto_literal':text,
            'localizacion':{'linea_inicio':line,'linea_fin':line+text.count('\n')},'orden_textual':order}


def run_case(c,root:Path,units:list[dict],routes:list[str]):
    src=root/'s.jsonl'; uni=root/'u.jsonl'; apps=root/'a.jsonl'; cons=root/'c.jsonl'; cov=root/'cov.jsonl'
    src.write_text(json.dumps({'id':'O','rutas_derivadas':routes},ensure_ascii=False)+'\n',encoding='utf-8')
    uni.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units),encoding='utf-8')
    result=c.run(obra_id='O',fuentes=src,unidades=uni,apariciones=apps,conceptos=cons,cobertura=cov)
    return result,rows(apps),rows(cons),{u['id']:u for u in units}


def concept(c,concepts:list[dict],name:str)->dict:
    matches=[x for x in concepts if c.g.norm(x['designacion_operativa'])==c.g.norm(name)]
    assert len(matches)==1,(name,[x['designacion_operativa'] for x in concepts])
    return matches[0]


def assert_identity_evidence(c,concept_row:dict,apps:list[dict],units:dict[str,dict],criterion_prefix:str):
    assert concept_row['estado_identidad_conceptual']=='establecida_por_evidencia'
    assert concept_row['estado_extraccion']=='extraido'
    evidence=concept_row['evidencia_identidad_ids']; assert evidence
    by_id={x['id']:x for x in apps}
    for aid in evidence:
        app=by_id[aid]
        assert app['concepto_id']==concept_row['id']
        assert app['fuente_id']=='O'
        assert app['unidad_id'] in units
        assert app['texto_literal']==app['forma_literal']==concept_row['designacion_operativa']
        assert app['criterio_deteccion'].startswith(criterion_prefix)
        source_text=units[app['unidad_id']]['texto_literal']
        assert app['texto_literal'] in source_text
        assert app['localizacion']['ruta']==units[app['unidad_id']]['archivo']


def main()->int:
    c=module('c',MOTORS/'conceptos_compuesto_fase10.py')
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); c.ROOT=root; c.g.ROOT=root

        # Positivo sin glosario: la declaración misma establece la designación.
        units=[unit('P1','Definimos voluntad operativa como la orientación descrita aquí.',0)]
        result,apps,concepts,unit_map=run_case(c,root,units,[])
        target=concept(c,concepts,'voluntad operativa')
        assert result['conceptos_confirmados_cuerpo']==1
        assert_identity_evidence(c,target,apps,unit_map,'declaracion_designativa_explicita_en_cuerpo:definimos_como')
        evidence_app=next(x for x in apps if x['id'] in target['evidencia_identidad_ids'])
        assert evidence_app['unidad_id']=='P1' and evidence_app['fuente_id']=='O'
        assert unit_map['P1']['texto_literal']=='Definimos voluntad operativa como la orientación descrita aquí.'

        # Negativo por recurrencia: repetir una forma no establece identidad.
        units=[unit('R1','Voluntad aparece en este pasaje.',0),unit('R2','Voluntad reaparece después.',1)]
        _,apps,concepts,_=run_case(c,root,units,[])
        repeated=concept(c,concepts,'Voluntad')
        assert repeated['estado_identidad_conceptual']=='no_determinada'
        assert repeated['evidencia_identidad_ids']==[]
        assert all('declaracion_designativa_explicita_en_cuerpo' not in x['criterio_deteccion'] for x in apps if x.get('concepto_id')==repeated['id'])

        # Negativo por semejanza: dos expresiones formalmente distintas no se fusionan.
        units=[unit('S1','Autonomía aparece aquí. Autonomía moral aparece aquí.',0),unit('S2','Autonomía reaparece. Autonomía moral reaparece.',1)]
        _,_,concepts,_=run_case(c,root,units,[])
        a=concept(c,concepts,'Autonomía'); am=concept(c,concepts,'Autonomía moral')
        assert a['id']!=am['id']
        assert a['estado_identidad_conceptual']==am['estado_identidad_conceptual']=='no_determinada'
        assert a['evidencia_identidad_ids']==am['evidencia_identidad_ids']==[]

        # Ambiguo: el patrón existe, pero el contexto condicional impide el ascenso.
        units=[unit('A1','Si definimos umbral operativo como una frontera, la hipótesis cambia.',0)]
        _,apps,concepts,_=run_case(c,root,units,[])
        ambiguous=concept(c,concepts,'umbral operativo')
        assert ambiguous['estado_identidad_conceptual']=='no_determinada'
        assert ambiguous['evidencia_identidad_ids']==[]
        assert any('marcador_definicional_formal' in x['criterio_deteccion'] for x in apps if x.get('concepto_id')==ambiguous['id'])
        assert all('declaracion_designativa_explicita_en_cuerpo' not in x['criterio_deteccion'] for x in apps if x.get('concepto_id')==ambiguous['id'])

        # Glosario: conserva la ruta ya validada y la evidencia pertenece a la misma obra.
        gl='corpus/libros/x/99-glosario.md'; gp=root/gl; gp.parent.mkdir(parents=True,exist_ok=True)
        gp.write_text('## Glosario\n\nPrimera mediación\nDefinición literal.\n→ referencia\n',encoding='utf-8')
        units=[unit('G1','Primera mediación',0,gl,3),unit('G2','Definición literal.',1,gl,4)]
        result,apps,concepts,unit_map=run_case(c,root,units,[gl])
        glossary=concept(c,concepts,'Primera mediación')
        assert result['conceptos_confirmados_glosario']==1
        assert_identity_evidence(c,glossary,apps,unit_map,'lema_en_glosario_tecnico_explicito')

        assert all(x['producido_por']=={'motor':'conceptos_apariciones','version':'1.3.0'} for x in concepts+apps)

    print('OK Fase 10 4A: identidad solo por evidencia explícita intraobra; recurrencia, semejanza y ambigüedad no ascienden')
    return 0
if __name__=='__main__': raise SystemExit(main())
