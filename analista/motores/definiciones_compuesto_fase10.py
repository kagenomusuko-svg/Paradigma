#!/usr/bin/env python3
"""4B de Fase 10: definiciones genéricas ligadas a conceptos de la misma obra.

Solo usa coincidencia literal/formal de designaciones ya recuperadas por 4A.
Las estructuras definicionales fuertes pueden registrarse como explícitas; la
cópula simple y la aposición quedan candidatas. No crea identidades ni sinónimos.
"""
from __future__ import annotations
import argparse, hashlib, json, re, unicodedata
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MOTOR="definiciones"; VERSION="1.2.0"; SCHEMA="1.0.0"; GLOSSARY="99-glosario.md"
SPACE=re.compile(r"\s+")
STRONG_AFTER=("se define como","significa","designa","se denomina","se entiende como")
STRONG_BEFORE=("llamamos ","denominamos ","definimos ","defino ","denomino ")

def norm(x:str)->str:return SPACE.sub(" ",unicodedata.normalize("NFKC",x).casefold()).strip()
def sid(prefix:str,*parts:str)->str:return f"{prefix}-{hashlib.sha1(chr(31).join(parts).encode()).hexdigest()[:12].upper()}"
def load(path:Path)->list[dict]:return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x]
def dump(path:Path,rows:list[dict])->None:
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text("".join(json.dumps(r,ensure_ascii=False,sort_keys=True)+"\n" for r in rows),encoding="utf-8")

def base(rid:str,literal:str,status:str,classification:str)->dict:
    return {"id":rid,"tipo_registro":"definicion","schema_version":SCHEMA,"texto_literal":literal,
      "normalizacion_formal":None,"normalizacion_lexica":None,"estatus_enunciativo":status,
      "estado_extraccion":"extraido" if classification=="definicion_explicita" else "candidato",
      "estado_verificacion":"pendiente","estado_auditoria":"pendiente",
      "producido_por":{"motor":MOTOR,"version":VERSION}}

def line_range(unit:dict,text:str,start:int,end:int)->tuple[int,int]:
    first=unit["localizacion"]["linea_inicio"]+text[:start].count("\n"); return first,first+text[start:end].count("\n")

def term_re(name:str)->re.Pattern[str]:
    body=r"\s+".join(re.escape(x) for x in name.split()); return re.compile(rf"(?<![\w\-‐‑]){body}(?![\w\-‐‑])",re.I)

def sentence_span(text:str,pos:int)->tuple[int,int]:
    starts=[text.rfind(c,0,pos) for c in ".!?\n"]; start=max(starts)+1
    ends=[text.find(c,pos) for c in ".!?\n" if text.find(c,pos)>=0]; end=min(ends)+1 if ends else len(text)
    while start<end and text[start].isspace():start+=1
    while end>start and text[end-1].isspace():end-=1
    return start,end

def classify(sentence:str,term_literal:str)->tuple[str,str,str]|None:
    n=norm(sentence); t=norm(term_literal); p=n.find(t)
    if p<0:return None
    before=n[:p].rstrip(); after=n[p+len(t):].lstrip()
    if after.startswith(STRONG_AFTER):return "definicion_explicita","definicion","estructura_definicional_fuerte_postnominal"
    if any(before.endswith(x.rstrip()) for x in STRONG_BEFORE):return "definicion_explicita","definicion","estructura_definicional_fuerte_prenominal"
    if before.endswith("por") and after.startswith("se entiende"):
        return "definicion_explicita","definicion","estructura_por_termino_se_entiende"
    if re.match(r"^(?:es|son)\b",after):return "definicion_candidata","no_determinado","copula_simple_no_autoriza_definicion_explicita"
    if after.startswith(":"):return "definicion_candidata","no_determinado","aposicion_dos_puntos_candidata"
    return None

def glossary_definitions(obra_id:str,source:dict,units:list[dict],concepts:list[dict])->list[dict]:
    gloss=[str(x) for x in source.get("rutas_derivadas",[]) if str(x).endswith(GLOSSARY)]
    if len(gloss)!=1:return []
    rel=gloss[0]; path=ROOT/rel
    if not path.is_file():raise SystemExit(f"Glosario inexistente: {rel}")
    lines=path.read_text(encoding="utf-8").splitlines(); by={norm(c["designacion_operativa"]):c for c in concepts if c.get("estado_identidad_conceptual")=="establecida_por_evidencia"}
    out=[]
    for i,line in enumerate(lines):
        c=by.get(norm(line.strip()))
        if c is None:continue
        j=i+1; body=[]
        while j<len(lines) and not lines[j].lstrip().startswith("→"):
            if lines[j].strip() and not lines[j].startswith("#"):body.append(j)
            j+=1
        if not body or j>=len(lines):continue
        start,end=body[0]+1,body[-1]+1; literal="\n".join(lines[start-1:end])
        holders=[u for u in units if u["archivo"]==rel and u["localizacion"]["linea_inicio"]<=start<=end<=u["localizacion"]["linea_fin"]]
        if len(holders)!=1:raise SystemExit(f"Definición de glosario sin unidad única: {c['id']}")
        rid=sid("DEF",obra_id,rel,str(start),str(end),c["id"],literal); r=base(rid,literal,"definicion","definicion_explicita")
        r.update({"fuente_id":obra_id,"unidad_id":holders[0]["id"],"concepto_id":c["id"],"clasificacion_definicion":"definicion_explicita",
          "localizacion":{"ruta":rel,"linea_inicio":start,"linea_fin":end},"criterio_deteccion":"entrada_de_glosario_tecnico_explicito"});out.append(r)
    return out

def run(*,obra_id:str,fuentes:Path,unidades:Path,conceptos:Path,salida:Path,cobertura:Path)->dict:
    src=[x for x in load(fuentes) if x.get("id")==obra_id]
    if len(src)!=1:raise SystemExit(f"Fuente {obra_id}: {len(src)}")
    units=[x for x in load(unidades) if x.get("fuente_id")==obra_id]; concepts=load(conceptos)
    if not units:raise SystemExit(f"Sin unidades: {obra_id}")
    rows=glossary_definitions(obra_id,src[0],units,concepts); seen={(r["unidad_id"],r["concepto_id"],r["texto_literal"]) for r in rows}
    for u in units:
        if u["archivo"].endswith(GLOSSARY) or u.get("tipo_estructural")=="encabezado":continue
        text=u["texto_literal"]
        for c in concepts:
            for m in term_re(c["designacion_operativa"]).finditer(text):
                a,b=sentence_span(text,m.start()); sentence=text[a:b]; result=classify(sentence,m.group(0))
                if result is None:continue
                classification,status,criterion=result; key=(u["id"],c["id"],sentence)
                if key in seen:continue
                seen.add(key); ls,le=line_range(u,text,a,b); rid=sid("DEF",obra_id,u["id"],str(a),str(b),c["id"],sentence)
                r=base(rid,sentence,status,classification);r.update({"fuente_id":obra_id,"unidad_id":u["id"],"concepto_id":c["id"],
                  "clasificacion_definicion":classification,"localizacion":{"ruta":u["archivo"],"linea_inicio":ls,"linea_fin":le},"criterio_deteccion":criterion});rows.append(r)
    rows.sort(key=lambda r:(r["localizacion"]["ruta"],r["localizacion"]["linea_inicio"],r["id"]));dump(salida,rows)
    cov={"id":sid("COB",obra_id,MOTOR,VERSION),"tipo_registro":"reporte_cobertura","schema_version":SCHEMA,"texto_literal":None,"normalizacion_formal":None,"normalizacion_lexica":None,"estatus_enunciativo":None,"estado_extraccion":"extraido","estado_verificacion":"pendiente","estado_auditoria":"no_aplica","producido_por":{"motor":MOTOR,"version":VERSION},"obra_id":obra_id,"motor":MOTOR,"version_motor":VERSION,"unidades_totales":len(units),"unidades_procesadas":len(units),"unidades_omitidas":[],"errores":[]};dump(cobertura,[cov])
    return {"version":VERSION,"obra_id":obra_id,"registros":len(rows),"explicitas":sum(r["clasificacion_definicion"]=="definicion_explicita" for r in rows)}

def main()->int:
    p=argparse.ArgumentParser();p.add_argument("--obra-id",required=True);p.add_argument("--fuentes",type=Path,required=True);p.add_argument("--unidades",type=Path,required=True);p.add_argument("--conceptos",type=Path,required=True);p.add_argument("--salida",type=Path,required=True);p.add_argument("--cobertura",type=Path,required=True);a=p.parse_args();print(json.dumps(run(obra_id=a.obra_id,fuentes=a.fuentes,unidades=a.unidades,conceptos=a.conceptos,salida=a.salida,cobertura=a.cobertura),ensure_ascii=False,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())
