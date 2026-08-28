### Capítulo 2
La estructura del
análisis
Cómo se piensa un caso antes de calcular nada
El capítulo anterior explicó de dónde viene el método y por
qué la causalidad es el punto de partida correcto. Este
capítulo explica cómo se aplica: la secuencia de preguntas
que el análisis responde, en qué orden, con qué
instrumentos y con qué tipos de evidencia.
No hay operaciones matemáticas en este capítulo. Hay algo
más importante: el mapa del terreno. Quien entienda este
capítulo llegará al siguiente —donde están los cálculos—
sabiendo exactamente qué va a encontrar y para qué sirve
cada operación. Quien se salte este capítulo e intente aplicar
los cálculos directamente descubrirá que las operaciones
son simples pero que el resultado no tiene sentido si no se
sabe qué pregunta responde.
El análisis tiene cinco pasos. Los cinco son necesarios.
Ninguno puede sustituirse con otro ni reordenarse sin
perder el sentido del conjunto.
Paso Nombre Pregunta que responde

El Método Prometeo: Imputación Causal para juristas y abogados
1 El mapa del ¿Quiénes participaron en la cadena
caso que produjo el daño y cómo se
conectan?
2 El peso de las ¿Con qué fuerza determinó cada
conexiones actor a los demás? ¿Qué evidencia lo
sustenta y en qué rango?
3 La distribución ¿Qué fracción del daño — y del
causal beneficio — le corresponde
causalmente a cada actor?
4 La idiosincrasia ¿Cuánto de esa fracción era
y la brecha idiosincrática del actor? ¿Cuánto ya
asumió?
5 La magnitud del ¿Cuánto vale el daño total y cuánto le
daño corresponde a cada actor en términos
económicos?
Sobre el orden: El orden importa. Los pasos 1 y 2 construyen el
mapa. El paso 3 distribuye la responsabilidad y el beneficio. El paso 4
refina esa distribución y mide la brecha con lo que ya se asumió. El paso
5 convierte las proporciones en dinero. No se puede calcular el paso 3 sin
el 2, ni el 5 sin el 3. El orden no es convención: es la lógica del análisis.

El Método Prometeo: Imputación Causal para juristas y abogados
Paso 1 — El mapa del caso: el
grafo causal
Paso 1 — El mapa del caso Antes de calcular cualquier
número, hay que tener el mapa. El mapa del método se
llama grafo causal. Es la representación de todos los actores
del caso, sus conexiones y la dirección de esas conexiones.
Sin el mapa, los cálculos son precisos, pero no dicen nada
sobre el caso real.
2.1.1 Los nodos: quiénes están en el caso
Un nodo es cualquier actor que tuvo posición causal en el
resultado. No es cualquier persona que aparece en el
expediente: es quien contribuyó a que el daño ocurriera o
fuera posible. Hay cuatro tipos de nodo que el análisis
siempre distingue porque tienen roles causales
fundamentalmente distintos:
Tipo Qué es Por qué importa para
el análisis
Nodo de Quien diseñó el Es el nodo con mayor
diseño sistema, el protocolo, R* en casi todos los
las condiciones bajo casos institucionales
las cuales el daño era complejos. Su
posible o inevitable. contribución causal no
Puede ser una requiere que haya
persona, un "querido" el daño: basta
departamento o una con que haya diseñado el
institución. sistema que lo producía.
Nodo de Quien operó dentro Su S (sustituibilidad) es
ejecución del sistema diseñado típicamente alta: el
por el nodo de análisis mostrará que
diseño. Ejecutó cualquier otro actor en
instrucciones, siguió esa misma posición
protocolos, actuó habría actuado igual. Eso
reduce su

El Método Prometeo: Imputación Causal para juristas y abogados
dentro de incentivos responsabilidad causal
que no diseñó. neta.
Nodo Un instrumento sin Su presencia en el grafo
instrumental voluntad que tiene apunta causalmente
posición causal: el hacia quien lo diseñó. El
contrato de adhesión, instrumento no puede
el algoritmo, el ser responsable; quien lo
protocolo, el script de creó y desplegó, sí.
ventas. No tiene ego:
es una mediación
neutral.
Nodo final El actor que recibió Define el resultado que
(Nf) el daño. Es el punto se está distribuyendo.
de llegada del grafo, No entra en el cálculo de
no un actor causal. R*: es el destinatario del
análisis.
Analogía: El organigrama y el mapa causal El organigrama
de una empresa muestra quién reporta a quién. El grafo causal muestra
quién condicionó el comportamiento de quién en relación con el daño
específico. A veces coinciden. Con frecuencia no: el responsable causal más
alto puede no aparecer en el organigrama, y quien aparece en la cúspide
puede tener poca influencia causal real sobre el resultado. El grafo se
construye desde los hechos del caso, no desde los títulos corporativos.
Nodo colectivo: Una institución, departamento o grupo que tomó
decisiones colectivas. En el análisis, debe desagregarse en los individuos que
participaron en las decisiones relevantes siempre que la evidencia lo
permita. El nodo colectivo es un agregado útil para mostrar la estructura
causal, pero la asignación de responsabilidad individual requiere la
desagregación.
2.1.2 Las aristas: cómo se conectan
Una arista es una conexión causal entre dos nodos. Si la
acción de A fue condición para que B pudiera actuar como

El Método Prometeo: Imputación Causal para juristas y abogados
actuó, hay una arista de A hacia B. La dirección de la arista
importa: una arista de A hacia B no es lo mismo que una de
B hacia A.
Cada arista tiene un tipo según la relación causal que
representa:
Tipo de Descripción Ejemplo
arista
Arista A realizó la acción que El asesor que entregó
directa produjo directamente el el contrato abusivo al
resultado en B. cliente. Las empleadas
que accedieron al
expediente de un
cliente.
Arista A creó las condiciones El banco que diseñó el
estructural bajo las cuales B pudo script que el asesor
causar el resultado. A no siguió. La institución
causó directamente: que diseñó el rol
habilitó la causa. ambiguo que el gerente
ocupó.
Arista de A tenía el deber y la El consejero
omisión capacidad de impedir el independiente que no
resultado y no lo hizo. actuó ante las señales
La inacción es de alarma. El regulador
causalmente relevante. que no inspeccionó.
Arista nula No existe conexión El acceso al expediente
(w = 0) causal entre A y el del gerente y el fraude
resultado. La arista nula que ocurrió dos días
requiere evidencia después en otro estado.
positiva de la ausencia: No hay ningún eslabón
no es simplemente que documentado.
no se encontró
evidencia.
⚠ La diferencia entre "no hay evidencia de la arista" y "hay
evidencia de que la arista no existe" es fundamental. La primera
produce incertidumbre (que se maneja con rangos). La segunda

El Método Prometeo: Imputación Causal para juristas y abogados
produce una arista nula documentada (w = 0 explícito).
Confundir las dos es el error más frecuente en la construcción
del grafo.
2.1.3 El protocolo de construcción del grafo

### 1. Identificar todos los actores causalmente relevantes del
caso. La pregunta es: ¿sin este actor, el daño habría
ocurrido de la misma manera? Si la respuesta es no, ese
actor es un nodo del grafo.

### 2. Clasificar cada nodo: ¿es un nodo de diseño, de
ejecución, instrumental o el nodo final?

### 3. Trazar las aristas: para cada par de nodos, ¿hay una
conexión causal? ¿En qué dirección? ¿De qué tipo
(directa, estructural, omisión)?

### 4. Documentar cada arista: ¿qué evidencia del expediente
sustenta esa conexión? Un contrato, un correo, un
protocolo, un registro, un testimonio. La arista sin
evidencia es una hipótesis, no un elemento del grafo.
Lo que el grafo NO es: El grafo no es la versión visual de la
acusación. No se construye para probar que alguien es culpable. Se
construye para mapear todas las conexiones causales relevantes, incluyendo
las que apuntan hacia actores que nadie ha mencionado todavía. Con
frecuencia, el nodo de mayor peso causal no aparece en la acusación
original.

El Método Prometeo: Imputación Causal para juristas y abogados
Paso 2 — El peso de las
conexiones: los pesos w
Paso 2 — El peso de las conexiones Trazar las aristas
no es suficiente: hay que medir su fuerza. El peso w de una
arista mide qué tanto determinó el nodo origen el
comportamiento del nodo destino. Un peso alto significa
que el nodo destino tenía poco margen de acción propio;
un peso bajo significa que tenía amplía discreción. El peso
no lo decide el analista libremente: lo determina la evidencia
disponible.
2.2.1 Qué mide el peso w
El peso w de una arista A → B responde a esta pregunta:
dado todo lo que el expediente documenta, ¿qué fracción
del comportamiento de B estaba determinada por A? Un
peso w = 0.85 entre el banco (A) y el asesor (B) dice que el
85% del comportamiento del asesor en la venta estaba
determinado por el diseño del banco —el script, los
incentivos, el protocolo. El 15% restante era margen de
discreción propio del asesor.
El peso no depende de las intenciones de nadie. Depende
de la estructura objetiva de la relación entre los nodos: qué
tan formalizado estaba el procedimiento, qué tan costoso
era apartarse de él, qué tan fungible era el actor en esa
posición.
2.2.2 Los criterios para estimar el peso
El peso de cada arista se estima respondiendo cuatro
preguntas sobre la relación entre los dos nodos:

El Método Prometeo: Imputación Causal para juristas y abogados
Pregunta Peso bajo Peso alto → Relevancia
→ 0 1 forense
1 ¿El Sin Script rígido. Los
comportamien protocolo. Sin variación documentos
to del nodo B Alta posible. institucional
estaba discreción. es
formalizado (manuales,
por un contratos,
protocolo, políticas)
script o son la
instrucción de evidencia
A? más directa
para este
criterio.
2 ¿Qué tan Fácil Imposible o El sistema
costoso era apartarse. con costo de
para B Sin extremo incentivos y
apartarse del consecuenci (despido, las
comportamien as. sanción, consecuenci
to que A exclusión). as
determinaba? documentad
as de la
desobedienc
ia.
3 ¿Hay casos Frecuentes y Inexistentes El historial
documentados sin o con institucional.
de actores en consecuenci consecuencia La cultura
la misma as. s severas organizacion
posición que documentad al
se apartaron? as. documentad
¿Con qué a.
consecuencias
?
4 ¿Qué tan Alta Alta La rotación
fungible es B especificidad fungibilidad. en el puesto,
en esa . Solo B Cualquiera los perfiles
posición? podría habría hecho del cargo, la
¿Cualquier haberlo lo mismo. comparació
persona con hecho. n con pares
esa formación en la misma
posición.

El Método Prometeo: Imputación Causal para juristas y abogados
habría actuado
igual?
La importancia de los criterios: Estos cuatro criterios
ayudan a determinar qué tipo de evidencia (E0-E8) respalda la
arista
2.2.3 La tabla de tipos de evidencia: del tipo
al rango
Una vez identificados los criterios, el analista asigna un
rango de peso — no un número puntual, sino un intervalo
[w_mínimo, w_máximo] — según el tipo de evidencia
disponible para esa arista. Este es el punto de innovación
central del Método Prometeo respecto a cualquier análisis
causal convencional: en lugar de afirmar un peso puntual
que la contraparte puede atacar con otro número, se declara
un rango que la evidencia disponible justifica y se demuestra
que la conclusión del análisis es válida en todo ese rango.
Tipo Descripción de la Rango Por qué ese rango
evidencia w
E1 Documento directo que [0.75 – La evidencia directa
muestra la acción del 0.95] deja poco espacio
nodo: contrato, correo, para la
acta firmada, registro interpretación. El
digital, minuta. rango superior refleja
que incluso un
documento puede
ser parcial o
ambiguo.
E2 Mecanismo causal [0.70 – La pericia técnica es
técnico documentado 0.90] casi tan sólida como
pericialmente: peritaje el documento directo

El Método Prometeo: Imputación Causal para juristas y abogados
contable, análisis pero requiere la
forense digital, validez del método
auditoría especializada. pericial.
E3 Testimonio múltiple [0.55 – El testimonio
convergente con al 0.75] convergente es
menos un corroborante sólido, pero más
documental. Varios disputables que el
testigos independientes documento. La
coinciden y hay divergencia entre
evidencia documental testigos reduce el
consistente (no directa). peso mínimo.
E4 Correlación estadística [0.50 – La correlación
controlada: análisis que 0.70] estadística es
muestra la relación evidencia de
entre el estructura, pero no
comportamiento del de mecanismo
nodo y el resultado, directo. El nivel de
controlando por las control de la
variables relevantes. regresión determina
en qué punto del
rango se cae.
E5 Testimonio único con [0.35 – La vulnerabilidad del
respaldo documental 0.55] testimonio único
parcial. Un solo testigo hace que el rango sea
con al menos un moderado. El
elemento documental elemento
consistente (que no documental
prueba directamente el corroborante lo eleva
hecho pero es del rango E8.
compatible con él).
E6 Inferencia razonada por [0.25 – La inferencia
posición estructural: el 0.45] estructural es
nodo tenía la posición, razonada pero
los recursos y los abierta a
incentivos para la interpretaciones
acción imputada, sin alternativas. Requiere
documentación directa. que no exista
ninguna explicación
alternativa plausible.
E7 Correlación temporal o [0.10 – La correlación sin
espacial sin mecanismo 0.30] mecanismo es la

El Método Prometeo: Imputación Causal para juristas y abogados
documentado. evidencia más débil
Proximidad entre la que produce una
acción del nodo y el arista con peso
resultado sin evidencia positivo. La
de la cadena de coincidencia
transmisión. temporal no es
causalidad.
E8 Dicho único sin ningún [0.05 – El dicho sin respaldo
respaldo. Un solo 0.20] es la evidencia más
testimonio sin débil que el sistema
corroboración de reconoce como tal.
ningún tipo — ni Úsese solo cuando
documental, ni no hay nada más y el
estadística, ni técnica. contexto lo hace
plausible.
E0 Arista nula w = No es la ausencia de
documentada. 0.00 evidencia. Es la
Evidencia positiva de presencia de
que la conexión causal evidencia de la
no existe: registro que ausencia. Requiere el
muestra que la mismo estándar que
información no salió, cualquier arista
imposibilidad técnica positiva.
documentada,
mecanismo alternativo
que excluye al nodo.
La regla del rango: El peso de una arista no es el número
que el analista cree que es correcto. Es el rango que la evidencia
disponible justifica. Si la evidencia es E1, el rango es [0.75,
0.95]. Si es E6, el rango es [0.25, 0.45]. El analista no puede
salirse del rango que su evidencia produce. Si quiere un rango
más estrecho o más alto, necesita evidencia de mejor tipo.
2.2.4 Cómo se defiende el peso ante la
impugnación

El Método Prometeo: Imputación Causal para juristas y abogados
Tipo de Argumento de la Respuesta estándar del
impugnación contraparte análisis
Del tipo de "El peso E3 es Mostrar que incluso con el
evidencia especulativo; peso E7 (rango mínimo
debería ser E7." 0.10-0.30), el banco sigue
siendo el nodo de mayor
R* en el escenario
mínimo. Si la robustez se
mantiene, el argumento de
la contraparte no cambia
la conclusión.
Del valor "El peso 0.80 es 0.50 está dentro del rango
puntual incorrecto; debería ya calculado. Calcular R*
ser 0.50." con w = 0.50: ¿cambia el
nodo de mayor R*? Si no
cambia, el argumento de
la contraparte es
irrelevante para la
conclusión.
De la arista "Ausencia de La arista nula requiere
nula evidencia no evidencia positiva de la
prueba que la arista ausencia (§2.1.2). Si el
sea cero." análisis tiene esa
evidencia, mostrarla. Si no
la tiene, reconocer que la
arista debe asignarse a E7
y recalcular con ese rango.
Del método "Este método no El método es peritaje
está reconocido en experto sobre causalidad
el Código de estructural, admisible
Procedimientos." como tal en la mayoría de
los sistemas procesales. La
declaración de robustez
no reemplaza la decisión
jurídica: aporta evidencia
estructurada que el foro
puede considerar. Ningún
sistema procesal prohíbe
el análisis causal
sistemático.

El Método Prometeo: Imputación Causal para juristas y abogados
2.2.5 El árbol de decisión del análisis de
sensibilidad
Una vez que tienes los tres vectores de R* (escenario
mínimo, central y máximo), este árbol de decisión te guía
hacia la declaración correcta:
# Pregunta Resultado Lo que declaras
posible en el expediente
1 ¿El nodo de SÍ → paso 2 El análisis es
mayor R* es el robusto en cuanto
mismo en w_min, al nodo de mayor
w_central y R*.
w_max?
NO → paso 5 El análisis
identifica dos
candidatos. Seguir
al paso 5.
2 ¿El orden relativo SÍ → paso 3 Robustez
de todos los completa: el
nodos es el ranking es estable
mismo en los tres en todo el rango.
escenarios?
NO → paso 4 El nodo líder es
robusto pero el
orden de los
demás puede
variar.
3 Robustez → "Con cualquier
completa DECLARACIÓN interpretación
alcanzada. A razonable de la
evidencia, el nodo
X es el de mayor
peso causal y el
orden de
responsabilidad es
X > Y > Z en
todo el rango."

El Método Prometeo: Imputación Causal para juristas y abogados
4 El nodo líder es → "Con cualquier
robusto pero el DECLARACIÓN interpretación
orden interno de B razonable de la
los demás puede evidencia, el nodo
cambiar. X tiene el mayor
peso causal. El
orden relativo
entre Y y Z
depende del
supuesto
adoptado respecto
a [arista
específica]."
5 El nodo de mayor SÍ → paso 6 Diferencia
R* cambia entre significativa: hay
escenarios. ¿La un candidato
diferencia entre dominante en el
los dos escenario central,
candidatos en el aunque no haya
escenario central robustez completa
es mayor al 10%? en el rango.
(Nota: el umbral
del 10% refleja la
práctica forense
— diferencias
menores suelen
estar dentro del
margen de
incertidumbre del
método y no
justifican afirmar
que hay un
candidato
dominante.)
NO → paso 7 Los dos
candidatos son
prácticamente
equivalentes.
6 Diferencia → "La evidencia base
significativa en el DECLARACIÓN sugiere que el
central (>10%) C nodo X tiene
mayor peso causal

El Método Prometeo: Imputación Causal para juristas y abogados
pero no hay que Y. Esta
robustez. conclusión podría
cambiar si se
demostrara que
[evidencia
específica que
reduciría la
incertidumbre]. La
pieza
determinante es:
[identificar]."
7 Los dos → "La evidencia
candidatos son DECLARACIÓN disponible no
prácticamente D permite
equivalentes en el determinar cuál de
rango. los dos nodos, X
o Y, tiene el
mayor peso
causal. Ambos
son responsables
causales de
magnitud
comparable. La
evidencia
adicional que
resolvería la
disputa es:
[identificar]."

El Método Prometeo: Imputación Causal para juristas y abogados
Paso 3 — La distribución
causal: R* y B*
Paso 3 — La distribución causal Con el mapa construido
y los pesos asignados, el análisis puede responder la
pregunta central: ¿qué fracción del resultado le corresponde
causalmente a cada actor? El método da dos respuestas
simultáneas y complementarias. R* mide la fracción del
daño causalmente atribuible a cada actor. B* mide la
fracción del beneficio obtenido por cada actor. El análisis
que solo calcula R* es incompleto: el daño al afectado y el
beneficio del causante son las dos caras del mismo evento.
2.3.1 R*: la fracción del daño
R* (R estrella): El vector que distribuye la responsabilidad
causal del daño entre todos los nodos del grafo. R*_i es el
porcentaje del daño causalmente atribuible al nodo i. La
suma de todos los R* es siempre 100%. R* no mide
intención, no mide culpabilidad, no mide cuánto reconoció
el actor su posición: mide posición causal objetiva en el
sistema de mediaciones.
R* se calcula mediante el método de las rondas, que se
explica en detalle en el Capítulo 3. Por ahora, lo que importa
entender es su lógica: cada nodo recibe una fracción de la
responsabilidad total en proporción a cuánto determinó el
comportamiento de los demás nodos y, a través de ellos, el
resultado final. Los nodos que determinaron a muchos con
peso alto tienen R* alto. Los nodos que operaron dentro de
sistemas diseñados por otros tienen R* bajo.
El resultado estructural que el método produce
consistentemente en casos institucionales complejos es este:
el nodo de diseño tiene el R* más alto. No por definición,
sino porque su red de aristas de alta influencia acumula más
peso que cualquier nodo individual de ejecución. Cuando el

El Método Prometeo: Imputación Causal para juristas y abogados
análisis produce lo contrario — cuando el ejecutor tiene
mayor R* que el diseñador — es señal de que el grafo está
mal construido.
R*_diseñador > R*_ejecutor en la estructura causal
típica de un caso institucional
2.3.2 B*: la fracción del beneficio
B* (B estrella): El vector que distribuye el beneficio
obtenido por los actores del grafo como consecuencia del
evento dañino. B*_i es el porcentaje del beneficio total que
obtuvo el nodo i. La suma de todos los B* positivos es
100% del beneficio total. B* y R* son vectores distintos: un
actor puede tener R* alto y B* bajo (causó mucho pero no
obtuvo beneficio directo) o R* bajo y B* alto (causó poco,
pero se benefició desproporcionadamente).
La diferencia entre R* y B* es el instrumento que hace
visible uno de los mecanismos más frecuentes en los casos
institucionales complejos: el actor que diseñó las
condiciones del daño obtuvo beneficio económico real
mientras que el ejecutor visible — que tiene el menor R* —
carga con la mayoría de las consecuencias y obtiene ningún
beneficio.
B* se calcula identificando las fuentes de beneficio del
evento dañino y distribuyéndolas entre los nodos según la
evidencia económica disponible: ahorros de costos,
ingresos adicionales, posiciones mantenidas,
responsabilidades evadidas, capital reputacional protegido.
No todos los beneficios son monetarios directos; todos son
cuantificables.
B*_i = Beneficio_neto_i / Beneficio_total

El Método Prometeo: Imputación Causal para juristas y abogados
Analogía: El seguro de incendio fraudulento Un propietario
contrata a un tercero para que incendie su local y cobre el seguro. R* del
tercero en el incendio: alto (fue quien prendió el fuego). B* del tercero: bajo
(cobró una tarifa, no el seguro). R* del propietario: moderado-alto (diseñó
y financió el plan). B* del propietario: muy alto (cobró el seguro, eliminó
deudas, se deshizo de un inmueble problemático). La comparación R* vs.
B* revela quién fue el verdadero beneficiario del daño y quién fue el ejecutor
fungible.
2.3.3 La relación entre R* y B*: el mapa
completo del caso
Comparar R* y B* para cada actor produce cuatro tipos de
posición que tienen traducciones jurídicas directas:
Posición Patrón Interpretación y relevancia jurídica
R* /
B*
Diseñador R* alto El actor más importante del caso.
beneficiario B* alto Causó mucho y se benefició mucho.
Es la base del argumento de
responsabilidad principal y de la
pretensión de restitución del
beneficio obtenido. Fraude annona en
su forma más visible.
Diseñador R* alto Causó mucho pero no obtuvo
sin beneficio B* bajo beneficio directo. Puede ser un
directo ejecutor de rango medio que diseñó el
subsistema sin ser el beneficiario
final. Su R* lo hace responsable; la
ausencia de B* puede modular la
pretensión.
Ejecutor sin R* bajo El perfil más frecuente del ejecutor
beneficio B* bajo sobre-imputado: causó poco y no
obtuvo nada. Es el argumento más
fuerte de la defensa: ni la causalidad

El Método Prometeo: Imputación Causal para juristas y abogados
ni el beneficio justifican que sea el
nodo principal de la imputación.
Beneficiario R* bajo Obtuvo mucho sin haber causado
sin B* alto directamente. Típico del beneficiario
causalidad final que aparece detrás de capas
directa corporativas. El contraste R*/B*
señala la pretensión de
enriquecimiento sin causa
independientemente del análisis de
causalidad directa.
El argumento que R* y B* juntos permiten: "El nodo X
causó el 59.8% del daño (R*) y obtuvo el 65% del beneficio
(B*). El nodo A causó el 19.1% del daño y no obtuvo ningún
beneficio. La pretensión contra X se sustenta en su posición
causal (R*) y en su enriquecimiento sin causa (B*). La
pretensión de la defensa de A se sustenta en que ni su posición
causal ni su beneficio justifican que sea el nodo principal de la
imputación." Ese es un argumento que ningún análisis de dolo
convencional puede construir con esta precisión.
2.3.4 El análisis de sensibilidad: de un
número a un rango defendible
R* y B* se calculan con los pesos asignados en el Paso 2.
Pero los pesos son rangos, no puntos únicos. Eso significa
que R* y B* también son rangos: hay un R* mínimo
(calculado con los pesos más bajos) y un R* máximo
(calculado con los pesos más altos).
El análisis de sensibilidad calcula R* y B* en tres puntos del
rango de pesos: el mínimo, el central y el máximo. Luego
aplica el criterio de robustez: ¿cambia el nodo de mayor R*
en algún punto del rango?
Pregunta del Respuesta en el caso del banco
criterio

El Método Prometeo: Imputación Causal para juristas y abogados
¿Es el mismo nodo el Sí. En los tres escenarios, B (banco)
de mayor R* en tiene el mayor R* (entre 53.2% y
w_min, w_central y 65.4%). El ranking no cambia.
w_max?
¿Cambia el orden No. En los tres escenarios: B > R > A. El
relativo de los demás banco tiene siempre el mayor R*, riesgos
nodos? el segundo, el asesor el menor.
Diagnóstico Análisis robusto: la conclusión sobre
quién tiene el mayor peso causal es
independiente del valor puntual de w
que se elija dentro de los rangos
razonables.
No todos los casos producen robustez. Si el rango de pesos
es suficientemente amplio o si dos actores tienen posiciones
causales cercanas, el nodo de mayor R* puede cambiar entre
los extremos del rango. Eso no invalida el análisis:
simplemente produce un resultado diferente.
⇄ Disputable: Si en el escenario mínimo el banco tiene R* =
42% y riesgos tiene R* = 45%, y en el escenario máximo el
banco tiene R* = 58% y riesgos tiene R* = 31%, el análisis
dice: "La evidencia disponible no determina con certeza cuál
de los dos tiene el mayor peso causal. Ambos son candidatos.
Esta es la pieza de evidencia que resolvería la disputa:
[identificar la evidencia específica que reduciría el rango de la
arista en cuestión]."
Un análisis que produce disputa estructural no es un análisis
fallido: es un análisis honesto que dice exactamente lo que
la evidencia permite afirmar y señala qué falta para poder
decir más.
Resultado Qué significa y qué se declara
Análisis El nodo de mayor R* es el mismo en el mínimo, el
robusto central y el máximo. La conclusión sobre quién tuvo
el mayor peso causal no depende del valor puntual
de los pesos elegido dentro del rango razonable.
Declaración: "Con cualquier interpretación

El Método Prometeo: Imputación Causal para juristas y abogados
razonable de la evidencia disponible, el nodo X es el
de mayor peso causal."
Caso El nodo de mayor R* cambia en algún punto del
disputable rango. El análisis no puede declarar un ganador
único. Declaración: "La evidencia disponible no
permite determinar con certeza cuál de los dos
nodos, X o Y, tiene el mayor peso causal. Esta es la
evidencia adicional que resolvería la disputa."
Por qué el rango blinda el argumento: Con un peso puntual,
la contraparte puede oponer un perito que diga otro número. Con un rango
y el criterio de robustez, la contraparte no puede simplemente decir que el
número es diferente: tiene que demostrar que existe una interpretación
razonable de la evidencia bajo la cual el nodo de mayor R* es diferente. Si
el análisis de sensibilidad ya exploró todo el rango razonable y el resultado
es siempre el mismo, esa demostración es prácticamente imposible. Ese es
el blindaje.

El Método Prometeo: Imputación Causal para juristas y abogados
Paso 4 — La idiosincrasia y la
brecha: S y Δ
Paso 4 — La idiosincrasia y la brecha R* dice cuánto
contribuyó cada actor al resultado. El Paso 4 responde dos
preguntas que R* no responde: ¿cuánto de esa contribución
era propia del actor y cuánto era del sistema? ¿Y cuánto de
lo que le correspondía ya asumió? La primera pregunta la
responde S. La segunda, Δ.
2.4.1 S: el índice de sustituibilidad
S (sustituibilidad): El porcentaje de la contribución causal
del actor que era estructural: lo que habría ocurrido igual
con cualquier otro actor en la misma posición bajo las
mismas condiciones. S = 1.0 significa que el actor era
completamente fungible. S = 0.0 significa que solo ese actor
específico podría haber producido ese resultado. La
responsabilidad causal neta de un actor = R* × (1 − S).
S es el instrumento más poderoso del método para el
argumento de defensa del ejecutor y para el argumento de
imputación al diseñador. Un asesor que siguió un script
obligatorio bajo amenaza de consecuencias laborales tiene
S ≈ 1.0: su R*_neta es prácticamente cero, aunque su R*
total sea significativo. El banco que diseñó ese script tiene
S ≈ 0.2: esa decisión específica dependía de la voluntad
deliberada de esa dirección, no de ningún sistema que lo
determinara.
R*_neta_i = R*_i × (1 − S_i)
S se calcula con los mismos cuatro criterios del Paso 2
(estandarización del procedimiento, costo de
desobediencia, casos documentados de desobediencia,
fungibilidad del actor). El Capítulo 3 mostrará el cálculo

El Método Prometeo: Imputación Causal para juristas y abogados
exacto. Por ahora, la lógica: cuanto más determinado estaba
el comportamiento del actor por el sistema en el que
operaba, mayor es S y menor es la responsabilidad que le
corresponde de manera idiosincrática.
2.4.2 α: el coeficiente de asunción
α (alfa, coeficiente de asunción): El grado en que el actor
ha actuado sobre su posición causal mediante acciones
concretas y verificables. α = 0: no hizo nada — no pagó, no
reparó, no modificó el sistema. α = 1: asumió
completamente — pagó proporcional a su R*, reparó el
daño, modificó el sistema que lo produjo. α mide acciones,
no intenciones ni arrepentimiento.
La confusión más frecuente sobre α es creer que mide la
culpa subjetiva del actor. No la mide. α es completamente
independiente del dolo. Un actor que actuó con plena
intención deliberada (Anteros dominante) puede tener α
alto si después pagó y reparó. Un actor que actuó desde
Fobos — sin dolo, bajo presión sistémica — puede tener α
= 0 si nunca hizo nada para remediar su posición causal.
Acción del actor ¿Cuenta Por qué
para α?
Pagar una multa Sí Acción concreta de asunción
regulatoria económica, verificable en el
proporcional a R* expediente.
Reparar Sí La forma más completa de α.
integralmente el Reconocimiento + reparación.
daño a los
afectados

El Método Prometeo: Imputación Causal para juristas y abogados
Modificar el Sí α estructural: reduce la
sistema que probabilidad del próximo
produjo el daño evento.
Reconocer la Sí — Reconocimiento sin reparación
posición causal parcial es α bajo pero distinto de cero.
ante el foro
Declarar No Declaración sin consecuencia
"lamentamos lo concreta. No modifica α.
ocurrido" sin
ninguna acción
Haber actuado con No El dolo es relevante para los
dolo deliberado afecta α hijos de Afrodita y para la
responsabilidad subjetiva. No
para α, que mide acciones
posteriores al evento.
⚠ α mide lo que el actor hizo después del evento, no con qué
intención actuó durante él. El análisis del dolo (si lo hubo) se
hace con los hijos de Afrodita, que se analizan en el expediente
como parte de la responsabilidad subjetiva. α y los hijos son
instrumentos distintos que responden preguntas distintas.
2.4.3 Δ: la brecha
Δ (Delta, déficit de asunción): La diferencia entre lo que
el actor causó (R*) y lo que asumió (α). Δ > 0 significa que
el actor causó más de lo que asumió: hay un déficit que
cierra la brecha de la pretensión. Δ < 0 significa que el actor
asumió más de lo que causó: es el argumento de la sobre-
imputación.
Δ_i = R*_i − α_i
Δ es la medida de la inversión causal cuantificada. En el
Caso Eje del libro, el banco tenía Δ = +51.8% (causó 59.8%
y asumió 8%) y el asesor tenía Δ = −40.9% (causó 19.1%

El Método Prometeo: Imputación Causal para juristas y abogados
pero cargó con el 60% de las consecuencias). Esos dos Δ
juntos son la demostración matemática de la inversión
causal: el actor de menor peso causal absorbió la mayor
parte de las consecuencias, y el actor de mayor peso causal
evadió la mayor parte de las suyas.
2.4.4 La escala de α: voluntario, forzado e
impuesto
La escala de α distingue seis niveles de asunción. En el
dominio clínico —donde este instrumento fue
originalmente desarrollado— todos los niveles
corresponden a procesos voluntarios de integración del
actor sobre su propia historia. En el dominio de la
imputación causal hay una diferencia fundamental que el
método hace explícita: α también puede ser forzado o
impuesto por otros actores del sistema, y ese α forzado
produce el mismo efecto sobre Δ que el α voluntario.
Si el banco pagó la multa porque el regulador se la impuso,
su α sube igual que si la hubiera pagado voluntariamente. Si
el asesor fue despedido y procesado penalmente por
decisión de la institución, su α sube, aunque nunca haya
reconocido ni deseado asumir nada. El método registra la
asunción efectiva, no la intención con la que ocurrió.
Nivel de Ran Descripción Fuente en Indicador
asunción go α observable imputació en el
n causal expedient
e
Negación / 0.00 El actor no Voluntaria Sin pagos,
evasión – reconoce su y forzada = sin
total 0.05 posición 0. El actor sanciones,
causal, no ha no asumió sin
reparado nada nada y el modificacio
y ha evadido sistema nes del
activamente tampoco le sistema, sin

El Método Prometeo: Imputación Causal para juristas y abogados
cualquier impuso reconocimi
consecuencia. nada. ento.
Reconocim 0.06 El actor Voluntaria Comunicad
iento – reconoció mínima. os públicos
nominal 0.20 formalmente Sin α documenta
su posición, forzado dos.
pero sin significativ Ningún
consecuencia o. pago ni
concreta. sanción.
Disculpa
pública,
comunicado
institucional,
"lamentamos
lo ocurrido".
Asunción 0.21 El actor pagó Combinaci Multas
parcial – o sufrió ón de α regulatorias
0.45 consecuencias voluntario de hasta el
menores a lo (acuerdos 20-30% del
que su R* parciales) y daño.
indica. α forzado Sanciones
Reconoció (multas administrat
parte de su moderadas, ivas
posición sin sanciones menores.
haber administrati Pagos
reparado vas). parciales.
proporcional
mente.
Asunción 0.46 El actor ha Combinaci Pagos del
activa en – asumido una ón activa 40-60% del
proceso 0.70 parte de α daño.
significativa voluntario Modificaci
de su (acuerdos, ones
posición y modificacio documenta
está en nes del das del
proceso de sistema) y α sistema.
reparación. forzado Sentencias
Hay acciones (sentencias con
concretas parciales, ejecución
aunque no embargos, parcial.
hayan despidos).
alcanzado la

El Método Prometeo: Imputación Causal para juristas y abogados
proporcionali
dad completa.
Asunción 0.71 El actor ha Frecuente Procesos
funcional – asumido la mente α penales
0.89 mayor parte forzado activos,
de su dominante: despidos
posición de el sistema documenta
manera le impuso dos,
verificable. consecuenc embargos
Las ias ejecutados,
consecuencias significativa exclusiones
sufridas son s (despido, de registro
proporcionale proceso sectorial.
s a su R* penal
aunque no activo,
perfectas. embargo,
exclusión
sectorial).
Asunción 0.90 El actor Combinaci Sentencias
plena – asumió ón de α firmes con
1.00 completamen voluntario pago
te su posición (reparación completo.
causal. La integral, Acuerdos
reparación es reconocimi de
proporcional ento ante el reparación
a su R*, el foro) y/o α integral.
sistema que forzado Modificaci
produjo el (sentencia ón
daño fue firme documenta
modificado y ejecutada). da del
la posición sistema
causal fue causante.
reconocida.
El asesor sobre-imputado: En el caso del banco, el asesor fue
despedido y procesado penalmente. Esas consecuencias le fueron impuestas
por la institución — no las eligió. Sin embargo, producen un α forzado ≈

### 0.60. Ese α alto en el asesor, combinado con su R* = 19.1%, genera un
Δ = −40.9%: asumió mucho más de lo que causó. El método registra
ese desequilibrio con precisión porque distingue entre la magnitud de lo que
causó (R*) y la magnitud de lo que asumió (α), independientemente de si
la asunción fue voluntaria o impuesta.

El Método Prometeo: Imputación Causal para juristas y abogados
La institución que impone α sin asumirlo: Un patrón
frecuente en los casos de inversión causal: la institución con R* alto impone
consecuencias al ejecutor (aumenta el α del ejecutor) mientras su propio α
permanece cerca de cero. El resultado es que la brecha Δ del ejecutor se
vuelve negativa (fue sobre-imputado) y la brecha Δ de la institución se
vuelve aún más positiva (causó mucho, no asumió nada, y encima usó al
ejecutor como vehículo de asunción subrogada). Eso no es accidental: es el
mecanismo del fraude annona en los sistemas institucionales.

El Método Prometeo: Imputación Causal para juristas y abogados
Paso 5 — La magnitud del
daño: D_total y el ajuste
debitor
Paso 5 — La magnitud del daño Los cuatro pasos
anteriores produjeron proporciones: R*, B*, S, R*_neta, α,
Δ son todos números entre 0 y 1 o porcentajes. El Paso 5
multiplica esas proporciones por el tamaño real del daño
para obtener los montos económicos que le corresponden
a cada actor. D_total es el denominador de todo el análisis.
El ajuste debitor (AD) es la traducción final de la causalidad
al dinero.
2.5.1 D_total: los tres componentes del daño
D_total: La suma de todos los daños causados por el
evento. Tiene tres componentes: lo que la víctima tenía y
perdió (T_invertido), lo que la víctima habría ganado y no
ganó (T_impedido), y la alteración permanente de la
trayectoria de la víctima (ΔT_trayectoria).
D_total = T_invertido + T_impedido + ΔT_trayectoria
Componente Nombre ¿Qué Disputabilida
jurídico incluye? d típica
T_invertido Daño Lo que la Baja — el más
emergente víctima tenía documentable
y perdió con estados de
directamente: cuenta y
capital, facturas.
activos,
contratos,
ingresos del
período del
daño.

El Método Prometeo: Imputación Causal para juristas y abogados
T_impedido Lucro Lo que la Media —
cesante víctima requiere
habría proyección
ganado y no con tasas de
ganó: mercado
rendimientos documentadas
, ingresos .
proyectados,
oportunidade
s no
aprovechadas
durante el
período de
afectación.
ΔT_trayectori Pérdida de La alteración Alta —
a oportunida permanente requiere
d / de lo que la pericia y
trayectoria víctima modelos de
habría proyección. El
podido ser o más
tener: daño al frecuentement
perfil e disputado y
crediticio, limitado por la
exclusión jurisprudencia
futura de .
mercados,
pérdida de
capacidad de
acumulación.
Sobre ΔT_trayectoria: No todos los sistemas procesales admiten
ΔT_trayectoria con la misma amplitud. En algunos fueros es limitado
por jurisprudencia; en otros es inexistente como categoría autónoma. El
método siempre calcula D_total con los tres componentes como base
máxima. El abogado decide qué componentes presentar según el foro. La
diferencia entre el D_total completo y el D_total procesalmente admisible
es información útil: señala exactamente qué quedó fuera del alcance del
foro.

El Método Prometeo: Imputación Causal para juristas y abogados
2.5.2 El ajuste debitor: de la proporción al
monto
Ajuste debitor (AD): El monto del daño total
proporcional al peso causal de cada actor. AD_i = R*_i ×
D_total. El ajuste debitor usa R* total, no R*_neta, porque
el daño existe independientemente de si el actor era
sustituible. S y R*_neta sirven para argumentar quién debe
cargar con el AD; no reducen el monto del daño.
AD_i = R*_i × D_total
El ajuste debitor es el punto de partida de la cuantificación
de la pretensión. No es el monto de la condena: el foro
puede ajustar ese monto según criterios jurídicos
adicionales (prescripción, topes legales, conducta
concurrente). Pero AD es lo que la causalidad indica que
corresponde, antes de cualquier ajuste procesal.
Cuando R* y B* se calculan juntos, el análisis produce dos
ajustes: el AD basado en R* (la responsabilidad por el daño)
y el AD_B basado en B* (el enriquecimiento sin causa). En
casos donde B_total > D_total —cuando el causante
obtuvo más de lo que la víctima perdió— el AD_B puede
ser el argumento más sólido de la pretensión.

El Método Prometeo: Imputación Causal para juristas y abogados
El protocolo completo: los
cinco pasos en una vista
Esta tabla resume el protocolo completo del análisis. Cada
fila es un paso; cada columna muestra qué produce, qué
herramienta usa y qué evidencia necesita. El Capítulo 3
desarrolla el cálculo de cada uno.
# Paso Producto Herramienta Evidencia clave
del expediente
1 El Grafo G = Clasificación Contratos,
mapa (N, A, w) de nodos y manuales,
aristas organigramas,
protocolos,
expediente
completo.
2 Los Rangos w Tabla E0-E8 Documentos
pesos ∈ [w_min, con criterios (E1), peritajes
w_max] (E2), testimonios
(E3-E5), posición
estructural (E6),
correlación (E4,
E7), dicho único
(E8).
3 R* y Vectores Método de las El grafo del Paso
B* R* y B* rondas + 1 y los pesos del
con rangos sensibilidad Paso 2. Fuentes
económicas para
B*: balances,
ingresos,
posiciones
mantenidas.
4 S y Δ S_i, Criterios de Casos de
R*_neta_i, sustituibilidad desobediencia
α_i, Δ_i + acciones documentados,
verificables estructura de
incentivos,

El Método Prometeo: Imputación Causal para juristas y abogados
acciones de
reparación
realizadas.
5 D_total D_total = D_total × R* Estados de
y AD T_inv + = AD cuenta (T_inv),
T_imp + pericia de
ΔT · proyección
AD_i por (T_imp), pericia
nodo de trayectoria
(ΔT).
Cómo se lee el resultado del
análisis
Una vez completados los cinco pasos, el análisis produce
para cada actor del caso un perfil con seis números. Este es
el perfil del caso del banco que usaremos como referencia a
lo largo del libro:
Actor R* B* S R*_net α Δ
a
Banco 59.8 65 0.2 47.8% 0.0 +51.8% ←
(direcció % % 0 8 DÉFICIT
n)
Direcció 21.1 18 0.6 8.4% 0.0 +19.1% ←
n de % % 0 2 DÉFICIT
riesgos
Asesor(es 19.1 0% 1.0 0.0% 0.6 −40.9% ←
) % 0 0 SOBRE-
IMPUTAD
O

El Método Prometeo: Imputación Causal para juristas y abogados
Este perfil de seis números es lo que el Capítulo 3 enseña a
calcular. Lo que este capítulo enseñó es cómo leerlo: el
banco causó el 59.8% del daño y obtuvo el 65% del
beneficio. El asesor causó el 19.1% del daño, obtuvo el 0%
del beneficio, y cargó con el 60% de las consecuencias. La
diferencia entre ambos Δ — +51.8% del banco y −40.9%
del asesor — es la inversión causal cuantificada con la que
este método trabaja.
Los números del análisis: tabla
de referencia rápida
Esta tabla resume el significado y el cálculo de cada número
del método para uso cotidiano en el trabajo forense:
Símb Nombre ¿Qué mide? Fórmula Uso en el
olo expediente
w Peso de La fuerza de la w ∈ [0,1] Se asigna
arista conexión según el
causal entre tipo de
dos nodos. evidencia
Cuánto (E0-E8) en
determinó A rangos
el [w_min,
comportamien w_max].
to de B. No es un
número
libre: lo
determina
la evidencia.
R* Peso La fracción Rondas Argumento
causal del daño central del
(daño) causalmente análisis. Se
atribuible a presenta
cada actor. La con su
suma de todos rango

El Método Prometeo: Imputación Causal para juristas y abogados
los R* es [R*_min,
siempre 100%. R*_max] y
la
declaración
de
robustez.
B* Peso La fracción Benef_i Se compara
causal del beneficio / con R* para
(beneficio total obtenido B_total revelar
) por cada actor quién causó
como y quién se
consecuencia benefició.
del evento Base de la
dañino. R* y pretensión
B* son de
vectores enriquecimi
distintos. ento sin
causa
cuando B*
> R*.
S Sustituibil Qué fracción (A+B+C Defensa del
idad de la )/3 ejecutor (S
contribución alto).
causal era Imputación
estructural: al diseñador
habría (S bajo).
ocurrido igual
con cualquier
otro actor en
esa posición.
R*net Resp. La R* × Argumento
a causal contribución (1−S) sobre quién
neta idiosincrática: debe cargar
lo que solo ese con la
actor, con sus mayor parte
características de la
específicas, responsabili
podría haber dad en los
producido. escritos.
α Asunción El grado en 0 a 1 Se verifica
que el actor en el

El Método Prometeo: Imputación Causal para juristas y abogados
actuó sobre su expediente:
posición pagos,
causal sanciones,
mediante modificacio
acciones nes del
concretas. sistema,
Incluye α reconocimi
voluntario y α entos ante
forzado. Mide el foro.
hechos, no
intenciones.
Δ Déficit La brecha R* − α El número
entre lo que
causado (R*) y cuantifica la
lo asumido inversión
(α). Δ > 0: causal. Δ
déficit (base positivo del
de la banco + Δ
pretensión). Δ negativo del
< 0: sobre- asesor = la
imputación medida del
(base de la desequilibri
defensa). o.
AD Ajuste El monto del R* × Punto de
debitor daño total D_total partida de
proporcional la
al R* de cada cuantificaci
actor. Usa R* ón. El foro
total, no aplica
R*_neta: el criterios
daño existe jurídicos
independiente adicionales
mente de la sobre este
sustituibilidad. monto
base.

El Método Prometeo: Imputación Causal para juristas y abogados
Lo que este capítulo estableció
✓ El análisis tiene cinco pasos en orden fijo. El orden no es
convención: es la lógica del método. La causalidad se resuelve
primero; el dinero llega al final.
✓ El grafo causal distingue cuatro tipos de nodo (diseño,
ejecución, instrumental, final) y cuatro tipos de arista (directa,
estructural, omisión, nula). Cada arista requiere evidencia del
expediente.
✓ El peso w de cada arista se determina por el tipo de evidencia
disponible (tabla E0-E8), no por la opinión del analista. La
evidencia produce un rango [w_min, w_max], no un punto
único.
✓ R* distribuye la responsabilidad causal del daño. B* distribuye
el beneficio obtenido. La comparación R*/B* revela el perfil
completo de cada actor: causante beneficiario, ejecutor sin
beneficio, o beneficiario sin causalidad directa.
✓ El análisis de sensibilidad calcula R* y B* en todo el rango de
pesos y declara si el resultado es robusto. La robustez blinda el
argumento contra la impugnación adversarial.
✓ S mide la fracción del R* que era estructural. R*_neta = R* ×
(1−S) es la contribución idiosincrática del actor. α mide
acciones concretas de asunción, no intenciones. Δ = R* − α es
la brecha.
✓ D_total = T_invertido + T_impedido + ΔT_trayectoria. El
ajuste debitor AD = R* × D_total. El Capítulo 3 calcula todo
esto paso a paso con aritmética básica.

El Método Prometeo: Imputación Causal para juristas y abogados
EL MÉTODO PROMETEO · IMPUTACIÓN CAUSAL

