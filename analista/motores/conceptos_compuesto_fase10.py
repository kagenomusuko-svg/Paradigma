#!/usr/bin/env python3
"""4A de Fase 10: identidad explícita por glosario + candidatos intraobra.

Compone dos señales mecánicas sin leer ni interpretar doctrinalmente la obra:
1) un lema declarado en el glosario técnico propio establece identidad;
2) el recuperador genérico encuentra otras designaciones candidatas por forma
   y recurrencia literal. Ninguna semejanza semántica fusiona conceptos.
"""
from __future__ import annotations
import argparse, importlib.util, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERIC = ROOT / "analista/motores/conceptos_obra_fase10.py"
MOTOR = "conceptos_apariciones"
VERSION = "1.2.0"
GLOSSARY = "99-glosario.md"
ARROW = re.compile(r"^\s*→")
ROMAN = re.compile(r"^[IVXLCDM]+$", re.I)

spec = importlib.util.spec_from_file_location("conceptos_generico_fase10", GENERIC)
assert spec and spec.loader
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)


def load(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x]


def dump(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in rows), encoding="utf-8")


def producer(row: dict) -> dict:
    row["producido_por"] = {"motor": MOTOR, "version": VERSION}
    return row


def glossary_entries(path: Path) -> list[tuple[str,int]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next((i for i,x in enumerate(lines) if "glosario" in g.norm(x)), None)
    if start is None: raise SystemExit(f"Glosario sin encabezado: {path}")
    out=[]; seen=set(); i=start+1
    while i < len(lines):
        term=lines[i].strip()
        if not term or term.startswith("#") or ROMAN.fullmatch(term): i+=1; continue
        term_line=i+1; i+=1; body=False; arrow=False
        while i < len(lines):
            cur=lines[i].strip()
            if ARROW.match(cur): arrow=True; i+=1; break
            if cur and not cur.startswith("#") and not ROMAN.fullmatch(cur): body=True
            i+=1
        if not (body and arrow): continue
        key=g.norm(term)
        if key in seen: raise SystemExit(f"Lema duplicado: {term}")
        seen.add(key); out.append((term,term_line))
    if not out: raise SystemExit(f"Glosario sin entradas: {path}")
    return out


def strict_records(obra_id: str, units: list[dict], glossary_rel: str) -> tuple[list[dict],list[dict],set[str]]:
    entries=glossary_entries(ROOT/glossary_rel)
    lines=(ROOT/glossary_rel).read_text(encoding="utf-8").splitlines()
    apps=[]; concepts=[]; confirmed=set(); seen_ids=set()
    for term, term_line in entries:
        key=g.norm(term); confirmed.add(key); cid=g.stable_id("CON", key)
        pattern=re.compile(r"(?<!\w)"+r"\s+".join(re.escape(x) for x in term.split())+r"(?!\w)", re.I)
        linked=[]; evidence=[]
        for u in units:
            text=u["texto_literal"]
            for m in pattern.finditer(text):
                ls,le=g.line_range(u,text,m.start(),m.end()); literal=m.group(0)
                declaration=(u["archivo"]==glossary_rel and ls==le==term_line and lines[term_line-1].strip()==term and g.norm(literal)==key)
                linked_here=declaration or (len(term.split())>1 and g.norm(literal)==key)
                aid=g.stable_id("APC",cid,u["id"],str(ls),str(m.start()),literal)
                if aid in seen_ids: raise SystemExit(f"Aparición duplicada: {aid}")
                seen_ids.add(aid)
                r=g.base_record(aid,"aparicion_conceptual",literal); producer(r)
                r["estado_extraccion"]="extraido" if linked_here else "candidato"
                r.update({"fuente_id":obra_id,"unidad_id":u["id"],"concepto_id":cid if linked_here else None,
                    "forma_literal":literal,"variante_formal":None if literal==term else term,"variantes_lexicas_busqueda":[],
                    "localizacion":{"ruta":u["archivo"],"linea_inicio":ls,"linea_fin":le},
                    "criterio_deteccion":"lema_en_glosario_tecnico_explicito" if declaration else (
                        "designacion_tecnica_multilexema_exacta; sin_normalizacion_semantica" if linked_here else
                        "coincidencia_formal_con_lema_glosario; identidad_conceptual_no_determinada")})
                apps.append(r)
                if linked_here: linked.append(aid)
                if declaration: evidence.append(aid)
        if len(evidence)!=1: raise SystemExit(f"Lema {term!r}: evidencia declarativa={len(evidence)}")
        c=g.base_record(cid,"concepto",term); producer(c); c["estado_extraccion"]="extraido"
        c.update({"designacion_operativa":term,"aparicion_ids":sorted(linked),"formas_literales_observadas":[term],
            "estado_identidad_conceptual":"establecida_por_evidencia","evidencia_identidad_ids":evidence})
        concepts.append(c)
    return apps,concepts,confirmed


def coverage(obra_id: str, n: int) -> dict:
    r=g.coverage_record(obra_id,n); producer(r); r["version_motor"]=VERSION; return r


def run(*, obra_id:str, fuentes:Path, unidades:Path, apariciones:Path, conceptos:Path, cobertura:Path) -> dict:
    sources=[x for x in load(fuentes) if x.get("id")==obra_id]
    if len(sources)!=1: raise SystemExit(f"Fuente {obra_id}: {len(sources)}")
    units=[x for x in load(unidades) if x.get("fuente_id")==obra_id]
    if not units: raise SystemExit(f"Sin unidades: {obra_id}")
    gloss=[x for x in sources[0].get("rutas_derivadas",[]) if str(x).endswith(GLOSSARY)]
    if len(gloss)>1: raise SystemExit(f"Glosarios ambiguos: {gloss}")
    sa=[]; sc=[]; confirmed=set()
    if gloss: sa,sc,confirmed=strict_records(obra_id,units,str(gloss[0]))
    ga,gc=g.build_candidate_records(obra_id,units,confirmed_norms=confirmed)
    for r in ga+gc: producer(r)
    all_a=sa+ga; all_c=sc+gc
    all_a.sort(key=lambda r:(r["localizacion"]["ruta"],r["localizacion"]["linea_inicio"],r["id"])); all_c.sort(key=lambda r:r["id"])
    ids=[r["id"] for r in all_a+all_c]
    if len(ids)!=len(set(ids)): raise SystemExit("IDs conceptuales duplicados")
    dump(apariciones,all_a); dump(conceptos,all_c); dump(cobertura,[coverage(obra_id,len(units))])
    return {"version":VERSION,"obra_id":obra_id,"unidades":len(units),"glosario":gloss[0] if gloss else None,
            "conceptos_confirmados":len(sc),"conceptos_candidatos":len(gc),"apariciones":len(all_a)}


def main()->int:
    p=argparse.ArgumentParser(); p.add_argument("--obra-id",required=True); p.add_argument("--fuentes",type=Path,required=True); p.add_argument("--unidades",type=Path,required=True); p.add_argument("--apariciones",type=Path,required=True); p.add_argument("--conceptos",type=Path,required=True); p.add_argument("--cobertura",type=Path,required=True); a=p.parse_args()
    print(json.dumps(run(obra_id=a.obra_id,fuentes=a.fuentes,unidades=a.unidades,apariciones=a.apariciones,conceptos=a.conceptos,cobertura=a.cobertura),ensure_ascii=False,sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
