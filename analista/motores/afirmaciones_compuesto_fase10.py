#!/usr/bin/env python3
"""4C de Fase 10: bloques proposicionales genéricos con referencias literales.

No atribuye tesis por coaparición. Cada salida es candidata; su estatus solo se
precisa cuando existe una señal formal (pregunta, condicional, cita o discurso
referido). ``concepto_ids`` funciona como índice de apariciones exactas dentro
del propio bloque, no como predicación inferida.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; MOTOR="afirmaciones"; VERSION="1.2.0"; SCHEMA="1.0.0"
HELPER=ROOT/"analista/motores/referencias_conceptuales_fase10.py"
s=importlib.util.spec_from_file_location("refs_f10",HELPER);assert s and s.loader;refs=importlib.util.module_from_spec(s);s.loader.exec_module(refs)
BOUNDARY=re.compile(r"(?<=[.!?])(?:[¹²³⁴⁵⁶⁷⁸⁹⁰]+)?\s+(?=[A-ZÁÉÍÓÚÜÑ¿¡«“])")
REFERRED=re.compile(r"\b(?:según|de acuerdo con|como (?:afirma|sostiene|propone|señala)|para [A-ZÁÉÍÓÚÜÑ][\wÁÉÍÓÚÜÑáéíóúüñ-]+)\b",re.I)

def sid(prefix,*parts):return f"{prefix}-{hashlib.sha1(chr(31).join(parts).encode()).hexdigest()[:12].upper()}"
def load(p):return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x]
def dump(p,rows):p.parent.mkdir(parents=True,exist_ok=True);p.write_text("".join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding="utf-8")
def line_range(u,text,a,b):
    x=u["localizacion"]["linea_inicio"]+text[:a].count("\n");return x,x+text[a:b].count("\n")
def spans(text):
    out=[];start=0
    for m in BOUNDARY.finditer(text):
        end=m.start();a=start
        while a<end and text[a].isspace():a+=1
        if a<end:out.append((a,end,text[a:end]))
        start=m.end()
    a=start
    while a<len(text) and text[a].isspace():a+=1
    if a<len(text):out.append((a,len(text),text[a:]))
    return out

def status(literal):
    x=literal.strip();n=refs.norm(x)
    if x.startswith("¿") or x.endswith("?"):return "pregunta"
    if n.startswith("si "):return "formulacion_condicional"
    if (x.startswith("«") and x.endswith("»")) or (x.startswith("“") and x.endswith("”")):return "cita"
    if REFERRED.search(x):return "discurso_referido"
    return "no_determinado"
def run(*,obra_id,unidades,conceptos,salida,cobertura):
    units=[x for x in load(unidades) if x.get("fuente_id")==obra_id];cons=load(conceptos);index,_=refs.build_index(cons)
    if not units:raise SystemExit(f"Sin unidades: {obra_id}")
    rows=[];ids=set()
    for u in units:
        if u.get("tipo_estructural") in {"encabezado","separador"}:continue
        text=u["texto_literal"]
        for a,b,literal in spans(text):
            occ=refs.occurrences(literal,index);cids=sorted({x["concepto_id"] for x in occ})
            if not cids:continue
            rid=sid("AF",obra_id,u["id"],str(a),str(b),literal)
            if rid in ids:raise SystemExit(f"Afirmación duplicada: {rid}")
            ids.add(rid);ls,le=line_range(u,text,a,b)
            rows.append({"id":rid,"tipo_registro":"afirmacion","schema_version":SCHEMA,"texto_literal":literal,
              "normalizacion_formal":None,"normalizacion_lexica":None,"estatus_enunciativo":status(literal),
              "estado_extraccion":"candidato","estado_verificacion":"pendiente","estado_auditoria":"pendiente",
              "producido_por":{"motor":MOTOR,"version":VERSION},"fuente_id":obra_id,"unidad_id":u["id"],"concepto_ids":cids,
              "clasificacion_afirmacion":"afirmacion_candidata","sujeto_literal":None,"predicado_literal":None,"objeto_literal":None,
              "localizacion":{"ruta":u["archivo"],"linea_inicio":ls,"linea_fin":le},
              "criterio_deteccion":"bloque_proposicional_con_referencia_conceptual_literal; sin_atribucion_doctrinal_por_coaparicion","confianza_extraccion":None})
    rows.sort(key=lambda r:(r["localizacion"]["ruta"],r["localizacion"]["linea_inicio"],r["id"]));dump(salida,rows)
    cov={"id":sid("COB",obra_id,MOTOR,VERSION),"tipo_registro":"reporte_cobertura","schema_version":SCHEMA,"texto_literal":None,"normalizacion_formal":None,"normalizacion_lexica":None,"estatus_enunciativo":None,"estado_extraccion":"extraido","estado_verificacion":"pendiente","estado_auditoria":"no_aplica","producido_por":{"motor":MOTOR,"version":VERSION},"obra_id":obra_id,"motor":MOTOR,"version_motor":VERSION,"unidades_totales":len(units),"unidades_procesadas":len(units),"unidades_omitidas":[],"errores":[]};dump(cobertura,[cov])
    return {"version":VERSION,"obra_id":obra_id,"registros":len(rows),"referencias":sum(len(r["concepto_ids"]) for r in rows)}
def main():
    p=argparse.ArgumentParser();p.add_argument("--obra-id",required=True);p.add_argument("--unidades",type=Path,required=True);p.add_argument("--conceptos",type=Path,required=True);p.add_argument("--salida",type=Path,required=True);p.add_argument("--cobertura",type=Path,required=True);a=p.parse_args();print(json.dumps(run(obra_id=a.obra_id,unidades=a.unidades,conceptos=a.conceptos,salida=a.salida,cobertura=a.cobertura),ensure_ascii=False,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
