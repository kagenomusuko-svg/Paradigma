### Capítulo 5
PLD y delitos
financieros complejos
El beneficiario invisible: imputar al arquitecto de un esquema que
nunca tocó el dinero
Este capítulo aplica el Método Prometeo al dominio que
plantea el problema de imputación más difícil: la prevención
de lavado de dinero y los delitos financieros complejos. La
razón de la dificultad no es la falta de documentos — en
muchos esquemas hay abundantes registros de
transacciones. La razón es que el actor de mayor peso causal
diseñó deliberadamente su propia invisibilidad. El
arquitecto del esquema no aparece en los documentos. El
testaferro que firma todo sí aparece.
Este capítulo tiene la misma estructura que el Capítulo 2:
primero explica las herramientas adaptadas al dominio del
PLD — cómo se renombran, qué significan aquí, qué tablas
se usan. Luego el Capítulo 7 (el de presentación ante el
tribunal) complementa con los documentos del expediente
en contexto de investigación financiera.
Hay un instrumento nuevo en este capítulo que no apareció
en los anteriores: el valor de Shapley. Se introduce porque
hay casos de lavado con múltiples eslabones donde ningún
nodo individual es condición necesaria del resultado — el
dinero podría haber viajado por otra ruta — y el método de

El Método Prometeo: Imputación Causal para juristas y abogados
las rondas convencional asigna cero a todos. Shapley
resuelve ese límite con precisión.
⚠ Una aclaración sobre el alcance: este capítulo enseña a
construir el análisis causal de una operación de lavado para
fines de investigación, litigio de recuperación de activos,
extinción de dominio, y argumentación en procedimientos
regulatorios. No es un manual de tipificación penal ni sustituye
el análisis del cuerpo del delito. El Método Prometeo aporta
evidencia estructurada sobre la necesidad causal — la decisión
sobre los elementos del tipo corresponde al fiscal y al juez.
§5.1 Por qué el PLD es el
problema de imputación más
difícil
En el fraude bancario del Capítulo 3, la inversión causal era
un efecto colateral: el banco diseñó un sistema dañino y los
ejecutores visibles cargaron con las consecuencias. En el
lavado de dinero, la inversión causal es el objetivo del
diseño. El esquema se construye precisamente para que el
beneficiario real no aparezca en ningún documento y para
que la cadena de intermediarios sea suficientemente larga
como para que cualquier investigación se detenga en algún
nodo intermedio.
El sistema convencional de PLD trabaja con señales de
alerta: transacciones inusuales, montos sobre umbral,
patrones de fragmentación. Esas señales son eficaces para
detectar al ejecutor — el que mueve el dinero, el que abre
las cuentas, el que firma los contratos. Raramente alcanzan
al arquitecto del esquema, porque el arquitecto no mueve
dinero: diseña el sistema que lo mueve. Su nombre puede

El Método Prometeo: Imputación Causal para juristas y abogados
no aparecer en ningún documento, o puede aparecer al final
de una cadena tan larga de intermediarios que la conexión
causal parece imposible de demostrar.
Analogía: La luz de una estrella muerta El astrónomo que
observa una estrella desde la Tierra ve la luz que salió hace miles de años.
La estrella puede ya no existir. El investigador de PLD que analiza una
transacción ve el movimiento de dinero tal como llegó a su jurisdicción, no
el origen que lo produjo meses o años atrás y en otra latitud. El grafo
causal es el instrumento que permite reconstruir la fuente a partir de la luz
que llegó.
La inversión causal en PLD: Patrón estructural donde el
actor de mayor peso causal (el arquitecto del esquema) tiene
visibilidad documental nula, mientras el actor de menor
peso causal (el testaferro) tiene visibilidad documental total
porque firma todo. El arquitecto tiene R* ≈ 55-70% y α =

### 0. El testaferro tiene R* ≈ 4-8% y α = 100% forzado porque
firmó los documentos y es el único identificable sin
investigación. Δ del arquitecto = +55-70% (inversión
máxima). Δ del testaferro = −70 a −90% (chivo expiatorio
estructural).
Esa inversión no es accidental. El arquitecto la diseñó. Y
hay una consecuencia matemática que el método hace
visible: cuanto más sofisticado es el esquema de lavado,
mayor es la concentración de R* en el nodo invisible. El
arquitecto, al aumentar la sustituibilidad (S) de todos los
nodos visibles para hacerlos fungibles, automáticamente
concentra la necesidad causal en él mismo. La firma
matemática del lavado bien diseñado es precisamente el R*
alto del nodo que no aparece en los documentos.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.2 La tabla de traducción:
las herramientas del método
en el lenguaje del PLD
Las herramientas del Capítulo 2 tienen exactamente los
mismos fundamentos en este dominio. Lo que cambia es
cómo se nombran y qué miden concretamente. Esta tabla
permite al oficial de compliance, al fiscal de delitos
financieros y al abogado de extinción de dominio moverse
entre el lenguaje del método y el lenguaje de su campo sin
tener que resolver ninguna ecuación adicional.
Herramienta En PLD se llama Qué significa en la
del método práctica del
compliance y la
investigación
Grafo causal G Mapa de la La red completa de
operación personas, entidades,
cuentas y jurisdicciones
que participaron en el
esquema, con sus
relaciones causales. Se
construye de afuera
hacia adentro: se
empieza por los nodos
visibles en documentos
y se trabaja hacia atrás
hasta el arquitecto.
Nodo de diseño Arquitecto del Quien eligió las
esquema jurisdicciones, definió
los vehículos jurídicos,
estableció los flujos y
coordinó a los
intermediarios.
Raramente firma nada.
Tiene el R* más alto y

El Método Prometeo: Imputación Causal para juristas y abogados
la visibilidad
documental más baja.
Nodo Vehículo La empresa fantasma, la
instrumental financiero cuenta bancaria, el
fideicomiso opaco. No
tiene voluntad propia.
No se le calcula α, pero
sí R* (necesidad causal
de la operación). Su R*
alto apunta hacia quien
lo controló.
Nodo de Testaferro / Persona física que
ejecución con S prestanombre aparece como director
alto o accionista sin tener
control real. Alta
visibilidad documental.
S muy alto (cualquier
otra persona dispuesta
habría firmado lo
mismo). R* muy bajo.
R* (vector) Necesidad causal R*_i mide cuánto
de la operación dependía el éxito del
esquema de que el
nodo i existiera y
actuara como lo hizo.
Alto R* con visibilidad
documental baja =
señal del beneficiario
real probable.
S Fungibilidad del S alto = el nodo era un
(sustituibilidad) rol recurso genérico:
cualquier otro
prestanombre, abogado
o entidad habría
cumplido la misma
función. El esquema no
dependía de esa
persona específica. S
bajo = el nodo era
idiosincrático.

El Método Prometeo: Imputación Causal para juristas y abogados
α (asunción) Cumplimiento de α mide si el nodo
la obligación de reportó la operación
reporte inusual, rechazó al
cliente, aplicó due
diligence reforzada, o
en cambio facilitó
activa o pasivamente la
operación. α = 0: no
reportó. α = 1: reportó
y cooperó.
Δ = R* − α Déficit de Δ alto positivo = el
compliance nodo fue causalmente
necesario para el
esquema y no cumplió
su obligación de
reporte. Es la medida
del incumplimiento
regulatorio
proporcional a la
participación causal.
D_total Daño al sistema T_invertido = monto
financiero lavado integrado en la
economía formal.
T_impedido = costo de
investigaciones,
distorsión de precios.
ΔT_trayectoria = daño
estructural persistente a
la institucionalidad.
B_total Enriquecimiento Lo que el arquitecto y
ilícito del los intermediarios
esquema obtuvieron del lavado.
Base para la acción de
extinción de dominio y
para calcular el monto
de recuperación de
activos.
Nodo final (Nf) El erario / el El daño del lavado no
sistema siempre tiene una
financiero víctima individual
identificable. Su

El Método Prometeo: Imputación Causal para juristas y abogados
destinatario es el
sistema financiero, el
erario público (cuando
hay evasión fiscal) o las
instituciones
corrompidas por el
esquema.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.3 Las tres fases del lavado y
su traducción al grafo
El lavado de dinero opera en tres fases clásicas que se
corresponden directamente con tres tipos de nodos en el
grafo causal. Construir el grafo correctamente requiere
identificar los nodos de cada fase — no solo los de la
primera, que son los más visibles.
Fase Descripción Tipo de nodo Su rol en el
dominante grafo

### 1. Colocación El dinero Nodos de Mayor
ilícito entra entrada visibilidad
al sistema documental.
financiero Menor R*
formal por relativo. Son
primera vez. los nodos que
Efectivo los controles
convertido convencionale
en s de PLD
transferencia detectan con
s, depósitos más facilidad.
fraccionados, Su alta
negocios de visibilidad es
efectivo. una señal de
que no son el
centro del
esquema.

### 2. El dinero se Nodos Mayor
Estratificació mueve a instrumentale densidad en el
n través de s (vehículos) grafo. Su
múltiples función es
transacciones aumentar la S
, efectiva del
jurisdiccione arquitecto:
s y vehículos hacen que el
para hacer sistema
imposible parezca no

El Método Prometeo: Imputación Causal para juristas y abogados
rastrear su depender de
origen. nadie
Capas de específico.
empresas Cuantas más
offshore, capas, mayor
transferencia la opacidad
s entre del esquema.
jurisdiccione
s, cambios de
divisa.

### 3. El dinero ya Nodos de Es donde el
Integración "limpio" salida / B_total del
regresa a la beneficio arquitecto se
economía materializa.
formal como Es también el
activo punto donde
legítimo: la extinción
propiedades, de dominio
inversiones, tiene mayor
empresas efectividad:
reales, los activos
fondos de integrados
inversión. son los que
pueden
embargarse y
recuperarse.
⚠ El error más frecuente al construir el grafo de una operación
de lavado es incluir solo los nodos de colocación (los más
visibles) y omitir los nodos de estratificación y el arquitecto.
Un grafo incompleto produce un R* que sobreestima la
responsabilidad de los testaferros y los ejecutores visibles, y no
detecta al arquitecto. El grafo debe construirse de afuera hacia
adentro: desde los documentos visibles, trabajando hacia atrás
hasta el nodo con R* alto y visibilidad baja.
5.3.1 El nodo inferido: cuando el arquitecto
no aparece en ningún documento

El Método Prometeo: Imputación Causal para juristas y abogados
El principio más importante del análisis causal de una
operación de lavado bien diseñada es este: si el grafo de
todos los nodos documentados produce un R* que
concentra la responsabilidad en testaferros y ejecutores con
S alto, el grafo está incompleto. Hay un nodo no
documentado que lo sostiene causalmente.
Nodo inferido: Un nodo cuya existencia no está
directamente documentada pero que es causalmente
necesario para explicar los patrones observados. En PLD,
el arquitecto suele ser un nodo inferido: su existencia se
deduce del hecho de que la operación requería un nivel de
coordinación y conocimiento que ninguno de los nodos
visibles podía haber tenido individualmente. R*_oculto ≈ 1
− Σ (R*_visible × (1−S_visible)). Cuando R*_oculto > 0.40
en una operación de aparente legitimidad, hay un actor no
identificado que sostiene causalmente la estructura.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.4 Tipos de evidencia
transaccional y sus rangos w
La tabla E0-E8 del Capítulo 2 aplica en PLD con
adaptaciones específicas para el tipo de evidencia disponible
en investigaciones financieras. El principio es el mismo: el
rango del peso de una arista lo determina el tipo de
evidencia que la sustenta. Lo que cambia es qué cuenta
como E1, E2, E3 en el contexto de una operación de
lavado.
Tipo Evidencia Rango Por qué ese rango
transaccional w en PLD
correspondiente
T- Registro directo de [0.75 – La instrucción
E1 instrucción: correo o 0.95] directa
comunicación donde el documentada es el
arquitecto instruye una eslabón más difícil
transacción o la creación de fabricar y el más
de una estructura difícil de negar.
específica. Contrato con Raro en esquemas
cláusula que documenta bien diseñados
el control real. precisamente por
eso.
T- Análisis forense [0.70 – El peritaje
E2 financiero: peritaje 0.90] financiero es casi
contable que sigue el tan sólido como el
dinero desde el origen documento directo
documentado hasta el cuando la cadena
destino. Análisis de documental es
beneficiario final (UBO) completa. Su validez
con cadena documental depende de la
completa. integridad del
perito.
T- Testimonios [0.55 – La convergencia de
E3 convergentes de 0.75] múltiples
intermediarios con intermediarios

El Método Prometeo: Imputación Causal para juristas y abogados
documentación parcial: apuntando al mismo
el abogado que afirma nodo sin conocerse
recibir instrucciones de entre sí es evidencia
N_x, corroborado por el sólida. Se debilita si
contador que también los testigos se
afirma haber recibido conocen o tienen
instrucciones del mismo incentivos
N_x. alineados.
T- Correlación estadística [0.50 – El patrón
E4 de patrones: todas las 0.70] estadístico de
entidades del esquema coordinación sin
se activan y desactivan evidencia de
simultáneamente, todas instrucción directa
reciben instrucciones en establece la
el mismo idioma, todas existencia del nodo
usan el mismo modelo controlador pero no
de contrato. lo identifica por
nombre.
T- Testimonio único de [0.35 – El testimonio único
E5 intermediario con 0.55] es vulnerable a
documentación parcial: retractación e
un solo abogado, impugnación. El
contador o testaferro corroborante
que afirma recibir documental parcial
instrucciones de N_x, lo eleva del rango T-
con algún documento E8.
consistente.
T- Inferencia por posición [0.25 – Quien se beneficia
E6 de beneficio: los activos 0.45] de un esquema sin
integrados en la fase que nadie más lo
final van haya instruido es el
documentalmente a una candidato natural al
persona o entidad que arquitecto. La
tiene la posición inferencia por
económica de beneficio final es
beneficiario real, sin razonada pero
documento de necesita
instrucción. corroboración.
T- Correlación temporal sin [0.10 – La correlación de
E7 mecanismo: las cuentas 0.30] timing sin
del presunto arquitecto mecanismo es la

El Método Prometeo: Imputación Causal para juristas y abogados
reciben fondos evidencia más débil
consistentemente que produce arista
después de cada fase de con peso positivo.
integración, sin que haya Útil para orientar la
documento del investigación,
mecanismo de insuficiente por sí
transmisión. sola.
T- Dicho único de testigo [0.05 – Evidencia mínima.
E8 sin ningún respaldo 0.20] Solo se usa cuando
documental, estadístico no hay nada más y
ni técnico. el contexto lo hace
plausible.
T- Arista nula w = No es ausencia de
E0 documentada: prueba 0.00 evidencia: es
pericial de que el nodo evidencia de la
no tenía acceso a los ausencia. En PLD:
fondos ni a las puede ser el análisis
instrucciones, o que el de los que muestra
mecanismo de conexión que el nodo nunca
es técnicamente tuvo acceso a las
imposible. cuentas en cuestión.
Sobre la evidencia de beneficiario final (T-E6): En la
mayoría de las jurisdicciones, los reportes de beneficiario último o real
(UBO — Ultimate Beneficial Owner) tienen fuerza equivalente a T-E2
cuando están completamente documentados con la cadena de control. Sin
embargo, en esquemas con múltiples capas de entidades, el UBO
documentado en los registros puede ser un testaferro adicional. La arista
entre el UBO nominal y el beneficiario real efectivo suele ser T-E4 a T-
E6 hasta que la investigación corrobore el control real.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.5 S: la fungibilidad del rol
en el esquema
En el PLD, S tiene una importancia estratégica que va más
allá del análisis individual de cada nodo. El arquitecto de un
esquema bien diseñado maximiza deliberadamente la S de
todos los nodos visibles: si cualquier testaferro habría
firmado, si cualquier abogado habría creado la empresa, si
cualquier banco habría procesado la transferencia, entonces
el esquema parece no depender de nadie en particular. Esa
apariencia es el objetivo del diseño.
El análisis de S rompe esa apariencia desde el otro lado: si
todos los nodos visibles tienen S alto, la necesidad causal
migra estructuralmente al nodo de diseño. No es que nadie
sea responsable — es que la responsabilidad está
completamente concentrada en quien diseñó un sistema
donde todos los ejecutores son fungibles.
Nodo típico S Razonamient Consecuencia
en PLD estimad o para el análisis
o
Testaferro / 0.85 – Cualquier otra R* bajo y S alto
prestanombr 0.95 persona → R*_neta
e dispuesta mínima.
habría firmado Argumento para
los mismos reducción de
documentos. cargos o acuerdo
El esquema no de cooperación
depende de como testigo.
esta persona
específica.
Abogado / 0.60 – Cualquier S depende del
estructurador 0.80 abogado en grado de
jurisdicción conocimiento
permisiva acreditado. Si es

El Método Prometeo: Imputación Causal para juristas y abogados
habría hecho lo el mismo
mismo — abogado en
salvo que múltiples
tuviera esquemas del
conocimiento mismo arquitecto,
específico del S baja
esquema y lo significativamente
eligiera .
activamente.
Banco que 0.55 – El dinero El Δ del banco
procesa 0.75 podría haber mide su déficit de
transferencia pasado por compliance
s otro banco con proporcional a su
controles participación
menos causal.
rigurosos. Pero
si el arquitecto
eligió ese
banco
específico por
una
característica, S
baja.
Jurisdicción 0.40 – Hay múltiples El R* de la
opaca 0.65 jurisdicciones jurisdicción
opacas, pero informa el análisis
no todas geopolítico del
ofrecen el PLD. No
mismo nivel de produce
protección. Si imputación
el esquema individual pero sí
requería las argumento para
características sanciones
específicas de sistémicas.
esa
jurisdicción, S
baja.
APNFD (ver 0.30 – Depende La distinción
§6.9) 0.60 fuertemente APNFD vs.
del tipo de institución
servicio y del financiera es
perfil del relevante para el

El Método Prometeo: Imputación Causal para juristas y abogados
cliente. Un nivel de
APNFD que obligación de
trabaja con ese reporte y el
tipo de cliente estándar de due
de manera diligence
especializada esperado.
tiene S menor.
Arquitecto 0.10 – Sin el S bajo →
del esquema 0.25 arquitecto, el R*_neta alta. Es
esquema no el nodo que el
habría existido análisis debe
en esa forma identificar
específica. Su aunque no
conocimiento aparezca en
de las documentos.
jurisdicciones,
sus conexiones
y su diseño
eran
idiosincráticos.
§5.6 α como cumplimiento de
la obligación de reporte
En el PLD, α tiene una definición operativa más precisa que
en el derecho general. No mide si el actor "reconoció y
reparó" en el sentido de los casos civiles: mide si el nodo
cumplió su obligación regulatoria de reporte cuando tuvo la
oportunidad de hacerlo. Esa obligación varía según la
posición del nodo: una institución financiera tiene
obligaciones de PLD que un testaferro no tiene, y un oficial
de compliance las tiene de manera diferente a un testaferro.
Nivel de Rango Conducta Consecuencia
cumplimiento α observable regulatoria

El Método Prometeo: Imputación Causal para juristas y abogados
Facilitación 0.00 El nodo no solo Responsabilidad
activa no reportó: penal autónoma.
activamente Sin atenuante
ayudó a regulatorio.
estructurar la
operación para
evitar los
controles. Falló
el deber de
reporte y
cometió
conducta ilícita
autónoma.
Omisión 0.02 – El nodo Sanción
deliberada 0.08 identificó señales regulatoria
de alerta y eligió severa. Potencial
no reportar. No responsabilidad
hay evidencia de penal por
facilitación omisión.
activa pero sí de Compatible con
omisión inicio de
consciente. Hijo investigación al
dominante: nodo.
Potós o Anteros.
Due diligence 0.08 – El nodo aplicó Sanción
insuficiente 0.25 procedimientos regulatoria
de due diligence, proporcional al
pero de manera riesgo. Programa
superficial o de remediación.
insuficiente. No Multa calculable
se puede como Δ ×
demostrar D_total × R*.
omisión
deliberada.
Procedimiento 0.40 – El nodo siguió Sin
correcto sin 0.65 sus responsabilidad
resultado procedimientos penal. Análisis
correctamente regulatorio de si
pero el esquema los
los evadió. La procedimientos
operación era eran suficientes
suficientemente

El Método Prometeo: Imputación Causal para juristas y abogados
sofisticada para para el perfil de
superar los riesgo.
controles
vigentes.
Reporte 0.70 – El nodo reportó Sin sanción
oportuno 0.88 la operación regulatoria sobre
inusual a la esta operación.
autoridad Posible
competente reconocimiento
(UIF / FIU) en positivo en
tiempo y forma. evaluaciones de
Cooperó con la efectividad.
investigación
posterior.
Rechazo y 0.90 – El nodo rechazó Harmonía
reporte 1.00 la operación, documentada.
completo reportó a la Sin
UIF/FIU, responsabilidad.
terminó la Potencial
relación con el reconocimiento
cliente y cooperó como nodo de
activamente con alerta en la
la investigación. cadena de
Harmonía investigación.
dominante.
Sobre los hijos en PLD: Los hijos de Afrodita aplican en PLD
solo para los nodos humanos: el arquitecto, los intermediarios profesionales
(abogados, contadores), los funcionarios bancarios y los testaferros. No
aplican a los nodos instrumentales (empresas, cuentas, fideicomisos). La
distinción más importante: quien actúa desde Eros+Anteros (codicia
deliberada, participación voluntaria) versus quien actúa desde Fobos o
Deimos (miedo a represalias, ignorancia genuina). Esa distinción afecta
directamente la culpabilidad penal, aunque no modifica R* ni Δ.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.7 Los valores de Shapley:
repartir la responsabilidad
cuando nadie era
indispensable por sí solo
5.7.1 El problema en lenguaje llano
El método de las rondas que usamos en los capítulos
anteriores funciona bien cuando hay al menos un actor sin
el cual el daño no habría ocurrido. En la mayoría de los
casos de lavado, ese actor es el arquitecto del esquema: sin
él no hay operación.
Pero hay casos donde esa condición no se cumple para
ningún intermediario individual. Imagina tres actores — el
arquitecto, un intermediario y un banco — donde el dinero
podría haber llegado a su destino, aunque el intermediario
hubiera sido diferente, o, aunque el banco hubiera sido otro.
En ese escenario, el método de las rondas asigna
responsabilidad cero a cada intermediario individualmente.
Matemáticamente correcto. Jurídicamente absurdo: los tres
participaron, los tres facilitaron, los tres deben responder en
alguna proporción.
Analogía: Tres cargadores que mueven un coche Tres
personas empujan un coche averiado hasta el taller. Individualmente,
ninguno de los tres puede moverlo solo. Pero juntos llegan. ¿Cómo se
distribuye el esfuerzo? No podemos decir que cada uno aportó cero porque
individualmente no alcanzó. La pregunta justa es: ¿cuánto aportó cada
uno, en promedio, considerando todos los órdenes posibles en que pudieron
haber empujado? Esa es exactamente la pregunta que Shapley responde.
El valor de Shapley: El aporte promedio de cada actor al
daño total, calculado considerando todos los órdenes
posibles en que pudieron haberse incorporado al esquema.

El Método Prometeo: Imputación Causal para juristas y abogados
La suma de todos los valores de Shapley siempre iguala el
daño total. Ningún actor queda en cero si contribuyó en
alguna combinación.
5.7.2 Cómo se determinan los montos de
cada combinación
Antes del cálculo hay una pregunta que el análisis debe
responder: ¿cuánto dinero habría podido lavar cada
combinación posible de actores si solo ellos hubieran
participado? Esos montos no caen del cielo — se
determinan con la misma lógica de pesos w del Capítulo 2,
aplicada a cada combinación:
Tipo de Qué acredita Ejemplo en este
evidencia caso
E1 Documentos que Contratos de
transaccional muestran que esa transferencia directa
combinación de actores entre el arquitecto e
operó o podía operar intermediarios que no
de forma usaron al banco en
independiente. operaciones previas.
E2 pericial Peritaje financiero que Análisis pericial que
demuestra la viabilidad confirma que las
técnica de la ruta transferencias
alternativa. internacionales
directas habrían
alcanzado el 60% del
monto sin necesitar al
banco.
E4 Patrones históricos en En operaciones
estadística operaciones similares anteriores del mismo
del mismo esquema o arquitecto con otros
del mismo arquitecto. intermediarios, el
monto promedio sin

El Método Prometeo: Imputación Causal para juristas y abogados
banco era el 60-65%
del total.
E6 Inferencia razonada El banco era el nodo
inferencial por la estructura del de integración de
esquema: si el banco activos inmobiliarios.
aportaba Sin banco, el esquema
principalmente en la podía estratificar pero
fase de integración, su no integrar la
ausencia reduce el totalidad.
monto integrable.
Los montos del ejemplo son ilustrativos: En el caso que sigue,
la evidencia mostró que el arquitecto y el intermediario podían lavar el
60% del total sin el banco (usaban transferencias directas a jurisdicciones
sin banca de corresponsalía). El arquitecto y el banco, sin intermediario,
alcanzaban el 40% porque sin el intermediario la estructura de
estratificación era más expuesta. Esos porcentajes vienen de la evidencia
— no de una regla matemática. En un caso real, se determinan aplicando
la tabla de tipos de evidencia de §6.4 a cada combinación.
5.7.3 El cálculo: el método de las órdenes
Con tres actores — Arquitecto (A), Intermediario (I) y
Banco (B) — hay exactamente 6 órdenes posibles en que
pudieron haberse incorporado al esquema. Para cada orden
calculamos cuánto aportó cada actor cuando entró. Luego
promediamos.
Los datos del caso:
• Daño total documentado: $1,000,000
• A + I solos: podían lavar $600,000 (60% — evidencia
E2)
• A + B solos: podían lavar $400,000 (40% — evidencia
E4)

El Método Prometeo: Imputación Causal para juristas y abogados
• I + B sin A: podían lavar $0 (sin el diseño del
arquitecto no hay operación)
• Cualquier actor solo: $0
Paso 1 — Los 6 órdenes posibles y el aporte de
cada actor:
Orden 1: A → I → B
A entra primero: daño pasa de $0 a $0 → A
aporta $0
I entra tras A: daño pasa de $0 a $600,000 → I aporta
$600,000
B entra al final: daño pasa de $600,000 a $1,000,000 → B
aporta $400,000
Orden 2: A → B → I
A entra primero: daño pasa de $0 a $0 → A
aporta $0
B entra tras A: daño pasa de $0 a $400,000 → B
aporta $400,000
I entra al final: daño pasa de $400,000 a $1,000,000 → I
aporta $600,000
Orden 3: I → A → B
I entra primero: daño pasa de $0 a $0 → I aporta
$0
A entra tras I: daño pasa de $0 a $600,000 → A
aporta $600,000
B entra al final: daño pasa de $600,000 a $1,000,000 → B
aporta $400,000

El Método Prometeo: Imputación Causal para juristas y abogados
Orden 4: I → B → A
I entra primero: daño pasa de $0 a $0 → I aporta
$0
B entra tras I: daño pasa de $0 a $0 → B aporta
$0
(I + B sin A = $0: sin el arquitecto no hay esquema)
A entra al final: daño pasa de $0 a $1,000,000 → A
aporta $1,000,000
Orden 5: B → A → I
B entra primero: daño pasa de $0 a $0 → B aporta
$0
A entra tras B: daño pasa de $0 a $400,000 → A
aporta $400,000
I entra al final: daño pasa de $400,000 a $1,000,000 → I
aporta $600,000
Orden 6: B → I → A
B entra primero: daño pasa de $0 a $0 → B aporta
$0
I entra tras B: daño pasa de $0 a $0 → I aporta $0
(B + I sin A = $0: sin el arquitecto no hay esquema)
A entra al final: daño pasa de $0 a $1,000,000 → A
aporta $1,000,000
Paso 2 — Sumar los aportes y dividir entre 6:
Actor O O O Or O Or Su ÷ 6 %
rd rd rd d. rd d. ma
. 1 . 2 . 3 4 . 5 6

El Método Prometeo: Imputación Causal para juristas y abogados
A 0 0 60 1,0 40 1,0 3,0 $500, 50
Arquit 0 00 0 00 00 000 %
ecto K K K K K
I 60 60 0 0 60 0 1,8 $300, 30
Interm 0 0 0 00 000 %
ediario K K K K
B 40 40 40 0 0 0 1,2 $200, 20
Banco 0 0 0 00 000 %
K K K K
Verific 6,0 $1,00 10
ación 00 0,000 0
K %
✓
Lo que el método de las órdenes demuestra: El arquitecto
responde por el 50%: en cuatro de los seis órdenes, cuando A
entra al esquema agrega una cantidad significativa. El
intermediario responde por el 30%: en los tres órdenes donde
I entra con A presente, agrega $600,000. El banco responde
por el 20%: en los tres órdenes donde B entra con A presente,
agrega $400,000. Nadie queda en cero, aunque ninguno era
individualmente indispensable.
Con más de tres actores: Con 4 actores hay 24 órdenes. Con 5
actores, 120. Con 6 actores, 720. Un abogado no hace eso a mano. Pero
la lógica es idéntica: se listan todos los órdenes, se anota el aporte de cada
actor cuando entra, se suman y se dividen entre el número de órdenes. El

### Apéndice incluye una plantilla de hoja de cálculo que automatiza el cálculo
para hasta 6 actores.
5.7.4 La fórmula para el lector técnico
Para el lector que quiere la derivación formal: El método de
las órdenes es matemáticamente equivalente a la fórmula de Shapley. ¡Los
pesos de la fórmula [|S|! (n−|S|−1)! /n!] son exactamente las

El Método Prometeo: Imputación Causal para juristas y abogados
probabilidades de que un actor se incorpore a una coalición de tamaño
|S| cuando el orden de llegada es aleatorio y equiprobable. Con 3 actores:
coalición vacía → peso 1/3, coalición de tamaño 1 → peso 1/6, coalición
de tamaño 2 → peso 1/3. Esos son los mismos pesos que el promedio de
los 6 órdenes produce automáticamente.
φᵢ = Σ [ |S|! (n−|S|−1)! / n!] × [ v(S∪{i}) − v(S)]
Símbolo Traducción al lenguaje del método de las
órdenes
S Una combinación de actores sin incluir a i.
Es el grupo que ya estaba en el esquema
antes de que i entrara.
v(S∪{i}) − v(S) "Cuánto aporta i cuando entra" —
exactamente el número que calculamos en
cada orden.
|S|!(n−|S|−1)!/n! El peso de esa combinación. Con 3 actores
equivale a 1/6 para combinaciones de
tamaño 1, y 1/3 para vacía o completa. El
promedio de los 6 órdenes produce
automáticamente esos mismos pesos.
5.7.5 Cuándo usar Shapley y cuándo usar el
método de las rondas
Situación Método Criterio de decisión
adecuado
Hay un actor sin Método de las El arquitecto o el nodo
el cual el rondas central es condición
esquema no necesaria. Usar R* del
habría existido Capítulo 2. Es el caso
más frecuente en

El Método Prometeo: Imputación Causal para juristas y abogados
esquemas con un solo
diseñador.
Múltiples Valores de Ningún intermediario
intermediarios Shapley (método es individualmente
donde cada uno de las órdenes) indispensable. El
podría haber sido dinero podría haber
reemplazado por viajado por rutas
otro alternativas. Usar el
método de órdenes.
Arquitecto Rondas para el El arquitecto tiene R*
indispensable + arquitecto + alto por el método de
intermediarios órdenes para los rondas. Para distribuir
fungibles entre sí intermediarios la responsabilidad
entre los
intermediarios
sustituibles, aplicar
Shapley solo a ese
subconjunto.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.8 La distinción entre el
APNFD y el beneficiario final
Dos categorías de nodos requieren un tratamiento
específico en el análisis de PLD porque su posición causal
es frecuentemente malentendida: las Actividades y
Profesiones No Financieras Designadas (APNFD) y el
beneficiario final real (UBO — Ultimate Beneficial Owner).
5.8.1 El APNFD: el nodo que habilita sin
ver el todo
APNFD (Actividades y Profesiones No Financieras
Designadas): El conjunto de profesionales y empresas
que sin ser instituciones financieras tienen obligaciones de
PLD porque sus servicios son frecuentemente utilizados en
esquemas de lavado: abogados, contadores, notarios,
agentes inmobiliarios, casinos, servicios de constitución de
empresas. Su posición causal en el grafo es típicamente de
habilitación estructural: no mueven el dinero directamente,
pero proveen los instrumentos jurídicos o las transacciones
que lo ocultan.
El análisis de R* para un APNFD depende de una
distinción que el grafo hace explícita: ¿el APNFD diseñó la
estructura del esquema, o simplemente proveyó un servicio
estándar que el arquitecto usó? Un abogado que
activamente diseñó la estructura offshore específica para
ese cliente tiene R* alto y S bajo. Un notario que protocolizó
documentos sin conocimiento del esquema tiene R* bajo y
S alto.
Tipo de R* S Criterio de distinción
APNFD típico típico

El Método Prometeo: Imputación Causal para juristas y abogados
Estructurador 15 – 0.20 – Diseñó la estructura
activo 35% 0.40 específica para ese cliente.
Eligió las jurisdicciones y
los vehículos. Tiene
conocimiento
documentado del perfil de
riesgo del cliente. Hijo
dominante: Eros+Potós.
Profesional con 8 – 0.45 – Proveyó un servicio
conocimiento 20% 0.65 estándar con señales de
parcial alerta que no reportó. No
diseñó el esquema. Tenía
indicios, pero no el cuadro
completo. Hijo dominante:
Potós o Fobos.
Proveedor de 3 – 0.70 – Proveyó el servicio dentro
buena fe 10% 0.90 de sus procedimientos
estándar. El esquema
estaba diseñado para
parecer legítimo. No tenía
indicios razonables. Hijo
dominante: Deimos.
5.8.2 El beneficiario final real: el nodo que
el grafo debe encontrar
El beneficiario final real (UBO) es la persona física que en
última instancia controla la entidad o que se beneficia de la
operación, aunque no aparezca en ningún documento como
tal. Es el nodo que el grafo debe identificar, aunque no esté
documentado directamente. Es el candidato natural al
mayor R* del esquema.
La distinción entre el UBO nominal (quien aparece en los
registros como accionista o director final) y el UBO real
(quien efectivamente controla y se beneficia) es el problema
central del análisis de beneficiario en PLD. Los esquemas

El Método Prometeo: Imputación Causal para juristas y abogados
bien diseñados tienen capas adicionales entre el UBO
nominal y el UBO real.
Tipo de Posición Cómo identificarlo
beneficiario en el
grafo
UBO nominal Nodo de Aparece en los documentos de las
(registrado) ejecución entidades. Alta probabilidad de ser
visible testaferro si: (a) es director de
múltiples empresas sin relación
aparente, (b) es nacional de la
jurisdicción donde se registra la
empresa pero no tiene actividad
económica en esa jurisdicción, (c)
tiene antecedentes de ser
prestanombre.
UBO real Nodo de Se identifica mediante: (a) análisis
(efectivo) diseño / del destinatario final de los activos
arquitecto integrados, (b) correlación entre
los patrones de activación del
esquema y los movimientos del
presunto UBO real, (c)
comunicaciones entre
intermediarios que lo mencionan
sin nombrarlo, (d) coincidencia
geográfica y temporal entre la
operación y los activos del
presunto UBO.
UBO oculto Nodo Se infiere cuando: ninguno de los
(no registrado inferido nodos visibles tiene el perfil
en ningún económico para ser el beneficiario
documento) real, el esquema tiene un nivel de
sofisticación que requiere
conocimiento especializado que
ningún nodo visible tiene, o los
activos integrados no van a
ningún nodo identificado.
R*_oculto > 0.40 es la señal.

El Método Prometeo: Imputación Causal para juristas y abogados
El caso trabajado de este capítulo: La operación completa de
lavado — con el funcionario público, las sociedades offshore y el análisis
de extinción de dominio — se desarrolla en el Capítulo 7. Las
herramientas de este capítulo (el grafo, los tipos de evidencia T-E0 a T-
E1, S, α, Shapley) se aplican allí sobre ese caso con el protocolo completo.

El Método Prometeo: Imputación Causal para juristas y abogados
§5.9 Lo que el análisis PLD
aporta que el análisis
convencional no puede
El análisis convencional de PLD está construido sobre la
búsqueda de transacciones inusuales y la trazabilidad del
dinero. Esas herramientas son necesarias pero insuficientes
cuando el esquema fue diseñado para que la trazabilidad se
detenga en un intermediario. El Método Prometeo añade
tres instrumentos que ese análisis no tiene:
Instrumento Qué aporta que el análisis convencional
no puede producir
R* como Identifica al arquitecto, aunque no aparezca
necesidad causal en los documentos. La concentración de R*
en el nodo con visibilidad baja es la firma
matemática del lavado bien diseñado. Esa
concentración orienta la investigación hacia
dónde buscar la evidencia corroborante.
El nodo inferido Cuando todos los nodos visibles tienen S alto,
con R*_oculto el cálculo produce R*_oculto alto
automáticamente. Ese número es la señal de
que existe un actor no identificado. No es
evidencia de condena — es evidencia de que
la investigación está incompleta.
Shapley para Cuando el dinero podría haber viajado por
cadenas rutas alternativas, el método de las rondas
redundantes falla. Shapley distribuye la responsabilidad
correctamente incluso cuando ningún actor
individual es condición necesaria — que es
exactamente el diseño de los esquemas de
lavado más sofisticados.
Δ de compliance El Δ = R* − α de cada institución financiera
como base de o APNFD mide su déficit de compliance
proporcional a su participación causal. Una

El Método Prometeo: Imputación Causal para juristas y abogados
sanción sanción regulatoria proporcional al Δ de la
proporcional institución — no al monto de la transacción
— es más justa y más eficiente como
disuasor.
Lo que este capítulo estableció
✓ En PLD, la inversión causal es un objetivo del diseño, no un
efecto colateral. El arquitecto tiene R* ≈ 55-70% y α = 0. El
testaferro tiene R* ≈ 4-8% y α = 100% forzado.
✓ Las herramientas del método se renombran en PLD: R* =
necesidad causal, α = cumplimiento de la obligación de
reporte, Δ = déficit de compliance, D_total = daño al sistema
financiero.
✓ La tabla de evidencia transaccional (T-E0 a T-E1) adapta los
tipos de evidencia al contexto de investigaciones financieras:
registros de instrucción, análisis forense bancario, correlación
de patrones.
✓ El nodo inferido es el nodo cuya existencia no está
documentada, pero es causalmente necesario. R*_oculto >
0.40 en una operación de aparente legitimidad es la señal de
que hay un actor no identificado.
✓ Los valores de Shapley distribuyen correctamente la
responsabilidad en cadenas con múltiples eslabones
redundantes, donde el método de las rondas convencional
asigna cero a todos.
✓ La distinción APNFD: el estructurador activo tiene R* alto y S
bajo (diseñó el instrumento). El proveedor de buena fe tiene
R* bajo y S alto (ejecutó sin conocimiento). El DA del caso
trabajado tuvo el mayor R* del esquema.
✓ B_total × R*_B es la base técnica para la extinción de dominio
proporcional, independientemente de a nombre de quién estén

El Método Prometeo: Imputación Causal para juristas y abogados
registrados los activos. El Capítulo 7 aplica este cálculo sobre
el caso completo.

El Método Prometeo: Imputación Causal para juristas y abogados
EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL

