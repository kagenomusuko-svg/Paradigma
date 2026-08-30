#!/usr/bin/env python3
"""Compatibilidad de Ágape y de la ruta sin glosario de Fase 10.

Una obra sin glosario debe ejecutar recuperación conceptual completa. La ausencia
de glosario no autoriza ni a vaciar los productos ni a impedir identidades que
estén respaldadas por una declaración explícita de la propia obra.
"""
from __future__ import annotations
import json, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
GENERIC=ROOT/"analista/pruebas/validar_obra_fase10.py"; EXTRACTOR=ROOT/"analista/motores/ejecutar_extractores_obra_fase10.py"
FUENTES=ROOT/"analista/generado/fuentes.jsonl"; UNIDADES=ROOT/"analista/generado/unidades.jsonl"; AGAPE="FUE-2C28F35DD6CF"

def load_jsonl(path): return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line]
def run(cmd): subprocess.run(cmd,cwd=ROOT,check=True)
def declarative(app):
 c=app.get("criterio_deteccion","")
 return c=="lema_en_glosario_tecnico_explicito" or c.startswith("declaracion_designativa_explicita_en_cuerpo:")

def main()->int:
 run([sys.executable,str(GENERIC),"--obra-id",AGAPE])
 sources=load_jsonl(FUENTES); units=load_jsonl(UNIDADES)
 without=next(source for source in sources if not any(str(route).endswith("99-glosario.md") for route in source.get("rutas_derivadas",[])))
 obra_id=without["id"]; work_units=[u for u in units if u.get("fuente_id")==obra_id]; assert work_units
 with tempfile.TemporaryDirectory() as td:
  out=Path(td)/obra_id
  run([sys.executable,str(EXTRACTOR),"--obra-id",obra_id,"--fuentes",str(FUENTES),"--unidades",str(UNIDADES),"--output-root",str(out)])
  manifest=json.loads((out/"manifest-extractores.json").read_text(encoding="utf-8"))
  assert manifest["version"]=="1.4.0" and manifest["obra_id"]==obra_id and manifest["glosario_tecnico"] is None
  assert manifest["perfil_conceptual"]=="sin_glosario_tecnico_explicito" and manifest["comparacion_interobra"] is False
  assert manifest["versiones_extractores"]["conceptos_apariciones"]=="1.3.0"
  limits=manifest["limitaciones_conceptuales"]
  assert limits["extraccion_conceptual_habilitada"] is True and limits["recuperacion_candidatos_habilitada"] is True
  assert limits["identidad_confirmada_requiere_evidencia_explicita"] is True and limits["candidatos_sin_evidencia_permanecen_no_determinados"] is True
  assert limits["identidades_conceptuales_inferidas"] is False and limits["glosario_interobra_reutilizado"] is False
  assert limits["interpretacion_cero_registros"]=="no_autoriza_afirmar_ausencia_semantica"

  apps={r["id"]:r for r in load_jsonl(out/"apariciones-conceptuales.jsonl")}; concepts=load_jsonl(out/"conceptos.jsonl")
  for concept in concepts:
   evidence=concept["evidencia_identidad_ids"]
   if concept["estado_identidad_conceptual"]=="establecida_por_evidencia":
    assert evidence and all(a in apps and declarative(apps[a]) for a in evidence)
    assert all(apps[a]["fuente_id"]==obra_id for a in evidence)
    assert all(apps[a]["criterio_deteccion"]!="lema_en_glosario_tecnico_explicito" for a in evidence)
   else:
    assert concept["estado_identidad_conceptual"]=="no_determinada" and evidence==[]

  for filename,motor in (("cobertura-conceptos.jsonl","conceptos_apariciones"),("cobertura-definiciones.jsonl","definiciones"),("cobertura-relaciones.jsonl","relaciones_explicitas")):
   rows=load_jsonl(out/filename); assert len(rows)==1; coverage=rows[0]
   assert coverage["motor"]==motor and coverage["obra_id"]==obra_id
   assert coverage["unidades_totales"]==coverage["unidades_procesadas"]==len(work_units)
   assert coverage["unidades_omitidas"]==[] and coverage["errores"]==[]
 print("OK Fase 10 compatibilidad: sin glosario hay recuperación completa; solo evidencia declarativa intraobra puede establecer identidad")
 return 0
if __name__=="__main__": raise SystemExit(main())
