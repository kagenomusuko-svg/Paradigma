#!/usr/bin/env python3
"""Segmentación conservadora del segundo lote documental del corpus Paradigma.

La fuente íntegra en corpus/fuentes/ es canónica. Este programa solo crea
copias derivadas y valida que su concatenación reproduzca exactamente la fuente.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
FUENTES = ROOT / "corpus" / "fuentes"

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

SPECS = [
    {"source":"Axiomatizacion_Sistema_Doble_Mediacion.md","dest":"corpus/libros/axiomatizacion-doble-mediacion","id":"AXIOM-SDM","title":"Axiomatización del sistema de la doble mediación","collection":"Metrología Causal","parser":"axiomatizacion"},
    {"source":"ECO_Entrevista_Clinica_Ontologica.md","dest":"corpus/libros/eco","id":"ECO","title":"ECO: Entrevista Clínica Ontológica","collection":"Autodeterminación Causal","parser":"eco"},
    {"source":"El_calculo_de_la_responsabilidad.md","dest":"corpus/libros/calculo-de-la-responsabilidad","id":"CALCULO-R","title":"El cálculo de la responsabilidad: Una ontología matemática para sistemas causales complejos","collection":"Reivindicación ontológica del ego","parser":"calculo"},
    {"source":"El_metodo_Prometeo_imputacion_causal_para_juristas_y_abogados.md","dest":"corpus/libros/metodo-prometeo-juristas-abogados","id":"PROMETEO-JUR","title":"El método Prometeo: Imputación causal para juristas y abogados","collection":"Método Prometeo de imputación causal","parser":"prometeo","source_anomalies":["La fuente contiene dos unidades distintas rotuladas «Capítulo 6»; se conservan como 6a y 6b en la capa derivada sin alterar la fuente."]},
    {"source":"HISTOS_Protocolo_de_Acompanamiento_Ontologico.md","dest":"corpus/libros/histos","id":"HISTOS","title":"HISTOS: Protocolo de Acompañamiento Ontológico","collection":"Autodeterminación Causal","parser":"histos"},
    {"source":"La_transformacion_formal_ontologia_del_ego_como_fundamento_del_calculo_causal.md","dest":"corpus/libros/transformacion-formal","id":"TRANSFORMACION-FORMAL","title":"La transformación formal: La ontología del ego como fundamento del cálculo causal","collection":"Autodeterminación Causal","parser":"transformacion"},
    {"source":"Metrologia_Causal_La_ciencia_de_la_medicion_causal.md","dest":"corpus/libros/metrologia-causal/01-la-ciencia-de-la-medicion-causal","id":"MC-I","title":"Metrología Causal: La ciencia de la medición causal","collection":"Metrología Causal","volume":1,"parser":"metrologia_i"},
    {"source":"Metrologia_Causal_Vol_II.md","dest":"corpus/libros/metrologia-causal/02-vol-ii","id":"MC-II","title":"Metrología Causal: Vol. II","collection":"Metrología Causal","volume":2,"parser":"metrologia_ii"},
    {"source":"SDO_Sistema_de_diagnostico_ontologico.md","dest":"corpus/libros/sdo","id":"SDO","title":"SDO: Sistema de Diagnóstico Ontológico","collection":"Autodeterminación Causal","parser":"sdo"},
    {"source":"Taxonomia_General_de_Aplicaciones.md","dest":"corpus/libros/taxonomia-general-de-aplicaciones","id":"TAXONOMIA","title":"Taxonomía General de Aplicaciones","collection":"Metrología Causal","parser":"taxonomia"},
]

def roman_to_int(value):
    total=0; previous=0
    for char in reversed(value):
        number=ROMAN[char]
        if number<previous: total-=number
        else: total+=number; previous=number
    return total

def previous_nonblank(lines,index,max_back=5):
    result=[]
    for position in range(index-1,max(-1,index-max_back-1),-1):
        value=lines[position].strip()
        if value: result.append((position,value))
    return result

def prefix_start(lines,index,pattern,max_back=4):
    compiled=re.compile(pattern)
    for position,value in previous_nonblank(lines,index,max_back):
        if compiled.fullmatch(value): return position
    return index

def unit(start,kind,filename,key,heading):
    return {"start":start,"kind":kind,"filename":filename,"key":key,"heading":heading}

def boundaries_axiomatizacion(lines):
    result=[]
    prologue=next(i for i,line in enumerate(lines) if line.strip()=="## Prólogo")
    result.append(unit(prologue,"prologo","01-prologo.md","PROLOGO","Prólogo"))
    expected=["0","I","II","III","IV","V","VI","VII","VIII","IX","X"]; found=[]
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"Parte (0|[IVX]+)(?: ·.*)?",raw.strip())
        if not match or index<=250: continue
        code=match.group(1)
        if len(found)<len(expected) and code==expected[len(found)]:
            found.append(code); number=0 if code=="0" else roman_to_int(code)
            result.append(unit(index,"parte",f"parte-{number:02d}.md",f"PARTE-{code}",raw.strip()))
    if found!=expected: raise RuntimeError(f"Secuencia de partes inesperada en Axiomatización: {found}")
    last_part=max(item["start"] for item in result if item["kind"]=="parte")
    for letter in "ABCD":
        index=next(i for i in range(last_part+1,len(lines)) if lines[i].strip()==f"## Apéndice {letter}")
        result.append(unit(index,"apendice",f"apendice-{letter.lower()}.md",f"AP-{letter}",f"Apéndice {letter}"))
    return result

def boundaries_eco(lines):
    result=[]

    def marker_before(index, marker_pattern):
        for position, previous in previous_nonblank(lines, index, 3):
            if re.fullmatch(marker_pattern, previous.strip()):
                return position, previous.strip()
        return None, None

    preliminary_pattern = r"<!-- PARTE: PRELIMINAR · Fundamentos del instrumento -->"
    preliminary_part = {"key":"PRELIMINAR","heading":"Parte preliminar · Fundamentos del instrumento"}
    for number in range(1,6):
        index=next(i for i,line in enumerate(lines) if line.strip()=="Capítulo P·%s" % number)
        start, marker=marker_before(index, preliminary_pattern)
        if start is None:
            raise RuntimeError("ECO: falta el marcador de parte preliminar antes del capítulo P·%s." % number)
        item=unit(start,"capitulo","capitulo-p-%s.md" % number,"P·%s" % number,"Capítulo P·%s" % number)
        item["part"]=preliminary_part
        result.append(item)

    part_labels = {
        "I": {"key":"PARTE-I","heading":"Parte I · Los Hijos de Afrodita"},
        "II": {"key":"PARTE-II","heading":"Parte II · Los cinco ejes del SDO"},
        "III": {"key":"PARTE-III","heading":"Parte III · La entrevista al ego colectivo"},
        "IV": {"key":"PARTE-IV","heading":"Parte IV · Principios generales de intervención"},
    }
    appendix_start=None
    for index,raw in enumerate(lines):
        text=raw.strip()
        if text == "<!-- PARTE: APÉNDICES · Instrumentos de trabajo del mediador -->":
            appendix_start=index
            continue
        if appendix_start is not None:
            continue
        if not re.match(r"^B·(?:I·[FDAPEH]|II·(?:I|II|III|IV|V)|III·[1-5]|IV(?: · §[2-5])?)\b",text): continue
        if text.startswith("B·IV · PRINCIPIOS"):
            code="IV"; key="B·IV·1"; filename="bloque-iv-01.md"
        elif text.startswith("B·IV · §"):
            code="IV"; number=int(re.match(r"^B·IV · §([2-5])",text).group(1)); key="B·IV·%s" % number; filename="bloque-iv-%02d.md" % number
        else:
            code=text.split("·")[1]
            key=text.split(" · ")[0]
            filename=key.replace("·","-").lower()+".md"
        marker_pattern = r"<!-- PARTE: %s -->" % re.escape(part_labels[code]["heading"].replace("Parte ","",1))
        start, marker=marker_before(index, marker_pattern)
        if start is None:
            raise RuntimeError("ECO: falta el marcador de %s antes de %s." % (part_labels[code]["heading"], key))
        item=unit(start,"modulo",filename,key,text)
        item["part"]=part_labels[code]
        result.append(item)

    if appendix_start is None:
        raise RuntimeError("ECO: falta el marcador de la parte de apéndices.")
    appendix_part={"key":"APENDICES","heading":"Apéndices · Instrumentos de trabajo del mediador"}
    item=unit(appendix_start,"apendices","90-apendices.md","APENDICES",appendix_part["heading"])
    item["part"]=appendix_part
    result.append(item)
    return result

def boundaries_calculo(lines):
    result=[]; prologue=next(i for i,line in enumerate(lines) if line.strip()=="PRÓLOGO")
    result.append(unit(prologue,"prologo","01-prologo.md","PROLOGO","PRÓLOGO")); expected=1
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo (\d+)",raw.strip())
        if match and int(match.group(1))==expected:
            start=prefix_start(lines,index,r"## PARTE .*",4)
            result.append(unit(start,"capitulo",f"capitulo-{expected:02d}.md",str(expected),raw.strip())); expected+=1
            if expected==19: break
    if expected!=19: raise RuntimeError(f"Se esperaban 18 capítulos en El cálculo; se detectaron {expected-1}")
    last=result[-1]["start"]
    for letter in "ABCDE":
        index=next(i for i in range(last+1,len(lines)) if lines[i].strip()==f"APÉNDICE {letter}")
        result.append(unit(index,"apendice",f"apendice-{letter.lower()}.md",letter,f"APÉNDICE {letter}"))
    return result

def boundaries_prometeo(lines):
    result=[]; prologue=next(i for i,line in enumerate(lines) if line.strip()=="Prólogo")
    result.append(unit(prologue,"prologo","01-prologo.md","PROLOGO","Prólogo")); chapters=[]
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo (\d+)\.?",raw.strip())
        if not match: continue
        if any(previous=="EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL" for _,previous in previous_nonblank(lines,index,5)):
            chapters.append((index,int(match.group(1)),raw.strip()))
    occurrences=Counter(number for _,number,_ in chapters); used=Counter()
    for index,number,heading in chapters:
        used[number]+=1; suffix=""
        if occurrences[number]>1: suffix=chr(ord("a")+used[number]-1)
        result.append(unit(index,"capitulo",f"capitulo-{number:02d}{suffix}.md",f"{number}{suffix}",heading))
    last=chapters[-1][0]
    for letter in "ABC":
        index=next(i for i in range(last+1,len(lines)) if lines[i].strip()==f"Apéndice {letter}")
        result.append(unit(index,"apendice",f"apendice-{letter.lower()}.md",letter,f"Apéndice {letter}"))
    return result

def boundaries_histos(lines):
    result=[]
    for number in range(1,6):
        index=next(i for i,line in enumerate(lines) if line.strip()==f"Capítulo P·{number}")
        start=prefix_start(lines,index,r"PARTE PRELIMINAR · Fundamentos del instrumento",3)
        result.append(unit(start,"capitulo",f"capitulo-p-{number}.md",f"P·{number}",f"Capítulo P·{number}"))
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo ([IVX]+)·(\d+)",raw.strip())
        if not match: continue
        block=None
        for position,previous in previous_nonblank(lines,index,3):
            if re.match(r"^BLOQUE [IVX]+ ·",previous): block=position; break
        if block is None: continue
        roman,number=match.group(1),int(match.group(2))
        result.append(unit(block,"capitulo",f"capitulo-{roman_to_int(roman):02d}-{number:02d}.md",f"{roman}·{number}",raw.strip()))
    return result

def boundaries_transformacion(lines):
    result=[]; prologue=next(i for i,line in enumerate(lines) if i>300 and line.strip()=="PRÓLOGO")
    result.append(unit(prologue,"prologo","01-prologo.md","PROLOGO","PRÓLOGO"))
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo (\d+)\.(\d+)",raw.strip())
        if not match: continue
        start=prefix_start(lines,index,r"## PARTE .*",4); a,b=int(match.group(1)),int(match.group(2))
        result.append(unit(start,"capitulo",f"capitulo-{a:02d}-{b:02d}.md",f"{a}.{b}",raw.strip()))
    epilogue=next(i for i,line in enumerate(lines) if i>result[-1]["start"] and line.strip()=="Epílogo")
    result.append(unit(epilogue,"epilogo","90-epilogo.md","EPILOGO","Epílogo")); return result

def boundaries_metrologia_i(lines):
    result=[]; prologue=next(i for i,line in enumerate(lines) if line.strip()=="PRÓLOGO")
    result.append(unit(prologue,"prologo","01-prologo.md","PROLOGO","PRÓLOGO"))
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo ([IVX]+)·(\d+)",raw.strip())
        if not match: continue
        start=prefix_start(lines,index,r"## PARTE .*",4); roman,number=match.group(1),int(match.group(2))
        result.append(unit(start,"capitulo",f"capitulo-{roman_to_int(roman):02d}-{number:02d}.md",f"{roman}·{number}",raw.strip()))
    for number in (1,2):
        index=next(i for i,line in enumerate(lines) if line.strip()==f"Capítulo E·{number}"); start=index
        for position in range(index-1,max(-1,index-5),-1):
            if lines[position].strip().startswith("EPÍLOGO ·"): start=position; break
        result.append(unit(start,"epilogo",f"epilogo-{number:02d}.md",f"E·{number}",f"Capítulo E·{number}"))
    for number in range(1,7):
        index=next(i for i,line in enumerate(lines) if line.strip()==f"Apéndice A·{number}"); start=index
        for position in range(index-1,max(-1,index-4),-1):
            if lines[position].strip().startswith("APÉNDICES ·"): start=position; break
        result.append(unit(start,"apendice",f"apendice-a-{number:02d}.md",f"A·{number}",f"Apéndice A·{number}"))
    glossary=next(i for i,line in enumerate(lines) if line.strip()=="## GLOSARIO")
    result.append(unit(glossary,"glosario","99-glosario.md","GLOSARIO","GLOSARIO")); return result

def boundaries_metrologia_ii(lines):
    result=[]; introduction=next(i for i,line in enumerate(lines) if line.strip()=="INTRODUCCIÓN")
    result.append(unit(introduction,"introduccion","01-introduccion.md","INTRO","INTRODUCCIÓN"))
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo ([IVX]+)·(\d+)",raw.strip())
        if not match: continue
        start=prefix_start(lines,index,r"## PARTE .*",4); roman,number=match.group(1),int(match.group(2))
        result.append(unit(start,"capitulo",f"capitulo-{roman_to_int(roman):02d}-{number:02d}.md",f"{roman}·{number}",raw.strip()))
    for letter in "AB":
        index=next(i for i,line in enumerate(lines) if i>4000 and line.strip()==f"Apéndice {letter}"); start=index
        for position in range(index-1,max(-1,index-4),-1):
            if lines[position].strip()=="APÉNDICES": start=position; break
        result.append(unit(start,"apendice",f"apendice-{letter.lower()}.md",letter,f"Apéndice {letter}"))
    return result

def boundaries_sdo(lines):
    result=[]; pattern=re.compile(r"(PI·\d+|I·0|I·E-\d+|II·0|II·M-\d+|III·0|III·V-\d+|IV·0|IV·D-\d+|V·0|V·T-(?:\d+|ext)|VI·\d+|VII·\d+|VIII·\d+)$")
    for index,raw in enumerate(lines):
        text=raw.strip()
        if not text.startswith("## PARTE"): continue
        match=pattern.search(text)
        if not match: continue
        code=match.group(1); filename=code.lower().replace("·","-")+".md"
        result.append(unit(index,"unidad",filename,code,text))
    return result

def boundaries_taxonomia(lines):
    result=[]
    for number in range(1,5):
        index=next(i for i,line in enumerate(lines) if line.strip()==f"Capítulo U·{number}")
        start=prefix_start(lines,index,r"PARTE U · Protocolo Universal",3)
        result.append(unit(start,"capitulo",f"capitulo-u-{number:02d}.md",f"U·{number}",f"Capítulo U·{number}"))
    numeric=[]
    for index,raw in enumerate(lines):
        match=re.fullmatch(r"### Capítulo (\d+)",raw.strip())
        if match: numeric.append((index,int(match.group(1)),raw.strip()))
    if [number for _,number,_ in numeric]!=list(range(1,79)): raise RuntimeError("La Taxonomía no contiene la secuencia exacta de capítulos 1–78.")
    for index,number,heading in numeric:
        start=prefix_start(lines,index,r"## PARTE .*",4)
        result.append(unit(start,"capitulo",f"capitulo-{number:02d}.md",str(number),heading))
    return result

PARSERS={"axiomatizacion":boundaries_axiomatizacion,"eco":boundaries_eco,"calculo":boundaries_calculo,"prometeo":boundaries_prometeo,"histos":boundaries_histos,"transformacion":boundaries_transformacion,"metrologia_i":boundaries_metrologia_i,"metrologia_ii":boundaries_metrologia_ii,"sdo":boundaries_sdo,"taxonomia":boundaries_taxonomia}

def _parts_index(segments):
    parts=[]
    by_key={}
    for segment in segments:
        part=segment.get("part")
        if not part: continue
        key=part["key"]
        if key not in by_key:
            entry={"key":key,"heading":part["heading"],"members":[]}
            by_key[key]=entry
            parts.append(entry)
        if segment.get("key") and segment["key"] not in by_key[key]["members"]:
            by_key[key]["members"].append(segment["key"])
    return parts


def segment(spec):
    source=FUENTES/spec["source"]
    if not source.exists(): return None
    text=source.read_text(encoding="utf-8"); lines=text.splitlines(keepends=True)
    boundaries=sorted(PARSERS[spec["parser"]](lines),key=lambda item:item["start"]); unique=[]; seen=set()
    for item in boundaries:
        if item["start"] not in seen: seen.add(item["start"]); unique.append(item)
    boundaries=unique; destination=ROOT/spec["dest"]
    if destination.exists(): shutil.rmtree(destination)
    destination.mkdir(parents=True)
    first=boundaries[0]["start"] if boundaries else len(lines); prelim=destination/"00-preliminares.md"
    prelim.write_text("".join(lines[:first]),encoding="utf-8",newline="")
    segments=[{"path":str(prelim.relative_to(ROOT)).replace("\\","/"),"kind":"preliminares","start_line":1,"end_line":first}]; names=Counter()
    for position,item in enumerate(boundaries):
        start=item["start"]; end=boundaries[position+1]["start"] if position+1<len(boundaries) else len(lines); filename=item["filename"]; names[filename]+=1
        if names[filename]>1:
            path=Path(filename); filename=f"{path.stem}-{names[filename]}{path.suffix}"
        target=destination/filename; target.write_text("".join(lines[start:end]),encoding="utf-8",newline="")
        segment={"path":str(target.relative_to(ROOT)).replace("\\","/"),"kind":item["kind"],"key":item["key"],"heading":item["heading"],"start_line":start+1,"end_line":end}
        if "part" in item: segment["part"]=item["part"]
        segments.append(segment)
    reconstructed=b"".join((ROOT/item["path"]).read_bytes() for item in segments)
    if reconstructed!=source.read_bytes(): raise RuntimeError(f"La segmentación no reconstruye exactamente {source.name}")
    metadata={"id":spec["id"],"title":spec["title"],"source":str(source.relative_to(ROOT)).replace("\\","/"),"sha256":hashlib.sha256(source.read_bytes()).hexdigest(),"collection":spec.get("collection"),"volume":spec.get("volume"),"source_anomalies":spec.get("source_anomalies",[]),"segmentation_rule":"Cortes estructurales conservadores; la fuente íntegra es canónica.","parts":_parts_index(segments),"segments":segments}
    (destination/"estructura.json").write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); return metadata

def main():
    processed=[]; missing=[]
    for spec in SPECS:
        metadata=segment(spec)
        if metadata is None: missing.append(spec["source"])
        else: processed.append(metadata["title"])
    print(f"Segundo lote segmentado y validado: {len(processed)} obras.")
    if missing: print(f"Fuentes del lote aún no presentes: {len(missing)}")

if __name__=="__main__": main()
