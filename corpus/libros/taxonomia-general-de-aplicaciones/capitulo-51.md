PARTE VII · Ingeniería y Tecnología

## Capítulo 51

### Transporte — accidentes, responsabilidad de sistemas y regulación

Organ.  Estru.  Model.  Educa.  Crisi.

Nivel B — aplica el cap. 12 al dominio del transporte: accidentes aéreos, ferroviarios, marítimos y terrestres. El instrumento central es el INCF en los nodos de decisión críticos del sistema de transporte, con énfasis en la distinción entre el error humano del operador (S alto — cualquier operador bajo las mismas condiciones habría producido el mismo resultado) y la decisión del diseñador del sistema que hizo que ese error fuera posible a esa escala (S moderado-bajo).

Si tu caso es de accidente por error del piloto / operador, ve a §3 caso A. Si es de accidente por diseño deficiente del sistema, ve a §3 caso B (isomorfismo con el Boeing 737 MAX del cap. 12).

### §1  Descripción del subcampo

El análisis de accidentes de transporte reproduce exactamente el patrón del cap. 12 (Challenger / Boeing 737 MAX) en el dominio del transporte. La narrativa espontánea del accidente identifica el error del operador — el piloto que entró en la configuración incorrecta, el maquinista que pasó la señal en rojo, el conductor que no detectó el peatón. El análisis causal pregunta: ¿el sistema estaba diseñado para que ese error fuera posible a esa escala? El nodo de diseño del sistema — el fabricante que no implementó la protección de vuelo completa, el operador ferroviario que no instaló el sistema de protección automática, el regulador que no requirió la

Taxonomía General de Aplicaciones

### tecnología disponible — es frecuentemente el de mayor INCF.

### §2  Escala de evidencia Cd0–Cd8 en accidentes de transporte

Nivel Tipo de evidencia Descripción Rango

w

Cd1 Informe de la agencia de seguridad + CVR + FDR + análisis de trayectoria verificado

El informe del NTSB, el BEA, o la autoridad equivalente con acceso al registrador de voz de cabina (CVR), el registrador de datos de vuelo (FDR), y el análisis de la trayectoria desde los datos de radar y los sensores del sistema.

[0.72, 0.90]

Cd2 Análisis pericial independiente del sistema con acceso a los datos del accidente

El análisis de un perito en seguridad del modo de transporte específico con acceso a los datos primarios del accidente.

[0.60, 0.78]

Cd3 Informes convergentes de múltiples autoridades de seguridad sobre el mismo accidente

Cuando dos o más agencias nacionales de seguridad convergieron en el análisis del mismo accidente desde perspectivas distintas.

[0.50, 0.68]

Cd4 Informes del operador + registros de mantenimiento + datos de los sistemas de la aeronave / vehículo

Los registros del operador sobre el mantenimiento, la formación de la tripulación, y los datos de los sistemas de la aeronave o el vehículo sin el análisis forense independiente.

[0.38, 0.56]

Cd0 Análisis Cd1 que establece

El informe de la agencia de seguridad que establece que el

w = 0.00

Taxonomía General de Aplicaciones

Nivel Tipo de evidencia Descripción Rango

w

que el accidente fue consecuencia de un evento no previsible dado el diseño correcto

accidente fue producido por una combinación de factores fuera del espectro de diseño requerido.

### §3  Casos resueltos

Caso A — Air France 447 (1 de junio de 2009): S alto de la tripulación, INCF del sistema de enseñanza

El vuelo AF447 de Air France se precipitó al Atlántico Sur el 1 de junio de 2009, matando a los 228 ocupantes. El informe del BEA estableció que la tripulación reaccionó al bloqueo temporal de los tubos de Pitot (que producía lecturas de velocidad inconsistentes) tirando del joystick hacia atrás — manteniendo la aeronave en una actitud de morro alto que producía la pérdida de sustentación — durante casi cuatro minutos, a pesar de múltiples indicaciones de alarma de pérdida.

Nodo Actor/Factor INCF S Análisis

N1 Sistema de formación y los procedimientos de recuperación de pérdida en alta altitud

~35% 0.42 S moderado-bajo: el sistema de formación de Air France del período no incluía el entrenamiento completo de recuperación de pérdida en alta altitud con el avión real. Otros programas de formación del período sí lo incluían.

N2 Diseño de la alternancia del

~25% 0.55 El sistema de protección de vuelo del A330 se

Taxonomía General de Aplicaciones

Nodo Actor/Factor INCF S Análisis

control entre piloto automático y control manual

desconecta cuando los datos de velocidad son inconsistentes, transfiriendo el control manual sin el feedback táctil que en modo normal comunica el estado de la aeronave a la tripulación.

N3 Tripulación (mantuvo la actitud de morro alto durante 4 minutos)

~18% 0.72 S moderada-alta: la conducta de la tripulación en condiciones de alta desorientación espacial sin formación específica de recuperación de pérdida era la respuesta que la formación del período producía.

N4 Air France como operadora (estándares de formación)

~15% 0.60 Los estándares de formación de Air France del período para situaciones de baja velocidad en alta altitud eran inferiores a los mejores de la industria.

N5 Proveedores de los tubos de Pitot (susceptibilidad al hielo)

~7% 0.70 Los tubos de Pitot tenían una susceptibilidad conocida al hielo en condiciones de tormenta en el trópico. Un modelo de sustitución mejorado estaba disponible.

Caso B — Siniestros ferroviarios por ausencia de ATP (Automatic Train Protection)

Múltiples siniestros ferroviarios graves en sistemas que carecían del sistema de Protección Automática de Trenes (ATP / ERTMS) — que frena automáticamente el tren cuando pasa una señal en rojo o excede la velocidad permitida

Taxonomía General de Aplicaciones

— ilustran el patrón más directo del dominio del transporte: la tecnología que habría prevenido el siniestro existía y estaba disponible, pero el operador ferroviario y el regulador no la habían implementado.

Sub-variante

INCF del nodo de decisión

crítico S del nodo

de siniestro

sin ATP

Siniestro por paso de señal en rojo (SPAD)

Operador ferroviario que no implementó ATP cuando el costo y la tecnología eran accesibles: INCF alto. Regulador que no exigió ATP como requisito: INCF moderado.

Moderada [0.38–0.58] para el operador (otros del mismo período sin ATP habrían producido el mismo resultado). Moderado-alta [0.55–0.72] para el regulador.

Siniestro por exceso de velocidad en curva

Diseñador de la infraestructura que no requirió ATP como requisito de seguridad para tramos de alta velocidad con curvas críticas: INCF alto. Regulador de certificación: INCF moderado.

Moderada-baja [0.30– 0.50] cuando el diseño sin ATP era idiosincrático respecto a los estándares europeos disponibles.

### §4  Preguntas que responde este capítulo

Pregunta Instrumento Nivel de certeza

¿El accidente fue por error del operador (S alto) o por diseño del sistema (INCF alto)?

Análisis del grafo con INCF por nodo: ¿sin el error del operador habría ocurrido el accidente? ¿El sistema estaba diseñado para que ese error fuera catastrófico?

Declaración A con informe Cd1 de la agencia de seguridad.

Taxonomía General de Aplicaciones

Pregunta Instrumento Nivel de certeza

¿La tecnología preventiva existía y estaba disponible — cuál es el INCF del no-adoptante?

Análisis del estado del arte de la tecnología de seguridad del período para el tipo de vehículo y operación.

Declaración B con Cd3/Cd4 del estándar técnico del período.

— Fin del Capítulo 51 —

Centro Multidisciplinario Meriadock Formación y Asesoría A.C. · 2026

Taxonomía General de Aplicaciones

