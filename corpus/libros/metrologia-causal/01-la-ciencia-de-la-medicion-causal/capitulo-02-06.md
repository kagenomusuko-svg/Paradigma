PARTE II · Los fundamentos formales de la medición

### Capítulo II·6

### R* II: derivación completa y propiedades

El método de potencias, Perron-Frobenius y la paradoja de la

visibilidad

### I.  El método de potencias para calcular el eigenvector principal

El eigenvector principal de la matriz de adyacencia ponderada W se calcula iterativamente mediante el método de potencias. Sea v⁽⁰⁾ un vector inicial no nulo (en la práctica, el vector uniforme v⁽⁰⁾ = (1/n, 1/n, ..., 1/n)). La iteración procede como: v⁽ᵏ⁺¹⁾ = W·v⁽ᵏ⁾ / ||W·v⁽ᵏ⁾||, donde ||·|| es la norma L1 o L2 (la elección afecta la velocidad de convergencia, pero no el resultado). Bajo las condiciones de Perron-Frobenius (ver sección siguiente), esta secuencia converge al eigenvector principal de W independientemente del vector inicial.

La interpretación de la iteración es iluminadora para la comprensión del eigenvector como medida de centralidad. En el paso 0, cada nodo tiene el mismo score. En el paso 1, cada nodo recibe el score de sus vecinos (multiplicado por los pesos de las aristas): los nodos con vecinos de mayor peso inicial ganan score. En el paso 2, cada nodo recibe los scores actualizados de sus vecinos: los nodos que en el paso 1

Metrología Causal

ganaron score ahora distribuyen más score a sus propios vecinos. Después de k iteraciones, el score de cada nodo refleja la influencia que ha llegado a ese nodo a través de todos los caminos de longitud hasta k en el grafo. En el límite, el score refleja la influencia a través de todos los caminos de toda longitud —que es exactamente la centralidad causal recursiva que R* debe medir.

La velocidad de convergencia depende del cociente λ₂/λ₁ entre el segundo y el primer eigenvalor. Cuanto más pequeño es este cociente (cuanto más domina el primer eigenvalor sobre el segundo), más rápida es la convergencia. En los grafos causales de sistemas institucionales complejos, la convergencia es típicamente rápida porque el primer eigenvalor suele dominar claramente. En casos donde la convergencia es lenta —grafos con estructura casi-bipartita o con ciclos muy largas— se aplican técnicas de aceleración estándar.

### II.  Las condiciones de existencia y unicidad: Perron-Frobenius

El teorema de Perron-Frobenius para matrices no negativas establece las condiciones bajo las cuales el eigenvector principal existe, es único y tiene todos sus componentes positivos. Para matrices no negativas irreducibles: el eigenvalor principal λ₁ es simple (no repetido), positivo y estrictamente mayor que el valor absoluto de cualquier otro eigenvalor; el eigenvector correspondiente v₁ tiene todos sus componentes estrictamente positivos; cualquier otro eigenvalor de W tiene valor absoluto estrictamente menor que λ₁.

La condición de irreducibilidad del grafo — que existe un camino dirigido entre cualquier par de nodos — es la condición que garantiza que W es una matriz no negativa

Metrología Causal

irreducible. Esta es la razón por la que la propiedad de irreducibilidad del grafo causal es una condición de validez del sistema (II·3): sin irreducibilidad, el teorema de Perron-Frobenius no garantiza la unicidad del eigenvector y R* puede no estar bien definido.

La condición de positividad de todos los componentes de v₁ tiene una interpretación directa para R*: garantiza que ningún nodo tiene R* = 0 cuando el grafo es irreducible. Todo nodo causalmente conectado al resultado D tiene responsabilidad causal positiva. Esta propiedad es correcta ontológicamente: en un sistema donde todos los nodos están causalmente conectados, ninguno tiene responsabilidad cero. Los nodos con responsabilidad mínima tienen R* pequeño pero positivo; la asignación de R* = 0 solo procede cuando un nodo está fuera del componente causalmente relevante del grafo.

### III.  La normalización de R* y la paradoja de la visibilidad

El eigenvector principal v₁ se normaliza para que Σᵢ R*ᵢ = 1. Esta normalización tiene interpretación ontológica precisa: el total de responsabilidad causal sobre el resultado D se distribuye completamente entre todos los nodos de N. No «sobra» ni «falta» responsabilidad; el sistema es cerrado. La normalización también garantiza la comparabilidad entre análisis de casos distintos: R*_i = 0.38 significa lo mismo en el caso A que en el caso B —el nodo i cargó con el 38% del total de la responsabilidad causal.

La paradoja de la visibilidad se demuestra directamente desde la estructura del eigenvector. Consideremos un grafo con cuatro nodos: el diseñador del campo (D), el ejecutor (E), el encubridor (C) y el receptor del daño (V). Las aristas son: D

Metrología Causal

→ E (fuerte: D crea las condiciones en las que E actúa), D → C (media: D crea la cultura de encubrimiento), E → V (muy fuerte: E ejecuta el acto que daña a V), C → V (media: C prolonga el daño). En el grafo documental, E tiene la mayor visibilidad (firmó el citatorio, tuvo la conversación, ejecutó el acto). Sin embargo, el eigenvector de este grafo asigna el mayor R* a D porque D influye sobre todos los demás nodos a través de los cuales el daño llegó a V.

El mecanismo de la paradoja: el eigenvector propaga la influencia de D a través de D → E → V y a través de D → C → V. Aunque D no tenga ninguna arista directa a V, su influencia llega a V a través de dos caminos independientes. La suma de esas influencias indirectas excede la influencia directa de E (que solo tiene E → V) y de C (que solo tiene C → V). La paradoja de la visibilidad no es una paradoja del eigenvector: es una consecuencia correcta de que el diseñador del campo tiene influencia sobre el resultado a través de múltiples caminos que la visibilidad documental oculta.

Notas al capítulo II·6

1 El teorema de Perron-Frobenius fue probado independientemente por Oskar Perron (1907) y Georg Frobenius (1912). La formulación para matrices no negativas irreducibles es la que aplica al grafo causal de Prometeo, donde los pesos son no negativos y el grafo es irreducible por construcción (II·3). La condición de primitividad — que garantiza la convergencia del método de potencias — se satisface para matrices no negativas irreducibles aperiódicas, que es la condición adicional que el grafo causal debe verificar para garantizar la velocidad de convergencia estándar.

2 La demostración de la paradoja de la visibilidad en el párrafo anterior es intuitiva, pero puede formalizarse con precisión. Para un grafo acíclico con estructura jerárquica (diseñador → ejecutores → víctima), el eigenvector principal concentra peso en los nodos de mayor nivel jerárquico porque influyen sobre todos los demás. Para grafos con estructuras más complejas (ciclos de retroalimentación, influencias cruzadas), la demostración requiere el cálculo explícito del eigenvector.

Metrología Causal

La Parte VI de este libro muestra cómo leer la paradoja de la visibilidad en los documentos del expediente.

Metrología Causal

