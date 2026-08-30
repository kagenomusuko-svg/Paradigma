#!/usr/bin/env python3
"""4E de Fase 10: relaciones textuales intraobra sin coaparición inferencial.

Exige dos designaciones conceptuales literales separadas por un conector
observable. Solo eleva a relación explícita cuando ambos conceptos tienen
identidad establecida por evidencia y el conector pertenece al conjunto fuerte;
en cualquier otro caso conserva el registro como candidato.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];MOTOR="relaciones_explicitas";VERSION="1.2.0";SCHEMA="1.0.0"
HELPER=ROOT/"analista/motores/referencias_conceptuales_fase10.py"
s=importlib.util.spec_from_file_location('refs_rel_f10',HELPER);assert s and s.loader;refs=importlib.util.module_from_spec(s);s.loader.exec_module(refs)
CONNECTORS=[
 (re.compile(r"\b(?:implica|produce|causa|requiere|presupone|incluye|excluye|equivale\s+a|depende\s+de|deriva\s+de|se\s+opone\s+a|se\s+distingue\s+de)\b",re.I),True),
 (re.compile(r"\b(?:es|son|constituye|orienta|determina|limita|afecta|modifica|permite|condiciona)\b",re.I),False),
]
BOUNDARY=re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÜÑ¿¡])")
def sid(prefix,*parts):return f"{prefix}-{hashlib.sha1(chr(31).join(parts).encode()).hexdigest()[:12].upper()}"
def load(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
def dump(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
def line_range(u,text,a,b):x=u['localizacion']['linea_inicio']+text[:a].count('\n');return x,x+text[a:b].count('\n')
def sentences(text):
 out=[];start=0
 for m in BOUNDARY.finditer(text):out.append((start,m.start(),text[start:m.start()]));start=m.end()
 out.append((start,len(text),text[start:]));return [(a,b,x) for a,b,x in out if x.strip()]
def pair_for_connector(occ:list[dict],a:int,b:int):
 left=[x for x in occ if x['fin']<=a];right=[x for x in occ if x['inicio']>=b]
 if not left or not right:return None
 l=max(left,key=lambda x:(x['fin'],x['inicio']));r=min(right,key=lambda x:(x['inicio'],-x['fin']))
 if l['concepto_id']==r['concepto_id']:return None
 return l,r
def run(*,obra_id,unidades,conceptos,salida,cobertura):
 units=[x for x in load(unidades) if x.get('fuente_id')==obra_id];cons=load(conceptos);index,by=refs.build_index(cons)
 if not units:raise SystemExit(f'Sin unidades: {obra_id}')
 rows=[];seen=set()
 for u in units:
  if u.get('tipo_estructural') in {'encabezado','separador'}:continue
  text=u['texto_literal']
  for sa,sb,sentence in sentences(text):
   occ=refs.occurrences(sentence,index)
   if len({x['concepto_id'] for x in occ})<2:continue
   for cre,strong in CONNECTORS:
    for cm in cre.finditer(sentence):
     pair=pair_for_connector(occ,cm.start(),cm.end())
     if pair is None:continue
     left,right=pair;key=(u['id'],sa+cm.start(),left['concepto_id'],right['concepto_id'])
     if key in seen:continue
     seen.add(key);literal=sentence.strip();trim=sentence.find(literal);a=sa+trim;b=a+len(literal);ls,le=line_range(u,text,a,b)
     established=by[left['concepto_id']].get('estado_identidad_conceptual')=='establecida_por_evidencia' and by[right['concepto_id']].get('estado_identidad_conceptual')=='establecida_por_evidencia'
     explicit=bool(strong and established);classification='relacion_explicita' if explicit else 'relacion_candidata'
     rid=sid('REL',obra_id,u['id'],left['concepto_id'],right['concepto_id'],str(a),str(b),cm.group(0))
     rows.append({'id':rid,'tipo_registro':'relacion_explicita','schema_version':SCHEMA,'texto_literal':literal,'normalizacion_formal':None,'normalizacion_lexica':None,'estatus_enunciativo':None,
      'estado_extraccion':'extraido' if explicit else 'candidato','estado_verificacion':'pendiente','estado_auditoria':'pendiente','producido_por':{'motor':MOTOR,'version':VERSION},'fuente_id':obra_id,'unidad_id':u['id'],
      'sujeto_ref':left['concepto_id'],'objeto_ref':right['concepto_id'],'relacion_literal':literal,'clasificacion_relacion':classification,'localizacion':{'ruta':u['archivo'],'linea_inicio':ls,'linea_fin':le}})
 rows.sort(key=lambda r:(r['localizacion']['ruta'],r['localizacion']['linea_inicio'],r['id']));dump(salida,rows)
 cov={'id':sid('COB',obra_id,MOTOR,VERSION),'tipo_registro':'reporte_cobertura','schema_version':SCHEMA,'texto_literal':None,'normalizacion_formal':None,'normalizacion_lexica':None,'estatus_enunciativo':None,'estado_extraccion':'extraido','estado_verificacion':'pendiente','estado_auditoria':'no_aplica','producido_por':{'motor':MOTOR,'version':VERSION},'obra_id':obra_id,'motor':MOTOR,'version_motor':VERSION,'unidades_totales':len(units),'unidades_procesadas':len(units),'unidades_omitidas':[],'errores':[]};dump(cobertura,[cov])
 return {'version':VERSION,'obra_id':obra_id,'registros':len(rows),'explicitas':sum(r['clasificacion_relacion']=='relacion_explicita' for r in rows)}
def main():
 p=argparse.ArgumentParser();p.add_argument('--obra-id',required=True);p.add_argument('--unidades',type=Path,required=True);p.add_argument('--conceptos',type=Path,required=True);p.add_argument('--salida',type=Path,required=True);p.add_argument('--cobertura',type=Path,required=True);a=p.parse_args();print(json.dumps(run(obra_id=a.obra_id,unidades=a.unidades,conceptos=a.conceptos,salida=a.salida,cobertura=a.cobertura),ensure_ascii=False,sort_keys=True));return 0
if __name__=='__main__':raise SystemExit(main())
