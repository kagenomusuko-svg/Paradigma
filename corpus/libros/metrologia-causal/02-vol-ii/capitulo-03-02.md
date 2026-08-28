## PARTE III · El análisis integrado: las tres series

### Capítulo III·2
La verificación cruzada entre series
Consistencias esperadas y diagnóstico de inconsistencias

### I. Por qué la verificación cruzada es parte del
protocolo
Las tres series del análisis integrado describen el mismo
sistema causal desde tres perspectivas. Si el análisis es
internamente coherente, sus resultados deben ser mutuamente
consistentes: lo que la Serie I dice sobre la posición del nodo de
diseño debe ser compatible con lo que la Serie II dice sobre su
congruencia, y ambas deben ser compatibles con lo que la Serie III
dice sobre la robustez de esa posición. Una inconsistencia entre
series no es un problema estético del expediente: es una señal de
que algo en la construcción del grafo o en la calibración de los
parámetros requiere revisión.
La verificación cruzada es el Paso 10 del protocolo integrado.
No produce un resultado nuevo — produce una auditoría de los
resultados existentes. Su output es binario: consistencia
confirmada o inconsistencia detectada con diagnóstico. Cuando
hay inconsistencia, el protocolo de diagnóstico de este capítulo

Metrología Causal · Vol. II
identifica el origen y prescribe la corrección antes de que el
expediente sea entregado al destinatario.

### II. Las cuatro consistencias esperadas del análisis
integrado
Hay cuatro relaciones de consistencia que el análisis
integrado debe cumplir. El mediador las verifica en orden después
de completar los Pasos 7, 8 y 9 del protocolo del Capítulo III·1.
Consistenci Relación Umbral de Qué señala la
a que se consistencia violación
verifica
C1 · R*(base) El ajuste de R*(ajustado)_N Si
↔ pesos por IIC D ≥ R*(ajustado)_N
R*(ajustado) debe ampliar R*(base)_ND en D <
R* del nodo todos los casos R*(base)_ND: el
de diseño donde IIC_ND coeficiente k del
N_D respecto < 1 ajuste está mal
al R*(base), o calibrado o la
mantenerlo fórmula de ajuste
igual si IIC = tiene un error

### 1. Nunca aritmético.
puede Revisar el Paso 8.
reducirlo: una
baja
congruencia
del diseño
siempre
amplifica su
peso causal
real, nunca lo
reduce.
C2 · Δ ↔ IIC El déficit de No hay umbral Si IIC bajo con Δ
asunción rígido. muy bajo: el

Metrología Causal · Vol. II
Consistenci Relación Umbral de Qué señala la
a que se consistencia violación
verifica
Δ_ND del Divergencia nodo de diseño
nodo de extrema: IIC < declaró mal su
diseño y su 0.30 con Δ_ND campo, pero
IIC deben < 0.10 (o IIC > asumió sus actos
moverse en la 0.80 con Δ_ND con alta calidad
misma > 0.60) — posible si el
dirección: diseño fue
cuando IIC es erróneo, pero de
bajo (alta buena fe.
brecha de Documentar y
congruencia), comunicar al
α tiende a ser destinatario. Si
bajo también IIC alto con Δ
(baja muy alto: el
asunción), y campo real
por tanto Δ coincidió con el
tiende a ser declarado pero el
alto. No es nodo no actuó
una identidad sobre sus
— son consecuencias.
dimensiones También posible
distintas del — documentar.
mismo ego —
pero una
divergencia
extrema
requiere
diagnóstico.
C3 · El vector |R*(adversarial) Si la diferencia
R*(adversarial R*(adversarial _i − supera 0.15: el
) ↔ ) de Serie III R*(ajustado)_i| grafo adversarial
R*(ajustado) debe ser ≤ 0.15 para el incorporó
consistente nodo principal cambios de
con de la atribución estructura
R*(ajustado) (aristas

Metrología Causal · Vol. II
Consistenci Relación Umbral de Qué señala la
a que se consistencia violación
verifica
de Serie II: si eliminadas,
el análisis nodos
adversarial se removidos) que
construye van más allá del
sobre estándar
R*(ajustado), adversarial.
la diferencia Verificar que la
entre los dos única diferencia
vectores debe entre el grafo
explicarse ajustado y el
solo por el adversarial es el
estándar estándar de
adversarial evidencia
más admisible.
restrictivo, no
por
diferencias en
la estructura
del grafo.
C4 · ρ(θ) ↔ La función de No hay umbral Si ρ(θ) baja con
amplitud de robustez ρ(θ) rígido. Señal de rangos estrechos:
rangos debe ser alerta: ρ(θ) < 0.70 la inestabilidad
consistente con amplitud es estructural, no
con la promedio de de evidencia.
amplitud rangos < 0.10 Significa que hay
promedio de múltiples nodos
los rangos con R* muy
[a_ij, b_ij] del similar y
grafo cualquier
adversarial: variación
rangos más pequeña cambia
estrechos el ranking. Este
(evidencia es el caso de
más fuerte) mayor
deben incertidumbre

Metrología Causal · Vol. II
Consistenci Relación Umbral de Qué señala la
a que se consistencia violación
verifica
producir ρ(θ) genuina del
más alto. Una sistema.
ρ(θ) baja con
rangos
estrechos es
una señal de
que el ranking
es
genuinamente
inestable — el
nodo
principal es
vulnerable a
pequeñas
variaciones de
los
parámetros.

### III. El protocolo de diagnóstico de inconsistencias
Cuando una o más de las cuatro consistencias se violan, el
mediador no entrega el expediente. Ejecuta el protocolo de
diagnóstico antes de continuar. El protocolo tiene tres pasos que
se aplican a cada inconsistencia detectada.
El primer paso es clasificar la inconsistencia: ¿es aritmética,
de calibración, o estructural? Una inconsistencia aritmética es un
error de cálculo — un número equivocado en algún paso. Una
inconsistencia de calibración es un parámetro (S, α, k, o los rangos)
que no refleja correctamente la evidencia disponible. Una
inconsistencia estructural es una propiedad del grafo que produce
resultados matemáticamente válidos, pero interpretativamente

Metrología Causal · Vol. II
incompatibles — típicamente, un nodo mal clasificado o una arista
mal dirigida.
El segundo paso es localizar el origen. Cada inconsistencia
tiene un paso del protocolo donde se origina. La tabla del Paso 10
del Capítulo III·1 mapea las series a sus pasos — el mediador sigue
esa traza hasta encontrar el paso específico donde la inconsistencia
se introduce.
El tercer paso es corregir y reverificar. Una vez corregido el
origen, el mediador repite todos los cálculos que dependen del
parámetro corregido — incluyendo todos los pasos de todas las
series que usan ese parámetro como insumo — y reverifica las
cuatro consistencias sobre los resultados nuevos.
Diagnóstico rápido por tipo de inconsistencia
C1 violada (R* ajustado < R* base): origen aritmético en el
Paso 8. Revisar la fórmula del ajuste de pesos: w_ij(ajustado)
debe ser mayor que w_ij(base) cuando IIC < 1 y k > 0.
Verificar que la renormalización de W(ajustado) se aplicó
correctamente.
C2 extrema (IIC bajo con Δ muy bajo): origen de calibración
de α. Revisar la Ruta B del nodo de diseño: los tres criterios
(conocimiento, acción, oportunidad) pueden estar calibrados
hacia arriba sin evidencia suficiente. O es un caso genuino de
diseño erróneo de buena fe — documentar.
C3 violada (R* adversarial diverge de R* ajustado > 0.15):
origen estructural en el grafo adversarial. El mediador
introdujo cambios de estructura al construir el grafo
adversarial que van más allá del estándar de evidencia. Solo
se pueden eliminar aristas que no cumplen el estándar
adversarial — no aristas que se podrían cuestionar por otras
razones.

Metrología Causal · Vol. II
C4 con ρ(θ) bajo y rangos estrechos: no es un error — es una característica
estructural del caso. El ranking es genuinamente inestable. Documentar en
el reporte de sensibilidad y comunicar al destinatario como incertidumbre
irreducible del análisis.

### IV. La inconsistencia que no se corrige: el caso de
incertidumbre genuina
Hay una situación donde la verificación cruzada detecta una
inconsistencia que no tiene corrección: cuando múltiples nodos
tienen valores de R* muy similares y cualquier variación razonable
de los parámetros cambia el ranking. Esta situación no es un error
del análisis — es una propiedad del sistema analizado: la
responsabilidad causal está distribuida de manera tan homogénea
entre varios nodos que no existe una diferencia estructural que el
sistema pueda capturar con la evidencia disponible.
En ese caso, la verificación cruzada produce el diagnóstico
correcto: incertidumbre estructural genuina. El expediente
integrado documenta esa incertidumbre explícitamente, la
Declaración de Serie III es nivel C o D, y el análisis narrativo
comunica al destinatario que la distribución de responsabilidad en
este caso no tiene un nodo principal claramente distinguible dado
el nivel de evidencia disponible. Esa comunicación honesta es más
valiosa para el destinatario que una falsa certeza producida por
ignorar la incertidumbre.
Producto de salida · Capítulo III·2
Verificación cruzada completada: las cuatro consistencias
C1–C4 verificadas con resultado documentado (consistente
/ inconsistente con diagnóstico). Si hay inconsistencias
corregidas: los cálculos afectados repetidos y las
consistencias reverificadas. Si hay incertidumbre genuina (C4

Metrología Causal · Vol. II
estructural): documentada en el expediente integrado con su
interpretación.
Notas al Capítulo III·2
1 La consistencia C2 entre Δ e IIC merece una clarificación conceptual
importante. Δ y el IIC miden fenómenos relacionados pero distintos. Δ
mide si el ego integró sus colapsos como propios mediante conducta
verificable — es una medición de la segunda mediación φ(cid:0) desde
afuera. El IIC mide si el campo que el ego de diseño prometió producir
corresponde al campo que efectivamente produjo — es una medición
de la congruencia entre el diseño declarado y el real. Son el mismo ego
visto desde dos dimensiones: la asunción de sus actos (Δ) y la integridad
de su diseño (IIC). Su relación es esperada pero no matemáticamente
determinada — dos egos pueden tener patrones distintos y ambos ser
internamente coherentes.
2 El protocolo de diagnóstico de tres pasos (clasificar → localizar → corregir
y reverificar) tiene un costo que el mediador debe anticipar: una
corrección en el Paso 3 (cálculo de R* base) invalida todos los cálculos
de los Pasos 4 al 9. Cuando se detecta una inconsistencia de origen
aritmético en pasos tempranos, el mediador repite el análisis desde ese
paso. La verificación cruzada al final del protocolo previene que errores
de pasos tempranos lleguen al expediente final — su costo es el tiempo
de la reverificación, que es siempre menor que el costo de entregar un
expediente incorrecto.

Metrología Causal · Vol. II

