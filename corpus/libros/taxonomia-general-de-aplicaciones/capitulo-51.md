## PARTE VII · Ingeniería y Tecnología

### Capítulo 51
Transporte — accidentes,
responsabilidad de sistemas y regulación
Organ. Estru. Model. Educa. Crisi.
Nivel B — aplica el cap. 12 al dominio del transporte: accidentes aéreos,
ferroviarios, marítimos y terrestres. El instrumento central es el INCF
en los nodos de decisión críticos del sistema de transporte, con énfasis en
la distinción entre el error humano del operador (S alto — cualquier
operador bajo las mismas condiciones habría producido el mismo
resultado) y la decisión del diseñador del sistema que hizo que ese error
fuera posible a esa escala (S moderado-bajo).
Si tu caso es de accidente por error del piloto / operador, ve a §3 caso
A. Si es de accidente por diseño deficiente del sistema, ve a §3 caso B
(isomorfismo con el Boeing 737 MAX del cap. 12).
§1 Descripción del subcampo
El análisis de accidentes de transporte reproduce exactamente
el patrón del cap. 12 (Challenger / Boeing 737 MAX) en el
dominio del transporte. La narrativa espontánea del accidente
identifica el error del operador — el piloto que entró en la
configuración incorrecta, el maquinista que pasó la señal en
rojo, el conductor que no detectó el peatón. El análisis causal
pregunta: ¿el sistema estaba diseñado para que ese error fuera
posible a esa escala? El nodo de diseño del sistema — el
fabricante que no implementó la protección de vuelo
completa, el operador ferroviario que no instaló el sistema de
protección automática, el regulador que no requirió la

Taxonomía General de Aplicaciones
tecnología disponible — es frecuentemente el de mayor
INCF.
§2 Escala de evidencia Cd0–Cd8 en accidentes
de transporte
Tipo de Rango
Nivel Descripción
evidencia w
Cd1 Informe de la El informe del NTSB, el BEA, o [0.72,
agencia de la autoridad equivalente con 0.90]
seguridad + acceso al registrador de voz de
CVR + FDR + cabina (CVR), el registrador de
análisis de datos de vuelo (FDR), y el
trayectoria análisis de la trayectoria desde los
verificado datos de radar y los sensores del
sistema.
Cd2 Análisis El análisis de un perito en [0.60,
pericial seguridad del modo de transporte 0.78]
independiente específico con acceso a los datos
del sistema con primarios del accidente.
acceso a los
datos del
accidente
Cd3 Informes Cuando dos o más agencias [0.50,
convergentes nacionales de seguridad 0.68]
de múltiples convergieron en el análisis del
autoridades de mismo accidente desde
seguridad perspectivas distintas.
sobre el mismo
accidente
Cd4 Informes del Los registros del operador sobre [0.38,
operador + el mantenimiento, la formación 0.56]
registros de de la tripulación, y los datos de
mantenimiento los sistemas de la aeronave o el
+ datos de los vehículo sin el análisis forense
sistemas de la independiente.
aeronave /
vehículo
Cd0 Análisis Cd1 El informe de la agencia de w =
que establece seguridad que establece que el 0.00

Taxonomía General de Aplicaciones
Tipo de Rango
Nivel Descripción
evidencia w
que el accidente fue producido por una
accidente fue combinación de factores fuera
consecuencia del espectro de diseño requerido.
de un evento
no previsible
dado el diseño
correcto
§3 Casos resueltos
Caso A — Air France 447 (1 de junio de 2009): S alto de la
tripulación, INCF del sistema de enseñanza
El vuelo AF447 de Air France se precipitó al Atlántico Sur el
1 de junio de 2009, matando a los 228 ocupantes. El informe
del BEA estableció que la tripulación reaccionó al bloqueo
temporal de los tubos de Pitot (que producía lecturas de
velocidad inconsistentes) tirando del joystick hacia atrás —
manteniendo la aeronave en una actitud de morro alto que
producía la pérdida de sustentación — durante casi cuatro
minutos, a pesar de múltiples indicaciones de alarma de
pérdida.
Nodo Actor/Factor INCF S Análisis
N1 Sistema de ~35% 0.42 S moderado-bajo: el
formación y los sistema de formación de
procedimientos Air France del período no
de incluía el entrenamiento
recuperación completo de
de pérdida en recuperación de pérdida
alta altitud en alta altitud con el
avión real. Otros
programas de formación
del período sí lo incluían.
N2 Diseño de la ~25% 0.55 El sistema de protección
alternancia del de vuelo del A330 se

Taxonomía General de Aplicaciones
Nodo Actor/Factor INCF S Análisis
control entre desconecta cuando los
piloto datos de velocidad son
automático y inconsistentes,
control manual transfiriendo el control
manual sin el feedback
táctil que en modo
normal comunica el
estado de la aeronave a la
tripulación.
N3 Tripulación ~18% 0.72 S moderada-alta: la
(mantuvo la conducta de la tripulación
actitud de en condiciones de alta
morro alto desorientación espacial
durante 4 sin formación específica
minutos) de recuperación de
pérdida era la respuesta
que la formación del
período producía.
N4 Air France ~15% 0.60 Los estándares de
como formación de Air France
operadora del período para
(estándares de situaciones de baja
formación) velocidad en alta altitud
eran inferiores a los
mejores de la industria.
N5 Proveedores de ~7% 0.70 Los tubos de Pitot tenían
los tubos de una susceptibilidad
Pitot conocida al hielo en
(susceptibilidad condiciones de tormenta
al hielo) en el trópico. Un modelo
de sustitución mejorado
estaba disponible.
Caso B — Siniestros ferroviarios por ausencia de ATP
(Automatic Train Protection)
Múltiples siniestros ferroviarios graves en sistemas que
carecían del sistema de Protección Automática de Trenes
(ATP / ERTMS) — que frena automáticamente el tren
cuando pasa una señal en rojo o excede la velocidad permitida

Taxonomía General de Aplicaciones
— ilustran el patrón más directo del dominio del transporte:
la tecnología que habría prevenido el siniestro existía y estaba
disponible, pero el operador ferroviario y el regulador no la
habían implementado.
Sub-
variante
INCF del nodo de decisión
de S del nodo
crítico
siniestro
sin ATP
Siniestro Operador ferroviario que no Moderada [0.38–0.58]
por paso implementó ATP cuando el para el operador (otros
de señal en costo y la tecnología eran del mismo período sin
rojo accesibles: INCF alto. ATP habrían
(SPAD) Regulador que no exigió ATP producido el mismo
como requisito: INCF resultado). Moderado-
moderado. alta [0.55–0.72] para el
regulador.
Siniestro Diseñador de la Moderada-baja [0.30–
por exceso infraestructura que no requirió 0.50] cuando el diseño
de ATP como requisito de sin ATP era
velocidad seguridad para tramos de alta idiosincrático respecto
en curva velocidad con curvas críticas: a los estándares
INCF alto. Regulador de europeos disponibles.
certificación: INCF
moderado.
§4 Preguntas que responde este capítulo
Pregunta Instrumento Nivel de certeza
¿El accidente Análisis del grafo con Declaración A con
fue por error INCF por nodo: ¿sin el informe Cd1 de la
del operador (S error del operador habría agencia de seguridad.
alto) o por ocurrido el accidente? ¿El
diseño del sistema estaba diseñado
sistema (INCF para que ese error fuera
alto)? catastrófico?

Taxonomía General de Aplicaciones
Pregunta Instrumento Nivel de certeza
¿La tecnología Análisis del estado del arte Declaración B con
preventiva de la tecnología de Cd3/Cd4 del estándar
existía y estaba seguridad del período para técnico del período.
disponible — el tipo de vehículo y
cuál es el INCF operación.
del no-
adoptante?
— Fin del Capítulo 51 —
Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

