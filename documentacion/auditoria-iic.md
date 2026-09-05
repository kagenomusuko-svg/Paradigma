# AUD-IIC-001 — Auditoría MANT del Índice de Integridad Causal

> **Documento derivado de auditoría.** No modifica fuentes canónicas ni adjudica todavía la normalización definitiva de la escala o del estimador de IIC.

- **ID:** `AUD-IIC-001`
- **Estado:** CONCEPTO ESTABLE / ESCALA Y MEDICIÓN FORMALMENTE INCONSISTENTES
- **Familia:** `IIC`, `c_k`, ajuste de pesos por congruencia, fraude annona
- **Obras contrastadas:** *Metrología Causal* I, *Metrología Causal* II
- **Revisiones vinculadas:** `review.mci.iic_definition`, `review.mci.iic_circularity`, `review.mci.w_iic_bounds`, `review.calc.IIC_scale`, `review.calc.IIC_measurement`

## 1. Núcleo conceptual estable

El IIC mide la congruencia entre:

- el campo/diseño que una institución o nodo de diseño declaró que produciría;
- el campo/operación que efectivamente produjo.

La interpretación nuclear permanece estable:

- IIC alto → alta congruencia entre declaración y operación;
- IIC bajo → gran brecha entre declaración y operación;
- el índice no mide intención, culpa moral ni legalidad;
- su función es describir una propiedad del diseño institucional respecto del resultado `D` analizado.

No se observa una tensión doctrinal comparable a Aego.

## 2. Primera formulación — Metrología Causal I

*Metrología Causal* I, III·9 presenta:

`IIC=(1/n)Σ_k c_k`

con:

`c_k=corr(declarado_k,observable_k)`

y declara:

`c_k∈[0,1]`, `IIC∈[0,1]`.

Interpreta:

- `IIC=0` como brecha total;
- `IIC=1` como congruencia total.

Esta formulación trata IIC como un índice de congruencia no negativo.

## 3. Segunda formulación — Metrología Causal II

*Metrología Causal* II, II·2 conserva la misma forma media:

`IIC=(1/n)Σ_k c_k`,

pero ahora establece correctamente para una correlación estándar:

`c_k∈[-1,1]`.

Interpreta:

- `IIC=1`: congruencia total;
- `IIC=0`: ausencia de correlación;
- `IIC<0`: divergencia sistemática, donde el campo real opera en dirección opuesta al declarado.

La segunda formulación cambia la semántica del cero y amplía el codominio.

## 4. La escala no está normalizada transversalmente

Las dos formulaciones no pueden utilizarse indistintamente:

### Escala no negativa

`IIC∈[0,1]`

permite leer `0` como máxima incongruencia.

### Escala correlacional

`IIC∈[-1,1]`

hace que:

- `-1` sea oposición perfecta;
- `0` sea ausencia de asociación;
- `1` sea coincidencia direccional perfecta.

Por tanto `review.mci.iic_definition` y `review.calc.IIC_scale` quedan confirmadas como problema real de **escala y semántica**, no de doctrina.

La segunda edición deberá escoger una escala canónica o distinguir dos objetos con nombres diferentes.

## 5. Inconsistencia interna de Metrología Causal II con fraude annona

En II·2 se permite `IIC<0`.

Sin embargo, IV·5 vuelve a imponer:

`IIC_D∈[0,1]`

y define:

`Fraude_annona_D=R*_D(1−α_D)(1−IIC_D)`.

Afirma además que:

- fraude annona pertenece a `[0,1]`;
- el máximo ocurre en `R*=1`, `α=0`, `IIC=0`;
- `IIC=0` representa el campo real opuesto al declarado.

Esto contradice la semántica correlacional de II·2.

Si `IIC=-1` es admisible, entonces:

`1−IIC=2`

y con `R*=1`, `α=0`:

`Fraude_annona=2`.

Por tanto:

- la cota `[0,1]` deja de ser válida;
- `IIC=0` deja de ser el máximo de divergencia;
- el máximo declarado en IV·5 no es máximo bajo la escala de II·2.

Éste es un **error formal confirmado de composición de escalas**.

## 6. El problema de llamar correlación a c_k

La notación:

`c_k=corr(declarado_k,observable_k)`

sólo es una correlación estadística si existen dos series/vectorizaciones comparables con variación suficiente y una definición explícita del coeficiente.

En muchos protocolos, lo declarado puede ser un objetivo constante —por ejemplo, “100% de operaciones debe cumplir el control”—. Una serie constante tiene varianza cero y una correlación de Pearson con ella no está definida.

Además, el propio Vol. II permite “estimar cualitativamente” `c_k` mediante bandas interpretativas. Un score cualitativo asignado por evidencia no es por ello una correlación estadística.

Por tanto `review.calc.IIC_measurement` queda confirmada como problema metrológico:

> el corpus mezcla **correlación estadística**, **grado de cumplimiento/congruencia** y **score cualitativo de similitud** bajo el mismo símbolo `c_k`.

La segunda edición deberá elegir o tipar explícitamente cada estimador.

## 7. Promediar c_k requiere reglas adicionales

Incluso si cada `c_k` estuviera bien definido, la media simple:

`IIC=(1/n)Σc_k`

presupone que todos los protocolos relevantes tienen el mismo peso.

El corpus no demuestra que esa ponderación uniforme sea universalmente adecuada.

También quedan abiertas preguntas sobre:

- protocolos con distinta materialidad respecto de `D`;
- diferente calidad de evidencia;
- dependencia entre protocolos;
- protocolos redundantes;
- múltiples observables por protocolo;
- valores faltantes o no estimables.

La igualdad de pesos es una **calibración/model choice**, no una consecuencia ontológica.

## 8. Ajuste de pesos por IIC

Metrología II propone:

`w_ij(aj)=w_ij(base)·[1+k(1−IIC_D)]`

con `k∈[0.5,1.5]`.

Si se adopta `IIC∈[0,1]`, el factor está en:

`[1, 1+k]`.

Si se adopta `IIC∈[-1,1]`, el factor puede llegar a:

`1+2k`,

que con `k=1.5` alcanza `4`.

Por tanto `review.mci.w_iic_bounds` depende directamente de la normalización de escala.

La renormalización posterior puede devolver pesos a una escala proporcional, pero no resuelve por sí misma la pregunta de qué magnitud causal representa el factor ni qué sensibilidad es admisible.

## 9. ¿Existe circularidad IIC ↔ R*?

El texto dice que Serie II nunca se aplica sin Serie I previa y que IIC necesita contexto causal de R*.

Leído operativamente, el pipeline es:

`R*_base → identificar nodo de diseño/protocolos relevantes → IIC → ajustar W → R*_ajustado`.

Esta secuencia **no es circularidad matemática** si:

- `R*_base` y `R*_ajustado` se distinguen;
- IIC se calcula desde variables declaradas/observables independientes del valor de `R*_ajustado`;
- no se reitera automáticamente hasta un punto fijo.

Por tanto `review.mci.iic_circularity` no se confirma como contradicción inevitable.

Clasificación:

- dependencia secuencial: sí;
- circularidad algebraica necesaria: no;
- posible dependencia de selección/path dependence: sí, porque el R* base participa en identificar el nodo de diseño relevante y el conjunto de protocolos.

La segunda edición debe hacer explícita la notación `R*_base` / `R*_aj`.

## 10. Problema adicional: doble modulación potencial

En Serie II, IIC afecta primero a `W` y por tanto a `R*_ajustado`.

Después el fraude annona vuelve a multiplicar por:

`(1−IIC)`.

Por tanto la misma brecha de congruencia interviene:

1. indirectamente dentro de `R*_ajustado`;
2. directamente como factor adicional del índice de fraude annona.

Esto no es automáticamente un error: puede ser una decisión de modelo deliberada si ambas apariciones representan efectos distintos.

Pero el corpus lo presenta como “identidad matemática” derivada sin demostrar por qué la doble entrada de IIC no constituye doble contabilización.

Debe quedar como revisión formal específica de segunda edición.

## 11. Fraude annona no es una identidad matemática por mera multiplicación

La expresión:

`Fraude_annona=R*(1−α)(1−IIC)`

es un **índice/modelo construido** salvo que se derive de definiciones previas que obliguen a esa multiplicación.

El hecho de que tres factores pertenezcan a un intervalo no hace que su producto sea una identidad matemática necesaria del sistema.

La segunda edición deberá presentar su estatus correctamente:

- definición de índice;
- modelo de interacción;
- o resultado derivado, si se aporta una demostración real.

Lo mismo vale para el umbral `0.20`: es una calibración/criterio operativo y requiere evidencia o debe etiquetarse como umbral convencional revisable.

## 12. Normalización conceptual de trabajo

Hasta segunda edición, conviene distinguir:

`IIC_cong`

= índice de congruencia normalizado, potencialmente en `[0,1]`.

`ρ_decl,obs`

= correlación estadística real, si existe una serie válida, en `[-1,1]`.

`c_app`

= score aplicado/estimado cualitativamente desde evidencia documental.

Esta nomenclatura es de auditoría, no canon.

## 13. Clasificación final

- **Concepto doctrinal de IIC:** estable.
- **Escala única vigente:** no.
- **Semántica de cero estable:** no.
- **Uso de correlación estadística bien especificado:** no.
- **Promedio uniforme demostrado:** no.
- **Ajuste de W sensible a la escala:** sí.
- **Circularidad R*↔IIC inevitable:** no; hay pipeline secuencial si se distingue base/ajustado.
- **Doble modulación IIC en R* y fraude annona:** revisión abierta.
- **Cota de fraude annona `[0,1]` bajo IIC negativo:** falsa.
- **Umbral 0.20 como teorema:** no; calibración/criterio operativo.
- **Normalización de segunda edición:** necesaria.

## 14. Pendiente

La segunda edición deberá decidir:

1. si IIC canónico vive en `[0,1]` o `[-1,1]`;
2. si “oposición” debe distinguirse de “incongruencia máxima”;
3. qué función concreta mide congruencia cuando no existe una correlación estadística legítima;
4. cómo ponderar protocolos;
5. cómo ajustar W bajo la escala elegida;
6. si la segunda aparición de `(1−IIC)` en fraude annona representa un efecto distinto o doble contabilización;
7. cómo recalibrar umbrales y ejemplos aguas abajo.
