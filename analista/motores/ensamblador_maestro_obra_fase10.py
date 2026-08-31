#!/usr/bin/env python3
"""Ensamblador intraobra de Fase 10 v1.4; no compara ni sintetiza obras."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SCHEMA_VERSION="1.4.0"; MOTOR_VERSION="1.2.0"; CONTROL_VERSION="1.2.0"
FILES={"apariciones_conceptuales":"apariciones-conceptuales.jsonl","conceptos":"conceptos.jsonl","definiciones":"definiciones.jsonl","afirmaciones":"afirmaciones-candidatas.jsonl","formulas":"formulas-candidatas.jsonl","relaciones_explicitas":"relaciones-explicitas.jsonl","distinciones":"distinciones.jsonl","negaciones":"negaciones.jsonl","excepciones":"excepciones.jsonl","restricciones_alcance":"restricciones-alcance.jsonl"}
COVER=("cobertura-conceptos.jsonl","cobertura-definiciones.jsonl","cobertura-afirmaciones.jsonl","cobertura-formulas.jsonl","cobertura-relaciones.jsonl","cobertura-limitadores.jsonl")
MOTORS={"conceptos_apariciones","definiciones","afirmaciones","formulas","relaciones_explicitas","limitadores"}
FIXED={"conceptos_apariciones":"1.3.0","definiciones":"1.3.0","afirmaciones":"1.2.0","relaciones_explicitas":"1.2.0","limitadores":"1.1.0"}
DECLARATIVE_CRITERIA=("lema_en_glosario_tecnico_explicito","declaracion_designativa_explicita_en_cuerpo:")

def loadl(p:Path):
 if not p.is_file(): raise AssertionError(f"Insumo inexistente: {p}")
 return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x]
def loadj(p:Path):
 if not p.is_file(): raise AssertionError(f"Insumo inexistente: {p}")
 return json.loads(p.read_text(encoding="utf-8"))
def sha(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p:Path):
 try:return p.resolve().relative_to(ROOT.resolve()).as_posix()
 except ValueError:return p.resolve().as_posix()
def ids(rows): return [(r["id"],r["tipo_registro"]) for r in rows]
def declarative(app:dict)->bool:
 c=app.get("criterio_deteccion","")
 return c==DECLARATIVE_CRITERIA[0] or c.startswith(DECLARATIVE_CRITERIA[1])

def scope(manifest:dict)->dict:
 if manifest.get("version")!="1.4.0": raise AssertionError("Manifest Fase 10 incompatible")
 expected={"extraccion_conceptual_habilitada":True,"recuperacion_candidatos_habilitada":True,"identidad_confirmada_requiere_evidencia_explicita":True,"candidatos_sin_evidencia_permanecen_no_determinados":True,"identidades_conceptuales_inferidas":False,"glosario_interobra_reutilizado":False,"interpretacion_cero_registros":"no_autoriza_afirmar_ausencia_semantica"}
 if manifest.get("limitaciones_conceptuales")!=expected: raise AssertionError("Contrato conceptual del manifest no autorizado")
 profile=manifest.get("perfil_conceptual"); gloss=manifest.get("glosario_tecnico")
 if profile=="glosario_tecnico_explicito":
  if not isinstance(gloss,str) or not gloss: raise AssertionError("Perfil con glosario inconsistente")
 elif profile=="sin_glosario_tecnico_explicito":
  if gloss is not None: raise AssertionError("Perfil sin glosario inconsistente")
 else: raise AssertionError("Perfil conceptual no autorizado")
 return {"perfil":profile,"glosario_tecnico":gloss,**expected}

def versions(manifest:dict,root:Path)->dict:
 declared=manifest.get("versiones_extractores")
 if not isinstance(declared,dict) or set(declared)!=MOTORS: raise AssertionError("Versiones de extractores incompletas")
 for k,v in FIXED.items():
  if declared.get(k)!=v: raise AssertionError(f"Versión no autorizada de {k}")
 if not isinstance(declared.get("formulas"),str) or not declared["formulas"]: raise AssertionError("Versión de fórmulas ausente")
 by={"conceptos_apariciones":("apariciones-conceptuales.jsonl","conceptos.jsonl"),"definiciones":("definiciones.jsonl",),"afirmaciones":("afirmaciones-candidatas.jsonl",),"formulas":("formulas-candidatas.jsonl",),"relaciones_explicitas":("relaciones-explicitas.jsonl",),"limitadores":("distinciones.jsonl","negaciones.jsonl","excepciones.jsonl","restricciones-alcance.jsonl")}
 for motor,names in by.items():
  for name in names:
   for row in loadl(root/name):
    if row.get("producido_por")!={"motor":motor,"version":declared[motor]}: raise AssertionError(f"Productor no coincide: {name}/{row.get('id')}")
 return declared

def validate_traceability(m:dict)->None:
 obra=m.get("obra_id")
 if {x["id"] for x in m["fuentes"]}!={obra}: raise AssertionError("El maestro debe contener solo la fuente de su obra")
 units={x["id"]:x for x in m["unidades"]}
 if not units or any(x.get("fuente_id")!=obra for x in units.values()): raise AssertionError("Unidad fuera de obra")
 rows=[r for f in FILES for r in m[f]]
 if len({r["id"] for r in rows})!=len(rows): raise AssertionError("ID duplicado entre productos")
 apps={r["id"]:r for r in m["apariciones_conceptuales"]}; cons={r["id"]:r for r in m["conceptos"]}; aff={r["id"]:r for r in m["afirmaciones"]}
 for r in rows:
  if r.get("estado_verificacion")!="verificado" or r.get("estado_auditoria")!="auditado": raise AssertionError(f"Registro no sellado: {r.get('id')}")
  uid=r.get("unidad_id"); sid=r.get("fuente_id")
  if uid is not None and uid not in units: raise AssertionError(f"Unidad rota: {r['id']}")
  if sid is not None and sid!=obra: raise AssertionError(f"Fuente rota: {r['id']}")
  k=r["tipo_registro"]
  if k=="aparicion_conceptual" and r.get("concepto_id") is not None and r["concepto_id"] not in cons: raise AssertionError(f"Concepto inexistente: {r['id']}")
  if k=="concepto":
   aids=r.get("aparicion_ids",[]); ev=r.get("evidencia_identidad_ids",[])
   if not aids or any(a not in apps or apps[a].get("concepto_id")!=r["id"] for a in aids): raise AssertionError(f"Aparición rota: {r['id']}")
   state=r.get("estado_identidad_conceptual")
   if state=="establecida_por_evidencia":
    if r.get("estado_extraccion")!="extraido" or not ev or any(a not in aids for a in ev): raise AssertionError(f"Identidad establecida sin evidencia: {r['id']}")
    if any(not declarative(apps[a]) for a in ev): raise AssertionError(f"Evidencia no declarativa: {r['id']}")
   elif state=="no_determinada":
    if r.get("estado_extraccion")!="candidato" or ev: raise AssertionError(f"Candidato conceptual sobreclasificado: {r['id']}")
   else: raise AssertionError(f"Estado conceptual no autorizado: {r['id']}")
  if k=="definicion" and r.get("concepto_id") not in cons: raise AssertionError(f"Definición sin concepto: {r['id']}")
  if k=="afirmacion" and any(c not in cons for c in r.get("concepto_ids",[])): raise AssertionError(f"Afirmación con concepto inexistente: {r['id']}")
  if k=="formula" and (r.get("unidad_id") not in r.get("contexto_unidad_ids",[]) or any(u not in units for u in r.get("contexto_unidad_ids",[]))): raise AssertionError(f"Fórmula con contexto roto: {r['id']}")
  if k=="relacion_explicita":
   if r.get("sujeto_ref") not in cons or r.get("objeto_ref") not in cons: raise AssertionError(f"Relación con referente inexistente: {r['id']}")
   if r.get("clasificacion_relacion")=="relacion_explicita" and (cons[r["sujeto_ref"]].get("estado_identidad_conceptual")!="establecida_por_evidencia" or cons[r["objeto_ref"]].get("estado_identidad_conceptual")!="establecida_por_evidencia"): raise AssertionError(f"Relación explícita con identidad no determinada: {r['id']}")
  if k in {"excepcion","restriccion_alcance"} and r.get("afirmacion_limitada_id") is not None and r["afirmacion_limitada_id"] not in aff: raise AssertionError(f"Limitador con afirmación inexistente: {r['id']}")
 for h in m["hallazgos_auditoria"]:
  if h.get("resolucion_doctrinal")!="no_realizada" or h.get("estado_verificacion")!="verificado" or h.get("estado_auditoria")!="auditado": raise AssertionError(f"Hallazgo doctrinal/no sellado: {h.get('id')}")
 cov=m["reportes_cobertura"]
 if {x["motor"] for x in cov}!=MOTORS: raise AssertionError("Cobertura incompleta")
 for x in cov:
  if x.get("obra_id")!=obra or x.get("unidades_totales")!=len(units) or x.get("unidades_procesadas")!=len(units) or x.get("unidades_omitidas") or x.get("errores"): raise AssertionError(f"Cobertura inválida: {x.get('id')}")
 c=m["controles_fase10"]
 if c.get("version")!=CONTROL_VERSION or c.get("obra_id")!=obra or c.get("comparacion_interobra") is not False: raise AssertionError("Controles Fase 10 inválidos")
 for k in ("maestro_independiente","normalizacion_recuperacion","verificacion_evidencia","auditoria_intraobra"):
  if c.get(k) is not True: raise AssertionError(f"Control no satisfecho: {k}")
 sc=c.get("alcance_conceptual",{})
 if sc.get("extraccion_conceptual_habilitada") is not True or sc.get("identidades_conceptuales_inferidas") is not False or sc.get("glosario_interobra_reutilizado") is not False: raise AssertionError("Alcance conceptual inválido")

def hist(rows):
 out=[{"version":f"{a}/{b}","descripcion":"Versión declarada por un producto incluido en el expediente."} for a,b in sorted({(r["producido_por"]["motor"],r["producido_por"]["version"]) for r in rows if r.get("producido_por")})]
 out += [{"version":"normalizacion/1.0.0","descripcion":"Overlay de recuperación sin alterar evidencia."},{"version":"expediente-maestro-fase10/1.4.0","descripcion":"Maestro independiente con recuperación conceptual en todas las obras."},{"version":"ensamblador_maestro_obra_fase10/1.2.0","descripcion":"Ensamblador descriptivo intraobra."}]
 seen=set(); return [x for x in sorted(out,key=lambda z:z["version"]) if not (x["version"] in seen or seen.add(x["version"]))]

def assemble(obra:str,root:Path,output:Path)->dict:
 root=root.resolve(); manifest=loadj(root/"manifest-extractores.json")
 if manifest.get("obra_id")!=obra or manifest.get("comparacion_interobra") is not False: raise AssertionError("Manifest ajeno o interobra")
 sc=scope(manifest); versions(manifest,root)
 src=[x for x in loadl(root/"fuente.jsonl") if x.get("id")==obra]; units=[x for x in loadl(root/"unidades.jsonl") if x.get("fuente_id")==obra]
 if len(src)!=1 or not units: raise AssertionError("Fuente/unidades inválidas")
 units.sort(key=lambda x:x["orden_textual"]); specs=[(root/"fuente.jsonl","fuente",1),(root/"unidades.jsonl","unidades",len(units)),(root/"manifest-extractores.json","manifest",1)]
 declared=manifest.get("productos",{}); arrays={}
 for field,name in FILES.items():
  raw=root/name; norm=root/"normalizados"/name; ver=root/"verificados"/name; aud=root/"auditados"/name
  rr,nr,vr,ar=map(loadl,(raw,norm,ver,aud))
  if declared.get(name)!=sha(raw): raise AssertionError(f"Hash extraído no coincide: {name}")
  if not (ids(rr)==ids(nr)==ids(vr)==ids(ar)): raise AssertionError(f"Cadena alteró identidad: {name}")
  arrays[field]=ar; specs += [(raw,"producto_extraido",len(rr)),(norm,"producto_normalizado",len(nr)),(ver,"producto_verificado",len(vr)),(aud,"producto_auditado",len(ar))]
 findings=loadl(root/"hallazgos-auditoria.jsonl"); specs.append((root/"hallazgos-auditoria.jsonl","hallazgos",len(findings)))
 cov=[]
 for name in COVER:
  p=root/name
  if declared.get(name)!=sha(p): raise AssertionError(f"Hash cobertura no coincide: {name}")
  rr=[x for x in loadl(p) if x.get("obra_id")==obra]
  if len(rr)!=1: raise AssertionError(f"Cobertura inválida: {name}")
  cov+=rr; specs.append((p,"cobertura",1))
 cal=manifest.get("calibracion",{}).get("formulas",{}); profile=cal.get("perfil")
 if profile:
  pp=ROOT/profile
  if not pp.is_file() or cal.get("perfil_sha256")!=sha(pp): raise AssertionError("Perfil de fórmulas inválido")
  specs.append((pp,"calibracion_obra",1))
 allrows=src+units+[r for x in arrays.values() for r in x]+findings+cov
 trace=sorted([{"ruta":rel(p),"sha256":sha(p),"funcion":f,"registros_incluidos":n} for p,f,n in specs],key=lambda x:x["ruta"])
 m={"id":f"MAE-{obra}","tipo_registro":"expediente_maestro_obra","schema_version":SCHEMA_VERSION,"texto_literal":None,"normalizacion_formal":None,"normalizacion_lexica":None,"estatus_enunciativo":None,"estado_extraccion":"extraido","estado_verificacion":"verificado","estado_auditoria":"no_aplica","producido_por":{"motor":"ensamblador_maestro_obra_fase10","version":MOTOR_VERSION},"obra_id":obra,"titulo":src[0]["titulo"],"fuentes":src,"unidades":units,**arrays,"hallazgos_auditoria":findings,"reportes_cobertura":sorted(cov,key=lambda x:x["motor"]),"controles_fase10":{"version":CONTROL_VERSION,"obra_id":obra,"fase":10,"comparacion_interobra":False,"maestro_independiente":True,"normalizacion_recuperacion":True,"verificacion_evidencia":True,"auditoria_intraobra":True,"alcance_conceptual":sc,"calibracion_formulas":{"perfil_calibrado":bool(cal.get("perfil_calibrado",False)),"version_produccion":cal.get("version_produccion"),"perfil":profile,"perfil_sha256":cal.get("perfil_sha256")}},"trazabilidad_archivos":trace,"historial_versiones":hist(allrows)}
 validate_traceability(m); output.parent.mkdir(parents=True,exist_ok=True)
 payload=(json.dumps(m,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode(); output.write_bytes(payload)
 digest=hashlib.sha256(payload).hexdigest(); output.with_suffix(output.suffix+".sha256").write_text(f"{digest}  {output.name}\n",encoding="utf-8")
 return m

def main():
 p=argparse.ArgumentParser();p.add_argument("--obra-id",required=True);p.add_argument("--obra-root",type=Path);p.add_argument("--output",type=Path);a=p.parse_args()
 root=a.obra_root or ROOT/"analista/generado/obras"/a.obra_id;out=a.output or ROOT/"analista/generado/maestros"/f"{a.obra_id}.json"
 m=assemble(a.obra_id,root,out); print(json.dumps({"obra_id":a.obra_id,"unidades":len(m["unidades"]),"registros_auditados":sum(len(m[k]) for k in FILES),"hallazgos":len(m["hallazgos_auditoria"]),"comparacion_interobra":False,"salida":rel(out)},ensure_ascii=False,sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
