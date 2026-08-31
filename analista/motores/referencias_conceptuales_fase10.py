#!/usr/bin/env python3
"""Índice formal de designaciones conceptuales de una sola obra.

No lematiza, no busca sinónimos y no compara obras. Solo localiza secuencias de
tokens que coinciden con la designación operativa normalizada de un concepto.
"""
from __future__ import annotations
import re, unicodedata
from collections import defaultdict
TOKEN_RE=re.compile(r"[^\W_]+(?:[-‐‑][^\W_]+)*|[φΦψΨ][₀-₉0-9]*",re.UNICODE)

def norm(x:str)->str:return " ".join(unicodedata.normalize("NFKC",x).casefold().split())
def tokens(text:str):return [(m.group(0),norm(m.group(0)),m.start(),m.end()) for m in TOKEN_RE.finditer(text)]

def build_index(concepts:list[dict]):
    idx=defaultdict(dict); by_id={}
    for c in concepts:
        ts=tuple(x[1] for x in tokens(c["designacion_operativa"]))
        if not ts:continue
        prev=idx[len(ts)].get(ts)
        if prev is not None and prev!=c["id"]:
            anterior=by_id.get(prev,{})
            raise SystemExit(
                "Designación formal duplicada: "
                f"tokens={ts!r}; "
                f"anterior={{id={prev!r}, designacion={anterior.get('designacion_operativa')!r}, "
                f"estado_identidad={anterior.get('estado_identidad_conceptual')!r}, estado_extraccion={anterior.get('estado_extraccion')!r}}}; "
                f"actual={{id={c.get('id')!r}, designacion={c.get('designacion_operativa')!r}, "
                f"estado_identidad={c.get('estado_identidad_conceptual')!r}, estado_extraccion={c.get('estado_extraccion')!r}}}"
            )
        idx[len(ts)][ts]=c["id"];by_id[c["id"]]=c
    return dict(idx),by_id

def occurrences(text:str,index:dict[int,dict[tuple[str,...],str]])->list[dict]:
    ts=tokens(text);out=[];seen=set()
    for n,mapping in index.items():
        if n>len(ts):continue
        for i in range(len(ts)-n+1):
            key=tuple(x[1] for x in ts[i:i+n]);cid=mapping.get(key)
            if cid is None:continue
            start,end=ts[i][2],ts[i+n-1][3];ident=(start,end,cid)
            if ident in seen:continue
            seen.add(ident);out.append({"concepto_id":cid,"inicio":start,"fin":end,"literal":text[start:end]})
    out.sort(key=lambda x:(x["inicio"],-(x["fin"]-x["inicio"]),x["concepto_id"]));return out
