INTRODUCCIÓN
El lenguaje universal del análisis causal
Cómo leer el sistema sin importar el dominio del caso

### I. El problema que esta introducción resuelve
El mediador que domina el Volumen I tiene un instrumento
preciso y un problema concreto: la primera vez que abre un
expediente real —un caso jurídico, una auditoría institucional, un
caso clínico, un análisis de política pública— se enfrenta a un
vocabulario que el sistema no habló. El abogado tiene nexo causal
y dolo. El médico tiene factor etiológico y negligencia. El
economista tiene variable instrumental y externalidad. El clínico
tiene patrón de conducta y déficit de mentalización. Cada
disciplina construyó durante siglos el lenguaje con el que describe
lo mismo: quién fue condición necesaria de qué resultado, en qué
proporción, con qué grado de asunción.
El sistema tiene la respuesta para todos ellos. La metrología
causal no es una ciencia jurídica, ni médica, ni económica, ni
psicológica: opera en el nivel de la estructura causal, que es
invariante al dominio [Vol.I · Cap. I·3]. Pero tener la respuesta en
un lenguaje que el interlocutor no reconoce produce el resultado
más costoso en cualquier práctica: el mediador que sabe lo que hay

Metrología Causal · Vol. II
que calcular no puede comunicarlo, y el destinatario que necesita
el análisis no puede usarlo.
Esta introducción resuelve ese problema una sola vez. No lo
resuelve para cada dominio por separado —eso produciría setenta
y ocho glosarios distintos para los setenta y ocho capítulos de la
Taxonomía General de Aplicaciones, que es exactamente lo que el
sistema no puede permitirse. Lo resuelve en el nivel de abstracción
correcto: el nivel donde los conceptos del sistema y los conceptos
de cada disciplina son reconocibles como instancias del mismo
operador.
Lo que esta introducción produce es un glosario operativo
de nueve conceptos con su tabla de equivalencias disciplinares, y
una clasificación de los cinco tipos de pregunta causal que
aparecen en todos los dominios. Con esos dos instrumentos, el
mediador puede entrar a cualquier caso en cualquier dominio y
comenzar a trabajar sin perder un grado de rigor formal.

### II. Lo que este glosario es y lo que no es
El glosario de esta introducción no es un glosario filosófico.
No define los conceptos en su nivel ontológico ni repite las
derivaciones formales del Volumen I. El lector que necesita saber
por qué el eigenvector es la medida correcta de la responsabilidad
causal tiene el Capítulo IV·2 de este volumen y la Parte II del
Volumen I. El lector que necesita saber qué es φ(cid:0) en su estructura
formal tiene la Axiomatización del Sistema de la Doble Mediación.
Este glosario asume que el mediador ya sabe qué son los conceptos
y responde una pregunta diferente: cómo se llaman en cada
dominio y cómo se operan.
La distinción es más importante de lo que parece. Un
glosario filosófico dice qué es algo. Un glosario operativo dice qué

Metrología Causal · Vol. II
hacer con algo cuando el caso lo requiere. Este es un glosario
operativo: cada entrada define el concepto en términos de la
operación que produce, no de la ontología que lo funda.
La segunda restricción es igualmente importante. Este
glosario no es exhaustivo sobre ninguna disciplina. Un abogado
penalista encontrará que la columna "Derecho" simplifica
vocabulario que en la práctica forense tiene matices importantes.
Esa simplificación es deliberada: el propósito no es que el sistema
hable el idioma de cada disciplina con toda su riqueza técnica
interna, sino que el mediador pueda identificar en el vocabulario
de su interlocutor el concepto del sistema que está siendo
descripto. El glosario es una tabla de traducción, no un tratado
disciplinar.

### III. El glosario operativo universal
Los nueve conceptos que siguen son los únicos que el
mediador necesita traducir para operar el sistema en cualquier
dominio. El resto del vocabulario —eigenvector, método de
potencias, grafo de Markov, convergencia, robustez— es
vocabulario técnico del sistema que el mediador usa internamente
y que no necesita traducirse al dominio del interlocutor. El análisis
puede entregarse completamente en el idioma de la disciplina del
destinatario; la maquinaria que lo produce es del sistema.
Concepto 1 · Nodo
Definición operativa: cualquier entidad —persona,
institución, norma, sistema, algoritmo, proceso— que tenía
capacidad de influir en el resultado analizado y que tomó
decisiones o generó condiciones que actuaron sobre el
grafo causal.

Metrología Causal · Vol. II
La condición de nodo no requiere intención ni conciencia: un protocolo
institucional mal diseñado es un nodo si su operación fue condición
necesaria de parte del resultado. Un algoritmo de scoring es un nodo si su
función fue condición de parte del daño.
Dominio Cómo se llama Lo que el mediador busca
el nodo
Derecho Sujeto, parte, Quien tenía capacidad jurídica de
penal / civil imputado, actuar y cuya actuación fue
demandado, condición del daño
tercero
Medicina / Factor etiológico, El factor cuya eliminación
Salud pública agente causal, contrafactual habría prevenido o
actor institucional modificado el resultado clínico
Economía / Agente, actor, El agente cuya decisión alteró la
Política variable trayectoria del sistema más allá del
pública estructural, ruido esperado
institución
Psicología Actor, figura La entidad cuyo patrón de
clínica vincular, sistema conducta fue condición del
familiar, patrón de respuesta del sujeto
institución
Ingeniería / Componente, El elemento cuya falla o decisión
Tecnología subsistema, fue condición estructural de la
equipo diseñador, falla sistémica
operador
Auditoría Área, directivo, La unidad de decisión cuya
institucional comité, protocolo, actuación fue condición de la
incentivo desviación auditada
Concepto 2 · Arista y peso

Metrología Causal · Vol. II
Definición operativa: la relación de influencia causal entre
dos nodos, con una dirección —quién influye sobre
quién— y un peso —con qué intensidad esa influencia
contribuye al resultado. Las aristas no son correlaciones ni
relaciones de precedencia temporal: son relaciones de
condición necesaria estructural verificadas con evidencia.
El peso de cada arista se expresa como un rango [a_ij, b_ij] calibrado
según el nivel de evidencia disponible. El mediador nunca asigna un peso
puntual arbitrario: asigna el rango que la evidencia puede sostener. El
midpoint del rango es el valor de cálculo; la amplitud determina la
robustez del resultado [Vol.I · Cap. VI·2].
Dominio Cómo se llama Cómo se calibra el peso
la arista
Derecho Nexo causal, Grado en que la actuación del
relación de nodo fue condición sine qua non
causalidad, verificada en el expediente
vínculo jurídico
Medicina Relación Fuerza de la evidencia clínica o
etiológica, epidemiológica que sostiene la
mecanismo causal, relación
vía de acción
Economía Transmisión, Magnitud estimada del efecto con
canal de impacto, su intervalo de confianza o rango
efecto estructural de sensibilidad
Psicología Influencia, patrón Frecuencia, intensidad y
vincular, consistencia temporal de la
condicionamiento influencia observada
Ingeniería Dependencia Probabilidad de propagación de
funcional, falla bajo condiciones operativas
propagación de documentadas
falla, interfaz

Metrología Causal · Vol. II
Dominio Cómo se llama Cómo se calibra el peso
la arista
Auditoría Línea de reporte, Grado en que la decisión del nodo
dependencia de superior condicionó la del nodo
decisión, flujo de subordinado
información
Concepto 3 · R* (peso causal estructural)
Definición operativa: la fracción del resultado total que se
explica por la posición estructural del nodo en el grafo
causal. R* no mide la intención del nodo ni su visibilidad
documental: mide cuánto del resultado desaparecería si el
nodo fuera eliminado del grafo y reemplazado por el nodo
nulo. Es el eigenvector principal normalizado de la matriz
de pesos W.
La propiedad más contraintuitiva de R* —que un nodo puede tener R*
alto, aunque esté poco documentado— es una consecuencia matemática
del eigenvector, no una hipótesis adicional. El nodo que influye sobre
muchos nodos de alto R* hereda centralidad, aunque sus aristas directas
al nodo sumidero sean débiles [Vol.I · Cap. III·2].
Dominio Cómo se llama Qué comunica al entregar
R* R*
Derecho Grado de "Este nodo explica el X% del
penal responsabilidad resultado dañoso
causal, independientemente de su
participación intención declarada"
estructural
Derecho civil Contribución "La distribución que satisface los
causal cuatro axiomas de
proporcional, proporcionalidad causal"

Metrología Causal · Vol. II
Dominio Cómo se llama Qué comunica al entregar
R* R*
cuota de
responsabilidad
Medicina Peso etiológico, "Este factor explica el X% del
fracción atribuible, resultado clínico en este sistema
contribución al específico"
resultado
Economía Atribución de "Esta decisión explica el X% de la
impacto, variación observada en el
contribución indicador"
estructural al
resultado
Psicología Peso causal del "Este factor vincular explica el
clínica factor, X% del patrón de conducta en
contribución al este sistema"
patrón
Auditoría Responsabilidad "Esta unidad concentra el X% de
estructural, peso la responsabilidad causal de la
en la distribución desviación"
del riesgo
Concepto 4 · S (sustituibilidad)
Definición operativa: la probabilidad de que cualquier otro
nodo con el mismo perfil en la misma posición estructural
hubiera producido el mismo resultado. S = 1.00 significa
que la conducta era completamente predecible desde el
campo: cualquier otro en esa posición habría hecho lo
mismo. S = 0.00 significa que la conducta era
completamente idiosincrática: ningún otro la habría
producido.

Metrología Causal · Vol. II
S no es un juicio moral sobre el nodo. Es una descripción estructural de
cuánto del resultado es atribuible al actor específico versus al campo que
lo contenía. Los tres criterios universales de calibración son: (1) existencia
de alternativa documentada, (2) conformidad con la norma o protocolo
del dominio, (3) replicabilidad ante un par equivalente en la misma
posición.
Dominio Cómo se llama Los tres criterios universales
S
Derecho Presión sistémica, Alternativa documentada +
estándar del conformidad con la norma +
sector, práctica replicabilidad ante par
habitual
Medicina Protocolo Guía clínica existente + desviación
estándar, práctica documentada + conducta de pares
clínica habitual, equivalentes
estándar de
cuidado
Economía Incentivo Alternativa viable + cumplimiento
estructural, regla de la regla del sector +
de decisión comparación con agentes
sectorial, equivalentes
restricción
institucional
Psicología Condicionamiento Historia de refuerzo documentada
heredado, patrón + respuesta alternativa disponible
vincular + conducta de pares
aprendido,
presión del
contexto
Auditoría Incentivo de Diseño del incentivo que generó la
diseño, presión de conducta + alternativas disponibles
meta, restricción + unidades equivalentes
de protocolo

Metrología Causal · Vol. II
Concepto 5 · α (asunción)
Definición operativa: la fracción de R* que el nodo integró
como propia mediante acciones verificables orientadas a
producir, modificar, o mitigar el resultado. α no mide
intención ni declaración: mide conducta verificable con
evidencia. Un nodo que declara alta responsabilidad, pero
no tomó ninguna acción orientada a modificar el resultado
tiene α bajo.
Los tres criterios universales de α: conocimiento —el nodo tenía
información suficiente para prever el resultado—; acción —tomó acciones
verificables orientadas a modificarlo—; oportunidad —tuvo momentos
concretos donde podía haber actuado diferente. Cada criterio que falla
pone un techo a α.
Dominio Cómo se llama Qué evidencia la calibra
α
Derecho Diligencia debida, Acciones preventivas
buena fe, documentadas + informes de
cumplimiento del riesgo + medidas correctivas
deber de cuidado tomadas
Medicina Adhesión al Historia clínica + órdenes
protocolo, médicas + registros de monitoreo
diligencia clínica, + acciones ante señal de alarma
manejo adecuado
Economía Cumplimiento Registros de implementación +
regulatorio, indicadores de cumplimiento +
implementación respuesta ante señales de alerta
de política,
capacidad de
respuesta
Psicología Responsabilidad Conducta observable de
clínica integrada, reconocimiento + acciones de

Metrología Causal · Vol. II
Dominio Cómo se llama Qué evidencia la calibra
α
reconocimiento reparación + cambio de patrón
del acto, capacidad verificable
de rectificación
Auditoría Cumplimiento del Evidencia de aplicación del
protocolo control + documentación de
declarado, excepciones + acciones
ejecución del correctivas
control interno
Conceptos 6 a 9 · Los cuatro conceptos derivados
Los cuatro conceptos que siguen se derivan formalmente
del Teorema de la Responsabilidad Causal Proporcional
[Vol.II · Cap. IV·2]. No son hipótesis adicionales: son
consecuencias necesarias de R*, S y α. Se presentan aquí en
su forma operativa; la demostración formal está en la Parte
IV de este volumen.
Concepto Definici Equivalen Equivale Equivalen
ón te en nte en te en
operativ derecho medicin auditoría
a a
R*_neta = R* La Responsabil Fracción Responsabil
× (1−S) fracción idad atribuible idad
idiosincrá personal idiosincrát individual
tica del neta ica neta
peso excluyendo excluyend excluyendo
causal: presión o el incentivo de
cuánto sistémica estándar diseño
del de
resultado práctica

Metrología Causal · Vol. II
Concepto Definici Equivalen Equivale Equivalen
ón te en nte en te en
operativ derecho medicin auditoría
a a
es
atribuible
al actor
específic
o,
excluyen
do lo que
cualquier
otro en
esa
posición
también
habría
producid
o
Δ = R* × El déficit Incumplimi Déficit de Brecha de
(1−α) de ento de manejo, cumplimien
asunción: obligación brecha to entre
cuánto de cuidado, entre protocolo
del peso brecha de deber de declarado y
causal del diligencia cuidado y ejecutado
nodo no conducta
fue real
integrado
mediante
acción
verificabl
e. Δ > 0
indica
que el
nodo
causó
más de lo

Metrología Causal · Vol. II
Concepto Definici Equivalen Equivale Equivalen
ón te en nte en te en
operativ derecho medicin auditoría
a a
que
asumió
IIC (Índice de La Buena fe Calidad Integridad
Integridad congruen objetiva, del del control
Causal) cia entre coherencia protocolo interno,
lo que el entre , congruencia
nodo de declaración congruen entre diseño
diseño y conducta cia entre y operación
declaró guía
que declarada
producirí y práctica
a y lo que real
produjo
en
operació
n real.
IIC = 1
indica
congruen
cia total;
IIC = 0
indica
divergenc
ia total
Fraude El Incumplimi Negligenc Falla
annona = producto ento ia sistémica de
R*×(1−α)×(1 de alta agravado institucio control
−IIC) centralida por nal interno con
d causal, posición de agravada responsabili
baja garante por dad de
asunción posición diseño
y baja de diseño
congruen
cia: la

Metrología Causal · Vol. II
Concepto Definici Equivalen Equivale Equivalen
ón te en nte en te en
operativ derecho medicin auditoría
a a
posición
más grave
que el
sistema
puede
medir en
un nodo
de diseño
institucio
nal

### IV. Los cinco tipos de pregunta causal
Todos los casos en todos los dominios producen
exactamente uno de cinco tipos de pregunta causal. Identificar el
tipo antes de construir el grafo es la primera operación del
mediador porque el tipo de pregunta determina la serie del Método
Prometeo que el análisis requiere, el estándar de evidencia que
aplica, y la forma del documento que el análisis entrega.
La identificación del tipo no requiere conocer el dominio del
caso: requiere escuchar con precisión lo que el destinatario
necesita saber. Las preguntas de umbral que siguen son
universales.

Metrología Causal · Vol. II
Tipo La pregunta Serie Ejemplo
que el multidominio
destinatario
necesita
responder
1 · ¿Quién o qué I Derecho: ¿quién causó
Diagnóstico fue condición el daño y en qué
necesaria de fracción? · Medicina:
este resultado, ¿qué factor produjo el
y en qué resultado clínico? ·
proporción? Auditoría: ¿qué
decisión generó la
desviación?
2 · ¿El nodo de II Derecho: ¿la empresa
Compliance diseño operó cumplió su deber
en declarado? · Medicina:
conformidad ¿el hospital siguió el
con lo que protocolo? · Auditoría:
declaró que ¿la política se
haría? implementó como fue
diseñada?
3 · ¿Puede III Derecho: ¿resiste el
Imputación sostenerse la análisis ante el
atribución de tribunal? · Regulación:
responsabilidad ¿resiste ante el
ante regulador? · Medicina:
impugnación ¿resiste ante el comité
adversarial? de ética?
4 · ¿Qué rediseño I + II Derecho: ¿cómo
Prevención reduciría la rediseñar el protocolo
centralidad para evitar
causal de los reincidencia? ·
nodos críticos Medicina: ¿cómo
en sistemas rediseñar el estándar? ·
futuros? Institución: ¿cómo
rediseñar el incentivo?

Metrología Causal · Vol. II
Tipo La pregunta Serie Ejemplo
que el multidominio
destinatario
necesita
responder
5 · ¿Cómo I Psicología: ¿está
Seguimiento evoluciona la longitudinal cambiando el patrón
posición causal de conducta? ·
de un nodo a lo Medicina: ¿está
largo del respondiendo el
tiempo? paciente? · Política
pública: ¿está
mejorando el
indicador?
Los tipos 4 y 5 no estaban en el documento editorial original
del Volumen II. Se incorporan en esta edición porque el corpus
empírico de programas de intervención longitudinal —entre ellos
el Programa ECO documentado en el Apéndice A— demostró
que el sistema necesita protocolo explícito para preguntas
prospectivas y de seguimiento, no solo retrospectivas. La serie que
activan es la misma Serie I; lo que cambia es la orientación
temporal del grafo y el tipo de declaración que el análisis puede
producir.

### V. Cómo leer este volumen
El Volumen II no explica. Opera. Cada sección responde
exactamente una pregunta: ¿qué hace el mediador ahora? Nada que
esté explicado en el Volumen I se repite aquí: se referencia con la

Metrología Causal · Vol. II
notación [Vol.I · Cap. X·Y]. El mediador que necesita entender
por qué algo funciona sabe exactamente dónde ir. El mediador que
ya lo entiende y necesita saber qué hacer lo encontrará sin rodeo.
La Parte I establece el flujo de trabajo completo del
mediador desde la entrada del caso hasta la entrega del expediente.
La Parte II recorre el protocolo completo para cada tipo de análisis
simple. La Parte III establece el protocolo del análisis integrado
con las tres series sobre el mismo grafo. La Parte IV contiene la
demostración formal del Teorema de la Responsabilidad Causal
Proporcional y sus corolarios.
El Apéndice A contiene el protocolo de calibración empírica
del sistema desde programas de intervención longitudinal. El
Apéndice B contiene la tabla de equivalencias extendida por
dominio para los nueve conceptos del glosario de esta
introducción.
Si el lector necesita que este volumen le explique qué es R* o por
qué se usa el eigenvector, ese lector debe leer el Volumen I primero.
Si el lector sabe qué es R* y necesita saber cómo calcularlo paso a
paso con un caso delante, este volumen fue escrito para él.
La prueba de audiencia del Volumen II
Notas a la introducción
1 La invarianza al dominio del operador causal es demostrada en La
transformación formal (Cap. 1.2) y presupuesta en todos los capítulos
del Volumen I. Lo que esta introducción agrega no es la demostración
sino el protocolo de traducción que hace esa invarianza operativa en la
práctica del mediador.
2 Los setenta y ocho capítulos de la Taxonomía General de Aplicaciones
desarrollan cada dominio con sus firmas documentales específicas, sus

Metrología Causal · Vol. II
rutas hacia S, y sus estándares de evidencia propios. Esta introducción
no reemplaza esos capítulos: establece el lenguaje común que los hace
comparables entre sí.
3 La incorporación de los tipos 4 (Prevención) y 5 (Seguimiento) responde
a evidencia acumulada en el Programa ECO (Apéndice A) y en las
aplicaciones de la Taxonomía en dominios de política pública y
acompañamiento clínico. La clasificación original del documento
editorial contemplaba solo los tres tipos asociados a las tres series. La
evidencia de campo demostró que esa clasificación era incompleta.
4 El glosario de este volumen complementa el glosario del Volumen I.
Donde el Volumen I define los términos en su nivel ontológico y
matemático, este volumen los define en su nivel operativo y disciplinar.
Los dos glosarios son complementarios, no redundantes.

Metrología Causal · Vol. II

