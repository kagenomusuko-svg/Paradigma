# Calibración de Fase 8

La calibración mide precisión y cobertura por separado. No modifica registros de extracción ni autoriza síntesis doctrinal.

## Separación obligatoria

1. `muestra-fase8.lock.json` congela la selección de unidades.
2. `patron-oro-v1.0.0.schema.json` valida anotaciones manuales contra texto literal.
3. Las salidas de extractores pueden usarse para **estratificar** casos de desafío, pero nunca para completar automáticamente `items_esperados`.
4. La detección se evalúa separadamente de la clasificación. Un registro conservador puede detectar correctamente un fenómeno y mantener una etiqueta candidata/no determinada.
5. El estrato `general` y el estrato `desafio` se reportan por separado. La muestra enriquecida combinada no se presenta como estimación poblacional.

## Muestra congelada

El estrato general contiene 31 unidades: una selección determinista por cada archivo de la obra piloto y controles estructurales de encabezado/separador. Los desafíos congelados cubren:

- conceptos/apariciones: 10 unidades;
- definiciones: 7 unidades;
- afirmaciones: 12 unidades;
- fórmulas: 18 unidades;
- relaciones explícitas: 2 unidades;
- limitadores: 27 unidades.

La unión contiene 96 unidades únicas. Cambiar un extractor no cambia esta muestra.

## Regla epistemológica

Un patrón de oro registra lo que la revisión textual considera recuperable bajo el contrato de cada motor. No resuelve ambigüedades doctrinales. Cuando la identidad conceptual, el estatus enunciativo o el alcance no son inequívocos, la anotación debe conservar `null`, `no_determinado` o una clasificación candidata según corresponda.

## Cierre

Fase 8 solo puede cerrarse cuando cada motor tenga anotación manual suficiente en los estratos aplicables, métricas de `precision`, `cobertura`, `falsos_positivos`, `falsos_negativos` y `unidades_procesadas`, y alcance el umbral de producción que se documente antes del cierre.
