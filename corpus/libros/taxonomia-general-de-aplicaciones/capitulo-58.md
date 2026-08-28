## PARTE VIII · Deporte y Rendimiento

### Capítulo 58
Lesiones y seguridad en el deporte —
responsabilidad en el diseño de reglas
Organ. Estru. Model. Educa. Crisi.
Para el mediador que busca precisión · Cómo usar este
capítulo
Este capítulo es Nivel B — derivación con rangos candidatos de
calibración. Aplica los instrumentos del cap. 12 (Ingeniería de sistemas
y confiabilidad) al dominio de la seguridad deportiva: las lesiones
producidas por el diseño de las reglas del deporte, la infraestructura de
los estadios y las prácticas de entrenamiento. El instrumento central es
el INCF (Índice de Necesidad Causal del Fallo) aplicado a la lesión
deportiva: no pregunta «¿quién golpeó al jugador?» sino «¿sin qué diseño
de reglas, equipamiento o gestión de la carga de entrenamiento la lesión
no habría ocurrido o no habría tenido esa gravedad?».
Los casos de referencia son las lesiones por conmoción cerebral en deportes
de contacto (fútbol americano, rugby, fútbol, boxeo) donde el sistema
médico-legal ha establecido que los diseñadores de las reglas tenían
información sobre el riesgo que no procesaron adecuadamente. El R* del
diseñador de las reglas es positivo cuando tenía esa información y no
actuó sobre ella.
§1 El daño deportivo como fallo del sistema de
seguridad
La lesión deportiva tiene la misma estructura que el accidente
de ingeniería del cap. 50: el fallo técnico observable (el golpe,
la caída, el impacto) y la decisión humana que hizo posible que

Taxonomía General de Aplicaciones
ese fallo produjera daño a esa escala (el diseñador de las reglas
que no modificó la mecánica del juego cuando el riesgo era
conocido, el federativo que no implementó los protocolos de
gestión de conmociones, el club que sobreexplotó a los
jugadores sin respetar los períodos de recuperación). El nodo
de mayor INCF frecuentemente no es el jugador que golpeó
ni el árbitro que no detuvo el juego: es el diseñador de las reglas
que no modificó el sistema cuando el estándar médico del
período establecía que la modificación era necesaria.
INCF_lesión(nodo_i) = P (daño_a_esa_gravedad | sin la
decisión/omisión del nodo_i)
El D_vital del atleta lesionado sigue la misma estructura del D_vital de los
dominios anteriores: D_vital = T_invertido (tiempo de vida en incapacidad
o tratamiento) + T_impedido (la actividad deportiva y profesional impedida
por la lesión) + ΔT_trayectoria (la brecha permanente entre la trayectoria
profesional que el atleta habría tenido sin la lesión y la trayectoria real). Para
las lesiones que producen daño neurológico acumulativo (la encefalopatía
traumática crónica de los deportes de contacto), el ΔT_trayectoria es el
componente de mayor magnitud y puede ser inconmensurable en su dimensión
de calidad de vida.
§2 Escala Dep0–Dep8 en lesiones y seguridad
deportiva
Tipo de
evidencia en Rango
Nivel Descripción
lesiones w
deportivas
Dep1 Análisis El análisis biomecánico de la [0.70,
biomecánico lesión que establece el 0.88]
forense de la mecanismo causal, combinado
lesión + con la documentación de que el
historial médico diseñador de las reglas (la
completo del federación, el club) tenía
atleta + análisis información del riesgo antes de
de la mecánica la lesión.

Taxonomía General de Aplicaciones
Tipo de
evidencia en Rango
Nivel Descripción
lesiones w
deportivas
del juego que
produjo la
lesión +
documentación
de que el
diseñador de las
reglas tenía
información del
riesgo
Dep2 Análisis médico El análisis médico de la lesión [0.58,
de la lesión con con acceso al historial del atleta 0.76]
acceso al y la documentación del
historial del conocimiento del riesgo por el
atleta + análisis sistema.
de la regla o
práctica que
contribuyó
causalmente +
documentación
del
conocimiento
del riesgo por el
sistema
Dep3 Estudios Los estudios epidemiológicos [0.46,
epidemiológicos que establecen la tasa de 0.62]
de la tasa de lesiones producidas por el tipo
lesiones por el de regla o práctica analizada,
tipo de regla o combinados con el análisis de la
práctica lesión específica.
analizada +
análisis de la
lesión específica
Dep4 Análisis médico El análisis médico que establece [0.28,
de la lesión sin el mecanismo causal de la lesión 0.46]
documentación pero sin documentación de que
del el diseñador de las reglas tenía
conocimiento información del riesgo antes de
del riesgo por el la lesión.
sistema

Taxonomía General de Aplicaciones
Tipo de
evidencia en Rango
Nivel Descripción
lesiones w
deportivas
Dep0 Análisis El análisis que establece que la w =
Dep1/Dep2 lesión fue producida por una 0.00
que establece combinación de factores fuera
que la lesión fue del espectro de riesgo que el
consecuencia de estándar médico del período
un evento no establecía para ese deporte.
previsible dado
el diseño
correcto del
sistema de
seguridad
§3 Los nodos del grafo de la lesión deportiva
Nodo del
Función
grafo de la INCF típico S típico
causal
lesión
Diseñador de las Las reglas del Moderado-alto Moderada
reglas deporte [0.25–0.45] [0.38–0.60]
(federación, liga, determinan cuando el cuando la
organismo la mecánica riesgo era resistencia a la
rector) del juego y el documentado y reforma de las
nivel de el estándar del reglas era
contacto período sistémica en el
permitido. El requería la deporte del
diseñador de reforma. período.
las reglas
tiene INCF
positivo
cuando el
riesgo de
lesión era
conocido por
el estándar
médico del
período y las
reglas no se
modificaron

Taxonomía General de Aplicaciones
Nodo del
Función
grafo de la INCF típico S típico
causal
lesión
para
reducirlo.
Club / El club tiene Moderado Moderada-alta
organización INCF [0.20–0.38] [0.45–0.65]
deportiva (carga positivo cuando la cuando la
de cuando la sobreexplotaci sobreexplotaci
entrenamiento y carga de ón era ón era la
sobreexplotació entrenamient idiosincrática convención del
n) o impuesta al del club. deporte
atleta excedía profesional del
los límites de período.
recuperación
que el
estándar de
medicina
deportiva del
período
establecía, o
cuando el
atleta fue
obligado a
competir con
lesiones
previas
conocidas.
Personal médico El médico Moderado Moderada
del equipo del equipo [0.18–0.35] [0.40–0.60]
(protocolo de tiene INCF cuando el cuando el
gestión de positivo protocolo de protocolo era el
lesiones cuando autorización al estándar del
inadecuado) autorizó al regreso no período.
atleta a seguía el
regresar al estándar.
juego con
una lesión
que el
protocolo
médico del
período
establecía
que requería
más tiempo
de

Taxonomía General de Aplicaciones
Nodo del
Función
grafo de la INCF típico S típico
causal
lesión
recuperación
.
Atleta que El atleta que Bajo [0.05– Muy alta [0.80–
produjo la lesión produjo la 0.20] cuando la 0.95] cuando la
(el jugador que lesión por acción era legal. acción era legal:
golpeó o la una acción cualquier atleta
conducta que dentro de las de ese deporte
causó la lesión) reglas del habría
juego tiene producido el
INCF bajo o mismo tipo de
nulo sobre la acción en el
lesión mismo
cuando la contexto.
acción era
legal dentro
del deporte.
El INCF del
atleta es
positivo
cuando la
acción era
ilegal según
las reglas
vigentes.
§4 Caso resuelto — CTE y la NFL: el INCF
del diseñador de las reglas
La encefalopatía traumática crónica (CTE) es una enfermedad
neurodegenerativa asociada a la exposición repetida a
traumatismos craneoencefálicos leves. La investigación
publicada en 2005 por el Dr. Bennet Omalu identificó CTE
en el cerebro de Mike Webster, jugador de la NFL. Estudios
posteriores del Boston University CTE Center encontraron
CTE en el 99% de los cerebros de ex jugadores de la NFL
donados para investigación. La NFL tuvo acceso a evidencia
creciente del riesgo entre 2002 y 2013 pero no modificó

Taxonomía General de Aplicaciones
sustancialmente las reglas del juego ni comunicó el riesgo a los
jugadores hasta las demandas colectivas de más de 5,000 ex
jugadores.
Nodo Actor INCF S Análisis
N1 NFL como ~38% 0.30 INCF muy alto. S
diseñadora de las moderado-bajo: la
reglas (no decisión de no
modificó la modificar las reglas
mecánica del cuando la evidencia
juego con médica era disponible
información era idiosincrática de la
disponible sobre NFL del período —
el riesgo de CTE) otras ligas (rugby,
fútbol australiano)
implementaron
modificaciones de
reglas orientadas a
reducir los impactos
craneoencefálicos
antes de que la NFL lo
hiciera.
N2 Sistema médico ~25% 0.32 El Comité de
de la NFL Concusiones de la
(negación activa NFL publicó estudios
de la evidencia que cuestionaban la
científica) investigación del Dr.
Omalu y afirmaban
que la NFL no tenía
evidencia de CTE en
jugadores activos. La
negación activa retrasó
la modificación de las
reglas. S moderado-
bajo: la negación activa
era idiosincrática del
sistema médico de la
NFL.
N3 Mecánica del ~18% 0.85 S muy alta: la
juego americano naturaleza de contacto
(la naturaleza de del fútbol americano es
contacto del condición estructural
deporte) del deporte, no una

Taxonomía General de Aplicaciones
Nodo Actor INCF S Análisis
decisión de ningún
actor específico.
N4 Clubs ~12% 0.55 Los clubs tenían
individuales incentivos para hacer
(sobreexplotación regresar a los jugadores
de jugadores con al juego antes de que
lesiones previas los protocolos de
conocidas) gestión de
conmociones lo
permitieran. S
moderada.
N5 Jugadores que ~5% 0.92 Las acciones que
produjeron los produjeron los
impactos impactos eran legales
dentro del reglamento
de la NFL. S casi
máxima: cualquier
jugador de ese deporte
habría producido las
mismas acciones.
N6 Diseñadores del ~2% 0.72 El diseño del casco no
equipamiento había optimizado la
protector (casco) protección contra los
traumatismos de baja
velocidad y alta
frecuencia. S
moderada-alta.
El acuerdo de 2013 entre la NFL y los 5,000 ex jugadores:
765M USD, que el análisis del INCF establece como
significativamente inferior al D_vital total de los afectados.
D_vital estimado por jugador con CTE diagnosticada:
ΔT_trayectoria de 10–25 años de vida en calidad reducida
(deterioro cognitivo progresivo, síntomas psiquiátricos
documentados, incapacidad funcional) + T_impedido de la
actividad profesional y personal durante el declive. El
AD_NFL sobre el D_vital colectivo era sustancialmente
mayor que los 765M acordados.

Taxonomía General de Aplicaciones
§5 El IAS_seguridad deportiva: las reformas
que actúan sobre los nodos de mayor INCF
El IAS_seguridad deportiva mide en qué medida las reformas
de las reglas y los protocolos de seguridad incorporaron las
lecciones de los casos documentados. Las reformas que actúan
sobre los jugadores que producen los impactos (sanciones más
severas por tacleadas ilegales) sin modificar la mecánica
fundamental del juego tienen IAS próximo a cero: actúan
sobre el nodo de menor INCF. Las reformas que modifican la
mecánica del juego para reducir los impactos de alta velocidad
(los cambios de reglas del rugby sobre los tacleadas a la cabeza,
el protocolo de conmoción con sustitución temporal
obligatoria) actúan sobre el nodo de mayor INCF.
Tipo de
reforma de
IAS típico Por qué funciona o no
seguridad
deportiva
Modificación IAS positivo [0.30– Actúa sobre el nodo de mayor
de las reglas 0.60] cuando las INCF — el diseño de las reglas
que reducen modificaciones que permite o requiere el tipo de
el contacto reducen la tasa de contacto que produce la lesión.
de alta conmociones La eficacia se verifica con la tasa
velocidad documentada en de lesiones post-reforma.
(penalización las temporadas
de tacleadas a siguientes.
la cabeza,
modificación
de la altura de
los placajes,
eliminación
de scrums sin
contestación
en rugby)
Protocolo de IAS positivo [0.25– Actúa sobre el nodo de gestión
conmoción 0.50] cuando el médica de las lesiones — el club
con protocolo se que vuelve al jugador al juego
sustitución implementa con antes de que el protocolo lo

Taxonomía General de Aplicaciones
Tipo de
reforma de
IAS típico Por qué funciona o no
seguridad
deportiva
temporal rigor y el personal permita. La eficacia depende de
obligatoria médico tiene la independencia del médico
(cuando el autoridad efectiva respecto al incentivo del club de
árbitro puede sobre el regreso al contar con el jugador.
detener el juego.
juego para
evaluación
médica)
Sanciones IAS muy bajo Actúa sobre el nodo de menor
más severas a [0.02–0.10] cuando INCF — el jugador individual
jugadores por las acciones que cuya acción legal dentro de las
acciones producen más reglas produce la lesión. No
ilegales que lesiones son legales cambia la mecánica del juego
producen según las reglas del que hace esa acción racional.
lesiones juego.
Mejoras del IAS moderado Actúa sobre la gravedad del
equipamiento [0.15–0.35] cuando daño cuando el impacto ocurre,
protector las mejoras del pero no sobre la probabilidad
(diseño de equipamiento del impacto. Las mejoras del
cascos, reducen la casco pueden producir el efecto
protecciones) severidad del daño paradójico de que los jugadores
por impacto pero tacleen con más intensidad
no la frecuencia. porque se sienten más
protegidos.
§6 Preguntas que responde este capítulo
Pregunta Instrumento Nivel de certeza
¿El diseñador Análisis del estado de la Declaración A con
de las reglas evidencia médica sobre el Dep1 (análisis
tenía tipo de lesión en el período biomecánico +
información del previo a la lesión analizada: documentación del
riesgo — cuál ¿el estándar médico del conocimiento del
es su INCF? período establecía el riesgo riesgo). Declaración B
y la necesidad de reforma? con Dep2/Dep3.

Taxonomía General de Aplicaciones
Pregunta Instrumento Nivel de certeza
¿El organismo tenía acceso
a esa evidencia?
¿El club Análisis de la carga de Declaración B con
sobreexplotó al entrenamiento y análisis del historial de
atleta — cuál es competición del atleta en el partidos y
el INCF del período previo a la lesión: entrenamientos del
club? ¿excedía los límites de atleta + estándar de la
recuperación que el medicina deportiva
estándar de medicina del período.
deportiva del período
establecía?
¿Cuál es el D_vital = T_invertido + Declaración B con
D_vital del T_impedido + análisis médico Dep2
atleta lesionado ΔT_trayectoria. El del impacto de la
— incluyendo ΔT_trayectoria es la brecha lesión sobre la
el entre la trayectoria trayectoria
ΔT_trayectoria? deportiva y personal que el profesional.
atleta habría tenido sin la Declaración C para el
lesión y la trayectoria real. ΔT_trayectoria de las
lesiones neurológicas
acumulativas.
¿El IAS de las IAS_seguridad = J_post − Declaración B con
reformas fue J_pre. Análisis de la tasa de datos
positivo — lesiones antes y después de epidemiológicos
actuaron sobre las reformas, distinguiendo Dep3 de la tasa de
los nodos de si las reformas actuaron lesiones antes y
mayor INCF? sobre la mecánica del juego después de las
(nodo de mayor INCF) o reformas.
sobre los jugadores
individuales (nodo de
menor INCF).
— Fin del Capítulo 58 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

