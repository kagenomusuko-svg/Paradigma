PARTE V · Validez y límites de la medición causal

### Capítulo V·5

### Taxonomía de errores de medición

Los cuatro tipos de error, sus fuentes y cómo cada uno se propaga

al resultado

### I.  El marco de la taxonomía de errores

Una taxonomía de errores es el instrumento más útil para el analista que quiere verificar la calidad de su propio análisis o evaluar el análisis de otro. Sin una taxonomía, los errores son optativos: el analista puede elegir no buscarlos o puede buscarlos sin saber sistemáticamente dónde están. Con una taxonomía, el analista tiene un protocolo de revisión que cubre todas las categorías posibles de error y que establece para cada categoría qué señales la delatan y qué protocolo aplica.

Los cuatro tipos de error del sistema están organizados por el punto del análisis donde el error se introduce. El Error Tipo I ocurre en la localización —en la identificación del Hijo dominante. El Error Tipo II ocurre en la ponderación —en la calibración de los pesos w_ij. El Error Tipo III ocurre en la frontera —en la definición de qué nodos pertenecen a N. El Error Tipo IV ocurre en la escala temporal —en la definición de qué período analiza el grafo. Los cuatro tipos son

Metrología Causal

independientes: uno puede cometer Tipo III sin cometer ninguno de los demás, y viceversa.

### II.  Los cuatro tipos y su propagación

Tipo Fuente del error

Cómo

Propagac

Señal de detección

se produce

ión al resultado

Error Tipo I (localiz ación incorre cta del Hijo)

Aplicació n incorrecta del árbol de decisión de la Taxonom ía o evidencia insuficien te para localizaci ón confirma ble.

El analista asigna Fobos donde correspo nde Anteros, o Deimos donde correspo nde Fobos, producie ndo una distribuci ón P(Hijos) incorrect a para el nodo.

S del nodo queda mal calibrado (tabla de S por Hijo). Si S del nodo es alto y debería ser bajo, R*_neta se subestima. Si S debería ser alto y se calculó bajo, R*_neta se sobreestim a. Error directo en la distribució n de

Inconsiste ncia entre la distribució n P(Hijos) y el comporta miento documenta do del actor. La firma de S calculado no es consistent e con la firma documenta l del nodo en el expediente .

Metrología Causal

responsabi lidades.

Error Tipo II (ponder ación incorre cta de aristas)

Calibració n de w_ij fuera del rango consistent e con la evidencia, por sesgo del analista, evidencia insuficien te o supuestos erróneos sobre la naturalez a de la influencia .

El peso de la arista (i → j) se calibra en 0.70 cuando la evidencia solo justifica [0.30, 0.55]. El eigenvect or calculado sobre W incorrect o produce R* incorrect o para todos los nodos conectad os a esa arista.

R* de todos los nodos del grafo queda afectado, no solo de los nodos directame nte involucrad os en la arista incorrecta. El eigenvecto r propaga el error a través de todos los caminos del grafo. Es el tipo de error de mayor alcance.

El ranking de R* no es consistent e con el análisis cualitativo del caso. El nodo con mayor R* no es el que la evidencia narrativa identifica como más central. El análisis de sensibilida d tiene puntos de quiebre inusualme nte sensibles.

Error Tipo III

Exclusión de nodos causalme

El nodo de diseño

R* de los ejecutores se

R*_neta de los ejecutores

Metrología Causal

(fronter a incorre cta del sistema )

nte relevantes de N (por invisibilid ad document al, por dificultad de cuantifica ción, o por sesgo del analista hacia los nodos más visibles).

del campo (el más frecuente mente excluido) no está en N. Su influenci a no está represent ada en el grafo. Su R* es atribuido a los nodos ejecutore s que sí están en N.

sobreestim a. El nodo de diseño no tiene R*. El análisis produce una distribució n que sobreimpu ta a los ejecutores visibles y subimputa al diseñador invisible. Es la paradoja de la visibilidad en su versión de error.

visibles es mayor que su R* (el descuento por S no es suficiente para reducir R*_neta a niveles plausibles dado el Hijo dominante ). El S de los ejecutores visible indica alta sustituibili dad pero R*_neta es alto, lo que es una inconsiste ncia.

Error Tipo IV (escala tempor al incorre cta)

Mezcla de influencia s de escalas temporale s distintas en el mismo grafo sin la

El grafo incluye la influenci a del diseñado r original del campo (hace décadas)

R* no tiene interpretac ión válida como distribució n de responsabi lidad para un

Los rangos de peso de las aristas son comparati vamente incompati bles: una arista tiene peso [0.40,

Metrología Causal

correcció n temporal correspon diente.

con el mismo peso que la influenci a del ejecutor del acto (hace semanas) , sin conversi ón temporal .

momento específico. El análisis de sensibilida d no puede producir una Declaració n porque el espacio de parámetro s no está bien definido.

0.60] basado en evidencia de décadas y otra tiene peso [0.55, 0.75] basado en evidencia de semanas. La amplitud no refleja incertidum bre sobre la misma escala temporal.

### III.  El error de mayor costo y el error más frecuente

El error de mayor costo es el Error Tipo III — la exclusión de nodos causalmente relevantes. Este error no solo produce una distribución incorrecta de R*; produce la inversión exacta del resultado que el sistema debe corregir. Si el Método Prometeo sirve para hacer visible al diseñador del campo invisible, y el error de frontera excluye al diseñador del campo del grafo, el resultado del análisis reproduce la misma invisibilidad que el sistema fue creado para corregir. Un análisis con Error Tipo III que produce una Declaración A sobre los ejecutores sin el nodo de diseño no es un análisis robusto: es un análisis que

Metrología Causal

incorrectamente identifica a los ejecutores como los nodos de mayor responsabilidad.

El error más frecuente es el Error Tipo II — la calibración incorrecta de los pesos. La frecuencia se debe a que la evidencia sobre la intensidad de las influencias causales entre nodos es típicamente incompleta y ambigua; la tentación de usar el punto central del rango plausible como el peso correcto, en lugar de usar el rango completo, es la fuente más común de este error. El análisis de sensibilidad es el instrumento de detección del Error Tipo II: si el ranking cambia con variaciones pequeñas de los pesos, los pesos están mal calibrados o el análisis está en el régimen de incertidumbre que requiere la Declaración C en lugar de la A.

Metrología Causal

