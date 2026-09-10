# RES-EVID-001 — Resolución MANT de la arquitectura E0–E8 y la estimación de `w`

> **Documento analítico derivado, no fuente canónica.** Esta resolución no modifica retrospectivamente *El Método Prometeo*, *Taxonomía General de Aplicaciones* ni las demás obras del corpus. Fija cómo debe leerse y normalizarse transversalmente la relación entre clase de evidencia, magnitud causal e incertidumbre bajo el aparato vigente de `R*`.

- **ID:** `RES-EVID-001`
- **Familia:** E0–E8 → evidencia → aristas → `w` → incertidumbre → `R*`
- **Estado:** **RESUELTA EN SU NÚCLEO CONCEPTUAL Y METROLÓGICO — calibración numérica diferida**
- **Fecha:** 2026-09-10
- **Auditoría rectora:** `AUD-EVID-001`
- **Resoluciones relacionadas:** `RES-RSTAR-001`, `RES-SDO-PROM-001`, `RES-HISTOS-PROM-001`
- **Revisión principal:** `review.prometeo.evidence_scale_versions`

---

## 1. Problema adjudicado

`AUD-EVID-001` confirmó dos hechos distintos:

1. existen tres tablas E0–E8 con rangos numéricos incompatibles entre Prometeo Cap. 2, Prometeo Apéndice A y Taxonomía U·2;
2. existe una incompatibilidad semántica fuerte en `E0`: Prometeo exige **evidencia positiva de ausencia causal**, mientras Taxonomía U·2 usa `E0` para **ausencia total de evidencia**.

La lectura posterior identifica además el problema arquitectónico que explica por qué las tres tablas no pueden resolverse simplemente escogiendo una como canónica:

> **la escala E mezcla fuerza epistémica con magnitud causal.**

La resolución separa ambas dimensiones.

---

## 2. Distinción rectora: mundo causal y conocimiento del mundo causal

En la arquitectura vigente, el peso local `w_ij` representa la magnitud de la determinación causal de `i` sobre `j` en la relación analizada.

Esa magnitud pertenece al **mecanismo causal del caso**. No es una propiedad de cuántos documentos existen ni de la fuerza probatoria con que el analista conoce el mecanismo.

Por tanto deben distinguirse:

- **magnitud causal:** cuánto determina causalmente `i` a `j`;
- **estimación de la magnitud:** qué valor puede sostener el analista para esa magnitud;
- **incertidumbre epistémica:** con qué precisión puede sostenerse esa estimación dadas las fuentes disponibles.

Para desambiguar en esta resolución se usa provisionalmente:

- `w_ij`: magnitud causal local del mecanismo;
- `ŵ_ij`: estimación analítica de `w_ij`;
- `U(ŵ_ij)`: objeto de incertidumbre asociado a la estimación —intervalo, radio, distribución u otra representación futura validada.

Esta notación es **editorial/provisional** y no reescribe el canon de primera edición.

---

## 3. Contraejemplos que prueban la independencia

La separación no es opcional porque existen casos conceptualmente válidos en ambas direcciones.

### 3.1 Evidencia fuerte, magnitud causal baja

Un contrato E1 puede documentar de manera casi perfecta una relación en la que el nodo origen sólo condicionaba una parte menor del comportamiento del nodo destino.

Ejemplo abstracto:

`E1 + mecanismo con 85 % de discrecionalidad propia del destino → ŵ ≈ 0.15`

La calidad documental no convierte una relación causal débil en una relación causal fuerte.

### 3.2 Evidencia débil, magnitud causal potencialmente alta

Una relación causal muy intensa puede dejar inicialmente sólo evidencia estructural o indirecta.

Ejemplo abstracto:

`E6 + mecanismo hipotetizado de alta determinación → ŵ potencialmente alto, pero con U(ŵ) amplio`

La debilidad epistémica obliga a cautela sobre la estimación; no obliga a colocar su centro cerca de cero.

Consecuencia:

> **E no determina la posición de `ŵ`; informa cuánto puede confiarse o cuán precisamente puede sostenerse.**

---

## 4. Nueva arquitectura de la clase E

La relación correcta queda separada en dos funciones.

### 4.1 Estimación de magnitud

`evidencia sustantiva + mecanismo causal + estructura de la relación → ŵ`

Aquí importan, según el caso:

- formalización de la conducta;
- margen real de discrecionalidad;
- costos de apartarse;
- fungibilidad;
- secuencia causal documentada;
- capacidad material;
- condiciones de habilitación;
- demás hechos sustantivos del mecanismo.

### 4.2 Estimación de incertidumbre

`clase E + calidad específica de las fuentes + cantidad/convergencia + dominio + contradicción → U(ŵ)`

Aquí la clase E conserva una función metodológica central: informa la fuerza epistémica y contribuye a determinar la precisión defendible de la estimación.

Por tanto:

> **E1–E8 clasifican el estatuto/fuerza epistémica de la evidencia que acredita una arista y contribuyen a la incertidumbre de `ŵ`; no fijan por sí solos su valor esperado ni la posición de su intervalo.**

---

## 5. E no es irrelevante para `w`

Separar E de la posición de `w` no significa eliminar E del cálculo.

La clase E sigue siendo relevante para:

- anchura o forma de `U(ŵ)`;
- análisis de sensibilidad;
- robustez de conclusiones;
- necesidad de evidencia adicional;
- trazabilidad adversarial de la estimación;
- condiciones para emitir Declaraciones A/B/C/D;
- comparación entre estimaciones sustentadas con evidencia heterogénea.

La diferencia es precisa:

- **E no decide cuánto vale causalmente una arista**;
- **E informa cuán precisamente puede sostenerse la estimación de ese valor**.

---

## 6. La jerarquía E1–E8 es un prior metodológico de precisión, no una ley universal

Las clases E1–E8 pueden conservar un orden metodológico general de fuerza epistémica.

En igualdad de las demás condiciones, evidencia más directa, independiente y corroborada debería permitir una estimación más precisa que evidencia meramente indiciaria.

Pero no se fija una regla rígida del tipo:

`E1 siempre produce U más estrecho que E2, ... que E8`.

La precisión efectiva también depende de:

- ambigüedad intrínseca de la fuente;
- completitud;
- independencia entre fuentes;
- sesgo;
- método pericial;
- tamaño y calidad de muestra cuando corresponda;
- contradicciones;
- condiciones del dominio.

Por ello la jerarquía es un **prior metodológico orientador**, no una ley epistémica universal.

---

## 7. E0 no pertenece a la jerarquía ordinal E1–E8

La denominación histórica puede sugerir:

`E0 < E8 < ... < E1`.

Esa lectura queda rechazada.

`E1–E8` describen evidencia que **acredita positivamente una conexión causal** con distintos niveles de fuerza epistémica.

`E0` describe otra operación:

> **evidencia positiva de que la conexión causal no existe.**

Por tanto:

`E0 → arista nula documentada → w = 0`

no porque la evidencia sea «más débil» que E8, sino porque la evidencia sostiene una conclusión causal negativa.

`E0` es un **estado especial de nulidad documentada**, no el extremo inferior de la escala ordinal de evidencia positiva.

---

## 8. Tres estados de arista que no deben colapsarse

La arquitectura normalizada distingue al menos:

### 8.1 Arista nula documentada

Existe evidencia positiva de ausencia causal.

`estado = nula documentada`

`w = 0`

Puede conservar la etiqueta histórica `E0`.

### 8.2 Arista hipotética / no acreditada

No existe evidencia suficiente para incorporar la conexión como arista causal validada.

`estado = hipótesis / no acreditada`

No debe convertirse en `w = 0`.

No entra a `G_D` como arista causal validada; puede permanecer en el espacio de hipótesis, investigación o sensibilidad estructural según el protocolo futuro.

La segunda edición deberá decidir si necesita notación explícita o si basta su exclusión tipada.

### 8.3 Arista acreditada

Existe evidencia positiva a favor de la conexión.

`estado = acreditada`

Recibe:

- clase E1–E8;
- estimación `ŵ` basada en mecanismo y contenido sustantivo;
- incertidumbre `U(ŵ)` justificada por la calidad y estructura de la evidencia.

---

## 9. Resolución de E0

Se adopta la semántica fuerte ya formulada por Prometeo:

> **ausencia de evidencia ≠ evidencia de ausencia.**

En consecuencia:

- `E0` se reserva para evidencia positiva de nulidad causal;
- falta de evidencia no es `E0`;
- evidencia insuficiente no es `E0`;
- una hipótesis no acreditada no es `E0`;
- una conexión acreditada pero pequeña tampoco es `E0`.

Esto elimina la regla de Taxonomía U·2 que convertía «ausencia total de evidencia» en exclusión causal con `w=0`.

---

## 10. Qué ocurre con las tres tablas históricas

Ninguna de las tres tablas puede adoptarse como tabla canónica vigente de la arquitectura normalizada mediante mera preferencia editorial.

Sus intervalos mezclan:

- posición esperada de `w`;
- amplitud de incertidumbre;
- tipo de fuente;
- fuerza epistémica.

Por tanto, los rangos históricos E→`w` quedan clasificados como:

> **calibraciones autorales provisionales/históricas, no demostraciones de la magnitud causal asociada a cada clase E.**

Se preservan como parte de las primeras ediciones y de la evolución del método.

No se recalculan ni se sustituyen durante MANT.

---

## 11. Perfiles futuros de incertidumbre

Si la segunda edición conserva guías numéricas, éstas no deberán ubicar automáticamente el centro de `w`.

La arquitectura admisible será, por ejemplo:

`ŵ = estimación de magnitud desde mecanismo`

`E + propiedades de la evidencia → perfil de U(ŵ)`.

Una tabla futura podría informar:

- amplitud típica;
- precisión mínima/máxima;
- factores de ensanchamiento;
- reglas de degradación por contradicción;
- perfiles distintos por dominio.

Pero los valores concretos requieren calibración independiente.

Esta resolución **no inventa** radios, distribuciones ni coeficientes numéricos.

---

## 12. Regla de intersección de Taxonomía

La intersección de intervalos no se prohíbe en abstracto.

Puede ser una operación legítima si en una edición futura:

1. cada intervalo estima el **mismo `w`**;
2. los intervalos comparten una semántica explícita de incertidumbre;
3. las fuentes son combinables bajo supuestos declarados;
4. la operación de intersección tiene justificación metrológica.

Lo que queda rechazado es la operación actual automática:

`clase E → banda predeterminada de magnitud → intersección de bandas E`.

Antes de combinar evidencia debe distinguirse:

1. qué hecho acredita cada fuente;
2. si la arista existe y qué mecanismo sostiene;
3. qué estimación de `w` se deriva de ese mecanismo;
4. qué incertidumbre tiene cada estimación;
5. qué regla de combinación es válida para esos objetos.

---

## 13. Regla de prioridad y contradicción

La regla de prioridad de Taxonomía tampoco puede conservarse como aritmética automática sobre rangos E mientras E predetermine la posición de `w`.

La contradicción entre fuentes puede ocurrir en niveles diferentes:

- existencia de la arista;
- dirección causal;
- mecanismo;
- magnitud `w`;
- hechos auxiliares;
- credibilidad/calidad de la fuente.

La segunda edición debe adjudicar primero **qué proposición está en contradicción** y sólo después modificar `ŵ` o `U(ŵ)`.

Una fuente de clase superior puede tener prioridad metodológica, pero la clase por sí sola no decide automáticamente la verdad del hecho ni un desplazamiento numérico universal.

---

## 14. Impacto sobre `R*`

Bajo `RES-RSTAR-001`, `Q_D` y `b_D` se construyen desde pesos locales del grafo.

Por tanto la normalización de E afecta directamente:

`evidencia → arista acreditada → ŵ/U(ŵ) → Q_D,b_D → R*(D)`.

Consecuencias:

- los ejemplos calculados con tablas históricas deberán recalcularse en segunda edición una vez fijado un estimador operativo de `w`;
- la sensibilidad de `R*` debe propagarse desde `U(ŵ)`, no desde bandas cuya posición venga dada únicamente por la clase E;
- una arista no acreditada no debe convertirse silenciosamente en cero;
- una arista nula documentada sí aporta `w=0` de manera explícita.

No se ejecutan recálculos durante esta resolución MANT.

---

## 15. Efecto sobre `AUD-EVID-001` y la revisión histórica

`AUD-EVID-001` queda **adjudicada en su núcleo conceptual/metrológico**.

`review.prometeo.evidence_scale_versions` se desdobla:

### Resuelto

- significado de `E0`;
- separación ausencia de evidencia / evidencia de ausencia;
- separación clase epistémica / magnitud causal;
- rechazo de una tabla E→`w` como definición intrínseca de `w`;
- estatuto histórico/provisional de las tres calibraciones;
- necesidad de reconstruir combinación de evidencia.

### Permanece abierto

- estimador operativo de `ŵ`;
- definición matemática definitiva de `U(ŵ)`;
- calibración de amplitudes/perfiles de incertidumbre;
- perfiles por dominio;
- reglas de combinación de fuentes;
- tratamiento formal de dependencia entre fuentes;
- representación de aristas hipotéticas/no acreditadas;
- recalibración de ejemplos y análisis de sensibilidad.

Estas deudas no reabren la adjudicación conceptual.

---

## 16. Resolución consolidada

`RES-EVID-001` fija:

> **La escala E no mide magnitud causal. E1–E8 clasifican el estatuto epistémico de la evidencia que acredita una arista y contribuyen a determinar la incertidumbre de la estimación de su peso `w`; no determinan su valor esperado ni la posición de su intervalo. E0 es un estado especial de nulidad causal positivamente documentada y no pertenece a la jerarquía ordinal E1–E8. La ausencia o insuficiencia de evidencia constituye un estado distinto —arista hipotética o no acreditada— que no puede representarse mediante `w=0`. La magnitud causal debe estimarse a partir del mecanismo y del contenido sustantivo de la evidencia; la clase E informa cuán precisamente puede sostenerse esa estimación.**

La tensión E0–E8 queda cerrada como contradicción conceptual/metrológica. La calibración numérica y la implementación de incertidumbre quedan diferidas a segunda edición y validación empírica.