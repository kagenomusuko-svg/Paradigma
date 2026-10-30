# APÉNDICE A
## El sistema como instrumento de gestión empresarial

*Encontrar a alguien a quien culpar no es lo mismo que resolver el problema — y confundirlo tiene costos reales para los accionistas*

---

Este apéndice no es una defensa de los empresarios. Es una advertencia para los accionistas. La distinción importa porque sus intereses no siempre coinciden.

A lo largo del libro, el sistema de imputación causal produce resultados que son, en muchos casos, adversos para las instituciones que aparecen en el grafo: la FHA/HOLC en el redlining, Union Carbide en Bhopal, Northpointe en COMPAS, la institución bancaria del Caso Eje. En ninguno de esos análisis se buscó la exoneración de la institución ni se suavizó la distribución del R*. El sistema no trabaja para proteger a las empresas. Trabaja para distribuir la responsabilidad donde causalmente corresponde.

Precisamente por eso tiene valor para los accionistas: porque cuando una institución imputa la responsabilidad al nodo equivocado, son los accionistas quienes pagan el costo de ese error. No una vez. Dos veces.

::: {.recuadro .tension-roja}
**Tensión real:** La tensión que este apéndice nombra sin resolverla artificialmente: hay casos en el libro donde el análisis causal es genuinamente adverso para la empresa, y ese análisis es correcto. El argumento no es que el sistema protege a las empresas. El argumento es que las empresas que confunden la narrativa de culpabilidad con el análisis causal real actúan contra los intereses de sus propios accionistas, y el sistema permite verlo con precisión antes de que el daño ocurra por segunda vez.
:::


#### Argumento 1 — El costo del chivo expiatorio para el accionista

Argumento 1 — Shareholder value Cuando una empresa procesa a un ejecutor de S alto mientras la estructura de R* alto permanece intacta, los accionistas absorben el costo del evento dos veces: una en el evento original, y otra cuando el mismo evento se repite con un ejecutor diferente.

El chivo expiatorio corporativo —el nodo de baja responsabilidad causal que asume la culpa del evento— es una herramienta de gestión de narrativa de corto plazo que produce un costo de largo plazo calculable. Para entenderlo, es necesario separar dos procesos que las instituciones frecuentemente confunden:

Proceso Pregunta que responde A quién protege

Gestión de la narrativa

"¿Quién tiene la culpa visible del evento?" Busca un nombre que satisfaga la demanda de responsabilidad de reguladores, prensa y accionistas.

Protege a la dirección ejecutiva de las consecuencias de corto plazo.

Análisis causal real

"¿Qué nodo del sistema fue condición necesaria del evento, y con qué S?" Busca la intervención que reduce la probabilidad del próximo evento.

Protege el capital de los accionistas a largo plazo.


Cuando la gestión de la narrativa sustituye al análisis causal, el accionista sufre el equivalente financiero de tratar los síntomas sin diagnosticar la enfermedad. El síntoma desaparece temporalmente; la enfermedad progresa.

#### 1.1 El costo del evento doble: la aritmética del S alto

Consideremos el patrón general: una institución tiene un evento de daño producido por un ejecutor con S = 0.85. Eso significa que el 85% del resultado habría ocurrido con cualquier otro ejecutor en la misma posición. La institución procesa al ejecutor, lo separa, y continúa operando con la misma estructura de incentivos y el mismo diseño del rol.

P (evento en año t) = P_base × [1 − α_estructura]

Si α_estructura = 0 (no se reformó el diseño) → P

(evento en t+1) ≈ P_base

La probabilidad del próximo evento no disminuyó. La institución solo cambió el nombre del ejecutor.

El costo acumulado de la estrategia del chivo expiatorio:

Período Evento Costo pagado

Quién paga

Accionistas

t₀ Evento original. La institución procesa al ejecutor A.

D_evento + costos legales del proceso

Accionistas

No se reforma la estructura de R* alto. Solo se sustituye al ejecutor

Costo de sustitución y onboarding

t₀ + reforma 0


A por el ejecutor B en la misma posición.

El mismo evento se repite con el ejecutor B. La institución vuelve a procesar al ejecutor.

D_evento × 2 + costos legales × 2

Accionistas × 2

t₁ (próximo ciclo)

Costo de la reforma + D_evento_t₁

Accionistas — solo una vez más

t₁ + reforma real

Si en t₁ se reforma la estructura (se actúa sobre el nodo de R* alto), la probabilidad del siguiente evento cae sustancialmente.

La estrategia del chivo expiatorio es una apuesta implícita: que el próximo evento ocurrirá suficientemente tarde como para que el costo actualizado del doble evento sea menor que el costo político y reputacional de reconocer que el problema estaba en el diseño, no en el ejecutor. Esa apuesta tiene probabilidades razonables de ganarse en el corto plazo para la dirección ejecutiva, y probabilidades altas de perderse en el largo plazo para los accionistas.

#### 1.2 Enron, VW y el costo de la sustitución sin reforma

Los casos del Capítulo 11 ilustran la diferencia entre instituciones que reformaron la estructura y las que solo sustituyeron ejecutores. En Volkswagen, después del Dieselgate, se procesó penalmente a varios ingenieros de nivel medio (los ejecutores de S alto) mientras la cultura corporativa que producía la presión de objetivos imposibles fue reformada solo parcialmente. Cuatro años después del Dieselgate, VW enfrentó nuevas investigaciones por irregularidades en sus procesos de certificación en otros


mercados. El nodo de diseño no fue suficientemente modificado.

En Boeing, después del 737 MAX, la FAA reformó sustancialmente el proceso de certificación delegada (N3, R* = 22%) pero actuó con menor intensidad sobre la arquitectura de presión comercial que producía los objetivos imposibles (N1, R* = 32%). Los ingenieros de nivel medio siguieron enfrentando el mismo dilema estructural con nombres diferentes.

En ambos casos, el análisis de R* predecía ese resultado: cuando las reformas no tocan el nodo de mayor R* × (1−S), la probabilidad del próximo evento no cae suficientemente.

ΔP(próximo_evento) ≈ −R*_reformado × (1 −

S_reformado)

Si la reforma actuó sobre el ejecutor de S = 0.85, ΔICRS ≈ −0.15 × (1−0.85) = −0.0225. Si actuó sobre el nodo de diseño de S = 0.28, ΔICRS ≈ −0.45 × (1−0.28) = −0.324. La diferencia es de 14x en la reducción del riesgo por unidad de reforma.

La regla de los 14x:  Reformar el nodo de diseño de alto R* y baja S produce 14 veces más reducción del riesgo sistémico por unidad de esfuerzo que reformar el ejecutor de bajo R* y alta S. Esa es la aritmética que convierte al sistema de imputación causal en un instrumento de gestión de riesgos, no solo de asignación de responsabilidades.

#### 1.3 La pregunta que el lector debería hacerse después de cada evento significativo

Antes de decidir qué nodo del grafo asumir públicamente como responsable del evento, el lector debería poder responder estas tres preguntas con evidencia: El Cálculo de la Responsabilidad · Apéndices

1. ¿Cuál es el R* × (1−S) de cada nodo del grafo? ¿El nodo que estamos procesando tiene el mayor R* neto o el mayor S? 2. Si procesamos a ese nodo y no reformamos los de mayor R* neto, ¿cuánto cae la probabilidad del próximo evento? ¿Esa reducción justifica el costo de no actuar sobre el diseño? 3. ¿Qué activo de largo plazo estamos sacrificando al no corregir el nodo de diseño? ¿Capital regulatorio? ¿Reputación con inversores de largo plazo? ¿Capacidad de retener talento que señala problemas?

Si el lector no puede responder esas tres preguntas con datos, está tomando la decisión sobre la gestión del evento con información incompleta. El sistema de imputación causal no le dice al lector qué decidir. Le dice qué información necesita para tomar la decisión correctamente.


#### Argumento 2 — La reputación como función del IIC, no de la narrativa

Argumento 2 — Reputación La reputación corporativa se daña más por el patrón visible —empresa que culpa a ex-empleados mientras el sistema que produjo el problema sigue operando— que por el reconocimiento honesto de los nodos de diseño y su corrección. El IIC de 0.125 del Caso Eje no es solo un número interno: es lo que los reguladores, los inversores y los periodistas de investigación verían si construyeran ese índice con información pública.

El riesgo reputacional convencional se gestiona como un problema de comunicación: qué decir, cuándo decirlo, a quién. Esa gestión asume que la reputación es una función de la narrativa. El sistema de imputación causal sugiere algo diferente: la reputación es una función del IIC — del nivel de congruencia entre lo que la institución dice que hace y lo que efectivamente hace. Y el IIC es, en principio, calculable por terceros con información pública.

#### 2.1 El IIC como métrica de riesgo reputacional anticipado

El Índice de Integridad Corporativa (IIC) mide la correlación entre los valores declarados de una institución y su comportamiento observable. Valores declarados bajos, pero comportamiento consistente con ellos produce IIC alto (hay integridad, aunque el estándar sea bajo). Valores declarados altos y comportamiento inconsistente produce


#### IIC bajo — que es la disforia de identidad corporativa del Capítulo 11.

#### El IIC puede ser calculado por terceros porque:

- Los valores declarados están en documentos públicos: códigos de ética, políticas de conducta, declaraciones de gobierno corporativo, reportes de sostenibilidad.
- El comportamiento observable está en expedientes de litigios, resoluciones regulatorias, noticias de prensa, testimonios de ex-empleados, y datos de rotación de talento.
- La correlación entre ambos produce una señal que los inversores institucionales sofisticados, los reguladores avanzados y los periodistas de investigación pueden construir independientemente de lo que la institución comunique.


#### Lo que el IIC de 0.125 del Caso Eje comunica hacia afuera:

Audiencia Señal que lee Consecuencia potencial

Regulador (CNBV, CONDUSEF)

La institución negoció inicialmente la existencia de un correo electrónico con la Fiscalía. El proceso de denuncia tiene dilación de tres años inexplicada.

Mayor probabilidad de auditoría de conducta. Menor crédito de buena fe en futuros procesos regulatorios.

Inversor institucional de largo plazo

Una empresa que imputa responsabilidad a ex-empleados para evitar la remediación de su diseño tiene una estructura de gobierno

Prima de riesgo adicional sobre el papel de deuda. Menor múltiplo en valoración. Preguntas


corporativo que no protege el capital.

en el próximo road show.

Talento de alta calidad

Esta empresa culpa a los empleados cuando algo sale mal y protege el sistema que lo produjo.

Dificultad de retener y atraer exactamente el tipo de talento que señala problemas antes de que escalen. Selección adversa de talento dócil.

El patrón narrativo del caso es la historia que los periodistas buscan: empresa que protege el sistema culpando al empleado.

Periodista de investigación

Dilación de tres años, correo omitido, perfil de puesto que contradice la imputación.

#### 2.2 El patrón que los terceros ven, aunque la empresa no lo diga

La gestión de narrativa convencional opera con la suposición de que los terceros ven lo que la empresa comunica. El IIC bajo opera de manera diferente: los terceros pueden ver el patrón, aunque la empresa no lo comunique, precisamente porque el patrón es observable en la divergencia entre lo declarado y lo actuado.

#### El patrón del Caso Eje, construido solo con información pública y el expediente activo, produce:

- Una institución que diseñó un perfil de puesto que requiere acceso a expedientes y argumenta que ese acceso era indebido. La contradicción está en el propio documento público de la empresa.
- Una denuncia presentada tres años después de los hechos, en el momento de mayor asimetría con el ex-



empleado. El patrón temporal es observable en el expediente.

- Un correo electrónico inicialmente negado ante la Fiscalía. Ese hecho queda en el expediente y es información pública del proceso.


Ninguno de esos tres elementos requiere acceso a información confidencial. Todos son observables por cualquier tercero que lea el expediente con la metodología del análisis causal. La narrativa institucional puede suprimir la cobertura inmediata; no puede eliminar el patrón de los archivos.

::: {.recuadro .tension-roja}
**Tensión real:** La tensión aquí es real: reconocer que el nodo de diseño tiene el mayor R* en el evento tiene costos de corto plazo (regulatorios, mediáticos, de gobierno corporativo). Pero el costo de no reconocerlo es la acumulación del patrón en el registro público, que erosiona el IIC de manera observable y creciente. La pregunta no es si la reputación se daña, sino en qué horizonte temporal y con qué profundidad.
:::

#### 2.3 El reconocimiento honesto como estrategia de protección reputacional

El argumento más contraintuitivo de este apéndice: las instituciones que reconocen su posición causal y actúan sobre ella antes de que un tercero los obligue tienen mejor perfil de IIC que las que esperan a ser descubiertas. Eso produce mejores outcomes regulatorios, mejor valoración por inversores sofisticados, y menor probabilidad de cobertura mediática adversa.

Esto no es idealismo. Es el patrón que los estudios de crisis corporativas muestran consistentemente: las empresas que actúan con α alto antes de la crisis tienen procesos regulatorios más cortos, multas menores y recuperación


más rápida de la valoración. Las que actúan con α bajo y son descubiertas tienen exactamente el opuesto.

ROI_reconocimiento_temprano = (Multa_evitada + Prima_de_riesgo_reducida + Costo_litigio_evitado) /

Costo_α

Para el Caso Eje, el ROI del reconocimiento temprano (actuar sobre el nodo de diseño en t₀, cuando ocurrieron los hechos) habría sido:

Numerador: ~$9.8M MXN (B_total no obtenido) + reducción de prima regulatoria

Denominador: ~$1.4M-$2.5M MXN (costo de α diferido)

ROI ≈ (9.8 / 1.95) − 1 ≈ 402% El reconocimiento temprano habría producido un retorno del 400% sobre la inversión de actuar correctamente. Eso no incluye el costo del litigio activo ni el daño al IIC. El ROI de actuar correctamente en el diseño es positivo por amplio margen; la institución tomó la decisión contraria porque el beneficio del comportamiento predatorio se materializa en el corto plazo y el costo se distribuye en el largo.


#### Argumento 3 — El ROI de la prevención: invertir donde R* × (1−S) es más alto

Argumento 3 — ROI de la prevención R* × (1−S) identifica exactamente dónde invertir en prevención para obtener el mayor retorno. Un nodo de diseño con R* = 45% y S = 0.28 es el nodo donde una intervención preventiva de $1M evita eventos de $10M. Procesar al ejecutor de R* = 10% con S = 0.90 no reduce en nada la probabilidad del próximo evento.

El análisis de R* × (1−S) produce, para cada nodo del grafo, un indicador de la eficiencia de la prevención: cuánto riesgo se elimina por unidad de inversión. Ese indicador es el instrumento más directamente accionable del sistema para los directores de riesgo, los consejos de administración y los equipos de gobierno corporativo.

#### 3.1 La fórmula del ROI de prevención

ROI_prevención_i = [D_total × ΔP (evento |

α_i_mejorada)] / Costo_intervención_i

ΔP (evento | α_i) ≈ R*_i × (1 − S_i) × (α_nueva −

α_actual)

La interpretación práctica: si un nodo tiene R* = 0.45, S = 0.28 y α actual = 0.03, una intervención que lleva α a 0.60 reduce la probabilidad del evento en:

ΔP ≈ 0.45 × (1−0.28) × (0.60−0.03) = 0.45 × 0.72 ×

#### 0.57 ≈ 18.5 pp


#### Una reducción de 18.5 puntos porcentuales en la probabilidad de un evento que costó $50M produce un beneficio esperado de $9.25M. Si la intervención cuesta $1M, el ROI es 825%.

#### 3.2 Tabla comparativa de ROI por tipo de intervención

Aplicando la fórmula a los casos del libro, la tabla siguiente muestra el contraste entre el ROI de actuar sobre el nodo de diseño (alto R*, baja S) y el ROI de actuar sobre el ejecutor (bajo R*, alta S):

Caso Nodo interveni do

R* S ΔP prevenci ón

ROI por $1M invertido

26% 0.7 0 −7.8 pp Alto: ~$3B de D_total × 7.8% = $234M estimado

Challeng er — actuar sobre el sistema de alianzas NASA

N2 Proceso NASA

22% 0.6 2 −8.4 pp Moderado : mismo D_total pero S más alta limita el efecto

Challeng er — procesar a directivos MT

N3 Directivo s MT

32% 0.3 0 −22.4 pp Muy alto: ~$33B × 22.4% = $7.4B estimado

Boeing 737MAX — reformar arquitect ura de

N1 Boeing dirección


presión comercial

18% 0.8 2 −3.2 pp Muy bajo: mismo D_total pero S casi máxima

Boeing 737MAX — procesar a los ingeniero s

N3 Ingeniero s

#### 0.2 8 −32.5 pp Muy alto: ROI estimado 825%

Caso Eje — reformar diseño del rol

N1 Institució n

#### 45.1 %

#### 0.9 0 −1.0 pp Negativo: D_cliente =0, costo del proceso es real

Caso Eje — procesar al ex-gerente

N4 Ex-gerente

#### 10.4 %

El patrón es consistente a través de todos los casos del libro: actuar sobre el nodo de diseño de alta R* y baja S produce entre 5x y 70x más reducción del riesgo por unidad de inversión que actuar sobre el ejecutor de baja R* y alta S. Ese diferencial es la medida del costo de la confusión entre encontrar a alguien a quien culpar y resolver el problema.

#### 3.3 El presupuesto de prevención como problema de optimización

Para un lector con un presupuesto de prevención limitado, el análisis de R* × (1−S) convierte la asignación de ese presupuesto en un problema de optimización con solución única: invertir primero en el nodo donde el producto R* × (1−S) × D_total_esperado es mayor.


Prioridad_intervención_i = R*_i × (1 − S_i) ×

D_total_esperado / Costo_intervención_i

Esta fórmula produce el ranking de intervenciones por eficiencia preventiva. Ninguna herramienta convencional de gestión de riesgos produce este ranking porque ninguna separa el R* del S: los sistemas de gestión de riesgos convencionales miden la probabilidad y el impacto del evento, pero no la fracción del evento causalmente atribuible a cada nodo ni su sustituibilidad.

El ejemplo más directo del libro:

En la empresa mediana del Capítulo 9, el análisis de R* × (1−S) mostró que certificar un proveedor alternativo (intervención sobre N2, R* = 32%, S = 0.20) tenía ROI del 975%, mientras la reserva de liquidez (intervención sobre el capital buffer general, S = 0.55) tenía ROI negativo. Sin el análisis causal, cualquier director financiero razonable habría priorizado la reserva de liquidez porque es la intervención más visible y más convencional. La más eficiente era la menos obvia.

#### 3.4 Lo que el consejo de administración necesita pedir después de un evento significativo

El análisis de ROI de prevención produce un conjunto específico de preguntas que el consejo de administración debería formular al equipo de dirección después de cualquier evento de daño significativo:

Pregunta Por qué importa

¿Cuál es el R* × (1−S) de cada nodo del grafo del evento?

Identifica dónde está la concentración idiosincrática del riesgo — el nodo cuya reforma


produce la mayor reducción del riesgo de repetición.

¿El nodo que estamos procesando tiene el mayor R* neto o el mayor S?

Distingue entre procesar al responsable real (alto R* neto) y procesar al más visible (S alto, bajo R* neto). Solo el primero reduce el riesgo.

¿Cuál es la P(próximo_evento) si procesamos al ejecutor pero no reformamos el nodo de diseño?

Hace explícita la apuesta implícita en la estrategia del chivo expiatorio: cuánto riesgo residual queda después de la gestión de narrativa.

¿Cuál es el ROI de actuar sobre el nodo de diseño vs. el ROI de procesar al ejecutor?

Convierte la decisión en términos financieros que el consejo puede evaluar con los mismos criterios que cualquier inversión de capital.

Conecta la decisión de gestión del evento con el riesgo reputacional de largo plazo que los inversores y reguladores observarán.

¿Cómo cambia el IIC de la institución con cada una de esas opciones?


#### Síntesis: las tres preguntas que el sistema responde para la gestión empresarial

Los tres argumentos de este apéndice producen tres preguntas específicas que el sistema de imputación causal responde y que los instrumentos convencionales de gestión de riesgos no pueden responder con la misma precisión:

Pregunta Cómo el sistema la responde

1 ¿Dónde está el riesgo de repetición del evento?

R* × (1−S) del nodo de diseño. Cuanto mayor el producto, mayor la probabilidad de repetición si no se actúa sobre ese nodo.

2 ¿Qué daño reputacional de largo plazo estamos asumiendo al actuar sobre el ejecutor en lugar del diseño?

IIC: la divergencia entre valores declarados y comportamiento observable es calculable por terceros. El patrón de la divergencia es el riesgo reputacional real.

3 ¿Cuál es el ROI de las distintas opciones de intervención?

R* × (1−S) × D_total_esperado / Costo_intervención. El ranking de esta fórmula identifica la intervención de mayor eficiencia preventiva por unidad de capital invertido.

Estas tres preguntas no son nuevas para los directores de riesgo: ya las hacen intuitivamente después de cualquier evento significativo. Lo que el sistema añade es la capacidad de responderlas con precisión cuantificada, con evidencia documentada, y con resultados que pueden ser debatidos, cuestionados y actualizados.


Eso transforma la gestión del evento de un problema de percepción —qué narrativa construir— en un problema de ingeniería: qué nodo reformar, con qué costo, con qué retorno esperado. Los accionistas son los principales beneficiarios de esa transformación.

::: {.recuadro .tension-roja}
**Tensión real:** La tensión que este apéndice no resuelve: en el corto plazo, la gestión de la narrativa produce resultados visibles y la reforma del nodo de diseño produce costos visibles. El horizonte temporal del director de riesgos que quiere conservar su posición y el horizonte temporal del accionista de largo plazo no siempre coinciden. El sistema identifica el problema con precisión; la alineación de incentivos entre gestores y accionistas es un problema de gobierno corporativo separado, aunque relacionado.
:::

::: {.recuadro .alcance-azul-gris}
**Lo que el libro no promete:** Este apéndice no sugiere que el análisis causal elimina los conflictos de interés dentro de las instituciones ni que la racionalidad económica de largo plazo domina automáticamente sobre los incentivos de corto plazo de los gestores. Sugiere que el sistema produce la información necesaria para que el consejo de administración, los inversores activos y los reguladores puedan hacer las preguntas correctas con los instrumentos correctos. Lo que se haga con esa información depende del diseño de los mecanismos de gobierno — que es, en última instancia, el dominio del Capítulo 11.
:::


