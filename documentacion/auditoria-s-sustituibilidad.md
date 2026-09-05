# AUD-S-001 — Auditoría MANT del índice de sustituibilidad S

> **Documento derivado de auditoría.** No modifica fuentes canónicas ni adjudica todavía una fórmula única para `S` en segunda edición.

- **ID:** `AUD-S-001`
- **Estado:** CONCEPTO ESTABLE / TIPADO Y FORMALIZACIÓN EN TENSIÓN
- **Familia:** `S`, `S_op`, `S_est`, estimadores aplicados y calibraciones
- **Obras contrastadas:** *Metrología Causal* I, *Axiomatización del sistema de la doble mediación*, *El cálculo de la responsabilidad*, *Método Prometeo*

## 1. Núcleo conceptual estable

La formulación más explícita del objeto en *Metrología Causal* II·9 es:

`S_i = P(D_forma_específica | c, sin i)`.

El sentido doctrinal permanece estable a través de las obras:

- `S` alto: el campo/configuración estructural habría producido el mismo resultado con otro actor o sin la idiosincrasia específica de `i`;
- `S` bajo: el resultado depende fuertemente de la posición singular/idiosincrática del actor `i`;
- `S` no es culpabilidad, dolo ni responsabilidad moral;
- `S` intenta separar cuánto de una contribución causal pertenece al campo y cuánto a la especificidad del actor.

Por tanto, no se observa una contradicción doctrinal nuclear comparable a Aego.

## 2. Primera tensión: la definición probabilística está subespecificada

*Metrología Causal* distingue:

`S_actor = P(D | c, con algún otro actor en la posición de i)`

y:

`S_campo = P(D | c, sin ningún actor en la posición de i)`.

Después propone:

`S_total = max(S_actor,S_campo)`

o una combinación ponderada según el contexto.

Esto no constituye una definición única de `S_total`: `max` y una combinación ponderada son operadores distintos y pueden producir valores diferentes para el mismo caso.

Clasificación:

- concepto: estable;
- definición probabilística objetivo: plausible pero incompleta;
- regla de agregación: pendiente.

## 3. S_op — proxy local de predominio estructural

*Axiomatización* define:

`S_op(t)=||c||_C / (||c||_C + ||a_t||_E)`.

Este objeto mide una razón local entre magnitud de configuración heredada y activación.

No es, por identidad matemática, la probabilidad contrafáctica de II·9.

Además, aunque el cociente final sea adimensional, `||c||_C` y `||a_t||_E` pertenecen a espacios distintos. El propio texto reconoce que deben normalizarse sobre escalas comparables antes de operar.

Por ello `review.axiom.Sop_units` se confirma como problema de **conmensurabilidad y calibración**, no como contradicción doctrinal.

Tipado recomendado para revisión futura:

`S_op = proxy/estimador local del predominio estructural`,

no identidad automática con el parámetro contrafáctico `S`.

## 4. S_est — sensibilidad estructural ante sustitución

*Axiomatización* define una matriz `W^(i)` reemplazando la fila del nodo `i` por el promedio de las otras filas y calcula un nuevo vector `R*^(i)`.

Después:

`S_est(i)=1−D_KL(R* || R*^(i))/log(m)`.

Este objeto mide cuánto cambia la distribución causal global bajo una regla particular de sustitución de nodo.

Es un objeto distinto de:

- la probabilidad contrafáctica `S_i`;
- la razón local `S_op`;
- el score aplicado de Prometeo.

## 5. Error formal en la normalización por KL

La demostración publicada afirma:

`D_KL(P||Q) ≤ log(m)`

para distribuciones sobre `m` elementos.

Eso no es cierto en general.

`D_KL(P||Q)` puede superar `log(m)` y puede ser infinita si existe un componente con `p_k>0` y `q_k=0`.

Por tanto:

`1−D_KL/log(m)`

no garantiza por sí mismo pertenecer a `[0,1]`.

Consecuencias:

- `review.axiom.Sest_KL` es un **error formal confirmado**;
- el rango de `S_est` no queda demostrado por la fórmula publicada;
- la normalización deberá sustituirse o acotarse si se conserva este estimador.

## 6. El puente S_op ↔ S_est no está demostrado

La Proposición 3.3 afirma la existencia de una función monótona creciente `g` tal que:

`S_op ≈ g(S_est)`

y que ambos preservan el orden entre nodos.

La demostración publicada no establece ese resultado.

En particular:

1. Pinsker relaciona divergencia KL y distancia total entre distribuciones; no prueba que el orden de `D_KL(R*,R*^(i))` sea el mismo que el orden de las desviaciones de filas de `W`.
2. Una cota superior sobre una distancia de salida no permite inferir el orden de las perturbaciones de entrada.
3. No se demuestra una aplicación inyectiva o monótona entre `||W_i−W_prom||` y `||a_t||_E`.
4. `S_op` es local y dependiente del estado `t`; `S_est` es una sensibilidad global de red bajo una sustitución definida editorialmente.

Por tanto `review.axiom.S_bridge` queda clasificada como **correspondencia formal no demostrada**, no como teorema vigente.

## 7. Efecto de RES-RSTAR-001 sobre S_est

`S_est` histórico depende de recalcular `R*^(i)` mediante la formalización anterior de `R*=eig(W/W^T)`.

Después de `RES-RSTAR-001`, cualquier estimador estructural basado en la perturbación de `R*` debe reconstruirse sobre el operador vigente:

`Q_D,b_D → r_D → M_R(D) → R*(D)`.

Por tanto, incluso si se conserva la idea de `S_est`, su implementación histórica no puede trasladarse intacta a segunda edición.

Esto no invalida la intuición:

> un nodo es más sustituible si reemplazarlo altera poco la distribución causal respecto de `D`.

Invalida únicamente la identificación con la fórmula publicada hasta nueva derivación.

## 8. El cálculo — índice aplicado de tres criterios

*El cálculo de la responsabilidad* usa:

`S_i=(A+B+C)/3`,

con componentes referidos a:

- formalización del procedimiento;
- costo/consecuencias de desobedecer;
- proporción de pares que habría actuado igual.

Éste es un **score operativo** construido desde evidencia del caso.

No es matemáticamente idéntico a `P(D|c,sin i)`, a `S_op` ni a `S_est`.

Puede funcionar como estimador aplicado del mismo constructo, pero necesita calibración si se quiere interpretar numéricamente como probabilidad.

## 9. Prometeo — score aplicado y deriva instrumental

Prometeo conserva la idea:

`S = porcentaje de la contribución causal que era estructural`.

En el cuerpo del método se utilizan criterios de formalización, reemplazabilidad y presión/incentivos sistémicos y se promedian valores entre 0 y 1.

Aunque la familia conceptual coincide con *El cálculo*, los criterios no son literalmente idénticos en todas las formulaciones.

Por tanto:

`S_calculo` y `S_prometeo`

deben tratarse como versiones de un **estimador operativo**, no como una única fórmula universal demostrada.

La igualdad de pesos entre criterios es además una calibración, no una consecuencia ontológica.

## 10. Tensión de estatus en los rangos por Hijos de Afrodita

*Metrología Causal* II·10 declara que los rangos numéricos de `S` por Hijo no son asignaciones empíricas sino una derivación ontológica de las definiciones de los Hijos.

*Axiomatización*, en cambio, presenta rangos análogos como calibrados desde casos documentados y afirma expresamente que no son consecuencia deductiva del marco, sino hipótesis empíricas revisables.

Estas dos afirmaciones no deben fusionarse.

La orientación cualitativa puede derivarse doctrinalmente:

- mayor predominio del campo → `S` esperablemente mayor;
- mayor idiosincrasia del eje propio → `S` esperablemente menor.

Pero los **intervalos numéricos concretos** requieren calibración o una derivación formal adicional. La ontología por sí sola no produce, por ejemplo, los extremos `0.60` y `0.80`.

Clasificación:

- correspondencia ordinal cualitativa: doctrinalmente defendible;
- intervalos numéricos: calibración metrológica;
- estatus publicado: inconsistente entre obras.

## 11. El nodo de diseño

La afirmación de que el diseñador tiene `S` cercano a cero puede funcionar como patrón frecuente cuando la decisión de diseño es idiosincrática.

No es una propiedad definitoria de ser diseñador.

Un diseño también puede ser altamente estandarizado, impuesto por regulación o replicado de forma casi inevitable por múltiples actores.

Así, `review.mci.s_designer_conflict` debe leerse como problema de universalización indebida, no como contradicción del concepto de `S`.

## 12. R*_neta

Las obras aplicadas usan:

`R*_neta = R* (1−S)`.

Esta operación puede conservarse provisionalmente como **definición aplicada de componente idiosincrático** si `S` está bien tipada en `[0,1]`.

No debe presentarse todavía como teorema que se siga automáticamente de la definición probabilística de `S`.

Su validez depende de qué estimador de `S` se adopte y de qué interpretación tenga el producto.

## 13. Normalización conceptual de trabajo

Hasta adjudicación posterior, conviene distinguir:

`S`

= constructo/objeto de sustituibilidad causal: grado en que el resultado específico pertenece al campo y no a la idiosincrasia del actor.

`S_prob`

= formulación contrafáctica probabilística de *Metrología Causal*.

`S_op`

= proxy local basado en predominio relativo de configuración/activación.

`S_est`

= estimador estructural por sensibilidad de la distribución causal bajo sustitución; fórmula histórica formalmente defectuosa y afectada por `RES-RSTAR-001`.

`S_app`

= score aplicado de *El cálculo* / Prometeo construido desde criterios documentales.

Esta nomenclatura es de auditoría y no modifica el canon.

## 14. Clasificación final

- **Contradicción doctrinal nuclear:** no.
- **Conflación semántica/tipado:** sí.
- **Error formal en S_est/KL:** sí.
- **Puente S_op–S_est demostrado:** no.
- **Problema de conmensurabilidad de S_op:** sí.
- **Variación instrumental entre obras aplicadas:** sí.
- **Conflicto de estatus de rangos numéricos:** sí.
- **Necesidad de calibración empírica:** sí.
- **Fórmula canónica única adjudicada:** no.

## 15. Revisiones

- `review.axiom.Sop_units`: confirmada — conmensurabilidad/calibración.
- `review.axiom.Sest_KL`: confirmada — error formal.
- `review.axiom.S_bridge`: confirmada — correspondencia no demostrada.
- `review.mci.s_probability`: definición objetivo aún subespecificada en agregación.
- `review.mci.s_ranges_calibration`: abierta — rangos numéricos requieren calibración.
- `review.mci.s_designer_conflict`: patrón contingente, no propiedad universal.
- `review.prometeo.S_calibration`: abierta — score aplicado requiere calibración/validación.

## 16. Pendiente para segunda edición

Antes de normalizar `S` editorialmente deberá decidirse:

1. qué objeto recibe el símbolo simple `S`;
2. cuáles son estimadores/proxies y con qué notación;
3. cómo se define el contrafactual de sustitución;
4. si `S_actor` y `S_campo` se mantienen separados;
5. qué regla válida reemplaza la normalización KL si se conserva `S_est`;
6. cómo se recalcula la sensibilidad estructural bajo `RES-RSTAR-001`;
7. qué dataset/protocolo calibra `S_app` y los rangos por Hijo;
8. bajo qué condiciones `R*_neta=R*(1−S)` conserva interpretación metrológica.
