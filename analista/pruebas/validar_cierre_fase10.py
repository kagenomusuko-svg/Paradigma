#!/usr/bin/env python3
"""Gate global y reproducible de cierre administrativo de Fase 10 v1.2.

Solo emite ``fase10_cerrada=true`` después de ejecutar y validar de forma
independiente las veinte obras previstas. No compara contenidos entre obras ni
produce síntesis doctrinal. La presencia de glosario es un rasgo editorial, no
un requisito para que evidencia explícita de la propia obra establezca identidad.
"""
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
INVENTORY_ENGINE=ROOT/"analista/motores/inventariar_obras_fase10.py"; INVENTORY_VALIDATOR=ROOT/"analista/pruebas/validar_inventario_fase10.py"; WORK_VALIDATOR=ROOT/"analista/pruebas/validar_obra_fase10.py"; PILOT_VALIDATOR=ROOT/"analista/pruebas/validar_maestro_fase9.py"
INVENTORY=ROOT/"analista/generado/fase10/inventario-obras.json"; MASTERS=ROOT/"analista/generado/maestros"; REPORT=ROOT/"analista/generado/fase10/cierre-fase10.json"
PILOT="AA-SP-V1"; VERSION="1.2.0"

def run(cmd): subprocess.run(cmd,cwd=ROOT,check=True)
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def conceptual_counts(master):
 rows=master.get("conceptos",[])
 return {"total":len(rows),"establecida_por_evidencia":sum(r.get("estado_identidad_conceptual")=="establecida_por_evidencia" for r in rows),"no_determinada":sum(r.get("estado_identidad_conceptual")=="no_determinada" for r in rows)}

def main()->int:
 run([sys.executable,str(INVENTORY_ENGINE)]); run([sys.executable,str(INVENTORY_VALIDATOR)])
 inventory=json.loads(INVENTORY.read_text(encoding="utf-8")); works=inventory["obras"]
 assert inventory["version"]=="1.1.0" and inventory["alcance_estado"]=="inventario_no_certifica_cierres_de_fase"
 assert len(works)==inventory["fuentes"]==20; assert inventory["obras_con_glosario"]==8 and inventory["obras_sin_glosario"]==12 and inventory["piloto_id"]==PILOT
 ids=[w["obra_id"] for w in works]; assert len(ids)==len(set(ids))==20 and ids.count(PILOT)==1
 assert all(w["estado_verificado"]=="no_verificado_por_inventario" for w in works)

 # El cierre del piloto se afirma aquí solo después de ejecutar su validador de Fase 9.
 run([sys.executable,str(PILOT_VALIDATOR)])
 # El orden de ejecución no tiene significado documental. Para fallar pronto
 # durante la construcción se validan primero las obras más pequeñas; el cierre
 # y su reporte conservan después el orden canónico del inventario.
 execution_order=sorted((w for w in works if w["obra_id"]!=PILOT),key=lambda w:(w["unidades"],w["obra_id"]))
 for work in execution_order:
  run([sys.executable,str(WORK_VALIDATOR),"--obra-id",work["obra_id"]])

 expected={f"{oid}.json" for oid in ids}; found={p.name for p in MASTERS.glob("*.json")}; assert found==expected,{"faltantes":sorted(expected-found),"extras":sorted(found-expected)}
 closure=[]
 for work in works:
  oid=work["obra_id"]; mp=MASTERS/f"{oid}.json"; side=mp.with_suffix(mp.suffix+".sha256"); assert mp.is_file() and side.is_file()
  master=json.loads(mp.read_text(encoding="utf-8")); assert master["tipo_registro"]=="expediente_maestro_obra" and master["obra_id"]==oid and master["titulo"]==work["titulo"]
  assert len(master["fuentes"])==1 and master["fuentes"][0]["id"]==oid and len(master["unidades"])==work["unidades"]
  digest,filename=side.read_text(encoding="utf-8").strip().split("  ",1); assert filename==mp.name and digest==sha(mp)
  if oid==PILOT:
   assert master["schema_version"]=="1.1.0"; route="piloto_cerrado_fase9"; comparison=False
  else:
   assert master["schema_version"]=="1.4.0" and master["producido_por"]=={"motor":"ensamblador_maestro_obra_fase10","version":"1.2.0"}
   controls=master["controles_fase10"]; assert controls["version"]=="1.2.0" and controls["obra_id"]==oid and controls["comparacion_interobra"] is False
   assert all(controls[k] is True for k in ("maestro_independiente","normalizacion_recuperacion","verificacion_evidencia","auditoria_intraobra"))
   scope=controls["alcance_conceptual"]; assert scope["perfil"]==work["perfil_conceptual"] and scope["glosario_tecnico"]==work["glosario_tecnico"]
   assert scope["extraccion_conceptual_habilitada"] is True and scope["recuperacion_candidatos_habilitada"] is True and scope["identidad_confirmada_requiere_evidencia_explicita"] is True and scope["candidatos_sin_evidencia_permanecen_no_determinados"] is True
   assert scope["identidades_conceptuales_inferidas"] is False and scope["glosario_interobra_reutilizado"] is False and scope["interpretacion_cero_registros"]=="no_autoriza_afirmar_ausencia_semantica"
   manifest=json.loads((ROOT/"analista/generado/obras"/oid/"manifest-extractores.json").read_text(encoding="utf-8")); assert manifest["version"]=="1.4.0" and manifest["obra_id"]==oid and manifest["comparacion_interobra"] is False
   assert manifest["versiones_extractores"]["conceptos_apariciones"]=="1.3.0"
   assert manifest["perfil_conceptual"]==scope["perfil"] and manifest["glosario_tecnico"]==scope["glosario_tecnico"]
   for key in ("extraccion_conceptual_habilitada","recuperacion_candidatos_habilitada","identidad_confirmada_requiere_evidencia_explicita","candidatos_sin_evidencia_permanecen_no_determinados","identidades_conceptuales_inferidas","glosario_interobra_reutilizado","interpretacion_cero_registros"):
    assert scope[key]==manifest["limitaciones_conceptuales"][key]
   assert all(h.get("resolucion_doctrinal")=="no_realizada" for h in master["hallazgos_auditoria"])
   route="repeticion_controlada_fase10"; comparison=False
  closure.append({"obra_id":oid,"titulo":work["titulo"],"ruta_cierre":route,"schema_maestro":master["schema_version"],"perfil_conceptual":work["perfil_conceptual"],"extraccion_conceptual_habilitada":True,"conceptos":conceptual_counts(master),"unidades":work["unidades"],"maestro":mp.relative_to(ROOT).as_posix(),"maestro_sha256":sha(mp),"comparacion_interobra":comparison})

 report={"version":VERSION,"fase":10,"fase10_cerrada":True,"criterio":"todas_las_obras_previstas_con_maestro_independiente_validado","inventario":{"obras":len(works),"con_glosario_tecnico_explicito":inventory["obras_con_glosario"],"sin_glosario_tecnico_explicito":inventory["obras_sin_glosario"],"piloto_id":PILOT},"clausura_descriptiva":{"comparacion_interobra":False,"sintesis_doctrinal":False,"resolucion_doctrinal":"no_realizada","ausencia_de_registros_implica_ausencia_semantica":False,"identidad_candidata_se_convierte_en_doctrina":False},"obras":closure}
 payload=(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode("utf-8"); REPORT.parent.mkdir(parents=True,exist_ok=True); REPORT.write_bytes(payload); REPORT.with_suffix(REPORT.suffix+".sha256").write_text(f"{hashlib.sha256(payload).hexdigest()}  {REPORT.name}\n",encoding="utf-8")
 persisted=json.loads(REPORT.read_text(encoding="utf-8")); assert persisted==report and persisted["fase10_cerrada"] is True and len(persisted["obras"])==20 and all(not x["comparacion_interobra"] for x in persisted["obras"])
 print(json.dumps({"fase":10,"fase10_cerrada":True,"obras":len(closure),"maestros":len(found),"repeticiones_fase10":len(closure)-1,"comparacion_interobra":False,"reporte_sha256":sha(REPORT)},ensure_ascii=False,sort_keys=True)); return 0
if __name__=="__main__": raise SystemExit(main())
