## PARTE III · La Taxonomía como instrumento de localización

### Capítulo III·9
El IIC: Índice de Integridad Causal —
derivación y propiedades
La medida formal de la brecha entre el diseño declarado y la
operación real

### I. La brecha entre diseño y operación como
objeto de medición
Las instituciones tienen dos versiones de sí mismas: la versión
declarada (los protocolos, las políticas, los procedimientos
formales que describen cómo debe operar la institución) y la
versión operacional (cómo opera efectivamente). La brecha
entre las dos versiones no es simplemente un problema de
implementación; es la medida del campo que el diseñador ha
producido en la realidad en comparación con el campo que
declaró haber producido. Cuando esa brecha es grande, el
campo real es distinto del campo declarado — y el daño que
se produce a través del campo real puede no atribuirse al
diseñador porque el diseñador puede señalar sus propios
protocolos como evidencia de que diseñó para evitar ese daño.
El Índice de Integridad Causal (IIC) mide formalmente esa
brecha. IIC_i ∈ [0, 1], donde IIC_i = 0 indica brecha total (el
diseño declarado y la operación real no se corresponden en

Metrología Causal
ningún aspecto relevante) e IIC_i = 1 indica congruencia total
(el diseño declarado y la operación real coinciden
completamente). En la práctica, el IIC de la mayoría de las
instituciones se encuentra en el intervalo [0.3, 0.7]: hay
congruencia parcial que protege parcialmente al diseñador de
la imputación plena pero que también refleja el fracaso parcial
del diseño en producir los comportamientos que declaró
producir.

### II. Derivación formal del IIC
El IIC se calcula para cada protocolo relevante del campo
institucional. Sea {p₁, p₂, ..., pₙ} el conjunto de protocolos
declarados por la institución en relación al resultado D. Para
cada protocolo pₖ, se calcula cₖ = corr (declarado_k,
observable_k) ∈ [0, 1], la correlación entre lo que el protocolo
declara que debería ocurrir y lo que el expediente muestra que
efectivamente ocurrió. El IIC global es: IIC = (1/n) Σₖ cₖ, el
promedio de las correlaciones sobre todos los protocolos
relevantes.
La elección de qué protocolos incluir en el conjunto {p₁, ...,
pₙ} es la decisión analítica central del cálculo del IIC. Los
protocolos relevantes son los que tienen relación directa con
el tipo de resultado D que se analiza. Para un caso de filtración
de información confidencial (el expediente Altamirano), los
protocolos relevantes son: el protocolo de confidencialidad de
carpetas de investigación, el protocolo de registro de visitas de
imputados, y el protocolo de atención de denuncias por
irregularidades. Para un caso de fraude financiero, los
protocolos relevantes son los de detección de transacciones
inusuales, los de supervisión de ejecutores y los de reporte a la
autoridad regulatoria.

Metrología Causal

### III. La relación entre el IIC y R* del nodo de
diseño
El IIC y R* del nodo de diseño tienen una relación inversa en
los casos típicos: a menor IIC, mayor R* del nodo de diseño.
Esta relación se deriva de la estructura del grafo causal. Si el
IIC del nodo de diseño es alto (el diseño declarado y la
operación real coinciden), entonces las aristas del grafo desde
el nodo de diseño hacia los ejecutores tienen pesos moderados
— el campo real es el que el diseñador declaró. Si el IIC es
bajo (hay una brecha grande), las aristas desde el nodo de
diseño tienen pesos más altos porque el campo real que el
nodo de diseño efectivamente produjo es más determinante
del comportamiento de los ejecutores que el campo que
declaró producir.
La consecuencia práctica: el IIC es el input que la Serie II del
sistema (Compliance Causal) usa para calibrar las aristas desde
el nodo de diseño en el grafo causal. Un IIC de 0.05 — como
el IIC_FRO en el caso Altamirano — implica aristas de alta
intensidad desde el nodo de diseño porque el campo real
diverge radicalmente del declarado. Ese campo real, que nadie
diseñó explícitamente pero que el nodo de diseño produjo con
sus omisiones y sus elecciones implícitas, es el campo que hizo
posibles los actos de los ejecutores.
El IIC tiene una propiedad que merece señalarse
explícitamente: mide la responsabilidad causal del diseñador
en el nivel del diseño del campo, independientemente de sus
intenciones. Un diseñador que declaró protocolos que no
implementó, que declaró una cultura organizacional que no
creó, que declaró mecanismos de control que no funcionaron
— ese diseñador tiene IIC bajo con independencia de si
«quiso» que los protocolos fallaran. La responsabilidad causal
de la brecha es del diseñador porque el diseñador es la

Metrología Causal
condición sine qua non de la coincidencia o divergencia entre
el diseño declarado y el real.
Notas al capítulo III·9
1 El IIC tiene antecedentes conceptuales en la literatura sobre la brecha
entre teoría expuesta y teoría en uso de Chris Argyris y Donald Schön
(Theory in Practice, 1974). Argyris y Schön distinguen entre lo que las
personas dicen que hacen (teoría expuesta) y lo que efectivamente hacen
(teoría en uso). El IIC es la medida formal de esa brecha aplicada al nivel
institucional en el contexto del análisis causal. La innovación del sistema
es convertir esa brecha en un parámetro del modelo que alimenta el
cálculo de R*, estableciendo la conexión directa entre la brecha de
integridad y la responsabilidad causal del nodo de diseño.

Metrología Causal

