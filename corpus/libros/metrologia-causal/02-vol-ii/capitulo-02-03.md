## PARTE II · El análisis simple: una sola serie

### Capítulo II·3
Serie III: Imputación Causal
El protocolo del análisis adversarial con Declaración de robustez

### I. Cuándo aplica la Serie III
La Serie III responde la pregunta de Tipo 3: ¿puede
sostenerse la atribución de responsabilidad ante impugnación
adversarial? Es la serie del escrutinio. Su función no es producir
una distribución de responsabilidad más precisa que la de la Serie
I — es verificar que la distribución de la Serie I es robusta: que no
cambia sustancialmente cuando los parámetros del grafo varían
dentro de los rangos que la evidencia permite.
La Serie III aplica siempre que el análisis deba resistir un
cuestionamiento externo organizado: el tribunal que puede revisar
cada arista del grafo, el regulador que puede impugnar cada valor
de S, el árbitro que puede cuestionar cada estimado de α. La
distinción respecto a la Serie I es de estándar, no de método: la
Serie I trabaja con midpoints; la Serie III trabaja con rangos
completos y verifica si la conclusión es estable a través de ellos.
La Serie III también se aplica siempre que el caso tenga
consecuencias de alta magnitud para el destinatario — no porque
las consecuencias cambien la metodología, sino porque el nivel de

Metrología Causal · Vol. II
escrutinio que esas consecuencias atraerán justifica invertir el
esfuerzo adicional del análisis de sensibilidad.

### II. Paso 1 · El estándar adversarial
El estándar adversarial restringe el grafo de Serie III a la
evidencia que resistiría impugnación en el foro donde el análisis
será usado. El mediador no puede usar en Serie III ninguna arista
que el adversario podría rechazar por deficiente en ese foro
específico.
En la práctica, el estándar adversarial se traduce en dos
restricciones concretas. Primera: solo las aristas con evidencia E1
o superior se incluyen en el grafo adversarial — las aristas E0
(nodos estructuralmente necesarios, pero no documentados)
quedan fuera o se incluyen con rangos muy amplios y nivel de
incertidumbre explícito. Segunda: los rangos [a_ij, b_ij] se calculan
con criterio conservador — se usa el rango más amplio que la
evidencia disponible puede justificar, no el más estrecho.
Foro Estándar de Restricción sobre el grafo
evidencia adversarial
aplicable
Tribunal civil Prueba por Aristas con evidencia E2 o
preponderancia de superior. Rangos moderados.
evidencia — más Declaración B o superior para
probable que no sostener la atribución.
Tribunal Más allá de duda Aristas con evidencia E3 o
penal razonable superior. Rangos estrechos.
Declaración A recomendada; B
como mínimo sostenible.
Regulador / Estándar específico Aristas con evidencia E2 o E3
Arbitraje del organismo — según el reglamento del

Metrología Causal · Vol. II
Foro Estándar de Restricción sobre el grafo
evidencia adversarial
aplicable
generalmente entre organismo. Verificar el estándar
civil y penal específico antes de construir el
grafo.
Auditoría Estándar de Aristas con evidencia E1 o
interna / razonabilidad superior. Rangos amplios
Investigación administrativa aceptables. Declaración C
suficiente en la mayoría de los
casos.
Comité de Escrutinio Todas las aristas documentadas y
ética / Par metodológico justificadas. Rangos con fuente
académico riguroso explícita. Declaración A o B
preferida.

### III. Paso 2 · R* bajo estándar adversarial
Con el grafo adversarial construido, el Paso 2 calcula R*
sobre los midpoints adversariales y R*_neta con S calibrado desde
evidencia admisible. El proceso es idéntico al de la Serie I — la
diferencia es que la hoja de calibración adversarial es más
restrictiva: menos aristas, rangos más amplios, valores de S con
fuentes explícitamente admisibles.
El vector R*(adversarial) es el punto de referencia del análisis
de sensibilidad del Paso 4. Si R*(adversarial) es significativamente
diferente de R*(base) de la Serie I, el mediador documenta la
diferencia y la incluye en el reporte de sensibilidad. Una
divergencia grande entre los dos vectores indica que parte de la
atribución de la Serie I descansa en evidencia que el foro
adversarial no admite — lo que el destinatario necesita saber antes
de presentar el análisis.

Metrología Causal · Vol. II

### IV. Paso 3 · El hipercubo de parámetros Π
El hipercubo de parámetros Π es el espacio de todas las
matrices de pesos W consistentes con los rangos [a_ij, b_ij] de la
hoja de calibración adversarial. Cada punto del hipercubo es una
matriz W específica — una asignación concreta de valores para
todos los pesos del grafo dentro de sus rangos admisibles.
El hipercubo tiene dimensión igual al número de aristas del
grafo. Un grafo de 4 nodos con 5 aristas tiene un hipercubo en
(cid:0)(cid:0). El espacio es continuo, pero el análisis de sensibilidad no
requiere explorarlo exhaustivamente: un conjunto de puntos de
evaluación bien elegido cubre las conclusiones relevantes.
Puntos de evaluación mínimos del hipercubo
Esquinas del hipercubo: todos los vértices donde cada peso
toma su valor mínimo a_ij o su valor máximo b_ij. Para n
aristas: 2ⁿ esquinas. En grafos de 4–6 nodos típicos (5–10
aristas): 32–1024 esquinas. Evaluar todas.
Centro del hipercubo: el vector de midpoints m_ij = (a_ij +
b_ij) / 2. Es el punto R*(adversarial) del Paso 2.
Muestreo aleatorio: si el número de esquinas supera 1000
(grafos de más de 10 aristas), completar con 500–1000
puntos aleatorios dentro del hipercubo usando distribución
uniforme sobre cada rango.
Puntos de quiebre: puntos específicos donde el ranking de los nodos cambia.
Identificarlos permite caracterizar exactamente qué condición produce cada
cambio de conclusión.

### V. Paso 4 · Análisis de estabilidad del ranking
σ(w)

Metrología Causal · Vol. II
Para cada punto w del hipercubo, el mediador calcula R*(w)
y registra el ranking σ(w): el ordenamiento de los nodos de mayor
a menor R*. La pregunta central del análisis de sensibilidad no es
si R* cambia — inevitablemente cambia cuando los parámetros
varían. La pregunta es si el ranking cambia: si el nodo que tiene el
mayor R* en el midpoint mantiene esa posición en todos los
puntos del hipercubo, o si en algunos puntos otro nodo lo supera.
Los puntos donde σ(w) cambia se llaman puntos de quiebre.
Un punto de quiebre es un valor específico de los parámetros
donde la conclusión sobre quién tiene mayor responsabilidad
causal se invierte. Identificar los puntos de quiebre permite al
mediador decirle al destinatario exactamente bajo qué condiciones
la atribución principal cambiaría.
Función de robustez ρ(θ)
ρ(θ) = Vol{ w ∈ Π : R*_θ(w) > R*_j(w) ∀ j ≠ θ } /
Vol(Π)
ρ(θ) es la fracción del hipercubo donde el nodo θ mantiene el ranking que
tiene en el midpoint. ρ(θ) = 1 significa que θ es siempre el nodo de mayor
R*, independientemente de cómo varíen los parámetros dentro de sus rangos
admisibles.

### VI. Paso 5 · La Declaración de robustez: niveles A,
B, C, D
La Declaración es el documento que comunica la robustez
del análisis al destinatario. Tiene cuatro niveles que corresponden
a distintos umbrales de la función ρ(θ). El nivel de Declaración
determina con qué fuerza el mediador puede sostener la atribución
ante el foro adversarial.

Metrología Causal · Vol. II
Nivel Condición Enunciado de la Cuando aplica
de ρ(θ) Declaración
A — ρ(θ) = 1.00 "La atribución es Análisis con
Robustez (100% del estructuralmente evidencia de alta
total hipercubo) robusta: el nodo θ calidad (E4–E8) y
mantiene la posición rangos estrechos.
causal más alta en Recomendado
todos los escenarios para foros
consistentes con la penales.
evidencia disponible.
Ninguna variación
admisible de los
parámetros cambia
esta conclusión."
B — ρ(θ) ≥ 0.90 "La atribución es Análisis con
Robustez (90% del sustancialmente mezcla de
sustancial hipercubo) robusta: el nodo θ evidencia E3–E5.
mantiene la posición Estándar para
causal más alta en el foros civiles y
90% o más de los regulatorios en la
escenarios mayoría de los
consistentes con la dominios.
evidencia. Los
escenarios donde esto
cambia representan
casos extremos de los
rangos admisibles."
C — ρ(θ) ≥ 0.70 "La atribución es Análisis con
Robustez (70% del moderadamente evidencia mixta o
moderada hipercubo) robusta: el nodo θ amplia
mantiene la posición incertidumbre en
causal más alta en el algunos
70–89% de los parámetros. Útil
escenarios para auditorías
consistentes con la internas y
evidencia. Existe un comités.
conjunto no trivial de
escenarios admisibles

Metrología Causal · Vol. II
Nivel Condición Enunciado de la Cuando aplica
de ρ(θ) Declaración
donde otro nodo tiene
mayor R*."
D — ρ(θ) < 0.70 "La atribución tiene La evidencia es
Robustez robustez limitada: en insuficiente para
limitada más del 30% de los sostener la
escenarios imputación ante
consistentes con la escrutinio
evidencia, otro nodo adversarial. Se
tiene mayor R* que θ. recomienda
La conclusión es buscar evidencia
sensible a variaciones adicional.
razonables de los
parámetros y requiere
evidencia adicional
antes de ser presentada
en foros
adversariales."

### VII. Paso 6 · El expediente de Serie III
El expediente de Serie III es el más completo del sistema.
Contiene todos los documentos de la Serie I y añade tres
documentos específicos del análisis adversarial.
Documento Contenido Nota
1 · Hoja de La hoja de calibración con el Diferente de la hoja de
calibración estándar adversarial Serie I: refleja las
adversarial aplicado: aristas excluidas restricciones del foro,
documentadas, rangos no la evidencia total
ampliados con justificación, disponible.
fuentes de evidencia con su
nivel admisible en el foro.

Metrología Causal · Vol. II
Documento Contenido Nota
2 · Vector El vector R* calculado bajo La comparación entre
R*(adversarial) el estándar adversarial. los dos vectores
Comparación con R*(base) informa al destinatario
de Serie I si hay diferencias qué parte de la
significativas. atribución descansa en
evidencia no admisible
en el foro.
3 · Reporte de La función ρ(θ) para el nodo El reporte de
sensibilidad principal de la atribución. sensibilidad es el
Los puntos de quiebre documento más
identificados con la técnico del expediente.
descripción de qué Se presenta en un
condición los produce. El apéndice separado para
mapa de estabilidad del audiencias no técnicas.
ranking sobre el hipercubo.
4 · El enunciado formal del La Declaración es el
Declaración nivel A, B, C o D con los documento que el
de robustez valores exactos de ρ(θ) que destinatario presenta
lo sustentan. Firmado por el en el foro. Es
mediador como responsable autocontenida: no
del análisis. requiere que el
destinatario entienda el
cálculo detrás.
Producto de salida · Capítulo II·3
Expediente de Serie III completo: hoja de calibración
adversarial + vector R*(adversarial) + reporte de sensibilidad
+ Declaración de robustez en nivel A, B, C, o D. La
Declaración es el producto central que el destinatario lleva al
foro adversarial.
Notas al Capítulo II·3

Metrología Causal · Vol. II
1 El análisis de sensibilidad de la Serie III responde una pregunta que con
frecuencia el destinatario no ha formulado pero que necesita responder:
¿qué tendría que ser verdad sobre el caso para que mi conclusión
cambiara? Los puntos de quiebre del hipercubo responden esa pregunta
con precisión. Un destinatario que conoce sus puntos de quiebre está
mejor preparado para el escrutinio adversarial que uno que solo conoce
R*(midpoint), porque sabe exactamente qué argumentos del adversario
cambiarían la conclusión y cuáles no.
2 La Declaración de nivel D no es un fracaso del análisis: es el resultado
honesto cuando la evidencia disponible no es suficiente para sostener la
atribución ante escrutinio adversarial. Una Declaración D informa al
destinatario que necesita evidencia adicional antes de presentar el
análisis — información que vale tanto como una Declaración A, porque
previene el error de presentar una atribución que el adversario puede
demoler con variaciones razonables de los parámetros.
3 La función ρ(θ) tal como se define en este capítulo mide la robustez de la
posición relativa de un nodo — si mantiene el ranking más alto. En
algunos casos el destinatario no necesita que el nodo θ tenga el R* más
alto; necesita que R*_θ supere un umbral específico (por ejemplo, que
supere 0.30 para activar una consecuencia normativa particular). En esos
casos, ρ se redefine como la fracción del hipercubo donde R*_θ(w) >
umbral, y el análisis sigue el mismo procedimiento con ese criterio de
estabilidad ajustado.

Metrología Causal · Vol. II

