## Prólogo

El problema, el sistema y su estatus

## I. El problema

Los sistemas de imputación causal —jurídicos, institucionales,
regulatorios— asignan consecuencias basándose en visibilidad
y apariencia. El actor que ejecutó el acto visible es el que el
expediente menciona; el actor que diseñó el sistema que hizo
ese acto inevitable está documentalmente ausente o
subrepresentado. Bajo condiciones estructurales específicas,
este mecanismo produce una inversión sistemática: el nodo
que más causó asume menos, y el nodo que menos causó
asume más.
El problema no es de mala intención. Los sistemas
convencionales de imputación funcionan bien cuando hay un
único actor, un acto directo y un resultado claro. Cuando el
sistema involucra jerarquías, protocolos, diseño institucional y
ejecutores intercambiables, la imputación basada en visibilidad
produce resultados que se alejan sistemáticamente de la
distribución causal real. La discrepancia no es pequeña ni
aleatoria: es estructural y predecible.
Este libro construye un sistema formal para describir esa
discrepancia con precisión matemática, demostrar bajo qué
condiciones ocurre, y proporcionar los instrumentos para
medirla desde evidencia documental.

## II. El sistema

Página | I

Axiomatización del Sistema de la Doble Mediación · Prólogo
El sistema opera sobre un espacio de Hilbert separable E —el
espacio de todos los estados posibles del sistema analizado—
y construye, sobre ese espacio, una cadena de objetos formales
interdependientes. La cadena tiene dos zonas:
La primera zona, Fundamentos (Partes 0–VI), construye los
instrumentos de medición: el espacio de base (E), las dos
mediaciones que producen e integran los actos del sistema
(φ(cid:0), φ(cid:0)), la integral acumulativa que recoge su historia (I(t)),
el índice de sustituibilidad que mide cuánto del
comportamiento es estructural (S), el coeficiente de asunción
que mide lo que el sistema reconoció como propio (α), el
déficit que cuantifica la brecha (Δ = R* − α), y el vector de
responsabilidad causal que distribuye la influencia sobre el
resultado (R*). Esta zona cierra con la Proposición de
Consistencia Interna, que verifica que los siete objetos son
mutuamente compatibles antes de usarlos en los resultados.
La segunda zona, Resultados (Partes VII–X), usa esos
instrumentos para cuatro resultados: la Relación de Escala del
Conocimiento (REC), que establece los límites del
autoconocimiento del sistema; el Teorema de Inversión Causal
(TIC), que demuestra la inversión bajo condiciones
documentables; el Modelo de Predictibilidad (MP), que estima
la probabilidad de decisiones futuras del sistema; y la clausura
del ego, que describe el estado del sistema en el momento de
su cierre.
Cuatro apéndices completan el libro: la demostración de la
cadena Davis-Kahan que sustenta el Lema 8.1 (A), la
calibración empírica de las funciones del TIC y la verificación
de su condición central sobre 18 casos en 9 dominios (B), el
glosario de traducción entre la terminología ontológica del
sistema y su equivalente matemático (C), y las extensiones del
marco formal —trayectoria discreta, función de imputación
neta sin doble conteo, operador contrafactual general,
teoremas de dominancia y estabilidad, nodos de bifurcación
causal (D).

## III. Mapa del libro

Página | II

Axiomatización del Sistema de la Doble Mediación · Prólogo
Parte 0. El espacio de Hilbert E. Dos objetos: el espacio
de base y la función de colapso. Sin estos dos objetos no
existe ninguno de los que siguen.
Parte I. La primera mediación φ(cid:0). Cómo el sistema
produce un acto a partir de su estado interno, su
configuración heredada y su historia. El Lema 1.1 fija la
distribución softmax sobre seis modos.
Parte II. La segunda mediación φ(cid:0) e I(t). Cómo el acto
producido por φ(cid:0) se evalúa, se integra o se rechaza, y
cómo se acumula la historia del sistema.
Parte III. El índice de sustituibilidad S. Dos versiones
—operacional y estructural— conectadas por una
función monótona que preserva orden.
Parte IV. El coeficiente de asunción α. La proporción
de lo producido que el sistema asumió como propio, en
versión continua y discreta.
Parte V. El déficit de asunción Δ = R* − α. Sus tres
signos, su evolución temporal y su función como señal de
inversión causal.
Parte VI. El vector de responsabilidad causal R*. El
eigenvector dominante de Wᵀ, único por Perron-
Frobenius, con el método de potencias para calcularlo.
Cierre. Proposición de Consistencia Interna. Cuatro
verificaciones de compatibilidad entre los objetos de las
Partes 0–VI.
Parte VII. Relación de Escala del Conocimiento. Una
cota informacional —no un principio de incertidumbre
cuántico— sobre la precisión simultánea con que el
sistema puede estimar I(t) y h(t).
Parte VIII. Teorema de Inversión Causal. El resultado
central del libro. Bajo tres condiciones estructurales
verificables desde el expediente, la imputación
convencional invierte la distribución causal real.
Parte IX. Modelo de Predictibilidad. Un modelo de
regresión logística sobre el estado completo Ψ(t). Estatus:
modelo estadístico, no teorema.
Página | III

Axiomatización del Sistema de la Doble Mediación · Prólogo
Parte X. Clausura del ego. El conjunto de todos los
colapsos del sistema, cerrado en E. El resultado más
breve y más directo del libro.

## Apéndice A. Demostración completa del Lema 8.1 por

la cadena S_est → Pinsker → Davis-Kahan.

## Apéndice B. Calibración de φ y ψ (n = 3 casos piloto,

análisis de sensibilidad), verificación de la Condición (1)
sobre 18 casos clasificados por nivel de evidencia, y
corroboración cualitativa de ψ sobre la muestra de 18
casos.

## Apéndice C. Glosario de traducción entre la

terminología ontológica de la colección y la terminología
matemática de este libro.

## Apéndice D. Extensiones: trayectoria causal discreta

con propiedad de Markov, función de imputación neta
Δ_net sin doble conteo, condiciones de identificabilidad,
operador contrafactual general (cid:0)(G,i,W'_i), dominancia,
estabilidad y nodos de bifurcación causal.

## IV. Estatus del sistema

El libro distingue explícitamente entre cuatro tipos de
contenido:
Resultados demostrados. Los teoremas de las Partes 0–
VIII y el Teorema 10 se siguen deductivamente de los axiomas
mediante herramientas estándar de análisis funcional, teoría de
la información y álgebra lineal. Los Axiomas 0–3 son las únicas
premisas no derivadas del núcleo formal.
Modelo estadístico. El Modelo de Predictibilidad de la Parte
IX es un modelo de regresión logística estándar. Sus
coeficientes se estiman por máxima verosimilitud sobre datos
de decisiones del sistema. No postula cotas teóricas
universales del error mínimo: el error empírico se estima en
cada aplicación.
Calibración empírica. Las funciones φ(V) =
1−(1−V)^{1.54} y ψ_real(x) = 0.21·x^{−0.55} de los
Página | IV

Axiomatización del Sistema de la Doble Mediación · Prólogo
Axiomas 8.1–8.2 se calibraron sobre tres casos piloto. Los
parámetros son puntos de partida revisables. El Apéndice
B.1.4 demuestra que las conclusiones cualitativas del TIC son
robustas en un rango amplio de valores paramétricos. La
propiedad estructural de ψ —que es decreciente en 1−S— está
corroborada por 18 casos en 9 dominios.
Trabajo futuro. El Teorema D.5 (nodos de bifurcación
causal) abre un programa de investigación: caracterizar los
grafos causales por su número de nodos de bifurcación y
derivar cotas para el cambio en Δ_net cuando un nodo de
bifurcación es perturbado. La cota del Teorema D.2 no aplica
directamente a nodos de bifurcación.
Este libro es un libro de fundamentos, no de aplicaciones. Su función es
establecer el lenguaje formal que hace posible la discusión rigurosa de la
imputación causal en sistemas complejos. Las aplicaciones en dominios
específicos —jurídico, clínico, de IA, histórico, ambiental— pertenecen a los
libros de la colección que usan este marco como base.

## V. Dependencias de lectura

La estructura axiomática impone un orden de dependencia
lógica: cada parte usa objetos definidos en las partes anteriores.
Sin embargo, no todas las partes son necesarias para todos los
resultados. El mapa de dependencias mínimas es el siguiente:
Para el TIC (Parte VIII). Partes 0–VI son necesarias. El
Corolario 7.2 de la Parte VII no es necesario para el TIC. El

## Apéndice A es necesario para el Lema 8.1.

Para la REC (Parte VII). Partes 0–II son necesarias (para
I(t) y h(t)). El Axioma 3 es el único axioma adicional. Las
Partes III–VI no son necesarias para la REC.
Para el MP (Parte IX). Partes 0–II y el Lema 1.1 son
suficientes. La REC de la Parte VII proporciona contexto
sobre la variabilidad de predicción, pero no es formalmente
necesaria.
Para la clausura del ego (Parte X). Solo la Parte 0
(Definición 0) y el Teorema 2 (Parte II) son necesarios.
Página | V

Axiomatización del Sistema de la Doble Mediación · Prólogo
Para las extensiones (Apéndice D). D.1 requiere Partes 0–

## II. D.2 requiere D.1 y el Apéndice A. D.3 requiere la Parte VI

y el Apéndice A. D.4 requiere D.2 y D.3.

## VI. Audiencia y notación

El libro asume familiaridad con análisis funcional elemental
(espacios de Hilbert, integrales de Bochner), álgebra lineal
(eigenvectores, matrices estocásticas), teoría de la probabilidad
y teoría de la información (divergencia KL, desigualdad de
Cramér-Rao). No asume conocimiento de la ontología de la
colección: el Apéndice C proporciona la traducción completa
para el lector que la necesite, y la nota al final de cada parte
donde aparece terminología ontológica libera explícitamente al
lector técnico de conocerla.
La notación sigue las convenciones estándar. Los objetos
matemáticos se identifican por tipo desde su primera
aparición: E es un espacio de Hilbert, c : T → E es una
función, R* (cid:0) Δⁿ es una distribución de probabilidad, h(v_t)
(cid:0) Δ(cid:0) es un vector de probabilidades sobre el simplex de
dimensión 5, Δᵢ (cid:0) [−1,1] es un escalar. El Apéndice C incluye
una tabla con los tipos matemáticos de todos los objetos del
sistema.
La terminología ontológica de la colección —Hijos de Afrodita, Caos, ego,
colapso en su sentido filosófico— no aparece en el cuerpo formal de este libro.
Aparece únicamente en notas al margen al final de las secciones relevantes,
marcadas con el título «Correspondencia con el sistema ontológico», y en el

## Apéndice C. El lector que no conoce esa terminología no pierde nada del rigor

formal del sistema.
Centro Multidisciplinario Meriadock · 2026
Página | VI

Axiomatización del Sistema de la Doble Mediación
