PARTE III · El análisis integrado: las tres series

### Capítulo III·2

### La verificación cruzada entre series

Consistencias esperadas y diagnóstico de inconsistencias

### I.  Por qué la verificación cruzada es parte del protocolo

Las tres series del análisis integrado describen el mismo sistema causal desde tres perspectivas. Si el análisis es internamente coherente, sus resultados deben ser mutuamente consistentes: lo que la Serie I dice sobre la posición del nodo de diseño debe ser compatible con lo que la Serie II dice sobre su congruencia, y ambas deben ser compatibles con lo que la Serie III dice sobre la robustez de esa posición. Una inconsistencia entre series no es un problema estético del expediente: es una señal de que algo en la construcción del grafo o en la calibración de los parámetros requiere revisión.

La verificación cruzada es el Paso 10 del protocolo integrado. No produce un resultado nuevo — produce una auditoría de los resultados existentes. Su output es binario: consistencia confirmada o inconsistencia detectada con diagnóstico. Cuando hay inconsistencia, el protocolo de diagnóstico de este capítulo

Metrología Causal · Vol. II

identifica el origen y prescribe la corrección antes de que el expediente sea entregado al destinatario.

### II.  Las cuatro consistencias esperadas del análisis integrado

Hay cuatro relaciones de consistencia que el análisis integrado debe cumplir. El mediador las verifica en orden después de completar los Pasos 7, 8 y 9 del protocolo del Capítulo III·1.

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

C1 · R*(base) ↔ R*(ajustado)

El ajuste de pesos por IIC debe ampliar R* del nodo de diseño N_D respecto al R*(base), o mantenerlo igual si IIC = 1. Nunca puede reducirlo: una baja congruencia del diseño siempre amplifica su peso causal real, nunca lo reduce.

R*(ajustado)_N D ≥ R*(base)_ND en todos los casos donde IIC_ND < 1

Si R*(ajustado)_N D < R*(base)_ND: el coeficiente k del ajuste está mal calibrado o la fórmula de ajuste tiene un error aritmético. Revisar el Paso 8.

C2 · Δ ↔ IIC El déficit de asunción

No hay umbral rígido.

Si IIC bajo con Δ muy bajo: el

Metrología Causal · Vol. II

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

Δ_ND del nodo de diseño y su IIC deben moverse en la misma dirección: cuando IIC es bajo (alta brecha de congruencia), α tiende a ser bajo también (baja asunción), y por tanto Δ tiende a ser alto. No es una identidad — son dimensiones distintas del mismo ego — pero una divergencia extrema requiere diagnóstico.

Divergencia extrema: IIC < 0.30 con Δ_ND < 0.10 (o IIC > 0.80 con Δ_ND > 0.60)

nodo de diseño declaró mal su campo, pero asumió sus actos con alta calidad — posible si el diseño fue erróneo, pero de buena fe. Documentar y comunicar al destinatario. Si IIC alto con Δ muy alto: el campo real coincidió con el declarado pero el nodo no actuó sobre sus consecuencias. También posible — documentar.

C3 · R*(adversarial ) ↔ R*(ajustado)

El vector R*(adversarial ) de Serie III debe ser consistente con R*(ajustado)

|R*(adversarial) _i − R*(ajustado)_i| ≤ 0.15 para el nodo principal de la atribución

Si la diferencia supera 0.15: el grafo adversarial incorporó cambios de estructura (aristas

Metrología Causal · Vol. II

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

de Serie II: si el análisis adversarial se construye sobre R*(ajustado), la diferencia entre los dos vectores debe explicarse solo por el estándar adversarial más restrictivo, no por diferencias en la estructura del grafo.

eliminadas, nodos removidos) que van más allá del estándar adversarial. Verificar que la única diferencia entre el grafo ajustado y el adversarial es el estándar de evidencia admisible.

C4 · ρ(θ) ↔ amplitud de rangos

La función de robustez ρ(θ) debe ser consistente con la amplitud promedio de los rangos [a_ij, b_ij] del grafo adversarial: rangos más estrechos (evidencia más fuerte) deben

No hay umbral rígido. Señal de alerta: ρ(θ) < 0.70 con amplitud promedio de rangos < 0.10

Si ρ(θ) baja con rangos estrechos: la inestabilidad es estructural, no de evidencia. Significa que hay múltiples nodos con R* muy similar y cualquier variación pequeña cambia el ranking. Este es el caso de mayor incertidumbre

Metrología Causal · Vol. II

Consistenci a

Relación que se verifica

Umbral de consistencia

Qué señala la violación

producir ρ(θ) más alto. Una ρ(θ) baja con rangos estrechos es una señal de que el ranking es genuinamente inestable — el nodo principal es vulnerable a pequeñas variaciones de los parámetros.

genuina del sistema.

### III.  El protocolo de diagnóstico de inconsistencias

Cuando una o más de las cuatro consistencias se violan, el mediador no entrega el expediente. Ejecuta el protocolo de diagnóstico antes de continuar. El protocolo tiene tres pasos que se aplican a cada inconsistencia detectada.

El primer paso es clasificar la inconsistencia: ¿es aritmética, de calibración, o estructural? Una inconsistencia aritmética es un error de cálculo — un número equivocado en algún paso. Una inconsistencia de calibración es un parámetro (S, α, k, o los rangos) que no refleja correctamente la evidencia disponible. Una inconsistencia estructural es una propiedad del grafo que produce resultados matemáticamente válidos, pero interpretativamente

Metrología Causal · Vol. II

incompatibles — típicamente, un nodo mal clasificado o una arista mal dirigida.

El segundo paso es localizar el origen. Cada inconsistencia tiene un paso del protocolo donde se origina. La tabla del Paso 10 del Capítulo III·1 mapea las series a sus pasos — el mediador sigue esa traza hasta encontrar el paso específico donde la inconsistencia se introduce.

El tercer paso es corregir y reverificar. Una vez corregido el origen, el mediador repite todos los cálculos que dependen del parámetro corregido — incluyendo todos los pasos de todas las series que usan ese parámetro como insumo — y reverifica las cuatro consistencias sobre los resultados nuevos.

Diagnóstico rápido por tipo de inconsistencia

C1 violada (R* ajustado < R* base): origen aritmético en el Paso 8. Revisar la fórmula del ajuste de pesos: w_ij(ajustado) debe ser mayor que w_ij(base) cuando IIC < 1 y k > 0. Verificar que la renormalización de W(ajustado) se aplicó correctamente.

C2 extrema (IIC bajo con Δ muy bajo): origen de calibración de α. Revisar la Ruta B del nodo de diseño: los tres criterios (conocimiento, acción, oportunidad) pueden estar calibrados hacia arriba sin evidencia suficiente. O es un caso genuino de diseño erróneo de buena fe — documentar.

C3 violada (R* adversarial diverge de R* ajustado > 0.15): origen estructural en el grafo adversarial. El mediador introdujo cambios de estructura al construir el grafo adversarial que van más allá del estándar de evidencia. Solo se pueden eliminar aristas que no cumplen el estándar adversarial — no aristas que se podrían cuestionar por otras razones.

Metrología Causal · Vol. II

C4 con ρ(θ) bajo y rangos estrechos: no es un error — es una característica estructural del caso. El ranking es genuinamente inestable. Documentar en el reporte de sensibilidad y comunicar al destinatario como incertidumbre irreducible del análisis.

### IV.  La inconsistencia que no se corrige: el caso de incertidumbre genuina

Hay una situación donde la verificación cruzada detecta una inconsistencia que no tiene corrección: cuando múltiples nodos tienen valores de R* muy similares y cualquier variación razonable de los parámetros cambia el ranking. Esta situación no es un error del análisis — es una propiedad del sistema analizado: la responsabilidad causal está distribuida de manera tan homogénea entre varios nodos que no existe una diferencia estructural que el sistema pueda capturar con la evidencia disponible.

En ese caso, la verificación cruzada produce el diagnóstico correcto: incertidumbre estructural genuina. El expediente integrado documenta esa incertidumbre explícitamente, la Declaración de Serie III es nivel C o D, y el análisis narrativo comunica al destinatario que la distribución de responsabilidad en este caso no tiene un nodo principal claramente distinguible dado el nivel de evidencia disponible. Esa comunicación honesta es más valiosa para el destinatario que una falsa certeza producida por ignorar la incertidumbre.

Producto de salida · Capítulo III·2

Verificación cruzada completada: las cuatro consistencias C1–C4 verificadas con resultado documentado (consistente / inconsistente con diagnóstico). Si hay inconsistencias corregidas: los cálculos afectados repetidos y las consistencias reverificadas. Si hay incertidumbre genuina (C4

Metrología Causal · Vol. II

### estructural): documentada en el expediente integrado con su interpretación.

Notas al Capítulo III·2

1  La consistencia C2 entre Δ e IIC merece una clarificación conceptual importante. Δ y el IIC miden fenómenos relacionados pero distintos. Δ mide si el ego integró sus colapsos como propios mediante conducta verificable — es una medición de la segunda mediación φ□ desde afuera. El IIC mide si el campo que el ego de diseño prometió producir corresponde al campo que efectivamente produjo — es una medición de la congruencia entre el diseño declarado y el real. Son el mismo ego visto desde dos dimensiones: la asunción de sus actos (Δ) y la integridad de su diseño (IIC). Su relación es esperada pero no matemáticamente determinada — dos egos pueden tener patrones distintos y ambos ser internamente coherentes.

2  El protocolo de diagnóstico de tres pasos (clasificar → localizar → corregir y reverificar) tiene un costo que el mediador debe anticipar: una corrección en el Paso 3 (cálculo de R* base) invalida todos los cálculos de los Pasos 4 al 9. Cuando se detecta una inconsistencia de origen aritmético en pasos tempranos, el mediador repite el análisis desde ese paso. La verificación cruzada al final del protocolo previene que errores de pasos tempranos lleguen al expediente final — su costo es el tiempo de la reverificación, que es siempre menor que el costo de entregar un expediente incorrecto.

Metrología Causal · Vol. II

