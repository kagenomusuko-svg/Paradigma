#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, re, unicodedata
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUENTES = ROOT / 'analista/generado/fuentes.jsonl'
UNIDADES = ROOT / 'analista/generado/unidades.jsonl'
CONCEPTOS = ROOT / 'analista/generado/conceptos.jsonl'
SALIDA = ROOT / 'analista/generado/definiciones.jsonl'
COBERTURA = ROOT / 'analista/generado/cobertura-definiciones.jsonl'
PILOTO_ID='AA-SP-V1'; SCHEMA_VERSION='1.0.0'; MOTOR_VERSION='1.1.0'
ROMAN_RE=re.compile(r'^[IVXLCDM]+$'); ARROW_RE=re.compile(r'^\s*→'); SPACE_RE=re.compile(r'\s+')
PREAMBULO=('los términos ','sistema.','introducido ')


def norm(text:str)->str:
    return SPACE_RE.sub(' ',unicodedata.normalize('NFKC',text).casefold()).strip()

def sid(prefix:str,*parts:str)->str:
    raw='\x1f'.join(parts).encode('utf-8'); return f'{prefix}-{hashlib.sha1(raw).hexdigest()[:12].upper()}'

def load_jsonl(path:Path)->list[dict]:
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line]

def dump_jsonl(path:Path,rows:list[dict])->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')

def parse_glossary(path:Path)->list[dict]:
    lines=path.read_text(encoding='utf-8').splitlines(); rel=path.relative_to(ROOT).as_posix()
    i=next((n for n,line in enumerate(lines) if 'glosario' in norm(line)),None)
    if i is None: raise SystemExit('Glosario sin encabezado')
    i+=1; out=[]
    while i<len(lines):
        candidate=lines[i].strip()
        if not candidate or candidate.startswith('#') or ROMAN_RE.fullmatch(candidate) or norm(candidate).startswith(PREAMBULO):
            i+=1; continue
        term=candidate; term_line=i+1; i+=1; content=[]; arrow=None
        while i<len(lines):
            current=lines[i].strip()
            if ARROW_RE.match(current): arrow=i+1; i+=1; break
            if current and not current.startswith('#') and not ROMAN_RE.fullmatch(current): content.append((i+1,current))
            i+=1
        if not content or arrow is None: continue
        start,end=content[0][0],content[-1][0]; legacy_flat=' '.join(text for _,text in content)
        out.append({'lema':term,'linea_inicio':start,'linea_fin':end,'texto_literal':'\n'.join(lines[start-1:end]),'id':sid('DEF',rel,str(term_line),term,legacy_flat)})
    return out

def base(record_id:str, kind:str, literal:str|None, audit:str, *, status:str|None=None, extraction:str='extraido')->dict:
    return {'id':record_id,'tipo_registro':kind,'schema_version':SCHEMA_VERSION,'texto_literal':literal,
            'normalizacion_formal':None,'normalizacion_lexica':None,'estatus_enunciativo':status,
            'estado_extraccion':extraction,'estado_verificacion':'pendiente','estado_auditoria':audit,
            'producido_por':{'motor':'definiciones','version':MOTOR_VERSION}}

def term_regex(name:str)->str:
    parts=name.split()
    core=r'\s+'.join(re.escape(p) for p in parts)
    return rf'(?<![\w\-‐‑])(?:{core})(?![\w\-‐‑])'

@dataclass(frozen=True)
class Rule:
    name:str; regex:re.Pattern[str]; classification:str; status:str; priority:int; fixed_concept:str|None=None


def build_rules(concepts:list[dict])->tuple[list[Rule],dict[str,dict]]:
    by_norm={norm(c['designacion_operativa']):c for c in concepts}
    names=sorted((c['designacion_operativa'] for c in concepts),key=len,reverse=True)
    alt='(?:'+'|'.join(term_regex(n) for n in names)+')'
    def R(name, pattern, classification, status, priority, fixed=None):
        return Rule(name,re.compile(pattern,re.I|re.S),classification,status,priority,fixed)
    rules=[
      R('condicional_estado',rf'Si\s+(?:el|la)\s+(?P<c>{alt})\s+es\s+el\s+estado(?:(?![,.;:]).){{1,180}}','definicion_candidata','formulacion_condicional',100),
      R('caos_definicion_negativa',rf'(?:el|la)\s+(?P<c>{alt})\s+no\s+está(?:(?!\.).)*\.\s+No\s+(?:(?!\.).)*\.\s+Es\s+(?:(?!\.).)*\.','definicion_explicita','definicion',100),
      R('aposicion_fuerza',rf'(?:el|la)\s+(?P<c>{alt})\s*:\s*la\s+fuerza\s+que(?:(?!\.).)*\.','definicion_explicita','definicion',100),
      R('sistema_no_es',rf'Para\s+este\s+sistema,\s+(?:el|la)\s+(?P<c>{alt})\s+no(?:(?!:).){{1,180}}:\s+es\s+(?:(?!\.).)*\.','definicion_explicita','definicion',100),
      R('phi2_formal',r'φ₂:\s+la\s+segunda\s+mediación\s+es\s+(?:(?!\.).)*\.','definicion_explicita','definicion',100,'φ₂ — Segunda mediación'),
      R('orientacion_pasion',rf'la\s+tendencia(?:(?!\.).){{1,260}}\.\s+Esa\s+orientación\s+es\s+su\s+(?P<c>{alt})','definicion_candidata','afirmacion_autoral',90),
      R('iteracion_produce',rf'la\s+iteración\s+de\s+la\s+(?:{alt})\s+describe:\s+cada\s+ciclo\s+produce\s+un\s+(?P<c>{alt})\s+que\s+es\s+(?:(?!,).){{1,180}}','definicion_candidata','afirmacion_autoral',90),
      R('existe_como',rf'(?:el|la)\s+(?P<c>{alt})\s+existe\s+como\s+(?:(?![,.;]).){{1,180}}','definicion_candidata','afirmacion_autoral',90),
      R('no_es_algo',rf'(?:El|La|el|la)\s+(?P<c>{alt})\s+no\s+es\s+algo(?:(?!:).){{1,180}}:\s+es\s+algo(?:(?!\.).)*\.','definicion_candidata','afirmacion_autoral',90),
      R('aposicion_candidata',rf'(?:el|la)\s+(?P<c>{alt})\s*:\s*(?:el|la)\s+(?:(?!\.).)*\.','definicion_candidata','no_determinado',40),
    ]
    return rules,by_norm

def concept_from_surface(surface:str,by_norm:dict[str,dict])->dict|None:
    return by_norm.get(norm(surface))

def range_for(unit:dict,text:str,start:int,end:int)->tuple[int,int]:
    first=unit['localizacion']['linea_inicio']+text[:start].count('\n')
    literal=text[start:end]
    return first,first+literal.count('\n')

def main()->int:
    fuentes,unidades,conceptos=load_jsonl(FUENTES),load_jsonl(UNIDADES),load_jsonl(CONCEPTOS)
    fuente=next(r for r in fuentes if r['id']==PILOTO_ID)
    glosarios=[r for r in fuente['rutas_derivadas'] if r.endswith('99-glosario.md')]
    if len(glosarios)!=1: raise SystemExit(f'Glosario ambiguo: {glosarios}')
    glosario_rel=glosarios[0]; entries=parse_glossary(ROOT/glosario_rel)
    pilot_units=[u for u in unidades if u['fuente_id']==PILOTO_ID]
    concepts_by_term={c['designacion_operativa']:c for c in conceptos}
    definitions=[]; seen=set()
    for entry in entries:
        concept=concepts_by_term.get(entry['lema'])
        if concept is None: raise SystemExit(f"Lema sin concepto 4A: {entry['lema']}")
        containers=[u for u in pilot_units if u['archivo']==glosario_rel and u['localizacion']['linea_inicio']<=entry['linea_inicio']<=u['localizacion']['linea_fin']]
        if len(containers)!=1: raise SystemExit(f"Inicio sin unidad única: {entry['lema']}")
        rec=base(entry['id'],'definicion',entry['texto_literal'],'pendiente',status='definicion',extraction='extraido')
        rec.update({'fuente_id':PILOTO_ID,'unidad_id':containers[0]['id'],'concepto_id':concept['id'],
                    'clasificacion_definicion':'definicion_explicita',
                    'localizacion':{'ruta':glosario_rel,'linea_inicio':entry['linea_inicio'],'linea_fin':entry['linea_fin']},
                    'criterio_deteccion':'entrada_de_glosario_bajo_declaracion_explicita_de_definicion_tecnica'})
        definitions.append(rec); seen.add((rec['unidad_id'],rec['concepto_id'],rec['texto_literal'],entry['linea_inicio'],entry['linea_fin']))
    rules,by_norm=build_rules(conceptos)
    for unit in pilot_units:
        if unit['archivo']==glosario_rel or unit.get('tipo_estructural')=='encabezado': continue
        text=unit['texto_literal']; candidates=[]
        for rule in rules:
            for match in rule.regex.finditer(text):
                concept=concepts_by_term.get(rule.fixed_concept) if rule.fixed_concept else concept_from_surface(match.group('c'),by_norm)
                if concept is None: continue
                candidates.append((match.start(),match.end(),-rule.priority,rule,concept))
        candidates.sort(key=lambda row:(row[0],row[2],-(row[1]-row[0]),row[4]['id']))
        selected=[]
        for start,end,negprio,rule,concept in candidates:
            if any(prior[4]['id']==concept['id'] and not (end<=prior[0] or start>=prior[1]) for prior in selected):
                continue
            selected.append((start,end,negprio,rule,concept))
        for start,end,_,rule,concept in selected:
            literal=text[start:end]; line_start,line_end=range_for(unit,text,start,end)
            key=(unit['id'],concept['id'],literal,line_start,line_end)
            if key in seen: continue
            record_id=sid('DEF',unit['archivo'],str(line_start),str(line_end),concept['designacion_operativa'],literal)
            extraction='extraido' if rule.classification=='definicion_explicita' else 'candidato'
            rec=base(record_id,'definicion',literal,'pendiente',status=rule.status,extraction=extraction)
            rec.update({'fuente_id':PILOTO_ID,'unidad_id':unit['id'],'concepto_id':concept['id'],
                        'clasificacion_definicion':rule.classification,
                        'localizacion':{'ruta':unit['archivo'],'linea_inicio':line_start,'linea_fin':line_end},
                        'criterio_deteccion':f'estructura_definicional_{rule.name}_sin_fusion_conceptual'})
            definitions.append(rec); seen.add(key)
    definitions.sort(key=lambda r:(r['localizacion']['ruta'],r['localizacion']['linea_inicio'],r['localizacion']['linea_fin'],r['id']))
    dump_jsonl(SALIDA,definitions)
    cov=base(sid('COB',PILOTO_ID,'definiciones',MOTOR_VERSION),'reporte_cobertura',None,'no_aplica',status=None,extraction='extraido')
    cov.update({'obra_id':PILOTO_ID,'motor':'definiciones','version_motor':MOTOR_VERSION,
                'unidades_totales':len(pilot_units),'unidades_procesadas':len(pilot_units),'unidades_omitidas':[],'errores':[]})
    dump_jsonl(COBERTURA,[cov])
    print(f'Fase 4B v{MOTOR_VERSION}: {len(definitions)} registros = {sum(r["clasificacion_definicion"]=="definicion_explicita" for r in definitions)} explícitos + {sum(r["clasificacion_definicion"]=="definicion_candidata" for r in definitions)} candidatos; {len(pilot_units)} unidades.')
    return 0
if __name__=='__main__': raise SystemExit(main())
