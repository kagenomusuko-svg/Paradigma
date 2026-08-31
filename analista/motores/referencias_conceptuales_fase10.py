#!/usr/bin/env python3
"""Índice formal de designaciones conceptuales de una sola obra.

No lematiza, no busca sinónimos y no compara obras. Solo localiza secuencias de
tokens que coinciden con la designación operativa normalizada de un concepto.
Si dos o más conceptos distintos colapsan a la misma firma mecánica de tokens,
la firma queda deliberadamente fuera del índice: el helper conserva los
conceptos, pero no elige ni fusiona una identidad ambigua.
"""
from __future__ import annotations
import re, unicodedata
from collections import defaultdict
TOKEN_RE=re.compile(r"[^\W_]+(?:[-‐‑][^\W_]+)*|[φΦψΨ][₀-₉0-9]*",re.UNICODE)

def norm(x:str)->str:return " ".join(unicodedata.normalize("NFKC",x).casefold().split())
def tokens(text:str):return [(m.group(0),norm(m.group(0)),m.start(),m.end()) for m in TOKEN_RE.finditer(text)]

def build_index(concepts:list[dict]):
    signatures=defaultdict(list);by_id={}
    for c in concepts:
        by_id[c["id"]]=c
        ts=tuple(x[1] for x in tokens(c["designacion_operativa"]))
        if ts:signatures[(len(ts),ts)].append(c["id"])
    idx=defaultdict(dict)
    for (n,ts),ids in signatures.items():
        unique=list(dict.fromkeys(ids))
        if len(unique)!=1:
            continue
        idx[n][ts]=unique[0]
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
