#!/usr/bin/env python3
"""Regresión específica de Ágape sobre la cadena genérica vigente de Fase 10.

Este punto de entrada no mantiene un contrato paralelo: primero ejecuta el gate
intraobra común y después verifica únicamente invariantes estables específicos de
Ágape. No convierte resultados históricos en validación de la implementación
actual.
"""
from __future__ import annotations
import hashlib, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
AGAPE="FUE-2C28F35DD6CF"; PILOTO="AA-SP-V1"
MASTER=ROOT/"analista/generado/maestros"/f"{AGAPE}.json"
GENERIC=ROOT/"analista/pruebas/validar_obra_fase10.py"
PROFILE=ROOT/"analista/calibracion/fase10"/AGAPE/"perfil-extractores.json"

def main()->int:
 subprocess.run([sys.executable,str(GENERIC),"--obra-id",AGAPE],cwd=ROOT,check=True)
 master=json.loads(MASTER.read_text(encoding="utf-8"))
 assert master["id"]==f"MAE-{AGAPE}" and master["obra_id"]==AGAPE
 assert master["titulo"]=="Afrodita Areia: Ágape"
 assert master["schema_version"]=="1.4.0"
 assert master["producido_por"]=={"motor":"ensamblador_maestro_obra_fase10","version":"1.2.0"}
 assert len(master["fuentes"])==1 and master["fuentes"][0]["id"]==AGAPE
 assert len(master["unidades"])==643
 controls=master["controles_fase10"]
 assert controls["version"]=="1.2.0" and controls["comparacion_interobra"] is False
 assert all(controls[k] is True for k in ("maestro_independiente","normalizacion_recuperacion","verificacion_evidencia","auditoria_intraobra"))
 scope=controls["alcance_conceptual"]
 assert scope["perfil"]=="glosario_tecnico_explicito"
 assert isinstance(scope["glosario_tecnico"],str) and scope["glosario_tecnico"].endswith("99-glosario.md")
 assert scope["extraccion_conceptual_habilitada"] is True
 assert scope["identidad_confirmada_requiere_evidencia_explicita"] is True
 assert scope["identidades_conceptuales_inferidas"] is False
 assert scope["glosario_interobra_reutilizado"] is False
 assert scope["interpretacion_cero_registros"]=="no_autoriza_afirmar_ausencia_semantica"
 calibration=controls["calibracion_formulas"]
 if calibration["perfil_calibrado"]:
  assert calibration["perfil"]==f"analista/calibracion/fase10/{AGAPE}/perfil-extractores.json"
  assert PROFILE.is_file()
  assert calibration["perfil_sha256"]==hashlib.sha256(PROFILE.read_bytes()).hexdigest()
 assert len(master["reportes_cobertura"])==6
 assert all(r["obra_id"]==AGAPE and r["unidades_totales"]==r["unidades_procesadas"]==643 and not r["unidades_omitidas"] and not r["errores"] for r in master["reportes_cobertura"])
 assert all(r["resolucion_doctrinal"]=="no_realizada" for r in master["hallazgos_auditoria"])
 assert PILOTO not in MASTER.read_text(encoding="utf-8")
 print("OK Fase 10 Ágape: regresión específica delegada al gate intraobra vigente; 643 unidades, sin comparación interobra ni cierre global")
 return 0
if __name__=="__main__": raise SystemExit(main())
