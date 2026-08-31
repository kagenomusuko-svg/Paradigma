#!/usr/bin/env python3
"""Comprueba 4F v1.1.1 contra el gold congelado, sin modificarlo."""
from __future__ import annotations
import json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MATERIALIZER=ROOT/'analista/calibracion/materializar_oro_limitadores.py'; GOLD=ROOT/'analista/calibracion/patron-oro-limitadores.jsonl'; MOTOR=ROOT/'analista/motores/limitadores.py'; EVAL=ROOT/'analista/calibracion/evaluar.py'; COVERAGE=ROOT/'analista/generado/cobertura-limitadores.jsonl'

def main():
 subprocess.run([sys.executable,str(MATERIALIZER)],cwd=ROOT,check=True);subprocess.run([sys.executable,str(MOTOR)],cwd=ROOT,check=True)
 coverage=[json.loads(x) for x in COVERAGE.read_text(encoding='utf-8').splitlines() if x];assert len(coverage)==1 and coverage[0]['version_motor']=='1.1.1' and coverage[0]['producido_por']=={'motor':'limitadores','version':'1.1.1'}
 with tempfile.TemporaryDirectory() as td:
  report=Path(td)/'report.json';subprocess.run([sys.executable,str(EVAL),'--patron',str(GOLD),'--salida',str(report)],cwd=ROOT,check=True);rows={r['estrato']:r for r in json.loads(report.read_text(encoding='utf-8'))['reportes']}
 expected={
  'general':(96,92,87,5,9,0.9456521739130435,0.90625),
  'desafio':(132,126,115,11,17,0.9126984126984127,0.8712121212121212),
  'combinado':(218,208,192,16,26,0.9230769230769231,0.8807339449541285),
 }
 for st,(gold,pred,tp,fp,fn,precision,recall) in expected.items():
  r=rows[st];assert r['motor']=='limitadores';assert (r['positivos_esperados'],r['predicciones_emitidas'],r['verdaderos_positivos'],r['falsos_positivos'],r['falsos_negativos'])==(gold,pred,tp,fp,fn);assert abs(r['precision']-precision)<1e-12 and abs(r['cobertura']-recall)<1e-12;assert r['exactitud_clasificacion']==1.0
 assert rows['general']['precision']>=0.90 and rows['general']['cobertura']>=0.85
 assert rows['desafio']['precision']>=0.90 and rows['desafio']['cobertura']>=0.85
 print('OK calibración 4F v1.1.1: general P=.946/R=.906; desafío P=.913/R=.871; clasificación=1.0; gold congelado 56 revisiones/218 ítems.')
 return 0
if __name__=='__main__':raise SystemExit(main())