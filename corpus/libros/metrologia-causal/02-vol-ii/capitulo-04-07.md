PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·7

### La conjetura del operador unificador

Programa de investigación: un operador que produce eigenvector o

Shapley según la estructura del grafo

### I.  El problema que la conjetura formula

Los Capítulos IV·2 y IV·6 establecen dos distribuciones de responsabilidad para dos tipos de grafo: el eigenvector cuando hay condición sine qua non individual, el Shapley cuando no la hay. Ambos métodos son matemáticamente sólidos y sus condiciones de aplicación están claramente delimitadas. La conjetura del operador unificador es la afirmación de que existe un operador único que produce la distribución correcta en ambos casos y en los casos mixtos.

### II.  El enunciado formal de la conjetura

Conjetura del Operador Unificador (C.O.U.)

Sea C la clase de grafos causales dirigidos ponderados G = (N, E, W) con W ≥ 0. Existe un operador O: C → □^|N| tal que: Metrología Causal · Vol. II

### (i) Cuando G tiene al menos un nodo condición sine qua non individual: O(G) = eigenvector principal normalizado de W.

### (ii) Cuando ningún nodo de G es condición sine qua non individual: O(G) = valor de Shapley del juego cooperativo v(S) asociado a G.

(iii) Para grafos mixtos con condición sine qua non parcial: O(G) interpola de manera continua entre los dos casos anteriores, sin discontinuidades.

### III.  Los cuatro precedentes en la literatura

Referencia Resultado relevante

Conexión con la C.O.U.

Hu & Shapley (2003) 'On authority distributions in organizations'

Demuestran que en estructuras jerárquicas, la distribución de autoridad que satisface el axioma eigenvectorial de centralidad y el axioma de Shapley de contribución marginal es la misma distribución.

Establece que eigenvector y Shapley pueden coincidir en una misma estructura. La C.O.U. generaliza este resultado a estructuras no jerárquicas.

Teng (2016) 'Scalable and Accurate Graph Clustering'

Demuestra que el PageRank puede interpretarse como el valor de Shapley de un juego de influencia social con función característica específica.

El eigenvector es un valor de Shapley para cierto juego. Si el juego correcto puede identificarse para el grafo causal, los dos son el mismo objeto con diferentes representaciones.

Metrología Causal · Vol. II

Referencia Resultado relevante

Conexión con la C.O.U.

Aleandri, Ciardiello & Di Liddo (2025) 'Power indices and graph centrality'

Demuestran que índices de poder que combinan centralidad eigenvectorial son valores de Shapley de juegos TU sobre grafos con uniones a priori.

Extiende el resultado de Teng a grafos con estructura de coalición explícita — el contexto del grafo causal con aristas ponderadas.

Forré & Jansma (2025) 'Causal Shapley values on DAGs'

Generalizan el valor de Shapley a funciones vectoriales en multigrafos dirigidos acíclicos ponderados.

El marco formal de Forré & Jansma es el contexto natural donde O podría definirse. Su generalización al grafo causal con IIC y los corolarios está pendiente.

### IV.  Lo que falta para la demostración

### Programa de demostración de la C.O.U. — tres pasos

Paso 1 — Definir C con precisión: especificar la clase de grafos sobre la que O está definido. La clase C debe incluir los grafos causales de este sistema (W ≥ 0, irreducibles, con nodo sumidero) y excluir los grafos donde ni eigenvector ni Shapley tienen interpretación causal válida.

Paso 2 — Encontrar los axiomas que determinan O unívocamente en toda C: los axiomas deben (a) reducirse a A1–A4 en el caso sine qua non, (b) reducirse a los axiomas de Shapley en el caso acumulativo, y (c) determinar una distribución única para casos mixtos.

Paso 3 — Demostrar continuidad entre los dos extremos: la interpolación del punto (iii) requiere una métrica sobre C que mida qué tan 'cerca' está

Metrología Causal · Vol. II

un grafo del caso sine qua non o del caso acumulativo, y demostrar que O varía continuamente con esa métrica.

### V.  El valor de la conjetura para el sistema

La conjetura del operador unificador no es necesaria para operar el sistema. El mediador que tiene claro cuándo usar eigenvector y cuándo usar Shapley tiene todo lo que necesita para el análisis de cualquier caso real. La conjetura importa por razones distintas.

La primera: la demostración de C.O.U. convertiría la metrología causal en una ciencia matemáticamente más completa. Un operador unificador sería la respuesta a todos los tipos de problema — lo que corresponde al nivel de generalidad que una teoría matemática de la responsabilidad causal debería alcanzar.

La segunda: la demostración identificaría la función característica v(S) del juego cooperativo que corresponde al grafo causal de este sistema. Esa función característica haría el cálculo del Shapley significativamente más eficiente para los casos acumulativos.

La tercera: el programa de investigación de C.O.U. es el punto de contacto más natural entre el sistema y la literatura matemática establecida. Una demostración publicable es la vía de validación externa más robusta que el sistema tiene disponible.

La conjetura del operador unificador se formula aquí con precisión matemática y honestidad sobre su estatus: es una conjetura, no un resultado. Su inclusión en este volumen no es para afirmar más de lo que la evidencia actual permite sino exactamente para lo contrario — para delimitar con precisión dónde está el límite del conocimiento formalizado del sistema y dónde comienza el programa de investigación que lo extenderá.

Metrología Causal · Vol. II

Principio de honestidad metrológica sobre los límites del sistema

### Producto de salida · Capítulo IV·7

La Conjetura del Operador Unificador formalmente enunciada: el operador O que produce el eigenvector en el caso sine qua non y el Shapley en el caso acumulativo, con interpolación continua en casos mixtos. Los cuatro precedentes de la literatura. El programa de demostración en tres pasos con identificación precisa de la brecha técnica que falta cerrar.

Notas al Capítulo IV·7

1  El enunciado del punto (iii) de la conjetura — interpolación continua para casos mixtos — es el más delicado porque 'fracción de sine qua non' no está formalmente definida. Una definición candidata: dado un grafo G con n nodos, sea k el número de nodos que pasan el test de condición sine qua non individual. La fracción de sine qua non es k/n. O(G) interpola entre el eigenvector (k/n = 1) y el Shapley (k/n = 0). El problema matemático es que k puede no ser continuo en ningún parámetro natural del grafo.

2  El resultado de Teng (2016) es el más directamente relevante para la C.O.U. Su demostración que el PageRank es el valor de Shapley de un juego de influencia social sugiere que la función característica v(S) del juego asociado al grafo causal podría expresarse en términos de la submatriz W_S. Esta línea de investigación es la más prometedora para el Paso 2 del programa de demostración.

3  La validación matemática externa de la C.O.U. es uno de los objetivos del programa de investigación del Centro Multidisciplinario Meriadock. Investigadores con formación en teoría de juegos cooperativos o álgebra lineal aplicada interesados en colaborar pueden contactar al Centro para acceder al manuscrito completo de la Axiomatización del Sistema de la Doble Mediación.

Metrología Causal · Vol. II

