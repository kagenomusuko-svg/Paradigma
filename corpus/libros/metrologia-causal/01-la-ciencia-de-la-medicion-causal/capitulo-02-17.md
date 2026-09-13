PARTE II · Los fundamentos formales de la medición

### Capítulo II·17

### Los rangos II: construcción formal del

### intervalo y análisis de sensibilidad

El protocolo de construcción, el criterio de robustez y la lógica del

adversario

### I.  Construcción formal del intervalo [a_ij, b_ij]

El intervalo [a_ij, b_ij] para cada peso w_ij se construye identificando el mínimo y el máximo de los valores de w_ij que son consistentes con la evidencia disponible para la arista (i, j). La consistencia con la evidencia se define como: el valor w_ij es consistente con la evidencia si y solo si no existe ninguna pieza de evidencia disponible que sea incompatible con ese valor como descripción de la intensidad de la influencia causal de i sobre j.

La construcción del intervalo procede en tres pasos. Primero: identificar la evidencia disponible para la arista (i, j) — los documentos, testimonios, registros y estructuras que informan sobre la influencia causal de i sobre j. Segundo: para cada pieza de evidencia, determinar el rango de valores de w_ij que es consistente con esa evidencia —qué tan fuerte o débil puede ser la influencia, dado lo que esa evidencia indica. Tercero: calcular la intersección de todos esos rangos — el conjunto de

Metrología Causal

valores de w_ij que es consistente con la totalidad de la evidencia disponible. El resultado es [a_ij, b_ij].

Los tres niveles de evidencia producen intervalos de amplitud distinta. Evidencia confirmatoria directa (documentos que describen explícitamente la influencia de i sobre j): intervalo estrecho, típicamente de amplitud 0.10-0.20. Evidencia inferida desde la estructura del campo (la influencia de i sobre j se sigue de la posición estructural de i, aunque no esté documentada directamente): intervalo medio, típicamente de amplitud 0.20-0.35. Evidencia hipotética (la influencia de i sobre j es plausible dado el contexto, pero no está confirmada): intervalo amplio, típicamente de amplitud 0.35-0.60.

### II.  El análisis de sensibilidad como exploración del espacio de parámetros

El análisis de sensibilidad explora cómo varía R* cuando los pesos del grafo varían dentro de sus intervalos. Formalmente: para cada punto (w₁₂, w₁₃, ..., w_{nm}) en el hipercubo Π_{ij} [a_ij, b_ij], calcular el vector R*(w) y registrar el ranking de los nodos. El análisis de sensibilidad mapea, para cada posible interpretación razonable de la evidencia, qué distribución de responsabilidad causal produce esa interpretación.

El resultado del análisis de sensibilidad es la función de ranking: ρ: Π_{ij} [a_ij, b_ij] → {rankings posibles}, que asigna a cada punto del hipercubo el ranking de responsabilidad que produce. Los «puntos de quiebre» son los puntos del hipercubo donde el ranking cambia — donde un nodo que era el primero en responsabilidad pasa a ser el segundo, o viceversa. La geometría de los puntos de quiebre describe la fragilidad del análisis: si los puntos de quiebre están

Metrología Causal

cerca del centro del hipercubo, el análisis es frágil; si están en los extremos, es robusto.

En la práctica, el hipercubo puede tener dimensionalidad alta (un grafo de diez nodos con quince aristas produce un hipercubo de quince dimensiones). El análisis exhaustivo de ese hipercubo no es computacionalmente inviable —el eigenvector se calcula rápidamente para cualquier punto— pero requiere una estrategia de muestreo eficiente. La estrategia estándar: muestreo sistemático en las esquinas del hipercubo (los puntos donde todos los pesos están en sus valores extremos), más muestreo aleatorio del interior, más búsqueda dirigida de puntos de quiebre en las dimensiones más sensibles.

### III.  El criterio de robustez y las cuatro declaraciones

El criterio de robustez establece qué nivel de estabilidad del ranking justifica cada tipo de declaración. La Declaración A — «con cualquier interpretación razonable de la evidencia disponible, el nodo i es el de mayor responsabilidad causal» — requiere que el ranking R*_i > R*_j para todo j ≠ i en todos los puntos del hipercubo. La robustez de la Declaración A es máxima: ni una sola interpretación razonable de la evidencia cambia el resultado.

La Declaración B — «el nodo i es el de mayor responsabilidad causal en la mayor parte de las interpretaciones razonables de la evidencia; las excepciones requieren supuestos sobre los pesos que están en los extremos del rango plausible» — permite que el ranking se invierta en los extremos del hipercubo, pero no en el interior. Esta declaración es robusta al rango central de la incertidumbre, aunque frágil en los

Metrología Causal

extremos. Es la declaración correcta cuando existe evidencia suficiente para el interior del rango, pero no para sus extremos.

La Declaración C — «el análisis produce un ranking probable pero no puede garantizar su estabilidad en todo el rango de la evidencia razonable» — corresponde a rangos de peso amplio donde el ranking cambia en una fracción significativa del hipercubo. Esta declaración no es un fracaso del análisis: es la descripción correcta de un caso donde la evidencia disponible es insuficiente para producir conclusiones robustas. El próximo paso es buscar evidencia adicional que estreche los rangos.

### IV.  La demostración sobre el adversario

La propiedad del rango más importante en contextos adversariales es la siguiente: para impugnar una Declaración A, el adversario debe demostrar que existe algún punto del hipercubo — alguna combinación de valores de w_ij dentro de sus rangos plausibles — donde el ranking cambia. Para hacer eso, el adversario debe demostrar que al menos uno de los pesos w_ij está fuera del intervalo [a_ij, b_ij] que el análisis estableció —que la evidencia que fundamenta ese intervalo es incorrecta o incompleta.

Esta transformación es fundamental para la dinámica del debate adversarial. El adversario ya no puede simplemente presentar un número puntual alternativo y decir «mi cálculo es diferente»: debe especificar qué pieza de evidencia justifica sacar algún peso de su rango plausible. La disputa migra de «¿cuál es el número correcto?» a «¿qué dice la evidencia sobre la intensidad de la influencia de i sobre j?». Ese es el debate correcto —y es el debate donde el analista que construyó el grafo desde evidencia rigurosa tiene ventaja estructural.

Metrología Causal

La Declaración A con análisis de sensibilidad es, en ese sentido, el instrumento más robusto que el sistema produce: no porque sea difícil de atacar técnicamente sino porque transforma el ataque correcto en un ataque sobre la evidencia, que es donde la estructura del caso vive. Un adversario que ataca el cálculo sin atacar la evidencia no ha impugnado la declaración: ha producido una alternativa aritmética sin base en los hechos.

Notas al capítulo II·17

1 El análisis de sensibilidad en sistemas de imputación causal tiene precedentes en el análisis de robustez de las sentencias de arbitraje internacional, donde se ha desarrollado la práctica de presentar «rangos de plausibilidad» en lugar de estimaciones puntuales para los parámetros de daño. Los trabajos de Rowe y otros sobre la incertidumbre en el análisis forense de daños económicos son un antecedente metodológico directo. La innovación de este sistema es la aplicación sistemática del análisis de sensibilidad al ranking de responsabilidad causal, no solo a la cuantificación del daño.

2 El hipercubo de parámetros y su análisis exhaustivo es computacionalmente tratable para grafos de hasta 20 nodos con los algoritmos actuales. Para grafos más grandes, se aplican técnicas de reducción de dimensionalidad: identificar las dimensiones (aristas) del hipercubo que más afectan el ranking y concentrar el análisis de sensibilidad en ellas. La identificación de las dimensiones más sensibles puede hacerse analíticamente usando el gradiente de R* respecto a cada peso w_ij, que se calcula directamente desde el eigenvector y el vector propio izquierdo de W.

Metrología Causal

