## PARTE III · El análisis integrado: las tres series

### Capítulo III·1
El protocolo integrado
Secuencia de producción de las tres series y por qué el orden importa

### I. Qué es el análisis integrado y cuándo se activa
El análisis integrado aplica las tres series del Método
Prometeo sobre el mismo grafo causal. No es la suma de tres
análisis independientes: es un análisis único cuyas tres series están
relacionadas por insumos compartidos, verificaciones cruzadas y
un expediente que consolida sus resultados en un producto
coherente. La diferencia entre ejecutar tres series separadas y
ejecutar el análisis integrado es exactamente esa coherencia: el
análisis integrado verifica que los tres resultados son mutuamente
consistentes, y cuando no lo son, lo diagnostica.
El análisis integrado se activa cuando el destinatario necesita
más de un tipo de respuesta sobre el mismo caso. Las
combinaciones más frecuentes son: Tipos 1+3 (diagnóstico e
imputación) → Series I+III; Tipos 1+2 (diagnóstico y
compliance) → Series I+II; y Tipos 1+2+3 (diagnóstico,
compliance e imputación) → las tres series. En todos los casos, la
regla es la misma: el mediador activa todas las series que

Metrología Causal · Vol. II
corresponden a todos los tipos identificados y las ejecuta en el
orden que este capítulo establece.

### II. Por qué el orden de producción es invariante
El orden de las tres series no es una convención
procedimental. Es una consecuencia de las dependencias
matemáticas entre sus resultados. La Serie II requiere el vector R*
de la Serie I como denominador del IIC y como base del ajuste de
pesos. La Serie III requiere el vector R* de la Serie I como punto
central del hipercubo de parámetros. Ninguna de las dos series
puede producir un resultado válido sin el vector R* que la Serie I
entrega.
La dependencia va en una sola dirección: I → II → III. No
existe ninguna operación de la Serie I que requiera resultados de la
Serie II o III. No existe ninguna operación de la Serie II que
requiera resultados de la Serie III. El grafo de dependencias es
acíclico y el orden topológico es único: Serie I primero, Serie II
después si aplica, Serie III al final si aplica.
Por qué ejecutar las series en orden incorrecto produce
resultados inválidos
Serie II antes de Serie I: el IIC no tiene denominador. El
ajuste de pesos no tiene referencia. El fraude annona es un
número sin contexto causal.
Serie III antes de Serie I: el hipercubo no tiene punto central.
El análisis de sensibilidad mide variación alrededor de un
punto inexistente. La Declaración no tiene R*(adversarial)
que sostener.
Serie III antes de Serie II (cuando ambas aplican): el grafo adversarial de
Serie III no incorpora el ajuste de pesos por IIC que Serie II produjo. La

Metrología Causal · Vol. II
Declaración mide la robustez del R*(base), no del R*(ajustado). Es una
robustez incompleta.

### III. El protocolo paso a paso del análisis integrado
El protocolo integrado tiene diez pasos. Los primeros siete
son idénticos a los siete pasos de la Serie I — construyen el grafo
base y producen el vector R* con todos sus componentes. Los
pasos ocho, nueve y diez añaden las series adicionales en el orden
correcto.
Paso Operación Producto Serie
1 Construcción del grafo G = Hoja de I
(N, E, W) con todos los calibración base
nodos, aristas, rangos [a_ij,
b_ij] y niveles E0–E8
2 Verificación de Hoja de I
irreducibilidad y calibración
aperiodicidad. Corrección ε si validada
hay periodicidad
3 Cálculo de R* por método de Vector R*(base) I
potencias sobre midpoints.
Verificar Σ R*_i = 1
4 Determinación de S para cada R*_neta por nodo I
nodo desde P(Hijos) o
criterios universales. Cálculo
de R*_neta
5 Determinación de α para cada Δ por nodo — I
nodo desde Ruta A, B o C. Δ_total
Cálculo de Δ por nodo y
Δ_total

Metrología Causal · Vol. II
Paso Operación Producto Serie
6 Cuantificación de D_total si Fracciones AD_i I
el destinatario lo requiere. (condicional)
Cálculo de AD_i
7 Producción del expediente de Expediente Serie I I
Serie I: hoja de calibración + completo
vector R* + hipótesis de
prevención
8 Identificación del nodo de Expediente Serie II
diseño N_D. Cálculo de IIC II completo
sobre protocolos declarados
relevantes. Ajuste de pesos
por IIC. Recalculo de
R*(ajustado). Cálculo de
fraude annona. Producción
del ajuste debitor
9 Construcción del grafo Expediente Serie III
adversarial sobre III completo
R*(ajustado) de Serie II.
Verificación del estándar del
foro. Construcción del
hipercubo Π sobre rangos
adversariales. Evaluación del
ranking σ(w) en esquinas,
centro y muestra. Cálculo de
ρ(θ). Determinación del nivel
de Declaración
10 Verificación cruzada de Expediente I+II+III
consistencia entre las tres integrado
series. Diagnóstico de
inconsistencias. Producción
del expediente integrado
consolidado

Metrología Causal · Vol. II

### IV. La decisión crítica del Paso 9: cuál vector R*
entra al hipercubo
Cuando el análisis integrado incluye las tres series, el
mediador debe decidir qué vector R* usa como punto central del
hipercubo de la Serie III. Hay dos opciones: R*(base) de la Serie I
o R*(ajustado) de la Serie II. La decisión no es discrecional.
Si el caso incluye Series I+II+III, el hipercubo de Serie III
se construye sobre R*(ajustado) de la Serie II. La razón es directa:
el análisis de compliance de la Serie II actualizó la distribución de
responsabilidad incorporando la congruencia real del nodo de
diseño. La Serie III evalúa la robustez de esa distribución
actualizada, no de la distribución sin ajuste. Presentar una
Declaración basada en R*(base) cuando hay un R*(ajustado)
disponible sería medir la robustez de una distribución que el
propio análisis ya superó.
Si el caso incluye solo Series I+III (sin Serie II), el hipercubo
se construye sobre R*(base). No hay ajuste disponible y el vector
base es el correcto. El mediador documenta en la hoja de
calibración adversarial que no se aplicó ajuste de compliance y los
motivos (tipo de pregunta Tipo 1+3, sin nodo de diseño
identificado, o sin pregunta de compliance formulada por el
destinatario).

### V. El grafo único como fuente de coherencia
La característica más importante del análisis integrado es que
las tres series operan sobre el mismo grafo. No son tres grafos
distintos adaptados a cada pregunta: son tres lecturas distintas del
mismo objeto. El grafo base construido en el Paso 1 es la fuente
común de todas las distribuciones R* del expediente integrado.
Esta unicidad del grafo no impide que las series tengan
diferencias en sus versiones del grafo. La Serie II añade aristas

Metrología Causal · Vol. II
prospectivas del nodo de diseño. La Serie III restringe el grafo al
estándar adversarial del foro. Pero esas diferencias son versiones
del grafo base — extensiones o restricciones de un objeto común,
no grafos independientes. El mediador que construye grafos
separados para cada serie produce resultados que no son
comparables entre sí y pierde la ventaja principal del análisis
integrado: la verificación cruzada del Paso 10.
Producto de salida · Capítulo III·1
Mapa de ruta del análisis integrado: qué pasos se ejecutan, en
qué orden, qué produce cada uno, y cuál es la fuente de
insumo de cada paso. La decisión sobre qué vector R* entra
al hipercubo de Serie III queda documentada en el
encabezado del expediente integrado.
Notas al Capítulo III·1
1 La analogía entre el análisis integrado y una auditoría financiera con tres
niveles de revisión es útil pero imprecisa. Una auditoría financiera puede
realizarse en niveles independientes — cada nivel produce su resultado
sin necesidad de los demás. El análisis integrado no: la Serie III
literalmente no puede comenzar sin el vector R* de la Serie I, y cuando
hay compliance, necesita el vector de la Serie II. La dependencia no es
opcional ni procedimental: es matemática.
2 El Paso 10 — la verificación cruzada — no está en la mayoría de los
sistemas de análisis multicapa porque esos sistemas no producen
resultados que deberían ser mutuamente consistentes. El análisis
integrado sí los produce, porque las tres series describen el mismo
sistema desde tres perspectivas. La verificación cruzada no añade un
cuarto resultado: detecta si los tres resultados existentes cuentan la
misma historia. Cuando no la cuentan, el Capítulo III·2 establece qué
significa esa divergencia y qué hacer con ella.

Metrología Causal · Vol. II

