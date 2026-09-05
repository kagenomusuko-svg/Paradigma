# AUD-RSC-IT-001 — Auditoría MANT de RSC, I(t) e irreversibilidad

> **Documento derivado de auditoría.** No modifica fuentes canónicas ni reabre las resoluciones vigentes de α, Δ o R*.

- **ID:** `AUD-RSC-IT-001`
- **Estado:** DOCTRINA ESTABLE / FORMALIZACIÓN DEFECTUOSA
- **Objetos:** `RSC(t)`, `I(t)`, `φ₂`, irreversibilidad, indicador de integración
- **Obras contrastadas:** *Caos* y *Axiomatización del sistema de la doble mediación*

## 1. Irreversibilidad ontológica en Caos

*Caos* formula la irreversibilidad principalmente como propiedad del **acto ya ocurrido**:

- lo posible se vuelve hecho;
- el acto no puede convertirse retrospectivamente en no-acto;
- una vez producido, modifica el campo de posibilidades futuras;
- la segunda mediación puede recontextualizar el acto, pero no hacer que no haya ocurrido.

Esta tesis no exige por sí sola que toda representación vectorial resumida del ego sea inyectiva en el tiempo ni que `I(t₂) ≠ I(t₁)` para todo `t₂>t₁`.

La distinción es crucial:

`irreversibilidad del evento ≠ imposibilidad algebraica de cancelación en un agregado vectorial`.

## 2. Definición publicada de I(t)

*Axiomatización* define:

`I(t)=∫_0^t c(τ)w(τ)dτ ∈ E`,

con `E` espacio vectorial/Banach y `w≥0`.

También define `φ₂` mediante actualizaciones:

`I(t+Δt)=I(t)+δ(a)·1_{eval(a,I)>θ}`.

Y más adelante afirma que `I(t)` es la integral de los colapsos que `φ₂` aceptó.

Estas formulaciones no son automáticamente equivalentes.

La integral `∫c(τ)w(τ)dτ` incluye todo valor de `c(τ)` salvo que `c` haya sido previamente redefinida como función de colapsos aceptados. Pero `RSC(t)` usa la misma `c` para representar **todos** los colapsos producidos, aceptados o rechazados.

Por tanto existe una inconsistencia de representación:

- `c` no puede ser simultáneamente, sin tipado adicional, “todos los colapsos” y “sólo los integrados”;
- la fórmula integral carece del indicador de aceptación que sí aparece en `φ₂`.

Una reparación futura deberá distinguir, por ejemplo, un flujo de eventos producidos de un flujo/medida de eventos integrados.

## 3. El Teorema 2.1 de irreversibilidad es falso bajo las hipótesis declaradas

El teorema pretende demostrar que, si `w(τ)>0` y `c(τ)≠0` en un conjunto de medida positiva, entonces:

`||I(t₂)−I(t₁)||_E>0`.

El paso decisivo afirma que si un integrando vectorial `g` es no nulo en un conjunto de medida positiva, entonces su integral tiene norma positiva.

Eso es falso en general.

Contraejemplo escalar, que ya basta porque `ℝ` es un espacio de Banach:

`g(τ)=1` en la primera mitad del intervalo y `g(τ)=−1` en la segunda mitad.

`g` es no nula en todo el intervalo, pero:

`∫g(τ)dτ=0`.

En un espacio vectorial, colapsos orientados en direcciones opuestas pueden cancelarse igualmente.

Por tanto:

`review.axiom.irreversibility`

queda confirmada como **error formal**.

## 4. La actualización φ₂ tampoco garantiza no-retorno

La regla:

`I_{t+1}=I_t+δ(a)`

para un colapso aceptado permite que un `δ(a)` posterior sea opuesto a una contribución previa.

La condición publicada:

`||δ(a)||≤||a||`

impide amplificación, pero no cancelación.

Luego tampoco la representación discreta de `φ₂` garantiza por sí sola:

`I(t₂)≠I(t₁)`.

Si se desea imponer esa propiedad sobre `I` y no sólo sobre el registro histórico, hace falta una estructura adicional no declarada: por ejemplo un cono sin cancelación, un estado aumentado con memoria o una construcción inyectiva sobre eventos.

La auditoría no adjudica cuál.

## 5. RSC(t) está mal tipado para la función que se le asigna

*Axiomatización* define:

`RSC(t)={c(τ):τ∈[0,t]}⊆E`.

Es decir, `RSC(t)` es un **conjunto de valores** en `E`.

Luego usa:

`RSC(t) \ I(t)`

para representar colapsos rechazados.

Pero:

- `RSC(t)` es un conjunto;
- `I(t)` es un elemento de `E`, no un subconjunto de `RSC(t)`.

La diferencia de conjuntos está mal tipada.

Lo mismo ocurre con expresiones posteriores como:

`c(τ) ∈ I(t)`

y:

`A_D ∩ I(t)`.

Un vector agregado no es el conjunto de eventos que fueron integrados.

Por tanto `review.axiom.rsc_type` queda confirmada como **incompatibilidad de tipos**.

## 6. RSC como conjunto pierde información necesaria

Incluso si se corrigiera la diferencia de conjuntos, definir `RSC` como mera imagen de `c` elimina información relevante:

- dos colapsos idénticos ocurridos en momentos distintos aparecen como un solo elemento del conjunto;
- se pierde multiplicidad;
- se pierde orden temporal;
- no queda asociada la decisión de integración/rechazo a cada ocurrencia;
- no queda asociada su profundidad, alcance o peso.

Para calcular proporciones históricas, α o trayectorias de integración hace falta un registro **indexado por evento/tiempo**, una secuencia/multiconjunto o una medida marcada, no sólo el conjunto imagen.

## 7. Propiedad correcta que sí puede preservar la irreversibilidad

La tesis de *Caos* puede preservarse sin exigir que una proyección vectorial nunca se repita.

Si `RSC` se tipa como registro de eventos:

`e_k=(t_k,a_k,...)`,

entonces la irreversibilidad factual se expresa como monotonía histórica del registro:

`RSC(t₁) ⊆ RSC(t₂)` para `t₂>t₁`

en el sentido de eventos indexados, no de valores vectoriales únicos.

El acto pasado permanece registrado aunque su efecto agregado sea después contrapesado o recontextualizado.

Esto corresponde mejor a la tesis ontológica:

> el acto puede ser integrado de otra manera en el futuro, pero no puede dejar de haber ocurrido.

Esta formulación es una **propuesta de reparación**, no canon todavía.

## 8. I(t) puede conservarse como estado derivado

Nada obliga a eliminar `I(t)` como objeto vectorial.

Puede tiparse como una proyección/estado agregado derivado del historial integrado:

`historial de eventos → operador de integración → I(t)`.

En ese caso:

- `RSC` conserva factualidad, multiplicidad y temporalidad;
- un subconjunto/registro `RSC_int` conserva qué eventos fueron integrados;
- `I(t)` resume geométricamente la trayectoria integrada;
- que `I(t₂)=I(t₁)` no borraría los eventos intermedios.

Esto separa memoria ontológica de estado agregado.

## 9. Impacto sobre α histórico

La Parte IV de *Axiomatización* define el indicador de integración mediante expresiones como:

`c(τ)∈I(t)`

y usa `RSC(t)\I(t)` para los rechazados.

Esas expresiones heredan el error de tipado.

Sin embargo, esto **no reabre `RES-ALPHA-001`**.

La resolución vigente de α ya separó:

- genealogía interna de integración;
- operacionalización aplicada de asunción efectiva.

Lo que debe corregirse en segunda edición es la representación formal histórica del registro/indicador, no la definición vigente de α.

## 10. La versión discreta con delta de Dirac tampoco es caso literal de la continua

La Definición 4 exige inicialmente:

`w:T→ℝ₊`

medible y acotada.

Después afirma que la versión discreta se obtiene tomando:

`w(τ)=Σ_i δ(τ−t_i)`.

La delta de Dirac no es una función real ordinaria medible y acotada bajo esas hipótesis; es una medida/distribución.

Por tanto la versión discreta no es literalmente un caso particular de la definición continua tal como está tipada.

Puede repararse usando una medida de eventos/medida de Dirac desde el inicio, pero eso requiere cambiar el tipo matemático de `w` o formular separadamente el caso discreto.

## 11. Clasificación final

- **Tesis ontológica de irreversibilidad:** estable.
- **Irreversibilidad factual del acto:** coherente con el corpus.
- **Teorema `||I(t₂)−I(t₁)||>0` bajo hipótesis publicadas:** falso.
- **RSC como registro histórico:** intuición válida, tipo publicado insuficiente.
- **`RSC\I`, `c∈I`, `A_D∩I`:** errores de tipos.
- **I como integral de todos vs. sólo aceptados:** inconsistencia de representación.
- **Dirac como w acotada:** error de tipado/medida.
- **Doctrina que deba adjudicarse nuevamente:** no.

## 12. Revisiones

- `review.axiom.rsc_type`: confirmada — error de tipos y pérdida de multiplicidad/tiempo.
- `review.axiom.irreversibility`: confirmada — demostración inválida y propiedad no garantizada.
- `review.axiom.phi2_integration`: confirmada — inconsistencia entre flujo producido, flujo aceptado e integral acumulativa.

## 13. Pendiente de segunda edición

La corrección deberá decidir una representación formal que conserve simultáneamente:

1. cada evento ocurrido;
2. multiplicidad y orden temporal;
3. integración/rechazo por evento;
4. profundidad/alcance/peso cuando corresponda;
5. un estado agregado `I(t)` si sigue siendo útil;
6. imposibilidad de borrar retrospectivamente un evento;
7. posibilidad de recontextualizar su efecto sin confundir recontextualización con no-ocurrencia.

No deberá volver a inferirse irreversibilidad histórica a partir de la sola ausencia de cancelación en una suma vectorial salvo que se impongan y demuestren condiciones geométricas suficientes.
