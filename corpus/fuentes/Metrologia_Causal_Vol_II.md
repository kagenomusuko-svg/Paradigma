CENTRO MULTIDISCIPLINARIO MERIADOCK
Formación y Asesoría A.C.
R.F.C. CMM250808AC8
“La fuerza interior nos impulsa, un pequeño apoyo de los demás nos bendice”
Metrología Causal
——————
Vol II
Miguel Hilario Olvera Aguilar
Colección: Metrología Causal
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. ·
2026

Primera edición: 2026
© Centro Multidisciplinario Meriadock Formación y Asesoría A.C.,
2026
Todos los derechos reservados. Ninguna parte de esta publicación
puede ser reproducida, almacenada o transmitida en manera alguna ni
por ningún medio, ya sea eléctrico, químico, mecánico, óptico, de
grabación o de fotocopia, sin permiso previo del editor.
Metrología Causal: Vol II causal © 2026 by Miguel Hilario Olvera
Aguilar is licensed under CC BY-NC-ND 4.0. To view a copy of this
license, visit https://creativecommons.org/licenses/by-nc-nd/4.0/

Metrología Causal · Vol. II
METROLOGÍA CAUSAL · VOLUMEN II
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

## PARTE I · El flujo de trabajo del mediador

### Capítulo I·1
Cómo entra un caso al sistema
Los cinco tipos de pregunta causal y qué serie activan

### I. El primer acto del mediador
El mediador no comienza el análisis construyendo el grafo.
Comienza con una pregunta anterior al grafo: ¿qué necesita poder
decir el destinatario cuando este análisis termine? Esa pregunta no
es retórica. Es el dato que determina qué instrumento del sistema
se activa, bajo qué estándar de evidencia opera, y qué documentos
el expediente entrega. Un análisis bien construido sobre la
pregunta equivocada produce resultados técnicamente correctos
que el destinatario no puede usar.
El primer acto del mediador es, por tanto, la escucha. No la
escucha del relato del caso —eso vendrá después— sino la escucha
de la necesidad del destinatario. La pregunta que el mediador hace
antes de abrir el expediente es invariante al dominio: ¿qué tiene
que ser verdad al final para que este análisis le sirva? La respuesta
a esa pregunta identifica el tipo de pregunta causal que el caso
plantea. El tipo de pregunta determina todo lo demás.

Metrología Causal · Vol. II

### II. Los cinco tipos de pregunta y su identificación
Existen exactamente cinco tipos de pregunta causal que
aparecen en todos los dominios. Cada tipo tiene una pregunta de
umbral —la frase que el mediador escucha del destinatario— y un
producto de salida distinto. Identificar el tipo no requiere conocer
el expediente: requiere escuchar con precisión lo que el
destinatario formula.
Tipo La frase que el Lo que el destinatario
mediador necesita
escucha
1 · "Necesito saber Distribución de R* con
Diagnóstico quién causó esto y Declaración de robustez. El
en qué medida" análisis describe la estructura
causal del resultado específico
2 · "Necesito saber si IIC del nodo de diseño + ajuste
Compliance el diseño operó debitor. El análisis evalúa la
como fue congruencia entre el campo
declarado" declarado y el observable
3 · "Necesito sostener Declaración de nivel A, B, C, o D
Imputación esta atribución ante con reporte de sensibilidad. El
impugnación" análisis resiste el escrutinio
adversarial
4 · "Necesito saber Mapa de nodos críticos +
Prevención cómo evitar que hipótesis de rediseño. El análisis
esto se repita" orienta intervenciones
estructurales futuras
5 · "Necesito saber si Curva longitudinal de R* y α. El
Seguimiento la posición causal análisis registra la evolución del
está cambiando" grafo a lo largo del tiempo

Metrología Causal · Vol. II
El tipo de pregunta no siempre se formula con esa claridad.
El destinatario puede decir simplemente: "Quiero saber qué pasó".
Eso puede ser un Tipo 1 o un Tipo 3 dependiendo de para qué lo
quiere saber. La pregunta de seguimiento del mediador —"¿qué
tiene que poder decir usted con este análisis en la mano?"—
resuelve la ambigüedad en la totalidad de los casos.

### III. La tabla de decisión: tipo de pregunta → serie
Cada tipo activa una serie del Método Prometeo o una
combinación de series. La selección no es discrecional: está
determinada por la estructura de la pregunta. El mediador que
activa la serie equivocada produce un análisis formalmente
impecable pero materialmente incorrecto: el cálculo cierra, los
números son internamente coherentes, el expediente tiene todos
sus documentos — pero el instrumento no era el que el
destinatario necesitaba. Esa es precisamente su peligrosidad: un
error de cálculo es visible porque algo no cuadra; un error de serie
no produce ninguna señal interna de fallo.
Tipo Serie Serie Por qué esta
principal adicional combinación
1 · I — — La Serie I produce la
Diagnóstico Contabilidad distribución R* que
Ontológica responde directamente
quién y en qué proporción
2 · II — Siempre Sin R* base de Serie I, el
Compliance Compliance precedida IIC no tiene denominador.
Causal de I Serie II ajusta los pesos;
Serie I los establece
3 · III — Siempre El hipercubo de
Imputación Imputación precedida parámetros de Serie III
Causal de I requiere el vector R* de

Metrología Causal · Vol. II
Tipo Serie Serie Por qué esta
principal adicional combinación
Serie I como punto de
referencia
4 · I + II — Prevención requiere tanto
Prevención combinadas el mapa causal (I) como el
diagnóstico de congruencia
del diseño (II)
5 · I — El mismo protocolo de
Seguimiento longitudinal Serie I aplicado en t(cid:0), t(cid:0)...
(repetida) t(cid:0). La curva es el
producto, no un punto
Una regla absoluta: la Serie II y la Serie III nunca se aplican
sin Serie I previa. La Serie II ajusta los pesos del grafo — para
ajustar, primero hay que tener pesos de referencia. La Serie III
construye el hipercubo sobre el vector R* — para construir el
hipercubo, primero hay que tener ese vector. El mediador que
aplica II o III sin I está construyendo sobre aire.

### IV. Los casos compuestos: cuando el destinatario
necesita más de un tipo
El destinatario puede necesitar más de un tipo de respuesta
sobre el mismo caso. El abogado que necesita explicar quién causó
el daño ante el juez (Tipo 3) y al mismo tiempo orientar al cliente
sobre cómo rediseñar el proceso (Tipo 4) necesita I + II + III —
el análisis integrado completo. El médico que necesita documentar
la contribución causal de cada factor (Tipo 1) y verificar si el
protocolo se siguió (Tipo 2) necesita I + II.
La regla de los casos compuestos es simple: se activan todas
las series que corresponden a todos los tipos identificados, en el

Metrología Causal · Vol. II
orden que la Parte III de este volumen establece. Nunca se reduce
la demanda del destinatario para simplificar el análisis: si el
destinatario necesita I + II + III, el mediador produce I + II + III.
Combinaciones más frecuentes en la práctica
Tipos 1 + 3 (Diagnóstico + Imputación) → Series I + III ·
La combinación más frecuente en contextos jurídicos
adversariales. El diagnóstico establece la distribución; la
imputación la blinda ante impugnación.
Tipos 1 + 2 (Diagnóstico + Compliance) → Series I + II ·
La combinación más frecuente en auditoría institucional y
salud pública. El diagnóstico identifica los nodos críticos; el
compliance evalúa el diseño que los produjo.
Tipos 1 + 2 + 3 (análisis completo) → Series I + II + III ·
La combinación más exigente. Reservada para casos donde
el análisis debe resistir tanto el escrutinio regulatorio como
el adversarial, y donde el diseño institucional es parte central
del resultado.

### V. Producto de salida: la hoja de ruta inicial
Al terminar este capítulo, el mediador tiene un dato y solo
uno: qué serie o series se activan en este caso. Ese dato es el
producto de salida del Capítulo I·1. No es un análisis, no es un
grafo, no es un cálculo. Es una decisión de arquitectura que
gobierna todo el trabajo que sigue.
Producto de salida · Capítulo I·1
Decisión documentada de serie(s) a aplicar: Tipo(s) de
pregunta identificado(s) → Serie(s) seleccionada(s) → Orden

Metrología Causal · Vol. II
de producción. Esta decisión queda registrada en el
encabezado del expediente y no se modifica sin revisión
explícita del tipo de pregunta con el destinatario.
Notas al Capítulo I·1
1 La pregunta de umbral —"¿qué tiene que poder decir usted con este análisis
en la mano?"— es el instrumento de elicitación más eficiente disponible
para el mediador. El destinatario que no puede responderla no ha
articulado aún su necesidad real. El mediador que comienza sin esa
respuesta trabaja sin brújula.
2 Los cinco tipos de pregunta corresponden a las cinco posiciones desde las
que un destinatario puede relacionarse con un resultado: quien lo padece
(Diagnóstico), quien diseñó el sistema que lo produjo (Compliance),
quien debe atribuirlo formalmente (Imputación), quien debe evitarlo en
el futuro (Prevención), y quien lo acompaña en su evolución
(Seguimiento). La clasificación no es exhaustiva en sentido lógico
absoluto, pero sí cubre la totalidad de los casos que la práctica de catorce
dominios ha producido.
3 La restricción de que Series II y III nunca se aplican sin Serie I no es una
convención procedimental. Es una consecuencia matemática: IIC
requiere el vector R* como denominador [Vol.I · Cap. V·3], y el
hipercubo de Serie III requiere el vector R* como punto central [Vol.I
· Cap. VI·8]. Sin R*, ninguna de las dos tiene objeto matemático.

Metrología Causal · Vol. II

## PARTE I · El flujo de trabajo del mediador

### Capítulo I·2
El mapa completo del proceso
De ECO al expediente: seis estaciones, un producto en cada una

### I. El proceso como cadena de productos
El análisis causal no es un evento sino una cadena. Cada
estación del proceso recibe el producto de la estación anterior y
entrega un producto nuevo. El mediador que sabe exactamente
qué produce en cada estación sabe cuándo terminó cada paso —
y sabe, también, qué pasa si una estación falla: qué producto queda
sin insumo y qué parte del expediente resulta comprometida.
El mapa que este capítulo establece tiene seis estaciones. No
todas se activan en todos los casos: la Estación ECO solo aplica
cuando hay un ego humano a localizar; la Estación HISTOS solo
aplica cuando el caso tiene componente de acompañamiento. Pero
el orden entre las estaciones que se activan es invariante: ninguna
puede producir su producto sin el insumo de la anterior.

### II. Estación 1 · ECO — Localización del ego

Metrología Causal · Vol. II
La Entrevista Clínica Ontológica es el primer instrumento
que opera cuando el caso tiene un ego humano como nodo
relevante. Su función no es clínica en el sentido de diagnóstico de
salud mental: es metrológica. ECO produce la localización del ego
en el campo de posibilidades — qué Hijo domina su voluntad, con
qué nivel de evidencia, con qué consistencia entre la
autopercepción del sujeto y la conducta observable.
El producto de la Estación ECO es la DI-ECO: la
Declaración de Identidad de la Entrevista Clínica Ontológica. La
DI-ECO contiene el vector P(Hijos) con sus niveles EP, el código
de eje del SDO, y la descripción del contexto que alimentará el
Bloque II del grafo. Todo lo que la DI-ECO no captura —el grafo
del campo, los nodos institucionales, los nodos normativos— es
insumo de las estaciones siguientes.
Estación ECO → Producto
Entrada: el ego a localizar (sujeto de la entrevista o caso
documental).
Operación: administración de los seis módulos del Bloque I
+ preguntas contextuales del Bloque II.
Producto: DI-ECO completa → P(Hijos) con niveles EP +
código de eje SDO + descripción de contexto.
Condición de completitud: todos los módulos administrados sin condiciones
de invalidación [ECO · Cap. II·V]. Si hay invalidación parcial,
documentar y aplicar protocolo de datos incompletos [Vol.I · Cap. IV·4].

### III. Estación 2 · SDO — Posición estructural del
ego
El Sistema de Diagnóstico Ontológico recibe la DI-ECO y
produce la lectura de los cinco ejes del ego. La diferencia entre
ECO y SDO no es de escala sino de perspectiva: ECO observa

Metrología Causal · Vol. II
desde el diálogo; SDO lee desde la estructura. El mismo ego puede
producir una DI-ECO con señales mixtas que el SDO resuelve al
leer la configuración de los cinco ejes en conjunto.
El producto del SDO es el código de eje: una secuencia de
cinco dígitos que describe la posición estructural del ego con
suficiente precisión para que el Capítulo I·4 asigne el rango de S
correcto. El código de eje es también el punto de entrada de
HISTOS si el caso tiene componente de acompañamiento — el
Protocolo Histos parte del código SDO como diagnóstico de
situación inicial.

### IV. Estación 3 · Grafo G = (N, E, W)
La construcción del grafo es la estación central del proceso.
Recibe como insumo la DI-ECO (para los nodos humanos), el
SDO (para la posición de S de esos nodos), y el expediente
documental del caso (para todos los nodos, incluyendo los
institucionales, normativos, y algorítmicos que ECO y SDO no
cubren).
El grafo tiene tres componentes que el mediador construye
en secuencia. Primero: el conjunto de nodos N — todos los
actores con capacidad causal sobre el resultado D, incluyendo los
que no aparecen en la evidencia disponible pero cuya posición
estructural los hace necesarios. Segundo: el conjunto de aristas E
con su dirección — quién influye sobre quién. Tercero: la matriz
de pesos W — la intensidad de cada influencia expresada como
rango [a_ij, b_ij] calibrado según el nivel de evidencia E0–E8.
El producto de la Estación Grafo es la hoja de calibración
completa: una tabla con todos los nodos, todas las aristas, todos
los rangos de peso, todos los niveles de evidencia, y los valores de
S y α asignados a cada nodo. La hoja de calibración es el insumo
completo de la Estación Cálculo.

Metrología Causal · Vol. II
Estación Grafo → Producto
Entrada: DI-ECO + código SDO + expediente documental.
Operación: identificación de nodos → construcción de
aristas → asignación de rangos [a_ij, b_ij] según E0–E8 →
asignación de S y α.
Producto: Hoja de Calibración completa [plantilla Vol.II ·
Sec. 4.1].
Condición de completitud: todos los nodos con capacidad causal
identificados — incluyendo los no documentados cuya posición estructural
los hace necesarios. Un grafo incompleto produce R* incorrecto con
independencia de la precisión del cálculo.

### V. Estación 4 · Cálculo
La Estación Cálculo recibe la hoja de calibración y produce
los parámetros del expediente. No requiere decisión sobre qué
calcular: esa decisión fue tomada en el Capítulo I·1 (qué serie), en
el I·4 (S), en el I·5 (α), y en el I·6 (eigenvector o Shapley). El
cálculo ejecuta.
Para la Serie I: el método de potencias sobre la matriz W de
midpoints produce el vector R*. Con R* y S se calcula R*_neta.
Con R* y α se calcula Δ. Para la Serie II: el IIC del nodo de diseño
ajusta los pesos de sus aristas; el cálculo se repite sobre W ajustada.
Para la Serie III: el hipercubo de parámetros se construye sobre
los rangos [a_ij, b_ij] y el ranking σ(w) se calcula en cada punto del
hipercubo. El nivel de la Declaración (A, B, C, D) emerge del
análisis de estabilidad del ranking.

### VI. Estaciones 5 y 6 · Expediente y HISTOS

Metrología Causal · Vol. II
El expediente recibe los parámetros del cálculo y los organiza
en los cuatro documentos que el análisis entrega: la hoja de
calibración (ya producida en la Estación 3), el vector R* (con sus
derivados R*_neta, Δ, e IIC según la serie), el reporte de
sensibilidad (solo para Serie III), y la Declaración. Las plantillas de
estos documentos están en la Sección 4 de este volumen.
HISTOS recibe el expediente completo y produce el plan de
acompañamiento cuando el caso lo requiere. El Protocolo Histos
parte del Δ como medida de la brecha que el acompañamiento
debe trabajar y del código SDO como diagnóstico de situación.
HISTOS es la estación de cierre del proceso en los casos con
componente de acompañamiento clínico u ontológico.
Producto de salida · Capítulo I·2
Mapa de ruta del caso: qué estaciones se activan, en qué
orden, qué produce cada una, y cuáles son las condiciones de
completitud que habilitan el paso a la siguiente. El mapa de
ruta queda registrado en el encabezado del expediente junto
a la decisión de serie del Capítulo I·1.
Notas al Capítulo I·2
1 La Estación ECO es opcional en el sentido de que no todos los casos
tienen un ego humano a localizar. Los casos de auditoría institucional
donde todos los nodos son institucionales o normativos —sin ego
individual identificable como objeto de localización— no activan ECO.
El grafo se construye directamente desde el expediente documental.
2 La condición de completitud del grafo —que incluya todos los nodos con
capacidad causal, incluyendo los no documentados— es la condición
metrológica más exigente del sistema y la más frecuentemente violada
en la práctica. Un nodo estructuralmente necesario que no aparece en el
expediente no desaparece del grafo real: desaparece del análisis,
concentrando artificialmente R* en los nodos documentados [Vol.I ·
Cap. III·5]. El mediador que sabe que hay un nodo relevante pero no

Metrología Causal · Vol. II
tiene evidencia de él debe incluirlo con nivel de evidencia E0 y
documentar la ausencia.
3 HISTOS no es una estación obligatoria. Es el protocolo de cierre cuando
el análisis tiene consecuencias de acompañamiento para el ego
localizado. En contextos puramente forenses o de auditoría, el proceso
termina con la entrega del expediente.

Metrología Causal · Vol. II

## PARTE I · El flujo de trabajo del mediador

### Capítulo I·3
Cómo la DI-ECO alimenta el grafo
De la localización clínica a los parámetros de la hoja de calibración

### I. Lo que la DI-ECO produce y lo que el grafo
necesita
La DI-ECO y la hoja de calibración del grafo parecen
documentos de mundos diferentes. La DI-ECO habla de Hijos de
Afrodita, de niveles EP, de la distinción entre φ(cid:0) y φ(cid:0). La hoja de
calibración habla de nodos, aristas, rangos de peso, y niveles de
evidencia E0–E8. La proposición central de este capítulo es que
esa diferencia es vocabulario, no contenido: cada elemento de la
DI-ECO tiene un correlato exacto en la hoja de calibración, y la
conversión es directa.
El grafo necesita cuatro tipos de información para cada nodo
humano: quién es el nodo (su identidad como actor), cuánto pesa
su influencia sobre el resultado (el rango de su arista hacia el
sumidero), cuánto de esa influencia es idiosincrática del ego vs. del
campo (S), y cuánto de su responsabilidad ha integrado como
propia (α). La DI-ECO produce, en ese mismo orden: el perfil del
sujeto, la intensidad de φ(cid:0) (Hijo dominante), la posición de v_t en
relación al campo (→ S), y la actividad de φ₂ (→ α).

Metrología Causal · Vol. II

### II. Del Bloque I al grafo: P(Hijos) y EP como
fuentes de S y v_t
El Bloque I de la DI-ECO administra seis módulos, uno por
Hijo. Cada módulo produce un código H (H-3, H-2, H-1, o no
determinado) y un nivel de evidencia EP (EP-0 a EP-5). El código
H indica la posición del sujeto respecto a ese Hijo: H-3 es
localización clara, H-2 es localización probable, H-1 es señal
presente pero no dominante, indeterminado es evidencia
insuficiente.
Del Bloque I emergen dos parámetros directos para el grafo.
El primero es el Hijo dominante: el Hijo con código H-3 más alto
EP determina el rango de S que el Capítulo I·4 formaliza. Si hay
más de un H-3 o si el máximo es H-2, se aplica el protocolo de
evidencia contradictoria de ese mismo capítulo. El segundo
parámetro es la calidad de v_t: la consistencia entre los códigos H
del Hijo dominante a lo largo de los módulos del Bloque I es el
proxy observable del grado de estructuración de v_t en el
momento del acto analizado.
Código H EP del Lectura para el grafo
del módulo
módulo
H-3 EP-5 o Localización confirmada. S desde el rango
EP-4 central del Hijo. v_t estructurado.
H-3 EP-3 Localización probable. S desde el rango
completo del Hijo. v_t estructurado con
moderada certeza.
H-3 EP-2 o Localización débil. Ampliar rango de S en
EP-1 0.10 hacia ambos lados. Documentar
incertidumbre.

Metrología Causal · Vol. II
Código H EP del Lectura para el grafo
del módulo
módulo
H-2 EP-4 o Señal probable. Usar rango del Hijo con
EP-5 margen inferior. Verificar módulos de
Hijos adyacentes.
H-1 cualquier Señal presente pero no dominante. Hijo
EP no es el dominante. Datos para análisis de
campo secundario.
? — Evidencia insuficiente. No asignar S desde
este módulo. Activar Ruta B para S [Cap.
I·5].

### III. Del Bloque II al grafo: el contexto como
fuente de aristas
El Bloque II de la DI-ECO recoge la descripción del campo
que el sujeto habita: las personas que influyen en sus decisiones,
las instituciones que estructuran su entorno, los eventos que
determinaron su historia acumulada. Este bloque no produce
parámetros para el nodo del ego — produce los candidatos a
nodos adicionales del grafo y las aristas entre ellos.
Cada persona mencionada en el Bloque II con influencia
recurrente sobre las decisiones del sujeto es un candidato a nodo.
Cada institución cuyo protocolo el sujeto sigue o viola es un
candidato a nodo de diseño. Cada evento histórico que el sujeto
identifica como determinante es evidencia de una arista de alta
intensidad entre ese evento y el nodo del ego. El mediador no
convierte automáticamente toda mención del Bloque II en un
nodo: convierte en nodo todo actor cuya presencia o ausencia
habría cambiado el resultado analizado.

Metrología Causal · Vol. II

### IV. La hoja de conversión DI-ECO → parámetros
del grafo
La hoja de conversión es el documento operativo que cierra
este capítulo. El mediador la completa con los datos de la DI-ECO
antes de construir la hoja de calibración del grafo. Una vez
completada, todos los parámetros del nodo del ego quedan
definidos con suficiente precisión para comenzar la construcción
del grafo.
Campo de la Operación de Parámetro en la hoja
DI-ECO conversión de calibración
Hijo dominante Tabla de conversión S del nodo del ego:
(código H-3 + P(Hijos) → rango de S rango [a_S, b_S]
EP más alto) [Cap. I·4]
Nivel EP del Hijo Modulación del rango: Amplitud del rango de S
dominante EP-5 → midpoint, EP-4 en la hoja
→ ±0.05, EP-3 →
rango completo
Actividad de φ(cid:0) Tabla de conversión φ(cid:0) α del nodo del ego:
observada en el → α [Cap. I·5, Ruta A] estimado inicial
módulo
dominante
Consistencia de Alta consistencia → v_t Anotación de calidad de
H-3 en los estructurado. Baja v_t en la hoja
módulos del consistencia → v_t
Bloque I difuso
Actores del Cada actor → nodo Nodos adicionales del
Bloque II con candidato con arista grafo con arista
influencia hacia el ego preliminar
recurrente

Metrología Causal · Vol. II
Campo de la Operación de Parámetro en la hoja
DI-ECO conversión de calibración
Instituciones del Cada institución Nodos de diseño con
Bloque II relevante → nodo de arista de campo hacia el
diseño candidato ego
Producto de salida · Capítulo I·3
Hoja de conversión DI-ECO → parámetros del grafo: S y α
del nodo del ego con sus rangos y niveles de certeza, calidad
de v_t, y lista de nodos candidatos desde el Bloque II. Esta
hoja es el insumo directo de la construcción del grafo en la
Estación 3.
Notas al Capítulo I·3
1 El Bloque II de la DI-ECO no es una entrevista de historia de vida. Es una
elicitación estructurada del campo del ego orientada a identificar nodos
causalmente relevantes. El mediador que deja que el Bloque II se
convierta en una narrativa sin estructura obtiene material clínico valioso,
pero no produce los datos que el grafo necesita.
2 La actividad de φ(cid:0) como proxy de α requiere una aclaración importante:
φ(cid:0) mide la integración del acto en I(t), mientras α mide la asunción
verificable mediante conducta observable. Son el mismo fenómeno
desde dos perspectivas [La transformación formal · Cap. 1.2]. En
contextos forenses donde la conducta es el único dato disponible, la
Ruta B [Cap. I·5] reemplaza a la Ruta A. En contextos clínicos donde
φ(cid:0) es directamente observable, la Ruta A es más precisa.

Metrología Causal · Vol. II

## PARTE I · El flujo de trabajo del mediador

### Capítulo I·4
Cómo el Hijo dominante determina S
Tabla de conversión P(Hijos) → rango de S para cada nodo del grafo

### I. Por qué el Hijo dominante determina S
S mide cuánto del acto del nodo es atribuible al campo y
cuánto al ego específico. La posición de la voluntad en el momento
del acto —qué Hijo domina v_t— es exactamente lo que
determina esa proporción. Cuando Fobos domina φ(cid:0), el ego actúa
desde el miedo al campo: cualquier otro ego con el mismo nivel de
amenaza habría actuado igual. La sustituibilidad es alta. Cuando
Harmonía domina φ(cid:0), el ego actúa desde la integración plena de
su historia acumulada: nadie más, con ninguna otra historia, habría
actuado igual. La sustituibilidad es mínima.
Esta no es una analogía entre el Hijo y S. Es la misma
dimensión del mismo fenómeno descrita desde dos perspectivas:
el Hijo la describe desde adentro del ego que opera φ(cid:0); S la
describe desde afuera del campo que observa el acto [La
transformación formal · Cap. 1.2]. La conversión entre los dos
vocabularios es, por tanto, una traducción entre perspectivas, no
una correlación entre variables independientes.

Metrología Causal · Vol. II

### II. La tabla de conversión P(Hijos) → rango de S
La tabla que sigue es el instrumento central de este capítulo.
El mediador identifica el Hijo dominante del nodo (desde la DI-
ECO para nodos humanos, desde la evidencia documental para
nodos institucionales) y lee directamente el rango de S que le
corresponde. El midpoint del rango es el valor de cálculo cuando
la evidencia es EP-5 o EP-4. Los extremos del rango se usan
cuando la evidencia es más débil.
Hijo Rango Midpoint Qué significa este S para
dominante de S el caso
Fobos (miedo 0.70 – 0.85 Alta sustituibilidad. El acto fue
al campo) 1.00 respuesta predecible a la
amenaza del campo. Cualquier
ego en esa posición habría
actuado igual ante el mismo
miedo. El campo explica la
mayor parte del resultado.
Deimos 0.60 – 0.73 Sustituibilidad alta-media. La
(angustia 0.85 angustia difusa ante el campo
difusa) produce respuestas
ampliamente compartibles.
Hay más varianza que en
Fobos pero el campo sigue
siendo dominante.
Anteros 0.40 – 0.55 Sustituibilidad media. El acto
(reciprocidad) 0.70 fue condicional a la respuesta
del otro. Depende de quién es
ese otro en este caso
específico. Requiere análisis de
la arista entre el ego y su
referente de reciprocidad.
Potós (anhelo 0.20 – 0.35 Sustituibilidad baja-media. El
de lo ausente) 0.50 acto está orientado a algo que

Metrología Causal · Vol. II
Hijo Rango Midpoint Qué significa este S para
dominante de S el caso
no está presente en el campo.
El objeto del anhelo es
particular del ego. La
idiosincrasia crece conforme el
objeto es más específico.
Eros (deseo 0.10 – 0.23 Sustituibilidad baja. El acto
presente) 0.35 emerge del deseo específico
del ego en el momento del
colapso. Difícilmente otro ego
en la misma posición
estructural habría tenido el
mismo deseo con la misma
intensidad.
Harmonía 0.00 – 0.13 Sustituibilidad mínima. El acto
(integración) 0.25 emerge de la integración plena
del ego. Es el acto más
idiosincrático posible: es el
resultado de toda la historia
acumulada de ese ego
específico, irreplicable.

### III. El nivel EP como modulador del rango
El rango de cada Hijo tiene una amplitud de 0.30. El nivel de
evidencia EP determina qué parte del rango se usa en el cálculo.
Esta modulación no es arbitraria: refleja que la localización del ego
en un Hijo con alta certeza de evidencia permite una asignación
más precisa de S que una localización con evidencia débil.

Metrología Causal · Vol. II
Nivel EP Cómo usar el rango de S
EP-5 — Usar el midpoint del rango. La localización es
Evidencia suficientemente precisa para un valor puntual.
múltiple
convergente
EP-4 — Usar el midpoint ± 0.05. El rango efectivo se reduce a
Evidencia 0.10 centrado en el midpoint.
directa sólida
EP-3 — Usar el rango completo del Hijo. El cálculo se realiza
Evidencia con el midpoint; la amplitud del rango alimenta el
directa análisis de sensibilidad.
moderada
EP-2 — Ampliar el rango del Hijo en ±0.10. El rango efectivo
Evidencia pasa de 0.30 a 0.50. Documentar la amplitud en la hoja
indirecta de calibración.
EP-1 — No asignar S desde este módulo. Activar Ruta B de
Evidencia calibración de S desde la evidencia documental [Cap.
mínima I·5].
EP-0 — Sin S no asignable desde ECO. El nodo requiere fuente
evidencia alternativa de S o tratamiento como nodo de evidencia
incompleta [Vol.I · Cap. IV·4].

### IV. El protocolo de evidencia contradictoria
El protocolo de evidencia contradictoria se activa cuando el
Bloque I de la DI-ECO produce señales de dos o más Hijos con
codificación H-3 o cuando la señal más fuerte es H-2 en múltiples
módulos. En esos casos, no existe un Hijo claramente dominante
y la tabla del apartado anterior no produce un rango de S sin
ambigüedad.
El protocolo tiene tres pasos. Primero: verificar si la
contradicción es real o es un artefacto de la administración. Las

Metrología Causal · Vol. II
condiciones de invalidación de la ECO —sesgo de imagen,
resistencia activa, fatiga— pueden producir señales mixtas que no
reflejan la posición real del ego. Si hay condición de invalidación,
repetir los módulos afectados antes de proceder.
Segundo: si la contradicción es real, identificar en qué
contexto se activa cada señal. Un ego que muestra Fobos en el
módulo de relaciones de autoridad y Eros en el módulo de
relaciones entre pares no tiene evidencia contradictoria sino
evidencia de que el Hijo dominante depende del tipo de relación.
El caso analizado determina cuál de los dos contextos es el
relevante.
Tercero: si la contradicción persiste sin resolución
contextual, usar el rango más amplio posible — el que cubre el
espectro entre los dos Hijos con mayor señal — y documentar la
incertidumbre con nivel EP-2 en la hoja de calibración. El análisis
de sensibilidad de la Serie III absorberá esa incertidumbre en el
hipercubo de parámetros.
Producto de salida · Capítulo I·4
Valor de S para cada nodo del grafo: rango [a_S, b_S]
derivado del Hijo dominante y modulado por el nivel EP,
con el midpoint como valor de cálculo y la amplitud
documentada en la hoja de calibración. Para nodos sin ECO
disponible: S desde Ruta B [Cap. I·5, criterios universales de
S].
Notas al Capítulo I·4
1 Los rangos de S por Hijo que este capítulo establece son valores de
referencia derivados de la correspondencia formal entre el Hijo
dominante y la sustituibilidad [La transformación formal · Cap. 2.1]. No
son valores empíricos calibrados sobre una muestra: son consecuencias
de la estructura de la doble mediación. Los datos empíricos del

Metrología Causal · Vol. II
Programa ECO [Vol.II · Apéndice A] permitirán, con suficiente
muestra, verificar si los rangos teóricos corresponden a los rangos
observados en poblaciones específicas.
2 La distinción entre Fobos y Deimos en términos de S merece una nota.
Fobos opera desde el miedo a una amenaza concreta y específica del
campo: la amenaza está en el objeto del miedo. Deimos opera desde la
angustia difusa ante el campo en general: la amenaza no tiene objeto
preciso. Esta distinción reduce ligeramente S en Deimos respecto a
Fobos porque la angustia difusa tiene algo más de idiosincrasia en cómo
se procesa — dos egos pueden tener la misma amenaza concreta (→
Fobos, S muy alto) pero la angustia ante el mismo campo general se
procesa con más variación individual (→ Deimos, S algo más bajo).

Metrología Causal · Vol. II

## PARTE I · El flujo de trabajo del mediador

### Capítulo I·5
Cómo se infiere α desde la localización y la
evidencia
Ruta A clínica, Ruta B forense, Ruta C longitudinal: tres fuentes de
un mismo parámetro

### I. Los tres orígenes de α y su jerarquía
α mide la fracción de R* que el nodo integró como propia
mediante acciones verificables. Esta definición abre tres
posibilidades de acceso al dato: desde la observación directa de φ(cid:0)
en la entrevista clínica (Ruta A), desde el análisis de la conducta
verificable en el expediente documental (Ruta B), y desde la
observación acumulada de patrones de atribución a lo largo del
tiempo (Ruta C). Las tres rutas miden el mismo parámetro desde
distintas perspectivas.
La jerarquía entre rutas no es de precisión sino de
disponibilidad. La Ruta A, cuando es posible, produce la
estimación más directa porque observa φ(cid:0) en acción. La Ruta B
es la ruta estándar en contextos forenses donde el ego no es
accesible para entrevista. La Ruta C es la más robusta en términos
de validez longitudinal, pero requiere observación acumulada a lo
largo del tiempo. Las tres pueden combinarse: cuando dos rutas

Metrología Causal · Vol. II
producen estimados convergentes, la certeza del valor de α
aumenta. Cuando divergen, el protocolo de resolución de este
capítulo aplica.

### II. Ruta A — Clínica: α desde la DI-ECO
La Ruta A infiere α desde la actividad de φ(cid:0) observable en
la sesión de ECO. φ(cid:0) es la función de retorno evaluativo del ego
sobre sus propios actos — el mecanismo por el que el acto
producido por φ(cid:0) es o no integrado en I(t). La ECO accede a φ(cid:0)
directamente a través de la calidad del reconocimiento del sujeto
de sus propios actos durante la entrevista.
El mediador no califica la actividad de φ(cid:0) con una escala
cuantitativa durante la entrevista. La calificación emerge de cuatro
observaciones que se realizan de forma natural en el módulo
dominante: si el sujeto reconoce actos propios sin ser preguntado
directamente, si conecta sus actos con sus consecuencias, si puede
nombrar qué habría hecho diferente, y si mantiene esa posición
cuando el facilitador introduce una perspectiva alternativa.
Observación de φ(cid:0) en α Descripción del patrón
ECO estimado
(Ruta A)
φ(cid:0) activo espontáneo: el 0.70 – 1.00 El ego integra sus colapsos
sujeto nombra actos en I(t) con mínima
propios con resistencia. Alta asunción.
consecuencias sin
facilitación directa
φ(cid:0) activo con facilitación: 0.40 – 0.70 El ego puede integrar, pero
el sujeto reconoce con requiere el señalamiento del
preguntas directas pero campo para hacerlo.
no evade Asunción media.

Metrología Causal · Vol. II
Observación de φ(cid:0) en α Descripción del patrón
ECO estimado
(Ruta A)
φ(cid:0) parcial: el sujeto oscila 0.20 – 0.45 El ego tiene capacidad de φ₂,
entre el reconocimiento y pero la ejerce selectivamente.
la atribución externa; El contexto y la audiencia
inconsistente afectan el resultado.
φ(cid:0) ausente: el sujeto 0.00 – 0.25 El ego no integra sus
atribuye colapsos en I(t). Δ alto. La
consistentemente los asunción no está bloqueada
actos al campo, al otro, o — está ausente.
al azar

### III. Ruta B — Forense: α desde la evidencia
documental
La Ruta B calcula α desde la evidencia disponible en el
expediente del caso, sin acceso directo al ego. Opera sobre los tres
criterios universales de asunción establecidos en la Introducción
de este volumen: conocimiento, acción, y oportunidad. Cada
criterio es verificable con evidencia documental y contribuye de
forma independiente al valor de α.
Criterio Pregunta de Contribución Evidencia que
verificación máxima a α lo acredita
Conocimiento ¿El nodo tenía 0.33 Informes de riesgo
información recibidos,
suficiente para reuniones
prever el documentadas,
resultado en el comunicaciones
momento del sobre el resultado
acto? potencial,

Metrología Causal · Vol. II
Criterio Pregunta de Contribución Evidencia que
verificación máxima a α lo acredita
evaluaciones
previas disponibles
Acción ¿El nodo 0.33 (gradable) Acciones
tomó acciones preventivas,
verificables protocolos
orientadas a activados,
modificar o controles
prevenir el implementados,
resultado? reportes
generados,
intervenciones
documentadas
Oportunidad ¿El nodo tuvo 0.33 Reuniones donde
momentos el resultado fue
específicos advertido,
donde podía comunicaciones
haber actuado que solicitaban
diferente y no acción, instancias
lo hizo? de decisión con
alternativa
documentada
El criterio de Acción es el único gradable: un nodo que tomó
algunas acciones, pero no las completas recibe una fracción de los
0.33 proporcional a la completitud de sus acciones. Los criterios
de Conocimiento y Oportunidad son binarios: el nodo tenía la
información o no la tenía; el momento existió o no existió. La
suma de los tres criterios produce α directamente en el rango [0.00,
1.00].

### IV. Ruta C — Longitudinal: α desde la
observación acumulada

Metrología Causal · Vol. II
La Ruta C produce α desde la observación sistemática del
patrón de atribución de un ego a lo largo del tiempo. Es la ruta
más robusta en términos de validez porque elimina el sesgo de un
momento único de observación: el patrón de diez sesiones es más
representativo del α estructural del ego que cualquier observación
puntual.
La Ruta C requiere un protocolo de observación longitudinal
con registros estructurados. El protocolo estándar para
poblaciones de acompañamiento está en el Apéndice A de este
volumen. Para otros contextos, el principio es el mismo: se
observa la gramática de atribución del ego (¿quién es el sujeto
gramatical de sus relatos sobre sus propios actos?) en situaciones
repetidas, y se promedian los valores a lo largo del tiempo.
El promedio de α en la Ruta C converge al valor estructural
del ego después de un número suficiente de observaciones. El
número mínimo de observaciones para una estimación estable
varía por población: el Apéndice A proporciona los datos para la
población de adolescentes en contexto escolar. Para otras
poblaciones, la estabilización se detecta cuando el promedio deja
de cambiar significativamente entre observaciones sucesivas.

### V. Cuándo las rutas divergen: el protocolo de
resolución
Cuando dos rutas disponibles producen estimados de α
significativamente diferentes — con una brecha mayor a 0.25 —
el mediador no promedia. La brecha es información: señala que
hay algo que una perspectiva ve y la otra no.
Protocolo de resolución de divergencia entre rutas de α
Ruta A > Ruta B: el ego reconoce en la entrevista más de lo
que su conducta documenta. Interpretación más frecuente:

Metrología Causal · Vol. II
φ(cid:0) está activo, pero no ha producido acción verificable. El
ego sabe que el acto es suyo, pero no ha actuado sobre esa
conciencia. Δ real puede ser mayor que Δ aparente. Usar el
valor más bajo (Ruta B) como estimado conservador y
documentar la brecha.
Ruta B > Ruta A: el ego tiene más acciones verificables de
asunción que las que reconoce en la entrevista.
Interpretación más frecuente: el ego actuó correctamente
por protocolo, pero no integró esos actos como propios. La
conducta supera la conciencia. Usar el promedio de ambas
rutas y documentar la interpretación.
Ambas rutas divergen de Ruta C: el patrón longitudinal es
diferente de la conducta documentada o del reconocimiento
en entrevista. Esto señala que α varía significativamente con
el contexto o el tiempo. No usar un único valor —
documentar el rango y comunicar la variabilidad al
destinatario.
Producto de salida · Capítulo I·5
Valor de α para cada nodo del grafo: estimado desde Ruta A,
B, o C (con fuente documentada), con el rango de certeza y
las notas de divergencia cuando aplican. Este valor queda
registrado en la columna α de la hoja de calibración, junto a
la fuente de evidencia que lo sostiene.
Notas al Capítulo I·5
1 α no mide remordimiento, culpa, ni declaración de responsabilidad. Mide
asunción verificable mediante conducta. Un ego que declara alta
responsabilidad, pero no tomó ninguna acción orientada a modificar el
resultado tiene α bajo independientemente de lo que diga. Un ego que
no declara responsabilidad, pero tomó acciones completas de mitigación
tiene α alto. La confusión entre declaración y asunción es el error más
frecuente de calibración de α en la práctica.

Metrología Causal · Vol. II
2 El criterio de Oportunidad merece una aclaración sobre su relación con S.
Es posible que un ego haya tenido oportunidades de actuar diferente
(→ Oportunidad presente, contribuye a α) pero que cualquier otro ego
en esa posición también las hubiera ignorado (→ S alto). En ese caso, el
ego tiene α bajo, pero también S alto: la responsabilidad neta (R*_neta
= R* × (1-S)) es pequeña, aunque Δ sea grande. El sistema captura
ambas dimensiones independientemente: S describe el acto en relación
al campo; α describe la integración del acto por el ego. Son dimensiones
ortogonales.

Metrología Causal · Vol. II

## PARTE I · El flujo de trabajo del mediador

### Capítulo I·6
El protocolo de decisión entre eigenvector y
Shapley
Cuándo cada método aplica y cómo elegir

### I. El problema que este capítulo resuelve
El sistema tiene dos métodos de cálculo de responsabilidad
causal: el eigenvector principal de W y el valor de Shapley. El
Volumen I establece cuándo cada uno es matemáticamente válido
[Vol.I · Cap. VII·3]. Este capítulo establece cómo el mediador
identifica, desde la estructura del grafo que tiene delante, cuál de
los dos métodos aplica a su caso.
La confusión entre los dos métodos no es un error de
cálculo: es un error de tipo. Aplicar el eigenvector cuando la
condición que lo justifica no se cumple produce R* que mide
centralidad estructural pero no responsabilidad causal. Aplicar
Shapley cuando el eigenvector es el método correcto produce un
cálculo más costoso computacionalmente que produce el mismo
resultado. El primero error es sustantivo; el segundo, ineficiente.
Este capítulo previene ambos.

Metrología Causal · Vol. II

### II. El eigenvector: condición de aplicación
El eigenvector principal de W es el método correcto cuando
al menos uno de los nodos del grafo es individualmente condición
sine qua non del resultado D. Un nodo i es condición sine qua non
de D si, al eliminar i del grafo y todas sus aristas, el resultado D no
puede ocurrir en su forma específica a través de los nodos y aristas
restantes.
La condición sine qua non individual es una condición
estructural del grafo, no una condición empírica. El mediador no
la verifica experimentalmente —el evento ya ocurrió. La verifica
estructuralmente: ¿existe en G algún camino alternativo de
cualquier otro nodo a D que no pase por i, con peso total
suficiente para producir D en su forma específica? Si no existe ese
camino alternativo, i es condición sine qua non individual.
El eigenvector mide cuánto de D se explica por la posición
estructural de cada nodo en el grafo, tomando en cuenta no solo la
influencia directa sino la indirecta a través de todos los caminos.
Su validez como medida de responsabilidad causal descansa sobre
la condición de que al menos un nodo sea condición necesaria
individual: sin esa condición, la distribución eigenvectorial no tiene
la interpretación causal que R* requiere.
Vol.I · Cap. VII·3

### III. El valor de Shapley: condición de aplicación
El valor de Shapley es el método correcto cuando ningún
nodo del grafo es individualmente condición sine qua non de D.
Esto ocurre cuando las contribuciones de los nodos son
genuinamente no separables: cada nodo solo produce D en
conjunto con otros nodos, y no existe ningún nodo cuya
eliminación sola impediría D.

Metrología Causal · Vol. II
El caso Shapley no es infrecuente en la práctica. Es el caso
de los sistemas donde el resultado emerge de la intersección de
múltiples condiciones necesarias colectivamente pero no
individualmente: la falla sistémica que requiere que todos los
controles fallen simultáneamente, el resultado social que requiere
que múltiples actores mantengan su conducta en paralelo, el
colapso organizacional que resulta de la acumulación de decisiones
ninguna de las cuales sola lo habría producido.
En el caso Shapley, la distribución de responsabilidad es el
valor de Shapley de la función característica v(S) donde S es
cualquier coalición de nodos y v(S) es la fracción del resultado D
que la coalición S puede producir por sí sola. El valor de Shapley
de cada nodo es su contribución marginal promedio sobre todas
las coaliciones posibles en las que podría participar.

### IV. El test de decisión: la prueba de condición
sine qua non
El test de decisión se aplica nodo por nodo sobre el grafo
construido. Para cada nodo i, el mediador responde la siguiente
pregunta estructural: eliminado i del grafo, ¿existe algún conjunto
de nodos restantes suficiente para producir D en su forma
específica?
El test de condición sine qua non individual · Protocolo
Paso 1: Identificar el nodo candidato i y el resultado
específico D (el nodo sumidero Nf).
Paso 2: Eliminar i y todas sus aristas del grafo. Llamar G' al
grafo resultante.

Metrología Causal · Vol. II
Paso 3: Verificar si en G' existe al menos un camino desde
cualquier nodo fuente a Nf con peso acumulado suficiente
para producir D en su forma específica.
Resultado A — No existe ese camino: i es condición sine qua
non individual → el eigenvector es el método correcto.
Resultado B — Existe ese camino: i no es condición sine qua
non individual → i no funda por sí solo la condición del
eigenvector.
Decisión final: si al menos un nodo produce Resultado A → eigenvector.
Si todos los nodos producen Resultado B → Shapley.

### V. Los casos mixtos y la conjetura del operador
unificador
Un caso mixto es un grafo donde algunos nodos son
condición sine qua non individual y otros no lo son. En ese caso,
la teoría del sistema predice que el eigenvector es el método
correcto para la distribución global — porque la condición que
funda su validez se cumple para al menos un nodo— pero que los
nodos que no son individualmente sine qua non tienen una
componente de su R* que el eigenvector distribuye de manera
diferente a como lo haría Shapley.
El sistema maneja los casos mixtos con el eigenvector como
método primario y el Shapley como verificación secundaria para
los nodos que no son individualmente sine qua non. Si los dos
métodos producen valores similares para esos nodos, el
eigenvector se usa como resultado definitivo. Si producen valores
significativamente diferentes, se documenta la diferencia y se
reporta al destinatario como incertidumbre estructural del análisis.
La conjetura del operador unificador — la demostración
formal de que existe un operador que produce el eigenvector en el
caso sine qua non y el Shapley en el caso no-sine-qua-non,

Metrología Causal · Vol. II
interpolando entre ellos en casos mixtos — está formulada con
precisión en el Capítulo IV·7 de este volumen y en la
Axiomatización del Sistema de la Doble Mediación. Es el
programa de investigación abierto más importante del paradigma.
Los precedentes de la literatura que apuntan en esta dirección (Hu
& Shapley 2003, Teng 2016, Aleandri et al. 2025) sugieren que la
conjetura es verdadera, pero la demostración completa no existe
aún.
Producto de salida · Capítulo I·6
Decisión de método de cálculo: eigenvector (si al menos un
nodo supera el test de condición sine qua non) o Shapley (si
ningún nodo la supera), con la documentación del test
aplicado. En casos mixtos: eigenvector primario con
verificación Shapley sobre los nodos no-sine-qua-non y
documentación de la diferencia.
Notas al Capítulo I·6
1 El "peso acumulado suficiente" del Paso 3 del test requiere una aclaración
operativa. En términos del grafo, significa que el camino alternativo en
G' produce un resultado D' tal que D' = D en su forma específica —
no en alguna forma aproximada. Si la eliminación de i produciría un
resultado cuantitativamente menor pero cualitativamente idéntico, i no
es condición sine qua non: el resultado habría ocurrido de todas formas,
solo con menor intensidad. Si la eliminación de i produciría un resultado
cualitativamente diferente, i es condición sine qua non.
2 La confusión entre la fórmula I = R* × (1−S) × (1−α) —que circuló en la
conversación con modelos de lenguaje externos— y el sistema formal
merece una aclaración explícita. Esa fórmula combina dos corolarios del
Teorema (R*_neta y Δ) en una sola cantidad que el sistema no define
como tal. R*_neta = R* × (1−S) mide la fracción idiosincrática del peso
causal. Δ = R* × (1−α) mide el déficit de asunción. Son cantidades
independientes con interpretaciones distintas. El producto de las dos es

Metrología Causal · Vol. II
una cantidad sin nombre en el sistema formal porque no tiene
interpretación metrológica propia.

Metrología Causal · Vol. II

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

## PARTE II · El análisis simple: una sola serie

### Capítulo II·1
Serie I: Contabilidad Ontológica
El protocolo completo del análisis causal base

### I. Cuándo aplica la Serie I
La Serie I es el análisis causal base del sistema. Responde la
pregunta de Tipo 1 —¿quién fue condición necesaria de este
resultado y en qué proporción? — y es el punto de partida
obligatorio de toda combinación de series. Ningún análisis del
sistema, con independencia del tipo de pregunta que responda,
omite la Serie I: sus siete pasos producen el vector R* que todas
las series subsiguientes usan como insumo.
La Serie I aplica en solitario cuando el destinatario necesita
únicamente el diagnóstico causal: la distribución de
responsabilidad entre los nodos del grafo, con sus componentes
de sustituibilidad y asunción, y con las hipótesis de prevención que
esa distribución produce. Cuando el destinatario necesita también
compliance o imputación adversarial, la Serie I se ejecuta primero
y sus resultados alimentan la Serie II o la III.

### II. Paso 1 · Construcción del grafo G = (N, E, W)

Metrología Causal · Vol. II
El grafo es el objeto matemático sobre el que opera todo el
cálculo de la Serie I. Su construcción no es un paso previo al
análisis: es la primera operación analítica, y determina la validez de
todo lo que sigue. Un grafo bien construido produce R* que mide
responsabilidad causal real. Un grafo mal construido produce R*
que mide algo diferente con exacta precisión formal.
El grafo G = (N, E, W) tiene tres componentes. El conjunto
de nodos N contiene todos los actores con capacidad causal sobre
el resultado D, incluyendo el nodo sumidero Nf que representa D.
El conjunto de aristas E contiene las relaciones de influencia causal
entre nodos, con su dirección. La matriz de pesos W asigna a cada
arista un peso w_ij que refleja la intensidad de la influencia del
nodo i sobre el nodo j.
El peso de cada arista no se asigna como un valor puntual:
se asigna como un rango [a_ij, b_ij] calibrado según el nivel de
evidencia disponible para esa relación. El valor de cálculo del Paso
3 es el midpoint m_ij = (a_ij + b_ij) / 2. La amplitud del rango
alimenta el análisis de sensibilidad de la Serie III si el caso lo
requiere.
Nivel Descripción de la evidencia Amplitud del rango
E [a_ij, b_ij]
E8 Evidencia experimental ±0.02 sobre el midpoint
controlada o réplica verificada estimado
E7 Estudio observacional ±0.05
prospectivo con grupo de control
E6 Múltiples estudios convergentes o ±0.07
consenso de expertos
E5 Evidencia documental directa y ±0.10
consistente

Metrología Causal · Vol. II
Nivel Descripción de la evidencia Amplitud del rango
E [a_ij, b_ij]
E4 Evidencia documental directa con ±0.12
inconsistencias menores
E3 Evidencia indirecta sólida o ±0.15
inferencia estructural fuerte
E2 Evidencia indirecta débil o ±0.18
inferencia estructural moderada
E1 Evidencia mínima o testimonial ±0.22
no corroborada
E0 Sin evidencia: nodo ±0.25 sobre midpoint
estructuralmente necesario pero 0.30
no documentado
Ejemplo numérico — Caso de referencia (4 nodos)
Nf = resultado D (nodo sumidero). N = {D (diseño), E
(ejecutor), S (supervisor), Nf}.
Aristas: D → Nf [0.35, 0.55], E → Nf [0.20, 0.40], S → Nf
[0.10, 0.24], D → E [0.40, 0.60], S → E [0.25, 0.45].
Niveles de evidencia: D→Nf E5, E→Nf E4, S→Nf E3, D→E E5,
S→E E4. Midpoints: D→Nf 0.45, E→Nf 0.30, S→Nf 0.17,
D→E 0.50, S→E 0.35.

### III. Paso 2 · Verificación de condiciones de validez
Antes del cálculo, el grafo debe cumplir dos condiciones que
el Teorema de Perron-Frobenius requiere para garantizar la
existencia y unicidad del eigenvector principal positivo:
irreducibilidad y aperiodicidad.

Metrología Causal · Vol. II
El grafo es irreducible si desde cada nodo existe al menos un
camino dirigido al nodo sumidero Nf. Un nodo sin camino al
sumidero no tiene relación causal con D y debe eliminarse del
grafo antes del cálculo. La irreducibilidad se verifica
inspeccionando el grafo: si hay nodos "flotantes" sin camino a Nf,
no son causalmente relevantes para el resultado analizado.
El grafo es aperiódico si no contiene ciclos de longitud fija
que atrapen el método de potencias en una oscilación permanente.
En la práctica, la aperiodicidad se garantiza añadiendo un autolazo
de peso ε = 0.01 al nodo sumidero Nf: w_Nf,Nf = ε. Este ajuste
es suficiente para romper cualquier periodicidad sin afectar la
distribución R* de manera significativa.
Corrección de aperiodicidad
w_Nf,Nf = ε = 0.01 → renormalizar cada columna de
W para que Σ_j w_ij = 1
Solo se aplica si el grafo falla el test de aperiodicidad. En la mayoría de los
casos prácticos el grafo ya es aperiódico.

### IV. Paso 3 · Cálculo de R* por el método de
potencias
Con la matriz W de midpoints construida y las condiciones
de validez verificadas, el método de potencias calcula el
eigenvector principal normalizado. El método es iterativo: parte
de un vector inicial uniforme y lo multiplica repetidamente por W
hasta que la diferencia entre iteraciones sucesivas cae por debajo
del umbral de convergencia.
Método de potencias — iteración
R*(k+1) = W · R*(k) / ||W · R*(k)||(cid:0)

Metrología Causal · Vol. II
Condición inicial: R*(0) = [1/n, 1/n, ..., 1/n]. Criterio de convergencia:
||R*(k+1) − R*(k)||₁ < 10⁻⁶. En sistemas de 3–8 nodos típicos,
la convergencia ocurre entre 15 y 40 iteraciones.
La condición de convergencia 10⁻ ⁶ garantiza que el vector
R* es estable hasta la sexta cifra decimal. Para los propósitos del
expediente, se reportan cuatro cifras decimales. La verificación
final es simple: Σ_i R*_i = 1.000 (±0.001 por redondeo).
Nodo R* Interpretación
(resultado
del caso de
referencia)
D — 0.4812 El nodo de diseño explica el 48% del
Diseño resultado. Su influencia directa sobre
Nf y su influencia estructural sobre E
lo posicionan como el nodo de mayor
centralidad causal.
E — 0.3104 El ejecutor explica el 31% del
Ejecutor resultado. Su posición es significativa
pero dependiente del diseño que lo
orienta.
S — 0.1521 El supervisor explica el 15% del
Supervisor resultado. Su influencia se ejerce
principalmente a través de E.
Nf — 0.0563 El nodo sumidero retiene el residuo
Resultado del autolazo ε. Este valor no tiene
interpretación de responsabilidad.

### V. Paso 4 · Determinación de S y cálculo de
R*_neta

Metrología Causal · Vol. II
Con el vector R* calculado, el Paso 4 determina S para cada
nodo y calcula R*_neta: la fracción idiosincrática del peso causal
de cada nodo, excluyendo la parte que cualquier otro en esa
posición también habría producido.
S se deriva del Hijo dominante de cada nodo usando la tabla
de conversión del Capítulo I·4. Para nodos institucionales o
algoritmos sin ECO disponible, S se determina desde los tres
criterios universales de la Introducción de este volumen: existencia
de alternativa documentada, conformidad con la norma del
dominio, y replicabilidad ante un par equivalente.
R*_neta
R*_neta_i = R*_i × (1 − S_i)
La fracción (1−S_i) es la proporción del acto que es idiosincrática del nodo
i. Σ R*_neta_i ≤ 1. La diferencia 1 − Σ R*_neta_i es la responsabilidad
sistémica total del campo.
Nodo R* S 1 − R*_neta Fuente de S
S
D — Diseño 0.4812 0.20 0.80 0.3850 Harmonía
dominante —
EP4. Decisión
de diseño
altamente
idiosincrática.
E — Ejecutor 0.3104 0.72 0.28 0.0869 Fobos
dominante —
EP4. Alta
presión del
sistema de
incentivos

Metrología Causal · Vol. II
Nodo R* S 1 − R*_neta Fuente de S
S
diseñado por
D.
S — Supervisor 0.1521 0.55 0.45 0.0684 Anteros
dominante —
EP3.
Supervisión
condicionada a
la respuesta del
ejecutivo.
Responsabilidad — — — 0.4597 Campo c:
sistémica fracción del
resultado que
cualquier actor
en estas
posiciones
habría
producido.

### VI. Paso 5 · Determinación de α y cálculo de Δ
El Paso 5 determina α para cada nodo usando la ruta
disponible (A, B, o C según el tipo de caso) y calcula Δ: el déficit
de asunción, la fracción de R* que el nodo causó, pero no integró
como propia mediante acciones verificables.
Δ — Déficit de asunción
Δ_i = R*_i × (1 − α_i) Δ_total = Σ_i Δ_i
Δ_i > 0 indica que el nodo causó más de lo que asumió. Δ_i < 0 indica
inversión causal: el nodo asumió más de lo que causó. Δ_i = 0 indica
equilibrio de asunción.

Metrología Causal · Vol. II
Nodo R* α 1 − Δ_i Fuente de α
α
D — 0.4812 0.15 0.85 0.4090 Ruta B — Criterio de
Diseño conocimiento: sí.
Acción: mínima.
Oportunidad: sí. α =
0.15.
E — 0.3104 0.40 0.60 0.1862 Ruta A — φ(cid:0) activo
Ejecutor con facilitación.
Reconoce el acto con
apoyo del ECO.
S — 0.1521 0.62 0.38 0.0578 Ruta B — Acción de
Supervisor supervisión
parcialmente
documentada. Tres
oportunidades de
intervención
identificadas, una
actuada.
Δ_total — — — 0.6530 63% del resultado total
no fue integrado como
propio por ningún
nodo. Brecha sistémica
de asunción.

### VII. Paso 6 · Cuantificación del daño D y las
fracciones AD_i
El análisis causal distribuye responsabilidad en términos
relativos (R*). Cuando el caso requiere también una distribución
en términos absolutos —cuánto del daño total corresponde a cada
nodo— el Paso 6 cuantifica D_total y calcula la fracción atribuible
AD_i a cada nodo.

Metrología Causal · Vol. II
D_total tiene tres componentes que el mediador cuantifica
desde el expediente del caso. T_inv es el daño de inversión: costos
directos incurridos como consecuencia del resultado analizado.
T_imp es el daño de impacto: consecuencias directas del resultado
sobre los afectados, cuantificadas en las mismas unidades que
T_inv. ΔT_tray es el daño de trayectoria: la diferencia entre el valor
de la trayectoria esperada sin el resultado y el valor de la trayectoria
real, proyectada al horizonte relevante para el caso.
D_total y fracción atribuible AD_i
D_total = T_inv + T_imp + ΔT_tray AD_i = R*_i
× D_total
AD_i es la contribución causal del nodo i al daño total en unidades
absolutas. La suma Σ AD_i = D_total. Las fracciones AD_i son el
insumo directo para cualquier determinación de compensación o reparación
proporcional.
La cuantificación de D_total es responsabilidad del
destinatario del análisis, no del mediador. El mediador recibe los
valores de T_inv, T_imp, y ΔT_tray del expediente del caso y
aplica la fórmula. Si el destinatario no tiene estimados de los tres
componentes, el mediador entrega únicamente R* y documenta
que AD_i está condicionado a la cuantificación de D_total por el
destinatario.

### VIII. Paso 7 · El expediente de Serie I
El expediente de Serie I contiene tres documentos. El
mediador los produce en el orden que sigue: primero la hoja de
calibración (ya completada en el Paso 1), después el vector R* con
su análisis descriptivo, y finalmente las hipótesis de prevención.

Metrología Causal · Vol. II
Documento Contenido Criterio de
completitud
1 · Hoja de Todos los nodos, todas las Todos los ítems de la
calibración aristas con sus rangos [a_ij, lista de verificación
b_ij] y niveles E0–E8, valores del Cap. I·7
de S y α con sus fuentes, completados y
método de cálculo firmados.
seleccionado.
2 · Vector R* Tabla de distribución con R*, Σ R*_i = 1.000
con análisis S, R*_neta, α, Δ para cada (±0.001). El análisis
descriptivo nodo. Párrafo narrativo que narrativo no
describe la distribución causal introduce juicios que
en lenguaje del dominio del el vector no sostiene.
destinatario. Δ_total y su
interpretación sistémica.
3 · Hipótesis Para cada nodo con R* > 0.15: Cada hipótesis
de una hipótesis de rediseño que especifica qué cambio
prevención reduciría su R* en sistemas en el grafo produciría
futuros similares. Las hipótesis qué reducción
se formulan como condiciones estimada en R*. No se
estructurales, no como formulan hipótesis sin
recomendaciones de ancla estructural.
conducta.
Producto de salida · Capítulo II·1
Expediente de Serie I completo: hoja de calibración + vector
R* con análisis descriptivo + hipótesis de prevención. El
vector R* es el producto central que toda serie subsiguiente
presupone. Sin el expediente de Serie I completo y
verificado, ninguna otra serie puede iniciarse.
Notas al Capítulo II·1

Metrología Causal · Vol. II
1 El nodo sumidero Nf no tiene R* interpretable como responsabilidad
causal: es el nodo que representa el resultado D, no un actor que lo
produjo. El valor residual que retiene por el autolazo ε no debe incluirse
en el análisis narrativo ni en las hipótesis de prevención. Cuando se
reporta el vector R*, Nf se excluye de la tabla o se incluye con la nota
explícita de que su valor es el residuo del ajuste de aperiodicidad.
2 La separación entre R* (responsabilidad causal estructural) y Δ (déficit de
asunción) es una de las distinciones más importantes del sistema para la
práctica. Un nodo con R* alto y Δ bajo ha asumido correctamente su
posición causal: el daño es grande pero la responsabilidad fue integrada.
Un nodo con R* bajo y Δ alto ha causado poco pero no ha asumido ni
eso: la proporción es pequeña pero la evasión es total. Las dos
situaciones tienen consecuencias completamente distintas para la
prevención y para cualquier determinación de reparación.
3 La cuantificación de ΔT_tray requiere especificar el horizonte temporal de
la proyección. Un horizonte demasiado corto subestima el daño de
trayectoria; uno demasiado largo lo sobreestima con incertidumbre
creciente. La práctica estándar es usar el horizonte que el destinatario
del análisis considera relevante para su decisión, documentado en el
expediente.

Metrología Causal · Vol. II

## PARTE II · El análisis simple: una sola serie

### Capítulo II·2
Serie II: Compliance Causal
El protocolo de evaluación de congruencia del nodo de diseño

### I. Cuándo aplica la Serie II
La Serie II responde la pregunta de Tipo 2: ¿el nodo de
diseño operó en conformidad con lo que declaró que haría? Es la
serie del compliance en su sentido más preciso — no el
cumplimiento de una norma externa sino la congruencia entre el
campo que el nodo de diseño declaró que produciría y el campo
que efectivamente produjo.
El nodo de diseño es el actor que diseñó las condiciones
estructurales bajo las cuales los demás nodos del grafo operaron:
la institución que estableció el protocolo, la organización que
diseñó el sistema de incentivos, el regulador que fijó las reglas, el
arquitecto del sistema que determinó las restricciones de
operación. La Serie II evalúa a ese nodo en términos de la brecha
entre su diseño declarado y su operación real.
La Serie II nunca se aplica sin Serie I previa. El IIC requiere
el vector R* del nodo de diseño como denominador de la fracción
de responsabilidad que la congruencia modula. Sin R*, el IIC no
tiene contexto causal: mide la brecha entre declaración y

Metrología Causal · Vol. II
operación, pero no dice cuánto pesa esa brecha en el resultado
analizado.

### II. Paso 1 · El grafo con horizonte prospectivo y el
nodo de diseño
El grafo de la Serie II tiene la misma estructura del grafo de
la Serie I con dos diferencias. La primera: el nodo de diseño N_D
debe estar identificado explícitamente antes de comenzar el Paso

### 2. No todos los grafos tienen un único nodo de diseño claro — en
algunos casos hay múltiples niveles de diseño. El mediador
identifica el nodo de diseño más relevante para la pregunta de
compliance que el destinatario plantea.
La segunda diferencia: el grafo puede incluir aristas
prospectivas — relaciones de influencia que el nodo de diseño
declaró que existirían pero que el análisis retroactivo de Serie I no
incluyó porque no se verificaron en la evidencia disponible. Estas
aristas prospectivas son el insumo del Paso 2: son los protocolos
declarados que el IIC contrasta con lo observable.
Identificación del nodo de diseño — criterios
El nodo de diseño N_D es el nodo que cumple
simultáneamente tres condiciones: (1) diseñó las condiciones
estructurales bajo las que operaron otros nodos, (2) declaró
explícitamente qué campo produciría su diseño (en
documentos, normas, contratos, o comunicaciones
verificables), y (3) tiene R* > 0 en el análisis de Serie I — es
causalmente relevante para el resultado analizado.
Si hay múltiples candidatos a nodo de diseño, el análisis de Serie II se
aplica al nodo con mayor R* entre ellos, salvo que el destinatario especifique
otro nodo explícitamente.

Metrología Causal · Vol. II

### III. Paso 2 · Cálculo del IIC
El Índice de Integridad Causal (IIC) mide la correlación
promedio entre lo que el nodo de diseño declaró que produciría y
lo que produjo. Opera sobre los protocolos declarados del nodo
de diseño que son relevantes para el resultado analizado: no sobre
todos los protocolos del nodo, sino sobre los que tienen relación
directa con la cadena causal que produjo D.
Para cada protocolo declarado k relevante para D, el
mediador calcula la correlación c_k entre la variable declarada (lo
que el protocolo prometía producir) y la variable observable (lo
que efectivamente produjo en el período analizado). La
correlación puede calcularse sobre datos cuantitativos o estimarse
cualitativamente usando la escala de la tabla siguiente.
IIC — Índice de Integridad Causal
IIC = (1/n) Σ_k c_k con c_k = corr(declarado_k,
observable_k)
n = número de protocolos declarados relevantes para D. c_k (cid:0) [−1, 1].
IIC = 1 indica congruencia total entre todos los protocolos. IIC = 0 indica
ausencia de correlación. IIC < 0 indica divergencia sistemática (el campo
real es opuesto al declarado).
Valor de Descripción Cómo se estima
c_k cualitativamente
c_k = 1.00 Congruencia El indicador de cumplimiento del
perfecta: el protocolo muestra 100% o el
protocolo produjo evaluador no puede distinguir el
exactamente lo que campo real del declarado.
declaró.
c_k (cid:0) Alta congruencia: el Las principales variables del
[0.70, 1.00) campo real sigue la protocolo se comportaron como

Metrología Causal · Vol. II
Valor de Descripción Cómo se estima
c_k cualitativamente
dirección del fueron diseñadas; hay
declarado con excepciones documentadas
desviaciones menores.
menores.
c_k (cid:0) Congruencia Algunos indicadores clave del
[0.40, 0.70) moderada: el campo protocolo funcionaron; otros no.
real se parece al Las desviaciones tienen efecto
declarado pero con material.
brechas
significativas.
c_k (cid:0) Congruencia baja: el La mayoría de los indicadores del
[0.00, 0.40) campo real diverge protocolo no produjeron lo
sustancialmente del prometido. El diseño existe en
declarado. papel.
c_k < 0 Divergencia: el El protocolo prometía controlar
campo real va en algo que en la práctica amplificó.
dirección opuesta al El diseño produjo el efecto
declarado. inverso al declarado.
Ejemplo numérico — IIC del nodo D (caso de
referencia)
Protocolos declarados relevantes (n = 3): P1 — sistema de
incentivos: c(cid:0) = 0.18 (los incentivos prometían alinear
crecimiento con riesgo; en la práctica desalinearon). P2 —
protocolo de aprobación: c(cid:0) = 0.35 (el protocolo prometía
filtrar activos tóxicos; en la práctica los aprobó con
excepciones). P3 — reporte de riesgo: c(cid:0) = 0.61 (el sistema
de reporte funcionó moderadamente).
IIC_D = (0.18 + 0.35 + 0.61) / 3 = 1.14 / 3 = 0.38. El nodo de
diseño opera con 38% de congruencia respecto a sus declaraciones. Baja
congruencia — el campo real diverge sustancialmente del declarado.

Metrología Causal · Vol. II

### IV. Paso 3 · Ajuste de pesos por IIC y recalculo de
R*
El IIC del nodo de diseño ajusta los pesos de sus aristas
estructurales salientes. La lógica del ajuste es directa: un nodo de
diseño con baja congruencia influye sobre los demás nodos con
menos efectividad de la que su posición estructural indicaría — su
influencia real es mayor que la que el campo observable refleja
porque parte de esa influencia opera a través de la brecha entre el
diseño declarado y el real.
Ajuste de pesos por IIC
w_ij(ajustado) = w_ij(base) × (1 + k × (1 − IIC_D))
k es el coeficiente de amplificación de la brecha: k (cid:0) [0.5, 1.5] según la
magnitud del resultado analizado. Valor estándar: k = 1.0. El ajuste
amplifica las aristas del nodo de diseño reflejando que la brecha entre su
campo declarado y real tiene efecto causal.
Con los pesos ajustados, se recalcula R* usando el mismo
método de potencias del Paso 3 de la Serie I sobre la nueva matriz
W(ajustado). El nuevo vector R*(ajustado) refleja la posición
causal del nodo de diseño una vez que su baja congruencia es
incorporada en la estructura del grafo.
Ejemplo numérico — Ajuste y recalculo (k = 1.0)
IIC_D = 0.38. Factor de ajuste: 1 + 1.0 × (1 − 0.38) = 1 +
0.62 = 1.62.
Aristas ajustadas de D: D→Nf pasa de 0.45 a 0.45 × 1.62 =
0.73 (luego renormalizado). D→E pasa de 0.50 a 0.81.
R*(ajustado): D = 0.5841, E = 0.2713, S = 0.1082. El ajuste por
IIC aumenta R* del nodo de diseño en 10 puntos porcentuales, reflejando
que su baja congruencia amplifica su peso causal real.

Metrología Causal · Vol. II

### V. Paso 4 · El fraude annona y el umbral de acción
El fraude annona es el corolario III del Teorema de la
Responsabilidad Causal Proporcional. Mide la posición más grave
que el sistema puede registrar en un nodo de diseño: alta
centralidad causal (R* alto), baja asunción (α bajo), y baja
congruencia (IIC bajo). El nombre proviene del término romano
annona — la gestión del suministro de grano — y la figura del
funcionario que administra un bien esencial prometiendo calidad
que no entrega.
Fraude annona
Fraude_annona_D = R*_D × (1 − α_D) × (1 −
IIC_D)
El fraude annona alcanza su máximo cuando R*_D = 1, α_D = 0, e
IIC_D = 0: el nodo es el único responsable, no ha asumido nada, y opera
en dirección opuesta a lo que declaró. En la práctica, valores superiores a
0.20 indican una posición de responsabilidad institucional grave.
Ejemplo numérico — Fraude annona del caso de
referencia
R*_D(ajustado) = 0.5841, α_D = 0.15, IIC_D = 0.38.
Fraude_annona_D = 0.5841 × (1 − 0.15) × (1 − 0.38) =
0.5841 × 0.85 × 0.62 = 0.3078.
Interpretación: el nodo de diseño genera una posición de fraude annona del
31% — dentro del rango de responsabilidad institucional grave. Este valor
supera el umbral de 0.20 que, en la mayoría de los dominios regulatorios,
activa requisitos formales de intervención.

### VI. Paso 5 · El ajuste debitor

Metrología Causal · Vol. II
El ajuste debitor es la propuesta del sistema al destinatario
sobre cómo reducir la brecha de compliance del nodo de diseño.
No es una sanción ni una prescripción: es la lectura estructural de
qué cambios en el nodo de diseño reducirían su Δ y su fraude
annona. El mediador formula el ajuste debitor en tres
componentes que corresponden a los tres orígenes de la brecha.
Componente Qué corrige Cómo se formula
del ajuste
debitor
Estructural — La brecha entre Para cada protocolo con c_k <
protocolos el campo 0.50: describir qué cambio de
declarado y el diseño elevaría c_k al rango [0.70,
real (IIC bajo). 1.00]. Expresar como condición
Corrige los estructural, no como instrucción
protocolos cuyo de conducta.
c_k es más bajo.
Procesal — El déficit de Para cada criterio de α que el nodo
acción acción del nodo de diseño no cumplió
pendiente de diseño (α (conocimiento sin acción,
bajo). Corrige oportunidades no actuadas):
los criterios de describir la acción concreta con
la Ruta B que no plazo verificable que cubriría ese
se cumplieron. criterio.
Reparatorio — La fracción Si D_total está cuantificado:
daño en curso AD_D del daño AD_D = R*_D(ajustado) ×
que el nodo de D_total. El ajuste reparatorio es
diseño generó y esa fracción no cubierta por
que no ha sido acciones verificables de α ya
abordada. registradas.
Corrige el Δ del
nodo de diseño
hacia atrás.

Metrología Causal · Vol. II

### VII. Paso 6 · El expediente de Serie II
El expediente de Serie II entrega cuatro documentos. Los
dos primeros son actualizaciones de los documentos de Serie I; los
dos siguientes son específicos de Serie II.
Documento Contenido Diferencia respecto a
Serie I
1 · Hoja de La hoja de Serie I con la Añade la sección de
calibración adición de: identificación compliance al
(actualizada) del nodo de diseño, documento base de Serie
protocolos declarados I.
relevantes con sus c_k,
coeficiente k del ajuste.
2 · Vector R* El vector R* recalculado El vector R* de Serie I es
ajustado con los pesos ajustados por el punto de referencia; el
IIC. Tabla comparativa de Serie II es el resultado
R*(base) vs R*(ajustado) del ajuste por
para cada nodo. congruencia.
3 · Mapa de Para cada protocolo Documento nuevo.
brecha IIC declarado relevante: c_k Específico de Serie II.
documentado, descripción
de la brecha, evidencia que
la sustenta. El IIC global
del nodo de diseño con su
cálculo explícito.
4 · Ajuste Los tres componentes del Documento nuevo.
debitor con ajuste debitor (estructural, Específico de Serie II.
cronograma procesal, reparatorio) con
plazos verificables para
cada acción propuesta.
Producto de salida · Capítulo II·2

Metrología Causal · Vol. II
Expediente de Serie II completo: hoja de calibración
actualizada + vector R* ajustado + mapa de brecha IIC +
ajuste debitor con cronograma. El IIC del nodo de diseño y
el fraude annona son los dos indicadores centrales que el
destinatario recibe como resultado del análisis de
compliance.
Notas al Capítulo II·2
1 El coeficiente k del ajuste de pesos por IIC tiene rango [0.5, 1.5]. El valor
estándar k = 1.0 aplica cuando la magnitud del resultado es consistente
con el dominio típico del sistema. En casos donde el resultado es
extraordinariamente grave para el dominio (colapsos sistémicos, daños
masivos, crisis institucionales) puede justificarse k > 1.0. En casos
donde el resultado es menor o el contexto es de alta incertidumbre
regulatoria genuina, puede justificarse k < 1.0. La elección de k debe
documentarse en la hoja de calibración con su justificación explícita.
2 El fraude annona tiene el nombre que tiene porque el sistema lo diseñó
para capturar una posición específica: la de quien administra un bien
esencial (un sistema de crédito, un protocolo de salud, un programa
social) declarando estándares que luego no cumple, con alta centralidad
causal en el resultado dañoso que esa brecha produce. No es una
calificación moral: es una medición estructural de la combinación de R*
alto, α bajo, e IIC bajo. El nombre orienta la interpretación, pero la
medición es formal.
3 El ajuste debitor en su componente reparatorio no es equivalente a una
determinación de reparación legal o contractual. Es la lectura estructural
de la fracción del daño que corresponde al nodo de diseño según el
análisis causal. Cualquier determinación de reparación formal requiere
instancias adicionales (jurídicas, regulatorias, arbitrales) que el análisis
causal informa, pero no reemplaza.

Metrología Causal · Vol. II

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

## PARTE III · El análisis integrado: las tres series

### Capítulo III·3
El expediente integrado completo
Qué documentos entrega, en qué formato y para qué audiencia

### I. La arquitectura del expediente integrado
El expediente integrado consolida los resultados de las tres
series en un conjunto ordenado de documentos. No es la
yuxtaposición de tres expedientes separados: es un expediente
único con una estructura interna que permite al destinatario
acceder a cualquier nivel de detalle que su audiencia o su foro
requiera, sin por ello renunciar a la coherencia del conjunto.
El expediente integrado tiene cuatro niveles de detalle. El
nivel de resumen ejecutivo es accesible a cualquier audiencia —
formula el resultado central del análisis en lenguaje del dominio
del destinatario, sin referencias al aparato técnico del sistema. El
nivel de documentos del análisis contiene los resultados formales
de las tres series — es el nivel que el destinatario usa en el foro
adversarial o en la reunión de dirección. El nivel de sustentación
contiene la hoja de calibración y los reportes de sensibilidad — es
el nivel que resiste el escrutinio técnico externo. El nivel de
verificación contiene los registros de la verificación cruzada — es

Metrología Causal · Vol. II
el nivel que el propio mediador consulta si el expediente es
revisado con posterioridad.

### II. Los documentos del expediente integrado
Docume Nivel Contenido Audiencia
nto principal
1 · Resumen Una página. El resultado Dirección
Resumen central del análisis en tres ejecutiva,
ejecutivo párrafos: qué ocurrió junta de
integrado (estructura causal en lenguaje gobierno,
del dominio), quién responde destinatario
y en qué proporción no técnico
(distribución R* en términos
absolutos si D_total está
cuantificado), y qué se
recomienda (hipótesis de
prevención más relevantes +
componentes del ajuste
debitor si aplica). Sin fórmulas,
sin referencias al aparato
técnico.
2 · Vector Análisis Tabla con R*(base), Destinatari
R* R*(ajustado) y R*(adversarial) o principal,
comparati para cada nodo, con sus abogado
vo componentes R*_neta, α y Δ. litigante,
Columna de fuente de S y α. regulador
Análisis narrativo de la
distribución: qué dice el vector
sobre la estructura causal del
sistema analizado.
3 · Mapa Análisis Los protocolos declarados Regulador,
de brecha relevantes del nodo de diseño auditor
IIC con sus c_k. El IIC global con interno,
su cálculo. La brecha entre el

Metrología Causal · Vol. II
Docume Nivel Contenido Audiencia
nto principal
campo declarado y el real comité de
descrita en lenguaje del compliance
dominio. Aplicar solo si Serie
II está en el análisis.
4 · Ajuste Análisis Los tres componentes del Consejo de
debitor ajuste debitor (estructural, administrac
con procesal, reparatorio) con sus ión,
cronogra plazos verificables. Aplicar directivo
ma solo si Serie II está en el responsable
análisis. , regulador
5 · Análisis El nivel A/B/C/D con el Tribunal,
Declaraci enunciado formal completo. árbitro,
ón de El valor exacto de ρ(θ) que lo regulador,
robustez sustenta. Aplicar solo si Serie foro
III está en el análisis. adversarial
6 · Hoja Sustentac La hoja de calibración Experto
de ión adversarial con todas las contrario,
calibració adiciones de Series II y III: revisor
n nodo de diseño identificado, técnico,
(consolida protocolos declarados con apelación
da) c_k, rangos adversariales con
sus fuentes admisibles. Es el
documento técnico completo
que sustenta todos los
resultados del expediente.
7 · Sustentac La función ρ(θ) con los puntos Experto
Reporte ión de quiebre identificados y su contrario,
de interpretación. El mapa de tribunal
sensibilida estabilidad del ranking sobre el técnico,
d hipercubo. Aplicar solo si revisión
Serie III está en el análisis. académica
8 · Verificaci Las cuatro consistencias C1– Revisión
Registro ón C4 con su resultado interna del
de (consistente/diagnosticado/c expediente,

Metrología Causal · Vol. II
Docume Nivel Contenido Audiencia
nto principal
verificació orregido). Las correcciones auditoría de
n cruzada aplicadas con su trazabilidad. calidad del
La incertidumbre residual análisis
documentada si la hay.

### III. Qué documentos entrega cada combinación
de series
No todas las combinaciones de series producen todos los
documentos. La tabla siguiente especifica qué documentos forman
el expediente según la combinación activada. Los documentos
marcados como obligatorios deben estar presentes para que el
expediente sea válido. Los marcados como condicionales se
incluyen solo si la operación que los produce se activó.
Document Solo Serie Series Series Series
o I I+II I+III I+II+III
1 · Resumen Obligatori Obligatori Obligatorio Obligatori
ejecutivo o o o
2 · Vector Solo R*(base) y R*(base) y Los tres
R* R*(base) R*(ajustad R*(adversaria vectores
comparativ o) l)
o
3 · Mapa de No aplica Obligatori No aplica Obligatori
brecha IIC o o
4 · Ajuste No aplica Obligatori No aplica Obligatori
debitor o o

Metrología Causal · Vol. II
Document Solo Serie Series Series Series
o I I+II I+III I+II+III
5 · No aplica No aplica Obligatorio Obligatori
Declaración o
de robustez
6 · Hoja de Base Base + Base + Base +
calibración compliance adversarial complianc
e +
adversarial
7 · Reporte No aplica No aplica Obligatorio Obligatori
de o
sensibilidad
8 · Registro Simplificad C1 y C2 C3 y C4 C1, C2,
de o C3 y C4
verificación

### IV. El formato del expediente según el foro
Los ocho documentos del expediente integrado tienen un
contenido invariante — lo que dicen no cambia según el foro. Lo
que cambia es el orden en que se presentan, el nivel de detalle que
se pone en primer plano, y el vocabulario del dominio que se usa
en el análisis narrativo. Esta sección establece las tres
configuraciones más frecuentes.
Configuración A — Presentación ante tribunal o árbitro
Orden: Declaración (5) → Vector R* comparativo (2) →
Hoja de calibración (6) → Reporte de sensibilidad (7) →
Resumen ejecutivo (1) como apéndice para el jurado no
técnico.

Metrología Causal · Vol. II
Énfasis: la Declaración al frente porque es el documento que
el foro evalúa primero. La hoja de calibración disponible para
revisión técnica. El resumen ejecutivo como auxiliar para
audiencias mixtas.
Vocabulario: usar el vocabulario jurídico del dominio en el análisis
narrativo. R* se comunica como 'contribución causal proporcional'. S como
'estándar del sector' o 'práctica habitual'. Δ como 'brecha de diligencia
debida'.
Configuración B — Presentación ante regulador o
auditor
Orden: Resumen ejecutivo (1) → Mapa de brecha IIC (3) →
Ajuste debitor (4) → Vector R* comparativo (2) → Hoja de
calibración (6) → Registro de verificación (8).
Énfasis: el mapa de brecha IIC y el ajuste debitor al frente
porque el regulador necesita la descripción del
incumplimiento de diseño antes que la distribución de
responsabilidad. La Declaración en el expediente solo si el
foro regulatorio la requiere explícitamente.
Vocabulario: usar terminología de compliance y regulación. R* como 'peso
en la distribución del riesgo'. IIC como 'índice de cumplimiento declarado
vs. real'. Fraude annona como 'posición de responsabilidad institucional
agravada'.
Configuración C — Presentación ante consejo de
administración o dirección
Orden: Resumen ejecutivo (1) → Ajuste debitor (4) →
Vector R* comparativo (2) → Hoja de calibración (6) en
apéndice.

Metrología Causal · Vol. II
Énfasis: el resumen ejecutivo y el ajuste debitor son los
documentos centrales para la toma de decisión de un
consejo. La distribución R* informa, pero la pregunta
práctica que el consejo necesita responder es qué debe
cambiar en el diseño del sistema — eso está en el ajuste
debitor.
Vocabulario: lenguaje de gestión y gobierno corporativo. R* como
'contribución causal al resultado'. Δ como 'brecha de asunción'. El ajuste
debitor se presenta como 'plan de acciones correctivas con responsables y
plazos'.
Producto de salida · Capítulo III·3
Expediente integrado completo en la configuración de
presentación correcta para el foro del destinatario. Los ocho
documentos están presentes según la combinación de series
activas. El orden y el vocabulario reflejan la audiencia
principal.
Notas al Capítulo III·3
1 El resumen ejecutivo de una página es el documento más difícil de producir
del expediente integrado. Requiere que el mediador traduzca resultados
técnicos precisos a lenguaje accesible sin perder la precisión de la
atribución. La regla práctica: si el resumen ejecutivo puede ser
malinterpretado de una manera que cambie la acción que el destinatario
tomaría, necesita más precisión. Si añadir más precisión lo hace ilegible
para la audiencia de dirección, necesita dos versiones: una ejecutiva y
una técnica.
2 La hoja de calibración consolidada es el documento que determina si el
expediente integrado puede ser reproducido independientemente por
otro mediador con la misma evidencia. Una hoja de calibración bien
construida contiene toda la información necesaria para que un par
metodológico pueda verificar el análisis desde el principio. Esta
propiedad de reproducibilidad es la condición de que el expediente sea
un documento científico y no solo una opinión experta.

Metrología Causal · Vol. II

## PARTE III · El análisis integrado: las tres series

### Capítulo III·4
La comunicación del análisis integrado
Resumen ejecutivo, tribunal, regulador y consejo: cuatro registros del
mismo resultado

### I. El problema de la comunicación técnica en
foros no técnicos
El análisis integrado produce resultados matemáticamente
precisos. La mayoría de los foros donde esos resultados importan
no tienen formación matemática. El tribunal que evalúa una
Declaración de nivel B no sabe qué es un hipercubo de
parámetros. El consejo de administración que recibe un ajuste
debitor no sabe qué es un eigenvector. El regulador que lee el
mapa de brecha IIC no sabe qué es la primera mediación.
El problema no es simplificar el análisis hasta perder
precisión — eso sería un error de comunicación que podría derivar
en un error de decisión. El problema es encontrar el registro
correcto para cada audiencia: el lenguaje que le permite al
destinatario entender lo suficiente para tomar la decisión que el
análisis informó, sin tener que aprender metrología causal para
hacerlo. Ese registro existe en cada dominio. Este capítulo lo
establece para los cuatro foros más frecuentes.

Metrología Causal · Vol. II

### II. El resumen ejecutivo: estructura invariante
El resumen ejecutivo tiene la misma estructura en todos los
casos y para todos los foros. Lo que cambia es el vocabulario. La
estructura tiene tres párrafos que responden tres preguntas en ese
orden exacto: qué ocurrió, quién responde y en qué proporción, y
qué debe cambiar.
Estructura del resumen ejecutivo
Párrafo 1 — Qué ocurrió: una descripción del resultado D
en términos del dominio del destinatario. Sin R*, sin
vectores, sin fórmulas. La descripción establece el resultado
específico que se analiza, su magnitud si está cuantificada, y
el sistema de actores que lo produjo.
Párrafo 2 — Quién responde y en qué proporción: la
distribución R* en lenguaje del dominio, reportando los
nodos con R* más alto y su fracción del resultado. Si D_total
está cuantificado: las fracciones AD_i. Si el análisis incluye
Series II y III: una frase sobre la congruencia del diseño y
una frase sobre el nivel de robustez de la atribución.
Párrafo 3 — Qué debe cambiar: las hipótesis de prevención
más relevantes (de Serie I) y los componentes del ajuste
debitor más urgentes (de Serie II si aplica). Formulados
como condiciones de rediseño, no como instrucciones de
conducta.
Extensión: una página. Si el caso tiene más nodos o más complejidad que
una página permite, el resumen ejecutivo reduce la granularidad — reporta
los tres nodos con mayor R*, no todos — y remite al Vector R*
comparativo para el detalle completo.

### III. El registro ante tribunal

Metrología Causal · Vol. II
La comunicación ante tribunal tiene dos audiencias
simultáneas: el juez o panel técnico que evalúa la metodología, y el
jurado o parte no técnica que necesita entender la conclusión. El
expediente atiende a los dos en paralelo con documentos
diferenciados.
Para el juez o panel técnico, los documentos centrales son la
Declaración, la hoja de calibración y el reporte de sensibilidad. La
comunicación oral del mediador sobre estos documentos debe ser
precisa y sin rodeos: el nivel de Declaración, el valor de ρ(θ), los
puntos de quiebre principales, y qué evidencia adicional cambiaría
la Declaración de nivel. Un experto técnico que cuestiona el
análisis recibe esta respuesta: los rangos [a_ij, b_ij] de la hoja de
calibración son los rangos que la evidencia admisible en este foro
justifica; si el experto contrario tiene evidencia adicional que
estrecharía esos rangos, el hipercubo se reduce y ρ(θ) sube.
Para el jurado o parte no técnica, el documento central es el
resumen ejecutivo en registro jurídico. Los términos clave tienen
una traducción estándar que el mediador usa consistentemente a
lo largo del proceso: R* se convierte en 'contribución causal
proporcional verificada', S se convierte en 'probabilidad de que
cualquier otro en esa posición hubiera actuado igual', Δ se
convierte en 'fracción de esa contribución que el nodo no ha
asumido como propia'.
La pregunta que el foro adversarial invariablemente formula y que
el mediador debe poder responder en dos oraciones: ¿qué tendría
que ser verdad para que su conclusión fuera incorrecta? La
respuesta correcta no es defender la conclusión — es describir
exactamente los puntos de quiebre del hipercubo: 'si el peso de la
arista entre N_D y Nf fuera menor a 0.28, el nodo D ya no
tendría el R* más alto'. Esa respuesta demuestra que el análisis
conoce sus propios límites, lo que es más convincente que pretender
que no los tiene.
Principio de comunicación adversarial del análisis causal

Metrología Causal · Vol. II

### IV. El registro ante regulador
La comunicación ante regulador tiene énfasis diferente al
tribunal. El regulador no evalúa si la atribución resiste una
impugnación adversarial — evalúa si el diseño institucional que
produjo el resultado debe ser modificado y cómo. Los
documentos centrales son el mapa de brecha IIC y el ajuste
debitor.
El registro regulatorio traduce el IIC como tasa de
cumplimiento declarado versus real: un IIC de 0.38 se comunica
como 'el sistema operó con 38% de congruencia respecto a sus
estándares declarados'. El fraude annona se comunica como
'índice de responsabilidad institucional del diseño': un valor de
0.31 indica que el nodo de diseño concentra una posición de
responsabilidad grave según los tres criterios del sistema
(centralidad causal, asunción y congruencia).
El ajuste debitor se comunica en el registro regulatorio como
un plan estructurado de tres componentes con plazos: qué
protocolos deben rediseñarse (componente estructural), qué
acciones deben tomarse de forma inmediata (componente
procesal), y qué fracción del daño debe ser abordada (componente
reparatorio). El regulador puede adoptar, modificar o rechazar
cada componente de forma independiente.

### V. El registro ante consejo de administración
La comunicación ante consejo tiene el registro más sintético.
El consejo necesita tres respuestas: qué ocurrió, qué posición
ocupa la organización en la distribución de responsabilidad, y qué
debe decidir. Los documentos centrales son el resumen ejecutivo
y el ajuste debitor en su componente estructural.
El vector R* se presenta ante el consejo como una tabla de
tres columnas: nodo, fracción del resultado, y acción

Metrología Causal · Vol. II
recomendada. Para cada nodo con R* relevante: su contribución
causal en porcentaje, si esa contribución es mayor o menor a la del
ciclo anterior si hay seguimiento, y la acción del ajuste debitor que
le corresponde. El consejo no necesita saber cómo se calculó R*
— necesita saber qué decisión tomar sobre la base de R*.
La Declaración de robustez, si aplica, se comunica ante el
consejo en términos de riesgo: 'la atribución tiene robustez
sustancial (nivel B): en más del 90% de los escenarios consistentes
con la evidencia disponible, la posición del nodo principal se
mantiene'. Ese lenguaje le permite al consejo evaluar el riesgo de
actuar sobre la base del análisis sin necesitar entender qué es un
hipercubo.
Producto de salida · Capítulo III·4
Versión del expediente calibrada para el foro principal del
destinatario: vocabulario del dominio en el análisis narrativo,
documentos en el orden de la configuración correcta (A, B o
C del Capítulo III·3), y resumen ejecutivo en el registro
apropiado. Los documentos técnicos del nivel de
sustentación están disponibles en apéndice para el escrutinio
experto.
Notas al Capítulo III·4
1 La traducción de términos técnicos al vocabulario del dominio requiere
una precaución importante: la traducción debe ser consistente a lo largo
de todo el proceso del caso. Si R* se traduce como 'contribución causal
proporcional' en el resumen ejecutivo, debe traducirse igual en el análisis
oral ante el tribunal y en cualquier documento adicional que el análisis
genere. La inconsistencia terminológica en un proceso adversarial es una
vulnerabilidad que el experto contrario puede explotar para cuestionar
la coherencia del análisis.
2 La pregunta de los puntos de quiebre — qué tendría que ser verdad para
que la conclusión cambiara — es la más poderosa en cualquier foro

Metrología Causal · Vol. II
porque demuestra que el análisis conoce sus propios límites con
precisión. Un análisis que no puede responder esa pregunta no tiene
robustez verificable. Un análisis que la responde con precisión — 'si el
peso de esta arista fuera menor a X, el ranking cambiaría' — demuestra
que la robustez fue calculada y no solo afirmada.

Metrología Causal · Vol. II

## PARTE III · El análisis integrado: las tres series

### Capítulo III·5
Los límites del expediente integrado
Qué puede responder el análisis y qué no puede responder por diseño

### I. Por qué comunicar los límites es parte del
protocolo
Un análisis que pretende responder más preguntas de las que
puede responder con rigor es menos útil que uno que conoce sus
límites con precisión. El destinatario que recibe un análisis sin
límites explícitos no tiene manera de saber cuándo confiar en el
resultado y cuándo buscar información adicional. El destinatario
que recibe un análisis con sus límites claramente establecidos sabe
exactamente qué preguntas el análisis responde con solidez, cuáles
responde con incertidumbre documentada, y cuáles están fuera de
su alcance por diseño.
Comunicar los límites no es una debilidad del análisis: es su
forma de integridad metrológica. La metrología establece no solo
qué mide un instrumento sino bajo qué condiciones es válida esa
medición y cuándo deja de serlo. Este capítulo establece esas
condiciones para el análisis integrado.

Metrología Causal · Vol. II

### II. Lo que el expediente integrado puede
responder
Pregunta Instrumento Condición de validez
que la
responde
¿Quién fue Vector R*(base) El grafo incluye todos los nodos
condición de Serie I con capacidad causal. El resultado
necesaria de D está específicamente definido.
este resultado
específico y en
qué
proporción?
¿Cuánto del R*_neta = R* × S está correctamente derivado
resultado es (1−S) de Serie I desde el Hijo dominante o los
atribuible al criterios universales con evidencia
actor específico suficiente.
vs. al campo que
lo contenía?
¿Cuánto causó Δ = R* × (1−α) α está correctamente estimado
cada nodo vs. de Serie I desde Ruta A, B o C con evidencia
cuánto asumió? documentada.
¿El nodo de IIC de Serie II Los protocolos declarados del
diseño operó en nodo de diseño están
conformidad identificados y son verificables. El
con sus período analizado es el mismo
estándares que el del grafo base.
declarados?
¿Qué fracción AD_i = R* × D_total ha sido cuantificado por
del daño D_total el destinatario en unidades
corresponde consistentes.
causalmente a
cada nodo?

Metrología Causal · Vol. II
Pregunta Instrumento Condición de validez
que la
responde
¿Puede Declaración El grafo adversarial refleja solo
sostenerse la A/B/C/D de evidencia admisible en el foro. El
atribución ante Serie III hipercubo fue evaluado en todos
impugnación los puntos requeridos.
con la evidencia
disponible?
¿Qué rediseño Hipótesis de Las hipótesis están ancladas en
estructural prevención de cambios verificables del grafo, no
reduciría la Serie I + en instrucciones de conducta.
responsabilidad componente
causal de los estructural del
nodos críticos ajuste debitor
en sistemas de Serie II
futuros?

### III. Lo que el expediente integrado no puede
responder por diseño
Los límites del análisis no son limitaciones contingentes que
una mejor evidencia o un análisis más extenso resolvería. Son
límites estructurales del instrumento: preguntas que el sistema no
está diseñado para responder, independientemente de la calidad de
la evidencia o la extensión del análisis.
Pregunta que Por qué no la Qué instrumento la
el análisis no responde respondería
responde
¿El nodo tuvo El sistema mide Análisis jurídico de dolo y
intención de responsabilidad culpa. Historia clínica de
causal estructural, no

Metrología Causal · Vol. II
Pregunta que Por qué no la Qué instrumento la
el análisis no responde respondería
responde
producir el intención. R* mide estado mental. Evaluación
resultado? posición en el grafo psicológica forense.
— un nodo puede
tener R* alto sin
intención y R* bajo
con intención plena.
La intención es
irrelevante para la
causalidad y el
sistema no la
incorpora por
diseño.
¿El resultado El sistema describe Análisis jurídico de equidad.
fue justo o qué fue: quién causó Evaluación ética. Decisión
injusto? qué, en qué de la autoridad competente.
proporción. No
prescribe qué debe
ser. La justicia del
resultado — si la
distribución es
equitativa, si el daño
merece reparación
— es una pregunta
normativa que el
sistema informa pero
no responde.
¿Qué habría El sistema analiza el Simulación de escenarios.
ocurrido si el grafo real del caso Modelado prospectivo.
sistema hubiera analizado. Las Análisis de política
sido diseñado hipótesis de comparada.
de manera prevención son
diferente? condicionales
estructurales sobre
sistemas futuros
similares — no son

Metrología Causal · Vol. II
Pregunta que Por qué no la Qué instrumento la
el análisis no responde respondería
responde
contrafácticos sobre
el caso analizado. La
pregunta 'qué habría
pasado si N_D
hubiera diseñado
diferente' no tiene
respuesta con el
mismo nivel de rigor
que R*(base).
¿Cuánto vale el El sistema distribuye Peritaje económico.
daño en el daño en Actuaría. Valoración de
unidades proporciones (AD_i daños en jurisdicción
monetarias o de = R*_i × D_total) competente.
bienestar? pero no cuantifica
D_total. La
cuantificación del
daño requiere
instrumentos de
valoración
económica, actuarial
o clínica que son
externos al análisis
causal.
¿El nodo va a El sistema describe Evaluación de riesgo de
repetir la la posición causal reincidencia. Análisis de
conducta en el histórica del nodo. trayectoria longitudinal (Tipo
futuro? La predicción de 5 del sistema).
conducta futura
requiere un modelo
prospectivo que el
análisis causal no
provee. Las hipótesis
de prevención no
son predicciones de
conducta — son

Metrología Causal · Vol. II
Pregunta que Por qué no la Qué instrumento la
el análisis no responde respondería
responde
condiciones
estructurales de
rediseño.
¿El resultado El sistema establece Evaluación psicológica del
fue evitable? que el nodo fue estado interno en el
condición necesaria momento del acto. Análisis
del resultado — sin del SDO con ECO
el nodo, el resultado completo.
no habría ocurrido
en esa forma
específica. Pero no
establece si el nodo
tenía la capacidad
real de actuar
diferente dado su
estado interno en ese
momento. Esa
pregunta requiere
acceso a v_t del
nodo en el instante
del colapso, que el
expediente puede
aproximar pero no
determinar con
certeza.

### IV. El protocolo de comunicación de límites
Cuando el destinatario formula una pregunta que el análisis
no puede responder, el mediador no intenta responderla con el
instrumento equivocado. Comunica el límite con precisión y
orienta al destinatario hacia el instrumento que sí puede
responderla.

Metrología Causal · Vol. II
La comunicación del límite tiene tres componentes. El
primero: confirmar que la pregunta es importante y legítima — no
es un defecto del destinatario formularla. El segundo: explicar por
qué el análisis causal no la responde — no por falta de evidencia
sino por diseño del instrumento. El tercero: señalar qué
instrumento externo al sistema respondería esa pregunta y qué
información del expediente integrado ese instrumento necesitaría
como insumo.
Este tercer componente es el más valioso para el
destinatario. El análisis causal integrado no opera en el vacío: es
un insumo para decisiones más amplias que requieren otros
instrumentos. El mediador que conoce con precisión los límites
del suyo está en posición de articular cómo se conecta con los
demás — y esa articulación es parte del valor del análisis.
Ejemplo de comunicación de límite — la pregunta de
intención
Pregunta del destinatario: '¿El director sabía que esto iba a
pasar? ¿Lo hizo a propósito?'
Comunicación incorrecta: 'El análisis muestra que R* del
director es 0.58, lo que indica alta responsabilidad causal.
Eso sugiere que tuvo un papel central en el resultado.' (La
respuesta usa R* para inferir intención, que es exactamente
lo que R* no mide.)
Comunicación correcta: 'El análisis establece que el director fue condición
necesaria del 58% del resultado — independientemente de su intención. Lo
que el análisis no puede establecer es si el director tuvo intención de producir
ese resultado: esa pregunta requiere un análisis jurídico de dolo o un peritaje
psicológico forense. Lo que el expediente sí puede aportar a ese análisis
externo es el mapa de oportunidades de conocimiento del director: los
momentos documentados donde tenía información sobre el resultado
potencial y las decisiones que tomó en cada uno.'

Metrología Causal · Vol. II
Producto de salida · Capítulo III·5
Protocolo de comunicación de límites documentado en el
expediente integrado: la tabla de lo que el análisis responde
y lo que no responde, con los instrumentos externos que
complementan el análisis causal para cada pregunta fuera de
alcance. Este protocolo acompaña al resumen ejecutivo
como apéndice de alcance del análisis.
Notas al Capítulo III·5
1 El límite más frecuentemente violado en la práctica es el de la intención.
El análisis causal mide posición estructural — cuánto del resultado se
explica por la posición del nodo en el grafo. Es tentador para el
destinatario, y a veces para el propio mediador, interpretar R* alto como
evidencia de intención. Esa interpretación es un error metrológico: R*
alto puede coexistir con intención nula (un nodo que ocupa una
posición estructural crítica sin ningún conocimiento de sus
consecuencias) e intención alta puede coexistir con R* bajo (un nodo
que quiso el resultado pero que no fue condición necesaria de él). La
confusión entre causalidad e intención es uno de los errores más
costosos que el análisis integrado puede producir si el mediador no
comunica este límite con claridad.
2 El límite sobre la evitabilidad — si el resultado era evitable — tiene una
relación especial con el parámetro α. α mide la asunción del acto: cuánto
del acto el nodo integró como propio mediante conducta verificable.
Un α bajo no significa que el resultado no era evitable — significa que
el nodo no actuó sobre esa posibilidad. La pregunta de si el nodo podía
actuar diferente dado su estado interno v_t en ese momento es una
pregunta distinta que requiere acceso a la dimensión interior del ego. El
SDO con ECO completo provee esa dimensión cuando está disponible.
Cuando no lo está, α es la mejor aproximación exterior disponible.
3 La pregunta sobre qué habría ocurrido con un diseño diferente —el
contrafáctico de diseño— tiene una respuesta parcial pero útil que el
análisis sí puede proveer: las hipótesis de prevención de la Serie I. Estas
hipótesis dicen qué cambio estructural en el grafo reduciría R* del nodo
crítico en sistemas futuros similares. No son contrafácticos sobre el caso

Metrología Causal · Vol. II
analizado, pero son la mejor aproximación a 'qué habría cambiado si el
sistema se hubiera diseñado diferente' que el análisis puede producir de
forma rigurosa.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·1
Los cuatro axiomas de la responsabilidad
causal proporcional
Enunciado formal y justificación de cada axioma

### I. La función del sistema axiomático
El Teorema de la Responsabilidad Causal Proporcional
descansa sobre cuatro axiomas. Los axiomas no son hipótesis
empíricas que pueden ser verificadas o refutadas con datos — son
condiciones que cualquier distribución de responsabilidad debe
satisfacer para ser interpretable como distribución de
responsabilidad causal proporcional en el sentido de este sistema.
Su función es doble: determinan de manera única la distribución
correcta (el Capítulo IV·2 demuestra que solo el eigenvector las
satisface simultáneamente) y permiten diagnosticar exactamente
qué propiedad se viola cuando una distribución alternativa es
propuesta.
Los cuatro axiomas son independientes entre sí: ninguno se
sigue de los demás. Y son suficientes en conjunto: cualquier
distribución que los satisface simultáneamente es el eigenvector.
La demostración de ambas propiedades — independencia y
suficiencia conjunta — forma el núcleo del Capítulo IV·2.

Metrología Causal · Vol. II

### II. Axioma A1 — Eficiencia
Axioma A1 · Eficiencia
Σᵢ R*(i) = 1
La totalidad del resultado D está distribuida entre los nodos causalmente
necesarios. Ninguna fracción se pierde ni se inventa.
La eficiencia exige que la distribución cierre: la suma de las
responsabilidades causales de todos los nodos es exactamente el
resultado total. No puede ser menor — eso significaría que parte
del resultado no tiene origen causal asignado, lo que contradice
que el grafo incluye todos los nodos causalmente relevantes. No
puede ser mayor — eso significaría que el sistema atribuye más
responsabilidad de la que el resultado contiene, lo cual es
metrológicamente incoherente.
La eficiencia no es una convención aritmética de
normalización. Es la condición de que el análisis causal es
completo: si el grafo es correcto y todos los nodos causalmente
relevantes están incluidos, la suma de sus pesos debe ser
exactamente uno. Una distribución que no cumple A1 señala que
el grafo está incompleto o que la distribución se calculó
incorrectamente.

### III. Axioma A2 — Causalidad necesaria
Axioma A2 · Causalidad necesaria
R*(i) > 0 (cid:0) i es condición sine qua non de D
El nodo i tiene responsabilidad causal positiva si y solo si su eliminación
del grafo produce un resultado D' tal que D' ≠ D en su forma específica.
Los nodos causalmente irrelevantes tienen R* = 0.

Metrología Causal · Vol. II
La causalidad necesaria vincula la distribución de
responsabilidad a la estructura causal del grafo. Un nodo que no
es condición necesaria de D — cuya eliminación dejaría D intacto
— no tiene responsabilidad causal en D. Asignarle R* > 0 violaría
el principio más básico de la causalidad: no se es responsable de
algo que hubiera ocurrido igual sin uno.
La dirección inversa del bicondicional es igualmente
importante: un nodo que sí es condición necesaria de D debe tener
R* > 0. Una distribución que asigna R* = 0 a un nodo que es
condición sine qua non viola A2, aunque sea aritméticamente
coherente. Esta exigencia es la condición que previene que el
análisis omita actores con alta responsabilidad estructural por
razones extra-metodológicas.

### IV. Axioma A3 — Centralidad recursiva
Axioma A3 · Centralidad recursiva
R*(i) es proporcional a Σ(cid:0) w_ij · R*(j)
La responsabilidad de un nodo es proporcional a la suma ponderada de las
responsabilidades de los nodos sobre los que ejerce influencia causal. La
responsabilidad se propaga recursivamente a través de toda la estructura del
grafo.
La centralidad recursiva captura la dimensión más
importante de la responsabilidad en sistemas complejos: que la
influencia no es solo directa. Un nodo que influye sobre nodos
intermedios que a su vez influyen sobre el resultado final tiene
responsabilidad causal que va más allá de sus aristas directas al
nodo sumidero. El diseñador que produce el incentivo que
produce la conducta que produce el daño es responsable no solo
de su arista directa al daño sino de toda la cadena causal que su
diseño habilitó.

Metrología Causal · Vol. II
Sin la centralidad recursiva, el análisis causal sería superficial:
mediría quién actuó en el último paso, ignorando quién construyó
el sistema que hizo posible ese último paso. A3 es el axioma que
hace al sistema capaz de identificar la responsabilidad estructural
de los nodos de diseño, que frecuentemente no tienen aristas
directas al resultado, pero tienen R* alto porque su influencia se
ejerce a través de múltiples niveles del grafo.

### V. Axioma A4 — Monotonicidad
Axioma A4 · Monotonicidad
Si w_ji aumenta → R*(i) no decrece
Si la influencia del nodo j sobre el nodo i se intensifica, la responsabilidad
causal de i no puede disminuir. Más influencia causal recibida no reduce la
centralidad causal del receptor.
La monotonicidad es la condición de coherencia ordinal del
sistema. Si un nodo recibe más influencia causal de otros nodos,
su posición causal en el resultado no puede ser menor que antes.
Una distribución que viola A4 produciría la paradoja de que un
nodo con más influencia sobre el resultado tiene menos
responsabilidad, lo que contradice el principio de que la
responsabilidad causal crece con la influencia estructural.
A4 también tiene una consecuencia importante para el
análisis de sensibilidad de la Serie III: cuando los pesos del grafo
varían dentro de sus rangos admisibles, el ranking de los nodos
solo puede cambiar de maneras consistentes con la
monotonicidad. Un nodo no puede ganar influencia y perder
posición en el ranking simultáneamente.

Metrología Causal · Vol. II
Axioma Nombre Condición Lo que viola si se
relaja
A1 Eficiencia Σᵢ R*(i) = 1 La distribución no cubre
todo el resultado o lo
excede. El análisis es
incompleto o
sobrecontribuyente.
A2 Causalidad R*(i) > 0 (cid:0) Nodos irrelevantes
necesaria condición reciben responsabilidad, o
sine qua non nodos necesarios son
ignorados. El vínculo
entre causalidad y
responsabilidad se rompe.
A3 Centralidad R*(i) (cid:0) Σ(cid:0) La responsabilidad es solo
recursiva w_ij · R*(j) directa. Los nodos de
diseño con influencia
indirecta son invisibles al
análisis.
A4 Monotonicidad ↑w_ji (cid:0) Más influencia produce
R*(i) no menos responsabilidad.
decrece El análisis viola
coherencia ordinal básica.
Producto de salida · Capítulo IV·1
Los cuatro axiomas formalmente enunciados con su
justificación. Cualquier distribución de responsabilidad
causal proporcional debe satisfacerlos simultáneamente. El

### Capítulo IV·2 demuestra que exactamente una distribución
los satisface: el eigenvector principal normalizado de W.
Notas al Capítulo IV·1
1 La independencia de los cuatro axiomas puede verificarse mostrando que
para cada axioma existe una distribución que satisface los tres restantes,

Metrología Causal · Vol. II
pero viola ese axioma específico. Para A3: la distribución de pesos
directos al sumidero (sin propagación recursiva) satisface A1, A2 y A4,
pero viola A3. La demostración completa de independencia está en el
apéndice de la Axiomatización del Sistema de la Doble Mediación.
2 El axioma A2 formula la condición sine qua non en términos de forma
específica del resultado: 'D' ≠ D en su forma específica'. Esta precisión
es metrológicamente crítica. Si un nodo es eliminado del grafo y el
resultado ocurre con menor magnitud, pero la misma forma, el nodo no
es condición sine qua non bajo A2. Si el resultado ocurre en una forma
diferente, sí lo es. La distinción entre magnitud y forma del resultado
tiene consecuencias directas para la aplicación en dominios donde la
forma del resultado importa más que su magnitud.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·2
Teorema de la Responsabilidad Causal
Proporcional
Existencia, unicidad y demostración

### I. El enunciado del teorema
Teorema de la Responsabilidad Causal Proporcional
Sea G = (N, E, W) un grafo causal dirigido con matriz de
adyacencia ponderada W ≥ 0 e irreducible sobre N(cid:0){Nf},
donde Nf es el nodo sumidero que representa el resultado
D.
Existe una única distribución R*: N → [0,1] con Σᵢ R*(i) =
1 que satisface simultáneamente los axiomas A1, A2, A3 y
A4.
Esa distribución es el eigenvector principal normalizado de W: el único
vector positivo v tal que W·v = λ_max·v, normalizado para que ||v||(cid:0)
= 1.

### II. Lema previo: el Teorema de Perron-Frobenius

Metrología Causal · Vol. II
La demostración del teorema descansa sobre el Teorema de
Perron-Frobenius para matrices no negativas e irreducibles. El
lema que este capítulo usa en su forma operativa es el siguiente.
Lema PF (Perron-Frobenius, forma operativa)
Sea W una matriz cuadrada n×n con entradas no negativas
(W ≥ 0) e irreducible. Entonces:
(i) W tiene un eigenvalor real positivo λ_max > 0,
estrictamente mayor que el módulo de cualquier otro
eigenvalor: λ_max > |λᵢ| para todo i ≠ max.
(ii) El eigenvector correspondiente a λ_max es único (salvo
escala) y tiene todas sus entradas estrictamente positivas: v_i
> 0 para todo i.
(iii) El método de potencias converge a v desde cualquier vector inicial
positivo: W^k·u / ||W^k·u||₁ → v cuando k → ∞.
La irreducibilidad de W es la condición que garantiza las tres
propiedades del lema. Un grafo es irreducible si y solo si su matriz
de adyacencia es irreducible — es decir, si desde cualquier nodo
existe un camino dirigido al nodo sumidero Nf. Esta es
exactamente la condición de completitud del grafo verificada en el
Paso 2 del protocolo.

### III. Demostración: el eigenvector satisface los
cuatro axiomas
La primera parte muestra que la distribución eigenvectorial
satisface A1, A2, A3 y A4.
A1 — Eficiencia: el eigenvector v está normalizado por
construcción: ||v||(cid:0) = Σᵢ v_i = 1. La normalización en la norma
ℓ¹ asegura exactamente que la suma de todas las entradas es uno.

Metrología Causal · Vol. II
R*(i) = v_i / ||v||(cid:0) satisface A1 por definición del
procedimiento de normalización.
A2 — Causalidad necesaria: por el lema PF(ii), todas las
entradas del eigenvector son estrictamente positivas: v_i > 0 para
todo i. Esto significa que todo nodo del grafo tiene R* > 0. La
dirección '→' (si R* > 0 entonces condición necesaria) se garantiza
porque el grafo por construcción contiene solo nodos causalmente
relevantes para D. La dirección '←' (si es condición necesaria
entonces R* > 0) se satisface por PF(ii).
A3 — Centralidad recursiva: la ecuación eigenvectorial W·v
= λ_max·v dice exactamente que v_i = (1/λ_max) · Σ(cid:0) w_ij · v_j.
Es decir: el valor de v_i es proporcional a la suma ponderada de
los valores v_j de los nodos sobre los que i ejerce influencia. Esto
es exactamente A3. La ecuación eigenvectorial es la forma
matricial de A3.
A4 — Monotonicidad: si el peso w_ji aumenta, la entrada
(W)_ji de la matriz W aumenta. Por el teorema de Perron para
matrices con entradas no negativas, el eigenvalor principal λ_max
es una función creciente de cada entrada de W. Y la entrada v_i
del eigenvector principal es proporcional a la suma de los pesos de
las aristas que entran a i, ponderados por los valores
eigenvectoriales de sus fuentes — por lo tanto, v_i no puede
decrecer cuando w_ji aumenta.

### IV. Demostración: unicidad por relajación de
axiomas
La segunda parte demuestra que relajar cualquier axioma
permite distribuciones distintas del eigenvector que satisfacen los
tres axiomas restantes.
Si se relaja A1: la distribución v' = 2·v satisface A2, A3 y A4
pero tiene Σ v'_i = 2 ≠ 1. Cualquier múltiplo escalar positivo del

Metrología Causal · Vol. II
eigenvector satisface A2–A4, pero no A1. La normalización ℓ¹
selecciona el único representante que satisface A1.
Si se relaja A2: la distribución que asigna R* = 0 al nodo de
mayor eigenvector y distribuye su peso uniformemente entre los
demás satisface A1, A3 (modificada) y A4, pero viola A2 porque
un nodo causalmente necesario tiene R* = 0.
Si se relaja A3: cualquier distribución proporcional al grado
de salida (número de aristas salientes de cada nodo, sin
ponderación recursiva) satisface A1, A2 y A4, pero viola A3
porque ignora la propagación recursiva de la influencia.
Si se relaja A4: la distribución que invierte el ranking del
eigenvector satisface A1 y A2, pero viola A4 porque los nodos con
mayor influencia recibida tienen menor responsabilidad. Los
cuatro casos muestran que cada axioma excluye una familia de
distribuciones distintas del eigenvector. Juntos, los cuatro no dejan
lugar para ninguna otra distribución.
La demostración por unicidad desde la relajación de axiomas no
solo prueba que el eigenvector es la respuesta correcta: muestra con
precisión por qué cada axioma es necesario. Un sistema que
propone una distribución de responsabilidad distinta del
eigenvector está, explícitamente, violando al menos uno de los
cuatro axiomas. Identificar cuál axioma viola una distribución
alternativa permite al mediador articular exactamente en qué
sentido esa alternativa es metodológicamente inadecuada.
Función de la demostración por unicidad en el contexto
adversarial

### V. La condición de irreducibilidad: qué pasa si no
se cumple
El teorema requiere que W sea irreducible. Si el grafo tiene
nodos desde los que no existe camino al sumidero, W es reducible

Metrología Causal · Vol. II
y el eigenvector principal puede no ser único o puede no tener
todas sus entradas positivas.
El protocolo maneja esta situación en el Paso 2 del análisis:
cualquier nodo sin camino al sumidero se elimina del grafo antes
del cálculo. Con esa eliminación, la submatriz resultante es
irreducible y el teorema aplica. Los nodos eliminados tienen R* =
0 por A2 — no son condición necesaria de D.
Producto de salida · Capítulo IV·2
Demostración completa del Teorema de la Responsabilidad
Causal Proporcional: el eigenvector principal normalizado de
W es la única distribución que satisface A1–A4
simultáneamente. La demostración tiene dos partes:
satisfacción directa de los cuatro axiomas (por verificación
con el lema PF) y unicidad (por demostración desde
relajación de axiomas).
Notas al Capítulo IV·2
1 La demostración de A2 presenta una sutileza técnica: el lema PF garantiza
que todas las entradas del eigenvector son positivas cuando la matriz es
irreducible. Pero la condición A2 exige que las entradas sean positivas
exactamente para los nodos sine qua non, y cero para los que no lo son.
La reconciliación es que el protocolo elimina del grafo los nodos no-
sine-qua-non antes del cálculo. Con esa eliminación, todos los nodos
presentes son sine qua non y el eigenvector les asigna entradas positivas.
2 La versión del Teorema de Perron-Frobenius que este capítulo usa es para
matrices no negativas e irreducibles, no necesariamente estrictamente
positivas. La irreducibilidad de la matriz (en el sentido de que el grafo
subyacente es fuertemente conexo al sumidero) es suficiente para
garantizar el eigenvector positivo único sin necesitar que todas las
entradas de W sean estrictamente positivas.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·3
Corolario I · La descomposición de R*
Derivación formal de R*_neta y R*_sistémica desde el teorema
principal

### I. La pregunta que el corolario responde
El teorema principal establece que R*(i) mide la contribución
causal estructural del nodo i al resultado D. Esta medición no
distingue entre dos fuentes de esa contribución que son
metrológicamente distintas: la parte que proviene del ego
específico del nodo y la parte que habría producido cualquier otro
actor en esa misma posición estructural. El Corolario I formaliza
esa descomposición.

### II. La definición de S como operador de
descomposición
S_i (cid:0) [0,1] mide la probabilidad de que cualquier otro nodo
con el mismo perfil en la misma posición estructural que i hubiera
producido el mismo resultado. S_i = 1 significa que el acto era
completamente determinado por el campo. S_i = 0 significa que
el acto era completamente idiosincrático.

Metrología Causal · Vol. II
La interpretación ontológica de S está en el Capítulo I·4 de
este volumen: S_i es la lectura exterior de la posición de v_t en φ(cid:0)
del ego i. Cuando c domina φ(cid:0) (S alto), el acto emerge
principalmente del campo heredado. Cuando v_t domina φ(cid:0) (S
bajo), el acto emerge principalmente de la posición propia de la
voluntad.

### III. La derivación del Corolario I
Corolario I · Descomposición de R*
Dado el Teorema IV·2 y la definición de S_i como la
fracción de R*(i) atribuible al campo c:
R*_neta_i = R*(i) × (1 − S_i) [fracción idiosincrática]
R*_sistémica_i = R*(i) × S_i [fracción del campo]
R*(i) = R*_neta_i + R*_sistémica_i
La descomposición es exhaustiva: los dos componentes suman exactamente
R*(i). La fracción idiosincrática mide cuánto del peso causal de i es
atribuible a ese ego específico. La fracción sistémica mide cuánto habría
producido cualquier otro en esa posición.
La derivación es directa desde el teorema y la definición de
S. R*(i) es la responsabilidad causal total del nodo i. S_i es la
fracción de esa responsabilidad que el campo explica. Por tanto (1
− S_i) es la fracción que el ego específico explica. R*_neta_i =
R*(i) × (1 − S_i) es esa fracción idiosincrática — el producto de la
responsabilidad total por la proporción que no puede explicarse
por el campo.

### IV. Propiedades de la descomposición

Metrología Causal · Vol. II
Propiedad 1 — Σᵢ R*_neta_i ≤ 1: la suma de las fracciones
idiosincráticas de todos los nodos es siempre menor o igual a uno.
La diferencia 1 − Σᵢ R*_neta_i = Σᵢ R*_sistémica_i es la
responsabilidad sistémica total del campo c.
Propiedad 2 — R*_neta_i = 0 cuando S_i = 1: si el acto del
nodo era completamente predecible desde el campo, su fracción
idiosincrática es cero. El nodo tiene R*(i) > 0 (fue condición
necesaria del resultado) pero R*_neta_i = 0 (cualquier otro habría
producido lo mismo). Esta es la posición del ejecutor
completamente sustituible.
Propiedad 3 — R*_neta_i = R*(i) cuando S_i = 0: si el acto
era completamente idiosincrático, toda la responsabilidad causal es
atribuible al ego específico. Nadie más en esa posición habría
producido ese resultado.
Producto de salida · Capítulo IV·3
Corolario I formalmente derivado: la descomposición R*(i)
= R*_neta_i + R*_sistémica_i con sus tres propiedades. La
fracción idiosincrática R*_neta_i = R*(i) × (1−S_i) es la
medida de responsabilidad causal que el sistema atribuye al
ego específico, excluyendo la parte que cualquier otro en esa
posición también habría producido.
Notas al Capítulo IV·3
1 El Corolario I tiene una consecuencia importante para la comunicación en
contextos donde la responsabilidad colectiva está en cuestión. Cuando
Σᵢ R*_neta_i es muy menor a 1 — cuando la responsabilidad sistémica
del campo es muy alta — el análisis puede y debe comunicar que el
problema es estructural: el resultado habría ocurrido en gran medida
independientemente de quiénes fueran los actores individuales. Esa
comunicación no exime a los individuos de su R*_neta — exige que el
análisis correctivo se dirija también a la estructura del campo.

Metrología Causal · Vol. II
2 La distinción entre R*_neta y R*_sistémica tiene un paralelo directo con la
distinción jurídica entre responsabilidad individual y responsabilidad
institucional. R*_neta corresponde aproximadamente a la
responsabilidad del individuo por encima y más allá del estándar del
sistema. R*_sistémica corresponde a la responsabilidad de quien diseñó
el sistema que produjo el comportamiento del individuo.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·4
Corolario II · El déficit de asunción Δ
Derivación formal del déficit desde el teorema principal

### I. La pregunta que el corolario responde
El Corolario I descompone R* entre la fracción del ego y la
fracción del campo. El Corolario II aborda una segunda
dimensión: la brecha entre lo que el nodo causó (R*) y lo que el
nodo integró como propio mediante conducta verificable (α). Esta
brecha — el déficit de asunción Δ — es la medida de cuánto del
impacto causal del nodo no fue reconocido ni abordado por ese
nodo.

### II. La definición de α como operador de
integración
α_i (cid:0) [0,1] mide la fracción de R*(i) que el nodo i integró
como propia mediante acciones verificables orientadas a producir,
modificar o mitigar el resultado. α_i = 1 significa asunción
completa. α_i = 0 significa que el nodo no asumió nada a pesar de
haber sido condición necesaria del resultado.

Metrología Causal · Vol. II
La interpretación ontológica de α es el grado en que la
segunda mediación φ(cid:0) operó sobre los colapsos del nodo: cuánto
de lo que φ(cid:0) produjo fue integrado en I(t) como parte constitutiva
del ego. La relación entre α y φ(cid:0) es una derivación formal
establecida en La transformación formal (Cap. 2.3).

### III. La derivación del Corolario II
Corolario II · El déficit de asunción
Dado el Teorema IV·2 y la definición de α_i como la
fracción de R*(i) que el nodo i integró como propia:
Δ_i = R*(i) × (1 − α_i) [déficit de asunción del nodo i]
Δ_total = Σᵢ Δ_i [déficit sistémico de asunción]
Δ_i mide la fracción de R*(i) que el nodo causó, pero no integró como
propia. Δ_i > 0 indica déficit. Δ_i < 0 indica inversión causal: el nodo
asumió más de lo que causó. Δ_i = 0 indica equilibrio.

### IV. Los tres casos de Δ y su interpretación
Signo Condición Nombre Interpretación operativa
de formal del
Δ_i patrón
Δ_i > R*(i) > α_i · Déficit de El nodo causó más de lo que
0 R*(i) asunción asumió. La brecha puede
originarse en evasión
deliberada (φ(cid:0) capaz pero no
ejercida) o en bloqueo
ontológico (φ(cid:0)
estructuralmente impedida).

Metrología Causal · Vol. II
Signo Condición Nombre Interpretación operativa
de formal del
Δ_i patrón
El SDO distingue los dos
casos.
Δ_i = α_i = 1 o R*(i) Equilibrio El nodo asumió exactamente
0 = 0 de lo que causó. El equilibrio
asunción puede ocurrir en cualquier
punto de la escala.
Δ_i < α_i · R*(i) > Inversión El nodo asumió más de lo que
0 R*(i) causal el análisis le asigna. Puede
indicar chivo expiatorio
(asume responsabilidad ajena)
o vanguardia de asunción
(integra su contribución antes
de que el campo la
reconozca).
V. Δ y los dos orígenes del déficit
Cuando Δ_i > 0, la brecha tiene dos orígenes
estructuralmente distintos. El primero es la evasión: φ(cid:0) tiene la
capacidad de operar sobre el colapso, pero el ego elige no ejercerla.
Desde el exterior, la evasión se manifiesta como α bajo en
presencia de los tres criterios de la Ruta B: el nodo tenía
conocimiento, capacidad de acción, y oportunidades verificadas de
actuar diferente.
El segundo origen es el bloqueo ontológico: φ(cid:0) no tiene la
capacidad de operar en este momento porque el estado de I(t) del
ego no lo permite. Desde el exterior, el bloqueo se manifiesta
como α bajo en ausencia del criterio de conocimiento. El SDO
accede a esta dimensión interior; el análisis forense no puede
hacerlo.

Metrología Causal · Vol. II
Producto de salida · Capítulo IV·4
Corolario II formalmente derivado: Δ_i = R*(i) × (1 − α_i)
con sus tres casos y su interpretación. Δ_total = Σᵢ Δ_i como
medida del déficit sistémico. La distinción entre los dos
orígenes del déficit (evasión y bloqueo ontológico) como
guía para la intervención y el acompañamiento.
Notas al Capítulo IV·4
1 La imposibilidad matemática de α_i > 1 cierra el corolario con precisión:
un nodo no puede asumir más del 100% de su responsabilidad causal.
Si la calibración de α produce α_i > 1, hay un error de calibración — el
criterio de acción de la Ruta B se aplicó sobre un denominador
incorrecto.
2 El caso Δ < 0 (inversión causal) tiene una interpretación asimétrica
importante. Si el Δ negativo se debe a que el nodo asumió la
responsabilidad del nodo de diseño (chivo expiatorio), el análisis
preventivo debe señalar ese patrón explícitamente: el rediseño que
previene el resultado debe redistribuir la responsabilidad desde el
ejecutor hacia el diseñador, no solo exigir más asunción del ejecutor.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·5
Corolario III · El fraude annona
Derivación formal como identidad matemática desde R*, α e IIC

### I. El fraude annona como caso específico del
Corolario II
El Corolario II establece el déficit de asunción Δ para
cualquier nodo del grafo. El Corolario III aplica el mismo marco
al nodo de diseño institucional incorporando una tercera
dimensión que solo es relevante para ese nodo: la congruencia
entre el campo que declaró que produciría y el campo que
efectivamente produjo.
El fraude annona es una identidad matemática — una
cantidad que se deriva directamente de R*, α e IIC sin supuestos
adicionales. Es el Corolario II aplicado al nodo de diseño con el
IIC como modulador de la fracción de Δ que proviene de la brecha
de congruencia.

### II. El papel del IIC en la derivación

Metrología Causal · Vol. II
El IIC_D del nodo de diseño mide la correlación entre el
campo que N_D declaró que produciría y el campo que
efectivamente produjo. Cuando IIC es bajo, la brecha de
congruencia genera por sí misma una fracción de Δ — incluso si
el nodo hubiera actuado con α moderado, la divergencia entre su
diseño declarado y su operación real amplía el déficit efectivo.
Un nodo que diseña un protocolo prometiendo ciertos
resultados y luego opera el sistema de manera diferente no solo
tiene el Δ de la asunción que cualquier nodo puede tener. Tiene
además la brecha entre lo que prometió y lo que hizo — que
amplifica su Δ en proporción a la magnitud de esa divergencia.

### III. La derivación del Corolario III
Corolario III · El fraude annona
Sea N_D el nodo de diseño con R*_D > 0, α_D (cid:0) [0,1] e
IIC_D (cid:0) [0,1]:
Fraude_annona_D = R*_D × (1 − α_D) × (1 − IIC_D)
El fraude annona es el Corolario II aplicado al nodo de diseño con (1 −
IIC_D) como el factor que amplifica el déficit de asunción en función de la
brecha de congruencia del diseño. Es equivalente a Δ_efectivo_D = Δ_D
× (1 − IIC_D).

### IV. Las propiedades formales
Propiedad 1 — Fraude annona (cid:0) [0,1]: los tres factores son
no negativos y menores o iguales a uno, por lo que su producto
también lo es.
Propiedad 2 — El máximo se alcanza en el vértice (R*_D =
1, α_D = 0, IIC_D = 0): el nodo de diseño es el único responsable

Metrología Causal · Vol. II
del resultado, no ha asumido nada, y su campo real va en dirección
opuesta al declarado. Esta es la posición más grave que el sistema
puede medir.
Propiedad 3 — El fraude annona es cero en tres casos
independientes: R*_D = 0 (no causalmente relevante), α_D = 1
(asunción completa), o IIC_D = 1 (congruencia plena). En
cualquiera de los tres casos, no hay fraude annona
independientemente de los otros factores. La figura más grave
requiere los tres factores simultáneamente.
R*_D α_D IIC_D Fraude Interpretación
annona
0.60 0.10 0.20 0.432 Posición grave. Alta centralidad,
baja asunción, baja congruencia.
El diseño es el factor dominante
y operó muy diferente a lo
declarado.
0.60 0.60 0.20 0.192 Posición moderada. Alta
centralidad, asunción moderada.
La congruencia sigue baja pero
la asunción parcial reduce el
fraude annona.
0.60 0.10 0.80 0.108 Posición baja-moderada. Alta
centralidad y baja asunción,
pero el campo real es
mayormente congruente con el
declarado.
0.20 0.10 0.20 0.144 A pesar de R* moderado, la
combinación de baja asunción y
baja congruencia supera el
umbral de 0.20.
Producto de salida · Capítulo IV·5

Metrología Causal · Vol. II
Corolario III formalmente derivado: Fraude_annona_D =
R*_D × (1−α_D) × (1−IIC_D) con sus tres propiedades. El
umbral de acción 0.20 corresponde al punto donde la
combinación de los tres factores es suficientemente
significativa para activar requisitos formales de intervención
en la mayoría de los dominios regulatorios.
Notas al Capítulo IV·5
1 El nombre fraude annona proviene del derecho romano: la annona era la
gestión del abastecimiento de grano de Roma, y el fraudator annonae
era el funcionario que adulteraba o desviaba el suministro de un bien
esencial. La analogía con el nodo de diseño institucional moderno es
precisa: quien diseña un sistema de salud, crédito, educación o justicia
está gestionando un bien esencial. El fraude annona causal mide qué
tanto ese gestor prometió una calidad de servicio que no entregó.
2 La relación formal entre el Corolario III y el Corolario II merece
explicitarse: el fraude annona es el Δ efectivo del nodo de diseño.
Δ_efectivo_D = Δ_D × (1 − IIC_D) = R*_D × (1−α_D) ×
(1−IIC_D). La baja congruencia del diseño amplifica el déficit de
asunción porque el nodo no solo no asumió su responsabilidad —
prometió controles que no implementó, amplificando el daño de su
déficit.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·6
Extensión al caso acumulativo
El valor de Shapley cuando ningún nodo es condición sine qua non
individual

### I. El límite del Teorema IV·2
El Teorema de la Responsabilidad Causal Proporcional
requiere que al menos un nodo del grafo sea condición sine qua
non individual de D. Hay sistemas causales complejos donde esta
condición no se cumple: el resultado emerge de la intersección de
múltiples contribuciones ninguna de las cuales es individualmente
necesaria. En esos sistemas, el axioma A2 no puede cumplirse en
su formulación original.
En esos sistemas, el eigenvector sigue siendo
matemáticamente calculable, pero su interpretación como
responsabilidad causal proporcional pierde el fundamento que A2
le provee. Este capítulo establece qué distribución aplica en ese
caso.

### II. La función característica del juego cooperativo
asociado

Metrología Causal · Vol. II
Cuando ningún nodo es condición sine qua non individual,
el sistema causal se modela como un juego cooperativo. El juego
tiene como jugadores los nodos de N (excluyendo Nf) y como
función característica v: 2^N → [0,1] donde v(S) mide la fracción
del resultado D que la coalición S puede producir por sí sola.
Función característica v(S)
v(S) = fracción de D que la submatriz W_S (restringida
a nodos en S) produce en Nf
v ((cid:0)) = 0 (la coalición vacía no produce nada) · v(N(cid:0){Nf}) = 1 (todos
los nodos producen todo D). v(S) se calcula como el eigenvector principal de
W_S normalizado sobre Nf.

### III. El valor de Shapley como distribución de
responsabilidad
El valor de Shapley φᵢ de cada nodo i es su contribución
marginal promedio sobre todas las coaliciones posibles. Mide
cuánto agrega cada nodo al resultado cuando se une a una
coalición que ya existía, promediado sobre todos los órdenes
posibles.
Valor de Shapley
φᵢ = Σ_ {¡S ⊆ ¡N∖ {i, Nf}} [|S|! · (n−|S|−1)! / n!] ×
[v(S∪{i}) − v(S)]
n = |N(cid:0){Nf}| es el número de nodos sin el sumidero. El factor
combinatorio es la probabilidad de que S sea exactamente el conjunto de
nodos que precedieron a i en un orden aleatorio.
El valor de Shapley satisface cuatro axiomas propios:
eficiencia (los valores suman v(N)), simetría (nodos con
contribuciones idénticas reciben valores idénticos), nulidad (nodos

Metrología Causal · Vol. II
que no contribuyen a ninguna coalición reciben cero), y aditividad.
En el caso acumulativo, estos axiomas determinan de manera
única la distribución Shapley.

### IV. El Shapley como caso límite del eigenvector
La relación entre el eigenvector y el valor de Shapley no es
de oposición sino de continuidad. El valor de Shapley es el caso
límite del eigenvector cuando la condición sine qua non individual
se debilita hacia cero. Esta continuidad tiene una consecuencia
práctica: en grafos donde la condición se cumple para algunos
nodos, pero no para todos, los dos métodos producen valores
similares.
Característica Eigenvector (caso Valor de Shapley (caso
s.q.n.) acumulativo)
Condición de Al menos un nodo es Ningún nodo es condición
aplicación condición sine qua sine qua non individual
non individual
Axiomas A1 eficiencia, A2 Eficiencia, simetría,
causalidad necesaria, nulidad, aditividad
A3 centralidad
recursiva, A4
monotonicidad
Complejidad O(n²·k) con k O(2ⁿ) exacto. Para n > 20
iteraciones. Eficiente requiere métodos de
para grafos grandes. aproximación.
Corolarios R*_neta, Δ, fraude R*_neta y Δ son válidos
derivados annona — todos con Shapley como base.
válidos Fraude annona requiere
adaptación del IIC.

Metrología Causal · Vol. II
Producto de salida · Capítulo IV·6
Extensión del Teorema IV·2 al caso acumulativo: el valor de
Shapley φᵢ como la distribución de responsabilidad cuando
ningún nodo es condición sine qua non individual. La
función característica v(S) del juego cooperativo asociado al
grafo G. El Shapley como caso límite del eigenvector con sus
axiomas propios.
Notas al Capítulo IV·6
1 La complejidad computacional O(2ⁿ) del valor de Shapley exacto es una
limitación práctica para grafos grandes. Los métodos de aproximación
más eficientes son: (a) muestreo de permutaciones aleatorias — calcular
la contribución marginal de cada nodo en K permutaciones aleatorias y
promediar, con error que decrece como 1/√K; y (b) el algoritmo de
Strömberg (2018) que calcula Shapley en tiempo O(n·2^(n/2)) para
estructuras con independencia condicional.
2 La relación entre el eigenvector y el Shapley tiene un precedente en la
literatura relevante para la Conjetura del Operador Unificador del

### Capítulo IV·7. Teng (2016) demuestra que el PageRank puede
interpretarse como el valor de Shapley de un juego de influencia social
específico. Si esa relación puede generalizarse al grafo causal ponderado
de este sistema, el eigenvector y el Shapley serían instancias del mismo
operador con diferentes funciones características.

Metrología Causal · Vol. II

## PARTE IV · El Teorema de la Responsabilidad Causal

### Capítulo IV·7
La conjetura del operador unificador
Programa de investigación: un operador que produce eigenvector o
Shapley según la estructura del grafo

### I. El problema que la conjetura formula
Los Capítulos IV·2 y IV·6 establecen dos distribuciones de
responsabilidad para dos tipos de grafo: el eigenvector cuando hay
condición sine qua non individual, el Shapley cuando no la hay.
Ambos métodos son matemáticamente sólidos y sus condiciones
de aplicación están claramente delimitadas. La conjetura del
operador unificador es la afirmación de que existe un operador
único que produce la distribución correcta en ambos casos y en
los casos mixtos.

### II. El enunciado formal de la conjetura
Conjetura del Operador Unificador (C.O.U.)
Sea C la clase de grafos causales dirigidos ponderados G =
(N, E, W) con W ≥ 0. Existe un operador O: C → (cid:0)^|N|
tal que:

Metrología Causal · Vol. II
(i) Cuando G tiene al menos un nodo condición sine qua non
individual: O(G) = eigenvector principal normalizado de W.
(ii) Cuando ningún nodo de G es condición sine qua non
individual: O(G) = valor de Shapley del juego cooperativo
v(S) asociado a G.
(iii) Para grafos mixtos con condición sine qua non parcial: O(G) interpola
de manera continua entre los dos casos anteriores, sin discontinuidades.

### III. Los cuatro precedentes en la literatura
Referencia Resultado Conexión con la C.O.U.
relevante
Hu & Shapley Demuestran que en Establece que eigenvector y
(2003) 'On estructuras Shapley pueden coincidir en
authority jerárquicas, la una misma estructura. La
distributions in distribución de C.O.U. generaliza este
organizations' autoridad que resultado a estructuras no
satisface el axioma jerárquicas.
eigenvectorial de
centralidad y el
axioma de Shapley
de contribución
marginal es la misma
distribución.
Teng (2016) Demuestra que el El eigenvector es un valor de
'Scalable and PageRank puede Shapley para cierto juego. Si
Accurate Graph interpretarse como el el juego correcto puede
Clustering' valor de Shapley de identificarse para el grafo
un juego de causal, los dos son el mismo
influencia social con objeto con diferentes
función representaciones.
característica
específica.

Metrología Causal · Vol. II
Referencia Resultado Conexión con la C.O.U.
relevante
Aleandri, Demuestran que Extiende el resultado de
Ciardiello & Di índices de poder que Teng a grafos con estructura
Liddo (2025) combinan de coalición explícita — el
'Power indices centralidad contexto del grafo causal con
and graph eigenvectorial son aristas ponderadas.
centrality' valores de Shapley de
juegos TU sobre
grafos con uniones a
priori.
Forré & Jansma Generalizan el valor El marco formal de Forré &
(2025) 'Causal de Shapley a Jansma es el contexto natural
Shapley values funciones vectoriales donde O podría definirse. Su
on DAGs' en multigrafos generalización al grafo causal
dirigidos acíclicos con IIC y los corolarios está
ponderados. pendiente.

### IV. Lo que falta para la demostración
Programa de demostración de la C.O.U. — tres pasos
Paso 1 — Definir C con precisión: especificar la clase de
grafos sobre la que O está definido. La clase C debe incluir
los grafos causales de este sistema (W ≥ 0, irreducibles, con
nodo sumidero) y excluir los grafos donde ni eigenvector ni
Shapley tienen interpretación causal válida.
Paso 2 — Encontrar los axiomas que determinan O
unívocamente en toda C: los axiomas deben (a) reducirse a
A1–A4 en el caso sine qua non, (b) reducirse a los axiomas
de Shapley en el caso acumulativo, y (c) determinar una
distribución única para casos mixtos.
Paso 3 — Demostrar continuidad entre los dos extremos: la interpolación
del punto (iii) requiere una métrica sobre C que mida qué tan 'cerca' está

Metrología Causal · Vol. II
un grafo del caso sine qua non o del caso acumulativo, y demostrar que O
varía continuamente con esa métrica.

### V. El valor de la conjetura para el sistema
La conjetura del operador unificador no es necesaria para
operar el sistema. El mediador que tiene claro cuándo usar
eigenvector y cuándo usar Shapley tiene todo lo que necesita para
el análisis de cualquier caso real. La conjetura importa por razones
distintas.
La primera: la demostración de C.O.U. convertiría la
metrología causal en una ciencia matemáticamente más completa.
Un operador unificador sería la respuesta a todos los tipos de
problema — lo que corresponde al nivel de generalidad que una
teoría matemática de la responsabilidad causal debería alcanzar.
La segunda: la demostración identificaría la función
característica v(S) del juego cooperativo que corresponde al grafo
causal de este sistema. Esa función característica haría el cálculo
del Shapley significativamente más eficiente para los casos
acumulativos.
La tercera: el programa de investigación de C.O.U. es el
punto de contacto más natural entre el sistema y la literatura
matemática establecida. Una demostración publicable es la vía de
validación externa más robusta que el sistema tiene disponible.
La conjetura del operador unificador se formula aquí con precisión
matemática y honestidad sobre su estatus: es una conjetura, no un
resultado. Su inclusión en este volumen no es para afirmar más de
lo que la evidencia actual permite sino exactamente para lo
contrario — para delimitar con precisión dónde está el límite del
conocimiento formalizado del sistema y dónde comienza el
programa de investigación que lo extenderá.

Metrología Causal · Vol. II
Principio de honestidad metrológica sobre los límites del
sistema
Producto de salida · Capítulo IV·7
La Conjetura del Operador Unificador formalmente
enunciada: el operador O que produce el eigenvector en el
caso sine qua non y el Shapley en el caso acumulativo, con
interpolación continua en casos mixtos. Los cuatro
precedentes de la literatura. El programa de demostración en
tres pasos con identificación precisa de la brecha técnica que
falta cerrar.
Notas al Capítulo IV·7
1 El enunciado del punto (iii) de la conjetura — interpolación continua para
casos mixtos — es el más delicado porque 'fracción de sine qua non' no
está formalmente definida. Una definición candidata: dado un grafo G
con n nodos, sea k el número de nodos que pasan el test de condición
sine qua non individual. La fracción de sine qua non es k/n. O(G)
interpola entre el eigenvector (k/n = 1) y el Shapley (k/n = 0). El
problema matemático es que k puede no ser continuo en ningún
parámetro natural del grafo.
2 El resultado de Teng (2016) es el más directamente relevante para la C.O.U.
Su demostración que el PageRank es el valor de Shapley de un juego de
influencia social sugiere que la función característica v(S) del juego
asociado al grafo causal podría expresarse en términos de la submatriz
W_S. Esta línea de investigación es la más prometedora para el Paso 2
del programa de demostración.
3 La validación matemática externa de la C.O.U. es uno de los objetivos del
programa de investigación del Centro Multidisciplinario Meriadock.
Investigadores con formación en teoría de juegos cooperativos o álgebra
lineal aplicada interesados en colaborar pueden contactar al Centro para
acceder al manuscrito completo de la Axiomatización del Sistema de la
Doble Mediación.

Metrología Causal · Vol. II
APÉNDICES
Apéndice A
Protocolo de calibración empírica
Recolección de datos desde programas de intervención longitudinal

### I. El propósito del Apéndice A
El Apéndice A documenta el protocolo completo para
generar datos de calibración del sistema desde programas de
intervención longitudinal. A diferencia de los datos forenses o
clínicos que alimentan el análisis causal en casos individuales, los
datos de calibración tienen un propósito diferente: verificar
empíricamente que los parámetros teóricos del sistema — los
rangos de S por Hijo dominante del Capítulo I·4, los pesos de φ(cid:0)
de la Axiomatización, la velocidad de convergencia del eigenvector
humano — corresponden a los valores observables en poblaciones
reales.
El protocolo está diseñado para funcionar con operadores
sin formación en el paradigma. Toda la inteligencia teórica está
contenida en el diseño de los instrumentos y en la tabla de
conversión — el operador marca casillas. El Centro
Multidisciplinario Meriadock aplica la tabla de conversión y
produce los parámetros de calibración. La cadena es: casillas →

Metrología Causal · Vol. II
parámetros operativos → calibración de instrumentos →
calibración de la Axiomatización.

### II. Los cuatro parámetros a estimar
El protocolo genera datos para estimar cuatro parámetros
que ningún otro corpus existente puede proveer, porque ningún
otro corpus combina una base ontológica formal con observación
longitudinal sistemática.
Parámetro Qué mide Por qué ningún otro corpus
lo provee
w(τ) — El peso que cada Requiere observación repetida
Función de momento del pasado del mismo sujeto a lo largo del
peso del tiene en el estado tiempo con variables
integral de presente de I(t). estructurales definidas
Bochner ¿Decae formalmente. Los corpus
exponencialmente, psicométricos no tienen la base
linealmente, o con ontológica; los filosóficos no
otra función? tienen datos longitudinales.
Pesos En la función Requiere que las tres variables
relativos de φ₁ (v_t, c, h) → acto, sean operacionalizadas con el
φ(cid:0) (v_t, c, h) qué tanto predice el mismo sistema conceptual. No
acto el estado hay instrumento externo que
interno del sujeto mida v_t, c y h simultáneamente
(v_t), su campo con la ontología de este sistema.
heredado (c), y su
historia acumulada
(h)
Dimensión Cuántas Requiere que las variables
efectiva de E dimensiones observadas mapeen
independientes son directamente al espacio E de la
necesarias para Axiomatización. Solo los
describir el patrón de

Metrología Causal · Vol. II
Parámetro Qué mide Por qué ningún otro corpus
lo provee
comportamiento de instrumentos de este sistema
un ego en un producen esas variables.
contexto específico.
Si n dimensiones
explican el 80% de la
varianza, la
dimensión efectiva
de E para esa
población es n.
Velocidad de Cuántas 'iteraciones' Requiere observación
convergencia (sesiones, longitudinal con suficientes
del interacciones, puntos de tiempo sobre las
eigenvector eventos) requiere el mismas variables estructurales.
humano eigenvector de un Los estudios de cambio
sistema humano real actitudinal típicos no miden las
para converger. El variables correctas.
análogo empírico de
la convergencia
10⁻ ⁶ del método de
potencias.

### III. Los dos formularios del protocolo
El protocolo opera con dos formularios que el operador usa
en cada sesión del programa de intervención. El Formulario A lo
llena el operador observando. El Formulario B lo llena el
participante al final de la sesión. Los dos son idénticos en las n
sesiones del programa — solo cambia el número de sesión. Toda
la inteligencia del sistema está en el diseño de las opciones y en la
tabla de conversión del Apartado V.

Metrología Causal · Vol. II
FORMULARIO A · Registro del operador
Una hoja por grupo por sesión. El operador observa durante
la sesión y marca UNA sola opción por variable para cada
participante. No escribe nada. No interpreta nada. Solo
marca.
Instrucción: marca lo que observaste, no lo que crees que el participante
quiso decir. Si no tuviste oportunidad de observar una variable, deja la
celda en blanco.
Variable Opción A Opción B Opción C
V1 · ¿Quién Dijo 'yo hice / Dijo 'me sentí / Dijo 'él me hizo
fue el sujeto de yo decidí / yo me ocurrió / / fue la presión /
sus frases? elegí' me di cuenta' no había opción'
V2 · ¿Su Su respuesta No respondió Su respuesta fue
respuesta fue fue diferente a nada en la similar a lo que
igual o las demás actividad ya habían dicho
diferente al otros
grupo?
V3 · ¿Sabía Sí, nombró qué Nombró cómo Solo habló de lo
qué quería quería antes de se sentía, pero que otros
antes de actuar no qué quería hicieron o de las
actuar? circunstancias
V4 · ¿Nombró Sí, nombró un Dijo que algo No mencionó
algo concreto acto específico dependía de él, nada de lo que él
que él hizo? suyo con sin especificar hizo
consecuencia qué
FORMULARIO B · Reporte del participante
Una hoja individual por participante por sesión. Se entrega
en los últimos 3 minutos. El participante la llena solo. 4

Metrología Causal · Vol. II
preguntas. Sin opciones neutras — cada pregunta obliga a
tomar posición. Los participantes no ven el Formulario A.
Sesión: ___ · Clave del participante: _________ · Fecha:
___________
Encierra en un círculo la opción que más se parece a lo que pasó HOY en
la sesión.

### 1. Cuando hablé de algo que hice o que me pasó, lo describí
como: A — Algo que yo decidí o hice, aunque no haya
salido bien B — Algo que sentí o que me ocurrió C —
Algo que pasó por lo que otros hicieron o por las
circunstancias

### 2. Lo que dije o compartí en la actividad de hoy fue: A —
Diferente a lo que dijeron mis compañeros B — No
compartí nada hoy C — Parecido a lo que ya habían dicho
otros

### 3. Cuando recuerdo algo que hice esta semana, puedo decir:
A — Sé qué quería lograr cuando lo hice B — Recuerdo
cómo me sentí, pero no bien qué quería C — No sé bien
por qué lo hice, simplemente pasó

### 4. Al terminar esta sesión, puedo decir: A — Identifiqué
algo concreto que yo hice y que tuvo consecuencias B —
Siento que algo de lo que pasó dependió de mí, pero no sé
exactamente qué C — Lo que pasó no tuvo mucho que
ver con lo que yo hice

### IV. La tabla de conversión — solo Meriadock

Metrología Causal · Vol. II
Esta tabla nunca sale del equipo central. Es el motor que
convierte los datos crudos de los formularios en parámetros del
sistema. El operador y el participante nunca la ven.
Variable Opción Valor Parámetro que
numérico alimenta
V1 · Atribución A 1.00 α directo — alta asunción
(α proxy) observada
B 0.50 α directo — asunción
media
C 0.00 α directo — baja asunción
V2 · A 0.10 S directo — baja
Conformidad (S sustituibilidad
proxy)
B — Sin dato — no se incluye
en el promedio de S
C 0.90 S directo — alta
sustituibilidad
V3 · Estado A 2 v_t estructurado
interno (v_t)
B 1 v_t difuso
C 0 v_t ausente
V4 · A 2 φ(cid:0) activo
Reconocimiento
(φ(cid:0))
B 1 φ(cid:0) parcial
C 0 φ(cid:0) ausente

Metrología Causal · Vol. II
El cálculo de Δ emerge de la brecha entre los dos formularios
sobre la misma variable. Para V1: Δ_sesión = valor de V1 en
Formulario A − valor de pregunta 1 en Formulario B. Δ > 0 indica
que el participante se atribuye menos responsabilidad de lo que su
lenguaje observable refleja (evasión conductual). Δ < 0 indica que
se atribuye más de lo que muestra (asunción que supera la
conducta observable). Δ ≈ 0 indica calibración: el participante se
ve aproximadamente como el operador lo ve.

### V. El árbol de clasificación del Hijo dominante
El árbol clasifica el Hijo dominante del participante desde los
promedios de las cuatro variables a lo largo de todas las sesiones
del programa. Se aplica después de la última sesión, sobre los
promedios (cid:0), S(cid:0), v(cid:0)_t y φ(cid:0)(cid:0).
Árbol de clasificación — lectura secuencial
Paso 1 — ¿S(cid:0) > 0.60? Si SÍ → el campo domina sobre la
voluntad individual. Ir al Paso 2. Si NO → hay individuación
en la voluntad. Ir al Paso 4.
Paso 2 (S(cid:0) > 0.60) — ¿(cid:0) < 0.30? Si SÍ → Ir al Paso 3. Si
NO → ANTEROS. La voluntad se orienta por reciprocidad.
Condicionamiento de la asunción a la respuesta del otro.
Paso 3 (S(cid:0) > 0.60, (cid:0) < 0.30) — ¿φ(cid:0)(cid:0) < 0.50? Si SÍ →
FOBOS. La voluntad se orienta por miedo al campo. No
asume, no reconoce, se conforma. Si NO → DEIMOS. La
voluntad se orienta por la amenaza difusa. Reconoce actos,
pero los atribuye a presión externa.
Paso 4 (S(cid:0) ≤ 0.60) — ¿(cid:0) > 0.60? Si SÍ → Ir al Paso 5. Si
NO → POTÓS. La voluntad se orienta por anhelo de lo
ausente. Baja sustituibilidad con asunción media.

Metrología Causal · Vol. II
Paso 5 (S(cid:0) ≤ 0.60, (cid:0) > 0.60) — ¿v(cid:0)_t > 1.0? Si SÍ →
HARMONÍA. La voluntad se orienta por integración plena. Alta
asunción, claridad interna, φ₂ activo. Si NO → EROS. La voluntad
se orienta por deseo presente. Asume, pero desde impulso más que desde
claridad.
Hijo (cid:0) S(cid:0) v(cid:0)_t φ(cid:0)(cid:0) Patrón Δ
esperad esperad esperad esperad típico
o o o o
Fobos 0.00– 0.70– 0.00– 0.00– Δ negativo
0.25 1.00 0.50 0.50 — asume
menos de
lo que hace
Deimos 0.20– 0.65– 0.50– 0.50– Δ negativo
0.40 0.90 1.00 1.00 moderado
Anteros 0.30– 0.40– 0.50– 0.50– Δ variable
0.60 0.70 1.20 1.20 —
depende de
la respuesta
del
referente
Potós 0.35– 0.20– 0.80– 0.50– Δ positivo
0.60 0.50 1.50 1.20 — asume
más de lo
que el
campo
justifica
Eros 0.55– 0.10– 0.80– 1.00– Δ ≈ 0 con
0.80 0.35 1.50 1.80 varianza
alta
Harmon 0.70– 0.00– 1.20– 1.50– Δ ≈ 0
ía 1.00 0.25 2.00 2.00 estable,
convergen

Metrología Causal · Vol. II
Hijo (cid:0) S(cid:0) v(cid:0)_t φ(cid:0)(cid:0) Patrón Δ
esperad esperad esperad esperad típico
o o o o
cia
temprana

### VI. El criterio de convergencia k_conv
Un participante ha convergido en la sesión k si las opciones
modales de V1 (proxy de α) y V4 (proxy de φ(cid:0)) en el Formulario
A son iguales en las sesiones k−2, k−1 y k. Es decir: tres sesiones
consecutivas con el mismo patrón en las dos variables
estructurales.
La sesión de convergencia se registra como k_conv. Si el
patrón no se estabiliza antes de la última sesión, k_conv =
indefinido — lo que es en sí mismo un dato: significa que el
proceso no fue suficiente para estabilizar la posición de ese sujeto.
El promedio de k_conv sobre toda la muestra es la estimación
empírica de cuántas iteraciones requiere el eigenvector humano
para converger en esa población.
k_conv Interpretación para Implicación para la
el sistema Axiomatización
Sesiones Patrón muy estable v_t y φ(cid:0) preexistían al
3–4 desde el inicio. El programa. El peso de h en φ(cid:0) es
programa lo reveló, no dominante para este sujeto.
lo formó.
Sesiones Convergencia media. Peso balanceado entre v_t y c en
5–6 El programa produjo el φ(cid:0). Valor típico para la
cambio en la primera población general.
mitad.

Metrología Causal · Vol. II
k_conv Interpretación para Implicación para la
el sistema Axiomatización
Sesiones Convergencia tardía. S alto al inicio — el campo
7–8 El proceso requirió dominaba φ(cid:0). El cambio
más iteraciones. requirió más exposición.
Sesiones Convergencia al límite. El sistema necesita más
9–n Las sesiones iteraciones que las del programa
disponibles apenas estándar.
suficientes.
Indefinido Sin convergencia en el Requiere análisis individual.
programa. Puede indicar bloqueo
ontológico o condición que
excede el programa.

### VII. La hoja de calibración de la Axiomatización
Al final de cada cohorte (todos los grupos del ciclo escolar),
los datos agregados producen la hoja de calibración de la
Axiomatización. Esta hoja es el insumo directo para verificar los
postulados formales del sistema y — con suficiente muestra —
para estimarlos empíricamente.
Parámetro de Cómo se estima Qué nivel de
la desde los datos del evidencia produce
Axiomatización protocolo
w(τ) — función Correlación entre α en la Evidencia empírica
de peso de I(t) sesión τ y α en la sesión directa de la forma de
final, para cada distancia w(τ) para esta
τ. Si la correlación población. Primer dato
decrece empírico de la
exponencialmente con Axiomatización sobre
τ, w(τ) tiene forma I(t).
exponencial. Si decrece

Metrología Causal · Vol. II
Parámetro de Cómo se estima Qué nivel de
la desde los datos del evidencia produce
Axiomatización protocolo
linealmente, tiene forma
lineal.
Pesos relativos de Regresión de α_final Estimación empírica de
v_t, c, h en φ(cid:0) sobre: v_t en sesión 1 la función φ(cid:0) para esta
(estado interno inicial), población. El predictor
S(cid:0) global (campo con mayor coeficiente
heredado — proxy de independiente es el
c), α en sesión 1 (historia input dominante.
previa — proxy de h).
Los coeficientes son los
pesos relativos de los
tres inputs de φ(cid:0).
Dimensión Análisis de La Axiomatización
efectiva de E componentes postula E separable.
principales sobre las 4 Este dato dice cuántas
variables × n sesiones. dimensiones son
El número de efectivamente
componentes necesarias en un sistema
necesarios para explicar humano adolescente en
el 80% de la varianza es contexto escolar.
la dimensión efectiva.
Velocidad de Promedio y desviación El k_conv promedio es
convergencia del estándar de k_conv la estimación empírica
eigenvector sobre la cohorte. del número de
Distribución de k_conv iteraciones que requiere
por Hijo dominante el eigenvector humano
clasificado. para converger en esta
población.
Con tres o más cohortes (ciclos escolares), los parámetros
estimados producen valores estables y comparables entre grupos.
Con diez o más cohortes, la estimación de w(τ) y de los pesos de
φ(cid:0) alcanza el nivel de precisión necesario para publicación en
literatura de psicometría formal.

Metrología Causal · Vol. II
Productos del Apéndice A
Formulario A (operador) y Formulario B (participante) listos
para imprimir y usar en campo. Tabla de conversión para
Meriadock. Árbol de clasificación del Hijo dominante.
Criterio de convergencia k_conv. Hoja de calibración de la
Axiomatización con sus cuatro parámetros estimables. Los
dos formularios son autosuficientes — el operador no
necesita ningún otro documento para su uso.
Notas al Apéndice A
1 El protocolo requiere que las claves de los participantes sean asignadas por
Meriadock antes de comenzar el programa — no por el operador o la
institución. Esto garantiza que los datos de múltiples escuelas y ciclos
son vinculables longitudinalmente sin exponer datos personales. La
clave es el identificador permanente del participante a través de todas
las cohortes en las que participe.
2 La escala de cuatro variables (V1–V4) es el mínimo operativo: cuatro
variables producen todos los parámetros necesarios si se observan en
suficientes sesiones. Agregar más variables por sesión aumenta la carga
del operador sin aumentar proporcionalmente la información de
calibración. La restricción de cuatro variables es un principio de diseño,
no una limitación técnica.
3 El protocolo puede adaptarse a poblaciones distintas de adolescentes en
secundaria con ajustes menores en el lenguaje del Formulario B. Los
valores de la tabla de conversión (Apartado IV) son los mismos para
cualquier población — representan la estructura formal del sistema, no
características de la población específica. Los rangos del árbol de
clasificación del Hijo dominante (Apartado V) pueden necesitar
calibración para poblaciones con características estructurales muy
diferentes (adultos mayores, contextos institucionales, poblaciones
clínicas).

Metrología Causal · Vol. II
APÉNDICES
Apéndice B
Tabla de equivalencias extendida por
dominio
Los nueve conceptos del sistema en ocho dominios disciplinares

### I. El propósito del Apéndice B
La Introducción de este volumen establece el glosario
operativo universal con tablas de equivalencias para los nueve
conceptos del sistema en seis dominios. El Apéndice B extiende
esas tablas en dos dimensiones: añade dos dominios adicionales
(educación y psicología forense) y profundiza cada equivalencia
con el vocabulario técnico específico que el mediador encuentra
en documentos, expedientes y comunicaciones formales de cada
disciplina.
La función de este apéndice no es reemplazar al glosario de
la Introducción — es complementarlo. La Introducción establece
el principio de traducción. Este apéndice provee el léxico
completo que el mediador necesita cuando trabaja en un dominio
específico con sus terminologías propias. Un abogado penalista y
un epidemiólogo describen el mismo fenómeno causal con
vocabularios tan distintos que el mediador sin este apéndice puede
no reconocer que está ante el mismo concepto del sistema.

Metrología Causal · Vol. II

### II. Tabla maestra de equivalencias — Nodo
Dominio Término Términos Criterio de
equivalente adicionales identificación
más del dominio
frecuente
Derecho Imputado, Autor material, Actor cuya
penal acusado, coautor, conducta activa u
responsable partícipe, omisiva fue
instigador, condición necesaria
cómplice, del tipo penal.
sujeto activo Incluye personas
jurídicas cuando el
sistema legal lo
permite.
Derecho Parte Garante, Actor con deber
civil / demandada, fiduciario, jurídico cuyo
mercantil deudor, mandatario, incumplimiento fue
responsable representante condición necesaria
civil legal, socio del daño resarcible.
gestor
Medicina y Factor de Comorbilidad, El factor cuya
salud riesgo, factor determinante eliminación
pública etiológico, de salud, contrafactual habría
agente causal variable de prevenido o
exposición, modificado el
actor resultado clínico.
institucional Incluye sistemas de
salud como nodos.
Economía Agente Formador de El agente cuya
y política económico, precios, decisión alteró la
pública actor regulador, trayectoria del
institucional, institución, sistema más allá del
variable de tomador de ruido esperado y es
política decisiones identificable como

Metrología Causal · Vol. II
Dominio Término Términos Criterio de
equivalente adicionales identificación
más del dominio
frecuente
condición necesaria
del resultado.
Psicología Actor vincular, Referente La entidad cuyo
clínica figura de apego, significativo, patrón de conducta
sistema familiar cuidador fue condición del
primario, patrón de respuesta
institución del sujeto analizado.
socializadora
Psicología Peritado, Imputado El sujeto cuya
forense evaluado, evaluado, capacidad de actuar,
sujeto de la víctima comprender o
pericia evaluada, integrar sus actos es
testigo el objeto de la
evaluado evaluación pericial.
Educación Estudiante, Comunidad El actor cuya
docente, educativa, decisión o patrón de
directivo, institución conducta fue
familia educativa, condición del
diseñador resultado educativo
curricular analizado
(abandono,
rendimiento,
comportamiento).
Ingeniería Componente, Subsistema, El elemento cuya
e industria sistema, equipo interfaz, falla o decisión de
de diseño, arquitecto del diseño fue
operador sistema, condición
proveedor estructural de la falla
crítico sistémica o del
accidente analizado.

Metrología Causal · Vol. II

### III. Tabla maestra de equivalencias — Arista
Dominio Término Lo que acredita la arista en ese
equivalente dominio
más frecuente
Derecho Nexo causal, Prueba de que la conducta del nodo
penal relación de fue condición necesaria del resultado
causalidad penal, típico. Estándar: más allá de duda
vínculo típico razonable en foros penales.
Derecho Relación de Prueba de que el daño es
civil causalidad consecuencia previsible de la
adecuada, nexo conducta del nodo. Estándar:
causal civil preponderancia de la evidencia.
Medicina Relación Evidencia de que el factor i actúa
etiológica, sobre el factor j a través de un
mecanismo causal, mecanismo biológico, farmacológico
vía fisiopatológica o conductual documentado.
Economía Canal de Evidencia teórica o empírica de que
transmisión, la decisión de i afecta el resultado en
efecto estructural, j a través de un mecanismo
mecanismo de económico identificable.
política
Psicología Influencia Historia de interacciones
clínica vincular, documentadas entre i y j con patrón
condicionamiento, de respuesta de j contingente al
transmisión comportamiento de i.
intergeneracional
Psicología Influencia sobre la Evidencia de que el nodo i afectó la
forense capacidad, capacidad de comprensión,
condicionamiento motivación o control de conducta del
de la conducta nodo j en el momento del acto.
Educación Influencia Evidencia de interacciones entre i y j
pedagógica, efecto (docente-estudiante, familia-
docente, estudiante, pares) con efecto

Metrología Causal · Vol. II
Dominio Término Lo que acredita la arista en ese
equivalente dominio
más frecuente
transmisión de documentado sobre el resultado
expectativas educativo.
Ingeniería Dependencia Documentación de que el estado o
funcional, decisión del componente i determina
propagación de o limita el estado del componente j
falla, interfaz en condiciones operativas normales y
crítica de falla.

### IV. Tabla maestra de equivalencias — R*
Dominio Cómo se Frase estándar de presentación
comunica R* ante ese foro
Derecho Grado de 'El análisis establece que el nodo [X]
penal responsabilidad fue condición causal del [resultado]
causal, con un peso estructural de
participación [R*×100]%.'
estructural en el
resultado
Derecho Cuota de 'La distribución causal proporcional
civil responsabilidad asigna al [demandado] el [R*×100]%
proporcional, del resultado dañoso analizado.'
contribución
causal al daño
Medicina Fracción 'El factor [X] explica el [R*×100]% del
atribuible, peso resultado clínico en este sistema causal
etiológico del específico.'
factor

Metrología Causal · Vol. II
Dominio Cómo se Frase estándar de presentación
comunica R* ante ese foro
Economía Atribución de 'Esta decisión de política explica el
impacto, [R*×100]% de la variación observada
contribución en el indicador analizado.'
estructural al
resultado
Psicología Peso causal del 'El patrón vincular de [X] explica el
clínica factor, [R*×100]% del patrón de conducta del
contribución al sujeto en este sistema.'
patrón de
respuesta
Psicología Contribución 'La influencia del factor [X] explica el
forense causal a la [R*×100]% del patrón conductual
capacidad o objeto de la pericia.'
conducta del
peritado
Educación Contribución al 'El factor [X] explica el [R*×100]% del
resultado resultado educativo analizado en este
educativo, peso contexto específico.'
en la trayectoria
Ingeniería Contribución a 'El componente [X] concentra el
la falla [R*×100]% de la responsabilidad
sistémica, peso causal de la falla sistémica analizada.'
causal del
componente

### V. Tabla maestra de equivalencias — S

Metrología Causal · Vol. II
Dominio Término Cómo se calibra en ese dominio
equivalente de
S
Derecho Presión del ¿Otro sujeto en esa posición habría
penal entorno, contexto cometido el mismo acto bajo la
coactivo, estado misma presión? Jurisprudencia del
de necesidad estándar del 'hombre medio' en ese
contexto.
Derecho Práctica habitual ¿El comportamiento del nodo era el
civil del sector, comportamiento estándar de otros
estándar de la actores en posición equivalente?
industria Evidencia de prácticas del sector.
Medicina Adherencia al ¿Otros profesionales en condición
protocolo, equivalente habrían actuado igual
práctica clínica según el protocolo vigente? Guías de
habitual práctica clínica del período.
Economía Incentivo ¿El comportamiento del agente era el
estructural, regla comportamiento racional dado el
de decisión del sistema de incentivos?
sector Documentación de incentivos y
restricciones del período.
Psicología Condicionamiento ¿La respuesta del sujeto era la
clínica heredado, presión respuesta condicionada por su
del sistema historia de aprendizaje? Historia de
vincular refuerzos documentada.
Psicología Imputabilidad ¿El estado interno del peritado en el
forense reducida, momento del acto limitaba su
disminución de la capacidad de actuar diferente?
capacidad de Evaluación del estado mental en el
control momento del acto.
Educación Presión ¿El comportamiento del estudiante o
normativa, docente era el comportamiento
expectativa esperado por el sistema educativo en
institucional, ese contexto?

Metrología Causal · Vol. II
Dominio Término Cómo se calibra en ese dominio
equivalente de
S
condicionamiento
del aula
Ingeniería Operación dentro ¿El componente operaba dentro de
de los parámetros de diseño en que
especificaciones, cualquier componente equivalente
condición de habría fallado igual?
diseño normal

### VI. Tabla maestra de equivalencias — α
Dominio Término Evidencia que lo acredita en
equivalente de α ese dominio
Derecho Culpabilidad Dolo directo / eventual: el imputado
penal subjetiva, sabía y quiso el resultado. Culpa: el
conocimiento y imputado debía haber previsto el
voluntad del acto resultado. Las acciones de mitigación
tomadas se suman al α.
Derecho Diligencia debida, Acciones preventivas documentadas,
civil buena fe objetiva, informes de riesgo, medidas
cumplimiento del correctivas tomadas antes y después
deber de cuidado del resultado.
Medicina Adhesión al Historia clínica completa, órdenes
protocolo, médicas, registros de monitoreo,
diligencia clínica, acciones tomadas ante señales de
consentimiento alarma documentadas.
informado
Economía Cumplimiento Registros de implementación,
regulatorio, indicadores de cumplimiento,

Metrología Causal · Vol. II
Dominio Término Evidencia que lo acredita en
equivalente de α ese dominio
implementación respuesta documentada ante señales
efectiva de política de alerta sistémica.
Psicología Reconocimiento Conducta observable de
clínica del acto, reconocimiento en sesión, acciones
responsabilidad de reparación verificables, cambio de
integrada, patrón documentado en el tiempo.
capacidad de
rectificación
Psicología Imputabilidad, Evaluación del estado mental en el
forense capacidad de momento del acto: ¿el peritado
comprensión y de comprendía el alcance de su
autodeterminación conducta y tenía capacidad de
autodeterminación?
Educación Responsabilidad Registros de asistencia, planificación
pedagógica, documentada, seguimiento del
actuación estudiante, acciones tomadas ante
conforme al rol señales de riesgo educativo.
Ingeniería Cumplimiento del Registros de mantenimiento,
protocolo de bitácoras de operación, reportes de
mantenimiento y anomalías, acciones correctivas ante
operación, alertas del sistema.
actuación del
operador

### VII. Tabla maestra de equivalencias — Δ, IIC y
Fraude annona

Metrología Causal · Vol. II
Concepto Dominio Término Consecuencia
equivalente normativa típica
Δ — Derecho Ausencia de Agravante de
Déficit de penal arrepentimiento responsabilidad penal en
asunción activo, falta de algunos sistemas.
colaboración Impacto en la
con la justicia determinación de la
pena.
Derecho Brecha entre Fundamento de la
civil responsabilidad responsabilidad solidaria
declarada y ampliada o del deber de
acciones reparación integral.
reparatorias
Medicina Déficit de Elemento de
manejo activo, responsabilidad médica.
falta de Fundamento de quejas
respuesta ante el ante colegios
evento adverso profesionales.
Economía Incumplimiento Fundamento de
de obligaciones sanciones regulatorias
de por incumplimiento de
implementación metas o compromisos
declarados.
Psicología Déficit de Objetivo central del
clínica integración, acompañamiento con
trabajo HISTOS. No tiene
ontológico consecuencia normativa
pendiente directa.
IIC — Derecho Buena fe Elemento de
Integridad civil / objetiva, responsabilidad por
causal regulatorio congruencia diseño defectuoso.
entre Fundamento de acciones
declaración y de compliance y
conducta regulación.

Metrología Causal · Vol. II
Concepto Dominio Término Consecuencia
equivalente normativa típica
Auditoría Tasa de Indicador central de
cumplimiento auditoría de efectividad.
declarado vs. Fundamento de
real observaciones y
recomendaciones.
Medicina Adherencia al Elemento de evaluación
protocolo de la calidad del sistema
declarado, de salud. Fundamento
calidad del de acreditaciones
diseño del institucionales.
protocolo
Fraude Derecho Incumplimiento Activación de medidas
annona regulatorio agravado por cautelares, intervención
posición de regulatoria,
garante o responsabilidad penal de
administrador administradores.
fiduciario
Medicina Negligencia Fundamento de
institucional del investigaciones de salud
sistema o de la pública, reformas de
autoridad protocolo,
sanitaria responsabilidad
institucional.
Educación Incumplimiento Fundamento de
del sistema evaluaciones de política
educativo como educativa, reformas
nodo de diseño curriculares,
responsabilidad
institucional.

### VIII. Nota sobre la precisión de las equivalencias

Metrología Causal · Vol. II
Las equivalencias de este apéndice son instrumentos de
traducción, no de identificación exacta. El vocabulario de cada
disciplina fue construido con propósitos propios — el concepto
jurídico de diligencia debida no coincide perfectamente con α, el
concepto epidemiológico de fracción atribuible no coincide
perfectamente con R*. En todos los casos, el concepto del sistema
es más preciso que el equivalente disciplinar: tiene una definición
operativa exacta, un procedimiento de cálculo reproducible, y una
justificación formal desde el Teorema IV·2.
El error que el mediador debe evitar es la dirección inversa:
usar el vocabulario disciplinar para interpretar los conceptos del
sistema. 'Diligencia debida' es lo que los abogados llaman α en
contextos civiles — pero α no es diligencia debida. α es la fracción
de R* integrada mediante acciones verificables, calculada con los
tres criterios del Capítulo I·5. La equivalencia sirve para comunicar
al abogado qué está leyendo cuando ve α en el expediente. No sirve
para sustituir la definición formal de α por la noción jurídica de
diligencia.
Este apéndice y el glosario de la Introducción son instrumentos de
comunicación, no de reducción. El sistema no se traduce al
vocabulario de ningún dominio — el vocabulario de cada dominio
se aproxima al sistema. Esa dirección asimétrica es la condición
de que el análisis causal mantenga su rigor cuando opera en
cualquier dominio.
Principio de dirección de la traducción terminológica
Productos del Apéndice B
Tablas de equivalencias extendidas para los nueve conceptos
del sistema (Nodo, Arista, R*, S, α, Δ, IIC, Fraude annona)
en ocho dominios: derecho penal, derecho civil, medicina,
economía, psicología clínica, psicología forense, educación,
e ingeniería. El mediador usa este apéndice como referencia

Metrología Causal · Vol. II
rápida cuando prepara la presentación del expediente para
un foro o audiencia específica.
Notas al Apéndice B
1 El dominio de psicología forense se agrega a los seis dominios de la
Introducción porque es el contexto donde la tensión entre el sistema y
el vocabulario establecido es más aguda. La psicología forense tiene
conceptos propios muy desarrollados (imputabilidad, capacidad de
comprensión, actio libera in causa) que parcialmente se solapan con los
del sistema (α, v_t, φ(cid:0)) pero que fueron construidos con propósitos
legales específicos. El mediador que opera en ese dominio necesita
conocer con precisión dónde coinciden y dónde divergen los dos
vocabularios.
2 El dominio de educación se agrega porque el Programa ECO del Apéndice
A genera datos en ese contexto, y los operadores educativos necesitan
el vocabulario equivalente para interpretar los resultados del protocolo.
R* en educación no es un concepto familiar para docentes y directivos
— pero 'contribución al resultado educativo' sí lo es, y esa es la
equivalencia que el apéndice provee.
3 La tabla de Fraude annona del Apartado VII es la más compleja porque el
concepto no tiene equivalente directo en ningún dominio — es una
identidad matemática específica de este sistema. Las equivalencias
listadas son aproximaciones funcionales que el mediador puede usar
para comunicar la gravedad de la posición del nodo de diseño, no para
equiparar el fraude annona con ningún concepto jurídico o disciplinar
preexistente. La precisión del concepto solo puede comunicarse
refiriendo al Corolario III del Capítulo IV·5.