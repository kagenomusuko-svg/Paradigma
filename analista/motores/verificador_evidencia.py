#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, copy, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FUENTES = ROOT / 'analista/generado/fuentes.jsonl'
DEFAULT_UNIDADES = ROOT / 'analista/generado/unidades.jsonl'
DEFAULT_INPUT = ROOT / 'analista/generado/normalizados'
DEFAULT_OUTPUT = ROOT / 'analista/generado/verificados'

FILES=(
 'apariciones-conceptuales.jsonl','conceptos.jsonl','definiciones.jsonl',
 'afirmaciones-candidatas.jsonl','formulas-candidatas.jsonl',
 'relaciones-explicitas.jsonl','distinciones.jsonl','negaciones.jsonl',
 'excepciones.jsonl','restricciones-alcance.jsonl'
)
EXPECTED_PRODUCER={
 'aparicion_conceptual':('conceptos_apariciones','1.1.0'),
 'concepto':('conceptos_apariciones','1.1.0'),
 'definicion':('definiciones','1.1.0'),
 'afirmacion':('afirmaciones','1.1.0'),
 'formula':('formulas','1.1.0'),
 'relacion_explicita':('relaciones_explicitas','1.1.0'),
 'distincion':('limitadores','1.0.1'),
 'negacion':('limitadores','1.0.1'),
 'excepcion':('limitadores','1.0.1'),
 'restriccion_alcance':('limitadores','1.0.1'),
}


def load(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x]

def dump(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')

def file_lines(repo: Path, route: str, cache: dict[str,list[str]]) -> list[str]:
    if route not in cache:
        cache[route]=(repo/route).read_text(encoding='utf-8').splitlines()
    return cache[route]

def excerpt(repo: Path, loc: dict, cache: dict[str,list[str]]) -> str:
    lines=file_lines(repo,loc['ruta'],cache)
    s,e=loc['linea_inicio'],loc['linea_fin']
    if not isinstance(s,int) or not isinstance(e,int) or s<1 or e<s or e>len(lines):
        raise ValueError('rango')
    return '\n'.join(lines[s-1:e])

def literal_matches_excerpt(literal: str, ex: str) -> bool:
    """El rango puede incluir prefijo/sufijo de sus líneas extremas, nunca líneas completas extra."""
    if not literal:
        return False
    position=ex.find(literal)
    if position<0:
        return False
    before=ex[:position]
    after=ex[position+len(literal):]
    return '\n' not in before and '\n' not in after

def occurrences_with_line_span(unit: dict, literal: str) -> list[tuple[int,int]]:
    if not literal:
        return []
    text=unit['texto_literal']; base=unit['localizacion']['linea_inicio']; out=[]; start=0
    while True:
        pos=text.find(literal,start)
        if pos<0: break
        line_start=base+text[:pos].count('\n')
        line_end=line_start+literal.count('\n')
        out.append((line_start,line_end))
        start=pos+1
    return out

def literal_matches_unit_location(unit: dict, literal: str, loc: dict) -> bool:
    return (loc['linea_inicio'],loc['linea_fin']) in occurrences_with_line_span(unit,literal)

def producer_ok(record: dict) -> bool:
    t=record.get('tipo_registro')
    expected=EXPECTED_PRODUCER.get(t)
    return bool(expected and record.get('schema_version')=='1.0.0' and record.get('producido_por')=={'motor':expected[0],'version':expected[1]})

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo-root',type=Path,default=ROOT)
    ap.add_argument('--fuentes',type=Path,default=DEFAULT_FUENTES)
    ap.add_argument('--unidades',type=Path,default=DEFAULT_UNIDADES)
    ap.add_argument('--input-root',type=Path,default=DEFAULT_INPUT)
    ap.add_argument('--output-root',type=Path,default=DEFAULT_OUTPUT)
    a=ap.parse_args()

    sources={r['id']:r for r in load(a.fuentes)}
    units={r['id']:r for r in load(a.unidades)}
    allrows={name:load(a.input_root/name) for name in FILES}
    flat=[r for rows in allrows.values() for r in rows]
    id_counts=collections.Counter(r.get('id') for r in flat)
    apps={r['id']:r for r in allrows['apariciones-conceptuales.jsonl']}
    concepts={r['id']:r for r in allrows['conceptos.jsonl']}
    affirm={r['id']:r for r in allrows['afirmaciones-candidatas.jsonl']}
    cache={}

    used_sources={r.get('fuente_id') for r in flat if r.get('fuente_id')}
    source_ok: dict[str,bool]={}
    for sid in used_sources:
        s=sources.get(sid); ok=bool(s)
        try:
            if ok:
                canonical=a.repo_root/s['ruta_canonica']
                h=hashlib.sha256(canonical.read_bytes()).hexdigest()
                ok = (
                    s.get('schema_version')=='1.0.0'
                    and s.get('producido_por')=={'motor':'fuentes','version':'1.0.1'}
                    and h==s.get('sha256')
                    and s.get('version_fuente')==f'sha256:{h}'
                    and set(s.get('rutas_derivadas',[]))==set(s.get('segmentaciones',[]))
                )
        except Exception:
            ok=False
        source_ok[sid]=bool(ok)

    unit_cache: dict[str,bool]={}
    def verify_unit(uid: str) -> bool:
        if uid in unit_cache: return unit_cache[uid]
        u=units.get(uid); ok=bool(u)
        try:
            if ok:
                sid=u['fuente_id']; s=sources.get(sid); loc=u['localizacion']
                ok = (
                    u.get('schema_version')=='1.0.0'
                    and u.get('producido_por')=={'motor':'unidades','version':'1.0.0'}
                    and source_ok.get(sid,False)
                    and s is not None
                    and u['archivo']==loc['ruta']
                    and u['archivo'] in s.get('rutas_derivadas',[])
                    and excerpt(a.repo_root,loc,cache)==u['texto_literal']
                    and hashlib.sha256(u['texto_literal'].encode('utf-8')).hexdigest()==u['sha256_texto']
                )
        except Exception:
            ok=False
        unit_cache[uid]=bool(ok); return bool(ok)

    results: dict[str,bool]={}
    reasons: dict[str,list[str]]={}
    def fail(rid: str, reason: str) -> None:
        reasons.setdefault(rid,[]).append(reason)

    def common_direct(r: dict) -> tuple[bool,dict|None,dict|None,str]:
        rid=r.get('id',''); ok=True
        if id_counts[rid]!=1: fail(rid,'id_no_unico'); ok=False
        if not producer_ok(r): fail(rid,'version_o_productor'); ok=False
        sid=r.get('fuente_id'); uid=r.get('unidad_id')
        if not source_ok.get(sid,False): fail(rid,'fuente_o_hash'); ok=False
        if not verify_unit(uid): fail(rid,'unidad'); ok=False
        u=units.get(uid); s=sources.get(sid)
        try:
            loc=r['localizacion']
            excerpt(a.repo_root,loc,cache)
            if u is None or u.get('fuente_id')!=sid: fail(rid,'unidad_fuente'); ok=False
            if s is None or loc['ruta'] not in s.get('rutas_derivadas',[]): fail(rid,'ruta_fuera_fuente'); ok=False
            if u is None or loc['ruta']!=u.get('archivo'): fail(rid,'ruta_fuera_unidad'); ok=False
        except Exception:
            fail(rid,'rango'); ok=False
            loc={}
        return ok,u,s,rid

    for name,rows in allrows.items():
        if name=='conceptos.jsonl': continue
        for r in rows:
            ok,u,s,rid=common_direct(r); t=r['tipo_registro']; loc=r.get('localizacion',{})
            try:
                ex=excerpt(a.repo_root,loc,cache)
                if t=='aparicion_conceptual':
                    if r['texto_literal']!=r['forma_literal']: fail(rid,'literal_aparicion'); ok=False
                    if not literal_matches_unit_location(u,r['forma_literal'],loc): fail(rid,'ubicacion_aparicion'); ok=False
                    cid=r.get('concepto_id')
                    if cid is not None and cid not in concepts: fail(rid,'concepto_inexistente'); ok=False
                elif t=='definicion':
                    uloc=u['localizacion']
                    if not (uloc['linea_inicio']<=loc['linea_inicio']<=uloc['linea_fin']): fail(rid,'inicio_fuera_unidad'); ok=False
                    if not literal_matches_excerpt(r['texto_literal'],ex): fail(rid,'literal_definicion'); ok=False
                    if r.get('concepto_id') not in concepts: fail(rid,'concepto_inexistente'); ok=False
                elif t=='afirmacion':
                    uloc=u['localizacion']
                    if not (
                        uloc['linea_inicio'] <= loc['linea_inicio'] <= loc['linea_fin'] <= uloc['linea_fin']
                    ):
                        fail(rid,'rango_afirmacion'); ok=False
                    if not literal_matches_excerpt(r['texto_literal'],ex): fail(rid,'literal_afirmacion'); ok=False
                    if any(cid not in concepts for cid in r.get('concepto_ids',[])): fail(rid,'concepto_inexistente'); ok=False
                elif t=='formula':
                    if r['texto_literal']!=r['formula_literal']: fail(rid,'literal_formula'); ok=False
                    if not literal_matches_unit_location(u,r['formula_literal'],loc): fail(rid,'ubicacion_formula'); ok=False
                    for cuid in r.get('contexto_unidad_ids',[]):
                        if not verify_unit(cuid): fail(rid,'contexto_unidad'); ok=False; continue
                        cu=units[cuid]
                        if cu['fuente_id']!=r['fuente_id'] or cu['archivo']!=u['archivo']: fail(rid,'contexto_fuera_archivo'); ok=False
                    if u['id'] not in r.get('contexto_unidad_ids',[]): fail(rid,'contexto_sin_unidad'); ok=False
                elif t=='relacion_explicita':
                    if r['texto_literal']!=r['relacion_literal'] or not literal_matches_excerpt(r['relacion_literal'],ex): fail(rid,'literal_relacion'); ok=False
                    if r.get('sujeto_ref') not in concepts or r.get('objeto_ref') not in concepts: fail(rid,'referente_relacion'); ok=False
                elif t=='distincion':
                    if not literal_matches_unit_location(u,r['texto_literal'],loc): fail(rid,'ubicacion_distincion'); ok=False
                    if r['termino_a_literal'] not in r['texto_literal'] or r['termino_b_literal'] not in r['texto_literal']: fail(rid,'terminos_distincion'); ok=False
                    if r.get('marcador_literal') is not None and r['marcador_literal'] not in ex: fail(rid,'marcador_distincion'); ok=False
                elif t=='negacion':
                    if not literal_matches_unit_location(u,r['texto_literal'],loc): fail(rid,'ubicacion_negacion'); ok=False
                    if r['objeto_negado_literal'] not in ex: fail(rid,'objeto_negado'); ok=False
                    if r.get('alcance_literal') is not None and r['alcance_literal'] not in ex: fail(rid,'alcance_negacion'); ok=False
                elif t=='excepcion':
                    if r['texto_literal']!=r['fragmento_exceptivo_literal'] or not literal_matches_unit_location(u,r['texto_literal'],loc): fail(rid,'literal_excepcion'); ok=False
                    aid=r.get('afirmacion_limitada_id')
                    if aid is not None and aid not in affirm: fail(rid,'afirmacion_limitada'); ok=False
                elif t=='restriccion_alcance':
                    if r['texto_literal']!=r['fragmento_restriccion_literal'] or not literal_matches_unit_location(u,r['texto_literal'],loc): fail(rid,'literal_restriccion'); ok=False
                    aid=r.get('afirmacion_limitada_id')
                    if aid is not None and aid not in affirm: fail(rid,'afirmacion_limitada'); ok=False
            except Exception:
                fail(rid,'excepcion_verificacion'); ok=False
            results[rid]=bool(ok)

    for c in allrows['conceptos.jsonl']:
        rid=c['id']; ok=True
        if id_counts[rid]!=1: fail(rid,'id_no_unico'); ok=False
        if not producer_ok(c): fail(rid,'version_o_productor'); ok=False
        aids=c.get('aparicion_ids',[]); evid=c.get('evidencia_identidad_ids',[])
        if not aids or any(x not in apps for x in aids): fail(rid,'apariciones'); ok=False
        if any(x not in aids for x in evid): fail(rid,'evidencia_fuera_apariciones'); ok=False
        if any(not results.get(x,False) for x in aids): fail(rid,'aparicion_no_verificada'); ok=False
        if any(apps[x].get('concepto_id')!=rid for x in aids if x in apps): fail(rid,'vinculo_aparicion'); ok=False
        if c.get('estado_identidad_conceptual')=='establecida_por_evidencia':
            if not evid: fail(rid,'sin_evidencia_identidad'); ok=False
            if any(not results.get(x,False) for x in evid): fail(rid,'evidencia_no_verificada'); ok=False
        results[rid]=bool(ok)

    total=failed=0
    for name,rows in allrows.items():
        out=[]
        for original in rows:
            r=copy.deepcopy(original); verdict=results.get(r['id'],False)
            r['estado_verificacion']='verificado' if verdict else 'fallido'
            total+=1; failed+=not verdict; out.append(r)
        dump(a.output_root/name,out)

    print(json.dumps({'total':total,'verificados':total-failed,'fallidos':failed,'fuentes':source_ok,'unidades_comprobadas':len(unit_cache),'unidades_validas':sum(unit_cache.values())},ensure_ascii=False,sort_keys=True))
    if failed:
        for rid in sorted(reasons):
            print(f"FALLO {rid}: {','.join(reasons[rid])}")
    return 0 if failed==0 else 2

if __name__=='__main__':
    raise SystemExit(main())
