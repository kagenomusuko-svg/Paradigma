#!/usr/bin/env python3
"""Control epistemológico específico de identidad conceptual para Fase 10.

Se ejecuta después de la verificación mecánica de Fase 6 y antes de auditoría.
No reclasifica registros ni interpreta el corpus: únicamente impide que una
identidad marcada como establecida continúe por la cadena si su evidencia no es
una aparición verificada de la misma obra con un criterio declarativo autorizado.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path

VERSION='1.0.0'
GLOSSARY_CRITERION='lema_en_glosario_tecnico_explicito'
BODY_PREFIX='declaracion_designativa_explicita_en_cuerpo:'


def load(path:Path)->list[dict]:
    if not path.is_file():
        raise AssertionError(f'Insumo inexistente: {path}')
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x]


def declarative(app:dict)->bool:
    criterion=app.get('criterio_deteccion','')
    return criterion==GLOSSARY_CRITERION or criterion.startswith(BODY_PREFIX)


def validate_rows(*,obra_id:str,conceptos:list[dict],apariciones:list[dict])->dict:
    apps={a['id']:a for a in apariciones}
    if len(apps)!=len(apariciones):
        raise AssertionError('Apariciones conceptuales con ID duplicado')
    checked=0; established=0
    for concept in conceptos:
        cid=concept.get('id'); state=concept.get('estado_identidad_conceptual')
        aids=concept.get('aparicion_ids',[]); evidence=concept.get('evidencia_identidad_ids',[])
        if not cid or not aids:
            raise AssertionError(f'Concepto sin identidad/apariciones: {cid}')
        if any(a not in apps or apps[a].get('concepto_id')!=cid for a in aids):
            raise AssertionError(f'Aparición conceptual rota: {cid}')
        if state=='establecida_por_evidencia':
            established+=1
            if concept.get('estado_extraccion')!='extraido' or concept.get('estado_verificacion')!='verificado':
                raise AssertionError(f'Identidad establecida no sellada: {cid}')
            if not evidence or any(a not in aids for a in evidence):
                raise AssertionError(f'Identidad establecida sin evidencia enlazada: {cid}')
            for aid in evidence:
                app=apps[aid]
                if app.get('estado_extraccion')!='extraido' or app.get('estado_verificacion')!='verificado':
                    raise AssertionError(f'Evidencia de identidad no sellada: {cid}/{aid}')
                if app.get('fuente_id')!=obra_id or not app.get('unidad_id'):
                    raise AssertionError(f'Evidencia de identidad fuera de obra o sin unidad: {cid}/{aid}')
                if not app.get('texto_literal') or not app.get('forma_literal'):
                    raise AssertionError(f'Evidencia de identidad sin literal: {cid}/{aid}')
                if not declarative(app):
                    raise AssertionError(f'Evidencia de identidad no declarativa: {cid}/{aid}')
        elif state=='no_determinada':
            if concept.get('estado_extraccion')!='candidato' or evidence:
                raise AssertionError(f'Concepto no determinado sobreclasificado: {cid}')
        else:
            raise AssertionError(f'Estado de identidad no autorizado: {cid}/{state}')
        checked+=1
    return {'version':VERSION,'obra_id':obra_id,'conceptos_revisados':checked,'identidades_establecidas':established}


def run(*,obra_id:str,conceptos:Path,apariciones:Path)->dict:
    return validate_rows(obra_id=obra_id,conceptos=load(conceptos),apariciones=load(apariciones))


def main()->int:
    p=argparse.ArgumentParser();p.add_argument('--obra-id',required=True);p.add_argument('--conceptos',type=Path,required=True);p.add_argument('--apariciones',type=Path,required=True);a=p.parse_args()
    print(json.dumps(run(obra_id=a.obra_id,conceptos=a.conceptos,apariciones=a.apariciones),ensure_ascii=False,sort_keys=True));return 0

if __name__=='__main__':raise SystemExit(main())
