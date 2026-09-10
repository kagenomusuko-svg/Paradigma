# RES-IIC-001 — Resolución MANT de escala, semántica y composición del Índice de Integridad Causal

> **Documento derivado de resolución.** No modifica fuentes canónicas ni ejecuta recálculos de segunda edición. Adjudica la arquitectura formal necesaria para que las formulaciones históricas de IIC puedan convivir sin confundir objetos distintos.

- **ID:** `RES-IIC-001`
- **Estado:** RESUELTO EN NÚCLEO CONCEPTUAL Y FORMAL / CALIBRACIÓN Y MEDICIÓN ABIERTAS
- **Familia:** `IIC`, `c_k`, compliance causal, ajuste de `W`, fraude annona
- **Autoridades contrastadas:** *Metrología Causal* I, III·9; *Metrología Causal* II, II·2 y IV·5
- **Auditoría de origen:** `AUD-IIC-001`
- **Revisiones vinculadas:** `review.mci.iic_definition`, `review.mci.iic_circularity`, `review.mci.w_iic_bounds`, `review.calc.IIC_scale`, `review.calc.IIC_measurement`

## 1. Problema adjudicado

El corpus mantiene estable el objeto conceptual de IIC pero utiliza bajo el mismo símbolo al menos tres objetos formales distintos:

1. una correlación estadística entre variables declaradas y observables;
2. un índice normalizado de congruencia entre diseño declarado y operación real;
3. un score cualitativo capaz de distinguir divergencia direccional u oposición.

La tensión histórica `[0,1]` frente a `[-1,1]` no se resuelve escogiendo cuál de las dos escalas «era la correcta» para todo uso. Se resuelve tipando correctamente los objetos que fueron colapsados bajo `c_k`/IIC.

## 2. Núcleo doctrinal que se conserva

**Explícito en el corpus:** IIC mide la congruencia o brecha entre el campo que un nodo de diseño declaró producir y el campo que efectivamente produjo, restringido a protocolos relevantes para el resultado `D`.

Por tanto:

- IIC alto significa alta congruencia entre declaración y operación;
- IIC bajo significa brecha alta;
- IIC no mide intención, culpa moral ni legalidad;
- su objeto es una propiedad del diseño/operación institucional en relación con `D`.

Esta doctrina permanece vigente.

## 3. Adjudicación de escala canónica

Se fija como representación canónica de trabajo:

`IIC_cong ∈ [0,1]`

con:

- `IIC_cong = 1`: congruencia total;
- `IIC_cong = 0`: brecha total o congruencia nula dentro del índice no direccional.

En segunda edición el símbolo ordinario `IIC` deberá reservarse para este objeto salvo decisión editorial posterior explícita.

La razón no es meramente conservadora. La escala `[0,1]` preserva la semántica de índice de congruencia que aparece en MC-I y mantiene bien tipadas las expresiones aguas abajo que usan `1−IIC`, siempre que su estatus como decisiones de modelo se conserve.

## 4. `IIC=0` no significa «campo opuesto»

Se corrige la composición semántica introducida en MC-II.

`IIC=0` significa congruencia nula o brecha máxima dentro del índice no direccional.

La proposición «el campo real opera en dirección opuesta al declarado» contiene información adicional: no sólo ausencia de congruencia, sino **dirección de la divergencia**. Esa información no debe colapsarse en el mismo objeto.

Por claridad terminológica, esta resolución habla de **semántica de `IIC=0`** y no de «E0 de IIC», porque `E0` ya designa en `RES-EVID-001` la nulidad causal documentada de una arista y pertenece a otra familia conceptual.

## 5. Correlación estadística y score direccional son objetos distintos

### 5.1 Correlación estadística real

Si existen dos series cuantitativas comparables, con definición estadística legítima y varianza suficiente, puede calcularse una correlación:

`ρ_decl,obs ∈ [-1,1]`.

Ese objeto puede distinguir asociación positiva, ausencia de asociación y asociación negativa.

No es idéntico a IIC.

Una variable declarada constante puede volver indefinida una correlación de Pearson, por lo que el uso de la palabra «correlación» no puede extenderse automáticamente a todos los protocolos.

### 5.2 Divergencia direccional aplicada

La categoría de MC-II `c_k < 0`, donde el campo real produce el efecto opuesto al declarado, conserva valor analítico pero deberá tiparse como objeto direccional separado del IIC canónico.

Esta resolución no impone todavía símbolo definitivo. Notaciones como `IIC_dir`, `d_k` o una transformación explícita de `ρ_decl,obs` pertenecen a la reparación editorial/metrológica de segunda edición.

## 6. El score cualitativo no debe llamarse correlación

La tabla cualitativa de MC-II puede conservar su función operacional como evaluación documentada de congruencia, pero su estimación cualitativa no constituye por sí misma una correlación estadística.

La segunda edición deberá distinguir al menos:

- medición estadística real, cuando sea posible;
- índice aplicado de congruencia por protocolo;
- señal direccional de oposición, cuando la evidencia la sostenga.

El nombre operativo recomendado para el objeto por protocolo es «índice de congruencia por protocolo» o equivalente, no `corr(...)` salvo que efectivamente se calcule una correlación.

## 7. Media de protocolos: modelo, no consecuencia ontológica

La forma histórica:

`IIC = (1/n) Σ_k c_k`

puede mantenerse como agregador provisional, pero la ponderación uniforme no se eleva a teorema ni a necesidad ontológica.

Debe quedar abierta una familia general:

`IIC = Σ_k λ_k g_k`, con `λ_k ≥ 0` y `Σ_k λ_k = 1`,

como forma editorial/metrológica de expresar que distintos protocolos pueden tener diferente materialidad respecto de `D`.

La elección de `λ_k`, la función `g_k`, el tratamiento de dependencias, redundancias, valores faltantes y calidad de evidencia permanecen abiertos a calibración.

La fórmula ponderada anterior se registra como **arquitectura editorial general**, no como fórmula canónica ya validada por el corpus.

## 8. Ajuste de pesos por IIC

MC-II propone:

`w_ij(aj)=w_ij(base)·[1+k(1−IIC_D)]`.

Con `IIC_D ∈ [0,1]`, el factor de amplificación permanece acotado entre `1` y `1+k`.

Esta resolución conserva la **compatibilidad de dominio** del ajuste, pero no declara validada su calibración, su magnitud causal ni el rango histórico `k∈[0.5,1.5]`.

El pipeline correcto continúa siendo secuencial:

`R*_base → identificar nodo de diseño/protocolos → IIC → ajustar W → R*_aj`.

No hay circularidad algebraica necesaria si `R*_base` y `R*_aj` se distinguen y el IIC se estima desde variables independientes del valor final de `R*_aj`.

## 9. Doble modulación: resuelta como distinción de función, no como teorema

El mismo IIC aparece históricamente en dos lugares:

1. ajuste de `W`, que modifica `R*_aj`;
2. factor `(1−IIC)` dentro del índice de fraude annona.

La lectura transversal del corpus permite distinguir sus funciones:

- en el ajuste de `W`, la brecha de congruencia se modela como parte de la estructura causal atribuida al nodo de diseño;
- en fraude annona, la brecha se usa como componente de un índice de gravedad/compliance que combina centralidad causal, asunción y congruencia declarada/real.

Por tanto, la doble aparición **no es por definición doble contabilización**, siempre que ambas funciones se declaren separadamente.

Sin embargo, esta distinción conceptual no demuestra que la segunda multiplicación sea necesaria, óptima o empíricamente calibrada. `Fraude_annona = R*(1−α)(1−IIC)` continúa siendo un índice/modelo construido salvo derivación independiente.

Así se resuelve la ambigüedad semántica sin convertir una decisión de modelo en identidad matemática.

## 10. Fraude annona bajo la escala canónica

Con:

- `R* ∈ [0,1]` bajo la normalización vigente;
- `α ∈ [0,1]` en su capa aplicada correspondiente;
- `IIC ∈ [0,1]`;

la expresión histórica:

`Fraude_annona = R*(1−α)(1−IIC)`

queda al menos bien tipada en `[0,1]`.

Esto **no** valida automáticamente:

- su forma multiplicativa;
- el nombre «corolario»;
- el umbral `0.20`;
- la interpretación regulatoria transversal;
- la independencia estadística o causal entre los factores.

Esos puntos permanecen como calibración/model choice y deberán tratarse editorialmente como tales.

## 11. Lo que queda resuelto

Quedan adjudicados:

- el objeto conceptual de IIC;
- la escala canónica `[0,1]` para el índice de congruencia;
- la semántica de `IIC=0`;
- la separación entre IIC, correlación estadística y divergencia direccional;
- la impropiedad de llamar «correlación» a una estimación cualitativa sin estimador estadístico real;
- la compatibilidad de dominio de `1−IIC` con el ajuste de `W` y fraude annona;
- la inexistencia de circularidad matemática necesaria en el pipeline base→ajustado;
- la interpretación diferenciada de las dos apariciones de IIC.

## 12. Lo que permanece abierto

No se resuelven ni se inventan:

- estimador operativo universal de congruencia;
- transformación entre correlación real y score de congruencia;
- símbolo definitivo para divergencia direccional;
- ponderación de protocolos por materialidad;
- dependencia/redundancia entre protocolos;
- calibración de `k`;
- validación causal del ajuste de `W`;
- calibración empírica del fraude annona;
- umbral `0.20`;
- recálculo de ejemplos históricos.

## 13. Consecuencia editorial

La segunda edición deberá reescribir MC-I III·9 y MC-II II·2/IV·5 de modo que el lector vea tres objetos separados:

`congruencia no direccional → IIC ∈ [0,1]`

`correlación estadística real → ρ ∈ [-1,1], si está definida`

`oposición/divergencia direccional → objeto separado, si la evidencia la sostiene`.

Ningún pasaje deberá volver a tratar estos tres objetos como si fueran la misma magnitud.
