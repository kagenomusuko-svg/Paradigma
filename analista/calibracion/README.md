# Calibración de Fase 8

La calibración mide precisión y cobertura por separado. No modifica registros de extracción ni autoriza síntesis doctrinal.

## Separación obligatoria

1. `muestra-fase8.lock.json` congela la selección de unidades.
2. `patron-oro-v1.0.0.schema.json` valida anotaciones manuales contra texto literal.
3. `patron-oro-manifiesto.json` declara explícitamente qué archivos forman el patrón evaluable; no se descubren archivos por glob.
4. Las salidas de extractores pueden usarse para **estratificar** casos de desafío, pero nunca para completar automáticamente `items_esperados`.
5. La detección se evalúa separadamente de la clasificación. Un registro conservador puede detectar correctamente un fenómeno y mantener una etiqueta candidata/no determinada.
6. El estrato `general` y el estrato `desafio` se reportan por separado. La muestra enriquecida combinada no se presenta como estimación poblacional.

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

## Reglas manuales de anotación

- **Definiciones:** una definición explícita conserva el bloque literal efectivamente dedicado a definir el lema. Un marcador de página interpuesto se conserva si cae dentro del bloque canónico. Una abreviatura o remisión no autoriza expandir la identidad conceptual por similitud.
- **Relaciones explícitas:** sujeto y objeto se registran solo cuando la relación entre ambos está textual y suficientemente establecida. No se aplica transitividad ni expansión automática de abreviaturas.
- **Fórmulas:** `texto_literal` contiene la expresión formal mínima completa que aparece en la fuente, preservando sus saltos de línea internos. Se excluye el prosema introductorio y la puntuación terminal que no forme parte de la expresión. El rango de líneas cubre exactamente las líneas tocadas por la expresión. Una expresión escrita de forma inequívoca puede anotarse como `formula_explicita`; no se normalizan ni fusionan expresiones matemáticamente parecidas.

Estas reglas se fijan antes de usar las métricas para ajustar extractores. Un cambio posterior exige versionar el criterio y no puede reetiquetar silenciosamente el patrón existente.

## Protocolo cuantitativo

`umbrales-v1.0.0.json` queda conservado como primera formulación histórica del gate. El protocolo vigente es `umbrales-v1.1.0.json` y el reporte de calibración tiene versión `1.1.0`.

Las métricas `precision` y `cobertura` conservan su definición ordinaria. Si su denominador es cero, el valor es `null`: no se sustituye por `0` ni por `1`. El reporte expone además `positivos_esperados` y `predicciones_emitidas`, y el gate comprueba mecánicamente que:

```text
positivos_esperados = verdaderos_positivos + falsos_negativos
predicciones_emitidas = verdaderos_positivos + falsos_positivos
```

Un estrato sin positivos solo puede funcionar como **control negativo** cuando el archivo de umbrales lo autoriza expresamente para ese motor. Ese control no satisface umbrales de precisión, cobertura o clasificación por ficción estadística. Cumple únicamente si:

- hay unidades manualmente revisadas;
- `positivos_esperados = 0`;
- los conteos son consistentes;
- los falsos positivos no superan el máximo declarado —para fórmulas, `0`—;
- el estrato complementario del mismo motor contiene al menos un positivo manual y se evalúa con los umbrales ordinarios.

En el patrón vigente de fórmulas, las 31 unidades del estrato general fueron revisadas manualmente y contienen 0 fórmulas recuperables bajo la regla congelada. Por ello ese estrato es un control negativo; las 18 unidades de desafío contienen 21 fórmulas positivas y sostienen la medición de cobertura y clasificación.

## Cierre

Fase 8 solo puede cerrarse cuando cada motor tenga anotación manual suficiente en los estratos aplicables, reporte como mínimo `precision`, `cobertura`, `falsos_positivos`, `falsos_negativos` y `unidades_procesadas`, mantenga denominadores y conteos consistentes, y alcance el umbral de producción documentado antes del cierre. Un control negativo autorizado no reemplaza un estrato positivo complementario.
