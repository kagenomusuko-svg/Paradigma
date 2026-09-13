PARTE IV · La incertidumbre y sus límites

### Capítulo 4.2

### La propagación de la incertidumbre de v_t

al cálculo de R* La mecánica matemática de la incertidumbre ontológica en el cálculo

### I.  El punto de partida: la distribución de probabilidad sobre Hijos

El capítulo 4.1 estableció que la incertidumbre ontológica sobre v_t se manifiesta en el sistema como incertidumbre sobre el Hijo dominante en φ₁ y en φ₂. Esa incertidumbre, cuando la observación SDO no puede producir una asignación puntual, se expresa como una distribución de probabilidad sobre los seis Hijos.

La distribución no es necesariamente una de los seis Hijos con probabilidad 1. La observación SDO produce con frecuencia resultados del tipo: 'las señales son más consistentes con Fobos, con algo de Deimos, y con una fracción que no puede asignarse a ninguno de los dos'. Eso es exactamente una distribución de probabilidad — no una ignorancia total sino una incertidumbre estructurada con información parcial.

La distribución de probabilidad sobre Hijos — notación P(v_t) = {P(Eros), P(Potós), P(Anteros), P(Fobos), P(Deimos),

P(Harmonía)}

La transformación formal

Con la restricción: Σ P(Hijo_k) = 1. La distribución refleja la certeza relativa del SDO sobre la posición de v_t. Una distribución concentrada (P(Fobos) = 0.92) indica alta certeza. Una distribución difusa (varios Hijos con probabilidades entre 0.20 y 0.30) indica alta incertidumbre.

Esta distribución no es arbitraria — está fundada en las señales observacionales que el SDO recolecta. Las señales para cada Hijo (establecidas en el capítulo 2.2 y la tabla de la sección IV de ese capítulo) son indicadores parciales del Hijo dominante. Cuando varias señales apuntan en la misma dirección, la distribución se concentra en un Hijo. Cuando las señales son mixtas o contradictorias, la distribución es más difusa.

El capítulo 4.1 ya estableció que esta distribución produce rangos de S y α más amplios que una asignación puntual. Este capítulo deriva la mecánica precisa de esa propagación.

### II.  Primer paso: de la distribución sobre Hijos al intervalo de S

El primer paso de la propagación es convertir la distribución de probabilidad sobre los Hijos en un intervalo para S. El capítulo 2.2 estableció las orientaciones de S para cada Hijo — rangos típicos derivados de la lógica del sistema. Este capítulo los usa para construir el intervalo de S que resulta de la distribución.

La orientación de S por Hijo — resumen operativo

Para cada Hijo k, la observación del SDO produce una orientación de S: un rango [S_mín_k, S_máx_k] dentro del cual S del actor cae cuando ese Hijo domina v_t. Los rangos están derivados de la lógica del sistema (capítulo 2.2, tabla de la sección IV) y se usan aquí como punto de partida.

Hijo_k S_mín_k S_máx_k Justificación

Harmonía 0.05 0.20 v_t opera desde la integración plena de ambas dimensiones. Máxima idiosincrasia — solo este ego específico produce este acto.

La transformación formal

Hijo_k S_mín_k S_máx_k Justificación

Anteros 0.08 0.30 v_t opera desde el eje propio del ego. Alta idiosincrasia, aunque sin la plenitud de Harmonía.

Eros 0.30 0.60 v_t se abre hacia lo posible sin objeto definido. Equilibrio entre v_t y c. Idiosincrasia moderada.

Potós 0.55 0.80 v_t sigue el patrón heredado de c hacia objeto ausente. c tiene peso significativo aunque v_t tiene dirección.

Fobos 0.70 0.92 v_t responde a amenaza concreta registrada por c. c domina fuertemente.

Deimos 0.75 0.95 v_t paralizada por posibilidad de amenaza (c anticipa). Máxima dominación de c.

### La derivación del intervalo de S desde P(Hijos)

### Dada la distribución P(v_t) sobre los Hijos, el intervalo de S se deriva de dos formas según el grado de concentración de la distribución:

Caso 1 — Distribución concentrada en un Hijo (P(Hijo_k) ≥ 0.75): el intervalo de S es el rango del Hijo dominante, posiblemente con un pequeño ensanchamiento que refleja la probabilidad residual de los otros Hijos. S ∈ [S_mín_k, S_máx_k]. La incertidumbre ontológica es baja. Caso 2 — Distribución difusa (ningún Hijo con probabilidad > 0.75): el intervalo de S abarca los rangos de todos los Hijos con probabilidad significativa (P(Hijo_k) > 0.10), ponderados por sus probabilidades. El intervalo resultante es más amplio que cualquier rango individual de Hijo.

El intervalo de S bajo distribución difusa — derivación formal S_mín = Σ_k P(Hijo_k) × S_mín_k     S_máx = Σ_k P(Hijo_k)

× S_máx_k El intervalo de S es el promedio ponderado de los rangos de cada Hijo, con los pesos de la distribución de probabilidad. Esto captura tanto el valor esperado de S como su incertidumbre: S_mín es el promedio ponderado de los límites inferiores, S_máx es el promedio ponderado de los límites superiores.

La transformación formal

Una alternativa más conservadora para el análisis de sensibilidad extendido: usar el envelope total en lugar del promedio ponderado. El envelope total es el intervalo más amplio que cubre todos los Hijos con probabilidad positiva: S_mín = min_k {S_mín_k para P(Hijo_k) > 0}. Esto garantiza que el análisis de sensibilidad cubre el peor caso de incertidumbre ontológica. El costo es que el intervalo es más amplio de lo necesario cuando la distribución tiene pesos muy desiguales.

Recomendación práctica: usar el promedio ponderado como estimación central del rango de S, y usar el envelope total para verificar que la conclusión es robusta bajo el peor caso de incertidumbre ontológica. Si el análisis es robusto bajo el envelope total, lo es a fortiori bajo el promedio ponderado.

Ejemplo con distribución típica

Distribución observada: P(Fobos) = 0.70, P(Deimos) = 0.20, P (indeterminado — tratado como Potós para el análisis) = 0.10.

S usando promedio ponderado: S_mín = 0.70 × 0.70 + 0.20 × 0.75 + 0.10 × 0.55 = 0.490 + 0.150 + 0.055 = 0.695. S_máx = 0.70 × 0.92 + 0.20 × 0.95 + 0.10 × 0.80 = 0.644 + 0.190 + 0.080 = 0.914. Intervalo resultante: S ∈ [0.695, 0.914]. S usando envelope total: S_mín = min {0.70, 0.75, 0.55} = 0.55. S_máx = max {0.92, 0.95, 0.80} = 0.95. Intervalo resultante: S ∈ [0.55, 0.95].

La diferencia: el promedio ponderado produce S ∈ [0.695, 0.914] — un rango que refleja la concentración de la distribución en Fobos/Deimos. El envelope total produce S ∈ [0.55, 0.95] — el rango máximo de incertidumbre. Para el análisis de sensibilidad conservador, se usa el envelope. Para la estimación central, se usa el promedio ponderado.

### III.  Segundo paso: del intervalo de S al rango de R*_neta

Con el intervalo [S_mín, S_máx] derivado del primer paso, el segundo paso propaga esa incertidumbre a R*_neta. R*_neta = R* × (1 − S), y R* es un parámetro que ya tiene su propio rango [R*_mín, R*_máx] derivado de la incertidumbre empírica sobre w.

La transformación formal

La propagación combina dos fuentes de incertidumbre: la empírica (R* tiene rango [R*_mín, R*_máx]) y la ontológica (S tiene rango [S_mín, S_máx]). La incertidumbre combinada sobre R*_neta requiere considerar todas las combinaciones posibles.

El rango de R*_neta bajo dos fuentes de incertidumbre

R*_neta ∈ [R*_mín × (1−S_máx), R*_máx × (1−S_mín)] El mínimo de R*_neta ocurre cuando R* es mínimo Y S es máxima. El máximo de R*_neta ocurre cuando R* es máximo Y S es mínima. Nota: este es el rango del envelope total — el más conservador.

Esta fórmula asume que R* y S son independientes — que la incertidumbre empírica sobre w y la incertidumbre ontológica sobre el Hijo dominante no están correlacionadas. Esa asunción es razonablemente válida cuando las aristas del grafo y la posición de v_t del actor son determinadas por fuentes de evidencia distintas. Cuando pueden estar correlacionadas — por ejemplo, cuando el mismo documento que indica el protocolo obligatorio (baja S) también indica el peso w de la arista de instrucción —, el analista debe tratar ese documento como fuente simultánea de información sobre w y sobre S, y el rango combinado puede ser más estrecho que el envelope.

El caso especial: cuando R* no varía y solo S varía

Hay casos donde la evidencia empírica es suficientemente sólida para que R* sea aproximadamente constante (w bien establecidos, eigenvector con poca sensibilidad) pero la incertidumbre ontológica sobre S es alta. En ese caso la fórmula simplifica: R*_neta ∈ [R* × (1−S_máx), R* × (1−S_mín)].

Este caso es frecuente en análisis de casos bien documentados donde el actor no está disponible para observación SDO. La evidencia documental es sólida (incertidumbre empírica baja) pero el Hijo dominante no puede determinarse con precisión (incertidumbre ontológica alta). R*_neta tiene un rango que puede ser muy amplio incluso cuando R* es puntual.

Ejemplo numérico: el ejecutor con R* bien establecido y Hijo incierto R* = 0.38 (bien establecido desde evidencia documental, rango estrecho [0.35, 0.42]). Distribución P(v_t): P(Fobos) = 0.60, P(Anteros) = 0.30, P(Eros) = 0.10 (señales mixtas — el ejecutor siguió el protocolo, pero también tomó algunas iniciativas propias

La transformación formal

no protocolizadas). S por promedio ponderado: S_mín = 0.60×0.70 + 0.30×0.08 + 0.10×0.30 = 0.420+0.024+0.030 = 0.474. S_máx = 0.60×0.92 + 0.30×0.30 + 0.10×0.60 = 0.552+0.090+0.060 = 0.702. R*_neta ∈ [0.35× (1−0.702), 0.42× (1−0.474)] = [0.35×0.298, 0.42×0.526] = [0.104, 0.221]. La incertidumbre ontológica produce un rango de R*_neta que va de 0.104 a 0.221 — un factor de 2.1. La conclusión sobre la responsabilidad neta del ejecutor es muy sensible a cuál Hijo dominaba.

### IV.  Tercer paso: del rango de R*_neta al rango de Δ

Δ = R* − α. Con la incertidumbre ontológica hay dos dimensiones de Δ que se ven afectadas: R*_neta (que ya se discutió) y α (que también tiene incertidumbre ontológica porque depende del Hijo en φ₂, que puede ser distinto al Hijo en φ₁).

Para el análisis de Δ bajo dos incertidumbres, hay que distinguir si el análisis usa R* (sin corrección de S) o R*_neta (con corrección). La respuesta depende del propósito del análisis:

Si el propósito es determinar la brecha entre la responsabilidad causal total y la asunción total, se usa Δ = R* − α. La incertidumbre de R* viene de la incertidumbre empírica sobre w, y la incertidumbre de α viene de la incertidumbre ontológica sobre el Hijo en φ₂. Si el propósito es determinar la brecha entre la responsabilidad idiosincrática y la asunción idiosincrática, se usa Δ_neta = R*_neta − α_neta. La incertidumbre de R*_neta viene de ambas fuentes (empírica sobre w y ontológica sobre el Hijo en φ₁), y la incertidumbre de α_neta viene de la incertidumbre sobre el Hijo en φ₂.

El rango de Δ bajo incertidumbre combinada

Δ ∈ [R*_mín − α_máx(φ₂), R*_máx − α_mín(φ₂)] El mínimo de Δ ocurre cuando R* es mínimo Y α es máximo. El máximo de Δ ocurre cuando R* es máximo Y α es mínimo. α_máx(φ₂) y α_mín(φ₂) se derivan del Hijo en φ₂ usando la tabla del capítulo 2.3.

Hay un caso donde el rango de Δ puede ser tan amplio que incluye tanto valores positivos como negativos: cuando la incertidumbre sobre α es alta y la incertidumbre sobre R* es moderada. Δ ∈ [−0.15, +0.35], por ejemplo, significa que el análisis no puede determinar si hay sobre-

La transformación formal

### asunción (Δ < 0) o sub-asunción (Δ > 0). En ese caso la Declaración sobre el estado de la asunción del actor no puede producirse.

### V.  La cadena completa de propagación: de P(Hijos) a los rangos finales

Los tres pasos del capítulo pueden sintetizarse en una cadena de propagación que el análisis implementa en secuencia. La cadena produce los rangos finales de S, R*_neta y Δ que el análisis de sensibilidad extendido usa.

Paso 1 — P(Hijos) → [S_mín, S_máx]

S_mín = Σ_k P(k)×S_mín_k · S_máx = Σ_k P(k)×S_máx_k Promedio ponderado de los rangos de S de cada Hijo por su probabilidad. Para análisis conservador: S_mín = min_k {S_mín_k | P(k)>0}, S_máx = max_k {S_máx_k | P(k)>0} (envelope total).

Paso 2 — [S_mín, S_máx] + [R*_mín, R*_máx] → [R*_neta_mín, R*_neta_máx] R*_neta_mín = R*_mín × (1−S_máx) · R*_neta_máx = R*_máx ×

(1−S_mín) El rango de R*_neta combina la incertidumbre empírica sobre R* y la incertidumbre ontológica sobre S. El rango resultante puede ser amplio cuando ambas incertidumbres son altas.

Paso 3 — [R*_mín, R*_máx] + [α_mín, α_máx] → [Δ_mín, Δ_máx]

Δ_mín = R*_mín − α_máx · Δ_máx = R*_máx − α_mín El rango de Δ combina la incertidumbre empírica sobre R* y la incertidumbre ontológica sobre α (derivada del Hijo en φ₂, que puede ser distinto al Hijo en φ₁).

La cadena completa produce cuatro rangos finales para cada nodo i del análisis: [S_mín_i, S_máx_i], [R*_i_mín, R*_i_máx] (de la incertidumbre empírica sobre w), [R*_neta_i_mín, R*_neta_i_máx] (combinación de ambas), y [Δ_i_mín, Δ_i_máx] (si α también tiene incertidumbre).

La transformación formal

### VI.  El análisis de sensibilidad combinado: dos espacios simultáneos

El análisis de sensibilidad estándar varía w dentro de sus rangos y verifica la robustez de la conclusión sobre la distribución de R*. El análisis de sensibilidad extendido varía simultáneamente w (incertidumbre empírica) y la distribución P(Hijos) de cada nodo (incertidumbre ontológica), y verifica la robustez de la conclusión sobre la distribución de R*_neta.

La implementación práctica del análisis combinado puede hacerse mediante tres métodos con distinto grado de rigor y costo computacional.

Método 1 — Análisis de vértices extremos (más rápido, suficiente para robustez completa)

Para cada parámetro con incertidumbre (cada w_ij y la S de cada nodo), calcular la distribución de R*_neta en los cuatro vértices extremos: (w_mín_todos, S_mín_todos), (w_mín_todos, S_máx_todos), (w_máx_todos, S_mín_todos), (w_máx_todos, S_máx_todos). Si la conclusión sobre quién tiene mayor R*_neta es la misma en los cuatro vértices, el análisis es completamente robusto (Declaración A extendida). Si cambia en alguno, identificar en cuál — eso señala el tipo de incertidumbre responsable.

Este método es suficiente para declarar robustez completa, pero puede perder sensibilidad en los casos intermedios: hay combinaciones de valores intermedios de w y S que podrían cambiar la conclusión, aunque los cuatro vértices extremos no lo hagan, especialmente cuando las relaciones son no lineales. En la práctica, para análisis con menos de diez nodos, el análisis de vértices es suficiente.

Método 2 — Grilla sistemática (más riguroso, mayor costo)

Dividir cada parámetro en N niveles dentro de su rango (típicamente N = 3 o 5: mínimo, central, máximo) y calcular la distribución de R*_neta para todas las combinaciones de niveles. El número de combinaciones crece exponencialmente con el número de parámetros (3^n para n parámetros con 3 niveles), lo que hace este método impráctico para grafos grandes pero muy informativo para grafos de 4 a 8 nodos.

La transformación formal

Método 3 — Monte Carlo (más completo, requiere implementación computacional)

Extraer aleatoriamente N combinaciones de (w, P(Hijos)) de sus distribuciones y calcular R*_neta para cada muestra. Los resultados producen una distribución empírica de R*_neta para cada nodo. La conclusión sobre quién tiene mayor R*_neta es robusta si se mantiene en la gran mayoría de las muestras (porcentaje de muestras donde la conclusión se mantiene como medida de robustez estadística).

Para el Monte Carlo, se necesita especificar las distribuciones de w y de P(Hijos). Para w: distribución uniforme sobre [w_mín, w_máx] es la opción por defecto cuando no hay información sobre la forma de la distribución. Para P(Hijos): distribución de Dirichlet con parámetros proporcionales a los pesos observados es la opción más apropiada — refleja la incertidumbre sobre una distribución de probabilidad sobre categorías.

La distribución de Dirichlet es la generalización multivariada de la distribución Beta: produce distribuciones de probabilidad sobre categorías (como los seis Hijos) con parámetros que reflejan la certeza relativa sobre cada categoría. Cuando el SDO observa P(Fobos) = 0.70 con incertidumbre moderada, la distribución de Dirichlet con parámetros proporcionales a {0.70, 0.20, 0.10, 0, 0, 0} produce muestras de distribuciones de probabilidad que tienen alta concentración en Fobos, pero con variabilidad que refleja la incertidumbre de la observación SDO.

### VII.  El criterio de prioridad: cuándo resolver la incertidumbre ontológica primero

Cuando el análisis de sensibilidad combinado produce Declaración C (la conclusión no es robusta), la pregunta práctica más urgente es: ¿qué debo resolver primero para mejorar la robustez — la incertidumbre empírica (más evidencia documental) o la incertidumbre ontológica (mejor observación SDO)?

El capítulo 4.1 estableció el diagnóstico de los dos análisis parciales (solo w vs. solo S/α). Este capítulo establece el criterio formal para determinar cuándo la incertidumbre ontológica es la que necesita resolverse primero.

El criterio formal de prioridad ontológica

La transformación formal

La incertidumbre ontológica necesita resolverse primero cuando la anchura del rango de R*_neta debida a la incertidumbre ontológica supera la anchura debida a la incertidumbre empírica.

Criterio de prioridad ontológica Prioritario SDO ⟺ (R*_máx − R*_mín) × (S_máx − S_mín) >

(w_máx − w_mín) × ΔR*/Δw Donde ΔR*/Δw es la sensibilidad de R* a variaciones en w (la pendiente del eigenvector respecto al peso ajustado). Cuando la contribución de la incertidumbre ontológica al rango de R*_neta supera la contribución de la incertidumbre empírica, el SDO es el instrumento prioritario.

En términos más intuitivos: la incertidumbre ontológica es prioritaria cuando el rango de S es tan amplio que, incluso si w se conociera con precisión perfecta, la conclusión sobre R*_neta no podría determinarse. Ese es el caso cuando la distribución sobre Hijos es muy difusa — cuando el SDO no puede distinguir entre Anteros (S baja) y Fobos (S alta), por ejemplo, la ambigüedad produce un rango de S tan amplio que domina cualquier incertidumbre empírica sobre w.

La incertidumbre empírica es prioritaria cuando, incluso si el Hijo dominante se conociera con certeza, la evidencia sobre w es tan pobre que la distribución de R* es tan amplia que la corrección por S no puede refinar suficientemente R*_neta. Ese es el caso cuando hay pocos documentos del caso y los testimonios son altamente contradictorios.

La prueba práctica

En la práctica, la forma más directa de aplicar el criterio es realizar los dos análisis parciales del capítulo 4.1 (sensibilidad solo a w con S central, sensibilidad solo a S/α con w central) y comparar los rangos de R*_neta que producen. El análisis parcial que produce el rango más amplio indica la fuente de incertidumbre que domina — y esa es la que debe resolverse primero.

Caso comparativo: cuando la ontología domina y cuando la empiria domina Caso A — La ontología domina: el grafo está bien documentado (w ∈ [0.68, 0.76] para todas las aristas, rangos estrechos). La distribución sobre Hijos del diseñador es P(Anteros) = 0.45, P(Fobos) = 0.45, P(Eros) = 0.10 (muy difusa). S_mín = 0.45×0.08 + 0.45×0.70 + 0.10×0.30 = 0.036+0.315+0.030 = 0.381. S_máx

La transformación formal

= 0.45×0.30 + 0.45×0.92 + 0.10×0.60 = 0.135+0.414+0.060 = 0.609. El rango de S es enorme (0.381, 0.609). El análisis parcial con w central produce R*_neta ∈ [0.30, 0.55]. El análisis parcial con S central (S ≈ 0.495) produce R*_neta ≈ 0.38. La ontología es el factor dominante — mejorar la observación SDO es prioritario. Caso B — La empiria domina: el Hijo del diseñador es claramente Anteros (P(Anteros) = 0.88), S ∈ [0.10, 0.32] (rango estrecho). Pero los documentos del caso son escasos: w ∈ [0.30, 0.75] para la arista clave (rango muy amplio). El análisis parcial con w fijo produce R*_neta ≈ R* × 0.79. El análisis parcial con S variable produce R*_neta ∈ R* × [0.68, 0.90]. La empiria domina — investigar más documentos es prioritario.

### VIII.  Caso completo: propagación en el análisis del banco con incertidumbre ontológica

Este capítulo trabaja el caso del banco con los parámetros del capítulo 3.2 y agrega la incertidumbre ontológica para mostrar la cadena de propagación completa.

Los actores y sus distribuciones sobre Hijos observadas por el SDO:

Director (diseñador del sistema): las señales del SDO muestran que el Director actuó con deliberación y desde su propio eje en la mayor parte del período, con algunos momentos de respuesta a presión del consejo. Distribución: P(Anteros) = 0.70, P(Fobos) = 0.20, P(Eros) = 0.10. Asesor (ejecutor del protocolo): el SDO localiza señales consistentes con respuesta a amenaza concreta (despidos previos de colegas que rechazaron) con algo de parálisis ante lo posible. Distribución: P(Fobos) = 0.65, P(Deimos) = 0.25, P(indeterminado) = 0.10.

Paso 1 — Rangos de S por promedio ponderado

Director: S_mín = 0.70×0.08 + 0.20×0.70 + 0.10×0.30 = 0.056+0.140+0.030 = 0.226. S_máx = 0.70×0.30 + 0.20×0.92 + 0.10×0.60 = 0.210+0.184+0.060 = 0.454. S_Director ∈ [0.226, 0.454].

Asesor: S_mín = 0.65×0.70 + 0.25×0.75 + 0.10×0.55 = 0.455+0.188+0.055 = 0.698. S_máx = 0.65×0.92 + 0.25×0.95 + 0.10×0.80 = 0.598+0.238+0.080 = 0.916. S_Asesor ∈ [0.698, 0.916].

Paso 2 — Rangos de R*_neta

La transformación formal

Del análisis del capítulo 3.2 (con ajuste por IIC): R*_Director ∈ [0.38, 0.48] (incertidumbre empírica sobre w). R*_Asesor ∈ [0.25, 0.35].

R*_neta_Director ∈ [0.38× (1−0.454), 0.48× (1−0.226)] = [0.38×0.546, 0.48×0.774] = [0.208, 0.372].

R*_neta_Asesor ∈ [0.25× (1−0.916), 0.35× (1−0.698)] = [0.25×0.084, 0.35×0.302] = [0.021, 0.106].

Verificación de robustez

R*_neta_Director ∈ [0.208, 0.372]. R*_neta_Asesor ∈ [0.021, 0.106]. Los dos rangos no se solapan: incluso en el peor caso para el Director (R*_neta_Director = 0.208) y el mejor caso para el Asesor (R*_neta_Asesor = 0.106), el Director sigue teniendo mayor R*_neta. La conclusión es robusta frente al análisis de sensibilidad combinado (empírico + ontológico). Declaración A extendida.

Este resultado es significativamente más sólido que el que el análisis estándar sin incertidumbre ontológica podría producir: no solo el eigenvector da mayor R* al Director (robusto frente a la incertidumbre empírica) sino que incluso bajo la peor distribución de Hijos plausibles para el Director, su R*_neta sigue siendo mayor que el mejor R*_neta posible para el Asesor. La identidad del responsable principal es doblemente robusta.

### IX.  Cuándo la propagación produce Declaración D: el caso de convergencia de rangos

La propagación de la incertidumbre ontológica puede producir Declaración D extendida cuando los rangos de R*_neta de dos o más nodos se solapan significativamente — cuando no hay ninguna combinación plausible de Hijos y pesos w que produzca una separación clara entre los nodos.

El caso típico de solapamiento: el diseñador tiene R* algo mayor que el ejecutor, pero la incertidumbre sobre el Hijo del diseñador es alta (puede ser Anteros con S baja o Fobos con S alta) y la del ejecutor es moderada (probablemente Fobos con S alta). Si el diseñador actuó desde Anteros, tiene S baja y R*_neta alto. Si actuó desde Fobos, tiene

La transformación formal

S alta y R*_neta bajo — incluso más bajo que el R*_neta del ejecutor que tiene S moderada.

Cuando los rangos de R*_neta de dos nodos se solapan, la pregunta '¿quién tiene mayor R*_neta?' no tiene respuesta robusta dentro de la incertidumbre disponible. En ese caso, la Declaración D extendida especifica:

Primera especificación: qué valor de Hijo del diseñador determinaría la conclusión. Si el diseñador actuó desde Anteros (S ∈ [0.08, 0.30]), R*_neta_diseñador > R*_neta_ejecutor. Si actuó desde Fobos (S ∈ [0.70, 0.92]), R*_neta_ejecutor ≥ R*_neta_diseñador. La observación SDO que determine el Hijo del diseñador es la clave de la Declaración. Segunda especificación: qué observación SDO resolvería la ambigüedad. Las señales observacionales que distinguen Anteros de Fobos en el momento del diseño del sistema (capítulo 2.2, tabla de señales observacionales): ¿describió el diseñador el sistema como una expresión de sus propias convicciones (Anteros) o como una respuesta a presiones externas que lo forzaban (Fobos)? ¿Hay evidencia de que hubiera tenido opciones y eligió ese diseño específico (Anteros) o de que el margen real era muy estrecho (Fobos)?

La Declaración D extendida es así un instrumento de investigación: no solo dice 'no sabemos' sino 'para saber necesitamos esto específicamente'.

### X.  Las contribuciones relativas: cuando los dos tipos se amplifican y cuando se compensan

Hay situaciones donde los dos tipos de incertidumbre se amplifican mutuamente y situaciones donde se compensan. Reconocer cuál ocurre en cada caso permite estimar mejor si la robustez es posible con recursos disponibles.

Amplificación: cuando los dos tipos apuntan en la misma dirección de incertidumbre

La incertidumbre se amplifica cuando la incertidumbre empírica produce rangos de R* amplios y la incertidumbre ontológica produce rangos de S que tienen el mismo efecto en la misma dirección. Por

La transformación formal

ejemplo: el diseñador tiene R* ∈ [0.20, 0.55] (amplio por evidencia pobre) y S ∈ [0.10, 0.55] (amplio por Hijo incierto). R*_neta_diseñador ∈ [0.20×0.45, 0.55×0.90] = [0.09, 0.495] — un rango enorme que no permite ninguna conclusión sobre responsabilidad neta. En ese caso, es muy probable que se requiera Declaración D y que ambos tipos de investigación sean necesarios simultáneamente.

Compensación: cuando los dos tipos se contrarrestan

La incertidumbre se compensa cuando la incertidumbre empírica produce un rango de R* amplio pero la incertidumbre ontológica es baja (Hijo bien determinado), o viceversa. Por ejemplo: R*_diseñador ∈ [0.20, 0.55] (amplio) pero S_diseñador ∈ [0.08, 0.18] (estrecho, Anteros claramente dominante). R*_neta_diseñador ∈ [0.20×0.82, 0.55×0.92] = [0.164, 0.506]. El rango es amplio, pero siempre mayor que, por ejemplo, R*_neta_ejecutor ∈ [0.02, 0.11] (bien determinado por Fobos claro y R* limitado). En este caso, a pesar del rango amplio de R* del diseñador, la conclusión puede ser robusta porque la comparación con el ejecutor es robusta.

### XI.  Errores frecuentes en la propagación de la incertidumbre ontológica

Error 1 — Propagar la distribución sobre Hijos directamente a R* sin pasar por S

Un error técnico: intentar construir directamente una distribución sobre R*_neta desde P(Hijos) sin el paso intermedio de S. Ese procedimiento omite la relación R*_neta = R* × (1−S) y puede producir rangos incorrectos. La propagación siempre debe seguir la cadena: P(Hijos) → [S_mín, S_máx] → [R*_neta_mín, R*_neta_máx].

Error 2 — Usar el mismo Hijo para φ₁ y φ₂ sin verificar si son distintos

El capítulo 2.3 estableció que el Hijo en φ₁ (que determina S) puede ser distinto al Hijo en φ₂ (que determina α). El análisis de propagación debe usar distribuciones separadas para los dos momentos cuando hay razones para pensar que el Hijo cambió entre el acto y la asunción. Si

La transformación formal

el mismo actor pudo haber actuado desde Anteros en φ₁, pero enfrenta Fobos en φ₂, los rangos de S y α son independientes y deben tratarse como tales en el análisis combinado.

Error 3 — Confundir la amplitud del rango con la probabilidad del extremo

Un rango [S_mín, S_máx] no dice que el valor de S es igualmente probable en todo el rango. El promedio ponderado de la distribución sobre Hijos produce una estimación de la distribución de S — no una distribución uniforme. Si P(Anteros) = 0.70 y P(Fobos) = 0.30, S está concentrada en el extremo inferior del rango (domina Anteros), aunque el rango cubra desde 0.08 hasta 0.92. El análisis de sensibilidad cubre el rango completo (para garantizar robustez), pero la declaración sobre el valor más probable de R*_neta debe reflejar la concentración de la distribución, no el rango completo.

Error 4 — No realizar la prueba de robustez cuando los rangos no se solapan por poco

Si los rangos de R*_neta de dos nodos apenas no se solapan (por ejemplo, R*_neta_Director ∈ [0.200, 0.372] y R*_neta_Asesor ∈ [0.021, 0.106] — diferencia de 0.094 en el peor caso), la robustez existe, pero es marginalmente. En ese caso, el analista debe verificar que el cálculo de los rangos es correcto y que no hay fuentes de incertidumbre adicionales que no fueron incluidas (como el parámetro β del ajuste por IIC). Un margen pequeño de no-solapamiento no es suficiente para una Declaración A extendida si hay incertidumbres adicionales no cubiertos.

### XII.  Lo que este capítulo establece para el capítulo 4.3

Este capítulo construyó la mecánica de la propagación de la incertidumbre ontológica al cálculo: cómo la distribución sobre Hijos produce rangos de S, cómo esos rangos se propagan a R*_neta, cómo el análisis de sensibilidad combinado cubre los dos tipos simultáneamente, y cómo el criterio de prioridad determina qué fuente de incertidumbre debe resolverse primero.

La transformación formal

Lo que este capítulo no establece — y lo que el capítulo 4.3 desarrolla — es qué ocurre cuando la incertidumbre no puede reducirse más. Hay incertidumbres que no se resuelven con más evidencia ni con mejor observación SDO. Hay propiedades del ego que el sistema, por principio ontológico, no puede calcular. Esos son los límites necesarios del método — no defectos técnicos sino consecuencias de la estructura del sistema que este libro derivó.

Notas al capítulo 4.2

1 El uso de la distribución de Dirichlet para muestrear distribuciones de probabilidad sobre los Hijos tiene una propiedad estadística conveniente: es la distribución conjugada para el modelo multinomial. Cuando el SDO observa señales que asigna a los distintos Hijos, el proceso de actualización de la distribución sobre Hijos sigue la lógica Bayesiana con prior de Dirichlet. Cada señal adicional que el SDO recolecta actualiza la distribución de Dirichlet — señales consistentes con un Hijo concentran la distribución en ese Hijo, señales contradictorias la difunden. Esto permite que el análisis de incertidumbre ontológica sea formalmente acumulativo: más señales SDO producen distribuciones más concentradas y rangos de S más estrechos.

2 La condición de independencia entre la incertidumbre empírica sobre w y la incertidumbre ontológica sobre el Hijo dominante merece una nota técnica. La independencia no es siempre válida: en algunos casos, la misma evidencia informa simultáneamente sobre w y sobre el Hijo. Un correo del Director instruyendo al Asesor de manera muy específica es evidencia de alta w (instrucción directa documentada) y también es una señal de que el Asesor actuó bajo Fobos (la instrucción explícita de un superior genera la amenaza concreta que Fobos describe). Cuando la misma evidencia afecta tanto w como la distribución sobre Hijos, la correlación debe modelarse explícitamente en el análisis de Monte Carlo en lugar de asumir independencia.

3 El método del análisis de vértices extremos como primera verificación de robustez tiene una ventaja computacional importante: solo requiere calcular el eigenvector para 2^n combinaciones de extremos (donde n es el número de parámetros con incertidumbre), lo que es manejable incluso para grafos de 10–15 nodos. El análisis de grilla con N=3 requiere 3^n cálculos, y el Monte Carlo requiere N cálculos independientemente del número de parámetros. Para análisis de gabinete donde la computación no es el factor limitante, el Monte Carlo con N ≥ 1000 muestras es la opción más completa. Para análisis de campo donde se necesita el resultado rápido, el análisis de vértices es suficiente para la primera verificación.

4 La especificación de qué observación SDO resolvería la ambigüedad en una Declaración D extendida tiene un paralelo en la metodología científica con la distinción entre 'experimento crucial' y 'observación de apoyo'. Una Declaración

La transformación formal

D que especifica exactamente qué señal observacional del SDO determinaría la conclusión es equivalente a proponer un experimento crucial — una observación cuyo resultado determinaría de manera decisiva entre las hipótesis en competencia. En el contexto del análisis causal, ese experimento crucial es la observación SDO que distingue el Hijo en φ₁ o en φ₂ del actor cuya incertidumbre ontológica limita la robustez.

La transformación formal

