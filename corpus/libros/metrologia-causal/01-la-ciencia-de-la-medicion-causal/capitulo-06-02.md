## PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·2
La hoja de calibración I: estructura y
producción
El mapa del caso: nodos, aristas, rangos de peso y evidencia

### I. Estructura completa de la hoja de calibración
La hoja de calibración tiene cinco columnas para cada arista
del grafo causal. La primera columna identifica la arista: el par
ordenado (i, j) que describe la influencia causal del nodo i
sobre el nodo j. La segunda columna describe la influencia en
lenguaje natural: qué tipo de relación causal existe entre i y j y
a través de qué mecanismo. La tercera columna establece el
rango de peso [a_ij, b_ij]: los valores mínimo y máximo de la
intensidad de la influencia causal que son consistentes con la
evidencia disponible. La cuarta columna describe la evidencia
que fundamenta el rango: qué documentos, testimonios o
registros informan sobre la influencia. La quinta columna
asigna el nivel de certeza al rango: alto (el rango es estrecho
porque hay evidencia directa), medio (el rango es moderado
porque la evidencia es inferida) o bajo (el rango es amplio
porque la evidencia es hipotética).
Las aristas se organizan en la hoja de calibración siguiendo el
orden topológico del grafo: primero las aristas que salen del

Metrología Causal
nodo de diseño (el nivel más alto de la jerarquía causal), luego
las aristas entre nodos del nivel de ejecución, luego las aristas
de los ejecutores hacia el resultado D. Esta organización
topológica hace visible la estructura jerárquica del caso antes
de cualquier cálculo: el lector de la hoja puede ver quién
influyó sobre quién y en qué dirección sin necesitar calcular el
eigenvector.
Además de las cinco columnas de cada arista, la hoja de
calibración incluye una sección de descripción de nodos: para
cada nodo de N, una descripción de quién es, cuál es su rol en
el sistema y qué posición ocupa en la jerarquía causal. Esa
descripción de nodos es el lugar donde el Hijo de Afrodita
dominante y el código de eje del SDO se registran para cada
nodo activo —los insumos que S tomará en la calibración de
los rangos.

### II. Los criterios formales para establecer los
rangos
Los rangos de peso se establecen siguiendo tres criterios
formales. El criterio de consistencia con la evidencia: w_ij ∈
[a_ij, b_ij] si y solo si el valor w_ij es consistente con toda la
evidencia disponible sobre la influencia de i sobre j — no
existe ninguna pieza de evidencia que sea incompatible con ese
valor. El criterio de amplitud proporcional a la incertidumbre:
la amplitud del rango (b_ij − a_ij) debe ser proporcional al
nivel de incertidumbre en la evidencia. Evidencia
confirmatoria directa produce rangos de amplitud ≤ 0.20;
evidencia inferida produce amplitud entre 0.20 y 0.40;
evidencia hipotética produce amplitud mayor de 0.40. El
criterio de no-solapamiento con cero: si hay evidencia de que
existe influencia causal de i sobre j, entonces a_ij > 0 — el
rango no incluye el cero.

Metrología Causal
Un error frecuente en la calibración es usar el mismo rango de
amplitud para todas las aristas del grafo, independientemente
del nivel de evidencia disponible para cada una. Este error
produce un espacio de parámetros artificialmente uniforme
que no refleja la estructura real de la incertidumbre en el caso.
Las aristas con evidencia directa tienen rangos estrechos; las
aristas hipotéticas tienen rangos amplios. La heterogeneidad
de los rangos es información sobre el caso, no un problema de
calibración.

### III. Los tipos de evidencia y su peso relativo
Las cuatro categorías de evidencia tienen distintos valores para
la calibración de rangos. La evidencia documental directa es la
más sólida: documentos que describen explícitamente la
influencia de i sobre j —correos que ordenan, registros que
confirman, contratos que establecen la relación. Esta evidencia
produce rangos de certeza alta con amplitud estrecha. La
evidencia estructural es la segunda: la influencia de i sobre j se
sigue de la posición estructural de i en el sistema (el diseñador
del protocolo influye sobre los ejecutores por definición de
posición), aunque no haya documento que lo describa
explícitamente. Esta evidencia produce rangos de certeza
media.
La evidencia testimonial es la tercera: testimonios de personas
que observaron la influencia de i sobre j, con la calibración
usual de los factores que afectan la credibilidad del testimonio
(interés del testigo, consistencia con otros testimonios,
consistencia con evidencia documental). La evidencia inferida
por exclusión es la cuarta: si la influencia no viene de ningún
otro nodo del grafo, debe venir de i — inferencia residual que
es la más débil y la que produce rangos de amplitud mayor.

Metrología Causal

