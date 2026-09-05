# RES-SDO-PROM-001 — Resolución MANT de la interfaz SDO → grafo causal → Prometeo

> **Documento analítico derivado, no fuente canónica.** Esta resolución no modifica retrospectivamente SDO, Prometeo ni Taxonomía. Fija cómo deben leerse transversalmente sus interfaces bajo las resoluciones MANT vigentes. Para establecer qué afirma cada obra prevalecen `corpus/fuentes/` y `/INSTRUCCIONES.md`.

- **ID:** `RES-SDO-PROM-001`
- **Familia:** SDO → configuración → grafo causal → Prometeo → R* / α / Δ
- **Estado:** **RESUELTA POR LECTURA TRANSVERSAL — interfaz válida como generación de hipótesis y traducción; no como identificación causal automática**
- **Fecha:** 2026-09-04
- **Resoluciones rectoras:** `RES-RSTAR-001`, `RES-ALPHA-001`, `RES-DELTA-001`, `RES-PHI2-OBS-001`, `RES-RSC-IT-001`
- **Revisiones históricas principales:** `review.sdo.code_to_graph_validity`, `review.sdo.alpha_semantics`, `review.sdo.delta_semantics`, `review.sdo.alphaT_validation`, `review.sdo.children_weight_calibration`, `review.sdo.prognostic_claims`, `review.taxonomia.feedback_circularity`

---

## 1. Pregunta auditada

La familia puede condensarse en una pregunta:

> ¿La localización cualitativa del SDO produce por sí misma el grafo causal que Prometeo necesita para calcular `R*`, `α` y `Δ`, o falta una operación intermedia de identificación y justificación causal?

La lectura transversal muestra que falta esa operación intermedia.

SDO contiene una interfaz explícita que afirma:

`localización SDO → nodos/aristas cualitativos → Prometeo → R*, α, Δ`.

Pero Prometeo exige para su propio grafo:

1. un resultado concreto que se analiza;
2. actores o factores con posición causal respecto de ese resultado;
3. aristas causales con dirección y tipo;
4. evidencia del caso que sostenga cada arista;
5. un peso `w` estimado a partir de la evidencia disponible.

La localización SDO, en cambio, describe una **configuración actual de la voluntad** mediante códigos inferidos desde señales observables y expresamente revisables.

Por tanto, los dos objetos no son idénticos.

---

## 2. Qué produce realmente SDO

SDO VI·3 y VIII·1 contienen una distinción epistemológica decisiva.

La secuencia propia del instrumento es:

`señales observadas → localización tentativa → contrastación → código/localización revisable`.

VIII·1 exige separar en la ficha:

- la **señal observada**;
- la **inferencia** que esa señal sustenta;
- la certeza de la localización.

La propia obra da el criterio: «el sujeto describe perplejidad...» es señal; «el sujeto está en E-4» es inferencia.

Por tanto, una localización como:

`E-4 · M-2 · V-2 · D-1`

no es un hecho causal bruto. Es una inferencia instrumental documentada y revisable sobre la configuración actual.

SDO puede usar esa localización para identificar:

- sujetos u Otros relevantes;
- eventos narrados;
- roles, máscaras o campos que parecen estructuralmente relevantes;
- relaciones que merecen investigación causal;
- una pregunta concreta para Prometeo.

Eso es información legítima para **proponer candidatos causales**.

No es todavía la demostración de que exista una arista causal con un peso determinado.

---

## 3. Qué exige el grafo de Prometeo

Prometeo, capítulo 2, define su grafo a partir del caso y del resultado analizado.

Su protocolo exige:

1. identificar actores causalmente relevantes;
2. clasificar nodos;
3. preguntar para cada par si existe conexión causal, dirección y tipo;
4. documentar cada arista con evidencia del expediente.

El propio texto declara:

> una arista sin evidencia es una hipótesis, no un elemento del grafo.

Y distingue expresamente:

`no hay evidencia de la arista`

frente a:

`hay evidencia de que la arista no existe`.

La evidencia se usa después para estimar `w`, que Prometeo entiende como el grado en que el origen determinó localmente el comportamiento del destino.

Este núcleo es compatible con `RES-RSTAR-001`, que tipa:

`w_ij = w(i→j)`

como determinación causal local.

---

## 4. Dos grafos que no deben confundirse

La interfaz debe distinguir al menos dos objetos.

### 4.1 Grafo/configuración SDO

Puede representarse editorialmente como:

`G_SDO`.

Su función es organizar una localización:

- códigos;
- actores y Otros relevantes;
- estados o posiciones;
- eventos narrados;
- relaciones cualitativamente sospechadas;
- señales y certeza de la inferencia.

`G_SDO` es un **grafo de configuración o de hipótesis causales**.

No necesita ser todavía un grafo causal válido para `R*`.

### 4.2 Grafo causal respecto de un resultado D

Bajo `RES-RSTAR-001`, debe existir un resultado explícito `D`.

La reconstrucción causal produce:

`G_D`.

De él se extraen:

`A_D`, `Q_D`, `b_D`

para calcular:

`r_D=(I−Q_D)^−1 b_D`

cuando `ρ(Q_D)<1`, y finalmente:

`R*(D)=r_D/(1^T r_D)`.

### 4.3 La interfaz correcta

La arquitectura consolidada es:

`observaciones O`

`→ localización L_SDO`

`→ candidatos/hipótesis G_SDO`

`→ pregunta causal + resultado D`

`→ evidencia específica del caso`

`→ reconstrucción causal G_D`

`→ w / Q_D / b_D`

`→ R*(D)`.

No:

`código SDO → arista causal ya validada → R*`.

---

## 5. Consecuencia para E-4, V-2, M-2 y demás códigos

SDO VII·1 contiene formulaciones como:

- E-4 produce un Otro con arista de alta `R*`;
- V-2 produce asimetría de pesos;
- M-2 opera como nodo intermedio;
- M-3 funciona como campo supraindividual con `R*` sobre otros nodos.

Estas formulaciones son útiles como **hipótesis estructurales**.

No pueden convertirse en reglas automáticas del cálculo.

Por ejemplo:

`E-4`

puede justificar la pregunta:

> ¿qué factores y qué Otro(s) contribuyen a que esta configuración E-4 persista?

Pero no justifica por sí solo:

`R*_Otro = 0.8`

o siquiera:

`R*_Otro > R*_otros`.

Eso debe emerger de una reconstrucción causal relativa al resultado definido.

De lo contrario se produciría circularidad conceptual:

1. E-4 se define como orientación desde un Otro;
2. se introduce por esa razón una arista fuerte desde ese Otro;
3. R* devuelve que el Otro tiene gran peso;
4. el resultado se presenta como confirmación cuantitativa de E-4.

El cálculo no habría descubierto el peso: lo habría recibido en la construcción del grafo.

---

## 6. Las Series 1, 2 y 3 de SDO deben tiparse como capa de interfaz

SDO VII·1 divide «Prometeo» en tres series:

1. factores sobre la segunda mediación;
2. densidad del campo y dinámica del vector;
3. cadena causal de eventos.

El Prometeo jurídico auditado se organiza canónicamente como un protocolo de cinco pasos y su plantilla automatiza `w → R* → S/R*_neta → sensibilidad → α/Δ/AD`.

Por ello las tres Series deben leerse como una **organización introducida por la interfaz SDO**, no como si fueran tres módulos canónicos preexistentes del Prometeo jurídico.

### Serie 3

Es la más directamente compatible con el objeto original de Prometeo porque parte de un evento específico y pregunta por la cadena causal que produjo un resultado.

### Series 1 y 2

Pueden ser compatibles con el aparato causal si se define explícitamente un resultado de análisis, por ejemplo:

- `D = persistencia de la configuración E-4 en el intervalo analizado`;
- `D = bloqueo observable de una operación definida de φ₂`;
- `D = configuración relacional V-3 bajo criterios operativos explícitos`.

Después deben identificarse mecanismos causales y evidencia hacia ese `D`.

Sin ese paso, «R* sobre φ₂», «R* de V-3» o «R* de M-3» quedan subtipados.

---

## 7. Nodo, arista, estado y resultado

La interfaz SDO mezcla en una misma tabla:

- personas;
- Otros;
- eventos traumáticos;
- máscaras;
- campos institucionales;
- `φ₂`;
- `I(t)`;
- códigos de ejes.

No todos pertenecen al mismo tipo causal.

La segunda edición deberá distinguir al menos:

1. **nodo actor/agente**;
2. **nodo estructural o instrumental**;
3. **evento causal**;
4. **estado/variable mediadora**;
5. **resultado D**.

Un campo, rol, máscara o evento puede formar parte de un modelo causal si existe una regla explícita que diga qué mecanismo representa.

Pero una etiqueta diagnóstica o estado no adquiere por sí sola agencia causal sólo por aparecer como nodo visual.

---

## 8. Error de tipo: R* no pertenece a las aristas

La ficha extendida de SDO incluye «Parámetros por nodo / arista: R*, α, Δ» y varios pasajes hablan del `R*` de una arista.

Bajo la formalización vigente:

`w_ij`

es el peso causal **local de la arista** `i→j`.

Mientras:

`R*_i(D)`

es la proporción estable de convergencia causal **del nodo i respecto de D**.

Por tanto:

`R* de arista`

no es una expresión bien tipada salvo que se defina otro objeto, por ejemplo una contribución de ruta o de arista, con símbolo y fórmula propios.

Regla vigente:

`arista → w`

`nodo respecto de D → R*`.

---

## 9. R* no es palanca de intervención

SDO afirma repetidamente que el factor con mayor `R*` es el que, si cambia, produce mayor efecto, y usa esa idea para elegir el «punto de entrada óptimo».

Eso no se sigue de `RES-RSTAR-001`.

`R*_i(D)` responde:

> ¿qué proporción estable de la atribución causal de D corresponde al nodo i bajo el modelo reconstruido?

No responde automáticamente:

> ¿cuánto cambiará D si intervenimos ahora sobre i?

Una causa puede haber contribuido mucho al resultado histórico y ser ahora inmodificable. Otro factor con menor atribución histórica puede ser mucho más sensible a intervención.

Por tanto deben separarse:

`atribución causal`

frente a:

`efecto o palanca de intervención`.

La segunda requiere una función de respuesta, sensibilidad o modelo de intervención adicional.

La selección del punto de entrada no puede derivarse de `R*` solo.

---

## 10. El producto R*·α no está validado como «potencial de movimiento»

SDO introduce:

`R*_α = R* × α`

como «potencial de movimiento real» y sostiene que el punto de entrada óptimo maximiza ese producto.

La lectura transversal no encuentra una derivación que haga de ese producto una magnitud causal o intervencional validada.

Además, el problema se agrava porque el `α` usado por SDO no es establemente el mismo objeto que el `α` aplicado de Prometeo.

Por tanto:

- `R*×α` puede conservarse como **heurística o candidato de investigación** si se renombra y tipa;
- no debe presentarse como teorema de Prometeo;
- no debe usarse para afirmar un punto de entrada óptimo sin validación intervencional independiente.

---

## 11. α de SDO y α de Prometeo no son automáticamente el mismo objeto

`RES-ALPHA-001` y `RES-PHI2-OBS-001` ya distinguen:

- `φ₂`: operación interna;
- α interno/clínico: proxy o estimación de integración;
- α aplicado: grado de asunción efectiva de la posición causal, observable mediante acciones, reparaciones, cargas y consecuencias verificables.

SDO VII·1 define α principalmente como:

> capacidad del sujeto de integrar genuinamente lo que ocurre en el campo.

Eso pertenece al **ramal interno/instrumental**.

Prometeo jurídico usa α para asunción/reparación efectiva y su plantilla incluso lo traduce a proporciones de cumplimiento o reparación en dominios aplicados.

Por tanto:

`α_SDO ≠ α_Prometeo_aplicado`

salvo que una aplicación defina y valide una transformación explícita.

La revisión `review.sdo.alpha_semantics` queda resuelta en este nivel:

> SDO no sustituye la definición consolidada de α; reutiliza el símbolo para un estimador local de integración/capacidad.

La segunda edición debe desambiguar la notación.

---

## 12. α_T es un índice local propuesto, no α formal ya calibrado

SDO VII·3 define:

`α_T = ΔI(t)_genuina_asumida / exposición_a_la_pérdida`.

La fórmula expresa una intuición clara: relación entre exposición a la pérdida e integración residual.

Pero no define todavía:

- unidad o medida del numerador;
- unidad o medida del denominador;
- regla de observación de `ΔI(t)_genuina_asumida`;
- regla de observación de «exposición»;
- estimador;
- error de medición;
- calibración de valores como `0.05` o `0.38`;
- relación validada con velocidad de amortiguación o número de sesiones.

Además depende de una representación de `I(t)` que `RES-RSC-IT-001` ya ordenó reconstruir formalmente.

Por tanto `review.sdo.alphaT_validation` no puede resolverse positivamente por lectura.

Sí puede resolverse su **estatus**:

> `α_T` es un índice autoral local propuesto y no una magnitud metrológicamente validada.

Sus valores publicados deben tratarse como ilustrativos mientras no exista una regla de medición reproducible.

---

## 13. Δ de SDO es otra variable

`RES-DELTA-001` fija:

`Δ_i = R*_i − α_i`.

SDO VII·1 y VII·4 reutilizan `Δ` para:

- cambio entre una localización inicial y una actual;
- magnitud de cambio producido;
- cambio proyectado ante una intervención;
- variación temporal de un «nodo traumático».

Estos objetos no son `R*−α`.

No existe una transformación que los haga equivalentes.

Por tanto `review.sdo.delta_semantics` queda resuelta:

> la Δ temporal/prospectiva de SDO es una variable distinta que debe recibir otro símbolo o subíndice inequívoco en segunda edición.

No debe alimentar ni sustituir la Δ formal de responsabilidad.

---

## 14. Pesos de los Hijos: composición inferida, no pesos causales

SDO VII·2 construye un vector:

`H=[w_E,w_D,w_A,w_F,w_P,w_Ar]`, `Σw_i=1`.

La propia obra reconoce que los Hijos **no son directamente observables**: el mediador observa manifestaciones y desde ellas infiere pesos.

La normalización a suma 1 produce una **distribución composicional** sobre seis categorías.

Eso no la convierte en:

- matriz `W`;
- peso causal de arista `w_ij`;
- `R*`;
- probabilidad validada.

El procedimiento publicado identifica hijos activos, estima intensidad relativa, aplica factores contextuales y normaliza, pero no contiene una regla numérica reproducible que convierta cada observación y factor contextual en scores previos a la normalización.

Por ello `review.sdo.children_weight_calibration` permanece abierta en validación/calibración.

La conclusión vigente es negativa y precisa:

> los pesos de Hijos son estimaciones composicionales autorales, no pesos causales de Prometeo.

La regla de Taxonomía que usa `P(Hijos)` para estimar `S` es, por su parte, una operacionalización adicional que requiere calibración propia; no valida retroactivamente los pesos de SDO.

---

## 15. Las afirmaciones pronósticas no son outputs demostrados de R*

SDO atribuye a Prometeo capacidades como:

- estimar cuántas sesiones requerirá un proceso;
- proyectar `Δ` de una intervención;
- calcular amortiguación de oscilaciones;
- predecir rapidez de integración;
- elegir el punto óptimo de entrada;
- proyectar trayectoria del duelo.

El Prometeo jurídico auditado calcula una distribución causal, sustituibilidad/asunción, sensibilidad de escenarios y magnitudes asociadas al daño. Su plantilla no contiene por sí sola una dinámica temporal de intervención que derive número de sesiones o trayectoria clínica/ontológica.

Por ello:

`R*`, `α` y `Δ`

no bastan para derivar esas predicciones.

`review.sdo.prognostic_claims` permanece abierta como problema empírico/intervencional, pero queda fijado su estatus:

> las afirmaciones pronósticas son hipótesis de aplicación de SDO y no resultados demostrados por el aparato Prometeo/R* vigente.

---

## 16. Taxonomía U·3: el feedback no es validación causal

Taxonomía propone:

`inputs → Prometeo → comparar output con evidencia → revisar inputs → recalcular`.

Como control de errores, esta idea puede ser útil.

Pero si la misma evidencia se usa:

1. para construir el grafo y calibrar inputs;
2. para decidir después que el output «debería» verse de determinada manera;
3. para reajustar inputs hasta obtener ese resultado,

el procedimiento se convierte en ajuste post hoc.

Por tanto:

> **coherencia interna no equivale a validación independiente.**

La retroalimentación es admisible para:

- detectar errores de entrada;
- comprobar invariantes predefinidos;
- localizar sensibilidad;
- pedir evidencia adicional;
- declarar incompatibilidad.

No es admisible como:

- regla para forzar un output intuitivamente esperado;
- criterio para modificar pesos hasta que un actor predeterminado quede primero;
- sustituto de evidencia externa o de una prueba causal independiente.

Esto encauza `review.taxonomia.feedback_circularity`.

---

## 17. Corrección de una regla heredada de Taxonomía

Taxonomía usa como señal de inconsistencia que un nodo de ejecución supere al nodo de diseño cuando el ejecutor siguió protocolos diseñados por otro.

Esa regla no puede conservarse como criterio universal.

La auditoría de `RES-RSTAR-001` ya resolvió que **no existe una presunción universal de que el nodo de diseño deba tener mayor R***.

La evidencia de diseño y condicionamiento debe incorporarse al grafo y a `w`; el resultado de `R*` debe emerger del cálculo.

No puede usarse después la expectativa «diseñador debe ganar» para recalibrar los mismos inputs.

---

## 18. Arquitectura consolidada de la interfaz

La interfaz vigente debe representarse así:

### Capa observacional

`O = señales, documentos, narraciones, registros`.

### Capa SDO

`O → L_SDO`.

`L_SDO` es una inferencia de localización con certeza explícita.

### Capa de hipótesis

`L_SDO → G_SDO`.

`G_SDO` organiza candidatos: factores, actores, eventos y relaciones que deben investigarse.

### Capa causal

`(G_SDO, D, evidencia específica) → G_D`.

Aquí se decide qué nodos y mecanismos tienen posición causal respecto de `D`.

### Capa metrológica local

`G_D → w_ij`.

Cada `w` requiere evidencia y calibración del mecanismo local.

### Capa de responsabilidad

`w → Q_D,b_D → M_R(D) → R*(D)`.

### Capas separadas

- α aplicado se estima según `RES-ALPHA-001`;
- `Δ=R*−α` según `RES-DELTA-001`;
- integración interna, Hijos, trayectoria o intervención requieren instrumentos propios y no se deducen automáticamente de `R*`.

---

## 19. Estado de las revisiones vinculadas

### Resueltas por esta lectura

- `review.sdo.code_to_graph_validity`:
  - **respuesta:** no existe validación causal automática; la traducción SDO genera candidatos/hipótesis y debe pasar por reconstrucción causal independiente respecto de `D`.

- `review.sdo.alpha_semantics`:
  - **respuesta:** la α de capacidad de integración SDO pertenece al ramal interno/instrumental y no sustituye α aplicado.

- `review.sdo.delta_semantics`:
  - **respuesta:** la Δ temporal/prospectiva de SDO es un objeto distinto de `Δ=R*−α`.

- `review.taxonomia.feedback_circularity`:
  - **respuesta:** el feedback es control interno legítimo sólo si no se usa para backfitting; coherencia con la misma evidencia no es validación independiente.

### Abiertas, pero con estatus ya tipado

- `review.sdo.alphaT_validation`:
  - índice local propuesto, pendiente de definición metrológica y validación longitudinal.

- `review.sdo.children_weight_calibration`:
  - composición inferida sin regla numérica reproducible/calibración.

- `review.sdo.prognostic_claims`:
  - hipótesis de aplicación, pendiente de modelo intervencional y evidencia empírica.

- `review.sdo.coding_reproducibility`:
  - requiere concordancia/interobservador y manual de codificación.

- calibración de `w`, E0–E8 y portabilidad entre dominios:
  - permanecen abiertas por separado.

---

## 20. Qué deberá cambiar en segunda edición

Sin modificar fuentes históricas de primera edición, la segunda edición deberá:

1. sustituir «SDO produce el grafo causal de Prometeo» por una formulación en dos etapas;
2. distinguir `G_SDO` de `G_D`;
3. exigir un resultado `D` explícito antes de calcular `R*`;
4. separar `w` de arista de `R*` de nodo;
5. tipar nodos/estados/eventos/resultados;
6. eliminar la inferencia automática `código SDO → R* alto/bajo`;
7. separar α interno/instrumental de α aplicado;
8. renotar la Δ temporal/prospectiva;
9. tratar `α_T` y pesos de Hijos como instrumentos propuestos pendientes de calibración;
10. retirar o rebajar las afirmaciones de número de sesiones, trayectoria y punto óptimo de entrada hasta disponer de modelo intervencional;
11. tipar `R*×α` como heurística no validada si se conserva;
12. convertir el feedback de Taxonomía en control de consistencia, no criterio de verdad;
13. retirar la presunción de que el diseñador debe superar siempre al ejecutor.

---

## 21. Fórmula de lectura breve

La resolución puede resumirse así:

`SDO localiza; no demuestra causalidad.`

`SDO puede proponer el grafo; la evidencia construye G_D.`

`Prometeo calibra w sobre mecanismos documentados.`

`R* distribuye atribución causal respecto de D; no mide palanca de intervención.`

`w pertenece a aristas; R* pertenece a nodos respecto de D.`

`α_SDO no es automáticamente α aplicado.`

`Δ_SDO no es Δ=R*−α.`

`coherencia interna no es validación independiente.`
