## PARTE I · El flujo de trabajo del mediador

### Capítulo I·7
Los errores más frecuentes del protocolo
Cómo detectarlos antes de que afecten el resultado

### I. Por qué los errores del protocolo son más
costosos que los del cálculo
Un error de cálculo —un error aritmético, un midpoint mal
computado, una suma que no cierra— es detectable y corregible.
La suma de los R* no da 1.00: el mediador lo ve, encuentra el error,
lo corrige. Los errores del protocolo son de otra naturaleza:
producen resultados técnicamente correctos que miden algo
diferente de lo que el análisis necesita medir. El R* de un grafo
construido sobre los nodos equivocados suma exactamente 1.00.
El análisis es impecable. El resultado es incorrecto.
Los errores que este capítulo cataloga son los que la práctica
del sistema en catorce dominios ha producido con mayor
frecuencia. No son errores de comprensión teórica — el mediador
que llegó a este capítulo tiene el dominio teórico requerido. Son
errores de ejecución: momentos específicos del protocolo donde
la presión del caso, la urgencia del destinatario, o la complejidad
del expediente llevan al mediador a tomar un atajo que
compromete el resultado.

Metrología Causal · Vol. II

### II. Errores en la identificación del tipo de
pregunta
El error más frecuente y más costoso del protocolo es
comenzar a construir el grafo sin haber identificado el tipo de
pregunta. El grafo se construye, el cálculo se realiza, el expediente
se entrega — y el destinatario dice que eso no era lo que necesitaba.
No hay versión más costosa de este error.
El segundo error de identificación es confundir el tipo que
el destinatario formula con el tipo que el destinatario necesita. El
destinatario que dice "quiero saber qué pasó" puede necesitar Tipo
1, Tipo 3, o Tipo 4 dependiendo de para qué lo quiere saber. La
pregunta de seguimiento —"¿qué tiene que poder decir usted con
este análisis en la mano?"— no es opcional.
El tercer error es activar una sola serie cuando el caso
requiere dos o tres. El análisis simple es más rápido, más barato, y
satisface menos al destinatario que llegó con una necesidad
compuesta. El mediador que simplifica la demanda para
simplificar el trabajo produce un análisis menor que el necesario.

### III. Errores en la construcción del grafo
Error Síntoma en el Cómo detectarlo antes del
resultado cálculo
Nodo R* distribuido Verificar que D pueda enunciarse
sumidero no entre nodos sin en una sola frase específica con
específico: D coherencia magnitud y forma. 'El fraude de
definido como interpretable. No 10M en Q3' es D específico. 'Los
'el problema' o hay forma de problemas del banco' no lo es.
'los daños' sin comunicar el
forma resultado.
específica

Metrología Causal · Vol. II
Error Síntoma en el Cómo detectarlo antes del
resultado cálculo
Nodos de alto R* Preguntarse: ¿hay algún actor
R* excluidos artificialmente cuya ausencia del grafo habría
por falta de concentrado en cambiado el resultado? Si la
documentación nodos respuesta es sí, ese actor es un
documentados. nodo necesario aunque no esté
El grafo describe documentado.
lo que se puede
probar, no lo que
ocurrió.
Aristas El grafo describe Para cada arista, verificar: ¿la
construidas por la secuencia de eliminación del nodo de origen
correlación o eventos, no la cambia el resultado del nodo de
precedencia estructura causal. destino? Si la respuesta es no, la
temporal, no R* mide quién arista no es causal.
por influencia actuó antes, no
causal quién fue
condición
necesaria.
Grafo no El eigenvector Verificar antes del cálculo que
irreducible: hay no está definido desde cada nodo existe al menos
nodos sin o no converge. un camino dirigido al sumidero
camino al El método de Nf. Si no existe, el nodo no es
sumidero potencias no causalmente relevante para D y
termina. debe eliminarse del grafo.

### IV. Errores en la calibración de S y α
Error Por qué ocurre Cómo corregirlo
S asignado por El mediador Siempre derivar S desde el Hijo
intuición, no conoce el dominio dominante con su nivel EP
del caso y cree [Cap. I·4]. Si no hay ECO, usar

Metrología Causal · Vol. II
Error Por qué ocurre Cómo corregirlo
desde la tabla saber qué tan los tres criterios universales de
P(Hijos) sustituible fue el S de la Introducción y
nodo sin pasar por documentar la fuente.
el instrumento.
α confundido El ego muestra α requiere conducta verificable,
con culpa intensa o no emoción ni declaración.
remordimiento declara alta Verificar los tres criterios de la
o declaración responsabilidad y el Ruta B [Cap. I·5] con evidencia
mediador registra α documental antes de asignar α
alto. alto.
S y α asignados El mediador S y α son parámetros del nodo
al caso en describe el perfil en relación a D específico. El
general, no al general del nodo, mismo nodo puede tener S =
acto específico no su posición en el 0.20 en un acto y S = 0.80 en
analizado acto que produjo otro del mismo caso si las
D. condiciones del campo
cambiaron.
α > 1 − S El nodo asume más No corregir el dato —
(asunción de lo que su documentar la condición. Es el
mayor que la idiosincrasia caso del 'vanguardista de la
fracción permite. asunción' [Vol.I · Cap. IX·4]: el
idiosincrática) Matemáticamente ego que asume antes de que el
posible; sistema lo requiera.
interpretativamente
señala que el ego se
hace cargo de
responsabilidad
sistémica.

### V. La lista de verificación pre-cálculo
La lista que sigue se completa antes de iniciar cualquier
cálculo. No es opcional: es la condición de validez del análisis. El

Metrología Causal · Vol. II
mediador que encuentra un ítem sin completar no avanza al
cálculo: regresa al paso del protocolo donde ese ítem se produce.
Lista de verificación pre-cálculo
☐ Tipo(s) de pregunta identificado(s) con el destinatario →
serie(s) seleccionada(s) [Cap. I·1]
☐ Nodo sumidero Nf identificado con resultado D
específico en una sola frase
☐ Todos los nodos con capacidad causal identificados,
incluyendo los no documentados [Cap. I·2]
☐ Cada arista verificada como relación de influencia causal,
no de correlación o precedencia temporal
☐ Cada arista tiene nivel de evidencia E0–E8 asignado y
rango [a_ij, b_ij] correspondiente [Vol.I · Cap. VI·2]
☐ S de cada nodo derivado desde la tabla P(Hijos) → rango
de S [Cap. I·4] o desde criterios universales con fuente
documentada
☐ α de cada nodo derivado desde Ruta A, B, o C [Cap. I·5]
con fuente de evidencia documentada
☐ Test de condición sine qua non realizado → método de
cálculo seleccionado (eigenvector o Shapley) [Cap. I·6]
☐ Grafo verificado como irreducible: desde cada nodo
existe camino al sumidero Nf
☐ Si Serie II: nodo de diseño identificado y protocolos
declarados relevantes documentados
☐ Si Serie III: estándar adversarial verificado — solo
evidencia E1–E4 en el grafo, rangos estrechos confirmados
Producto de salida · Capítulo I·7

Metrología Causal · Vol. II
Lista de verificación completada y firmada: todos los ítems
confirmados. Esta lista queda archivada en el expediente
como evidencia de que el protocolo fue completado antes
del cálculo. Un ítem sin completar invalida el análisis hasta
que sea resuelto.
Notas al Capítulo I·7
1 El ítem sobre nodos no documentados —que el grafo debe incluir todo
actor cuya presencia o ausencia habría cambiado el resultado, aunque no
esté en el expediente— es el ítem más frecuentemente omitido y el que
produce los errores más costosos. La razón es comprensible: el análisis
documental crea un sesgo de visibilidad hacia lo que está en el
expediente. El mediador que trabaja en un caso largo puede confundir
lo que está documentado con lo que ocurrió. El test preventivo es
simple: "¿hay algún actor que obviamente importó en este resultado,
pero del que no tengo evidencia?" Si la respuesta es sí, ese actor entra al
grafo con nivel de evidencia E0 y rango amplio.
2 El ítem sobre la irreducibilidad del grafo tiene una consecuencia técnica
que el mediador debe conocer: la irreducibilidad no solo es condición
del método de potencias, sino del Teorema de Perron-Frobenius que
garantiza la existencia y unicidad del eigenvector positivo [Vol.II · Cap.
IV·2]. Un grafo reducible puede tener múltiples eigenvectores y el
método de potencias converge al mayor de ellos, que no necesariamente
corresponde a la distribución de responsabilidad causal. La verificación
de irreducibilidad no es burocrática: es la verificación de que el resultado
tiene interpretación metrológica válida.

Metrología Causal · Vol. II

