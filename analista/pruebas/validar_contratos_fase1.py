#!/usr/bin/env python3
import copy,hashlib,json,sys
from pathlib import Path
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError
P=Path(__file__).resolve().parents[1]/"esquema/contratos-v1.0.0.schema.json"
def b(t,i,txt=None,e=None):return {"id":i,"tipo_registro":t,"schema_version":"1.0.0","texto_literal":txt,"normalizacion_formal":None,"normalizacion_lexica":None,"estatus_enunciativo":e,"estado_extraccion":"extraido","estado_verificacion":"verificado","estado_auditoria":"auditado","producido_por":{"motor":"fixture_contractual","version":"1.0.0"}}
def L(n):return {"ruta":"fixture-sintetico.md","linea_inicio":n,"linea_fin":n}
def main():
 s=json.loads(P.read_text());Draft202012Validator.check_schema(s);v=Draft202012Validator(s)
 f=b("fuente","FUE-T");f.update(titulo="Fixture",ruta_canonica="fixture-sintetico.md",rutas_derivadas=[],sha256="0"*64,version_fuente="1",metadatos_documentales={},segmentaciones=["SEG-T"])
 u=b("unidad_textual","UT-T","X se define como A.");u.update(fuente_id="FUE-T",archivo="fixture-sintetico.md",seccion=None,localizacion=L(1),orden_textual=0,tipo_estructural="parrafo",sha256_texto=hashlib.sha256(u["texto_literal"].encode()).hexdigest())
 ap=b("aparicion_conceptual","AP-T","X","no_determinado");ap.update(fuente_id="FUE-T",unidad_id="UT-T",concepto_id="CON-T",forma_literal="X",variante_formal=None,variantes_lexicas_busqueda=[],localizacion=L(1),criterio_deteccion="fixture")
 c=b("concepto","CON-T");c.update(designacion_operativa="X",aparicion_ids=["AP-T"],formas_literales_observadas=["X"],estado_identidad_conceptual="no_determinada",evidencia_identidad_ids=[])
 d=b("definicion","DEF-T","X se define como A.","definicion");d.update(fuente_id="FUE-T",unidad_id="UT-T",concepto_id="CON-T",clasificacion_definicion="definicion_explicita",localizacion=L(1),criterio_deteccion="fixture")
 a=b("afirmacion","AF-T","Si Q, X produce B.","formulacion_condicional");a.update(fuente_id="FUE-T",unidad_id="UT-T",concepto_ids=["CON-T"],clasificacion_afirmacion="afirmacion_explicita",sujeto_literal="X",predicado_literal="produce",objeto_literal="B",localizacion=L(2),criterio_deteccion="fixture",confianza_extraccion=1.0)
 fo=b("formula","FOR-T","Fórmula: X=A+B.","no_determinado");fo.update(fuente_id="FUE-T",unidad_id="UT-T",formula_literal="X=A+B",contexto_unidad_ids=["UT-T"],simbolos_literales=["X","A","B"],localizacion=L(3),clasificacion_formula="formula_explicita")
 r=b("relacion_explicita","REL-T","X depende de Q.","afirmacion_autoral");r.update(fuente_id="FUE-T",unidad_id="UT-T",sujeto_ref="CON-T",objeto_ref="CON-Q",relacion_literal="depende de",clasificacion_relacion="relacion_explicita",localizacion=L(4))
 di=b("distincion","DIS-T","X se distingue de Z.","afirmacion_autoral");di.update(fuente_id="FUE-T",unidad_id="UT-T",termino_a_literal="X",termino_b_literal="Z",marcador_literal="se distingue de",clasificacion_distincion="distincion_explicita",localizacion=L(5))
 n=b("negacion","NEG-T","X no es Y.","negacion_autoral");n.update(fuente_id="FUE-T",unidad_id="UT-T",objeto_negado_literal="X es Y",alcance_literal=None,clasificacion_negacion="negacion_explicita",localizacion=L(6))
 e=b("excepcion","EXC-T","Excepto en C, X produce B.","afirmacion_autoral");e.update(fuente_id="FUE-T",unidad_id="UT-T",afirmacion_limitada_id="AF-T",fragmento_exceptivo_literal="Excepto en C",clasificacion_excepcion="excepcion_explicita",localizacion=L(7))
 rs=b("restriccion_alcance","RES-T","Si Q, X produce B.","formulacion_condicional");rs.update(fuente_id="FUE-T",unidad_id="UT-T",afirmacion_limitada_id="AF-T",tipo_restriccion="condicional",fragmento_restriccion_literal="Si Q",clasificacion_restriccion="restriccion_explicita",localizacion=L(2))
 h=b("hallazgo_auditoria","HAL-T");h.update(obra_id="OB-T",categoria="restriccion_de_alcance",registro_ids=["AF-T","RES-T"],descripcion_documental="El registro conserva una restricción separada.",resolucion_doctrinal="no_realizada")
 co=b("reporte_cobertura","COB-T");co.update(obra_id="OB-T",motor="fixture_contractual",version_motor="1",unidades_totales=1,unidades_procesadas=1,unidades_omitidas=[],errores=[])
 m=b("expediente_maestro_obra","EMO-T");m.update(obra_id="OB-T",titulo="Fixture",fuentes=[f],unidades=[u],apariciones_conceptuales=[ap],conceptos=[c],definiciones=[d],afirmaciones=[a],formulas=[fo],relaciones_explicitas=[r],distinciones=[di],negaciones=[n],excepciones=[e],restricciones_alcance=[rs],hallazgos_auditoria=[h],reportes_cobertura=[co],historial_versiones=[{"version":"1.0.0","descripcion":"fixture"}])
 regs=[f,u,ap,c,d,a,fo,r,di,n,e,rs,h,co,m]
 for x in regs:v.validate(x)
 for bad in [(a,"deberia_ser","X"),(r,"transitividad",True)]:
  y=copy.deepcopy(bad[0]);y[bad[1]]=bad[2]
  try:v.validate(y)
  except ValidationError:pass
  else:raise AssertionError("clausura vulnerada")
 y=copy.deepcopy(d);y["estado_verificacion"]="pendiente"
 try:v.validate(y)
 except ValidationError:pass
 else:raise AssertionError("auditoría sin verificación aceptada")
 print("OK: 15 contratos interoperables; expediente maestro válido; clausura estructural activa")
if __name__=="__main__":sys.exit(main())
