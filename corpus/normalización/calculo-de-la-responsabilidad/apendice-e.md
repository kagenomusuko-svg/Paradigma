# APÉNDICE E Glosario unificado por

## Todos los términos del sistema con su traducción en cada dominio de aplicación Este glosario contiene todos los términos del sistema de imputación causal organizados en dos secciones: primero los términos del núcleo universal (que aplican a todos los dominios), y luego los términos específicos de cada dominio. Para cada término se indica el símbolo matemático cuando existe, la definición operativa, y el capítulo donde aparece por primera vez. ▌ Núcleo Término Símbolo Definición operativa AD = R*ᵢ × D_total El monto o la acción que el nodo i debería asumir en proporción a su peso causal en el daño total. No es el monto de la multa ni el de la condena: es el cálculo de la responsabilidad proporcional a la posición causal. Ajuste debitor (AD) Alpha (α) α ∈ [0,1] Coeficiente de asunción de la responsabilidad causal. α = 0: el nodo no asumió nada. α = 1: asumió completamente su posición causal. En el dominio histórico, α_diferido es la asunción por parte de sucesores institucionales. B_total — Beneficio total obtenido por un actor como consecuencia causal del evento. En tanatología, B_total = 0 por definición ontológica. En el resto de los dominios, B_total incluye G_inmediato + G_acumulado + ΔG_trayectoria. D_total D = T_inv + T_imp + ΔT Daño total causado por el evento. Suma de T_invertido (pérdida directa), T_impedido (oportunidades negadas) y ΔT_trayectoria (diferencial permanente de potencial). D_vital D_vital = D/w_ref El daño total expresado en horas de vida de trabajo cristalizado. w_ref es el salario de referencia por hora en PPP. Convierte el daño monetario en tiempo de vida, la unidad ontológica fundamental del sistema. Delta (Δ) Δ = R* − α Déficit de responsabilidad causal no asumida. Δ > 0: el actor causó más de lo que asumió (base para el ajuste debitor). Δ < 0: el actor asumió más de lo que causó (chivo expiatorio o acción extraordinaria). Delta_B (Δ_B) Δ_B = B_total − α_B Déficit de asunción del beneficio obtenido. Base para la acción de enriquecimiento sin causa. Cuando Δ_B > 0, el actor obtuvo beneficio del evento sin haber reconocido su posición causal. Ego(t) Ego(t) = ∫φ(s)dμ La integral de los colapsos asumidos por el sujeto hasta el tiempo t. En la muerte, la integral se cierra produciendo el ego final inmodificable. En el Aego, la integral se detiene sin que el sujeto haya muerto. Grafo causal G G = (N, A, w) El mapa de nodos (actores, estructuras, instrumentos) y aristas ponderadas que representan las dependencias causales entre ellos. Base del análisis de R* en todos los dominios. J = 1 − Σ|Δᵢ| Medida de ecuanimidad en la distribución de responsabilidad y asunción. J = 1: distribución perfecta Índice de Justicia Estructural (J) (cada nodo asumió exactamente su R*). J = 0: distribución completamente desequilibrada. J < 0: distribución inversa a la causal. r_D = (I − Q_D)⁻¹ b_D Operador de responsabilidad El procedimiento de cálculo de R* conforme al método vigente: separar los ancestros causales de D del nodo sumidero, construir la submatriz Q_D y el vector b_D de determinaciones directas, resolver r_D = (I − Q_D)⁻¹ b_D, y normalizar R*(D) = r_D / (1ᵀ r_D). El operador espectral asociado es M_R(D) = Q_D + η_D b_D 1ᵀ, cuyo eigenvector dominante es R*. Para grafos DAG (acíclicos), Q_D es nilpotente y la solución es exacta. Nodo de diseño — El actor que diseñó las condiciones bajo las cuales el evento dañino era posible. Tiene el mayor INCF o R* en la mayoría de los análisis y la S más baja (sus características específicas eran condición idiosincrática del resultado). Postulado I5 dD/dNᵢ ≠ 0 El postulado de la condición necesaria: el nodo Nᵢ es causalmente necesario para el daño D si eliminar Nᵢ del grafo cambia D. Cuando I5 no se cumple para ningún nodo individual (causalidad acumulativa), se requiere la extensión Shapley. R* (R-estrella) R*(D) = r_D /

Z_D

El vector de distribución estable de la responsabilidad causal entre los nodos ancestros de D. R*ᵢ(D) es la proporción del resultado causalmente atribuible al nodo i: el porcentaje estable al que converge la atribución causal del nodo i respecto de D. La suma de todos los componentes es 1. Se obtiene mediante r_D = (I − Q_D)⁻¹ b_D y normalización Z_D = 1ᵀ r_D. R* es el eigenvector dominante del operador de responsabilidad M_R(D), con eigenvalor λ₁ = 1.

S ∈ [0,1] Índice de fungibilidad del nodo en el resultado. S = 0: el nodo es completamente idiosincrático (su contribución es única). S = 1: cualquier nodo equivalente habría producido el mismo resultado. R* × (1−S) = responsabilidad causal neta.

S (sustituibilidad)

τ(M) = M/w_ref — La fórmula de conversión de dinero a tiempo de vida. M es el monto monetario, w_ref es el salario de referencia por hora. Permite expresar cualquier daño o beneficio económico en horas de vida cristalizada.

Valor de Shapley (φᵢ)

φᵢ = Σ [|S|!(n-|S|-1)!/n!]×[v(S∪{i})−v(S)] La extensión del R* para casos de causalidad acumulativa donde el postulado I5 no se cumple para ningún nodo individual. Mide la contribución marginal

promedio de cada actor sobre todas las coaliciones posibles. Propiedad de eficiencia: Σφᵢ = v(N).

### ▌ Hijos

Término Símbolo Definición operativa

Anteros — El hijo de Afrodita que describe la afirmación de sí mismo contra el mundo o contra la norma. El personaje que actúa desde su propia convicción. En exceso sin Harmonía: produce transgresión deliberada. En los directivos: dolo probable.

Deimos — El hijo de Afrodita que describe la parálisis ante la multiplicidad de lo que enfrenta el sujeto. La incapacidad de actuar por la amplitud de lo que está en juego. En los directivos: negligencia por vértigo ante la complejidad.

Eros — El hijo de Afrodita que describe la orientación activa hacia algo nuevo o deseado en el presente. En el duelo: la señal de que el doliente comienza a abrirse hacia la vida sin sentir traición. En los directivos: la disposición hacia el crecimiento genuino.

Fobos — El hijo de Afrodita que describe la acción desde el miedo a las consecuencias. El sujeto que hace lo que no quiere para evitar un daño. En los operadores: compatibilidad con presión sistémica sin dolo. En los directivos: culpa habitual con menor responsabilidad subjetiva.

Harmonía — El hijo de Afrodita que describe la deliberación plena. El sujeto que ha integrado la información disponible y actúa desde esa integración. En los análisis: el estándar de la decisión bien tomada.

Anteros + Harmonía = afirmación deliberada.

Potós — El hijo de Afrodita que describe el anhelo hacia lo ausente o perdido. El vector de voluntad apuntando hacia lo que ya no está disponible. En el duelo: fase normal del proceso. En los directivos: persistencia en el sistema heredado sin revisión crítica.

### ▌ Ingeniería

Término Símbolo Definición operativa

INCF = R*

El R* aplicado al análisis de fallos de ingeniería. Mide la fracción del fallo sistémico causalmente atribuible a cada nodo. El INCF del componente físico que "causó" el accidente típicamente es menor al 20%; el INCF de los nodos organizacionales domina.

INCF (Índice de Necesidad Causal del Fallo)

### ▌ Finanzas

Término Símbolo Definición operativa

ICRS = R*

El R* aplicado al análisis de riesgo sistémico y quiebra. Mide cuánto del colapso sistémico dependía causalmente de cada nodo. Formaliza el "too big to fail" como ICRS alto, no como tamaño grande.

ICRS (Índice de Concentración de Riesgo Sistémico)

### ▌ Ingeniería/Histórico

Término Símbolo Definición operativa

IAS = J_post − J_pre

IAS (Índice de Aprendizaje Sistémico)

Mide en qué medida el sistema incorporó las lecciones de un evento previo en su diseño posterior. IAS > El Cálculo de la Responsabilidad · Apéndices

0: aprendizaje real. IAS ≈ 0: sin aprendizaje. IAS < 0: el sistema se volvió más injusto después del evento.

### ▌ Corporativo

Término Símbolo Definición operativa

IIC = corr(valores_decl, comp_obs)

Mide la congruencia entre los valores declarados de una institución y su comportamiento observable. IIC ∈ [0,1]. IIC < 0.30: disforia de identidad corporativa severa. Calculable por terceros con información pública.

IIC (Índice de Integridad Corporativa)

### ▌ Histórico/Corporativo

Término Símbolo Definición operativa

α_diferido — La asunción de responsabilidad causal por parte de sucesores institucionales del actor histórico que ya no puede asumir. Aplica en el dominio histórico (el Estado belga respecto al Congo, los EE.UU. respecto al redlining) y en el corporativo (cuando la institución reconoce el diseño defectuoso décadas después).

### ▌ Ontológico

Término Símbolo Definición operativa

— El campo del ego colectivo que ha acumulado tanta densidad que determina la trayectoria de los individuos sin que ninguno lo haya diseñado explícitamente.

Aego-Damasén

La cultura corporativa como Aego-Damasén produce el Dieselgate: no por dolo individual sino por el campo que hace que la solución prohibida sea la más obvia.

— El ego colectivo que opera activamente para impedir que los individuos que operan dentro de él ejerzan su propio eje. El Estado que usa la disforia de identidad para que el soberano no reconozca la asimetría del contrato fiscal.

Aego-Peribea

— La condición del ego (individual o colectivo) cuya imagen de sí mismo no corresponde a lo que realmente es. En el ego colectivo corporativo: la institución que declara valores de integridad y actúa consistentemente en su contra. IIC bajo es la medida cuantitativa de la disforia de identidad corporativa.

Disforia de identidad

— La paradoja del sujeto que enfrenta dos umbrales θ simultáneamente incompatibles: el umbral de la acción necesaria para su supervivencia y el umbral del costo que esa acción le exige. En el Caso Eje: defender el proceso requiere más recursos de los que el proceso mismo dejó disponibles.

Dilema de Aquiles

### ▌ Ontológico/Jurídico

Término Símbolo Definición operativa

— El incumplimiento por parte de un ente con poder institucional de las condiciones materiales de posibilidad que prometió o que su posición requería proveer. En el contrato fiscal: el Estado que recibe el capital ciudadano y no genera las condiciones de desarrollo prometidas. En el laboral: la institución que diseña la trampa y culpa al empleado por caer en ella.

Fraude annona

### ▌ Deportes/Beneficio

Término Símbolo Definición operativa

R*_B R*_B = eigenvector dom.(W_beneficio)

El R* aplicado al análisis de contribución al beneficio (triunfo deportivo, resultado positivo). Mide la fracción del resultado positivo causalmente atribuible a cada jugador o factor. Es el instrumento de la negociación salarial basada en contribución causal, no en comparación de mercado.

### ▌ Deportes

Término Símbolo Definición operativa

CI = R*_B × (1−S_B)

La fracción del resultado deportivo causalmente atribuible al jugador específico y no reproducible por ningún otro. CI = 0: el triunfo habría ocurrido de la misma forma sin ese jugador. El número correcto para la negociación salarial.

CI (Contribución Idiosincrática)

### ▌ Literatura

Término Símbolo Definición operativa

— El personaje de una obra ficcional que diseñó las condiciones del evento central del relato sin estar necesariamente presente en él. Tiene el mayor R* narrativo con S más baja. Tywin Lannister en La Boda Roja. El autor mismo como meta-nodo de segundo nivel.

Nodo narrativo de diseño

arco(t) = {pⱼ(t)}

Arco narrativo

La secuencia de distribuciones de hijos de un personaje a lo largo del tiempo del relato. El arco de Raskolnikov: Anteros → Fobos → Harmonía. La secuencia que el

sistema ontológico predice para la transformación auténtica del sujeto que actuó sin deliberación y encontró la realidad.

### ▌ Histórico

Término Símbolo Definición operativa

S_hist = 1 − |P(E|con) − P(E|sin)|

La sustituibilidad histórica del detonador de un evento histórico. S_Princip ≈ 0.92 en la Primera Guerra Mundial: el sistema habría encontrado otra chispa. S_alto del detonador implica que el nodo de diseño estructural tiene mayor R*.

S histórica

### ▌ IA/Crédito

Término Símbolo Definición operativa

DI = P(neg|grupo_A)/P(neg|grupo_B)

El ratio de denegación entre grupos protegidos y no protegidos. DI > 1.25: umbral regulatorio estándar de discriminación estadística. R*_dataset = (DI_observado − 1) / DI_observado mide la fracción del disparate impact causalmente atribuible al dataset histórico.

DI (Disparate Impact)

### ▌ Seguros

Término Símbolo Definición operativa

PAC = P(sin) × E[D] × R*_as × (1−S_as)

La prima de seguro que refleja únicamente la contribución causal idiosincrática del asegurado al riesgo. La prima que excede este umbral transfiere el costo del riesgo estructural (causado por el regulador o el entorno) al asegurado que no lo causó.

Prima Actuarial Justa (PAC)

Miguel Hilario Olvera Aguilar Centro Multidisciplinario Meriadock Formación y Asesoría A.C., 2026
