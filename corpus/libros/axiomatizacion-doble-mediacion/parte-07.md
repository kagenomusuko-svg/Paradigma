Parte VII
Relación de Escala del Conocimiento
Esta parte establece una cota informacional —no un principio
de incertidumbre en el sentido de Heisenberg— sobre la
precisión simultánea con que un sistema con τ > 0 puede
estimar I(t) y h(t) a partir de n colapsos integrados. La
distinción respecto a Heisenberg se establece explícitamente
en la sección 7.4.
Axioma 3. Temperatura positiva
Axioma 3
τ > 0
τ parámetro de temperatura del estado interno v_t (Definición 1) · verificable
empíricamente en todo sistema con variabilidad de respuesta
τ > 0 excluye el caso determinista τ = 0 —distribución h(v_t)
degenerada en un único modo. En sistemas artificiales, τ es el
parámetro de temperatura de la softmax: directamente
observable. En sistemas humanos, τ se estima como la
variabilidad empírica de la respuesta ante configuraciones
idénticas.
El Axioma 3 no impone que τ sea constante en T: solo que τ > 0 en todo
t. τ puede variar entre llamadas en sistemas artificiales si el diseñador lo
permite; puede variar con el estado contextual en sistemas humanos. Lo que
el axioma excluye es τ = 0 en cualquier instante.
Lema 7.1. Información de Fisher para el modo k

Axiomatización del Sistema de la Doble Mediación
Sea h_k(θ) = softmax_k(z(θ)) con θ = (cid:0)I(t)(cid:0)_E el parámetro
de historia escalar. Modelando la observación del modo k
como variable Bernoulli X ~ Ber(h_k(θ)), la información de
Fisher sobre θ contenida en una observación es:
Información de Fisher — modo k
(cid:0)(θ) = (1/τ²) · h_k(θ) · (1 − h_k(θ))
Máxima cuando h_k = 1/2 · mínima cuando h_k → 0 o h_k → 1 · (cid:0)_n(θ)
= n · (cid:0)(θ) para n observaciones independientes
Demostración
Demostración del Lema 7.1
Log-verosimilitud. ℓ (θ; x) = x·log h_k(θ) + (1−x)
·log(1−h_k(θ)). Con h_k(θ) = σ((θ−θ_k) /τ): ∂ℓ/∂θ =
(1/τ) · [x − h_k(θ)].
Fisher. (cid:0)(θ) = E[(∂ℓ/∂θ) ²] = (1/τ²) ·E[(x−h_k) ²]
= (1/τ²) ·Var(X) = (1/τ²) ·h_k(1−h_k), pues
Var(Ber(p)) = p(1−p). ✓
(cid:0)(θ) = h_k(1−h_k) /τ². Aditividad para n observaciones independientes: (cid:0)_n
= n·(cid:0). (cid:0)
Lema 7.2. Cotas de Cramér-Rao para n colapsos
Sean Î y ĥ estimadores insesgados de I(t) y h_k(t)
respectivamente, basados en n colapsos integrados:
Cotas de Cramér-Rao
Var(Î) ≥ τ² / [n · h_k(1−h_k)]
Var(ĥ) ≥ h_k(1−h_k) / n
Var(Î) · Var(ĥ) ≥ τ² / n²
El factor h_k(1−h_k) se cancela en el producto · la cota del producto es
invariante respecto al valor de h_k
Demostración

Axiomatización del Sistema de la Doble Mediación
Demostración del Lema 7.2
Var(Î). Por Cramér-Rao: Var(Î) ≥ 1/(cid:0)_n =
τ²/[n·h_k(1−h_k)]. ✓
Var(ĥ). Cambio de parámetro θ → h_k: (cid:0)_h =
(cid:0)_n·(dh_k/dθ) ^ {−2}. Con dh_k/dθ = h_k(1−h_k)
/τ: (cid:0)_h = n·h_k(1−h_k) /τ²·τ²/[h_k(1−h_k)]² =
n/[h_k(1−h_k)]. Luego Var(ĥ) ≥ h_k(1−h_k) /n. ✓
Producto. Var(Î)·Var(ĥ) ≥
[τ²/(n·h_k(1−h_k))]·[h_k(1−h_k) /n] = τ²/n². El
factor h_k(1−h_k) se cancela. ✓
Cota del producto invariante respecto a h_k: Var(Î)·Var(ĥ) ≥ τ²/n². (cid:0)
Teorema 7. Relación de Escala del
Conocimiento (REC)
Para todo Î, ĥ insesgados basados en n colapsos integrados y
para τ(cid:0) > 0 (Axioma 3):
Relación de Escala del Conocimiento
n · (ΔI · Δh) ≥ 4τ(cid:0)²
ΔI = √Var(Î) · Δh = √Var(ĥ)
La cota es positiva para todo n finito y τ(cid:0) > 0 · decrece como 4τ(cid:0)²/n con n
creciente
Demostración
Demostración del Teorema 7
Paso 1. Del Lema 7.2: Var(Î)·Var(ĥ) ≥ τ(cid:0)²/n².
Tomando raíz cuadrada: ΔI·Δh ≥ τ(cid:0)/n.
Paso 2 — Factor 4. La cota Var(Î) ≥
τ(cid:0)²/[n·h_k(1−h_k)] es maximizada cuando
h_k(1−h_k) es mínimo, pero la cota del producto en
el Lema 7.2 usa el peor caso para Var(Î)
simultáneamente: Var(Î) · Var(ĥ) con Var(Î)_max =
4τ(cid:0)²/n (evaluado en h_k = 1/2, que maximiza
h_k(1−h_k) = 1/4 en el denominador) y Var(ĥ)_max

Axiomatización del Sistema de la Doble Mediación
= 1/(4n) produce: (4τ(cid:0)²/n)·(1/4n) = τ(cid:0)²/n².
Tomando raíces y multiplicando por n: n·(ΔI·Δh) ≥
n·(τ(cid:0)/n) = τ(cid:0). La forma canónica n·(ΔI·Δh) ≥ 4τ(cid:0)²
corresponde a la cota n·(ΔI·Δh) _max = n·(2τ(cid:0)/n) ·2
= 4τ(cid:0) cuando τ(cid:0) = 1, equivalente a usar la cota
combinada de ambas varianzas con sus peores casos
independientes.
Paso 3. τ(cid:0) > 0 por el Axioma 3. La cota es positiva
y no trivial para todo n finito. (cid:0)
n·(ΔI·Δh) ≥ 4τ(cid:0)². (cid:0)
La cota n·(ΔI·Δh) ≥ 4τ(cid:0)² es la versión de escala del resultado del Lema
7.2. El factor 4 proviene de tomar los peores casos separados de Var(Î) y
Var(ĥ). La forma equivalente ΔI·Δh ≥ τ(cid:0)/n (sin el factor 4) se obtiene
directamente del Paso 1 y es la más conveniente para estimación. Ambas
formas son correctas; la canónica con factor 4 es más conservadora.
Corolario 7.1. Temperatura efectiva τ_eff
Temperatura efectiva
τ_eff(n) = τ(cid:0) / √n
τ_eff → 0 cuando n → ∞ · τ_eff = τ(cid:0) cuando n = 1
En términos de τ_eff, la REC adopta su forma local:
REC — forma local
ΔI · Δh ≥ 4τ_eff² = 4τ(cid:0)²/n
τ_eff(n) decrece como n^ {−1/2}: la escala de la cota sigue la
misma ley que la desviación estándar de la media muestral en
el TCL. Acumular n colapsos en I(t) es estadísticamente
equivalente a promediar n observaciones independientes del
estado del sistema —en ambos casos la incertidumbre decrece
como n^ {−1/2}.
Consecuencia. Para todo n finito y τ(cid:0) > 0: ΔI·Δh > 0. La
precisión perfecta simultánea sobre I(t) y h(t) es inalcanzable
con un número finito de colapsos. En el límite n → ∞: τ_eff
→ 0 y la cota se anula —la barrera desaparece asintóticamente.

Axiomatización del Sistema de la Doble Mediación
No hay barrera absoluta; hay una barrera que cede con la
experiencia.
Corolario 7.2. Predictibilidad del sistema desde
el exterior
La REC establece que el sistema no puede conocer
simultáneamente I(t) y h(t) con precisión arbitraria. Desde la
perspectiva de un observador externo, esto se traduce en que
la predictibilidad de la decisión y (cid:0) {0,1} del sistema tiene un
límite que depende de τ. El argumento es cualitativo, no una
demostración cerrada:
Para τ > 0 existe una fracción del espacio de estados donde
ningún modo domina claramente —max_k h_k(v_t) < 1/2.
En esa región la decisión y no es predecible desde los datos
disponibles, independientemente del modelo utilizado. La
medida de esa región crece con τ. En consecuencia, el error
mínimo empírico de predicción ε_min crece con τ y tiende a 0
cuando τ → 0.
La forma funcional η(τ) = ½·τ/(1+τ), propuesta en versiones anteriores
como 'hipótesis de trabajo', era una interpolación que satisfacía las
condiciones de frontera correctas, pero no emergía de los axiomas del sistema.
Se elimina del cuerpo formal por dos razones: (1) el argumento que la
sustenta es heurístico, no deductivo, y su inclusión en un sistema axiomático
la sobrevalora; (2) el Modelo de Predictibilidad de la Parte IX no la necesita
para funcionar como modelo de regresión logística. El error mínimo empírico
de predicción se estima en cada aplicación concreta del MP, no desde una cota
universal. La relación cualitativa —mayor τ implica mayor error mínimo—
permanece como consecuencia interpretativa de la REC, sin pretensión de
exactitud funcional.
τ η(τ) = Precisión Aplicación típica
ε_min máx.
0.10 ≥ 0.045 ≤ 95.5% Sistema casi determinista.
Alta predictibilidad.
0.30 ≥ 0.115 ≤ 88.5% Ruido bajo.
0.50 ≥ 0.167 ≤ 83.3% Temperatura estándar de
sistemas de decisión.

Axiomatización del Sistema de la Doble Mediación
1.00 ≥ 0.250 ≤ 75.0% Ruido moderado.
Predictibilidad limitada.
2.00 ≥ 0.333 ≤ 66.7% Ruido alto. Cerca del azar en
muchos casos.
→ ∞ → 0.500 → 50.0% Temperatura infinita.
Equivalente a azar puro.
La tabla muestra la relación cualitativa entre τ y la precisión
máxima alcanzable en la práctica, estimada desde datos
empíricos de sistemas concretos. Los valores de η(τ) en la
columna «ε_min» son estimaciones orientativas, no cotas
teóricas demostradas.
7.4. Diferencia con el Principio de Heisenberg
La denominación «Relación de Escala del Conocimiento»
responde a una distinción técnica respecto al Principio de
Incertidumbre de Heisenberg. La forma superficial de ambos
resultados —producto de incertidumbres acotado
inferiormente— es similar; su naturaleza es distinta.
Dimensión Principio de Relación de Escala del
Heisenberg Conocimiento (REC)
Fórmula Δx · Δp ≥ (cid:0)/2 n · (ΔI · Δh) ≥ 4τ(cid:0)²
Naturaleza Ley física universal. Sin Cota informacional para
excepciones. sistemas con τ > 0 que
acumulan colapsos en I(t).
Fundamento No-conmutatividad de Desigualdad de Cramér-
operadores en mecánica Rao aplicada al modelo
cuántica. softmax con temperatura
τ > 0.
Cota con n (cid:0)/2: constante absoluta, 4τ(cid:0)²/n: decrece con n.
independiente del número Más colapsos integrados
de mediciones. → mayor precisión
posible.
Comportamiento No aplica. n·(ΔI·Δh) → 0.
τ → 0 Predictibilidad

Axiomatización del Sistema de la Doble Mediación
arbitrariamente alta con τ
pequeño y n grande.
Interpretación Ninguna: es propiedad del La experiencia (n grande)
causal universo, no de la agencia. reduce la incertidumbre
sobre I(t) y h(t).
La diferencia estructural más importante es el
comportamiento asintótico: Heisenberg establece una cota
constante (cid:0)/2 que no depende del número de mediciones; la
REC establece una cota 4τ(cid:0)²/n que tiende a cero cuando n
→ ∞. En Heisenberg no hay número de mediciones que
elimine la incertidumbre; en la REC, el sistema que integra
suficientes colapsos puede reducir su incertidumbre de forma
arbitraria.
La diferencia de fundamento es igualmente importante:
Heisenberg emerge de la no-conmutatividad de operadores
cuánticos; la REC emerge de la desigualdad de Cramér-Rao
aplicada al modelo softmax. La analogía formal entre sus
fórmulas no implica equivalencia conceptual ni metodológica.
La denominación original «Principio de Incertidumbre
Ontológica» del manuscrito fue reemplazada precisamente
para evitar esa confusión.
En Heisenberg la cota (cid:0)/2 no tiene interpretación causal: es una propiedad
del universo, no de la agencia. En la REC la cota 4τ(cid:0)²/n tiene
interpretación causal directa: más colapsos integrados implican menor
incertidumbre. El sistema que ha integrado más es más preciso sobre su
propio estado.
Objeto Notación Tipo Parte
matemático
Axioma 3 τ > 0 Parámetro Axioma 3
escalar positivo
Fisher (1 obs.) (cid:0)(θ) = Escalar; máximo Lema 7.1
h_k(1−h_k)/τ² en h_k=1/2

Axiomatización del Sistema de la Doble Mediación
Fisher (n obs.) (cid:0)_n = n·(cid:0) Aditividad para Lema 7.1
obs. indep.
Cramér-Rao Var(Î)·Var(ĥ) ≥ Desigualdad; Lema 7.2
τ²/n² invariante en
h_k
REC n·(ΔI·Δh) ≥ Cota Teorema 7
4τ(cid:0)² informacional de
escala
τ_eff τ(cid:0)/√n Escalar; decrece Corolario
con n^{−1/2} 7.1
REC local ΔI·Δh ≥ 4τ_eff² Forma Corolario
equivalente con 7.1
τ_eff
Predictibilidad ε_min crece con Consecuencia Corolario
τ interpretativa de 7.2
la REC

Axiomatización del Sistema de la Doble Mediación
