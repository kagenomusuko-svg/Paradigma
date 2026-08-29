# Contratos de datos del analista

`analista/README.md`, `analista/FASES.md` y `analista/config/clausura-descriptiva.yaml` siguen siendo la especificación vinculante.

## Contratos atómicos — v1.0.0

`contratos-v1.0.0.schema.json` es el contrato cerrado en Fase 1. Define `$defs` independientes para fuente, unidad textual, aparición conceptual, concepto, definición, afirmación, fórmula, relación explícita, distinción, negación, excepción, restricción de alcance, hallazgo de auditoría, reporte de cobertura y el expediente maestro previsto inicialmente.

Todos distinguen `texto_literal`, `normalizacion_formal`, `normalizacion_lexica`, `estatus_enunciativo`, `estado_extraccion`, `estado_verificacion` y `estado_auditoria`. Los IDs son referencias estables, no afirmaciones de identidad doctrinal. La normalización solo amplía recuperación. `additionalProperties: false`/`unevaluatedProperties: false` impide introducir campos ad hoc; un registro `auditado` exige evidencia `verificado`.

La prueba `analista/pruebas/validar_contratos_fase1.py` mantiene la compatibilidad de estos quince contratos. El archivo no se reescribe retroactivamente al avanzar de fase.

## Expediente maestro — v1.1.0

Fase 9 exige, además de los campos previstos en Fase 1, **métricas de calibración, cierre cuantitativo y hashes de trazabilidad de los insumos**. Esos datos no caben honestamente en `historial_versiones` ni en metadatos libres. Por ello `expediente-maestro-v1.1.0.schema.json` es una extensión específica del contenedor maestro, sin modificar los contratos atómicos v1.0.0.

El contrato v1.1.0:

- referencia los registros atómicos del esquema v1.0.0 en vez de redefinirlos;
- exige `metricas_calibracion` de Fase 8 y `cierre_calibracion=true`;
- exige `trazabilidad_archivos` con SHA-256 y número de registros incluidos por insumo;
- conserva un historial de versiones puramente documental;
- no añade campos de síntesis, armonización o resolución doctrinal.

El ensamblador de Fase 9 debe copiar los registros auditados **sin transformarlos**. La prueba `analista/pruebas/validar_maestro_fase9.py` comprueba el contrato, la igualdad exacta con las entradas auditadas, las referencias, los hashes, el gate de calibración y la reproducibilidad byte a byte.

El esquema histórico `analisis/esquema/registro-v0.1.schema.json` se conserva como artefacto del prototipo y no es contrato vigente de `analista/`.
