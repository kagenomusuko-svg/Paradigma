## PARTE II · Los fundamentos formales de la medición

### Capítulo II·3
El grafo causal: construcción y
propiedades
La estructura formal sobre la que opera todo el aparato del
sistema

### I. Definición formal del grafo G = (N, E, W)
El grafo causal G = (N, E, W) tiene tres componentes. El
primero: N es el conjunto de nodos. Cada nodo representa un
actor, institución o factor que tiene posición causal en el
resultado D. Los nodos pueden ser personas (el agente fiscal
que filtró la carpeta), instituciones (la fiscalía que diseñó el
campo de trabajo sin protocolos de confidencialidad), factores
estructurales (el sistema de incentivos que presionaba hacia la
productividad medida en expedientes cerrados), o ausencias
relevantes (la falta del protocolo de registro de visitas). La
definición del conjunto N es la primera decisión analítica y la
que más afecta los resultados finales.
El segundo: E ⊆ N × N es el conjunto de aristas dirigidas.
Cada arista (i, j) ∈ E representa una influencia causal del nodo
i sobre el nodo j en la producción del resultado D. La dirección
importa: (i, j) ≠ (j, i) en general. La arista (i, j) significa que i
influye causalmente sobre j; la arista (j, i) significaría que j

Metrología Causal
influye causalmente sobre i. En la mayor parte de los grafos
causales de sistemas institucionales, las aristas son asimétricas:
el diseñador influye sobre el ejecutor, no al revés (al menos no
con el mismo tipo de influencia causal).
El tercero: W: E → [0, 1] es la función de pesos. Cada arista
(i, j) tiene un peso w_ij ∈ [0, 1] que mide la intensidad de la
influencia causal de i sobre j en la producción de D. w_ij = 0
significa que i no influye causalmente sobre j (equivalente a (i,
j) ∉ E); w_ij = 1 significa que i determina completamente la
contribución causal de j. En la práctica, los pesos son rangos
[a_ij, b_ij] que capturan la incertidumbre sobre la magnitud de
la influencia; el cálculo puntual de R* usa el valor central (a_ij
+ b_ij) /2 y el análisis de sensibilidad explora el espacio
completo.

### II. Las propiedades que el grafo debe tener para
que R* sea interpretable
Para que R* sea interpretable como distribución de
responsabilidad causal, el grafo debe satisfacer cuatro
propiedades. La primera es la no-negatividad: todos los pesos
w_ij ≥ 0. Esta propiedad se satisface por construcción en la
mayoría de los casos: la influencia causal es positiva (i
contribuye a D a través de j) o nula. Las influencias negativas
(i inhibe la contribución de j) se modelan de manera distinta y
no como pesos negativos.
La segunda es la irreducibilidad: para todo par de nodos i, j ∈
N, existe un camino dirigido de i a j. Esta propiedad asegura
que la red de influencias está conectada — que no hay nodos
«aislados» cuya influencia no llega en última instancia al
resultado D. En grafos causales de sistemas institucionales
complejos, la irreducibilidad no siempre se satisface

Metrología Causal
directamente; puede requerir la adición de aristas de influencia
indirecta (a través del campo institucional compartido) o la
reducción del grafo al subconjunto irreducible de nodos
causalmente relevantes.
La tercera es la aperiodicidad: el grafo no tiene ciclos de
longitud fija que atrapan la propagación de influencia en un
loop. Los grafos con retroalimentación temporal (A influye
sobre B que a su vez influye sobre A en el siguiente período)
son en principio periódicos; el sistema los trata mediante
descomposición temporal, separando los ciclos en secuencias
de influencia unidireccional en el tiempo. La cuarta es la
orientación hacia el resultado: todas las aristas del grafo deben
representar influencias causales hacia D o hacia nodos que
influyen sobre D. Un nodo sin camino al resultado D no
debería estar en N.

### III. La construcción del grafo desde evidencia
La construcción del grafo es el trabajo analítico principal del
mediador. Requiere identificar los nodos, establecer las aristas
y asignar los rangos de peso. Cada una de estas tres
operaciones tiene criterios formales que determinan su validez.
La identificación de nodos sigue el criterio del nodo necesario
(II·2): se incluye en N todo actor, institución o factor sin el
cual D no se habría producido de esa forma específica. La
exclusión de un nodo necesario no produce un grafo
incompleto; produce un grafo incorrecto cuyo R* subestima
la responsabilidad del nodo excluido y sobreestima la de los
demás. El error de frontera —excluir nodos causalmente
relevantes— es el tipo de error más difícil de detectar y el más
costoso para la validez del resultado.

Metrología Causal
La identificación de aristas sigue tres niveles de certeza. Las
aristas documentalmente confirmadas (w_ij con rango
estrecho): la influencia está registrada en documentos,
testimonios o registros del sistema. Las aristas inferidas desde
la estructura del campo (w_ij con rango medio): la influencia
es estructuralmente necesaria, aunque no esté documentada
directamente. Las aristas hipotéticas (w_ij con rango amplio):
la influencia es plausible dado el contexto, pero no está
confirmada. Cada nivel de certeza produce un rango de w_ij
diferente; el análisis de sensibilidad posterior determina si el
resultado es robusto a través de todos los niveles.
La regla de construcción del grafo
Incluir en N todo nodo sin el cual D no se habría producido
de esa forma específica.
Incluir en E toda influencia causal de i sobre j que contribuya
a D, con independencia de la visibilidad de esa influencia.
Asignar a cada arista un rango [a_ij, b_ij] que refleje el nivel
de certeza de la evidencia disponible.
Verificar que el grafo es irreducible y aperiódico antes de
calcular R*.
Si el grafo no es irreducible, identificar qué nodos están fuera
del componente principal y tratar su exclusión como hipótesis
de análisis de sensibilidad.
Notas al capítulo II·3
1 El modelo del grafo causal usado en este sistema tiene antecedentes en
la teoría de los grafos causales de Judea Pearl (Causality, 2000) y en los
modelos de ecuaciones estructurales (SEM). La diferencia central con el
modelo de Pearl es que el sistema de Prometeo no usa el formalismo
do-calculus para definir la intervención causal: usa el criterio del nodo
necesario para definir la posición causal, lo que es más restrictivo, pero
también más interpretable en contextos forenses y clínicos. Pearl busca
definir qué ocurriría si se interviniera; este sistema busca describir quién
fue condición necesaria de lo que ocurrió.

Metrología Causal
2 La construcción del grafo desde evidencia documental es el trabajo
central de la Parte U de la Taxonomía General. Los capítulos I a XIII de
la Taxonomía establecen las firmas documentales específicas que cada
dominio produce para cada tipo de nodo. La Parte II de Metrología
Causal establece las propiedades formales que el grafo debe tener; la
Taxonomía establece cómo construirlo desde evidencia real en cada
campo específico.

Metrología Causal

