# Capítulo 12
## Ingeniería de sistemas y confiabilidad

*El índice de necesidad causal del fallo: cuando la junta teórica no era el problema*

---

### §1.  El problema

El 28 de enero de 1986 a las 11:38 de la mañana, el transbordador espacial Challenger se desintegró setenta y tres segundos después del despegue. Los siete tripulantes murieron. La causa técnica inmediata fue el fallo de una junta teórica —un anillo de goma de unos centímetros— en el cohete propulsor sólido derecho. La junta perdió su sellado en las condiciones de frío extremo de esa mañana en Cabo Cañaveral (la temperatura en el momento del lanzamiento era de 36°F, muy por debajo del mínimo para el que la junta había sido diseñada y probada).

La noche anterior al lanzamiento, los ingenieros de Morton Thiokol —el fabricante de los propulsores— habían realizado una teleconferencia urgente con la NASA. Roger Boisjoly y Arnie Thompson, los dos ingenieros que mejor conocían el comportamiento de las juntas teóricas, presentaron datos inequívocos: el desempeño de las juntas se degradaba con el frío, y las temperaturas previstas para el lanzamiento de la mañana siguiente estaban muy por fuera


confiabilidad

del rango de datos documentados. Boisjoly recomendó explícitamente no lanzar. Su recomendación fue anulada.

El Informe de la Comisión Rogers (1986) identificó como causa del accidente el fallo de la junta teórica y la falta de comunicación de la información de riesgo a los decisores del lanzamiento. Treinta y dos años después, en octubre de 2018, el vuelo JT610 de Lion Air se precipitó al mar trece minutos después del despegue. En marzo de 2019, el vuelo ET302 de Ethiopian Airlines se precipitó seis minutos después del despegue. Los dos aviones eran Boeing 737 MAX 8. Trescientas cuarenta y seis personas murieron. La causa técnica en ambos casos fue el sistema MCAS — Maneuvering Characteristics Augmentation System— que empujó el morro del avión hacia abajo en respuesta a lecturas erróneas de un sensor defectuoso, sin que los pilotos tuvieran el entrenamiento ni los instrumentos necesarios para comprender lo que estaba ocurriendo y contrarrestarlo.

El sistema no aprendió. En 1986, los ingenieros que sabían advirtieron y fueron ignorados. En 2018, los ingenieros que diseñaron el MCAS lo hicieron sin que la documentación técnica para pilotos mencionara su existencia, porque su clasificación de riesgo había sido rebajada deliberadamente para evitar que se requiriera un programa de entrenamiento adicional —lo que habría encarecido el avión y hecho perder el contrato con American Airlines frente al Airbus A320neo. El patrón estructural es el mismo: la presión del sistema sobre los nodos de decisión humana produjo el fallo que esa presión era condición necesaria de producir.

#### 1.1 La diferencia entre el fallo técnico y el fallo causal

La ingeniería de confiabilidad convencional analiza los fallos técnicos: qué parte falló, por qué razón física, bajo


confiabilidad

qué condiciones. El árbol de fallos (Fault Tree Analysis, FTA) y el análisis de modos y efectos de fallo (FMEA) son los instrumentos estándar. Ambos producen distribuciones de probabilidad sobre los componentes físicos del sistema.

El cálculo de la responsabilidad añade una capa que el FTA y el FMEA no pueden capturar: el índice de necesidad causal del fallo (INCF), que pregunta no "¿qué parte falló?" sino "¿sin qué actor o condición del sistema el fallo no habría alcanzado esta escala?". Esa pregunta tiene respuestas que apuntan frecuentemente a nodos organizacionales, regulatorios y políticos, no a componentes físicos.

Índice de necesidad causal del fallo (INCF = R*):  La fracción del fallo sistémico causalmente atribuible a cada nodo del sistema: el componente técnico, el operador, el diseñador, el sistema de certificación, la presión organizacional. INCF alto de un nodo significa que sin ese nodo (en esa condición) el fallo no habría alcanzado esa escala. Es el instrumento que convierte el análisis forense de accidentes en análisis de responsabilidad distribuida.

#### 1.2 Por qué los hijos aplican solo a los operadores

En el dominio de la ingeniería de sistemas, los hijos de Afrodita aplican exclusivamente a los operadores: las personas que tomaron decisiones en los nodos críticos del sistema donde una decisión diferente habría cambiado el resultado. No aplican a los componentes físicos (la junta teórica, el sensor MCAS) que no tienen voluntad, ni a las organizaciones como entidades abstractas —cuyo análisis de ego colectivo pertenece al Capítulo 11.

La razón de esta restricción es la misma que en los dominios anteriores: los hijos describen la posición de la voluntad de un sujeto en el momento de un acto. En el Challenger, los


confiabilidad

operadores relevantes son el equipo de dirección de la NASA que tomó la decisión de lanzar y los directivos de Morton Thiokol que anularon la recomendación de sus ingenieros. En el 737 MAX, son los directivos de Boeing que rebajaron la clasificación de riesgo del MCAS y los supervisores de la FAA que aceptaron la delegación de la certificación. Sus hijos en esos momentos describen desde qué disposición actuaron —y esa descripción tiene consecuencias directas para la evaluación de la culpabilidad y para el diseño de los mecanismos de prevención.

#### 1.3 El patrón estructural que se repite

La comparación entre el Challenger y el 737 MAX no es solo histórica: es la demostración más poderosa del capítulo. Treinta y dos años separan los dos accidentes. En ambos casos, la estructura del grafo causal es casi idéntica:

Challenger 1986 Boeing 737 MAX 2018-19

Elemento estructural

Componente técnico fallido

Junta teórica O-ring: diseñada para temperaturas > 53°F, lanzada a 36°F.

Sensor AoA defectuoso + MCAS sin redundancia en el sensor input, sin indicador en cabina estándar.

Ingenieros que advirtieron

Boisjoly y Thompson (Morton Thiokol): datos claros, recomendación explícita de no lanzar.

Ingenieros internos de Boeing que señalaron problemas con la clasificación de riesgo del MCAS. Algunos documentos post-accidente los muestran preocupados.

Mecanismo de anulación

Directivos de Morton Thiokol

Reclasificación del MCAS de riesgo


confiabilidad

"poniéndose el sombrero de gestión" para anular la recomendación de ingeniería.

"catastrófico" a "hazardous" para evitar el requisito de entrenamiento adicional.

Presión del sistema

Presión política del lanzamiento (Reagan lo mencionaría en el discurso del Estado de la Unión esa noche).

Presión comercial: el 737 MAX debía ser más barato que el A320neo para no requerir entrenamiento diferencial con el 737 NG.

Fallo del sistema de certificación

La NASA aceptó la decisión de lanzar sin documentar formalmente las objeciones de los ingenieros.

La FAA delegó la certificación del MCAS a Boeing con supervisión insuficiente. Aprobó el avión sin entender completamente el sistema.

R* del componente físico

~18% (la junta teórica fallida era condición técnica pero no suficiente sin las otras condiciones del sistema).

~15% (el sensor defectuoso era condición técnica pero el MCAS sin redundancia ni transparencia era la condición sistémica).

R* de los nodos organizacionales

~82% distribuido entre NASA, Morton Thiokol dirección, y el sistema de decisión de lanzamiento.

~85% distribuido entre Boeing dirección, FAA, y el sistema de certificación delegada.

Principio de ingeniería:  El patrón estructural que se repite en ambos casos es el isomorfismo más importante del capítulo: en ambos, el componente físico que "causó" el accidente según el análisis convencional tiene un INCF inferior al 20%. El 80% restante está en los nodos organizacionales que crearon las condiciones bajo las cuales ese componente físico era


confiabilidad

condición necesaria del fallo a esa escala. El sistema no aprendió porque el análisis forense del Challenger identificó la junta teórica como causa y el sistema de decisión como contexto. El cálculo causal invierte esas etiquetas.


confiabilidad

### §2.  Página puente — Traducción al lenguaje de la ingeniería de sistemas

Esta página resume las herramientas del sistema en el contexto de la ingeniería de sistemas y la confiabilidad. El lector con formación en ingeniería, gestión de seguridad operacional o análisis de accidentes puede comenzar aquí.

Herramienta En ingeniería de sistemas se llama

Qué significa

Grafo causal G

Red causal del fallo sistémico

El mapa de todos los nodos que contribuyeron causalmente al fallo: el componente técnico, el operador, el diseñador, el sistema de certificación, la presión organizacional y política. Es el árbol de fallos expandido para incluir nodos organizacionales.

R* (vector) INCF — Índice de Necesidad Causal del Fallo

La fracción del fallo causalmente atribuible a cada nodo. INCF alto del componente físico: el fallo era principalmente técnico. INCF alto de los nodos organizacionales: el fallo era principalmente de diseño del sistema sociotécnico.

Nodo de diseño

Diseñador del sistema / arquitecto de las

El nodo que diseñó las condiciones bajo las cuales el componente físico era condición necesaria del fallo: los directivos que fijaron las


confiabilidad

condiciones del fallo

restricciones de certificación, los que aprobaron el diseño con las tolerancias inadecuadas.

Nodo de presión

Fuente de la presión que anuló la señal de advertencia

En accidentes de ingeniería, hay siempre un nodo que generó la presión (temporal, económica, política) que hizo que las advertencias técnicas fueran ignoradas. Ese nodo tiene INCF positivo real aunque no haya diseñado el sistema.

Operador Nodo humano con decisión en el punto crítico

La persona que tomó la decisión de lanzar, de certificar, de no reportar. Sus hijos describen desde qué disposición actuó. S mide si esa decisión era idiosincrática o sistémica.

S del operador

Fungibilidad del operador en la decisión

S alto: cualquier persona en esa posición, bajo la misma presión del sistema, habría tomado la misma decisión. El problema es sistémico, no personal. S bajo: la decisión dependía de las características idiosincráticas de ese operador.

α del operador

Grado de contención del riesgo ejercido

Lo que el operador hizo para reducir el riesgo: protestó formalmente, documentó su disidencia, detuvo el proceso, escaló a niveles superiores. α = 0: no hizo nada para contener. α = 1: ejerció todas las acciones de contención a su alcance.

Δ del operador

Déficit de contención

La brecha entre el peso causal del operador en el fallo y su ejercicio de contención. Δ El Cálculo de la Responsabilidad · Cap. 12 — Ingeniería de sistemas y

confiabilidad

proporcional al INCF

positivo alto: tenía poder de intervención y no lo usó. Δ negativo: ejerció más contención de la que su posición requería (los ingenieros que protestaron tenían Δ negativo).

D_total Daño del fallo sistémico

T_invertido (vidas perdidas, activos destruidos), T_impedido (programas interrumpidos, proyectos cancelados), ΔT_trayectoria (pérdida permanente de confianza en el sistema, desvíos de recursos hacia investigación y litigios).

Fobos: miedo a las consecuencias de detener el proceso (la carrera, la relación con el cliente). Potós: persistencia en el procedimiento establecido sin cuestionar. Anteros: afirmación deliberada de la decisión a pesar del riesgo conocido. Harmonía: el operador que protesta formalmente actúa desde Anteros + Harmonía.

Hijos del operador

Disposición de la voluntad en el momento de la decisión crítica

Para el lector que viene del núcleo universal:  Este dominio tiene dos características singulares. Primera: el componente físico (la junta teórica, el sensor MCAS) es un nodo causal real, pero sin voluntad — su INCF apunta hacia quienes lo diseñaron y certificaron. Segunda: los hijos aplican solo a los operadores humanos en los puntos críticos de decisión, no a la organización como entidad abstracta.


confiabilidad

### §3.  Las herramientas en el contexto de la ingeniería de sistemas

#### 3.1 El grafo causal del fallo sistémico: del árbol de fallos al grafo de responsabilidad

El árbol de fallos (FTA) convencional mide la probabilidad de fallo como función de las probabilidades de fallo de los componentes. Es un instrumento hacia abajo: parte del evento de nivel superior (el accidente) y desciende hacia los componentes físicos. El grafo causal del fallo sistémico es un instrumento hacia arriba y hacia los lados: parte del mismo evento de nivel superior y expande el análisis para incluir los nodos organizacionales, regulatorios y políticos que determinaron las condiciones bajo las cuales el fallo técnico fue posible.

Tipo Función causal en el fallo

Nivel del nodo

Ejemplo (Challenger)

Físico Componente técnico que falló.

El modo de fallo directo. INCF típicamente bajo-moderado porque sin las condiciones sistémicas no habría fallado en ese momento.

Junta teórica O-ring: falló a 36°F porque N2 fijó ese día de lanzamiento.


confiabilidad

Diseño técnico El diseño del componente y sus tolerancias.

Si el componente fue diseñado sin margen suficiente para las condiciones de operación real, el diseño tiene INCF positivo.

Morton Thiokol diseñó la junta con tolerancias que no cubrían temperaturas < 53°F.

Operativo El operador que tomó la decisión crítica.

La persona con poder de detener el proceso y no lo detuvo, o que tomó la decisión bajo la presión del sistema.

Nivel de gestión NASA y dirección MT que aprobó el lanzamiento.

Organizacional La cultura y los procesos de la organización.

Los protocolos de toma de decisión, la estructura de incentivos, los mecanismos de escalamiento de señales de riesgo.

NASA: proceso de decisión de lanzamiento que separaba la voz de los ingenieros de la voz de la gestión.

Sistémico / político

Las presiones externas que actuaron sobre el sistema.

Plazos, presión económica, presión política, compromisos con clientes. Estas presiones modifican el valor de

Presión para lanzar antes del discurso del Estado de la Unión de Reagan.


confiabilidad

umbral θ de los operadores.

#### 3.2 INCF y la regla de los nodos de decisión críticos

En los sistemas de ingeniería complejos, hay siempre uno o más nodos de decisión críticos: momentos donde una decisión diferente habría cambiado el resultado con alta probabilidad. Esos nodos tienen el mayor INCF relativo del grafo porque su S es moderado-bajo: en ellos, las características del operador —su umbral de Fobos, su disposición de Harmonía, su conocimiento técnico del riesgo— son condición determinante del resultado.

La regla de los nodos de decisión críticos: el nodo de mayor INCF en un accidente de ingeniería es raramente el componente físico que falló. Es típicamente el nodo organizacional que tomó la decisión de operar bajo condiciones para las cuales el sistema no estaba certificado, o que diseñó el sistema sin los márgenes de seguridad que los datos disponibles recomendaban.

INCF_nodo_decisión >> INCF_componente_físico

en la mayoría de los accidentes

Esta afirmación puede verificarse empíricamente: los estudios de accidentes de aviación, ingeniería nuclear y transporte marítimo muestran consistentemente que el componente físico que inicia la cadena de fallo tiene un INCF inferior al 25% cuando se incluyen los nodos organizacionales en el grafo. El 75% restante está en los factores humanos, organizacionales y regulatorios.


confiabilidad

#### 3.3 El índice de sustituibilidad S del operador en decisiones de seguridad

En el dominio de la ingeniería de seguridad, S del operador es el predictor más importante de si la reforma debe ser individual (sustituir al operador que tomó la decisión errónea) o sistémica (cambiar el sistema que hizo que esa decisión fuera racional dado los incentivos).

- S alto del operador: cualquier persona en esa posición, bajo la misma estructura de incentivos y presiones, habría tomado la misma decisión. La reforma sistémica es la única efectiva. Sustituir al operador produce el mismo resultado con nombres diferentes.
- S bajo del operador: la decisión dependía de características idiosincráticas del operador —su tolerancia al riesgo, su conocimiento técnico específico, su disposición a enfrentar la presión institucional. La reforma puede incluir criterios de selección y formación de operadores para ese nodo.


En el Challenger, S de los directivos de Morton Thiokol que anularon la recomendación de Boisjoly es alto (0.78): cualquier directivo bajo la misma presión de la NASA y con la misma estructura de incentivos de contrato habría "puesto el sombrero de gestión" de la misma manera. La reforma que siguió al Challenger —cambiar los protocolos de decisión de lanzamiento— fue correcta precisamente porque atacó el factor sistémico (S alto) en lugar de solo culpar a los directivos específicos.

#### 3.4 α del operador: las formas de la contención del riesgo


confiabilidad

#### En el dominio de la ingeniería de seguridad, α del operador tiene una escala específica que va desde la no intervención hasta la disidencia documentada y el paro del proceso:

Nivel de α Rango Conducta observable del operador

Silencio pasivo 0.00– 0.05 El operador no expresó ninguna objeción, aunque tenía información de riesgo. No intervino en ningún momento del proceso.

Objeción verbal sin documentar

0.06– 0.20 Expresó preocupación verbalmente pero no la documentó formalmente. La objeción no quedó en el registro del proceso de decisión.

Objeción documentada

0.21– 0.45 Documentó su disidencia formalmente. La objeción consta en el registro pero no detuvo el proceso.

Escala formal 0.46– 0.70 Escaló la objeción a niveles superiores del sistema. Usó los canales formales de reporte de riesgo.

Disidencia institucional

0.71– 0.89 Rechazó formalmente participar en la decisión o certificar el proceso. Boisjoly recomendó no lanzar y documentó su recomendación: α ≈ 0.80.

0.90– 1.00 Detuvo unilateralmente el proceso o reportó externamente el riesgo. Solo posible cuando el operador tiene autoridad o cuando las consecuencias de la objeción son aceptables para él.

Paro del proceso

El análisis del α de Boisjoly es el más rico del caso Challenger: ejerció objeción verbal, documentación formal y disidencia institucional (recomendó explícitamente no lanzar). Su α ≈ 0.80 es alto. Pero su INCF es bajo porque su posición en el grafo (ingeniero sin autoridad final de decisión) limitaba el impacto de su acción. La conclusión es


confiabilidad

importante: el problema no era el α bajo de Boisjoly. Era el diseño del sistema que no conectaba la voz de los ingenieros con el poder de decisión.

#### 3.5 Los hijos de los operadores: la disposición de la voluntad en la decisión crítica

Los hijos del operador en el momento de la decisión crítica de ingeniería describen desde qué disposición tomó esa decisión. La distinción más importante en este dominio es entre:

- Fobos dominante: el operador cedió ante la presión por miedo a las consecuencias personales de resistir (perder el contrato, ser marginado en la organización, enfrentar la presión de un superior). El sistema produjo el Fobos; el operador lo siguió.
- Potós dominante: el operador siguió el procedimiento establecido sin cuestionarlo, porque "siempre lo hacemos así". No hubo deliberación sobre si ese procedimiento era adecuado para esas condiciones específicas.
- Anteros dominante: el operador tomó la decisión sabiendo que implicaba un riesgo superior al aceptable, pero la afirmó de todas formas porque lo convenía (mantener el contrato, cumplir el plazo, satisfacer al cliente). Esta es la disposición de mayor culpabilidad subjetiva en el dominio de la ingeniería.
- Harmonía: el operador deliberó con plena información y tomó la decisión que consideró correcta dado el balance de riesgos disponibles. Puede haber equivocado el cálculo (error de ingeniería) pero no actuó desde el miedo ni desde la presión.



confiabilidad

### §4.  Casos resueltos

Caso A — Challenger STS-51-L (28 de enero de 1986)

La junta teórica no era el problema: INCF de la presión política, Morton Thiokol y la NASA

A.1 El contexto histórico

El programa del Transbordador Espacial había acumulado nueve misiones exitosas consecutivas antes del Challenger. El 28 de enero de 1986 iba a ser el vigésimo quinto vuelo del programa. A bordo viajaba Christa McAuliffe, la primera maestra en el espacio, seleccionada dentro del programa Teacher in Space de la NASA. Ronald Reagan iba a mencionar la misión en su discurso del Estado de la Unión esa noche.

La noche anterior al lanzamiento, los ingenieros de Morton Thiokol llevaban horas en una teleconferencia con los centros de la NASA debatiendo el efecto del frío sobre las juntas teóricas. Los datos de Boisjoly eran claros: en los vuelos anteriores donde se habían observado erosiones de las juntas, la temperatura era invariablemente más alta que en las condiciones previstas para el día siguiente. La extrapolación a 29°F (la temperatura mínima prevista) estaba completamente fuera del rango de experiencia documentada.

El gerente de nivel intermedio de Morton Thiokol, Joe Kilminster, solicitó una pausa para que los directivos de la empresa deliberaran sin los representantes de la NASA. En esa pausa, el vicepresidente de ingeniería de Morton Thiokol, Jerald Mason, le dijo a Robert Lund —el vicepresidente de ingeniería que había apoyado a los


confiabilidad

#### ingenieros— que "se pusiera el sombrero de gestión y dejara el de ingeniero". Lund cambió su posición. Kilminster firmó la autorización de lanzamiento.

#### A.2 El grafo causal del Challenger

Tipo Función causal en el accidente

Nod o

Actor/Facto r

N1 Presión política / agenda del lanzamiento

Sistémico/político La fecha de lanzamiento estaba vinculada al discurso de Reagan. La presión para lanzar en esa fecha específica fue el factor que comprimió el umbral de θ de todos los nodos de decisión. Sin esa presión, el lanzamiento habría sido pospuesto.

N2 NASA: gestión del programa (nivel L-II y L-III)

Organizacional/decisió n

El proceso de decisión de la NASA no tenía un mecanismo formal para que las objeciones de los ingenieros subcontratista s bloquearan el lanzamiento.


confiabilidad

La gestión de la NASA operaba con la expectativa de que Morton Thiokol recomendaría el lanzamiento.

N3 Directivos de Morton Thiokol (Mason, Lund, Kilminster)

Operadores en nodo crítico

Tomaron la decisión de revertir la recomendació n de los ingenieros y firmar la autorización de lanzamiento. Es el nodo de decisión más crítico del grafo.

N4 Sistema de diseño de la junta teórica

Diseño técnico La junta fue diseñada con tolerancias que no cubrían temperaturas < 53°F. Esa brecha de diseño era conocida y había producido erosiones en vuelos anteriores sin consecuencias fatales.

N5 Junta teórica O-

Componente físico El componente


confiabilidad

ring del propulsor derecho

que falló técnicamente. Su INCF es real pero no dominante: sin las condiciones de N1-N3, no habría fallado en ese momento específico.

N6 Boisjoly y Thompson (ingenieros)

Operadores de contención

Ejercieron la mayor contención disponible en su posición. α ≈ 0.80. Su Δ es negativo (asumieron más de lo que su INCF requería). No son causalmente responsables del accidente: son el nodo de mayor α del grafo.

Nf Los siete tripulantes del Challenger

Nodo final No entra en el cálculo de INCF.

#### A.3 INCF, S y el análisis de los hijos

Nodo INCF S α Interpretación


confiabilidad

~28% 0.40 0.00 S moderado-bajo: era esta presión específica la que hizo que ese día en particular fuera inamovible. Otro ciclo de presión habría producido una dinámica diferente.

N1 — Presión política

~26% 0.70 0.05 S alto: cualquier gestor de programa bajo la misma estructura de decisión habría operado igual. El problema era el proceso, no las personas.

N2 — NASA gestión

~22% 0.62 0.08 S moderado-alto: bajo la misma presión de contrato y relación con la NASA, otros directivos habrían actuado similarmente. Pero la frase de Mason "ponte el sombrero de gestión" indica Anteros: deliberación que culminó en la decisión de asumir el riesgo.

N3 — Directivos MT

~14% 0.55 0.10 Brecha de diseño conocida pero no corregida. INCF real por la decisión de operar sin corregir el diseño.

N4 — Diseño de la junta

~8% 0.85 0.00 Componente físico con S alto: cualquier junta teórica del mismo diseño habría fallado en esas condiciones. El INCF del componente es bajo porque el diseño (N4) y las condiciones sistémicas (N1-N3) eran la causa dominante.

N5 — Junta teórica física


confiabilidad

~2% 0.30 0.80 Δ = 2% − 80% = −78%: asumieron mucho más de lo que su posición causal requería. Son el modelo de lo que el sistema de seguridad necesita y no tenía mecanismos para potenciar.

N6 — Boisjoly / Thompson

#### A.4 Los hijos en el momento de la decisión: dos noches, dos disposiciones

#### Boisjoly y Thompson — La noche antes del lanzamiento:

Anteros     ██████████░░░░░░░░░░ 48% Harmonía    ██████░░░░░░░░░░░░░░ 28% Fobos       ███░░░░░░░░░░░░░░░░░ 14% Deimos      █░░░░░░░░░░░░░░░░░░░ 6% Potós       █░░░░░░░░░░░░░░░░░░░ 4% Eros        ░░░░░░░░░░░░░░░░░░░░ 0%

#### Directivos de Morton Thiokol (Mason, Lund) — En la pausa:

Fobos       ████████░░░░░░░░░░░░ 40% Potós       ██████░░░░░░░░░░░░░░ 28% Anteros     ████░░░░░░░░░░░░░░░░ 18% Deimos      ██░░░░░░░░░░░░░░░░░░ 10% Harmonía    █░░░░░░░░░░░░░░░░░░░ 4% Eros        ░░░░░░░░░░░░░░░░░░░░ 0%

El contraste entre los dos perfiles es el diagnóstico central del caso: los ingenieros actuaron desde Anteros + Harmonía (afirmación de su criterio con deliberación plena de la información disponible). Los directivos actuaron desde Fobos + Potós + Anteros institucional (miedo a las


confiabilidad

consecuencias de contradecir a la NASA, persistencia en la relación habitual, y la afirmación de que su rol como gestión era tomar la decisión, aunque los ingenieros no estuvieran de acuerdo).

La frase que define el caso:  Jerald Mason le dijo a Robert Lund "ponte el sombrero de gestión". Esa instrucción es la descripción más precisa que existe de la transición de Harmonía a Fobos en tiempo real: "deja de deliberar con tus datos de ingeniería y actúa desde tu posición en la jerarquía". Es la instrucción de desactivar φ₂ y actuar desde el campo del sistema en lugar de desde el eje propio. Boisjoly no siguió esa instrucción. Lund sí. Esa diferencia de disposición es la diferencia entre α = 0.80 y α = 0.08 en el momento más crítico del grafo.

A.5 El D_total del Challenger

Parámetros:

- Siete vidas perdidas. Edad promedio: 37 años. Esperanza de vida residual promedio: ~43 años = 376,680 horas.
- Costo directo de la investigación y las reformas del programa: ~$3,200 millones USD (en dólares de 1986 = ~$9,000M en 2024).
- Programa del Transbordador suspendido 32 meses. Pérdida de misiones y daño reputacional de la NASA.
- ΔT_trayectoria del programa espacial: el retraso en el desarrollo del programa científico tiene un costo de oportunidad estimado en $25,000-35,000M USD en valor presente.


D_vital_directo = 7 × 376,680 h = 2.637 × 10⁶ horas de

vida

D_monetary_equiv_vital = 2.637M h × $8/h = $21.1M

USD (2024)

D_total_sistémico ≈ $9,000M + $30,000M = $39,000M

USD (2024)


confiabilidad

La distribución del ajuste debitor (AD) entre los nodos del grafo:

AD_N1 (presión política) = 0.28 × $39,000M =

$10,920M

AD_N2 (NASA gestión) = 0.26 × $39,000M =

$10,140M

AD_N3 (directivos MT) = 0.22 × $39,000M =

$8,580M

Las reformas institucionales que siguieron al Challenger (los protocolos de decisión de lanzamiento del Informe Rogers, la reorganización de la NASA) actuaron principalmente sobre N2 —el proceso de decisión de la NASA. Eso es α_diferido del nodo regulatorio-institucional. No actuaron con la misma intensidad sobre N1 (la presión política del calendario de lanzamiento), que fue el nodo de mayor INCF. Eso explica parcialmente por qué el patrón se repitió con el 737 MAX: la reforma no tocó el nodo dominante.


confiabilidad

Caso B — Boeing 737 MAX (octubre 2018 — marzo 2019)

El mismo patrón 32 años después: INCF del sistema de certificación delegada y de la presión comercial

B.1 El contexto histórico

En 2010, Airbus anunció el A320neo —una versión del exitoso A320 con motores de nueva generación significativamente más eficientes en combustible. American Airlines, que tenía una relación exclusiva con Boeing, comenzó a negociar la compra de aviones Airbus. Boeing necesitaba una respuesta rápida que no requiriera que las aerolíneas entrenaran de nuevo a sus pilotos —el entrenamiento diferencial es caro y una ventaja competitiva de tener flotas uniformes.

Boeing eligió modernizar el 737 NG en lugar de diseñar un avión completamente nuevo. Los nuevos motores LEAP-1B eran más grandes y eficientes, pero requerían montarse más adelante y más arriba en el ala para dar espacio al suelo —lo que cambiaba el comportamiento aerodinámico del avión, tendiendo el morro a subir en ciertas condiciones. Boeing diseñó el MCAS para compensar automáticamente esa tendencia y mantener las características de vuelo similares a las del 737 NG.

El MCAS, sin embargo, fue certificado como sistema de categoría de riesgo "hazardous" en lugar de "catastrophic" —la clasificación que sus consecuencias reales ameritaban. La razón documentada: la clasificación "catastrophic" habría requerido un programa de entrenamiento diferencial para los pilotos, lo que habría eliminado la principal ventaja competitiva del 737 MAX frente al A320neo. El MCAS fue mencionado en los manuales de operación con una nota de pie de página. Los pilotos del JT610 y del ET302 no sabían


confiabilidad

#### que existía cuando el avión comenzó a empujar el morro hacia abajo de manera que no podían comprender ni contrarrestar.

#### B.2 El grafo causal del 737 MAX

Nodo Actor/Factor Tipo Función causal en los accidentes

N1 Boeing dirección: presión comercial y la decisión de reclasificar el MCAS

Diseño del incentivo sistémico

La decisión de reducir la clasificación de riesgo del MCAS de "catastrophic" a "hazardous" para evitar el requerimiento de entrenamiento diferencial. Sin esa decisión, los pilotos habrían tenido la información y el entrenamiento para contrarrestar el MCAS.

N2 Diseño del MCAS: sensor único sin redundancia + sin indicador estándar

Diseño técnico con omisión crítica

El MCAS dependía de un solo sensor AoA (Angle of Attack). Si ese sensor fallaba, el MCAS actuaba de todas formas. Adicionalmente, el indicador de desacuerdo entre sensores AoA no era estándar —era una opción de pago. Dos 737 MAX crasheados no lo tenían activado.

N3 FAA: certificación delegada sin

Omisión regulatoria

La FAA había delegado gran parte de la certificación del


confiabilidad

supervisión suficiente

737 MAX a los propios ingenieros de Boeing bajo el ODA (Organization Designation Authorization). Los supervisores de la FAA no entendieron completamente el MCAS antes de certificar el avión.

N4 Sensor AoA defectuoso del JT610 y ET302

Componente físico

El sensor que envió lecturas erróneas al MCAS. INCF bajo: cualquier sensor con una falla equivalente en el mismo sistema habría producido el mismo resultado.

N5 Aerolíneas: falta de información sobre el MCAS

Brecha de información

Las aerolíneas no tenían información suficiente sobre el MCAS para diseñar procedimientos de emergencia o entrenar a sus pilotos.

N6 Pilotos del JT610 y ET302

Operadores terminales sin información

Enfrentaron una situación para la que no tenían información ni entrenamiento. Su S es muy alto: cualquier piloto sin el conocimiento del MCAS habría tenido las mismas dificultades.

Nf 346 víctimas Nodo final No entra en el cálculo de INCF.


confiabilidad

#### B.3 INCF y el isomorfismo con el Challenger

Nodo INCF S Analogía con Challenger

~32% 0.30 Análogo a N1 (presión política) + N3 (directivos MT) del Challenger. La presión comercial es el equivalente funcional de la presión política.

N1 — Boeing dirección

~28% 0.40 Análogo a N4 (diseño de la junta). La brecha de diseño conocida pero no corregida: MCAS sin redundancia de sensor.

N2 — Diseño MCAS

~22% 0.65 Análogo a N2 (NASA gestión). El regulador que aceptó la clasificación de riesgo rebajada sin comprenderla completamente.

N3 — FAA certificación

~8% 0.88 Análogo a N5 (junta teórica). Componente físico con S alto: cualquier sensor equivalente con la misma falla en el mismo sistema.

N4 — Sensor AoA

~6% 0.80 Brecha de información con S alto: cualquier aerolínea en la misma situación informativa habría operado igual.

N5 — Aerolíneas

N6 — Pilotos ~4% 0.95 S muy alto. Su α es prácticamente cero no porque no actuaran sino porque no tenían la información para actuar.

El isomorfismo entre los dos accidentes es casi perfecto: los nodos de diseño organizacional tienen INCF dominante (~82% combinado en ambos casos), el componente físico tiene INCF < 10%, y el sistema de certificación tiene INCF en el rango 22-26%. La diferencia más importante es que en


confiabilidad

el Challenger había ingenieros con información (Boisjoly, Thompson) que ejercieron contención real. En el 737 MAX, la información que habría permitido ejercer contención estaba deliberadamente ocultada — los pilotos no sabían que el MCAS existía.

B.4 Los hijos de la dirección de Boeing en la decisión de reclasificar

El análisis de las comunicaciones internas de Boeing, reveladas durante las investigaciones del Congreso y la FAA, permite reconstruir el perfil de hijos de los directivos que tomaron la decisión de reclasificar el MCAS:

Anteros     █████████░░░░░░░░░░░ 45% Potós       ██████░░░░░░░░░░░░░░ 28% Fobos       ███░░░░░░░░░░░░░░░░░ 16% Deimos      ██░░░░░░░░░░░░░░░░░░ 8% Harmonía    █░░░░░░░░░░░░░░░░░░░ 3% Eros        ░░░░░░░░░░░░░░░░░░░░ 0%

El perfil de hijos de la dirección de Boeing es estructuralmente similar al de los directivos de Morton Thiokol: Anteros dominante con Fobos secundario. Pero hay una diferencia significativa: en el caso de Morton Thiokol, la información de riesgo era conocida y fue ignorada en una teleconferencia documentada. En el caso de Boeing, la información de riesgo fue activamente gestionada para que no llegara al nivel donde habría forzado una decisión diferente. Los correos internos de ingenieros de Boeing mostrando preocupaciones sobre el MCAS no fueron escalados al nivel de decisión en ningún momento antes del primer accidente.

Esa diferencia —ignorar la información vs. gestionar que la información no llegue al decisor— es la diferencia entre


confiabilidad

Anteros sobre la información disponible (Challenger) y Anteros sobre el flujo de información (737 MAX). El segundo caso tiene mayor culpabilidad subjetiva porque implica un diseño activo de la opacidad.

B.5 Por qué el sistema no aprendió: el análisis de J

El Índice de Justicia Estructural del proceso post-Challenger fue aproximadamente:

J_Challenger = 1 − Σ|Δᵢ| ≈ 1 − (0.28 + 0.21 + 0.14 +

...) ≈ 0.30

Un J = 0.30 indica que las reformas del Challenger redujeron, pero no eliminaron el déficit de asunción en los nodos de mayor INCF. La reforma atacó principalmente N2 (proceso de decisión NASA, α pasó de 0.05 a ~0.45 con las nuevas reglas de Rogers), pero no tocó N1 (la presión política del calendario) ni cambió sustancialmente la estructura de incentivos de los subcontratistas.

Treinta y dos años después, la estructura de incentivos que había producido el comportamiento de Morton Thiokol reapareció en Boeing: la presión comercial (análoga a la presión política del calendario) sobre los directivos que certificaban el sistema. J_Challenger no era suficientemente alto para haber producido los cambios sistémicos que habrían prevenido el 737 MAX.

Lección estructural: J_sistema < 0.60 → el patrón

causal puede reaparecer con nombres diferentes

La condición para que el sistema aprenda genuinamente no es el proceso forense del accidente (que siempre identifica el componente físico con mayor precisión que los nodos organizacionales) sino el análisis de INCF completo que distribuye la responsabilidad causal entre todos los nodos y mide el J del sistema de respuesta.


confiabilidad

### §5.  Límites del método en ingeniería de sistemas

#### 5.1 El problema de los fallos concurrentes

Muchos accidentes de ingeniería complejos son el resultado de múltiples fallos simultáneos cuya combinación produce el accidente, aunque ninguno de ellos individualmente lo habría producido. En esos casos, el postulado de la condición necesaria no se cumple para ningún nodo individual. El análisis de INCF debe complementarse con el valor de Shapley —desarrollado en las extensiones del Apéndice— para distribuir la responsabilidad en fallos de causación múltiple acumulativa.

#### 5.2 El problema de los testigos no disponibles

La reconstrucción del grafo causal en accidentes de ingeniería frecuentemente requiere información sobre decisiones que no quedaron documentadas. La investigación forense puede recuperar parte de esa información (cajas negras, registros de vuelo, correos internos), pero siempre habrá decisiones cuyos pesos solo pueden estimarse con incertidumbre. El análisis de sensibilidad es especialmente importante en esos casos.

#### 5.3 La distinción entre el fallo como sistema y el fallo como accidente

El método produce un vector INCF sobre el grafo de un accidente específico. Ese vector describe qué nodos fueron condición necesaria de este accidente. No dice nada sobre la frecuencia esperada de accidentes similares en el futuro


confiabilidad

—eso requiere el análisis de probabilidad del FTA convencional. El INCF y el FTA son complementarios: el FTA mide la frecuencia, el INCF distribuye la responsabilidad sobre el accidente que ya ocurrió.

#### 5.4 Los hijos y las decisiones grupales

Muchas de las decisiones críticas en ingeniería de seguridad se toman en grupo (los directorios de lanzamiento de la NASA, los comités de certificación). El diagnóstico de hijos individuales dentro de un proceso grupal es más complejo porque la decisión grupal emerge de interacciones que no reducen al perfil de hijos de ningún individuo. El sistema recomienda en esos casos diagnosticar el "hijo del grupo" (la disposición emergente del proceso colectivo) en lugar de intentar reconstruir el perfil de cada participante.


confiabilidad

§6.  Profundización formal — Esta sección puede saltarse sin perder el argumento del capítulo

### §6.  Profundización formal

#### 6.1 INCF vs. FTA: la relación formal

Sea G_fallo el grafo causal del accidente y sea P_FTA(N_i) la probabilidad de fallo del nodo i calculada con el árbol de fallos convencional. El INCF y P_FTA están relacionados, pero no son equivalentes:

P_FTA(N_i) = P (N_i falla) independientemente del

grafo

INCF(N_i) = R*ᵢ sobre el grafo G_fallo

La diferencia: P_FTA es una medida de la fragilidad intrínseca del componente. INCF es una medida de la necesidad causal del nodo en el accidente específico. Un componente con P_FTA alta puede tener INCF bajo si hay redundancia (S alto: si falla N_i, otro nodo lo sustituye y el accidente no ocurre). Un componente con P_FTA baja puede tener INCF alto si es el único punto de fallo del sistema (S bajo: si falla N_i, el accidente es inevitable).

Para el análisis de responsabilidad, INCF es el instrumento correcto. Para el diseño preventivo del sistema, la combinación de P_FTA e INCF es óptima:

Prioridad_mejora_i = P_FTA(N_i) × INCF(N_i) × (1

− α_i)

El nodo de mayor prioridad de mejora es el que combina alta probabilidad de fallo, alta necesidad causal en el accidente y baja provisión de seguridad.


confiabilidad

#### 6.2 El modelo del umbral de presión y el fallo de Harmonía

Cada operador tiene un umbral θ que define el nivel de presión del sistema que puede soportar antes de que sus hijos cambien de Harmonía/Anteros a Fobos/Potós. Formalmente:

h_dominante(t) = Harmonía     si Presión_sistema(t)

< θᵢ

h_dominante(t) = Fobos/Potós si Presión_sistema(t)

≥ θᵢ

El colapso del sistema de decisión ocurre cuando la presión supera el umbral del operador en el nodo crítico. Las reformas de seguridad que aumentan θᵢ (aumentan la resiliencia del operador ante la presión) son más eficientes que las que intentan reducir la presión del sistema, porque la presión suele ser exógena al sistema de seguridad.

Los mecanismos que aumentan θᵢ efectivamente:

- Protección explícita a quien reporta: el operador que frena el proceso no pierde su posición en la organización.
- Separación formal entre la voz técnica y la decisión de gestión: el "sombrero de gestión" no puede anular unilateralmente la recomendación de ingeniería sin un proceso documentado.
- Requerimiento de doble firma para decisiones de alta consecuencia: si hay una voz técnica disidente, la decisión de proceder requiere firma adicional de un nivel superior al del decisor de gestión.
- Cultura de incidentes sin consecuencias: los operadores pueden reportar near-misses sin temor a consecuencias, lo que permite identificar el perfil de presión sistémica antes de que produzca el accidente.



confiabilidad

#### 6.3 El Índice de Aprendizaje Sistémico (IAS)

El Índice de Aprendizaje Sistémico mide en qué medida el sistema de seguridad incorporó las lecciones de un accidente previo en su diseño. Es la aplicación del J al ciclo de reforma:

IAS = J_post_reforma − J_pre_reforma

Si J_post_reforma ≈ J_pre_reforma, el sistema no aprendió: las reformas no redujeron el déficit de asunción en los nodos de mayor INCF. Si IAS es alto, el sistema genuinamente transformó la distribución de responsabilidad causal y asunción.

Para el ciclo Challenger → 737 MAX:

J_pre_Challenger ≈ 0.10 (sin reforma ninguna) J_post_Rogers ≈ 0.30 (reforma parcial: N2 mejorado)

IAS_Challenger = 0.30 − 0.10 = 0.20

J_pre_737MAX ≈ 0.30 (herencia de las reformas del Challenger) J_necesario para prevenir ≈ 0.60 (umbral para que el patrón no se repita) La brecha entre J_post_Rogers = 0.30 y J_necesario = 0.60 es exactamente la medida de por qué el sistema no aprendió suficientemente: el IAS fue positivo, pero no suficientemente alto. La reforma tocó el nodo correcto (N2, el proceso de decisión NASA) pero no con la profundidad necesaria para que el mismo patrón no emergiera tres décadas después con un actor diferente (Boeing) en un rol análogo al de Morton Thiokol.

#### 6.4 Código Python de referencia

import numpy as np from scipy.stats import pearsonr  def analisis_fallo_ingenieril(W_fallo, alpha_operadores,


confiabilidad

P_FTA=None, D_total=None,                                w_ref=8.0):     """ Análisis de responsabilidad causal en fallos de ingeniería de sistemas. W_fallo:          matriz de pesos del grafo causal del fallo alpha_operadores: α por nodo (contención ejercida por cada operador) P_FTA:            vector de probabilidades de fallo FTA (opcional) D_total:          daño total del accidente     """     n = W_fallo.shape[0] # ── INCF = R*: índice de necesidad causal del fallo ──     R = np.ones(n) / n     for _ in range(500):         Rn = W_fallo @ R; s = np.sum(Rn)         if s < 1e-12: break         Rn /= s         if np.max(np.abs(Rn - R)) < 1e-9: break         R = Rn     INCF = Rn      # ── S: fungibilidad del nodo en el fallo ──     S = np.zeros(n)     for i in range(n):         max_c = 0         for j in range(n):             if j == i: continue             Wm = W_fallo.copy()             Wm[i,:] = np.mean(W_fallo, axis=0)             Rm = np.ones(n)/n             for _ in range(200):                 Rm2 = Wm @ Rm; sm = np.sum(Rm2) if sm < 1e-12: break                 Rm2 /= sm                 if np.max(np.abs(Rm2-Rm)) < 1e-6: break                 Rm = Rm2             c, _ = pearsonr(INCF, Rm2)             max_c = max(max_c, abs(c))         S[i] = 1 - max_c      Delta = INCF - alpha_operadores     INCF_neta = INCF * (1 - S)  # responsabilidad idiosincrática      result = { 'INCF': INCF,         'S': S,         'Delta_contencion': Delta, 'INCF_neta': INCF_neta,         'nodo_critico': int(np.argmax(INCF_neta)),         'J_sistema': float(1 -np.sum(np.abs(Delta))),     }      # ── Prioridad de mejora (FTA × INCF × (1−α)) ──     if P_FTA is not None: result['prioridad_mejora'] = P_FTA * INCF * (1 - alpha_operadores) result['nodo_mejora_prioritaria'] = int(np.argmax(result['prioridad_mejora']))      if D_total:         result['AD'] = INCF * D_total         result['D_vital'] = D_total / w_ref      return result  def indice_aprendizaje_sistemico(J_antes, J_despues):     """ IAS: mide si el sistema genuinamente incorporó las lecciones del accidente.     """     IAS = J_despues - J_antes     nivel = ('Aprendizaje pleno' if IAS > 0.30              else 'Aprendizaje parcial' if IAS > 0.15 else 'Aprendizaje mínimo' if IAS > 0.05              else 'Sin aprendizaje') return {'IAS': IAS, 'nivel': nivel,             'J_antes': J_antes, 'J_despues': J_despues}  # ── Challenger ── W_ch = np.zeros((7,7)) # N0=Presión_política, N1=NASA_gestión, N2=Directivos_MT, # N3=Diseño_junta, N4=Junta_tórica, N5=Boisjoly, N6=Nf W_ch[0,1]=0.80; W_ch[0,2]=0.75; W_ch[0,6]=0.65 W_ch[1,2]=0.85; W_ch[1,6]=0.70 W_ch[2,6]=0.80; W_ch[3,4]=0.90; W_ch[3,6]=0.55 W_ch[4,6]=0.70; W_ch[5,6]=0.10  # Boisjoly intentó frenar  alpha_ch = np.array([0.00, 0.05, 0.08, 0.10, 0.00, 0.80, 0.0]) P_FTA_ch = np.array([0.05, 0.08, 0.12, 0.20, 0.35, 0.02, 0.0])  res_ch = analisis_fallo_ingenieril(     W_ch, alpha_ch, P_FTA=P_FTA_ch, D_total=39_000_000_000, w_ref=8.0)  nodos_ch = ['N0-Presión_pol.','N1-NASA_gest.','N2-Directivos_MT',             'N3-Diseño_junta','N4-O-ring','N5-Boisjoly','Nf'] print("=== Challenger — Análisis de fallo sistémico ===") for nm, incf, si, di in zip(nodos_ch, res_ch['INCF'],                               res_ch['S'], res_ch['Delta_contencion']):     flg = ' ← CRÍTICO' if incf == max(res_ch['INCF']) else ''     print(f"  {nm:18s}  INCF={incf:.3f}


confiabilidad

S={si:.2f}  Δ={di:+.3f}{flg}")  J_ch = res_ch['J_sistema'] print(f"\nJ_sistema (Challenger):  {J_ch:.3f}")  ias = indice_aprendizaje_sistemico(0.10, J_ch) print(f"IAS post-Rogers: {ias['IAS']:.3f}  ({ias['nivel']})") ias2 = indice_aprendizaje_sistemico(J_ch, 0.60) print(f"IAS necesario para prev. 737MAX: {ias2['IAS']:.3f} adicionales")

Miguel Hilario Olvera Aguilar Centro Multidisciplinario Meriadock Formación y Asesoría A.C., 2026 Continúa en el Capítulo 13 — Inteligencia artificial y algoritmos de decisión

El Cálculo de la Responsabilidad  ·  Cap. 13 — IA y algoritmos de decisión


