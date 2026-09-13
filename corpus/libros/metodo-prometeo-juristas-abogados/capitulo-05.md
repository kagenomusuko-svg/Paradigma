### Capítulo 5 PLD y delitos financieros complejos

El beneficiario invisible: imputar al arquitecto de un esquema que

nunca tocó el dinero

Este capítulo aplica el Método Prometeo al dominio que plantea el problema de imputación más difícil: la prevención de lavado de dinero y los delitos financieros complejos. La razón de la dificultad no es la falta de documentos — en muchos esquemas hay abundantes registros de transacciones. La razón es que el actor de mayor peso causal diseñó deliberadamente su propia invisibilidad. El arquitecto del esquema no aparece en los documentos. El testaferro que firma todo sí aparece.

Este capítulo tiene la misma estructura que el Capítulo 2: primero explica las herramientas adaptadas al dominio del PLD — cómo se renombran, qué significan aquí, qué tablas se usan. Luego el Capítulo 7 (el de presentación ante el tribunal) complementa con los documentos del expediente en contexto de investigación financiera.

Hay un instrumento nuevo en este capítulo que no apareció en los anteriores: el valor de Shapley. Se introduce porque hay casos de lavado con múltiples eslabones donde ningún nodo individual es condición necesaria del resultado — el dinero podría haber viajado por otra ruta — y el método de

El Método Prometeo: Imputación Causal para juristas y abogados

las rondas convencional asigna cero a todos. Shapley resuelve ese límite con precisión.

⚠ Una aclaración sobre el alcance: este capítulo enseña a construir el análisis causal de una operación de lavado para fines de investigación, litigio de recuperación de activos, extinción de dominio, y argumentación en procedimientos regulatorios. No es un manual de tipificación penal ni sustituye el análisis del cuerpo del delito. El Método Prometeo aporta evidencia estructurada sobre la necesidad causal — la decisión sobre los elementos del tipo corresponde al fiscal y al juez.

### §5.1 Por qué el PLD es el problema de imputación más difícil

En el fraude bancario del Capítulo 3, la inversión causal era un efecto colateral: el banco diseñó un sistema dañino y los ejecutores visibles cargaron con las consecuencias. En el lavado de dinero, la inversión causal es el objetivo del diseño. El esquema se construye precisamente para que el beneficiario real no aparezca en ningún documento y para que la cadena de intermediarios sea suficientemente larga como para que cualquier investigación se detenga en algún nodo intermedio.

El sistema convencional de PLD trabaja con señales de alerta: transacciones inusuales, montos sobre umbral, patrones de fragmentación. Esas señales son eficaces para detectar al ejecutor — el que mueve el dinero, el que abre las cuentas, el que firma los contratos. Raramente alcanzan al arquitecto del esquema, porque el arquitecto no mueve dinero: diseña el sistema que lo mueve. Su nombre puede

El Método Prometeo: Imputación Causal para juristas y abogados

no aparecer en ningún documento, o puede aparecer al final de una cadena tan larga de intermediarios que la conexión causal parece imposible de demostrar.

Analogía: La luz de una estrella muerta El astrónomo que observa una estrella desde la Tierra ve la luz que salió hace miles de años. La estrella puede ya no existir. El investigador de PLD que analiza una transacción ve el movimiento de dinero tal como llegó a su jurisdicción, no el origen que lo produjo meses o años atrás y en otra latitud. El grafo causal es el instrumento que permite reconstruir la fuente a partir de la luz que llegó.

La inversión causal en PLD:  Patrón estructural donde el actor de mayor peso causal (el arquitecto del esquema) tiene visibilidad documental nula, mientras el actor de menor peso causal (el testaferro) tiene visibilidad documental total porque firma todo. El arquitecto tiene R* ≈ 55-70% y α = 0. El testaferro tiene R* ≈ 4-8% y α = 100% forzado porque firmó los documentos y es el único identificable sin investigación. Δ del arquitecto = +55-70% (inversión máxima). Δ del testaferro = −70 a −90% (chivo expiatorio estructural).

Esa inversión no es accidental. El arquitecto la diseñó. Y hay una consecuencia matemática que el método hace visible: cuanto más sofisticado es el esquema de lavado, mayor es la concentración de R* en el nodo invisible. El arquitecto, al aumentar la sustituibilidad (S) de todos los nodos visibles para hacerlos fungibles, automáticamente concentra la necesidad causal en él mismo. La firma matemática del lavado bien diseñado es precisamente el R* alto del nodo que no aparece en los documentos.

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.2 La tabla de traducción: las herramientas del método en el lenguaje del PLD

Las herramientas del Capítulo 2 tienen exactamente los mismos fundamentos en este dominio. Lo que cambia es cómo se nombran y qué miden concretamente. Esta tabla permite al oficial de compliance, al fiscal de delitos financieros y al abogado de extinción de dominio moverse entre el lenguaje del método y el lenguaje de su campo sin tener que resolver ninguna ecuación adicional.

En PLD se llama Qué significa en la práctica del compliance y la investigación

Herramienta del método

Grafo causal G Mapa de la operación

La red completa de personas, entidades, cuentas y jurisdicciones que participaron en el esquema, con sus relaciones causales. Se construye de afuera hacia adentro: se empieza por los nodos visibles en documentos y se trabaja hacia atrás hasta el arquitecto.

Nodo de diseño Arquitecto del esquema

Quien eligió las jurisdicciones, definió los vehículos jurídicos, estableció los flujos y coordinó a los intermediarios. Raramente firma nada. Tiene el R* más alto y

El Método Prometeo: Imputación Causal para juristas y abogados

la visibilidad documental más baja.

Nodo instrumental

Vehículo financiero

La empresa fantasma, la cuenta bancaria, el fideicomiso opaco. No tiene voluntad propia. No se le calcula α, pero sí R* (necesidad causal de la operación). Su R* alto apunta hacia quien lo controló.

Nodo de ejecución con S alto

Testaferro / prestanombre

Persona física que aparece como director o accionista sin tener control real. Alta visibilidad documental. S muy alto (cualquier otra persona dispuesta habría firmado lo mismo). R* muy bajo.

R* (vector) Necesidad causal de la operación

R*_i mide cuánto dependía el éxito del esquema de que el nodo i existiera y actuara como lo hizo. Alto R* con visibilidad documental baja = señal del beneficiario real probable.

S (sustituibilidad)

Fungibilidad del rol

S alto = el nodo era un recurso genérico: cualquier otro prestanombre, abogado o entidad habría cumplido la misma función. El esquema no dependía de esa persona específica. S bajo = el nodo era idiosincrático.

El Método Prometeo: Imputación Causal para juristas y abogados

α (asunción) Cumplimiento de la obligación de reporte

α mide si el nodo reportó la operación inusual, rechazó al cliente, aplicó due diligence reforzada, o en cambio facilitó activa o pasivamente la operación. α = 0: no reportó. α = 1: reportó y cooperó.

Δ = R* − α Déficit de compliance

Δ alto positivo = el nodo fue causalmente necesario para el esquema y no cumplió su obligación de reporte. Es la medida del incumplimiento regulatorio proporcional a la participación causal.

D_total Daño al sistema financiero

T_invertido = monto lavado integrado en la economía formal. T_impedido = costo de investigaciones, distorsión de precios. ΔT_trayectoria = daño estructural persistente a la institucionalidad.

B_total Enriquecimiento ilícito del esquema

Lo que el arquitecto y los intermediarios obtuvieron del lavado. Base para la acción de extinción de dominio y para calcular el monto de recuperación de activos.

Nodo final (Nf) El erario / el sistema financiero

El daño del lavado no siempre tiene una víctima individual identificable. Su

El Método Prometeo: Imputación Causal para juristas y abogados

destinatario es el sistema financiero, el erario público (cuando hay evasión fiscal) o las instituciones corrompidas por el esquema.

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.3 Las tres fases del lavado y su traducción al grafo

El lavado de dinero opera en tres fases clásicas que se corresponden directamente con tres tipos de nodos en el grafo causal. Construir el grafo correctamente requiere identificar los nodos de cada fase — no solo los de la primera, que son los más visibles.

Fase Descripción Tipo de nodo dominante

Su rol en el grafo

1. Colocación El dinero ilícito entra al sistema financiero formal por primera vez. Efectivo convertido en transferencia s, depósitos fraccionados, negocios de efectivo.

Nodos de entrada

Mayor visibilidad documental. Menor R* relativo. Son los nodos que los controles convencionale s de PLD detectan con más facilidad. Su alta visibilidad es una señal de que no son el centro del esquema.

### 2. Estratificació n

El dinero se mueve a través de múltiples transacciones , jurisdiccione s y vehículos para hacer imposible

Nodos instrumentale s (vehículos)

Mayor densidad en el grafo. Su función es aumentar la S efectiva del arquitecto: hacen que el sistema parezca no

El Método Prometeo: Imputación Causal para juristas y abogados

rastrear su origen. Capas de empresas offshore, transferencia s entre jurisdiccione s, cambios de divisa.

depender de nadie específico. Cuantas más capas, mayor la opacidad del esquema.

Es donde el B_total del arquitecto se materializa. Es también el punto donde la extinción de dominio tiene mayor efectividad: los activos integrados son los que pueden embargarse y recuperarse.

### 3. Integración

El dinero ya "limpio" regresa a la economía formal como activo legítimo: propiedades, inversiones, empresas reales, fondos de inversión.

Nodos de salida / beneficio

⚠ El error más frecuente al construir el grafo de una operación de lavado es incluir solo los nodos de colocación (los más visibles) y omitir los nodos de estratificación y el arquitecto. Un grafo incompleto produce un R* que sobreestima la responsabilidad de los testaferros y los ejecutores visibles, y no detecta al arquitecto. El grafo debe construirse de afuera hacia adentro: desde los documentos visibles, trabajando hacia atrás hasta el nodo con R* alto y visibilidad baja.

### 5.3.1 El nodo inferido: cuando el arquitecto no aparece en ningún documento

El Método Prometeo: Imputación Causal para juristas y abogados

El principio más importante del análisis causal de una operación de lavado bien diseñada es este: si el grafo de todos los nodos documentados produce un R* que concentra la responsabilidad en testaferros y ejecutores con S alto, el grafo está incompleto. Hay un nodo no documentado que lo sostiene causalmente.

Nodo inferido:  Un nodo cuya existencia no está directamente documentada pero que es causalmente necesario para explicar los patrones observados. En PLD, el arquitecto suele ser un nodo inferido: su existencia se deduce del hecho de que la operación requería un nivel de coordinación y conocimiento que ninguno de los nodos visibles podía haber tenido individualmente. R*_oculto ≈ 1 − Σ (R*_visible × (1−S_visible)). Cuando R*_oculto > 0.40 en una operación de aparente legitimidad, hay un actor no identificado que sostiene causalmente la estructura.

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.4 Tipos de evidencia transaccional y sus rangos w

La tabla E0-E8 del Capítulo 2 aplica en PLD con adaptaciones específicas para el tipo de evidencia disponible en investigaciones financieras. El principio es el mismo: el rango del peso de una arista lo determina el tipo de evidencia que la sustenta. Lo que cambia es qué cuenta como E1, E2, E3 en el contexto de una operación de lavado.

Tipo Evidencia transaccional correspondiente

Rango w

Por qué ese rango en PLD

T-E1

Registro directo de instrucción: correo o comunicación donde el arquitecto instruye una transacción o la creación de una estructura específica. Contrato con cláusula que documenta el control real.

[0.75 –

0.95] La instrucción directa documentada es el eslabón más difícil de fabricar y el más difícil de negar. Raro en esquemas bien diseñados precisamente por eso.

T-E2

Análisis forense financiero: peritaje contable que sigue el dinero desde el origen documentado hasta el destino. Análisis de beneficiario final (UBO) con cadena documental completa.

[0.70 –

0.90] El peritaje financiero es casi tan sólido como el documento directo cuando la cadena documental es completa. Su validez depende de la integridad del perito.

T-E3

Testimonios convergentes de intermediarios con

[0.55 –

0.75] La convergencia de múltiples intermediarios

El Método Prometeo: Imputación Causal para juristas y abogados

documentación parcial: el abogado que afirma recibir instrucciones de N_x, corroborado por el contador que también afirma haber recibido instrucciones del mismo N_x.

apuntando al mismo nodo sin conocerse entre sí es evidencia sólida. Se debilita si los testigos se conocen o tienen incentivos alineados.

T-E4

Correlación estadística de patrones: todas las entidades del esquema se activan y desactivan simultáneamente, todas reciben instrucciones en el mismo idioma, todas usan el mismo modelo de contrato.

[0.50 –

0.70] El patrón estadístico de coordinación sin evidencia de instrucción directa establece la existencia del nodo controlador pero no lo identifica por nombre.

T-E5

Testimonio único de intermediario con documentación parcial: un solo abogado, contador o testaferro que afirma recibir instrucciones de N_x, con algún documento consistente.

[0.35 –

0.55] El testimonio único es vulnerable a retractación e impugnación. El corroborante documental parcial lo eleva del rango T-E8.

T-E6

Inferencia por posición de beneficio: los activos integrados en la fase final van documentalmente a una persona o entidad que tiene la posición económica de beneficiario real, sin documento de instrucción.

[0.25 –

0.45] Quien se beneficia de un esquema sin que nadie más lo haya instruido es el candidato natural al arquitecto. La inferencia por beneficio final es razonada pero necesita corroboración.

T-E7

Correlación temporal sin mecanismo: las cuentas del presunto arquitecto

[0.10 –

0.30] La correlación de timing sin mecanismo es la

El Método Prometeo: Imputación Causal para juristas y abogados

reciben fondos consistentemente después de cada fase de integración, sin que haya documento del mecanismo de transmisión.

evidencia más débil que produce arista con peso positivo. Útil para orientar la investigación, insuficiente por sí sola.

T-E8

Dicho único de testigo sin ningún respaldo documental, estadístico ni técnico.

[0.05 –

0.20] Evidencia mínima. Solo se usa cuando no hay nada más y el contexto lo hace plausible.

w = 0.00 No es ausencia de evidencia: es evidencia de la ausencia. En PLD: puede ser el análisis de los que muestra que el nodo nunca tuvo acceso a las cuentas en cuestión.

T-E0

Arista nula documentada: prueba pericial de que el nodo no tenía acceso a los fondos ni a las instrucciones, o que el mecanismo de conexión es técnicamente imposible.

Sobre la evidencia de beneficiario final (T-E6):  En la mayoría de las jurisdicciones, los reportes de beneficiario último o real (UBO — Ultimate Beneficial Owner) tienen fuerza equivalente a T-E2 cuando están completamente documentados con la cadena de control. Sin embargo, en esquemas con múltiples capas de entidades, el UBO documentado en los registros puede ser un testaferro adicional. La arista entre el UBO nominal y el beneficiario real efectivo suele ser T-E4 a T-E6 hasta que la investigación corrobore el control real.

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.5 S: la fungibilidad del rol en el esquema

En el PLD, S tiene una importancia estratégica que va más allá del análisis individual de cada nodo. El arquitecto de un esquema bien diseñado maximiza deliberadamente la S de todos los nodos visibles: si cualquier testaferro habría firmado, si cualquier abogado habría creado la empresa, si cualquier banco habría procesado la transferencia, entonces el esquema parece no depender de nadie en particular. Esa apariencia es el objetivo del diseño.

El análisis de S rompe esa apariencia desde el otro lado: si todos los nodos visibles tienen S alto, la necesidad causal migra estructuralmente al nodo de diseño. No es que nadie sea responsable — es que la responsabilidad está completamente concentrada en quien diseñó un sistema donde todos los ejecutores son fungibles.

Nodo típico en PLD

S estimad o

Razonamient o

Consecuencia para el análisis

Testaferro / prestanombr e

### 0.85 – 0.95 Cualquier otra persona dispuesta habría firmado los mismos documentos. El esquema no depende de esta persona específica.

R* bajo y S alto → R*_neta mínima. Argumento para reducción de cargos o acuerdo de cooperación como testigo.

Abogado / estructurador

### 0.60 – 0.80 Cualquier abogado en jurisdicción permisiva

S depende del grado de conocimiento acreditado. Si es

El Método Prometeo: Imputación Causal para juristas y abogados

habría hecho lo mismo — salvo que tuviera conocimiento específico del esquema y lo eligiera activamente.

el mismo abogado en múltiples esquemas del mismo arquitecto, S baja significativamente .

Banco que procesa transferencia s

0.55 – 0.75 El dinero podría haber pasado por otro banco con controles menos rigurosos. Pero si el arquitecto eligió ese banco específico por una característica, S baja.

El Δ del banco mide su déficit de compliance proporcional a su participación causal.

Jurisdicción opaca

0.40 – 0.65 Hay múltiples jurisdicciones opacas, pero no todas ofrecen el mismo nivel de protección. Si el esquema requería las características específicas de esa jurisdicción, S baja.

El R* de la jurisdicción informa el análisis geopolítico del PLD. No produce imputación individual pero sí argumento para sanciones sistémicas.

APNFD (ver §6.9)

### 0.30 – 0.60 Depende fuertemente del tipo de servicio y del perfil del

La distinción APNFD vs. institución financiera es relevante para el

El Método Prometeo: Imputación Causal para juristas y abogados

cliente. Un APNFD que trabaja con ese tipo de cliente de manera especializada tiene S menor.

nivel de obligación de reporte y el estándar de due diligence esperado.

Arquitecto del esquema

0.10 – 0.25 Sin el arquitecto, el esquema no habría existido en esa forma específica. Su conocimiento de las jurisdicciones, sus conexiones y su diseño eran idiosincráticos.

S bajo → R*_neta alta. Es el nodo que el análisis debe identificar aunque no aparezca en documentos.

### §5.6 α como cumplimiento de la obligación de reporte

En el PLD, α tiene una definición operativa más precisa que en el derecho general. No mide si el actor "reconoció y reparó" en el sentido de los casos civiles: mide si el nodo cumplió su obligación regulatoria de reporte cuando tuvo la oportunidad de hacerlo. Esa obligación varía según la posición del nodo: una institución financiera tiene obligaciones de PLD que un testaferro no tiene, y un oficial de compliance las tiene de manera diferente a un testaferro.

Nivel de cumplimiento

Rango α

Conducta observable

Consecuencia regulatoria

El Método Prometeo: Imputación Causal para juristas y abogados

### 0.00 El nodo no solo no reportó: activamente ayudó a estructurar la operación para evitar los controles. Falló el deber de reporte y cometió conducta ilícita autónoma.

Facilitación activa

Responsabilidad penal autónoma. Sin atenuante regulatorio.

Omisión deliberada

0.02 – 0.08 El nodo identificó señales de alerta y eligió no reportar. No hay evidencia de facilitación activa pero sí de omisión consciente. Hijo dominante: Potós o Anteros.

Sanción regulatoria severa. Potencial responsabilidad penal por omisión. Compatible con inicio de investigación al nodo.

Due diligence insuficiente

### 0.08 – 0.25 El nodo aplicó procedimientos de due diligence, pero de manera superficial o insuficiente. No se puede demostrar omisión deliberada.

Sanción regulatoria proporcional al riesgo. Programa de remediación. Multa calculable como Δ × D_total × R*.

Procedimiento correcto sin resultado

### 0.40 – 0.65 El nodo siguió sus procedimientos correctamente pero el esquema los evadió. La operación era suficientemente

Sin responsabilidad penal. Análisis regulatorio de si los procedimientos eran suficientes

El Método Prometeo: Imputación Causal para juristas y abogados

sofisticada para superar los controles vigentes.

para el perfil de riesgo.

Reporte oportuno

### 0.70 – 0.88 El nodo reportó la operación inusual a la autoridad competente (UIF / FIU) en tiempo y forma. Cooperó con la investigación posterior.

Sin sanción regulatoria sobre esta operación. Posible reconocimiento positivo en evaluaciones de efectividad.

Rechazo y reporte completo

### 0.90 – 1.00 El nodo rechazó la operación, reportó a la UIF/FIU, terminó la relación con el cliente y cooperó activamente con la investigación. Harmonía dominante.

Harmonía documentada. Sin responsabilidad. Potencial reconocimiento como nodo de alerta en la cadena de investigación.

Sobre los hijos en PLD:  Los hijos de Afrodita aplican en PLD solo para los nodos humanos: el arquitecto, los intermediarios profesionales (abogados, contadores), los funcionarios bancarios y los testaferros. No aplican a los nodos instrumentales (empresas, cuentas, fideicomisos). La distinción más importante: quien actúa desde Eros+Anteros (codicia deliberada, participación voluntaria) versus quien actúa desde Fobos o Deimos (miedo a represalias, ignorancia genuina). Esa distinción afecta directamente la culpabilidad penal, aunque no modifica R* ni Δ.

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.7 Los valores de Shapley: repartir la responsabilidad cuando nadie era indispensable por sí solo

### 5.7.1 El problema en lenguaje llano

El método de las rondas que usamos en los capítulos anteriores funciona bien cuando hay al menos un actor sin el cual el daño no habría ocurrido. En la mayoría de los casos de lavado, ese actor es el arquitecto del esquema: sin él no hay operación.

Pero hay casos donde esa condición no se cumple para ningún intermediario individual. Imagina tres actores — el arquitecto, un intermediario y un banco — donde el dinero podría haber llegado a su destino, aunque el intermediario hubiera sido diferente, o, aunque el banco hubiera sido otro. En ese escenario, el método de las rondas asigna responsabilidad cero a cada intermediario individualmente. Matemáticamente correcto. Jurídicamente absurdo: los tres participaron, los tres facilitaron, los tres deben responder en alguna proporción.

Analogía: Tres cargadores que mueven un coche Tres personas empujan un coche averiado hasta el taller. Individualmente, ninguno de los tres puede moverlo solo. Pero juntos llegan. ¿Cómo se distribuye el esfuerzo? No podemos decir que cada uno aportó cero porque individualmente no alcanzó. La pregunta justa es: ¿cuánto aportó cada uno, en promedio, considerando todos los órdenes posibles en que pudieron haber empujado? Esa es exactamente la pregunta que Shapley responde.

El valor de Shapley:  El aporte promedio de cada actor al daño total, calculado considerando todos los órdenes posibles en que pudieron haberse incorporado al esquema.

El Método Prometeo: Imputación Causal para juristas y abogados

La suma de todos los valores de Shapley siempre iguala el daño total. Ningún actor queda en cero si contribuyó en alguna combinación.

### 5.7.2 Cómo se determinan los montos de cada combinación

Antes del cálculo hay una pregunta que el análisis debe responder: ¿cuánto dinero habría podido lavar cada combinación posible de actores si solo ellos hubieran participado? Esos montos no caen del cielo — se determinan con la misma lógica de pesos w del Capítulo 2, aplicada a cada combinación:

Qué acredita Ejemplo en este caso

Tipo de evidencia

E1 transaccional

Documentos que muestran que esa combinación de actores operó o podía operar de forma independiente.

Contratos de transferencia directa entre el arquitecto e intermediarios que no usaron al banco en operaciones previas.

E2 pericial Peritaje financiero que demuestra la viabilidad técnica de la ruta alternativa.

Análisis pericial que confirma que las transferencias internacionales directas habrían alcanzado el 60% del monto sin necesitar al banco.

E4 estadística

Patrones históricos en operaciones similares del mismo esquema o del mismo arquitecto.

En operaciones anteriores del mismo arquitecto con otros intermediarios, el monto promedio sin

El Método Prometeo: Imputación Causal para juristas y abogados

banco era el 60-65% del total.

E6 inferencial

Inferencia razonada por la estructura del esquema: si el banco aportaba principalmente en la fase de integración, su ausencia reduce el monto integrable.

El banco era el nodo de integración de activos inmobiliarios. Sin banco, el esquema podía estratificar pero no integrar la totalidad.

Los montos del ejemplo son ilustrativos:  En el caso que sigue, la evidencia mostró que el arquitecto y el intermediario podían lavar el 60% del total sin el banco (usaban transferencias directas a jurisdicciones sin banca de corresponsalía). El arquitecto y el banco, sin intermediario, alcanzaban el 40% porque sin el intermediario la estructura de estratificación era más expuesta. Esos porcentajes vienen de la evidencia — no de una regla matemática. En un caso real, se determinan aplicando la tabla de tipos de evidencia de §6.4 a cada combinación.

### 5.7.3 El cálculo: el método de las órdenes

Con tres actores — Arquitecto (A), Intermediario (I) y Banco (B) — hay exactamente 6 órdenes posibles en que pudieron haberse incorporado al esquema. Para cada orden calculamos cuánto aportó cada actor cuando entró. Luego promediamos.

### Los datos del caso:

### • Daño total documentado: $1,000,000 • A + I solos: podían lavar $600,000 (60% — evidencia E2) • A + B solos: podían lavar $400,000 (40% — evidencia E4)

El Método Prometeo: Imputación Causal para juristas y abogados

• I + B sin A: podían lavar $0 (sin el diseño del arquitecto no hay operación) • Cualquier actor solo: $0

### Paso 1 — Los 6 órdenes posibles y el aporte de cada actor:

Orden 1:  A → I → B

A entra primero:     daño pasa de $0       a $0         → A aporta $0 I entra tras A:      daño pasa de $0       a $600,000   → I aporta $600,000 B entra al final:    daño pasa de $600,000 a $1,000,000 → B aporta $400,000

Orden 2:  A → B → I

A entra primero:     daño pasa de $0       a $0         → A aporta $0 B entra tras A:      daño pasa de $0       a $400,000   → B aporta $400,000 I entra al final:    daño pasa de $400,000 a $1,000,000 → I aporta $600,000

Orden 3:  I → A → B

I entra primero:     daño pasa de $0       a $0         → I aporta $0 A entra tras I:      daño pasa de $0       a $600,000   → A aporta $600,000 B entra al final:    daño pasa de $600,000 a $1,000,000 → B aporta $400,000

El Método Prometeo: Imputación Causal para juristas y abogados

Orden 4:  I → B → A

I entra primero:     daño pasa de $0       a $0         → I aporta $0 B entra tras I:      daño pasa de $0       a $0         → B aporta $0 (I + B sin A = $0: sin el arquitecto no hay esquema) A entra al final:    daño pasa de $0       a $1,000,000 → A aporta $1,000,000

Orden 5:  B → A → I

B entra primero:     daño pasa de $0       a $0         → B aporta $0 A entra tras B:      daño pasa de $0       a $400,000   → A aporta $400,000 I entra al final:    daño pasa de $400,000 a $1,000,000 → I aporta $600,000

Orden 6:  B → I → A

B entra primero:     daño pasa de $0       a $0         → B aporta $0 I entra tras B:      daño pasa de $0       a $0         → I aporta $0 (B + I sin A = $0: sin el arquitecto no hay esquema) A entra al final:    daño pasa de $0       a $1,000,000 → A aporta $1,000,000

### Paso 2 — Sumar los aportes y dividir entre 6:

Actor O rd . 1

÷ 6 %

O rd . 2

O rd . 3

Or d. 4

O rd . 5

Or d. 6

Su ma

El Método Prometeo: Imputación Causal para juristas y abogados

0 0 60 0 K

A Arquit ecto

1,0 00 K

40 0 K

1,0 00 K

3,0 00 K

$500, 000 50 %

0 0 60 0 K

0 1,8 00 K

I Interm ediario

60 0 K

60 0 K

$300, 000 30 %

0 0 0 1,2 00 K

B Banco

40 0 K

40 0 K

40 0 K

$200, 000 20 %

$1,00 0,000 10 0 % ✓

Verific ación 6,0 00 K

Lo que el método de las órdenes demuestra:  El arquitecto responde por el 50%: en cuatro de los seis órdenes, cuando A entra al esquema agrega una cantidad significativa. El intermediario responde por el 30%: en los tres órdenes donde I entra con A presente, agrega $600,000. El banco responde por el 20%: en los tres órdenes donde B entra con A presente, agrega $400,000. Nadie queda en cero, aunque ninguno era individualmente indispensable.

Con más de tres actores:  Con 4 actores hay 24 órdenes. Con 5 actores, 120. Con 6 actores, 720. Un abogado no hace eso a mano. Pero la lógica es idéntica: se listan todos los órdenes, se anota el aporte de cada actor cuando entra, se suman y se dividen entre el número de órdenes. El Apéndice incluye una plantilla de hoja de cálculo que automatiza el cálculo para hasta 6 actores.

### 5.7.4 La fórmula para el lector técnico

Para el lector que quiere la derivación formal:  El método de las órdenes es matemáticamente equivalente a la fórmula de Shapley. ¡Los pesos de la fórmula [|S|! (n−|S|−1)! /n!] son exactamente las

El Método Prometeo: Imputación Causal para juristas y abogados

probabilidades de que un actor se incorpore a una coalición de tamaño |S| cuando el orden de llegada es aleatorio y equiprobable. Con 3 actores: coalición vacía → peso 1/3, coalición de tamaño 1 → peso 1/6, coalición de tamaño 2 → peso 1/3. Esos son los mismos pesos que el promedio de los 6 órdenes produce automáticamente.

### φᵢ = Σ [ |S|! (n−|S|−1)! / n!]  × [ v(S∪{i}) − v(S)]

Símbolo Traducción al lenguaje del método de las órdenes

S Una combinación de actores sin incluir a i. Es el grupo que ya estaba en el esquema antes de que i entrara.

v(S∪{i}) − v(S) "Cuánto aporta i cuando entra" — exactamente el número que calculamos en cada orden.

|S|!(n−|S|−1)!/n! El peso de esa combinación. Con 3 actores equivale a 1/6 para combinaciones de tamaño 1, y 1/3 para vacía o completa. El promedio de los 6 órdenes produce automáticamente esos mismos pesos.

### 5.7.5 Cuándo usar Shapley y cuándo usar el método de las rondas

Situación Método adecuado

Criterio de decisión

Hay un actor sin el cual el esquema no habría existido

Método de las rondas

El arquitecto o el nodo central es condición necesaria. Usar R* del Capítulo 2. Es el caso más frecuente en

El Método Prometeo: Imputación Causal para juristas y abogados

esquemas con un solo diseñador.

Múltiples intermediarios donde cada uno podría haber sido reemplazado por otro

Valores de Shapley (método de las órdenes)

Ningún intermediario es individualmente indispensable. El dinero podría haber viajado por rutas alternativas. Usar el método de órdenes.

El arquitecto tiene R* alto por el método de rondas. Para distribuir la responsabilidad entre los intermediarios sustituibles, aplicar Shapley solo a ese subconjunto.

Arquitecto indispensable + intermediarios fungibles entre sí

Rondas para el arquitecto + órdenes para los intermediarios

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.8 La distinción entre el APNFD y el beneficiario final

Dos categorías de nodos requieren un tratamiento específico en el análisis de PLD porque su posición causal es frecuentemente malentendida: las Actividades y Profesiones No Financieras Designadas (APNFD) y el beneficiario final real (UBO — Ultimate Beneficial Owner).

### 5.8.1 El APNFD: el nodo que habilita sin ver el todo

APNFD (Actividades y Profesiones No Financieras Designadas):  El conjunto de profesionales y empresas que sin ser instituciones financieras tienen obligaciones de PLD porque sus servicios son frecuentemente utilizados en esquemas de lavado: abogados, contadores, notarios, agentes inmobiliarios, casinos, servicios de constitución de empresas. Su posición causal en el grafo es típicamente de habilitación estructural: no mueven el dinero directamente, pero proveen los instrumentos jurídicos o las transacciones que lo ocultan.

El análisis de R* para un APNFD depende de una distinción que el grafo hace explícita: ¿el APNFD diseñó la estructura del esquema, o simplemente proveyó un servicio estándar que el arquitecto usó? Un abogado que activamente diseñó la estructura offshore específica para ese cliente tiene R* alto y S bajo. Un notario que protocolizó documentos sin conocimiento del esquema tiene R* bajo y S alto.

Criterio de distinción

Tipo de APNFD

R* típico

S típico

El Método Prometeo: Imputación Causal para juristas y abogados

Estructurador activo

15 – 35% 0.20 – 0.40 Diseñó la estructura específica para ese cliente. Eligió las jurisdicciones y los vehículos. Tiene conocimiento documentado del perfil de riesgo del cliente. Hijo dominante: Eros+Potós.

Profesional con conocimiento parcial

8 – 20% 0.45 – 0.65 Proveyó un servicio estándar con señales de alerta que no reportó. No diseñó el esquema. Tenía indicios, pero no el cuadro completo. Hijo dominante: Potós o Fobos.

3 – 10% 0.70 – 0.90 Proveyó el servicio dentro de sus procedimientos estándar. El esquema estaba diseñado para parecer legítimo. No tenía indicios razonables. Hijo dominante: Deimos.

Proveedor de buena fe

### 5.8.2 El beneficiario final real: el nodo que el grafo debe encontrar

El beneficiario final real (UBO) es la persona física que en última instancia controla la entidad o que se beneficia de la operación, aunque no aparezca en ningún documento como tal. Es el nodo que el grafo debe identificar, aunque no esté documentado directamente. Es el candidato natural al mayor R* del esquema.

La distinción entre el UBO nominal (quien aparece en los registros como accionista o director final) y el UBO real (quien efectivamente controla y se beneficia) es el problema central del análisis de beneficiario en PLD. Los esquemas

El Método Prometeo: Imputación Causal para juristas y abogados

### bien diseñados tienen capas adicionales entre el UBO nominal y el UBO real.

Cómo identificarlo

Tipo de beneficiario

Posición en el grafo

UBO nominal (registrado)

Nodo de ejecución visible

Aparece en los documentos de las entidades. Alta probabilidad de ser testaferro si: (a) es director de múltiples empresas sin relación aparente, (b) es nacional de la jurisdicción donde se registra la empresa pero no tiene actividad económica en esa jurisdicción, (c) tiene antecedentes de ser prestanombre.

UBO real (efectivo)

Nodo de diseño / arquitecto

Se identifica mediante: (a) análisis del destinatario final de los activos integrados, (b) correlación entre los patrones de activación del esquema y los movimientos del presunto UBO real, (c) comunicaciones entre intermediarios que lo mencionan sin nombrarlo, (d) coincidencia geográfica y temporal entre la operación y los activos del presunto UBO.

Se infiere cuando: ninguno de los nodos visibles tiene el perfil económico para ser el beneficiario real, el esquema tiene un nivel de sofisticación que requiere conocimiento especializado que ningún nodo visible tiene, o los activos integrados no van a ningún nodo identificado. R*_oculto > 0.40 es la señal.

UBO oculto (no registrado en ningún documento)

Nodo inferido

El Método Prometeo: Imputación Causal para juristas y abogados

El caso trabajado de este capítulo:  La operación completa de lavado — con el funcionario público, las sociedades offshore y el análisis de extinción de dominio — se desarrolla en el Capítulo 7. Las herramientas de este capítulo (el grafo, los tipos de evidencia T-E0 a T-E1, S, α, Shapley) se aplican allí sobre ese caso con el protocolo completo.

El Método Prometeo: Imputación Causal para juristas y abogados

### §5.9 Lo que el análisis PLD aporta que el análisis convencional no puede

El análisis convencional de PLD está construido sobre la búsqueda de transacciones inusuales y la trazabilidad del dinero. Esas herramientas son necesarias pero insuficientes cuando el esquema fue diseñado para que la trazabilidad se detenga en un intermediario. El Método Prometeo añade tres instrumentos que ese análisis no tiene:

Instrumento Qué aporta que el análisis convencional no puede producir

R* como necesidad causal

Identifica al arquitecto, aunque no aparezca en los documentos. La concentración de R* en el nodo con visibilidad baja es la firma matemática del lavado bien diseñado. Esa concentración orienta la investigación hacia dónde buscar la evidencia corroborante.

El nodo inferido con R*_oculto

Cuando todos los nodos visibles tienen S alto, el cálculo produce R*_oculto alto automáticamente. Ese número es la señal de que existe un actor no identificado. No es evidencia de condena — es evidencia de que la investigación está incompleta.

Shapley para cadenas redundantes

Cuando el dinero podría haber viajado por rutas alternativas, el método de las rondas falla. Shapley distribuye la responsabilidad correctamente incluso cuando ningún actor individual es condición necesaria — que es exactamente el diseño de los esquemas de lavado más sofisticados.

Δ de compliance como base de

El Δ = R* − α de cada institución financiera o APNFD mide su déficit de compliance proporcional a su participación causal. Una

El Método Prometeo: Imputación Causal para juristas y abogados

sanción regulatoria proporcional al Δ de la institución — no al monto de la transacción — es más justa y más eficiente como disuasor.

sanción proporcional

### Lo que este capítulo estableció

✓ En PLD, la inversión causal es un objetivo del diseño, no un efecto colateral. El arquitecto tiene R* ≈ 55-70% y α = 0. El testaferro tiene R* ≈ 4-8% y α = 100% forzado.

✓ Las herramientas del método se renombran en PLD: R* = necesidad causal, α = cumplimiento de la obligación de reporte, Δ = déficit de compliance, D_total = daño al sistema financiero.

✓ La tabla de evidencia transaccional (T-E0 a T-E1) adapta los tipos de evidencia al contexto de investigaciones financieras: registros de instrucción, análisis forense bancario, correlación de patrones.

✓ El nodo inferido es el nodo cuya existencia no está documentada, pero es causalmente necesario. R*_oculto > 0.40 en una operación de aparente legitimidad es la señal de que hay un actor no identificado.

✓ Los valores de Shapley distribuyen correctamente la responsabilidad en cadenas con múltiples eslabones redundantes, donde el método de las rondas convencional asigna cero a todos.

✓ La distinción APNFD: el estructurador activo tiene R* alto y S bajo (diseñó el instrumento). El proveedor de buena fe tiene R* bajo y S alto (ejecutó sin conocimiento). El DA del caso trabajado tuvo el mayor R* del esquema.

✓ B_total × R*_B es la base técnica para la extinción de dominio proporcional, independientemente de a nombre de quién estén

El Método Prometeo: Imputación Causal para juristas y abogados

registrados los activos. El Capítulo 7 aplica este cálculo sobre el caso completo.

El Método Prometeo: Imputación Causal para juristas y abogados

EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL

