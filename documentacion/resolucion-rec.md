# RES-REC-001 — Resolución MANT de la Relación de Escala del Conocimiento

> **Documento derivado de resolución.** No modifica fuentes canónicas ni ejecuta recálculos de segunda edición. Adjudica qué parte de la REC publicada está realmente demostrada, qué parte contiene un error formal y qué resultados requieren supuestos más estrechos.

- **ID:** `RES-REC-001`
- **Estado:** ERROR FORMAL RESUELTO / RESULTADO CONDICIONAL CONSERVADO / GENERALIZACIÓN ABIERTA
- **Familia:** `REC`, `τ`, Fisher, Cramér–Rao, `ΔI`, `Δh`, `τ_eff`
- **Autoridad principal:** *Axiomatización del sistema de la doble mediación*, Parte VII
- **Auditoría de origen:** `AUD-REC-001`

## 1. Problema adjudicado

La Parte VII contiene una cadena formal con dos niveles que deben separarse:

1. los Lemas 7.1–7.2, que bajo una parametrización logística específica producen una cota de producto;
2. el Teorema 7, que sustituye esa cota por otra con factor `4τ₀²` mediante un Paso 2 inválido.

La resolución no elimina la intuición informacional de la Parte VII. Corrige el estatus de sus afirmaciones matemáticas.

## 2. Resultado que sí se sigue de la cadena publicada

Bajo el modelo efectivamente usado en la demostración:

`h_k(θ)=σ((θ−θ_k)/τ)`

con observación Bernoulli one-vs-rest y las condiciones regulares necesarias para aplicar Cramér–Rao, el Lema 7.1 obtiene:

`F(θ)=h_k(1−h_k)/τ²`.

El Lema 7.2 deriva:

`Var(Î) ≥ τ²/[n h_k(1−h_k)]`

`Var(ĥ) ≥ h_k(1−h_k)/n`

por lo que:

`Var(Î)Var(ĥ) ≥ τ²/n²`.

Tomando raíces:

`ΔI·Δh ≥ τ/n`.

Para una cota inferior `τ≥τ₀>0`, la consecuencia directa es:

`ΔI·Δh ≥ τ₀/n`

o equivalentemente:

`n(ΔI·Δh) ≥ τ₀`.

Ésta es la única cota de escala que la cadena algebraica publicada justifica sin un argumento adicional.

## 3. La forma canónica con factor 4 no está demostrada

El Teorema 7 publica:

`n(ΔI·Δh) ≥ 4τ₀²`.

Esa forma no se sigue del Lema 7.2.

La dependencia respecto de `τ₀` cambia de lineal a cuadrática:

`τ₀` frente a `4τ₀²`.

No existe equivalencia algebraica general entre ambas expresiones. Para `τ₀>0` coinciden únicamente en el valor particular `τ₀=1/4`.

Por tanto quedan rechazadas como afirmaciones formales generales:

- la equivalencia entre ambas cotas;
- el factor `4` como consecuencia del Lema 7.2;
- la afirmación de que la forma `4τ₀²` es simplemente una versión «más conservadora» de la cota demostrada.

## 4. Error formal del Paso 2

El Paso 2 afirma correctamente que:

`τ²/[n h(1−h)]`

aumenta cuando `h(1−h)` disminuye.

Pero luego evalúa en:

`h=1/2`,

donde:

`h(1−h)=1/4`

es máximo, no mínimo.

Por tanto, en `h=1/2`, la cota inferior de `Var(Î)` es mínima:

`Var(Î) ≥ 4τ²/n`.

La misma elección produce para la otra cota:

`Var(ĥ) ≥ 1/(4n)`.

Al multiplicarlas:

`[4τ²/n]·[1/(4n)] = τ²/n²`.

No aparece ningún factor adicional: se recupera exactamente la cota del Lema 7.2.

Además, ambas expresiones dependen del mismo `h`; no pueden tratarse como extremos independientes para fabricar una cota universal diferente.

## 5. Alcance real del Lema 7.1

El enunciado de la Parte VII introduce:

`h_k(θ)=softmax_k(z(θ))`.

La demostración, sin embargo, sustituye ese objeto por:

`h_k(θ)=σ((θ−θ_k)/τ)`

y usa:

`dh_k/dθ=h_k(1−h_k)/τ`.

Esta derivada corresponde a una parametrización logística binaria específica. No es la derivada general de un componente softmax respecto de un parámetro escalar arbitrario sin especificar cómo dependen de `θ` todos los logits.

Por tanto:

- el Lema 7.1 puede conservarse como resultado para una **logística Bernoulli one-vs-rest explícitamente parametrizada**;
- no está demostrado como resultado universal para softmax general;
- tampoco equivale automáticamente a una cota para el vector multinomial completo `h(t)`.

La cota `ΔI·Δh≥τ/n` se conserva, por ello, como **resultado condicional del modelo publicado**, no como ley universal de todos los sistemas de doble mediación.

## 6. Corolario 7.1 y `τ_eff`

El texto define:

`τ_eff=τ₀/√n`

y afirma:

`ΔI·Δh ≥ 4τ_eff² = 4τ₀²/n`.

Esta reparametrización no corrige el error del Teorema 7. La cota que deriva del Lema 7.2 sigue siendo:

`ΔI·Δh ≥ τ₀/n`.

Una definición nueva de `τ_eff` no puede cambiar la dependencia funcional de la desigualdad original sin una derivación adicional.

Por tanto el Corolario 7.1 deberá reconstruirse editorialmente. Puede conservarse la observación de que la incertidumbre disminuye con más observaciones bajo el modelo estadístico, pero no la identidad local `4τ_eff²` como consecuencia demostrada de los lemas.

## 7. Corolario 7.2: predictibilidad

El propio texto declara que su argumento es cualitativo y no una demostración cerrada. Esta clasificación se vuelve normativa para la lectura de segunda edición.

En particular, la afirmación universal:

`max_k h_k < 1/2`

en alguna región para todo `τ>0` no puede sostenerse en el caso binario, porque para dos clases:

`h_1+h_2=1`

y necesariamente:

`max(h_1,h_2)≥1/2`.

La relación entre temperatura y error predictivo puede conservarse como hipótesis o consecuencia interpretativa dependiente del modelo, no como corolario matemático universal de la REC.

## 8. Tabla `η(τ)`

La función histórica:

`η(τ)=1/2·τ/(1+τ)`

ya es reconocida por el propio texto como heurística y eliminada del cuerpo formal.

La tabla numérica puede conservarse únicamente si queda visual y textualmente separada de teoremas y lemas, con estatus inequívoco de:

- estimación orientativa;
- heurística ilustrativa;
- no cota teórica demostrada.

No debe utilizarse como evidencia retrospectiva de la REC ni como calibración validada.

## 9. Núcleo informacional que se conserva

La Parte VII mantiene una intuición útil que no depende del factor 4:

- bajo el modelo estadístico explícito, aumentar `n` reduce la cota del producto de incertidumbres;
- para `n` fijo, una temperatura `τ` mayor aumenta la cota derivada `τ/n`;
- la barrera es de escala estadística y disminuye con la acumulación de observaciones;
- la analogía con Heisenberg no implica identidad física, conceptual ni metodológica.

Esto no autoriza por sí solo a convertir la intuición en una ley ontológica universal ni a inferir una función universal de error predictivo.

## 10. Qué queda resuelto

Queda adjudicado que:

- `n(ΔI·Δh)≥4τ₀²` no está demostrado por la Parte VII;
- el factor `4` se introduce mediante un argumento formal inválido;
- la frase «ambas formas son equivalentes» es falsa en general;
- el Corolario 7.1 no rescata la cota cuadrática mediante `τ_eff`;
- el Lema 7.1 debe restringirse a la parametrización logística que realmente demuestra;
- el modelo Bernoulli one-vs-rest no equivale automáticamente a un softmax multinomial general;
- el corolario de predictibilidad no es teorema universal;
- la tabla `η(τ)` es heurística.

## 11. Qué permanece abierto

No se decide ni se inventa todavía:

- una generalización correcta para softmax multinomial;
- una Fisher matricial para el vector completo de modos;
- dependencia entre componentes de `h`;
- estimadores concretos de `I(t)` y `h(t)` en aplicaciones reales;
- calibración empírica de `τ` en humanos o sistemas artificiales;
- una función universal entre `τ` y error predictivo;
- una derivación alternativa que produzca legítimamente un factor `4`;
- si la REC debe conservarse finalmente como teorema condicionado, modelo estadístico ilustrativo o resultado auxiliar.

## 12. Adjudicación de estatus

Hasta la segunda edición:

- **resultado formal conservable:** `ΔI·Δh≥τ₀/n`, sólo bajo los supuestos logístico-Bernoulli declarados correctamente;
- **REC canónica publicada con factor 4:** no demostrada;
- **generalización a softmax:** abierta;
- **predictibilidad:** interpretativa/heurística;
- **η(τ):** heurística orientativa.

La doctrina ontológica de la doble mediación no queda afectada por esta corrección: el problema se localiza en la formalización estadística de la Parte VII.
