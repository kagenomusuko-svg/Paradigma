PARTE V · Validez y límites de la medición causal

### Capítulo V·2

### Condiciones de validez de R*

Las condiciones del grafo que garantizan que el eigenvector es

interpretable

### I.  Irreducibilidad: todos los nodos están causalmente conectados

La primera condición de validez de R* es la irreducibilidad del grafo: para todo par de nodos i, j ∈ N, debe existir un camino dirigido de i a j. En términos causales: cada nodo del grafo debe tener una cadena de influencias que llega, directa o indirectamente, al resultado D. La irreducibilidad garantiza que la matriz de adyacencia ponderada W es irreducible, que es la condición que el teorema de Perron-Frobenius requiere para la existencia y unicidad del eigenvector principal positivo.

La violación de la irreducibilidad ocurre cuando el grafo tiene componentes causalmente desconectadas: dos subgrupos de nodos donde la influencia no fluye entre ellos. Esto ocurre en la práctica cuando el analista incluye en N nodos que considera causalmente relevantes pero que no tienen camino al resultado D a través de los nodos del grafo. Un nodo que influyó sobre el contexto general pero no sobre ningún nodo que influya sobre D no tiene camino a D y viola la irreducibilidad.

Metrología Causal

El protocolo cuando se detecta violación de irreducibilidad: verificar si el nodo desconectado tiene influencia real sobre D a través de aristas que no fueron incluidas en el grafo (en ese caso, añadir las aristas y el nodo queda conectado) o si efectivamente no tiene influencia sobre D (en ese caso, retirar el nodo de N y reducir el grafo al subconjunto irreducible). Un nodo retirado del grafo por no tener camino a D no tiene R* calculable; declarar su exclusión es parte del protocolo de transparencia del análisis.

### II.  Aperiodicidad: el grafo no está atrapado en ciclos de longitud fija

La segunda condición de validez de R* es la aperiodicidad del grafo. El grafo es aperiódico si el máximo común divisor de las longitudes de todos los ciclos que contiene es 1. Si el grafo tiene solo ciclos de longitud 2 (A → B → A) o de longitud 3 (A → B → C → A) sin ciclos de otras longitudes, el grafo es periódico y el método de potencias oscila en lugar de converger.

La aperiodicidad es más fácil de satisfacer de lo que parece: cualquier grafo que tiene al menos un bucle (i → i) o al menos un nodo con un ciclo de longitud diferente a los demás es aperiódico. En la práctica, los grafos causales de sistemas institucionales tienen típicamente estructuras suficientemente complejas para ser aperiódicos. Los grafos donde la aperiodicidad puede fallar son los grafos muy simples con estructura bipartita perfecta: A→B, C→B, B→D, donde los nodos del «nivel 1» solo influyen sobre los del «nivel 2» y viceversa.

El protocolo cuando se detecta un grafo periódico: verificar si hay aristas de retroalimentación que no fueron incluidas (en

Metrología Causal

sistemas institucionales, las retroalimentaciones son frecuentes y su omisión puede producir periodicidad artificiosa) o añadir un pequeño peso ε en la diagonal de W para garantizar la aperiodicidad, con la declaración explícita de que se realizó esta modificación técnica y de que no cambia el resultado sustantivo del análisis.

### III.  Condiciones sobre la escala temporal y la estabilidad del campo

La tercera familia de condiciones de validez de R* es menos formal pero igualmente importante: las condiciones sobre la escala temporal del análisis. R* es una medida de centralidad causal sobre el grafo del evento D; ese grafo es válido para la escala temporal en que los pesos w_ij son estables. Si el análisis mezcla influencias de escalas temporales muy distintas — la influencia que un diseñador ejerció sobre el campo hace treinta años y la influencia que un ejecutor ejerció hace tres semanas — la comparación de sus R* puede no tener interpretación válida porque los dos pesos están midiendo cosas de naturaleza temporal distinta.

El protocolo para el análisis con múltiples escalas temporales: construir capas temporales del grafo. Para el nivel de diseño histórico (influencias de largo plazo que configuraron el campo c), usar una capa temporal; para el nivel de ejecución inmediata (influencias que operaron directamente sobre el evento D), usar otra capa. El R* de cada capa es válido dentro de esa capa; la comparación entre capas requiere una conversión que declare explícitamente los supuestos sobre la relación entre las dos escalas.

Notas al capítulo V·2

Metrología Causal

1 La condición de aperiodicidad puede verificarse calculando el máximo común divisor de los ciclos del grafo usando el algoritmo de Floyd-Warshall para la detección de ciclos. Para grafos de hasta veinte nodos, el cálculo es trivialmente rápido. La modificación ε en la diagonal —que se usa cuando la aperiodicidad falla— es una técnica estándar en la teoría de cadenas de Markov, donde la condición análoga se llama 'primitividad' de la matriz de transición.

Metrología Causal

