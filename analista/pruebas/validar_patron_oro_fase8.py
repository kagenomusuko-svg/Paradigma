#!/usr/bin/env python3
"""Valida el patrón efectivo completo de Fase 8 y sus sustituciones explícitas."""
from __future__ import annotations
import copy,importlib.util,json,subprocess,sys,tempfile
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; CAL=ROOT/'analista/calibracion'; VALIDATOR=CAL/'validar_patron_oro.py'; MANIFEST=CAL/'patron-oro-manifiesto.json'; SCHEMA=CAL/'patron-oro-v1.0.0.schema.json'; LOCK=CAL/'muestra-fase8.lock.json'; UNITS=ROOT/'analista/generado/unidades.jsonl'
MATERIALIZERS=[CAL/'materializar_oro_conceptos.py',CAL/'materializar_oro_afirmaciones.py',CAL/'materializar_oro_limitadores.py']
spec=importlib.util.spec_from_file_location('gold_validator',VALIDATOR);assert spec and spec.loader;mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def validate(path):return mod.validate_paths(gold=path,schema=SCHEMA,lock=LOCK,units=UNITS,corpus_root=ROOT)
def expect_failure(rows,text):
 with tempfile.TemporaryDirectory() as td:
  p=Path(td)/'gold.jsonl';p.write_text(''.join(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n' for r in rows),encoding='utf-8')
  try:validate(p)
  except AssertionError as e:
   assert text in str(e),(text,e);return
  raise AssertionError(f'Debía fallar: {text}')
def expect_manifest_failure(mutator,text):
 doc=json.loads(MANIFEST.read_text(encoding='utf-8'));mutator(doc);p=CAL/'.manifest-test.tmp.json'
 try:
  p.write_text(json.dumps(doc,ensure_ascii=False)+'\n',encoding='utf-8')
  try:mod.effective_manifest_rows(p)
  except AssertionError as e:assert text in str(e),(text,e);return
  raise AssertionError(f'Debía fallar: {text}')
 finally:p.unlink(missing_ok=True)
def items(rows,motor,stratum=None):
 selected=[r for r in rows if r['motor']==motor and (stratum is None or stratum in r['estratos'])];return selected,[i for r in selected for i in r['items_esperados']]
def main():
 for m in MATERIALIZERS:subprocess.run([sys.executable,str(m)],cwd=ROOT,check=True)
 rows=mod.manifest_rows(MANIFEST);result=mod.validate_manifest(manifest=MANIFEST,schema=SCHEMA,lock=LOCK,units=UNITS,corpus_root=ROOT)
 expected_files=['patron-oro.jsonl','patron-oro-formulas.jsonl','patron-oro-formulas-general.jsonl','patron-oro-relaciones-general.jsonl','patron-oro-relaciones-desafio-v2.jsonl','patron-oro-relaciones-general-correccion-v2.jsonl','patron-oro-definiciones-general.jsonl','patron-oro-conceptos-desafio.jsonl','patron-oro-conceptos-general.jsonl','patron-oro-afirmaciones.jsonl','patron-oro-limitadores.jsonl']
 assert result=={'revisiones':259,'items':542,'motores':['afirmaciones','conceptos_apariciones','definiciones','formulas','limitadores','relaciones_explicitas'],'archivos_gold':expected_files,'reemplazos':3},result
 strata=Counter((r['motor'],s) for r in rows for s in r['estratos'])
 assert strata==Counter({('conceptos_apariciones','general'):31,('conceptos_apariciones','desafio'):10,('definiciones','general'):31,('definiciones','desafio'):7,('afirmaciones','general'):31,('afirmaciones','desafio'):12,('formulas','general'):31,('formulas','desafio'):18,('relaciones_explicitas','general'):31,('relaciones_explicitas','desafio'):2,('limitadores','general'):31,('limitadores','desafio'):27})
 _,cg=items(rows,'conceptos_apariciones','general');_,cd=items(rows,'conceptos_apariciones','desafio');assert len(cg)==114 and sum(i['tipo_registro']=='concepto' for i in cg)==3 and sum(i['tipo_registro']=='aparicion_conceptual' and i['concepto_designacion'] is not None for i in cg)==17;assert len(cd)==70 and sum(i['concepto_designacion'] is not None for i in cd)==8
 _,dg=items(rows,'definiciones','general');_,dd=items(rows,'definiciones','desafio');assert len(dg)==12 and Counter(i['clasificacion'] for i in dg)==Counter({'definicion_explicita':7,'definicion_candidata':5}) and len(dd)==21
 _,ag=items(rows,'afirmaciones','general');_,ad=items(rows,'afirmaciones','desafio');_,aa=items(rows,'afirmaciones');assert len(ag)==34 and len(ad)==26 and len(aa)==58;assert Counter(i['clasificacion'] for i in aa)==Counter({'afirmacion_explicita':49,'afirmacion_candidata':9});assert Counter(i['estatus_enunciativo'] for i in aa)==Counter({'afirmacion_autoral':27,'discurso_referido':17,'negacion_autoral':7,'formulacion_condicional':3,'ejemplo':2,'objecion':1,'pregunta':1})
 fg,fig=items(rows,'formulas','general');fd,fid=items(rows,'formulas','desafio');assert len(fg)==31 and not fig and len(fd)==18 and len(fid)==21
 rg,rig=items(rows,'relaciones_explicitas','general');rd,rid=items(rows,'relaciones_explicitas','desafio');assert len(rg)==31 and len(rig)==14 and sum(bool(r['items_esperados']) for r in rg)==6 and len(rd)==2 and len(rid)==14
 lg,lig=items(rows,'limitadores','general');ld,lid=items(rows,'limitadores','desafio');_,lia=items(rows,'limitadores');assert len(lg)==31 and len(lig)==96 and len(ld)==27 and len(lid)==132 and len(lia)==218;assert Counter(i['tipo_registro'] for i in lia)==Counter({'negacion':162,'distincion':50,'restriccion_alcance':5,'excepcion':1});assert Counter(i['clasificacion'] for i in lia)==Counter({'negacion_explicita':152,'negacion_candidata':10,'distincion_explicita':48,'distincion_candidata':2,'restriccion_explicita':5,'excepcion_explicita':1})
 historical=[r for r in mod.load_jsonl(CAL/'patron-oro.jsonl') if r['motor']=='relaciones_explicitas'];assert (len(historical),sum(len(r['items_esperados']) for r in historical))==(2,4) and len(rid)==14
 corrected=next(r for r in rg if r['unidad_id']=='UT-4EC2EC8C08A8');pe=next(i for i in corrected['items_esperados'] if i['sujeto_designacion']=='Pasión' and i['objeto_designacion']=='Ego');assert pe['linea_inicio']==154 and pe['linea_fin']==155 and pe['texto_literal']=='existencia de un ego que la pasión construyó con\nanterioridad al pensamiento que lo encuentra.'
 mutated=copy.deepcopy(rows);mutated.append(copy.deepcopy(rows[0]));expect_failure(mutated,'duplicada unidad–motor')
 mutated=copy.deepcopy(rows);mutated[0]['items_esperados'][0]['texto_literal']+=' CORRUPCIÓN';expect_failure(mutated,'Literal no coincide')
 mutated=copy.deepcopy(rows);mutated[0]['items_esperados'][0]['clasificacion']='definicion_inferida';expect_failure(mutated,'Clasificación inválida')
 mutated=copy.deepcopy(rows);mutated[0]['estratos']=['general'];expect_failure(mutated,'marcado general')
 mutated=copy.deepcopy(rows);mutated[0]['items_esperados'][0]['tipo_registro']='formula';expect_failure(mutated,'no pertenece al motor')
 expect_manifest_failure(lambda d:d['reemplazos'].append(copy.deepcopy(d['reemplazos'][0])),'Reemplazo duplicado unidad–motor');expect_manifest_failure(lambda d:d['reemplazos'][0].update({'archivo_origen':'inexistente.jsonl'}),'archivo no declarado');expect_manifest_failure(lambda d:d['reemplazos'][0].update({'archivo_sustituto':'patron-oro.jsonl'}),'Origen y sustituto no pueden coincidir')
 print('OK Fase 8 infraestructura: 259 revisiones/542 ítems; seis motores manifestados; 3 sustituciones históricas explícitas; gold 4F=56 revisiones/218 ítems.')
 return 0
if __name__=='__main__':raise SystemExit(main())
