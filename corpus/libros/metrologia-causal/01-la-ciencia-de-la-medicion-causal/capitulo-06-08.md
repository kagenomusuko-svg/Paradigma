## PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·8
El reporte de sensibilidad II: cómo leerlo
Los puntos de quiebre como mapa de vulnerabilidades y las dos
lecturas del reporte

### I. La lectura del ranking estable
La primera lectura del reporte es la de la función de robustez:
¿en qué porcentaje de los puntos del hipercubo explorados el
ranking es el mismo que en el punto central? Un ranking
estable en el 100% de los puntos explorados (incluyendo todas
las esquinas) es la señal de la Declaración A. La estabilidad
completa no dice que el análisis es perfecto — dice que, con
cualquier interpretación razonable de la evidencia, la
conclusión sobre quién tiene mayor responsabilidad causal es
la misma. Esto es lo que el adversario necesita refutar para
impugnar el análisis.
La lectura de la estabilidad parcial: si el ranking es estable en el
93% de los puntos, pero cambia en el 7% — y ese 7% está
concentrado en las esquinas del hipercubo en la dirección de
los pesos extremos — la Declaración B es la correcta. La
lectura identifica que los supuestos extremos sobre ciertos
pesos producen el cambio de ranking; la Declaración B declara
ese patrón explícitamente. El adversario puede atacar la

Metrología Causal
Declaración B demostrando que los supuestos extremos que
producen el cambio de ranking son en realidad los supuestos
centrales — que la evidencia justifica esos valores extremos
como los más plausibles.

### II. La lectura de los puntos de quiebre: el mapa
de vulnerabilidades
Los puntos de quiebre son el corazón diagnóstico del reporte.
Cada punto de quiebre especifica exactamente qué valores de
qué pesos producen el cambio de ranking. La tabla de puntos
de quiebre del reporte es el instrumento más valioso para el
analista que quiere fortalecer el análisis antes de presentarlo en
un foro adversarial: identifica exactamente qué evidencia
adicional sobre qué aristas reduciría la incertidumbre de
manera que el punto de quiebre quedaría fuera del rango
plausible.
La lectura estratégica de los puntos de quiebre: ¿están
concentrados en las aristas del nodo de diseño (las aristas con
certeza media o baja en la hoja de calibración) o en las aristas
de los ejecutores visibles (las aristas con certeza alta)? Si los
puntos de quiebre están en las aristas del nodo de diseño, el
ranking es vulnerable exactamente donde la evidencia es más
difícil de obtener — el diseñador del campo opera a través de
mecanismos informales que no dejan rastro documental. Esta
vulnerabilidad es constitutiva del tipo de caso y no puede
eliminarse completamente; solo puede minimizarse con la
evidencia estructural más sólida posible.

### III. El reporte como instrumento de diálogo con
el adversario

Metrología Causal
En contextos adversariales, el reporte de sensibilidad no es
solo una herramienta interna del analista — es el instrumento
de diálogo con la contraparte. La contraparte que recibe el
reporte puede leer los puntos de quiebre e identificar cuáles
son los supuestos sobre la evidencia que ella está dispuesta a
impugnar. El diálogo entonces no es «tu número es 0.38 y el
mío es 0.25» — es «yo argumento que la influencia de FRO
sobre ECP es ≤ 0.40 porque [evidencia], y si es ≤ 0.40 el punto
de quiebre que describes en el reporte aplica».
Este tipo de diálogo es más productivo para el tribunal que la
comparación de números puntuales: obliga a las dos partes a
concentrarse en la evidencia sobre la intensidad de la influencia
causal, que es exactamente el objeto de la disputa. El reporte
de sensibilidad convierte la disputa sobre la responsabilidad en
una disputa sobre la evidencia — que es donde debería estar.
Un reporte de sensibilidad bien construido que declara
explícitamente los puntos de quiebre es el mejor argumento
que un analista puede presentar ante un adversario sofisticado,
porque le dice al adversario exactamente qué necesita probar.

Metrología Causal

