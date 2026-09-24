# Capítulo 14. Medio ambiente y

## Contribución causal al daño ecológico: el límite del método y su extensión Cuando ningún nodo individual es condición necesaria y suficiente: la extensión mediante valores de Shapley

## §1.  El problema

En la madrugada del 3 de diciembre de 1984, una válvula de seguridad en la planta de Union Carbide en Bhopal, India, falló. En pocas horas, toneladas de isocianato de metilo —un gas utilizado en la producción de pesticidas— se escaparon hacia los barrios cercanos. Las cifras oficiales hablan de entre 3,800 y 7,575 muertes directas. Los estudios epidemiológicos más completos estiman entre 15,000 y 20,000 muertes relacionadas con la exposición durante los años siguientes. Medio millón de personas fueron expuestas. Decenas de miles sufren secuelas permanentes cuatro décadas después. El suelo y el agua subterránea en la zona de la planta siguen contaminados.

La pregunta de responsabilidad causal en Bhopal tiene tres dimensiones que el sistema puede analizar con precisión: la

responsabilidad de la filial india (Union Carbide India Limited, UCIL, operadora directa de la planta), la responsabilidad de la casa matriz estadounidense (Union Carbide Corporation, UCC, que diseñó la tecnología y aprobó los estándares de seguridad rebajados), y la responsabilidad del gobierno indio (que en su interés por atraer inversión extranjera había permitido el asentamiento de barrios de trabajadores a metros de la planta y había presionado para que la planta usara tecnología más barata). Los tres nodos contribuyeron causalmente al resultado. El sistema que siguió al accidente —el litigio internacional más complejo de la historia ambiental— nunca distribuyó la responsabilidad con precisión proporcional al peso causal de cada uno.

El segundo caso de este capítulo —Chevron-Ecuador— produce el límite más importante del método de imputación causal. En la Amazonia ecuatoriana, Texaco (adquirida por Chevron en 2001) operó pozos de petróleo entre 1964 y 1992 y abandonó miles de piscinas de desechos tóxicos que contaminaron el suelo y el agua de una región de la selva con alta densidad de comunidades indígenas. Veinte años de litigios produjeron una sentencia ecuatoriana de $9,500 millones contra Chevron y una sentencia estadounidense que la declaró producto de fraude procesal. Los detalles del caso son complejos. Pero la pregunta metodológica que el caso plantea es más importante: cuando hay múltiples fuentes de contaminación que operaron durante décadas en la misma área, ninguna de las cuales es por sí sola condición necesaria y suficiente del daño total, ¿cómo se distribuye la responsabilidad causal?

Este capítulo tiene una estructura diferente a los anteriores en su parte final: no solo aplica el método, sino que desarrolla explícitamente su límite y su extensión. El límite es la causalidad difusa acumulativa: el daño ecológico de largo plazo producido por múltiples actores sin que ninguno sea condición necesaria y suficiente. La extensión

### es el valor de Shapley: el instrumento de la teoría de juegos cooperativos que distribuye correctamente la responsabilidad en ese escenario.

### 1.1 La singularidad ontológica del daño ecológico

### El daño ecológico tiene cuatro características que lo distinguen de todos los dominios anteriores del libro y que determinan los instrumentos adecuados para su análisis:

Característica Descripción Consecuencia para el análisis

Difusión temporal

El daño ecológico se acumula a lo largo de décadas o siglos. Los efectos pueden manifestarse mucho después de que la causa dejó de operar.

El grafo causal debe incluir nodos históricos que ya no operan. La distancia temporal entre causa y efecto complica la atribución causal directa.

Difusión espacial

Los contaminantes se dispersan por agua, aire y suelo cruzando fronteras jurisdiccionales. El punto de medición del daño puede estar lejos del punto de emisión.

El R* de un nodo emisor puede calcularse aun cuando el daño ocurrió en otra jurisdicción, pero requiere modelado de la dispersión.

Causalidad acumulativa

El daño es frecuentemente el resultado de la acumulación de contribuciones de múltiples actores, sin que ninguno de ellos sea por sí solo

El postulado de la condición necesaria del sistema no se cumple para ningún actor individual. Aquí es donde R* falla y Shapley es necesario.

condición necesaria y suficiente.

ΔT_trayectoria es el componente dominante del daño ecológico de largo plazo. La incertidumbre sobre el horizonte temporal de la recuperación introduce rangos amplios en el cálculo.

Irreversibilidad parcial

Algunos daños ecológicos son permanentes o requieren siglos para recuperarse. La pérdida de biodiversidad y el cambio climático tienen componentes irreversibles.

### 1.2 Cuándo el método funciona y cuándo necesita extensión

El método de imputación causal basado en R* funciona correctamente cuando al menos un actor tiene una posición de "condición necesaria" en el grafo: el daño no habría ocurrido (o habría sido sustancialmente menor) sin ese actor. Bhopal cumple esa condición: sin la filial UCIL y sin la casa matriz UCC, la planta no habría existido en esa forma. El análisis de R* es directamente aplicable.

El método necesita extensión cuando el daño es acumulativo y ningún actor es condición necesaria individualmente: incluso si ese actor hubiera eliminado completamente sus emisiones, el daño habría ocurrido de todas formas por la suma de las emisiones de los demás. Chevron-Ecuador se aproxima a ese escenario: había múltiples operadores de petróleo en la región, y la contaminación es el resultado de la acumulación de las operaciones de varios de ellos durante décadas.

⊘ Límite del método:  El límite del postulado de la condición necesaria: cuando hay n actores y el daño D ocurre si y solo si la suma de sus contribuciones supera un umbral θ,

pero ningún actor individual supera θ, entonces dD/dNᵢ = 0 para todo i. El postulado I5 no se cumple para ningún nodo y el vector R* convencional asigna cero a todos los actores, lo que es evidentemente incorrecto. Este es el límite más importante del método y el que justifica la extensión mediante valores de Shapley.

Valor de Shapley φᵢ:  La distribución justa de la responsabilidad en un problema de causalidad acumulativa, calculada como la contribución marginal promedio de cada actor sobre todas las posibles coaliciones de actores. φᵢ mide "cuánto añade el actor i a la contaminación total, en promedio, cuando se une a cada subconjunto posible de los otros actores". Es la extensión de R* para el caso en que ningún actor es condición necesaria individualmente.

## §2. Página puente — Traducción al lenguaje ambiental y ecológico

Esta página resume las herramientas en el contexto del daño ambiental, la ecología y el litigio climático. El lector con formación en derecho ambiental, ecología o economía ambiental puede comenzar aquí.

Herramienta En medio ambiente se llama

Qué significa

Grafo causal G

Red causal del daño ecológico

El mapa de todos los actores, condiciones y factores que contribuyeron causalmente al daño ambiental: la empresa operadora, la casa matriz, el regulador, las condiciones del entorno, el contexto de desarrollo económico.

R* (vector) Contribución causal al daño

La fracción del daño ambiental causalmente atribuible a cada actor. Aplicable cuando al menos un actor es condición necesaria del daño. En daños de contaminación puntual (Bhopal), R* es el instrumento correcto.

Valores de Shapley φᵢ

Contribución marginal promedio en causalidad acumulativa

La extensión de R* para daños acumulativos donde ningún actor es condición necesaria individualmente. φᵢ distribuye la responsabilidad

proporcional a la contribución marginal de cada actor sobre todas las posibles coaliciones. Se usa cuando R* convencional falla.

S del operador

Fungibilidad del contaminador

S alto: cualquier empresa con la misma capacidad y bajo el mismo marco regulatorio habría generado el mismo daño. El problema es del marco normativo, no de ese contaminador específico. S bajo: las prácticas específicas de ese contaminador eran condición necesaria del daño.

α del contaminador

Grado de remediación y prevención implementado

Las medidas que el contaminador tomó para prevenir o remediar el daño: tecnologías más limpias, tratamiento de residuos, planes de contingencia, remediación de suelos. α = 0: ninguna medida.

Δ del contaminador

Déficit de remediación

La brecha entre la contribución causal al daño y la remediación implementada. Δ positivo es la base para la acción de responsabilidad ambiental y para las órdenes de remediación proporcionales.

D_total ambiental

Daño ecológico integral

T_invertido (daño inmediato: muertes, destrucción de hábitat, contaminación del suelo y agua), T_impedido (pérdida de servicios ecosistémicos durante el período de

contaminación activa), ΔT_trayectoria (pérdida permanente de biodiversidad, daño irreversible al sistema ecológico).

D_vital ecológico

Daño en tiempo de vida de las comunidades afectadas

La misma fórmula del Capítulo 1: D_vital = D_total / w_ref. Cuando el daño ambiental afecta la salud de comunidades, sus costos de salud, su esperanza de vida y sus medios de subsistencia son tiempo de vida cristalizado que el sistema de imputación causal cuantifica.

El nivel de contaminación acumulada por encima del cual el daño se manifiesta. En causalidad acumulativa, el daño ocurre cuando la suma de contribuciones supera θ. Ningún actor individual supera θ pero la suma sí.

Umbral de daño θ

Umbral de acumulación de contaminación

Para el lector que viene del núcleo universal:  Este capítulo tiene la estructura más compleja del libro porque incluye dos instrumentos que los anteriores no usaron juntos: R* convencional para Bhopal (donde el postulado de la condición necesaria se cumple) y valores de Shapley para Chevron-Ecuador (donde no se cumple). El §5 desarrolla el límite del método con precisión y el §6 desarrolla la extensión Shapley formalmente.

## §3. Las herramientas en el dominio ambiental

### 3.1 El grafo causal del daño ambiental: cuatro niveles

### El grafo del daño ambiental tiene una estructura de cuatro niveles que incluye tanto actores humanos como condiciones ecológicas del sistema afectado:

Nivel Tipo de nodo Función causal

Ejemplo (Bhopal)

Operador directo

La empresa que opera la fuente de contaminación.

Causa inmediata del daño. R* alto cuando es condición necesaria. S mide si cualquier otra empresa en las mismas condiciones habría actuado igual.

UCIL: operó la planta con estándares de seguridad debajo del nivel aprobado originalmente.

Diseñador / casa matriz

La empresa que diseñó la tecnología y aprobó los estándares.

R* del nodo de diseño. En la mayoría de los desastres industriales, la casa matriz tiene R* comparable o mayor que la filial operadora.

UCC: diseñó la tecnología, estableció los estándares de seguridad y aprobó las reducciones de costo que resultaron en estándares más bajos.

Regulador / gobierno

El Estado que autorizó la operación y reguló las condiciones de seguridad.

R* positivo cuando el regulador aprobó condiciones de operación que el sistema no debería haber tolerado, o cuando la omisión de inspección fue condición del daño.

Gobierno indio: asentó comunidades cercanas a la planta, presionó para bajar costos de operación, no inspeccionó las condiciones de seguridad.

Ecosistema receptor

Las condiciones del medio ambiente que determinaron la dispersión y el impacto del contaminante.

No tiene R* en el sentido de responsabilidad (no es un actor), pero sus condiciones son parte del grafo causal: determinan la magnitud del daño dado el nivel de emisión.

Dirección del viento, densidad de población circundante, características del suelo para la absorción del gas.

### 3.2 R* en el dominio ambiental: la filial vs. la casa matriz

Uno de los debates más importantes del derecho ambiental internacional es la responsabilidad de las casas matrices de empresas multinacionales por el daño causado por sus filiales en otros países. El cálculo de R* permite resolver ese debate con precisión cuando el grafo causal está bien construido.

La condición para que la casa matriz tenga R* positivo es que sus decisiones sean condición causal del daño: si la filial no hubiera podido operar de esa manera sin la tecnología, los estándares o los recursos de la casa matriz, entonces la casa matriz es un nodo del grafo con arista hacia el resultado dañino.

R*_casa_matriz > 0 ⟺ sin las decisiones de la casa

matriz,

el daño no habría ocurrido o habría sido

menor

La distinción entre el daño producido por la filial operando dentro de los estándares aprobados por la casa matriz y el daño producido por la filial operando por debajo de esos estándares es crucial para el análisis:

•  Si la filial operaba dentro de los estándares aprobados por la casa matriz y de todas formas ocurrió el daño: R* de la casa matriz es alto por el diseño de los estándares. •  Si la filial operaba por debajo de los estándares aprobados y la casa matriz no supervisó: R* de la casa matriz es moderado por la omisión de supervisión. •  Si la filial operaba por debajo de los estándares aprobados y la casa matriz lo sabía y no actuó: R* de la casa matriz es alto por la omisión deliberada.

### 3.3 El índice de sustituibilidad S en el daño ambiental

En el dominio ambiental, S del contaminador tiene implicaciones directas para el tipo de regulación más eficiente:

•  S alto del contaminador: cualquier empresa con la misma tecnología disponible y bajo el mismo marco

regulatorio habría generado el mismo daño. El problema no es esa empresa en particular: es el marco regulatorio que lo permitía. La reforma debe ser normativa (cambiar los estándares del sector) más que orientada a ese contaminador específico. •  S bajo del contaminador: las prácticas específicas de esa empresa —sus reducciones de costos, sus omisiones de mantenimiento, sus decisiones de localización— eran causalmente determinantes. La regulación puede focalizarse en esa empresa y en su comportamiento idiosincrático.

La combinación R*_contaminador × (1 − S) produce la responsabilidad causal neta del contaminador, que es la base técnica para la cuantificación de la orden de remediación:

Orden_remediación_proporcional_i = R*ᵢ × (1 − Sᵢ) ×

D_total

### 3.4 El daño ambiental integral y los servicios ecosistémicos

El D_total en el dominio ambiental incluye tres componentes que en los dominios anteriores están presentes pero que aquí adquieren su mayor escala:

Componente En daño ambiental

Cómo se cuantifica

T_invertido Daño inmediato: muertes, lesiones, destrucción de activos naturales, contaminación de suelo y agua en el momento del evento.

Inventario de daños documentados, costo de atención médica de urgencia, pérdida inmediata de medios de subsistencia. Para accidentes industriales: 

sumas calculables con evidencia documental.

T_impedido Pérdida de servicios ecosistémicos durante el período de contaminación activa: agua potable, suelo cultivable, recursos pesqueros, ecoturismo.

Valoración económica de los servicios ecosistémicos perdidos por año multiplicada por el período de contaminación activa. Métodos: costo de reemplazo, preferencia revelada, valoración contingente.

ΔT_trayectoria Pérdida permanente de biodiversidad, daño irreversible a los ecosistemas, reducción permanente de la esperanza de vida de la comunidad afectada.

Estudios epidemiológicos de largo plazo, modelos de recuperación ecológica con y sin remediación, diferencial de esperanza de vida entre la comunidad afectada y una comparable sin exposición.

Principio ecológico:  Los servicios ecosistémicos son tiempo de vida cristalizado de las comunidades que dependen de esos ecosistemas para subsistir. Cuando una comunidad agrícola pierde su suelo cultivable durante una década por un derrame tóxico, cada año de pérdida de cosecha es trabajo no recompensado y subsistencia no posible. D_vital = D_total / w_ref captura esa dimensión: el daño ambiental siempre es también un daño a la economía del tiempo de vida de las comunidades afectadas.

### 3.5 La extensión Shapley: cuando R* convencional falla

El valor de Shapley fue desarrollado por Lloyd Shapley en 1953 en el contexto de la teoría de juegos cooperativos para distribuir justa y eficientemente la ganancia de una coalición

entre sus miembros. Su aplicación a la distribución de responsabilidad en daños acumulativos es directa: en lugar de distribuir una ganancia, distribuye un daño.

Formalmente, sea N = {1, 2, ..., n} el conjunto de actores contaminadores y sea v(S) la función de valor de la coalición: el daño que produciría la coalición S de actores si operaran juntos (con sus contribuciones conjuntas). El valor de Shapley de actor i es:

φᵢ = Σ_{S⊆N\{i}} [ |S|! (n-|S|-1)! /n!] × [v(S∪{i}) −

v(S)]

Interpretación intuitiva: φᵢ es la contribución marginal promedio del actor i, calculada sobre todas las posibles coaliciones que podría unirse. ¡El factor [|S|! (n-|S|-1)! /n!] es el peso asignado a cada coalición de tamaño |S|, que garantiza que todos los órdenes de llegada sean igualmente probables.

Extensión Shapley:  Los valores de Shapley tienen cuatro propiedades que los hacen la distribución más justa para daños acumulativos: (1) Eficiencia: Σᵢ φᵢ = v(N) — la suma de todas las responsabilidades individuales iguala el daño total. (2) Simetría: actores con la misma contribución marginal en todas las coaliciones reciben la misma φ. (3) Nulo: un actor que no añade nada a ninguna coalición tiene φ = 0. (4) Aditividad: si hay dos problemas de daño independientes, la responsabilidad total es la suma de las responsabilidades en cada problema.

## §4. Casos resueltos

Caso A — Bhopal, India (2-3 diciembre 1984)

R* de la filial UCIL, de la casa matriz UCC, y del gobierno indio. El litigio ambiental más complejo de la historia hasta ese momento

A.1 El contexto histórico

La planta de Union Carbide en Bhopal producía Sevin, un pesticida ampliamente usado en la agricultura india. El proceso de producción usaba isocianato de metilo (MIC), un gas altamente tóxico, como intermediario. En su diseño original, la planta incluía sistemas redundantes de seguridad: un refrigerante que mantenía el MIC en estado líquido y menos reactivo, un sistema de neutralización con hidróxido de sodio, y una antorcha de quemado de emergencia.

En los meses previos al accidente, por razones de reducción de costos, todos esos sistemas habían sido comprometidos: el refrigerante había sido desconectado para ahorrar en costos operativos, el sistema de neutralización no estaba funcionando adecuadamente, y la antorcha de quemado había sido apagada para mantenimiento. Cuando el agua entró al tanque de MIC —ya sea por accidente o por sabotaje, según versiones distintas— la reacción química fue incontrolable.

El litigio que siguió fue uno de los más complejos de la historia del derecho ambiental. Union Carbide Corporation (la casa matriz estadounidense) argumentó que UCIL (la filial india) era una entidad legalmente separada y que las decisiones operativas de la planta eran responsabilidad de la gestión india. El gobierno indio, por su parte, enfrentaba la acusación de haber permitido el asentamiento de comunidades cercanas a la planta y de haber presionado

para que la tecnología fuera localizada con menor costo. La resolución judicial fue un acuerdo de $470 millones en 1989 que muchos consideraron insuficiente. Dos de los directivos de UCIL fueron condenados en 2010 a dos años de prisión —veintiséis años después del accidente.

### A.2 El grafo causal de Bhopal

Nodo Actor/Factor Tipo Función causal en el accidente

N1 Union Carbide Corporation (UCC), casa matriz EE.UU.

Diseño del sistema y estándares

Diseñó la tecnología de producción con MIC. Estableció los estándares de seguridad originales (que incluían los sistemas redundantes). Aprobó o no impidió las reducciones de costo que comprometieron esos sistemas. R* alto con S moderado-bajo.

N2 Union Carbide India Limited (UCIL), filial india

Operación y mantenimiento

Operó la planta con los sistemas de seguridad comprometidos. Tomó las decisiones de apagar el refrigerante y la antorcha de quemado. Nodo de ejecución con posición causal alta.

N3 Gobierno indio: permisos y decisiones de localización

Marco regulatorio y decisiones de localización

Permitió el asentamiento de barrios de trabajadores a menos de un kilómetro de la planta. Presionó para que la tecnología fuera de menor costo. No inspeccionó las condiciones de seguridad de la planta.

N4 Decisiones de reducción de costo operativo

Nodo instrumental de decisión

La decisión específica de apagar el refrigerante y no reparar los sistemas de neutralización. Es tanto parte de N2 (quien tomó la decisión) como un nodo funcional separado en el grafo.

N5 Condiciones meteorológicas de esa noche

Factor ambiental

La dirección del viento, la temperatura y la humedad de la madrugada del 2-3 de diciembre determinaron que el gas se dispersara hacia los barrios más densamente poblados. S muy alto.

Nodo final No entra en el cálculo de R*.

Nf 500,000 afectados

### A.3 R*, S y la controversia UCC vs. UCIL

Nodo R* S α Interpretación y Δ

~38% 0.30 0.10 S moderado-bajo. Diseñó la tecnología con MIC y los estándares originales. Sin UCC, la planta no habría existido en esa forma. Δ = +0.28. UCC pagó $470M (subproporcional a su AD).

N1 — UCC (casa matriz)

~30% 0.55 0.08 S moderado. Cualquier operador bajo la misma presión de costos y con la misma supervisión laxa habría tenido incentivos similares, pero las decisiones específicas de UCIL tenían S moderado. Δ = +0.22.

N2 — UCIL (filial)

~18% 0.65 0.05 S moderado-alto. Las decisiones del gobierno indio reflejaban políticas de desarrollo industrial comunes en países en desarrollo en la época. Δ = +0.13.

N3 — Gobierno indio

~10% 0.45 0.00 Condición técnica directa: los sistemas comprometidos eran condición necesaria del accidente dado el fallo del tanque.

N4 — Reducción costos

~4% 0.92 0.00 S muy alto. Factor exógeno amplificador del daño.

N5 — Condiciones meteor.

### La conclusión más importante del análisis: UCC (la casa matriz estadounidense) tiene R* = 38% y pagó $470

millones en el acuerdo de 1989. Ese acuerdo representó aproximadamente $940 por víctima afectada —una fracción mínima del D_total proporcional a su responsabilidad causal. Su argumento de que UCIL era una entidad legalmente separada fue aceptado por los tribunales estadounidenses, pero en el análisis causal es irrelevante para la distribución del daño: la separación jurídica entre casa matriz y filial no elimina la arista causal entre UCC y el accidente.

La distribución del ajuste debitor proporcional al R*:

AD_N1 (UCC) = 0.38 × D_total

AD_N2 (UCIL) = 0.30 × D_total

AD_N3 (Gobierno indio) = 0.18 × D_total

A.4 El D_total de Bhopal en tiempo de vida

Parámetros:

•  Muertes directas documentadas: 3,787-7,575 (usamos 5,000 como estimación central). Edad promedio: 30 años. Esperanza de vida residual: ~47 años = 411,720 horas. •  Enfermos crónicos permanentes: ~120,000 personas con secuelas respiratorias, neurológicas y reproductivas permanentes. q_real promedio: 0.60 (pérdida del 40% de calidad de vida). •  Personas expuestas con daño documentado: ~500,000. Período de impacto agudo: promedio 3 años de síntomas persistentes. •  Pérdida de servicios ecosistémicos (suelo contaminado, agua contaminada) por 20+ años en la zona afectada. •  w_ref = $8 USD/hora PPP 2024.

D_vital_muertes = 5,000 × 411,720 h × 1.0 = 2.059 ×

10⁹ horas

D_vital_enfermos_crónicos = 120,000 × (47×8,760h)

× 0.40 = 1.978 × 10¹⁰ horas

D_vital_total ≈ 2.18 × 10¹⁰ horas

D_monetary_equiv ≈ $174,000M USD (2024)

Los $470 millones pagados por UCC representan el 0.27% del D_monetary_equiv proporcional. Incluso si se incluyen todas las compensaciones posteriores —los acuerdos adicionales del gobierno indio, los programas de salud— el total no supera el 0.5% del daño ontológico en tiempo de vida. J_Bhopal ≈ 0.08: injusticia estructural severa.

Caso B — Chevron-Ecuador (1964–2011 y posterior)

El caso límite: causalidad acumulativa y la extensión mediante valores de Shapley

B.1 El contexto y la complejidad

Entre 1964 y 1992, Texaco (adquirida por Chevron en 2001) operó pozos de petróleo en la Amazonia ecuatoriana en consorcio con la empresa estatal ecuatoriana Petroecuador. Al retirarse, Texaco acordó con el gobierno ecuatoriano un plan de remediación y supuestamente llevó a cabo parte de él. Los trabajos de remediación posteriores mostraron que grandes extensiones de contaminación permanecían sin tratar.

En 1993 se inició una demanda colectiva en nombre de aproximadamente 30,000 personas de comunidades indígenas afectadas. El litigio migró de los tribunales estadounidenses (donde Chevron argumentó que Ecuador era el foro adecuado) a los tribunales ecuatorianos (donde Chevron argumentó que el proceso estaba contaminado por fraude). En 2011, un tribunal de Ecuador emitió una sentencia de $9,500 millones contra Chevron. En 2014, un tribunal federal de los EE.UU. determinó que la sentencia ecuatoriana era producto de corrupción y fraude procesal y era inaplicable en los Estados Unidos.

Para el análisis de responsabilidad causal, la controversia sobre el proceso legal es secundaria. Lo que importa metodológicamente es la pregunta sustantiva: dado que había múltiples fuentes de contaminación (Texaco/Chevron, Petroecuador y las operaciones posteriores de terceros), dado que la contaminación se acumuló durante décadas, y dado que ninguna fuente individual es responsable del 100% de la contaminación documentada, ¿cómo se distribuye la responsabilidad?

B.2 Por qué R* convencional falla en este caso

El método de R* convencional requiere que al menos un actor sea condición necesaria del daño: que sin ese actor el daño no habría ocurrido. En el caso de Chevron-Ecuador, el escenario es más complejo:

•  Texaco/Chevron operó la región entre 1964 y 1992 y dejó contaminación documentada. •  Petroecuador continuó operando la región después de 1992 y también produjo contaminación. •  Operadores posteriores añadieron capas adicionales de contaminación. •  El daño documentado en comunidades es el resultado de décadas de acumulación de estas fuentes.

La pregunta causal no es "¿habría habido contaminación sin Texaco?" (sí, por las otras fuentes). Es "¿cuánto del daño total es causalmente atribuible a la contribución específica de Texaco/Chevron?". Esa es exactamente la pregunta que el valor de Shapley responde cuando R* convencional no puede hacerlo.

⊘ Límite del método:  El postulado I5 (dD/dN_Texaco ≠ 0) podría no cumplirse si sin Texaco el daño habría sido casi el mismo por las otras fuentes. En ese caso, R*_Texaco ≈ 0 aunque Texaco claramente contribuyó al daño. Este es el escenario que requiere la extensión Shapley: el valor de Shapley asigna a Texaco su contribución marginal promedio sobre todas las posibles coaliciones, no su contribución como condición necesaria única.

B.3 La extensión Shapley: aplicación al caso Chevron-Ecuador

Para aplicar los valores de Shapley al caso, se define la función de valor v(S) como el daño producido por la coalición S de actores: 

### Actores en el juego (simplificado a los tres principales):

•  Actor 1: Texaco/Chevron (1964-1992, ~18% del territorio afectado según estudios periciales). •  Actor 2: Petroecuador (1992-presente, operación continua, ~45% del territorio afectado). •  Actor 3: Operadores posteriores + contaminación difusa (fuentes menores, ~37% del territorio afectado).

### Función de valor v(S) basada en estudios periciales de superposición de contaminación:

Coalición S v(S) = daño producido

Justificación

v(∅) = 0 Sin ningún actor, no hay contaminación.

S = ∅ (ninguno)

S = {1} solo Texaco

v({1}) = 0.22 × D_total

La contaminación de Texaco por sí sola produciría aproximadamente el 22% del daño (solapamiento con otras fuentes eliminado).

S = {2} solo Petroecuador

v({2}) = 0.40 × D_total

Petroecuador opera más tiempo y más extensión, pero sobre parte del territorio ya contaminado por Texaco.

S = {3} otros operadores

v({3}) = 0.15 × D_total

Fuentes menores con menor extensión.

S = {1,2} v({1,2}) = 0.70 × D_total

La superposición de las dos fuentes principales produce un daño no aditivo: se amplifican mutuamente.

S = {1,3} v({1,3}) = 0.42 × D_total

Menor superposición entre Texaco y las fuentes menores.

S = {2,3} v({2,3}) = 0.58 × D_total

Petroecuador y fuentes menores se solapan en parte del territorio.

S = {1,2,3} (todos)

v({N}) = 1.00 × D_total

El daño total observado es la función del conjunto completo.

### Cálculo del valor de Shapley para el Actor 1 (Texaco/Chevron):

φ₁ se obtiene ponderando las contribuciones marginales por el tamaño de la coalición precedente:

φ₁ = (1/3)(0.22−0) + (1/6)(0.70−0.40) + (1/6)(0.42−0.15) + (1/3)(1.00−0.58)

= 0.07333 + 0.05000 + 0.04500 + 0.14000 = 0.30833.

### El valor de Shapley de Texaco/Chevron es φ₁ ≈ 0.308: aproximadamente el 30.8% del daño total. Este es el resultado que el litigio debería haber establecido como base

### para la responsabilidad de Chevron, independientemente de las controversias procesales.

### Valores de Shapley para los tres actores (verificación de eficiencia):

Actor φᵢ (Shapley)

Fracción del D_total

Contraste con R* convencional

Texaco/Chevron 0.308 30.8% R* convencional daría 0 si Texaco no es condición necesaria. Shapley da 30.8% por su contribución marginal real.

Petroecuador 0.478 47.8% Mayor porción porque opera más tiempo y más territorio.

Otros operadores

0.213 21.3% Menor porción, aunque conserva contribución marginal por el solapamiento con las dos fuentes principales.

Otros operadores

1.000 100% Propiedad de eficiencia de Shapley: la suma es exactamente el daño total.

Suma (verificación)

### La verificación de eficiencia confirma que los valores de Shapley suman exactamente el 100% del D_total —una propiedad que R* convencional comparte pero que aquí

tiene especial importancia porque hay actores cuya condición de necesidad individual no se cumple.

B.4 El argumento de Chevron y la respuesta del análisis causal

Chevron argumentó en el litigio que (a) había cumplido un plan de remediación acordado con el gobierno ecuatoriano antes de retirarse, (b) Petroecuador era responsable de la contaminación posterior, y (c) la sentencia ecuatoriana estaba contaminada por fraude. Los dos primeros argumentos tienen relevancia para el análisis causal.

Respecto al argumento (a): el valor de Shapley de Chevron (0.237) refleja su contribución marginal al daño total, no solo el daño en los sitios donde la remediación fue incompleta. Si la remediación acordada fue parcialmente efectiva, ese α_Chevron ≈ 0.25 reduce el Δ de Chevron:

Δ_Chevron = φ₁ − α_Chevron = 0.237 − 0.25 = −0.013

Un Δ ligeramente negativo significaría que Chevron asumió marginalmente más que su responsabilidad causal proporcional. Eso no significa que el daño está reparado — las otras fuentes siguen teniendo Δ positivo— sino que la responsabilidad residual de Chevron es muy pequeña comparada con la de Petroecuador (Δ_Petro = 0.488 − α_Petro).

Respecto al argumento (b): el análisis de Shapley confirma que Petroecuador tiene el mayor valor φ (0.488) y por tanto la mayor responsabilidad causal en el daño total. El análisis no exculpa a Chevron, pero sí redistribuye correctamente la carga entre los actores, a diferencia de la sentencia ecuatoriana que imputó el 100% a Chevron.

## §5. Los límites del método y su desarrollo explícito

Este capítulo es el lugar donde el sistema hace más visible lo que puede y lo que no puede hacer. Los límites que se describen aquí no son una crítica al sistema: son el mapa honesto de su alcance. Un sistema que no conoce sus límites no es honesto. Un sistema que los conoce y los nombra con precisión es más útil que uno que promete más de lo que puede dar.

### 5.1 Límite I: el postulado de la condición necesaria en causalidad acumulativa

Este es el límite más importante del libro. El postulado I5 establece que el nodo N_i es causalmente necesario para el daño D si dD/dN_i ≠ 0: si eliminar N_i del grafo cambiaría el daño. Cuando el daño es acumulativo y hay múltiples fuentes que cada una es marginal —el cambio climático es el ejemplo más grande y más claro— el postulado no se cumple para ninguna fuente individual y R* convencional asigna cero a todos los actores.

La extensión Shapley resuelve este límite en los casos donde la función de valor v(S) puede estimarse con datos suficientes. Pero tiene su propio límite: calcular φᵢ exactamente requiere evaluar 2ⁿ coaliciones posibles, lo que es computacionalmente prohibitivo para n grande. Los métodos de aproximación de Monte Carlo para φᵢ son la solución práctica (implementada en el código del §6).

⚠ El cambio climático es el caso donde el límite de la condición necesaria se manifiesta con mayor urgencia política. Ningún actor individual (ningún país, ninguna empresa emisora) es condición necesaria del cambio climático: incluso si ese actor eliminara completamente sus emisiones, el cambio

climático ocurriría de todas formas por la suma de las demás emisiones. R* convencional = 0 para todos. Shapley produce valores positivos para todos, proporcionales a su contribución marginal promedio. Los valores de Shapley son la base técnica para el diseño de compromisos climáticos equitativos.

### 5.2 Límite II: la incertidumbre en los datos de dispersión

El cálculo de R* y de los valores de Shapley en el dominio ambiental requiere estimar cuánto del daño observado es atribuible a cada fuente. En los daños de largo plazo (décadas de contaminación acumulada), esa atribución requiere modelos de dispersión que tienen incertidumbre inherente. El resultado del análisis debe siempre presentarse como un rango, no como un valor puntual. Un análisis de sensibilidad que muestre cómo cambia φᵢ bajo distintos supuestos de dispersión es parte del análisis bien hecho.

### 5.3 Límite III: la función de valor v(S) no siempre es estimable

El cálculo de los valores de Shapley requiere la función v(S): el daño producido por cada posible coalición de actores. En muchos casos reales, solo el daño del conjunto completo v(N) es observable (el daño total documentado), mientras que los daños de las coaliciones parciales deben estimarse con modelos contrafácticos. Esa estimación tiene incertidumbre que se propaga a los valores de Shapley calculados. Cuanto mayor es la incertidumbre sobre v(S) para las coaliciones parciales, mayor es el intervalo de confianza de φᵢ.

### 5.4 Límite IV: la irreversibilidad y la limitación de la compensación monetaria

Algunos daños ecológicos son irreversibles: la extinción de especies, la destrucción de ecosistemas únicos, el daño permanente a comunidades culturalmente arraigadas en un territorio. Para estos daños, D_monetary_equiv puede ser calculable pero la promesa de reparación monetaria es ontológicamente vacía: no hay cantidad de dinero que devuelva una especie extinta o un ecosistema único destruido. El sistema reconoce honestamente este límite: D_monetary_equiv no es lo que se debe pagar —es la medida de la magnitud del daño. Cuando esa magnitud supera cualquier capacidad de compensación, la fórmula no falla: cumple su función más importante, que es hacer visible la inconmensurabilidad entre el daño y cualquier reparación posible.

### 5.5 El alcance de Shapley: hasta dónde llega la extensión

Los valores de Shapley distribuyen correctamente la responsabilidad en la causalidad acumulativa bajo una condición implícita: que todos los actores de la coalición son comparables en sus mecanismos de contribución al daño. Cuando hay actores de tipos radicalmente distintos —una empresa que emite CO₂, un gobierno que no regula las emisiones, y un consumidor individual que compra el producto— los valores de Shapley producen una distribución que puede ser técnicamente correcta pero políticamente impráctica. La decisión de qué actores incluir en el juego es en sí misma una decisión normativa con R* real.

## §6. Profundización formal

### 6.1 La función de valor característica y sus propiedades

En teoría de juegos, una función de valor v: 2^N → ℝ es superaditiva si v (S ∪ T) ≥ v(S) + v(T) para coaliciones disjuntas S, T. En el contexto del daño ambiental acumulativo, la función de valor es frecuentemente superaditiva porque los contaminantes de distintas fuentes se amplifican mutuamente en el ecosistema receptor: la toxicidad combinada puede ser mayor que la suma de las toxicidades individuales.

Si v es superaditiva, los valores de Shapley distribuyen más responsabilidad a los actores que más amplifican las contribuciones de los otros. Si v es subaditiva (las fuentes de contaminación interfieren entre sí o se diluyen), los valores de Shapley distribuyen menos responsabilidad que la aditiva simple.

La condición de eficiencia de Shapley (Σᵢ φᵢ = v(N)) garantiza que, independientemente de si v es superaditiva o subaditiva, la suma de las responsabilidades individuales asignadas por Shapley es exactamente igual al daño total observable. Esto es la propiedad más importante para el litigio ambiental: no hay "daño no atribuido" ni "sobreatribución".

### 6.2 La relación entre R* y φ cuando el postulado I5 se cumple

Cuando el postulado de la condición necesaria se cumple para al menos un actor, R* y φ son coherentes, pero no idénticos. En ese caso, φᵢ converge a R*ᵢ cuando la función de valor es aditiva (v(S) = Σᵢ∈S v({i})) y las contribuciones marginales son constantes. Cuando la función de valor tiene interacciones (superaditiva o subaditiva), φᵢ y R*ᵢ pueden diferir porque Shapley captura los efectos de interacción entre actores que R* no captura.

En la práctica, para los casos donde el postulado I5 se cumple claramente (Bhopal, el Challenger, el fraude de Enron), R* es más eficiente computacionalmente y produce resultados igualmente interpretables. Para los casos donde el postulado I5 falla (Chevron-Ecuador, cambio climático), Shapley es el instrumento correcto y R* produce resultados incorrectos (φ = 0 cuando debería ser > 0).

### 6.3 Aproximación de Shapley por Monte Carlo

El cálculo exacto de los valores de Shapley requiere evaluar 2ⁿ − 1 coaliciones, lo que es impracticable para n > 20. La aproximación por Monte Carlo produce estimaciones con incertidumbre controlable:

φᵢ ≈ (1/m) × Σ_{k=1} ^{m} [v (S_k ∪ {i}) − v(S_k)]

donde S_k es una muestra aleatoria de las posibles coaliciones sin el actor i. Con m = 10,000 simulaciones, el error estándar del estimador de Monte Carlo es típicamente inferior al 2% del valor verdadero, suficiente para el análisis legal y regulatorio.

### 6.4 Especificación operativa

Las magnitudes y relaciones desarrolladas en este capítulo quedan determinadas por las definiciones, ecuaciones y criterios de interpretación expuestos en las secciones anteriores. La especificación operativa reúne esas relaciones en una secuencia única de cálculo, de modo que los datos del caso puedan transformarse en los indicadores correspondientes.

Para la aplicación sistemática se emplean las convenciones de entrada, normalización y salida descritas en el Apéndice D. El resultado se expresa en los mismos términos conceptuales del capítulo: posición causal, sustituibilidad, déficit de asunción, daño y prioridad de intervención.
