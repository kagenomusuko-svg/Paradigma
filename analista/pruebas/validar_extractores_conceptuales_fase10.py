#!/usr/bin/env python3
"""Regresión sintética de 4A/4B genéricos de Fase 10."""
from __future__ import annotations
import importlib.util, json, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MOTORS=Path(__file__).resolve().parent

def module(name,path):
    s=importlib.util.spec_from_file_location(name,path); assert s and s.loader
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def main()->int:
    c=module('c',MOTORS/'conceptos_compuesto_fase10.py'); d=module('d',MOTORS/'definiciones_compuesto_fase10.py')
    with tempfile.TemporaryDirectory() as td:
        r=Path(td); c.ROOT=r; c.g.ROOT=r; d.ROOT=r
        gl='corpus/libros/x/99-glosario.md'; gp=r/gl; gp.parent.mkdir(parents=True)
        gp.write_text('## Glosario\n\nPrimera mediación\nDefinición literal.\n→ referencia\n',encoding='utf-8')
        units=[
          {'id':'U1','fuente_id':'O','archivo':gl,'tipo_estructural':'parrafo','texto_literal':'Primera mediación','localizacion':{'linea_inicio':3,'linea_fin':3},'orden_textual':0},
          {'id':'U1D','fuente_id':'O','archivo':gl,'tipo_estructural':'parrafo','texto_literal':'Definición literal.','localizacion':{'linea_inicio':4,'linea_fin':4},'orden_textual':1},
          {'id':'U2','fuente_id':'O','archivo':'c1.md','tipo_estructural':'parrafo','texto_literal':'La primera mediación actúa. Voluntad es una orientación.','localizacion':{'linea_inicio':1,'linea_fin':1},'orden_textual':1},
          {'id':'U3','fuente_id':'O','archivo':'c2.md','tipo_estructural':'parrafo','texto_literal':'Voluntad reaparece. Autonomía se define como capacidad propia.','localizacion':{'linea_inicio':1,'linea_fin':1},'orden_textual':2},
          {'id':'U4','fuente_id':'O','archivo':'c3.md','tipo_estructural':'parrafo','texto_literal':'Autonomía reaparece.','localizacion':{'linea_inicio':1,'linea_fin':1},'orden_textual':3},
        ]
        src=r/'s.jsonl'; uni=r/'u.jsonl'; apps=r/'a.jsonl'; cons=r/'c.jsonl'; ccov=r/'ccov.jsonl'; defs=r/'d.jsonl'; dcov=r/'dcov.jsonl'
        src.write_text(json.dumps({'id':'O','rutas_derivadas':[gl]},ensure_ascii=False)+'\n',encoding='utf-8')
        uni.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units),encoding='utf-8')
        cr=c.run(obra_id='O',fuentes=src,unidades=uni,apariciones=apps,conceptos=cons,cobertura=ccov)
        concepts=[json.loads(x) for x in cons.read_text(encoding='utf-8').splitlines()]
        assert cr['conceptos_confirmados']==1
        assert any(x['designacion_operativa']=='Primera mediación' and x['estado_identidad_conceptual']=='establecida_por_evidencia' for x in concepts)
        assert any(c.g.norm(x['designacion_operativa'])=='voluntad' and x['estado_identidad_conceptual']=='no_determinada' for x in concepts)
        assert all(x['producido_por']=={'motor':'conceptos_apariciones','version':'1.2.0'} for x in concepts)
        d.run(obra_id='O',fuentes=src,unidades=uni,conceptos=cons,salida=defs,cobertura=dcov)
        definitions=[json.loads(x) for x in defs.read_text(encoding='utf-8').splitlines()]
        assert any(x['clasificacion_definicion']=='definicion_candidata' and 'Voluntad es' in x['texto_literal'] for x in definitions)
        assert any(x['clasificacion_definicion']=='definicion_explicita' and 'Autonomía se define como' in x['texto_literal'] for x in definitions)
        assert all(x['producido_por']=={'motor':'definiciones','version':'1.2.0'} for x in definitions)
    print('OK Fase 10 4A/4B: candidatos auditables + identidad solo por evidencia')
    return 0
if __name__=='__main__':raise SystemExit(main())
