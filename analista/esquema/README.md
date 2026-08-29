# Contratos de datos del analista — Fase 1

Versión: **1.0.0**. Este directorio implementa la Fase 1 de `analista/FASES.md`; `analista/README.md` y `analista/config/clausura-descriptiva.yaml` siguen siendo la especificación vinculante.

`contratos-v1.0.0.schema.json` define contratos independientes en `$defs` para fuente, unidad textual, aparición conceptual, concepto, definición, afirmación, fórmula, relación explícita, distinción, negación, excepción, restricción de alcance, hallazgo de auditoría, reporte de cobertura y expediente maestro de obra.

Todos distinguen `texto_literal`, `normalizacion_formal`, `normalizacion_lexica`, `estatus_enunciativo`, `estado_extraccion`, `estado_verificacion` y `estado_auditoria`. Los IDs son referencias estables, no afirmaciones de identidad doctrinal. La normalización solo amplía recuperación. `additionalProperties: false`/`unevaluatedProperties: false` impide introducir campos ad hoc; un registro `auditado` exige evidencia `verificado`.

El esquema histórico `analisis/esquema/registro-v0.1.schema.json` se conserva como artefacto del prototipo y no es contrato vigente de `analista/`.

La prueba `analista/pruebas/validar_contratos_fase1.py` valida el esquema real, instancia los quince contratos y verifica que se rechacen campos prescriptivos, transitividad no documentada y auditoría con verificación pendiente. Sus datos son sintéticos y no pertenecen al corpus.
