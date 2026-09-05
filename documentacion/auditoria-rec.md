# AUD-REC-001 — Auditoría MANT de la Relación de Escala del Conocimiento

> **Documento derivado de auditoría.** No modifica fuentes canónicas ni adjudica todavía si la REC debe conservarse, reformularse o eliminarse en segunda edición.

- **ID:** `AUD-REC-001`
- **Estado:** ERROR FORMAL CONFIRMADO / IDEA INFORMACIONAL PENDIENTE DE REFORMULACIÓN
- **Familia:** `REC`, `τ`, Fisher, Cramér–Rao, `ΔI`, `Δh`, `τ_eff`
- **Obra principal:** *Axiomatización del sistema de la doble mediación*, Parte VII

## 1. Estructura publicada

La Parte VII intenta construir una cota informacional sobre la precisión simultánea de estimadores de `I(t)` y `h_k(t)`.

El Lema 7.1 propone:

`F(θ)=h_k(1−h_k)/τ²`

para una observación Bernoulli del modo `k`.

El Lema 7.2 deriva:

`Var(Î) ≥ τ²/[n h_k(1−h_k)]`

`Var(ĥ) ≥ h_k(1−h_k)/n`

por tanto:

`Var(Î)Var(ĥ) ≥ τ²/n²`.

Tomando raíces:

`ΔI·Δh ≥ τ/n`.

Hasta este punto, la cadena algebraica publicada es internamente coherente bajo los supuestos estadísticos declarados.

## 2. El Teorema 7 cambia de cota sin derivación válida

El Teorema 7 declara:

`n(ΔI·Δh) ≥ 4τ₀²`.

Pero su propio Paso 1 deriva:

`ΔI·Δh ≥ τ₀/n`

y por tanto:

`n(ΔI·Δh) ≥ τ₀`.

No existe una transformación algebraica general que convierta:

`τ₀`

en:

`4τ₀²`.

Las dos cotas sólo coinciden para valores particulares de `τ₀`, no de forma universal.

Por tanto la afirmación posterior de que ambas formas son “equivalentes” es falsa.

## 3. El factor 4 está introducido mediante un razonamiento contradictorio

El Paso 2 afirma que la cota:

`Var(Î) ≥ τ²/[n h(1−h)]`

se maximiza cuando `h(1−h)` es mínimo.

Eso es correcto.

Pero inmediatamente evalúa en:

`h=1/2`,

donde:

`h(1−h)=1/4`

es **máximo**, no mínimo.

Por tanto en `h=1/2` la cota inferior para `Var(Î)` es mínima:

`Var(Î) ≥ 4τ²/n`.

Cuando `h→0` o `h→1`, el denominador tiende a cero y esa cota diverge.

El argumento publicado usa simultáneamente “peor caso” y el punto que minimiza la cota de `Var(Î)`.

## 4. Combinar extremos separados no produce una nueva cota universal

El texto toma por separado valores extremos de las cotas de `Var(Î)` y `Var(ĥ)` para justificar el factor 4.

Pero la cota de producto ya fue derivada exactamente en el Lema 7.2:

`Var(Î)Var(ĥ) ≥ τ²/n²`.

Elegir máximos o mínimos separados de funciones que dependen del mismo `h` no permite reemplazar esa cota por otra sin una demostración adicional.

Además, el producto de las dos cotas puntuales ya cancela exactamente `h(1−h)` para cada `h` admisible.

No queda ningún factor 4 pendiente de “conservadurismo”.

## 5. La forma directa que sí se sigue del Lema 7.2

Bajo los supuestos publicados y sin entrar todavía a discutir si esos supuestos son adecuados, la consecuencia directa es:

`ΔI·Δh ≥ τ/n`.

Equivalente:

`n(ΔI·Δh) ≥ τ`.

Ésta es la única forma que el argumento presentado demuestra.

Esto no adjudica que dicha cota sea finalmente válida para el sistema completo; sólo identifica qué conclusión se sigue del lema tal como fue escrito.

## 6. Corolario 7.1 hereda la inconsistencia

El texto define:

`τ_eff=τ₀/√n`

y luego afirma:

`ΔI·Δh ≥ 4τ_eff² = 4τ₀²/n`.

Pero del Lema 7.2 se obtiene:

`ΔI·Δh ≥ τ₀/n`.

Estas expresiones tienen distinta dependencia funcional respecto de `τ₀`.

Por tanto la forma local de la REC no queda derivada por la definición de `τ_eff`.

## 7. Problema de dimensionalidad/escala

Si `τ` conserva unidades o escala compatible con el parámetro `θ`, entonces:

`ΔI·Δh`

tiene una dependencia lineal en `τ` en la derivación de Cramér–Rao, mientras la forma canónica publicada depende de `τ²`.

Incluso si `τ` se declara adimensional mediante normalización, la discrepancia algebraica permanece.

Por tanto el problema no se resuelve diciendo que `τ` es una temperatura normalizada.

## 8. Lema 7.1 requiere supuestos más estrechos de los declarados

La Parte VII comienza con:

`h_k(θ)=softmax_k(z(θ))`,

pero la demostración usa:

`h_k(θ)=σ((θ−θ_k)/τ)`

y:

`dh_k/dθ=h_k(1−h_k)/τ`.

Esa derivada es la forma logística binaria específica. No es la derivada general de un componente de softmax respecto de un parámetro escalar arbitrario `θ` sin especificar cómo dependen todos los logits de `θ`.

Por tanto el Lema 7.1, tal como está escrito, no es un resultado general para cualquier softmax: requiere una parametrización particular que debe declararse.

Clasificación:

- resultado potencialmente válido para un modelo logístico específico: sí;
- demostrado para el softmax general declarado: no.

## 9. El modelo Bernoulli del modo k también es una reducción específica

Modelar “el modo k ocurrió / no ocurrió” como Bernoulli puede ser una reducción one-vs-rest válida.

Pero eso no equivale automáticamente a modelar toda la distribución multinomial de modos.

Si la REC pretende hablar de `h(t)` como vector completo, la segunda edición deberá especificar si:

- la cota se aplica por componente;
- se usa Fisher multinomial;
- se agrega información entre modos;
- existe dependencia entre estimadores componentes.

## 10. Corolario de predictibilidad no está demostrado por la REC

El propio texto reconoce que el argumento es cualitativo, pero formula afirmaciones adicionales:

- para `τ>0` existe una región donde `max_k h_k<1/2`;
- la medida de esa región crece con `τ`;
- el error mínimo de predicción crece con `τ`.

Estas propiedades no se siguen sólo de `τ>0` sin hipótesis sobre los logits, el número de modos y la distribución de estados.

En particular, para dos clases siempre:

`max(h_1,h_2) ≥ 1/2`.

Así que la condición `max_k h_k<1/2` es imposible en el caso binario.

El corolario debe permanecer como hipótesis/modelo cualitativo hasta una derivación específica.

## 11. La tabla de η(τ)

La Parte VII dice que la función:

`η(τ)=1/2·τ/(1+τ)`

fue eliminada del cuerpo formal por ser heurística y no derivarse de los axiomas.

Sin embargo mantiene una tabla numérica basada en esa misma función como orientación.

Eso puede ser editorialmente legítimo si se etiqueta inequívocamente como **heurística ilustrativa**, pero no debe coexistir visualmente con los teoremas de modo que parezca una cota derivada.

## 12. Qué puede conservarse conceptualmente

La intuición general:

> más observaciones independientes pueden reducir incertidumbre estadística sobre parámetros estimados

es compatible con teoría estadística ordinaria.

También puede ser razonable explorar cómo una temperatura de decisión afecta la información disponible.

Lo que no queda demostrado es la fórmula canónica:

`n(ΔI·Δh) ≥ 4τ²`.

Por tanto debe distinguirse:

- intuición informacional;
- modelo estadístico particular;
- teorema realmente demostrado.

## 13. Clasificación final

- **Lema 7.2 → `ΔIΔh≥τ/n`:** consecuencia algebraica del modelo publicado.
- **REC `nΔIΔh≥4τ²`:** no derivada.
- **Factor 4:** error formal confirmado.
- **“Ambas formas son equivalentes”:** falso en general.
- **`τ_eff` como justificación de `4τ²/n`:** no válida.
- **Softmax general:** no demostrado; la prueba usa logística específica.
- **Bernoulli one-vs-rest:** modelo particular, no distribución completa.
- **Corolario de predictibilidad:** heurístico, no teorema general.
- **Doctrina ontológica afectada:** no necesariamente; el problema es formal/estadístico.
- **Segunda edición:** requiere reconstrucción completa antes de presentar REC como teorema.

## 14. Pendiente de segunda edición

La revisión deberá decidir entre:

1. conservar únicamente la cota realmente derivada bajo un modelo logístico explícito;
2. reconstruir la REC con Fisher multinomial/parametrización adecuada;
3. degradar la REC a modelo estadístico ilustrativo;
4. retirar la formulación si no aporta una medición necesaria al sistema.

En cualquier caso, deben retirarse o corregirse el factor 4, la equivalencia falsa y los corolarios que dependan de ellos.
