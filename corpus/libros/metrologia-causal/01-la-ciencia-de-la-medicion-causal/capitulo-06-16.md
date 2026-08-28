## PARTE VI · Los documentos del análisis: producción e interpretación

### Capítulo VI·16
El expediente como herramienta de
comunicación
Cómo presentar el expediente ante audiencias técnicas y no técnicas

### I. El expediente no es solo un instrumento
analítico
El expediente de análisis causal tiene dos funciones. La
primera es la función analítica: describir la estructura causal del
caso con precisión suficiente para que el análisis sea
verificable, reproducible y resistente a la impugnación. La
segunda es la función comunicativa: transmitir las
conclusiones del análisis a las audiencias que toman decisiones
sobre el caso, de manera que esas audiencias puedan
procesarlas y actuar sobre ellas. Las dos funciones son
complementarias, pero requieren estrategias distintas.
Un expediente que maximiza la función analítica — con la
hoja de calibración más detallada, el vector R* con todas las
columnas, el reporte de sensibilidad con todos los puntos de
quiebre y la Declaración con toda su formulación técnica —
puede ser inaccesible para una audiencia no técnica. Un
expediente que maximiza la función comunicativa — con la
Declaración en lenguaje simple y un resumen narrativo del

Metrología Causal
caso — puede no tener la profundidad analítica que el estándar
adversarial requiere. La estrategia de presentación debe
balancear las dos funciones según el foro.

### II. Presentación ante audiencias técnicas vs. no
técnicas
La presentación ante audiencias técnicas (árbitros con
formación cuantitativa, peritos contraparte, auditores
regulatorios especializados) usa el expediente completo como
documento de referencia y concentra la presentación oral en
tres puntos: la construcción del grafo y sus fundamentos de
evidencia (hoja de calibración), la robustez de la conclusión
(reporte de sensibilidad y Declaración), y los supuestos críticos
que el adversario necesitaría refutar (puntos de quiebre del
reporte). Esta presentación asume que la audiencia puede
verificar los cálculos y que la profundidad técnica es un activo,
no un obstáculo.
La presentación ante audiencias no técnicas (jurado, consejo
de administración sin formación cuantitativa, medios de
comunicación) requiere una traducción del análisis a tres
afirmaciones verificables en lenguaje natural. Primera: «el
sistema identifica [nodo] como el factor más determinante del
resultado, con independencia de cómo se interprete
razonablemente la evidencia». Segunda: «la razón es que
[descripción narrativa de la posición del nodo en el grafo y del
mecanismo de influencia]». Tercera: «el análisis puede ser
impugnado demostrando que [descripción en lenguaje simple
de lo que el adversario necesitaría demostrar]». Estas tres
afirmaciones son la esencia de la Declaración A en formato
accesible.

Metrología Causal

### III. El resumen ejecutivo: qué contiene y
cuándo es suficiente
El resumen ejecutivo del expediente tiene una página y
contiene cinco elementos. Primero: la descripción del sistema
analizado (quiénes son los nodos, cuál es el resultado D).
Segundo: la conclusión principal (qué nodo tiene mayor
R*_neta y en qué proporción). Tercero: el diagnóstico del
sistema (Δ_total como indicador del déficit de asunción
global). Cuarto: la robustez de la conclusión (el nivel de
Declaración y su formulación en lenguaje natural). Quinto: las
preguntas que el expediente no puede responder (para que el
lector no confunda lo que el análisis dice con lo que el análisis
no dice).
El resumen ejecutivo es suficiente cuando la audiencia necesita
tomar una decisión de primer orden sobre el caso — si el caso
merece investigación adicional, si el nodo identificado merece
ser sometido a un proceso formal, si el plan de remediación
está correctamente orientado. El resumen ejecutivo no es
suficiente cuando la audiencia necesita verificar el análisis,
impugnarlo o construir sobre él. En esos casos, el expediente
completo — los cuatro documentos — es el instrumento
necesario.
La regla de uso del resumen ejecutivo: cuando la audiencia
actúa sobre la conclusión (el consejo que aprueba el plan de
remediación, el regulador que impone la medida cautelar, el
fiscal que decide si investigar), el resumen puede ser suficiente.
Cuando la audiencia evalúa la conclusión (el árbitro que decide
si aceptar el análisis como prueba, la contraparte que decide si
impugnar, el analista independiente que verifica), el expediente
completo es necesario.
El expediente no es el análisis: es el registro del análisis. El
análisis ocurre en la mente del analista que construye el grafo,

Metrología Causal
calibra los pesos, lee la distribución de R* y decide qué
Declaración producen los datos. El expediente hace ese
análisis verificable — hace posible que otro analista, con los
mismos datos, llegue al mismo resultado o identifique dónde
difiere. Esa verificabilidad es la condición de la objetividad:
no que nadie pueda disentir, sino que, si alguien disiente,
pueda mostrar exactamente en qué punto del expediente el
desacuerdo comienza.
Notas al capítulo VI·16
1 El principio de que el expediente hace el análisis «verificable»
corresponde al criterio de falsificabilidad de Karl Popper (La lógica de
la investigación científica, 1934) aplicado al análisis forense. El análisis
causal que no puede ser verificado ni falsificado no es científico en
sentido popperiano: puede ser correcto o incorrecto, pero no puede
distinguirse entre los dos estados. El expediente de cuatro documentos
con los rangos de evidencia explícitos y el análisis de sensibilidad es el
instrumento que hace el análisis causal falsificable: la contraparte puede
demostrar que algún peso está fuera de su rango, que algún nodo falta
en el grafo, o que el análisis de sensibilidad no cubre suficientemente el
espacio de parámetros. Esa posibilidad de falsificación es la condición
de la credibilidad del análisis.
2 La distinción entre el resumen ejecutivo y el expediente completo tiene
un paralelo directo en la práctica de auditoría financiera. El dictamen del
auditor es el equivalente del resumen ejecutivo: una o dos páginas con
la conclusión sobre si los estados financieros presentan razonablemente
la situación financiera de la empresa. Los papeles de trabajo del auditor
son el equivalente del expediente completo: toda la evidencia, los
cálculos y los supuestos que fundamentan el dictamen. El dictamen es
suficiente para la mayoría de los usuarios; los papeles de trabajo son
necesarios para quien quiere verificar el dictamen o impugnarlo.

Metrología Causal
CASO DE CIERRE
El expediente Altamirano
Caso real anonimizado — análisis integrado en tres series
Este caso recorre el sistema completo desde la construcción
del grafo hasta la Declaración A. Es a la vez el ejemplo más
complejo y el más instructivo del libro, porque demuestra en
un caso real las propiedades que las partes anteriores
establecieron en abstracto: la paradoja de la visibilidad, el
fraude annona, la distinción entre el criterio del dolo y el
criterio causal, la Declaración A como producto del análisis de
sensibilidad y no como punto de partida.
Los nombres, fechas y detalles identificatorios han sido
anonimizados. La estructura del caso, los hechos causalmente
relevantes y todos los valores numéricos son reales.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·1
Presentación del caso y los hechos
La secuencia completa desde la rescisión hasta el impedimento
estructural de empleo

### I. El contexto y el detonante
Rodrigo Altamirano Vega es gerente de nivel medio en una
institución financiera con operaciones en tres estados. El 3 de
abril, la institución rescinde su contrato de manera unilateral
invocando una carpeta de investigación iniciada en la Fiscalía
Regional de Occidente (FRO) por presunta malversación de
fondos institucionales. Altamirano niega los hechos y solicita
asesoría legal. La investigación está en etapa inicial; no hay
imputación formal ni medida cautelar.
La rescisión activa dos consecuencias inmediatas. Primera:
Altamirano queda registrado en el sistema de recursos
humanos de la institución financiera con un código de salida
que señala la causa como «desvinculación por proceso legal en
curso». Segunda: la carpeta de investigación de la FRO, que en
ese momento contiene declaraciones preliminares, registros
internos de la institución y datos personales de Altamirano, es
el documento más sensible del proceso.

Metrología Causal

### II. La secuencia de los hechos causalmente
relevantes
El 15 de mayo, el agente del Ministerio Público Claudia
Esperanza Partida (ECP) atiende a Altamirano en la vía
pública, fuera del edificio de la FRO, en una conversación no
registrada. No existe folio de atención, no existe registro de
visita, no existe acta de la conversación. En algún momento
de esa conversación o de sus consecuencias inmediatas — la
cadena causal exacta es objeto del análisis de sensibilidad —
ECP entrega a un tercero, identificado en este análisis como
Garmendia Leal, documentos de la carpeta de investigación.
Garmendia Leal no tiene representación formal de Altamirano
ni acceso autorizado a la carpeta.
El 20 de mayo — cinco días después de la conversación no
registrada — Banco Meridional (BM) entrega a Garmendia
Leal la tarjeta de crédito vinculada al contrato 80314809399 de
Altamirano. La entrega no fue autorizada por Altamirano. Para
que BM entregara la tarjeta a Garmendia Leal, este tuvo que
presentar información que no es pública ni fácilmente
accesible — el número de contrato, la identificación del
producto, datos que solo estarían disponibles para alguien con
acceso a la carpeta de investigación o a los documentos que
esa carpeta contiene.
El 22 de mayo, Altamirano presenta denuncia a través del
mecanismo VISITEL de la FRO, describiendo los hechos del
15 de mayo, la relación causal que infiere entre la conversación
no registrada y la suplantación bancaria del 20 de mayo, y la
identidad de ECP como el agente de la FRO que atendió la
conversación. La denuncia recibe un folio de registro. No
produce ninguna acción documentada de la FRO sobre ECP
ni sobre la carpeta.

Metrología Causal
A partir del 23 de mayo, una segunda agente del MP,
identificada en este análisis como Paola Serrano Morales
(PSM), pasa a ser el contacto institucional de Altamirano en la
FRO. PSM confirma haber recibido el expediente del caso,
confirma tener conocimiento de la denuncia VISITEL, y no
documenta ninguna acción sobre ECP. En la semana siguiente
al 23 de mayo, PSM deja de responder comunicaciones. No
existe documentación de su salida del caso ni de quién la
reemplazó.
El banco Meridional aplica el estatus 25 al contrato
80314809399 de Altamirano. El estatus 25, documentado
fotográficamente en la pantalla del sistema BM durante una
gestión posterior de Altamirano, corresponde a un estado de
inhabilitación de la cuenta que bloquea la emisión de nuevos
productos financieros a nombre del titular. Este estado no
requiere acción continua de ningún actor para mantenerse: es
estructuralmente persistente hasta que sea modificado por
BM.
Durante los doce meses siguientes, Altamirano busca empleo
en el sector financiero. La rescisión con código de «proceso
legal en curso» y el estatus 25 en BM producen un efecto
combinado: los empleadores del sector financiero que
verifican antecedentes laborales y crediticios reciben señales
negativas que impiden la contratación. Al momento del
análisis, Altamirano lleva más de doce meses sin empleo en su
sector de especialización, con las consecuencias económicas
correspondientes.

### III. Los documentos disponibles
El análisis se construye sobre los siguientes documentos. El
contrato de rescisión de la institución financiera con el código
de causa. El folio de la denuncia VISITEL de Altamirano. Las

Metrología Causal
comunicaciones de Altamirano con PSM durante la semana
del 23 al 30 de mayo (incluyendo la frase, en mensaje de texto
de PSM: «ojalá no haya más sorpresas»). La fotografía del
sistema BM mostrando el estatus 25 en el contrato

### 80314809399. El historial de solicitudes de empleo y sus
respuestas durante los doce meses posteriores. La
comunicación de ECP a Altamirano en la que sugiere la
reunión fuera del edificio («paso por allá al rato»).
Notas al capítulo C·1
1 El caso ha sido anonimizado mediante el cambio de todos los nombres
de personas (Altamirano Vega, Partida, Serrano Morales, Garmendia
Leal), la omisión de la denominación completa de las instituciones
(FRO, BM), la modificación de las fechas específicas manteniendo los
intervalos temporales exactos, y el redondeo de los valores monetarios
al rango. Los hechos causalmente relevantes — la secuencia de actos,
los mecanismos de daño, los documentos disponibles y los valores
calculados — son fieles al caso real.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·2
Los nodos del sistema y la evidencia
documental
Descripción, posición en la cadena causal y evidencia disponible
para cada nodo

### I. Descripción de los cuatro nodos del sistema
El sistema tiene cuatro nodos causalmente necesarios para el
resultado D (el daño económico diferido de Altamirano: doce
meses sin empleo en el sector de especialización con
consecuencias económicas estimadas en $336,000–$540,000
pesos).
No Descripció Posición Tipo de Evidencia
do n en la influenci disponible
cadena a
EC Agente del Nodo Acto Comunicaci
P Ministerio detonante. comisivo ón «paso
Público. La arista directo: por allá al
Contacto ECP→B entrega de rato».

Metrología Causal
de M es la document Ausencia de
Altamirano que os a folio de
en la FRO habilita el persona atención del
en el mecanism no 15 de mayo.
período o de daño autorizada Mensaje
anterior al económic . Acto «ojalá no
22 de mayo. o omisivo: haya más
Ejecutó la estructural no sorpresas».
conversació . registrar la
n no visita.
registrada
del 15 de
mayo y
entregó
documento
s de la
carpeta a
Garmendia
Leal.
PS Segunda Nodo de Acto Comunicaci
M agente del encubrimi omisivo: ones con
MP, ento y no actuar Altamirano
contacto de prolongac sobre la de la
Altamirano ión del denuncia semana 23–
a partir del daño VISITEL. 30 de mayo.
23 de mayo. procesal. Acto Ausencia de
Recibió el comisivo: acción
expediente responder documenta
con a da sobre
conocimien Altamiran ECP o
to de la o sobre la
denuncia producien carpeta.
VISITEL. do la Frase «ojalá
No expectativ no haya
documentó a de más
acción acción sin sorpresas»

Metrología Causal
alguna producirla como
sobre ECP. . evidencia
Desapareci de
ó del conocimien
proceso sin to y
documenta evasión.
ción de
reemplazo.
FR Fiscalía Nodo de Diseño Protocolos
O Regional de diseño del institucion declarados
Occidente campo. al: la de la FRO
como nodo Tiene el ausencia (si existen).
de diseño mayor R* de Ausencia de
del campo. y el menor protocolo registro de
Diseñó (o S por s acción
no diseñó) construcci operativos sobre la
los ón. efectivos denuncia
protocolos produjo el VISITEL.
de registro campo en Ausencia de
de visitas, el que registro de
de ECP pudo salida de
confidencia actuar sin PSM del
lidad de rastro y caso.
carpetas y PSM pudo
de atención encubrir
de sin
denuncias consecuen
VISITEL. cias.
El IIC
sobre estos
tres
protocolos
es el
parámetro

Metrología Causal
central de la
Serie II.
BM Banco Nodo de Acto Fotografía
Meridional. daño comisivo: del estatus
Entregó la estructural entrega no 25 en
tarjeta de persistent autorizada pantalla del
crédito a e. El de la sistema
Garmendia estatus 25 tarjeta. BM.
Leal el 20 produce Diseño Ausencia de
de mayo sin daño sistémico: autorizació
autorizació económic el n de
n de o diferido mecanism Altamirano
Altamirano. sin o del para
Aplicó el necesidad estatus 25 entrega de
estatus 25 al de acción como tarjeta.
contrato continua. respuesta
803148093 automátic
99. a ante
señales de
irregularid
ad.

### II. La posición causal de cada nodo y su prueba
desde la condición sine qua non
ECP es condición necesaria del daño porque la entrega de
documentos a Garmendia Leal — que habilitó la suplantación
bancaria — no habría ocurrido sin la conversación no
registrada del 15 de mayo. Sin ECP, Garmendia Leal no habría
tenido los datos que usó el 20 de mayo. ECP satisface el test:
sin ECP, D no ocurre de esa forma específica.

Metrología Causal
PSM es condición necesaria del daño diferido — no del
detonante — porque la denuncia VISITEL de Altamirano, si
hubiera producido acción, habría interrumpido el mecanismo
de daño antes de que el estatus 25 se consolidara como
impedimento estructural de empleo. Sin la omisión de PSM (y
de la FRO a través de PSM), el daño habría sido procesal
agudo, pero no habría llegado a ser daño económico diferido
de doce meses. PSM satisface el test para el resultado D
extendido.
FRO es condición necesaria de todo el sistema porque el
campo que hizo posible que ECP actuara sin rastro y que PSM
encubriera sin consecuencias es el campo que FRO diseñó (o
no diseñó) con sus protocolos. Sin el campo de FRO — con
los protocolos declarados realmente operativos — ECP habría
tenido que registrar la visita (lo que habría dejado rastro
documental y habría inhibido la entrega), y PSM habría tenido
que documentar su acción sobre la denuncia (lo que habría
producido consecuencias para ECP). Sin ese campo, D no
ocurre de esa forma.
BM es condición necesaria del daño económico diferido
porque el estatus 25 es el mecanismo que convierte el daño
procesal en impedimento estructural de empleo. Sin el estatus
25 —sin la respuesta automática de BM ante las señales de
irregularidad que ECP habilitó con la entrega de
documentos— el daño habría sido reputacional sin el
componente crediticio que bloquea la contratación en el sector
financiero. BM satisface el test para el resultado D con el
horizonte temporal de doce meses.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·3
La estructura del daño en tres capas
Por qué ninguna capa se produce sin las otras dos y sin embargo
cada una tiene su nodo primario

### I. Capa 1: el daño procesal inmediato (ECP)
La primera capa del daño es el daño procesal inmediato: la
entrega de documentos de la carpeta de investigación a un
tercero no autorizado, la suplantación bancaria que se produce
cinco días después, y la exposición de información
confidencial de Altamirano a un actor externo. Este daño tiene
un nodo primario: ECP. Es la entrega de documentos de ECP
a Garmendia Leal la que habilita directamente la suplantación
bancaria del 20 de mayo. Sin ese acto específico de ECP, la
cadena causal de la Capa 1 no se inicia.
La Capa 1 no requiere la Capa 2 ni la Capa 3 para existir como
daño: la exposición de la carpeta y la suplantación bancaria son
daños por sí mismos, con independencia de que la FRO
actuara o no sobre la denuncia y con independencia de que
BM aplicara o no el estatus 25. En ese sentido, ECP es el nodo
con mayor R* en el subgrafo de la Capa 1.

Metrología Causal

### II. Capa 2: el daño procesal prolongado (PSM y
FRO)
La segunda capa es el daño procesal prolongado: la inacción
ante la denuncia VISITEL, el encubrimiento de PSM, la
ausencia de consecuencias para ECP dentro de la FRO. Esta
capa transforma el daño procesal agudo de la Capa 1 en un
daño procesal crónico: la carpeta de investigación permanece
expuesta, el proceso no produce consecuencias para quien
expuso la carpeta, y la señal que BM recibió sobre la
irregularidad de la entrega de la tarjeta no es corregida por
ninguna autoridad.
El nodo primario de la Capa 2 es la FRO como sistema y PSM
como agente de ese sistema. La inacción de PSM no es
idiosincrática — cualquier agente que recibiera el expediente
en el contexto del campo producido por la FRO habría tenido
los mismos incentivos para no actuar (S_PSM alto). El diseño
del campo de la FRO — sin mecanismos efectivos de
rendición de cuentas, sin seguimiento obligatorio de denuncias
VISITEL, sin documentación de cambios de agente — es lo
que hace que la Capa 2 sea sistémicamente inevitable.
La Capa 2 depende de la Capa 1 porque sin el acto detonante
de ECP no habría denuncia VISITEL. Pero la Capa 2 no es
simplemente la consecuencia de la Capa 1: es la amplificación
del daño por inacción institucional. El daño de la Capa 2 — el
daño procesal prolongado — no es el mismo que el de la Capa
1: es más extenso, más estructural y más difícil de reparar
porque involucra a la institución y no solo a un agente
individual.

### III. Capa 3: el daño económico diferido (BM
habilitado por ECP y FRO)

Metrología Causal
La tercera capa es el daño económico diferido: doce meses sin
empleo en el sector de especialización, con pérdida de ingresos
estimada en $336,000–$540,000 pesos. El nodo primario de
esta capa es BM — no porque BM sea el más responsable del
sistema completo, sino porque el mecanismo específico que
produce el daño económico diferido (el estatus 25) pertenece
a BM. Sin el estatus 25, el daño se habría mantenido en el nivel
procesal sin alcanzar el nivel económico estructural.
Pero la Capa 3 no existe sin las Capas 1 y 2. BM activó el
estatus 25 porque recibió señales de irregularidad que vinieron
de la cadena causal habilitada por ECP y no corregida por
FRO a través de PSM. El estatus 25 es la respuesta sistémica
de BM ante esas señales — una respuesta que tiene S alto
(cualquier banco habría activado un mecanismo similar ante
las mismas señales) pero que produce el daño económico
diferido con independencia de si la señal que la activó era
correcta o fraudulenta.
La interdependencia de las tres capas es la estructura causal
central del caso: ninguna capa produce el daño completo por
sí sola, pero cada una tiene su nodo primario que es condición
necesaria de esa capa específica. El análisis de R* distribuirá la
responsabilidad entre los cuatro nodos de manera que refleje
esta estructura de capas interdependientes.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·4
La hoja de calibración completa
Siete aristas con intervalos, evidencia y nivel de certeza

### I. Las siete aristas del grafo causal
El grafo causal del caso Altamirano tiene cuatro nodos (ECP,
PSM, FRO, BM) y siete aristas. Las siete aristas capturan todos
los mecanismos causales identificados en el análisis de los
hechos. La numeración sigue el orden topológico: primero las
aristas desde el nodo de diseño (FRO), luego las aristas entre
ejecutores, luego las aristas hacia el resultado diferido.
Arista Mecanis Ran Fuente de Certeza
mo go evidencia
causal [a,
b]
FRO → FRO [0.4 Ausencia Media — la
ECP diseñó (o 5, de folio de arista es
no diseñó) 0.75 atención estructural,
el campo ] del 15 de no
de trabajo mayo directamen

Metrología Causal
sin (evidencia te
protocolos estructural: documenta
de registro el da como
de visitas, protocolo instrucción
de no existía o de FRO a
confidenci no se ECP.
alidad de aplicaba).
carpetas y Comunicac
de ión «paso
supervisió por allá al
n de rato» como
agentes. evidencia
Ese de
campo normalizaci
habilitó a ón de
ECP para contacto
actuar sin informal.
rastro.
ECP no
habría
podido
ejecutar la
conversaci
ón no
registrada
en un
campo
con
protocolos
operativos
.
FRO → FRO [0.4 Ausencia Media —
PSM diseñó el 0, de acción misma base
campo en 0.70 documenta estructural
el que ] da sobre que
PSM denuncia

Metrología Causal
operó: sin VISITEL. FRO→EC
mecanism Ausencia P.
o de de registro
seguimient de salida de
o PSM.
obligatori Ausencia
o de de
denuncias consecuenc
VISITEL, ias
sin documenta
document das para
ación de ningún
cambio de agente en
agente, sin relación
consecuen con el caso.
cias para la
inacción.
PSM
habría
actuado de
manera
distinta en
un campo
con esos
mecanism
os.
ECP → ECP [0.5 Coincidenc Media-alta
BM entregó a 0, ia temporal — la
Garmendi 0.85 de cinco coincidenci
a Leal ] días entre la a temporal
document conversaci es
os de la ón no evidencia
carpeta de registrada fuerte. La
investigaci (15/may) y falta de
ón que la registro de
contenían suplantació la

Metrología Causal
informaci n bancaria conversaci
ón (20/may). ón impide
suficiente Tipo de certeza
para que informació plena.
Garmendi n requerida
a Leal se para la
suplantara suplantació
ante BM el n (datos del
20 de contrato y
mayo. La producto)
coincidenc solo
ia disponible
temporal en la
de cinco carpeta o a
días y el través de
tipo de ella.
informaci
ón
requerida
para la
suplantaci
ón hace
esta arista
el eje del
diagnóstic
o del caso.
ECP → La acción [0.2 Secuencia Baja —
FRO de ECP 0, temporal: arista de
(feedback) creó una 0.45 ECP retroalimen
situación ] (15/may) tación
en la que → inferida, no
FRO tenía denuncia directamen
que actuar VISITEL te
o no (22/may) documenta
actuar ante → inacción da.
la de

Metrología Causal
denuncia PSM/FRO
VISITEL. . La
La retroalimen
inacción tación es
de FRO (a inferida
través de desde la
PSM) es estructura
en parte de
una incentivos
respuesta instituciona
al campo les.
de
incentivos
institucion
ales ante el
riesgo de
reconocer
que un
agente
propio
expuso
una
carpeta.
PSM → La [0.2 Ausencia Media-baja
FRO inacción 5, de — la
(encubrim de PSM 0.50 documenta inacción de
iento) consolidó ] ción de PSM es
la posición acción. documenta
de FRO Frase «ojalá ble en su
como no haya ausencia
campo sin más pero el
consecuen sorpresas» mecanismo
cias para la como de
violación evidencia amplificaci
de la de ón del
carpeta. conocimie campo

Metrología Causal
PSM nto del FRO es
amplió el riesgo sin inferido.
campo acción.
disfuncion
al de FRO
al no
document
ar, no
actuar y
desaparece
r del caso.
FRO → El campo [0.3 Ausencia Media — la
BM disfuncion 0, de acción habilitación
(habilitaci al de FRO 0.60 de FRO sistémica es
ón (IIC = ] sobre estructural.
sistémica) 0.017) VISITEL. La
habilitó El evidencia
que la mecanismo específica
señal de de de la arista
irregularid corrección es inferida.
ad que que FRO
llegó a BM no activó es
no fuera estructural
corregida (existe en
por los
ninguna protocolos
autoridad de
del coordinaci
proceso ón entre
penal. Si la fiscalías y
FRO entidades
hubiera financieras)
actuado .
sobre la
denuncia
VISITEL,

Metrología Causal
BM habría
recibido
una señal
de
corrección
que podría
haber
modificad
o o
levantado
el estatus
25.
BM → D BM aplicó [0.6 Fotografía Alta — la
el estatus 5, del estatus existencia
25 al 0.85 25 en del estatus
contrato ] pantalla del 25 está
80314809 sistema fotográfica
399, BM. mente
bloqueand Historial de documenta
o la solicitudes da. El
emisión de de empleo mecanismo
nuevos y sus de bloqueo
productos respuestas de empleo
financiero durante está bien
s. El doce documenta
estatus 25 meses. do en el
produjo el Testimonio sector.
daño de
económic Altamirano
o diferido sobre la
de doce razón
meses comunicad
porque las a por los
verificacio empleadore
nes de s.
empleador

Metrología Causal
es del
sector
financiero
producen
señal
negativa
ante ese
estado.

### II. La arista ECP→BM como eje del
diagnóstico
La arista ECP→BM es la de mayor incertidumbre en el grafo
y la de mayor peso diagnóstico. Si el peso de esta arista está en
el extremo inferior de su rango [0.50, 0.85] — es decir, si la
relación causal entre la conversación del 15 de mayo y la
suplantación bancaria del 20 de mayo es menos intensa de lo
que la coincidencia temporal sugiere — la distribución de R*
se modifica: ECP retiene alta R* pero BM la reduce. Si el peso
está en el extremo superior, BM eleva su R* acercándose al
nivel de ECP.
La razón por la que esta arista es el eje diagnóstico: es la única
arista del grafo donde la incertidumbre epistémica es
potencialmente reducible. La evidencia de la coincidencia
temporal es fuerte pero no establece el mecanismo con certeza
plena; evidencia adicional — el historial de contactos de
Garmendia Leal con BM antes del 20 de mayo, los
documentos específicos que Garmendia Leal presentó ante
BM — podría estrechar el rango significativamente. En el
análisis de sensibilidad, esta arista produce los únicos puntos
de quiebre del caso.

Metrología Causal
La firma de la arista ECP→BM como señal de Fobos
La coincidencia temporal de cinco días es una firma
estructural de Fobos en ECP: el actor en Fobos opera para
producir invisibilidad del acto (la conversación no registrada)
y el resultado del acto (la suplantación bancaria) se produce
en el intervalo mínimo necesario para que la información sea
usada.
La ausencia de registro de la conversación del 15 de mayo es
la firma de Fobos-preventivo: ECP evitó el rastro antes de
que ninguna amenaza se materializara. Esa evitación previa es
incompatible con Anteros soberano (que habría confrontado
el riesgo) y con Harmonía (que no habría necesitado operar
en ausencia de rastro).
S_ECP = 0.08: la firma de Fobos-preventivo en un agente del
MP con acceso a carpetas sensibles no es altamente sustituible
— el acto requería la v_t específica de quien tenía acceso,
conocimiento del sistema de registro y disposición a operar
fuera de él.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·5
El vector R* y los parámetros del sistema
R*, S, α y Δ con su derivación desde la evidencia del caso

### I. Derivación de S para cada nodo
S_ECP = 0.08. Hijo dominante: Fobos estructural (firma
documental confirmable desde la ausencia de registro y la
operación en espacio informal). Según la tabla de S por Hijo
(II·10), Fobos produce S ∈ [0.60, 0.80] en el caso general. Sin
embargo, la especificidad del acto — filtrar una carpeta de
investigación requiere acceso específico, conocimiento del
sistema y disposición particular — reduce S al extremo inferior
del rango de Fobos. La modulación adicional por el código E-
1 (ego genuino que opera el Fobos desde sí mismo, no desde
un campo completamente determinante) reduce S
adicionalmente. S_ECP = 0.08.
S_PSM = 0.74. Hijo dominante: Fobos estructural con señal
de Anteros reactivo tardío. La frase «ojalá no haya más
sorpresas» es evidencia de conocimiento del riesgo y de Fobos
ante las consecuencias de actuar. En el campo de la FRO (IIC
= 0.017), cualquier agente que recibiera el expediente habría
tenido los mismos incentivos estructurales para no actuar.

Metrología Causal
S_PSM = 0.74: la inacción de PSM es altamente sustituible —
el campo la produce sistemáticamente.
S_FRO = 0.05. El diseñador del campo tiene S cercano a 0
por construcción (II·11). La FRO diseñó el campo específico
que hizo posibles los actos de ECP y PSM. Sin ese campo
específico — con los protocolos declarados realmente
operativos — ECP no habría podido operar sin rastro y PSM
no habría podido no actuar sin consecuencias. S_FRO = 0.05.
S_BM = 0.51. El mecanismo del estatus 25 es una respuesta
sistémica de BM ante señales de irregularidad — tiene
componente de diseño del campo (el mecanismo fue diseñado
institucionalmente) y componente de acto ejecutivo (la
decisión de activarlo en este caso específico). S_BM = 0.51: la
mitad de la responsabilidad de BM es sistémica (cualquier
banco con un mecanismo similar lo habría activado) y la mitad
es idiosincrática (el diseño específico del mecanismo de BM y
su aplicación sin verificación adicional).

### II. Derivación de α para cada nodo con
evidencia textual
α_ECP = 0.11. La frase «ojalá no haya más sorpresas» en el
mensaje de PSM a Altamirano es la evidencia más directa de
α_ECP disponible en el expediente — no porque sea un
mensaje de ECP, sino porque describe la posición de PSM
ante el riesgo de que ECP haya producido consecuencias
adicionales. La frase indica que ECP no ha producido ningún
reconocimiento documentado del acto ni ha reportado lo
ocurrido a PSM o a la FRO. Un reconocimiento habría
producido documentación. La ausencia de cualquier folio de
actuación interna de la FRO sobre ECP después del 22 de

Metrología Causal
mayo confirma: α_ECP = 0.11 (reconocimiento parcial de tipo
α₁ bajo).
α_PSM = 0.06. La frase «ojalá no haya más sorpresas» es
también la evidencia central para α_PSM. La frase tiene la
estructura exacta de Anteros reactivo en φ₂: reconocimiento
del riesgo sin integración del acto como propio («las sorpresas»
son externas a PSM, no son consecuencias de su propia
omisión). La desaparición sin documentación confirma α ≈ 0:
PSM no ha integrado su inacción como parte de lo que ella
produjo.
α_FRO = 0.03. El archivo de la denuncia VISITEL sin acción
es la señal más directa de α_FRO. La FRO tenía información
(la denuncia) que describía exactamente el mecanismo del
daño causado por un agente suyo. No actuar sobre esa
información es la forma más directa de no integrar el acto
como propio. α_FRO = 0.03: el nivel más bajo del sistema,
consistente con una institución que señalaría sus protocolos
declarados como evidencia de que no cometió ningún acto.
α_BM = 0.24. BM tiene el mayor α del sistema. La fotografía
del estatus 25 es evidencia de que BM aplicó el mecanismo,
pero no evidencia directa de que BM reconoce el daño que ese
mecanismo produjo. Sin embargo, la existencia del mecanismo
de estatus 25 como política documentada de BM implica que
BM ha integrado en sus procedimientos la posibilidad de
producir ese tipo de consecuencia sobre sus clientes — lo que
es una forma tenue de integración del acto como parte del
diseño del sistema. α_BM = 0.24.

### III. El vector R* completo del caso Altamirano

Metrología Causal
Nod R* Ran R*_n S α Δ Δ /
o (midp go eta = Δ_to
oint) R* R* tal
×
(1−
α)
ECP 0.308 [0.2 0.283 0. 0. 0.2 30.4
71, 08 11 74 %
0.34
4]
PSM 0.118 [0.0 0.031 0. 0. 0.1 12.3
98, 74 06 11 %
0.13
9]
FRO 0.381 [0.3 0.362 0. 0. 0.3 41.0
49, 05 03 70 %
0.41
3]
BM 0.193 [0.1 0.095 0. 0. 0.1 16.3
68, 51 24 47 %
0.21
8]
TOT 1.000 — 0.771 — — 0.9 100.
AL 02 0%

Metrología Causal
Lectura inmediata del vector. FRO tiene el mayor R* (0.381) y
el mayor R*_neta (0.362) — es el nodo más central
causalmente y el que tiene la menor fracción sistémica. ECP
tiene el segundo mayor R*_neta (0.283) a pesar de no ser el de
mayor R* bruto. BM tiene el tercer R* pero el segundo
R*_neta más bajo (0.095) porque S_BM = 0.51 descuenta la
mitad de su responsabilidad como sistémica. PSM tiene el
menor R*_neta (0.031) porque S_PSM = 0.74 descuenta el
74% de su responsabilidad.
Δ_total = 0.902: el 90.2% del daño no ha sido reconocido por
ningún nodo del sistema. De ese total, el 41.0% corresponde
a FRO — la institución que diseñó el campo y que tiene el
mayor déficit de asunción. Esa distribución de Δ es la
información más operativa del expediente: dice dónde está
concentrado el trabajo pendiente de integración.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·6
Serie I: Contabilidad Ontológica
La distribución del D_total, la cuantificación del daño económico
diferido y el estatus 25

### I. La distribución del D_total entre nodos
En la Serie I, el análisis describe la estructura causal del daño
sin propósito atributivo. La pregunta es: ¿qué ocurrió y quién
contribuyó causalmente en qué proporción? La distribución
del D_total entre los cuatro nodos sigue directamente de R*:
FRO aportó el 38.1% de la contribución causal total al daño,
ECP el 30.8%, BM el 19.3% y PSM el 11.8%.
La descripción narrativa de la distribución: el resultado de
doce meses sin empleo con daño económico de $336,000–
$540,000 fue producido causalmente en mayor proporción
por el diseño institucional de la FRO (que creó el campo sin
controles), seguido por el acto detonante de ECP (que habilitó
la suplantación bancaria), seguido por el mecanismo
estructural de BM (que convirtió la señal de irregularidad en
bloqueo persistente), seguido por el encubrimiento de PSM
(que prolongó el proceso sin corrección). Esta descripción es
la comprensión causal del caso — no es todavía una atribución
formal de responsabilidad.

Metrología Causal

### II. La cuantificación del daño económico
diferido
El daño económico diferido es calculable desde los datos del
caso. Altamirano llevaba más de doce meses sin empleo en su
sector de especialización al momento del análisis. Su ingreso
previo a la rescisión era consistente con el mercado para un
gerente de nivel medio en el sector financiero en la región. El
rango de pérdida de ingreso se estima en $336,000–$540,000
pesos, calculado como el rango entre el percentil 25 y el
percentil 75 del salario mensual para el perfil correspondiente,
multiplicado por doce meses.
La distribución del daño económico diferido entre nodos sigue
la misma distribución de R*. La fracción causalmente
atribuible a FRO: $128,016–$205,200 pesos (38.1% del total).
La fracción atribuible a ECP: $103,488–$166,320 pesos
(30.8%). La fracción atribuible a BM: $64,848–$104,220 pesos
(19.3%). La fracción atribuible a PSM: $39,648–$63,720 pesos
(11.8%). Estas fracciones no son el monto de reparación que
cada nodo debe pagar — son la descripción de cuánto del
daño fluye causalmente a través de cada nodo.
El estatus 25 como la arista que produce daño persistente: la
propiedad más importante del daño económico diferido es que
no requiere acción continua de ningún nodo para mantenerse.
El estatus 25 de BM es estructuralmente persistente: una vez
aplicado, se mantiene hasta que BM lo levante activamente.
Esa persistencia estructura es la razón por la que el daño llega
a doce meses: no es que ECP, PSM o FRO hayan hecho algo
adicional en esos doce meses. Es que BM aplicó un
mecanismo que produce daño continuo sin necesidad de
actuación continua.

Metrología Causal

### III. Lo que la Serie I produce y lo que no
produce
La Serie I produce la comprensión del caso: qué campo causal
produjo el daño, cuánto contribuyó cada nodo y a través de
qué mecanismos. Esta comprensión es directamente útil para
el diseño de intervenciones preventivas. Si la FRO implementa
sus protocolos declarados con IIC alto, la próxima ECP en el
sistema tendrá que registrar la visita — lo que inhibiría la
conversación no registrada. Si BM implementa un mecanismo
de verificación adicional ante suplantaciones, el mecanismo
del estatus 25 quedaría condicionado.
La Serie I no produce la imputación formal: no establece que
FRO deba responder ante ningún foro por $128,016–
$205,200 pesos. Esa pregunta requiere la Serie III, con los
estándares adversariales que la Serie I no tiene. La confusión
entre las dos preguntas —cuánto causó FRO (Serie I) y cuánto
debe FRO (Serie III)— es el error más frecuente en la lectura
del expediente.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·7
Serie II: Compliance Causal
IIC_FRO = 0.017, el fraude annona formalizado y el ajuste
debitor en tres componentes

### I. El cálculo del IIC_FRO
La Serie II evalúa la brecha entre los protocolos declarados de
la FRO y su operación real sobre los tres protocolos
directamente relevantes para el caso.
Protocolo 1: registro obligatorio de visitas de imputados y
personas relacionadas con carpetas activas. Corr (declarado₁,
observable₁): la FRO declara que toda visita a agentes del MP
en relación con carpetas activas debe registrarse con folio,
hora y firma del visitante. Observable: la conversación del 15
de mayo entre ECP y Altamirano (o su representante) no tiene
registro en el sistema. c₁ = 0.00.
Protocolo 2: confidencialidad de carpetas de investigación y
protocolo de entrega de información. Corr (declarado₂,
observable₂): la FRO declara que los documentos de carpetas
activas no pueden entregarse a terceros sin autorización del
MP titular del caso y registro documentado. Observable: los

Metrología Causal
documentos de la carpeta de Altamirano llegaron a Garmendia
Leal sin ningún registro de autorización. c₂ = 0.00.
Protocolo 3: mecanismo VISITEL de atención de denuncias
por irregularidades. Corr (declarado₃, observable₃): la FRO
declara que las denuncias por irregularidades de agentes
recibidas a través de VISITEL tienen plazo de respuesta
documentada de 15 días hábiles, con notificación al
denunciante. Observable: la denuncia de Altamirano del 22 de
mayo recibió folio, pero no produjo ninguna acción
documentada ni notificación en el período de análisis. c₃ =
0.05 (el folio fue otorgado, lo que satisface el 5% del protocolo
de VISITEL).
IIC_FRO = (c₁ + c₂ + c₃) / 3 = (0.00 + 0.00 + 0.05) / 3 =
0.017.
IIC_FRO = 0.017 — interpretación
La FRO opera al 1.7% de sus propios protocolos declarados
sobre los tres criterios más básicos del proceso penal en este
caso.
El campo real que la FRO produce diverge al 98.3% del
campo que sus propios protocolos declaran que debería ser.
Ese campo real es la condición de posibilidad de los actos de
ECP y de la inacción de PSM.
El IIC no dice que la FRO quiso producir el daño. Dice que
la FRO produjo un campo que hace posible el daño de
manera sistemática, con independencia de la intención de
cualquier agente individual.

### II. El fraude annona de la FRO formalizado

Metrología Causal
El contrato fiscal de la FRO con el sistema jurídico tiene la
siguiente estructura. Capital recaudado: la FRO recibe el
capital de legitimidad del proceso penal — la obediencia de los
ciudadanos al proceso, la colaboración de los imputados con
las investigaciones, la credibilidad institucional que hace
posible que las denuncias tengan sentido para quienes las
presentan. Altamirano colaboró con la FRO (respondió a
comunicaciones, presentó la denuncia VISITEL, aportó
información). Esa colaboración es el capital que Altamirano
cedió a la FRO en el contexto del contrato fiscal.
Condiciones prometidas: a cambio de ese capital, la FRO
prometió las condiciones del proceso penal justo:
confidencialidad de la información, registro de las visitas,
atención de las denuncias por irregularidades. Esas
condiciones están en los protocolos declarados de la FRO y
en el marco constitucional del proceso penal.
La brecha: la FRO recaudó el capital (la colaboración de
Altamirano) pero no entregó las condiciones prometidas. IIC
= 0.017 sobre los tres protocolos más básicos. La FRO
incumplió el contrato fiscal al 98.3%.
La formalización: Fraude_annona_FRO = R*_FRO × (1 −
α_FRO) × (1 − IIC_FRO) = 0.381 × 0.97 × 0.983 = 0.381 ×
0.954 = 0.364. El fraude annona de la FRO en el caso
Altamirano es de 0.364 sobre 1.000 — el 36.4% del daño total
es fraude annona formalizado de la FRO: responsabilidad
causal alta, reconocimiento mínimo, campo real radicalmente
divergente del declarado.

### III. El ajuste debitor en tres componentes
El ajuste debitor de la FRO en la Serie II tiene tres
componentes. El primer componente es estructural:

Metrología Causal
implementar los protocolos declarados con IIC operativo. El
protocolo de registro de visitas (c₁ = 0.00 → c₁ = 1.00), el
protocolo de confidencialidad de carpetas (c₂ = 0.00 → c₂ =
1.00) y el mecanismo VISITEL con respuesta documentada
(c₃ = 0.05 → c₃ = 1.00). Este componente cierra la brecha de
diseño que hizo posible los actos de ECP y PSM.
El segundo componente es procesal: actuar sobre la denuncia
VISITEL de Altamirano. El folio existe; la acción no. La
actuación sobre la denuncia es el componente que cerraría la
Capa 2 del daño (el daño procesal prolongado) y que reduciría
el Δ_FRO en la fracción correspondiente a la omisión de PSM.
Este componente tiene un límite temporal: la corrección
procesal es posible mientras la carpeta de investigación esté
activa.
El tercer componente es reparatorio: la coordinación con BM
para el levantamiento del estatus 25 en el contrato
80314809399 de Altamirano. Este componente es el que más
directamente reduce el daño económico diferido en curso —
el único mecanismo que puede detener el daño persistente del
estatus 25 es que BM lo levante, y ese levantamiento requiere
que la FRO confirme a BM que la señal de irregularidad que
originó el estatus 25 fue producto de un acto no autorizado de
un agente de la FRO.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·8
Serie III: Imputación Causal
Análisis de sensibilidad en tres escenarios y Declaración A

### I. El análisis de sensibilidad: los tres escenarios
El análisis de sensibilidad del caso Altamirano explora el
hipercubo de siete dimensiones definido por los rangos de las
siete aristas de la hoja de calibración. Los puntos de quiebre
del ranking se concentran exclusivamente en la arista
ECP→BM (rango [0.50, 0.85]), que es la única arista con rango
suficientemente amplio para producir cambios en la
distribución de R* cuando toma sus valores extremos.
Los tres escenarios de referencia del análisis de sensibilidad
son: el escenario central (midpoints de todos los rangos:
w_ECP→BM = 0.675), el escenario favorable a ECP (todos
los rangos en dirección de reducir R*_ECP: w_ECP→BM =
0.50, demás pesos en su valor mínimo), y el escenario
desfavorable a ECP (todos los rangos en dirección de
aumentar R*_ECP: w_ECP→BM = 0.85, demás pesos en su
valor máximo).

Metrología Causal
Parámetro Escenario Escenario Escenario
central favorable a desfavorable
ECP a ECP
w_ECP→BM 0.675 0.500 0.850
w_FRO→ECP 0.600 0.450 0.750
w_FRO→PSM 0.550 0.400 0.700
w_FRO→BM 0.450 0.300 0.600
R*_FRO 0.381 0.349 0.413
R*_ECP 0.308 0.271 0.344
R*_BM 0.193 0.168 0.218
R*_PSM 0.118 0.098 0.139
Ranking FRO > FRO > FRO > ECP
ECP > BM ECP > BM > BM > PSM
> PSM > PSM

Metrología Causal

### II. La estabilidad del ranking en todo el
hipercubo
El ranking FRO > ECP > BM > PSM es estable en los tres
escenarios de referencia y, como demuestra la exploración del
hipercubo, en todo el espacio de parámetros definido por los
rangos de la hoja de calibración. Aun en el escenario más
favorable a ECP — donde todos los pesos están en su valor
mínimo y la arista ECP→BM está en 0.50 — FRO mantiene
el primer lugar (R*_FRO = 0.349 > R*_ECP = 0.271). Aun
en el escenario más desfavorable a FRO — donde todos los
pesos están en su valor máximo — la diferencia entre FRO y
ECP se mantiene (R*_FRO = 0.413 > R*_ECP = 0.344).
La razón de la estabilidad: el ranking de FRO sobre ECP
descansa sobre una propiedad estructural del grafo que
ninguna variación de los pesos dentro de sus rangos plausibles
puede deshacer. FRO influye sobre ECP, PSM y BM
directamente y sobre D a través de esos tres nodos. ECP
influye sobre BM y a través de BM sobre D, pero no influye
sobre PSM ni sobre FRO de manera directa. La estructura
topológica del grafo hace que FRO sea más central que ECP
en el eigenvector con independencia de la intensidad específica
de cada influencia dentro de los rangos plausibles.

### III. La Declaración A del caso Altamirano
La Declaración A del expediente Altamirano puede formularse
de la siguiente manera:
DECLARACIÓN A

Metrología Causal
Con cualquier interpretación razonable de la evidencia
disponible — incluyendo los supuestos más extremos
dentro del rango plausible de cada peso del grafo causal
— la Fiscalía Regional de Occidente (FRO) tiene mayor
responsabilidad causal en el daño a Rodrigo Altamirano
Vega que cualquier otro actor del sistema analizado.
Para impugnar esta Declaración, la contraparte debe
demostrar que existe algún valor de algún peso de las
siete aristas del grafo que sea consistente con la
evidencia disponible y que, bajo ese valor, la FRO ya no
es el nodo de mayor responsabilidad causal. El único
punto de quiebre identificado en el análisis de
sensibilidad — en el que ECP podría desplazar a FRO
del primer lugar — requeriría que la arista ECP→BM
tuviera un peso superior a 0.97, lo que es inconsistente
con cualquier interpretación razonable de la evidencia
disponible.
La Declaración A no afirma que ECP, PSM y BM no son
responsables. Afirma que FRO tiene mayor responsabilidad
causal que cualquier otro nodo. Los tres nodos restantes tienen
R* positivo; sus responsabilidades causales son reales. El
ranking no dice que los últimos en el ranking no respondan —
dice que responden en proporciones distintas, siendo FRO el
que responde en mayor proporción.

Metrología Causal
CASO DE CIERRE · El expediente Altamirano
Capítulo C·9
Lectura integrada del expediente
Las consistencias confirmatorias, lo que el caso responde y la
diferencia entre el criterio del dolo y el criterio causal

### I. Las tres consistencias que confirman el
análisis
La primera consistencia confirmatoria es la S–Hijo para todos
los nodos. S_ECP = 0.08 es consistente con la firma de
Fobos-preventivo (operación para producir invisibilidad del
acto): un actor en Fobos-preventivo tiene S bajo porque la
operación para producir invisibilidad requiere su v_t específica
— otro actor con diferente disposición no habría operado para
producir invisibilidad activamente. S_PSM = 0.74 es
consistente con Fobos estructural + campo disfuncional
(cualquier agente en ese campo con esa señal de amenaza
habría producido la misma inacción). S_FRO = 0.05 es
consistente con el diseñador del campo. S_BM = 0.51 es
consistente con un actor que opera un mecanismo sistémico
diseñado institucionalmente. Las cuatro derivaciones de S son
coherentes con las localizaciones de la Taxonomía.
La segunda consistencia es IIC–Δ. IIC_FRO = 0.017 y
Δ_FRO = 0.370 (el mayor Δ del sistema). La institución que

Metrología Causal
opera al 1.7% de sus protocolos declarados tiene el mayor
déficit de asunción del sistema: no ha reconocido casi nada de
su contribución causal al daño. Esta coherencia no es circular
— proviene de instrumentos distintos (el IIC se calcula sobre
los protocolos declarados; α se infiere desde la ausencia de
actuación documentada sobre la denuncia VISITEL). Los dos
instrumentos coinciden en señalar a FRO como el nodo de
mayor distancia entre lo que causó y lo que reconoció.
La tercera consistencia es temporal. La coincidencia de cinco
días entre la conversación del 15 de mayo y la suplantación del
20 de mayo justifica el rango alto de la arista ECP→BM ([0.50,
0.85]). La rapidez del mecanismo (cinco días) es inconsistente
con una explicación alternativa que no involucre la
información de la carpeta: para que Garmendia Leal obtuviera
los datos del contrato de Altamirano por otra vía en cinco días,
habría necesitado acceso a sistemas bancarios internos o a
información no pública. La coincidencia temporal es la firma
estructural de la arista — su evidencia más sólida.

### II. Las preguntas que el expediente puede y no
puede responder
El expediente puede responder: quién fue el factor causal de
mayor peso en el resultado (FRO, con Declaración A). En qué
proporción contribuyó cada nodo (38.1%, 30.8%, 19.3%,
11.8%). Cuánto de esa responsabilidad es idiosincrática
(R*_neta del diseñador) y cuánto sistémica. Cuál es el déficit
total de asunción del sistema (Δ_total = 0.902). Qué medidas
concretas reduciría la probabilidad de que el mismo sistema
cause el mismo resultado en el futuro (el ajuste debitor de la
Serie II).

Metrología Causal
El expediente no puede responder: si la conducta de FRO,
ECP, PSM o BM constituyó un delito específico en el
ordenamiento jurídico mexicano — eso requiere el análisis de
los tipos penales aplicables y está fuera del alcance del análisis
causal. Si Altamirano «merece» una reparación de $X — la
valoración del mérito de la reparación requiere criterios
normativos. Si ECP actuó con el dolo que el tipo penal
eventualmente aplicable requiere — el análisis causal establece
R*, no el estado mental del actor. Si PSM habría actuado de
manera diferente en otro campo institucional — los
contrafácticos sobre otros campos requieren construir un
grafo diferente con supuestos hipotéticos.

### III. Lo que el caso demuestra sobre el sistema:
dolo vs. criterio causal
El caso Altamirano es el ejemplo más nítido disponible de la
diferencia entre el criterio del dolo y el criterio causal en la
práctica. El criterio del dolo pregunta: ¿quién quiso producir
el daño? La respuesta — si el sistema funciona como suele
funcionar — sería ECP: el agente que hizo el acto más visible
y que presumiblemente tenía el motivo más directo. FRO
puede señalar sus propios protocolos como evidencia de que
no quiso producir el daño. PSM puede señalar que solo
cumplía con el ritmo habitual del sistema. BM puede señalar
que solo aplicó sus propios procedimientos de seguridad.
El criterio causal pregunta: ¿quién fue el factor sine qua non
de mayor centralidad en el daño? La respuesta es FRO. No
porque FRO haya querido el daño — el sistema no puede
establecer eso y no lo necesita. Sino porque el campo que FRO
diseñó (o no diseñó) con IIC = 0.017 es la condición
estructural que hizo posibles los actos de ECP, el
encubrimiento de PSM y el daño persistente de BM. Sin ese

Metrología Causal
campo específico, el resultado D no se habría producido de
esa forma específica. FRO es condición necesaria del daño con
la mayor centralidad causal del sistema.
La diferencia práctica: bajo el criterio del dolo, el sistema
jurídico tendría dificultad para establecer la responsabilidad de
la FRO como institución porque ningún agente individual de
la FRO puede ser identificado como teniendo el dolo de dañar
a Altamirano. ECP puede tener dolo. La FRO como
institución no tiene un agente individual que quiso el daño y
que pueda ser identificado. Bajo el criterio causal, la FRO tiene
la mayor R* del sistema con Declaración A y el IIC más bajo
— lo que establece que el campo real que produjo es
radicalmente distinto del campo que declaró producir, y que
ese campo real fue la contribución causal más importante al
daño.
El criterio del dolo hace invisible exactamente lo que más
importa: el diseño del campo. La FRO no dañó a
Altamirano porque algún funcionario lo quisiera. Lo dañó
porque durante años construyó un campo sin protocolos
efectivos, y ese campo hizo posible que un agente actuara sin
rastro y que otro encubriera sin consecuencias. El criterio
causal ve eso con precisión. El criterio del dolo lo convierte en
nadie.
Notas al caso integrado
1 La Declaración A del caso Altamirano descansa sobre una propiedad
topológica del grafo que es independiente de la calibración de los pesos:
FRO es el único nodo que influye directamente sobre los otros tres
nodos del sistema (ECP, PSM, BM) a través de su diseño del campo.
Esa posición topológica garantiza que FRO tendrá mayor eigenvector
que cualquier otro nodo en cualquier grafo donde esas cuatro aristas
existan con pesos positivos, con independencia de su magnitud exacta.
La Declaración A no es solo una propiedad del análisis de sensibilidad
— es una propiedad de la estructura del grafo que puede demostrarse
analíticamente.

Metrología Causal
2 El cálculo del daño económico diferido ($336,000–$540,000 pesos)
usa el rango salarial de gerencia media en el sector financiero de la región
en el período de análisis. El rango refleja la variabilidad del mercado para
ese perfil; el punto central ($438,000 pesos) es la estimación de la pérdida
de ingreso más probable. La distribución de ese daño entre nodos según
R* es una aplicación directa del principio de la Contabilidad Ontológica:
la fracción del daño que fluye causalmente a través de cada nodo es
proporcional a R*.
3 El estatus 25 como mecanismo de daño persistente ilustra una
propiedad general de los daños producidos por diseños institucionales
deficientes: una vez activados, no requieren acción continua para
mantenerse. Los sistemas de seguridad bancaria, los registros de
antecedentes laborales, los sistemas de información crediticia — todos
tienen mecanismos que, una vez activados por señales de irregularidad,
producen daño persistente hasta que se activa un mecanismo de
corrección. Esos mecanismos de corrección son parte del diseño
institucional; cuando no existen o no funcionan (IIC bajo), el daño se
perpetúa con independencia de que ningún actor lo desee activamente.

Metrología Causal
