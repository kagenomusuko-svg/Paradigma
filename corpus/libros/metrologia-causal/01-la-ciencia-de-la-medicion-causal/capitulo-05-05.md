## PARTE V · Validez y límites de la medición causal

### Capítulo V·5
Taxonomía de errores de medición
Los cuatro tipos de error, sus fuentes y cómo cada uno se propaga
al resultado

### I. El marco de la taxonomía de errores
Una taxonomía de errores es el instrumento más útil para el
analista que quiere verificar la calidad de su propio análisis o
evaluar el análisis de otro. Sin una taxonomía, los errores son
optativos: el analista puede elegir no buscarlos o puede
buscarlos sin saber sistemáticamente dónde están. Con una
taxonomía, el analista tiene un protocolo de revisión que cubre
todas las categorías posibles de error y que establece para cada
categoría qué señales la delatan y qué protocolo aplica.
Los cuatro tipos de error del sistema están organizados por el
punto del análisis donde el error se introduce. El Error Tipo I
ocurre en la localización —en la identificación del Hijo
dominante. El Error Tipo II ocurre en la ponderación —en la
calibración de los pesos w_ij. El Error Tipo III ocurre en la
frontera —en la definición de qué nodos pertenecen a N. El
Error Tipo IV ocurre en la escala temporal —en la definición
de qué período analiza el grafo. Los cuatro tipos son

Metrología Causal
independientes: uno puede cometer Tipo III sin cometer
ninguno de los demás, y viceversa.

### II. Los cuatro tipos y su propagación
Tipo Fuente Cómo Propagac Señal de
del error se ión al detección
produce resultado
Error Aplicació El S del nodo Inconsiste
Tipo I n analista queda mal ncia entre
(localiz incorrecta asigna calibrado la
ación del árbol Fobos (tabla de S distribució
incorre de donde por Hijo). n P(Hijos)
cta del decisión correspo Si S del y el
Hijo) de la nde nodo es comporta
Taxonom Anteros, alto y miento
ía o o debería ser documenta
evidencia Deimos bajo, do del
insuficien donde R*_neta se actor. La
te para correspo subestima. firma de S
localizaci nde Si S calculado
ón Fobos, debería ser no es
confirma producie alto y se consistent
ble. ndo una calculó e con la
distribuci bajo, firma
ón R*_neta se documenta
P(Hijos) sobreestim l del nodo
incorrect a. Error en el
a para el directo en expediente
nodo. la .
distribució
n de

Metrología Causal
responsabi
lidades.
Error Calibració El peso R* de El ranking
Tipo II n de w_ij de la todos los de R* no
(ponder fuera del arista (i nodos del es
ación rango → j) se grafo consistent
incorre consistent calibra queda e con el
cta de e con la en 0.70 afectado, análisis
aristas) evidencia, cuando no solo de cualitativo
por sesgo la los nodos del caso.
del evidencia directame El nodo
analista, solo nte con mayor
evidencia justifica involucrad R* no es el
insuficien [0.30, os en la que la
te o 0.55]. El arista evidencia
supuestos eigenvect incorrecta. narrativa
erróneos or El identifica
sobre la calculado eigenvecto como más
naturalez sobre W r propaga central. El
a de la incorrect el error a análisis de
influencia o través de sensibilida
. produce todos los d tiene
R* caminos puntos de
incorrect del grafo. quiebre
o para Es el tipo inusualme
todos los de error de nte
nodos mayor sensibles.
conectad alcance.
os a esa
arista.
Error Exclusión El nodo R* de los R*_neta de
Tipo de nodos de ejecutores los
III causalme diseño se ejecutores

Metrología Causal
(fronter nte del sobreestim visibles es
a relevantes campo a. El nodo mayor que
incorre de N (por (el más de diseño su R* (el
cta del invisibilid frecuente no tiene descuento
sistema ad mente R*. El por S no es
) document excluido) análisis suficiente
al, por no está produce para
dificultad en N. Su una reducir
de influenci distribució R*_neta a
cuantifica a no está n que niveles
ción, o represent sobreimpu plausibles
por sesgo ada en el ta a los dado el
del grafo. Su ejecutores Hijo
analista R* es visibles y dominante
hacia los atribuido subimputa ). El S de
nodos a los al los
más nodos diseñador ejecutores
visibles). ejecutore invisible. visible
s que sí Es la indica alta
están en paradoja sustituibili
N. de la dad pero
visibilidad R*_neta es
en su alto, lo que
versión de es una
error. inconsiste
ncia.
Error Mezcla de El grafo R* no Los rangos
Tipo IV influencia incluye la tiene de peso de
(escala s de influenci interpretac las aristas
tempor escalas a del ión válida son
al temporale diseñado como comparati
incorre s distintas r original distribució vamente
cta) en el del n de incompati
mismo campo responsabi bles: una
grafo sin (hace lidad para arista tiene
la décadas) un peso [0.40,

Metrología Causal
correcció con el momento 0.60]
n mismo específico. basado en
temporal peso que El análisis evidencia
correspon la de de décadas
diente. influenci sensibilida y otra tiene
a del d no puede peso [0.55,
ejecutor producir 0.75]
del acto una basado en
(hace Declaració evidencia
semanas) n porque de
, sin el espacio semanas.
conversi de La
ón parámetro amplitud
temporal s no está no refleja
. bien incertidum
definido. bre sobre
la misma
escala
temporal.

### III. El error de mayor costo y el error más
frecuente
El error de mayor costo es el Error Tipo III — la exclusión de
nodos causalmente relevantes. Este error no solo produce una
distribución incorrecta de R*; produce la inversión exacta del
resultado que el sistema debe corregir. Si el Método Prometeo
sirve para hacer visible al diseñador del campo invisible, y el
error de frontera excluye al diseñador del campo del grafo, el
resultado del análisis reproduce la misma invisibilidad que el
sistema fue creado para corregir. Un análisis con Error Tipo
III que produce una Declaración A sobre los ejecutores sin el
nodo de diseño no es un análisis robusto: es un análisis que

Metrología Causal
incorrectamente identifica a los ejecutores como los nodos de
mayor responsabilidad.
El error más frecuente es el Error Tipo II — la calibración
incorrecta de los pesos. La frecuencia se debe a que la
evidencia sobre la intensidad de las influencias causales entre
nodos es típicamente incompleta y ambigua; la tentación de
usar el punto central del rango plausible como el peso
correcto, en lugar de usar el rango completo, es la fuente más
común de este error. El análisis de sensibilidad es el
instrumento de detección del Error Tipo II: si el ranking
cambia con variaciones pequeñas de los pesos, los pesos están
mal calibrados o el análisis está en el régimen de incertidumbre
que requiere la Declaración C en lugar de la A.

Metrología Causal

