#!/usr/bin/env python3
"""Gate E2E intraobra de Fase 10 v1.4; no realiza comparación interobra."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
ROOT=Path(__file__).resolve().parents[2]
FUENTES=ROOT/"analista/generado/fuentes.jsonl"; UNIDADES=ROOT/"analista/generado/unidades.jsonl"
OLD=ROOT/"analista/esquema/contratos-v1.0.0.schema.json"; MASTER_SCHEMA=ROOT/"analista/esquema/expediente-maestro-fase10-v1.4.1.schema.json"
EX=ROOT/"analista/motores/ejecutar_extractores_obra_fase10.py"; NORM=ROOT/"analista/motores/normalizacion.py"; VER=ROOT/"analista/motores/verificador_evidencia.py"; IDV=ROOT/"analista/motores/validador_identidad_fase10.py"; AUD=ROOT/"analista/motores/auditor_estructural.py"; DESC=ROOT/"analista/motores/auditor_descriptivo_fase10.py"; ASM=ROOT/"analista/motores/ensamblador_maestro_obra_fase10.py"
PILOT="AA-SP-V1"
PRODUCT={"apariciones-conceptuales.jsonl":"aparicion_conceptual","conceptos.jsonl":"concepto","definiciones.jsonl":"definicion","afirmaciones-candidatas.jsonl":"afirmacion","formulas-candidatas.jsonl":"formula","relaciones-explicitas.jsonl":"relacion_explicita","distinciones.jsonl":"distincion","negaciones.jsonl":"negacion","excepciones.jsonl":"excepcion","restricciones-alcance.jsonl":"restriccion_alcance"}
FIELD={"apariciones-conceptuales.jsonl":"apariciones_conceptuales","conceptos.jsonl":"conceptos","definiciones.jsonl":"definiciones","afirmaciones-candidatas.jsonl":"afirmaciones","formulas-candidatas.jsonl":"formulas","relaciones-explicitas.jsonl":"relaciones_explicitas","distinciones.jsonl":"distinciones","negaciones.jsonl":"negaciones","excepciones.jsonl":"excepciones","restricciones-alcance.jsonl":"restricciones_alcance"}
COVER=("cobertura-conceptos.jsonl","cobertura-definiciones.jsonl","cobertura-afirmaciones.jsonl","cobertura-formulas.jsonl","cobertura-relaciones.jsonl","cobertura-limitadores.jsonl")
MOTORS={"conceptos_apariciones","definiciones","afirmaciones","formulas","relaciones_explicitas","limitadores"}; FIXED={"conceptos_apariciones":"1.3.1","definiciones":"1.3.0","afirmaciones":"1.2.0","relaciones_explicitas":"1.2.1","limitadores":"1.1.1"}

def loadl(p):
 if not Path(p).is_file(): raise AssertionError(f"Falta JSONL: {p}")
 return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(*args):subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,check=True)
def atomic(schema,name):return Draft202012Validator({"$schema":schema["$schema"],"$defs":schema["$defs"],"$ref":f"#/$defs/{name}"})
def assembler():
 s=importlib.util.spec_from_file_location("asm_f10",ASM);assert s and s.loader;m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def declarative(app):
 criterion=app.get("criterio_deteccion","")
 return criterion=="lema_en_glosario_tecnico_explicito" or criterion.startswith("declaracion_designativa_explicita_en_cuerpo:")

def execute(obra,root,master):
 run(EX,"--obra-id",obra,"--fuentes",FUENTES,"--unidades",UNIDADES,"--output-root",root)
 run(NORM,"--input-root",root,"--output-root",root/"normalizados")
 man=json.loads((root/"manifest-extractores.json").read_text(encoding="utf-8")); versions=man.get("versiones_extractores",{})
 if set(versions)!=MOTORS:raise AssertionError("Manifest sin seis versiones")
 cmd=[str(VER),"--repo-root",str(ROOT),"--fuentes",str(root/"fuente.jsonl"),"--unidades",str(root/"unidades.jsonl"),"--input-root",str(root/"normalizados"),"--output-root",str(root/"verificados")]
 for motor in ("conceptos_apariciones","definiciones","afirmaciones","formulas","relaciones_explicitas","limitadores"):
  cmd += ["--producer-version",f"{motor}={versions[motor]}"]
 run(*cmd);run(IDV,"--obra-id",obra,"--conceptos",root/"verificados"/"conceptos.jsonl","--apariciones",root/"verificados"/"apariciones-conceptuales.jsonl");run(AUD,"--input-root",root/"verificados","--output-root",root/"auditados","--unidades",root/"unidades.jsonl");run(DESC,"--input-root",root/"auditados","--output",root/"hallazgos-auditoria.jsonl","--obra-id",obra);run(ASM,"--obra-id",obra,"--obra-root",root,"--output",master)

def outputs(root,master):return [root/"fuente.jsonl",root/"unidades.jsonl",root/"manifest-extractores.json",root/"hallazgos-auditoria.jsonl",*[root/x for x in PRODUCT],*[root/x for x in COVER],*[root/l/x for l in ("normalizados","verificados","auditados") for x in PRODUCT],master,master.with_suffix(master.suffix+".sha256")]

def validate(obra,root,master):
 sources=loadl(FUENTES);units=loadl(UNIDADES);src=[x for x in sources if x.get("id")==obra];wu=[x for x in units if x.get("fuente_id")==obra]
 assert len(src)==1 and wu and loadl(root/"fuente.jsonl")==src and loadl(root/"unidades.jsonl")==wu
 man=json.loads((root/"manifest-extractores.json").read_text(encoding="utf-8"));assert man["version"]=="1.4.0" and man["obra_id"]==obra and man["titulo"]==src[0]["titulo"] and man["unidades"]==len(wu) and man["comparacion_interobra"] is False
 gloss=[x for x in src[0].get("rutas_derivadas",[]) if str(x).endswith("99-glosario.md")];assert len(gloss)<=1; has=bool(gloss);profile="glosario_tecnico_explicito" if has else "sin_glosario_tecnico_explicito";assert man["perfil_conceptual"]==profile and man["glosario_tecnico"]==(gloss[0] if has else None)
 expected={"extraccion_conceptual_habilitada":True,"recuperacion_candidatos_habilitada":True,"identidad_confirmada_requiere_evidencia_explicita":True,"candidatos_sin_evidencia_permanecen_no_determinados":True,"identidades_conceptuales_inferidas":False,"glosario_interobra_reutilizado":False,"interpretacion_cero_registros":"no_autoriza_afirmar_ausencia_semantica"};assert man["limitaciones_conceptuales"]==expected
 versions=man["versiones_extractores"];assert set(versions)==MOTORS
 for k,v in FIXED.items():assert versions[k]==v
 assert isinstance(versions["formulas"],str) and versions["formulas"]
 for name,digest in man["productos"].items():assert (root/name).is_file() and sha(root/name)==digest
 schema=json.loads(OLD.read_text(encoding="utf-8"));Draft202012Validator.check_schema(schema)
 raw_by={}; aud_by={}
 for name,defn in PRODUCT.items():
  layers=[loadl(root/name),loadl(root/"normalizados"/name),loadl(root/"verificados"/name),loadl(root/"auditados"/name)]; ids=[[r["id"] for r in x] for x in layers];assert ids[0]==ids[1]==ids[2]==ids[3]
  v=atomic(schema,defn)
  for li,rows in enumerate(layers):
   for r in rows:
    errs=list(v.iter_errors(r));assert not errs,(name,r.get("id"),errs[0].message if errs else "")
    if r.get("fuente_id") is not None:assert r["fuente_id"]==obra
   if li==2:assert all(r["estado_verificacion"]=="verificado" for r in rows)
   if li==3:assert all(r["estado_verificacion"]=="verificado" and r["estado_auditoria"]=="auditado" for r in rows)
  for a,b in zip(layers[0],layers[1],strict=True):
   aa=copy.deepcopy(a);bb=copy.deepcopy(b)
   for k in ("normalizacion_formal","normalizacion_lexica"):aa.pop(k,None);bb.pop(k,None)
   assert aa==bb
  raw_by[name]=layers[0];aud_by[name]=layers[3]
 apps={r["id"]:r for r in raw_by["apariciones-conceptuales.jsonl"]};cons=raw_by["conceptos.jsonl"]
 for c in cons:
  aids=c["aparicion_ids"];ev=c["evidencia_identidad_ids"];assert aids and all(a in apps and apps[a].get("concepto_id")==c["id"] for a in aids)
  if c["estado_identidad_conceptual"]=="establecida_por_evidencia":
   assert c["estado_extraccion"]=="extraido" and ev and all(a in aids and declarative(apps[a]) for a in ev)
   assert all(apps[a]["fuente_id"]==obra and apps[a]["unidad_id"] in {u["id"] for u in wu} for a in ev)
  else:assert c["estado_identidad_conceptual"]=="no_determinada" and c["estado_extraccion"]=="candidato" and ev==[]
 cov=[];cv=atomic(schema,"reporte_cobertura")
 for name in COVER:
  rows=loadl(root/name);assert len(rows)==1 and not list(cv.iter_errors(rows[0]));r=rows[0];assert r["obra_id"]==obra and r["unidades_totales"]==r["unidades_procesadas"]==len(wu) and not r["unidades_omitidas"] and not r["errores"];cov.append(r)
 assert {r["motor"] for r in cov}==MOTORS
 findings=loadl(root/"hallazgos-auditoria.jsonl");fv=atomic(schema,"hallazgo_auditoria")
 for h in findings:assert not list(fv.iter_errors(h)) and h["obra_id"]==obra and h["resolucion_doctrinal"]=="no_realizada"
 m=json.loads(master.read_text(encoding="utf-8"));ms=json.loads(MASTER_SCHEMA.read_text(encoding="utf-8"));Draft202012Validator.check_schema(ms);reg=Registry().with_resource(schema["$id"],Resource.from_contents(schema));errs=list(Draft202012Validator(ms,registry=reg).iter_errors(m));assert not errs,errs[0].message if errs else ""
 assert m["schema_version"]=="1.4.1" and m["producido_por"]=={"motor":"ensamblador_maestro_obra_fase10","version":"1.2.2"} and m["obra_id"]==obra and m["fuentes"]==src and m["unidades"]==sorted(wu,key=lambda x:x["orden_textual"])
 c=m["controles_fase10"];assert c["version"]=="1.2.0" and c["comparacion_interobra"] is False and c["alcance_conceptual"]=={"perfil":profile,"glosario_tecnico":gloss[0] if has else None,**expected}
 for name,field in FIELD.items():assert m[field]==aud_by[name]
 assert m["hallazgos_auditoria"]==findings and {r["motor"] for r in m["reportes_cobertura"]}==MOTORS
 assembler().validate_traceability(m)
 trace=m["trazabilidad_archivos"];funcs={r["funcion"] for r in trace};assert "producto_extraido" in funcs and "producto_normalizado" in funcs and "producto_verificado" in funcs and "producto_auditado" in funcs
 for e in trace:
  p=Path(e["ruta"]);p=p if p.is_absolute() else ROOT/p;assert p.is_file() and sha(p)==e["sha256"]
 side=master.with_suffix(master.suffix+".sha256");digest,name=side.read_text(encoding="utf-8").strip().split("  ",1);assert name==master.name and digest==sha(master)
 return {"obra_id":obra,"titulo":src[0]["titulo"],"unidades":len(wu),"perfil_conceptual":profile,"conceptos":len(m["conceptos"]),"identidades_establecidas":sum(x["estado_identidad_conceptual"]=="establecida_por_evidencia" for x in m["conceptos"]),"hallazgos":len(findings),"maestro_sha256":sha(master)}

def main():
 p=argparse.ArgumentParser();p.add_argument("--obra-id",required=True);a=p.parse_args();assert a.obra_id!=PILOT,"El piloto conserva Fase 9";root=ROOT/"analista/generado/obras"/a.obra_id;master=ROOT/"analista/generado/maestros"/f"{a.obra_id}.json";execute(a.obra_id,root,master);r=validate(a.obra_id,root,master);paths=outputs(root,master);first={str(p):p.read_bytes() for p in paths};execute(a.obra_id,root,master);second={str(p):p.read_bytes() for p in paths};assert first==second,f"{a.obra_id}: cadena no byte-reproducible";print(json.dumps({"fase":10,"estado":"obra_validada","segunda_ejecucion":"byte_identica_a_producto_validado",**r},ensure_ascii=False,sort_keys=True));return 0
if __name__=="__main__":raise SystemExit(main())