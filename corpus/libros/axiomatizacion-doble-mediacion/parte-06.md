### Parte VI

### El vector de responsabilidad causal R*

### Definición 6.  El grafo causal G

Sea G = (N, A, w) un grafo dirigido donde:

N  Conjunto finito de nodos N = {1, 2, …, n, n+1}. Los nodos {1, …, n} son los actores causalmente relevantes del sistema. El nodo n+1 es el nodo final (sumidero): representa el resultado cuya responsabilidad se distribuye. No tiene aristas salientes. A  Conjunto de aristas dirigidas A □ N × N. La arista (i, j) □ A indica que i ejerce influencia causal sobre j. Para todo j: (n+1, j) □ A. w  Función de peso w: A → [0,1] tal que Σ□ w (i, j) = 1 para todo i □ {1,…,n}. Los pesos representan la magnitud relativa de la influencia de i sobre sus sucesores. La fila n+1 de la matriz W es el vector cero.

La matriz de pesos W □ □^{(n+1) ×(n+1)} es no negativa, estocástica por filas en las filas {1,…,n}, con la fila n+1 nula.

Construcción de G desde la evidencia.  En aplicaciones, los pesos w (i, j) son estimaciones sustentadas en evidencia documental y se expresan como intervalos [a_{ij}, b_{ij}] según la escala E0–E8 de Metrología Causal Vol. I. Para el cálculo de R* se usan los midpoints m_{ij} = (a_{ij}+b_{ij}) /2 como estimación puntual; los extremos producen R*(min) y R*(max) (Lema 6.1).

Axiomatización del Sistema de la Doble Mediación

La condición Σ□ w (i, j) = 1 garantiza que los pesos son proporciones, no magnitudes absolutas. No impone que i influya sobre un único sucesor: la distribución puede estar repartida. Si la evidencia sustenta una sola arista (i, j), entonces w (i, j) = 1 y w (i, j') = 0 para j' ≠ j.

### Definición 6.1.  El vector de responsabilidad causal R*

Sea W la matriz de pesos de G. El vector de responsabilidad causal R* es el eigenvector dominante de Wᵀ normalizado en Δⁿ:

Vector de responsabilidad causal R*

Wᵀ R* = λ□ R*,    Σᵢ R*ᵢ = 1, R*ᵢ > 0 ∀ i λ□ > 0 eigenvalor dominante de Wᵀ · R* □ Δⁿ simplex estándar de dimensión n · existencia y unicidad garantizadas por el Teorema 6

R*ᵢ es la fracción de la influencia causal del resultado n+1 que transita por el nodo i, considerando todas las trayectorias causales posibles en G. R*ᵢ alto indica que el resultado depende significativamente de la presencia idiosincrática del nodo i en su posición.

Elección de Wᵀ sobre W.  El eigenvector de W recoge la influencia que i ejerce sobre sus sucesores. El eigenvector de Wᵀ recoge la influencia acumulada que los predecesores ejercen sobre i y, por transitividad, la participación de i en la producción del resultado final. Para la distribución de responsabilidad causal —cuánto del resultado pasa por i— el eigenvector de Wᵀ es el objeto correcto. La elección es análoga a la de PageRank: una página es importante si páginas importantes apuntan hacia ella.

Alcance de R*.  R* es la distribución de influencia causal estructural, no la distribución de culpabilidad jurídica ni de responsabilidad moral. La calificación jurídica o ética es una operación posterior que usa R* como input técnico. El sistema no impone esa calificación.

Axiomatización del Sistema de la Doble Mediación

### Teorema 6.  Existencia y unicidad de R* — Perron-Frobenius

### Si G satisface las condiciones de la tabla siguiente, entonces:

(i)  Existe λ□ > 0 único con |λ| < λ□ para todo otro eigenvalor λ de Wᵀ. (ii)  Existe R* con R*ᵢ > 0 para todo i y Wᵀ R* = λ□ R*. (iii)  R* es único en Δⁿ (salvo normalización, el espacio propio de λ□ tiene dimensión 1). (iv)  Para W estocástica por filas: λ□ = 1 y R* □ Δⁿ es la distribución estacionaria de la cadena de Markov inducida.

Condición Definición técnica Verificación en G  / Procedimiento si falla

No negatividad

w(i,j) ≥ 0 para toda arista (i,j) □ A.

Garantizada por Definición 6: w : A → [0,1].

Irreducibilidad ∀ ∈ ∃ i,j  N  camino dirigido i → j en G.

G fuertemente conexo. Si falla: W(ε) = (1−ε)W + ε·J/n con ε □ (0,1) pequeño.

Aperiodicidad mcd de las longitudes de todos los ciclos de G es 1.

Garantizada si □ nodo con lazo (ciclo de longitud 1) o ciclos de longitudes coprimas. Si falla: misma perturbación W(ε).

Estocástica por filas

Σ□ w(i,j) = 1 para todo i ≠ n+1.

Garantizada por Definición 6. Implica λ□ = 1 directamente.

Consecuencia λ□ = 1, simple; |λ□| < 1 para k ≥ 2.

R* □ Δⁿ⁻ ¹ único: todas las componentes R*ᵢ > 0, Σᵢ R*ᵢ = 1.

### Demostración

Axiomatización del Sistema de la Doble Mediación

Demostración del Teorema 6

Paso 1.  Wᵀ es no negativa (w (i, j) ≥ 0). Si G es irreducible y aperiódico, Wᵀ es primitiva (irreducible + aperiódica). El Teorema de Perron-Frobenius para matrices no negativas primitivas garantiza las propiedades (i)–(iii). Paso 2 — λ□ = 1.  W es estocástica por filas: W·1 = 1, luego 1 es eigenvalor de W con eigenvector 1. Por simetría espectral, λ□ = 1 es eigenvalor de Wᵀ. La primitiva garantiza que es el único de módulo 1. Paso 3 — Unicidad.  El espacio propio de λ□ = 1 en Wᵀ tiene dimensión 1 (Perron-Frobenius). Imponiendo Σᵢ R*ᵢ = 1, R* queda completamente determinado. Paso 4 — Positividad.  Para matrices primitivas, el eigenvector dominante tiene todas las componentes estrictamente positivas. Luego R*ᵢ > 0 para todo i □ N, lo que garantiza Δᵢ = R*ᵢ − αᵢ □ [−1,1] (Teorema 5). Las cuatro propiedades se siguen del Teorema de Perron-Frobenius para matrices no negativas primitivas. □

Perturbación cuando G no es primitivo.  Si G no satisface irreducibilidad o aperiodicidad: sustituir W por W(ε) = (1−ε) W + (ε/n) ·J, donde J es la matriz de unos y ε □ (0,1) pequeño. W(ε) es primitiva para todo ε > 0. El Teorema 6 aplica a W(ε) y R*(ε) → R* cuando ε → 0. En práctica, ε = 0.01 produce resultados estables para n ≤ 20.

La perturbación ε tiene interpretación estructural: representa la posibilidad de que cualquier nodo influya mínimamente sobre cualquier otro del grafo. En sistemas organizacionales complejos esta posibilidad es realista; ε = 0.01 equivale a asignar un 1% de influencia difusa uniforme sobre todos los nodos.

### Lema 6.1.  Método de potencias y rangos de evidencia

### El método de potencias calcula R* iterativamente bajo las condiciones del Teorema 6:

Axiomatización del Sistema de la Doble Mediación

Algoritmo — método de potencias para R*

Entrada:  W □ □ⁿ□ⁿ estocástica por filas · ε_conv > 0 tolerancia Inicio:  R*(0) = (1/n, …, 1/n) distribución uniforme Paso k+1:  v ← Wᵀ · R*(k) R*(k+1) ← v / □v□□ Parar si:  □R*(k+1) ₁ ‖ − R*(k) < ε_conv ε_conv = 10 ⁶ ⁸ ⁻ ⁻ estándar · 10 alta precisión Salida:  R* = R*(k+1) Complejidad por iteración: O(n²) · Iteraciones típicas: 20–50 para n ≤ 20 con ε_conv = 10 ⁶ ⁻

### Demostración de convergencia

Demostración del Lema 6.1

Paso 1.  Descomposición: R*(0) = c□·R* + Σ_{k≥2} c□·v□ en la base de eigenvectores de Wᵀ, con |λ□| < 1 para k ≥ 2. Paso 2.  (Wᵀ)^m · R*(0) = c□·R* + Σ_{k≥2} c□·λ□ᵐ·v□. Como |λ□| < 1, el segundo término → 0 cuando m → ∞. Paso 3.  Tras normalización en cada iteración, R*(k) → R* con velocidad geométrica de razón |λ□|, donde λ□ es el segundo eigenvalor en módulo. La brecha espectral δ = 1 − |λ□| determina la velocidad de convergencia. Convergencia para todo R*(0) con componentes positivas bajo las condiciones del Teorema 6. □

### Rangos de evidencia y estimación por intervalos

Axiomatización del Sistema de la Doble Mediación

### Cuando los pesos están expresados como intervalos [a_{ij}, b_{ij}], el procedimiento estándar produce tres estimaciones de R*:

R*(mid)  Ejecutar el algoritmo con m_{ij} = (a_{ij}+b_{ij}) /2. Estimación puntual de R*. R*(min)  Ejecutar con a_{ij} para cada arista. Cota inferior del intervalo de R*. R*(max)  Ejecutar con b_{ij} para cada arista. Cota superior del intervalo de R*.

El nivel de certeza de la estimación se declara según la anchura max_i (R*(max)_i − R*(min)_i): anchura ≤ 0.05 → declaración A; anchura ≤ 0.10 → declaración B; anchura > 0.10 → declaración C, según la escala del Vol. I de Metrología Causal.

El intervalo [R*(min), R*(max)] refleja la incertidumbre empírica del analista sobre los pesos del grafo, no la incertidumbre ontológica del sistema. El vector R* del sistema real es único y determinado (Teorema 6). La REC de la Parte VII cuantifica la incertidumbre del sistema sobre su propio estado I(t); los intervalos de R* cuantifican la incertidumbre del analista sobre los pesos del grafo G. Son dos fuentes de incertidumbre conceptualmente distintas.

Objeto Notación Tipo matemático

Parte

G = (N, A, w) Dígrafo ponderado

Grafo causal

Definició n 6

Nodo final n+1 □ N Sumidero; fila de W nula

Definició n 6

W □ □^{(n+1)×(n+1)} No negativa; estocástica en {1,…,n}

Matriz de pesos

Definició n 6

Axiomatización del Sistema de la Doble Mediación

Vector R* Wᵀ R* = λ□ R*, R* □ Δⁿ Distribución sobre N

Definició n 6.1

λ□ = 1 Para W estocástica por filas

Eigenvalor dominante

### Teorema 6

Positividad R*ᵢ > 0 ∀i Garantiza Δᵢ □ [−1,1]

### Teorema 6

Unicidad dim ker(Wᵀ−I) = 1 Espacio propio unidimension al

### Teorema 6

W(ε)=(1−ε)W+(ε/n)J Hace W primitiva; ε → 0 → R*

Perturbació n

### Teorema 6

### Lema 6.1

Método de potencias

Converge con razón |λ□|

R*(k+1)=Wᵀ R*(k)/□·□□

### Lema 6.1

□R*(k+1) ₁ ‖ −R*(k) <ε_c onv

Criterio de conv.

ε_conv=10⁻ □ estándar

[R*(min), R*(max)] Incertidumbr e empírica del analista

### Lema 6.1

Intervalo de R* Axiomatización del Sistema de la Doble Mediación

### Cierre de los Fundamentos

### Proposición de Consistencia Interna

Esta proposición no introduce resultados nuevos. Verifica que los objetos de las Partes 0–VI son mutuamente compatibles antes de usarlos en los resultados de las Partes VII–X. La consistencia es condición necesaria pero no suficiente para la corrección del sistema: garantiza que los resultados no se contradicen entre sí; no garantiza que sean verdaderos respecto al sistema que modelan.

Un sistema inconsistente puede demostrar cualquier cosa, incluyendo su propia negación. La consistencia interna es el piso que separa un conjunto de definiciones de un sistema formal.

Ítem Par de

Partes de referencia

Condición verificada

objetos

(i) S_op, S_est — R*

Defs. 3.1, 3.2; Def. 6.1

S_est(i) → 1 ⟹ D_KL (R* □ R*^(i)) → 0 ⟹ ‖R* − R*^(i) ₁ ‖ → 0. Alta sustituibilidad implica mínima idiosincrasia causal.

(ii) φ□ — h(v_t) h_k(v_t) = softmax_k(z): h_k ≥ 0 y Σ_k h_k = 1 para todo v_t □ V. h(v_t) □ Δ□.

### Lema 1.1 (Parte I)

(iii) α continuo — α discreto

Defs. 4, 4.1; Prop. 4.1 (Parte IV)

Con w(τ) = δ(τ−tᵢ): la integral continua colapsa a p_pres·f·g por la propiedad de muestreo. Una sola

Axiomatización del Sistema de la Doble Mediación

definición, dos granularidades.

(iv) Δ — TIC Δᵢ □ [−1,1] garantiza que {Δ(D) > 0 ∧ Δ(E) < 0} es algebraicamente posible. El TIC opera sobre un espacio no vacío.

Teoremas 5, 8 (Partes V, VIII)

### Ítem (i).  Compatibilidad S — R*

Compatibilidad S–R*

S_est(i) → 1 ⟹ ‖R* ₁ ‖ − R*^(i) → 0 R*^(i) eigenvector dominante de (W^(i)) ᵀ con fila i reemplazada por promedio

Verificación del Ítem (i)

Por Def. 3.2.  S_est(i) = 1 − D_KL (R* □ R*^(i)) /log(m). S_est → 1 implica D_KL (R* ‖ R*^(i)) → 0. Por Pinsker.  □R* ₁ ‖ − R*^(i) ≤ √ (2 D_KL (R* □ R*^(i))). Luego D_KL ‖ → 0 implica R* ₁ ‖ − R*^(i) → 0. Coherencia con Def. 3.1.  Si R* no cambia al sustituir i, entonces R*ᵢ ≈ 1/m (valor promedio): la contribución causal del nodo i es mínima. Por la Def. 3.1, esto corresponde a □c□_C >> □a_t□_E, es decir, S_op → 1. Los dos índices son coherentes. ✓ Coherencia con el TIC.  La Condición (2) del Teorema 8 (S_est(E) > θ_S) implica R*(E) bajo vía el Lema 8.1, que usa exactamente esta cadena. Sin la compatibilidad S–R*, el Lema 8.1 carecería de fundamento. ✓

Axiomatización del Sistema de la Doble Mediación

S y R* son objetos independientes pero coherentes: mayor S implica menor idiosincrasia causal. No hay contradicción. ✓

### Ítem (ii).  Validez probabilística de h(v_t)

h(v_t) □ Δ□ para todo v_t □ V h_k(v_t) ≥ 0    y ∈ ∀ ∈ Σ_{k K} h_k(v_t) = 1     v_t  V Consecuencia directa de la forma softmax del Lema 1.1

Verificación del Ítem (ii)

h_k ≥ 0.  exp(z_k) > 0 para todo z_k □ □; denominador positivo; razón positiva. ✓ Σ h_k = 1.  Σ_k exp(z_k) / Σ_j exp(z_j) = 1 por cancelación exacta. ✓ Corrección del manuscrito.  La formulación original con sigmoide independiente producía Σ_k σ(z_k) □ {1}, invalidando la interpretación probabilística y haciendo al argmax k* no interpretable como moda de una distribución. La corrección a softmax de la Parte I elimina esa inconsistencia. Esta verificación confirma su efectividad. Consecuencia sistémica.  La REC (Parte VII) y el MP (Parte IX) usan h_k como probabilidades en sus argumentos. La validez de ambos resultados depende de h(v_t) □ Δ⁵ ✓ . h(v_t) □ Δ□ para todo v_t □ V. φ□ produce siempre un colapso dentro de A □ E. ✓

### Ítem (iii).  Coherencia de α continuo y discreto

Versión discreta como caso particular de la continua

### w(τ) = δ (τ − tᵢ) ⟹ α(aᵢ) = p_pres · f(τᵢ) · g(τᵢ)

Axiomatización del Sistema de la Doble Mediación

Por la propiedad de muestreo de la delta de Dirac — demostrado en la Proposición 4.1

Verificación del Ítem (iii)

Numerador.  ∫□ᵗ 1_{int}(τ)·δ(τ−tᵢ) ·p(τ) dτ = 1_{int}(tᵢ)·p(tᵢ) por la propiedad de muestreo: ∫ f(τ)·δ(τ−tᵢ) dτ = f(tᵢ). ✓ Denominador.  ∫□ᵗ δ(τ−tᵢ) dτ = 1. ✓ Resultado.  α = p_pres · p(tᵢ) = p_pres · f(τᵢ) · g(τᵢ) por la descomposición de la Tabla 4.1. No existen dos objetos distintos: hay una única definición con dos granularidades de cómputo. ✓ La versión continua y la discreta son el mismo objeto. ✓

### Ítem (iv).  Compatibilidad Δ — Teorema de Inversión Causal

No vacuidad del espacio del TIC

### Δᵢ □ [−1,1] ⟹ {Δ(D) > 0 ∧ Δ(E) < 0} es

algebraicamente posible Este ítem no demuestra que las condiciones del TIC se cumplan en sistemas reales; solo que el espacio donde opera no es vacío

Verificación del Ítem (iv)

Acotación.  Δᵢ = R*ᵢ − αᵢ □ [−1,1] por el Teorema 5. Los extremos ±1 son alcanzables. No vacuidad.  Se requiere simultáneamente: (a) □D con R*(D) > α(D), y (b) □E con R*(E) < α(E). Ejemplo explícito: R*(D) = 0.40, α(D) = 0.05 → Δ(D) = 0.35 > 0; R*(E) = 0.05, α(E) = 0.60 → Δ(E) = −0.55 < 0. Ambos valores en [−1,1] y R*(D) + R*(E) = 0.45 es parte de una distribución que suma 1. ✓ Compatibilidad con Σ R*ᵢ = 1.  La normalización de R* no impone Σ αᵢ = 1. Luego Δ(D) > 0 y Δ(E) < Axiomatización del Sistema de la Doble Mediación

0 simultáneamente son compatibles con la normalización. ✓ El espacio donde opera el TIC es no vacío dentro del marco formal de los Fundamentos. ✓

### Cierre.  Estado del sistema tras los Fundamentos

Los cuatro ítems establecen:

(i)  S y R* son coherentes: mayor sustituibilidad implica menor idiosincrasia causal. El Lema 8.1 tiene fundamento. (ii)  h(v_t) □ Δ□ para todo v_t. La REC y el MP tienen fundamento. (iii)  α es un único objeto con dos granularidades. Los resultados de la Parte IV son coherentes entre sí. (iv)  Δ □ [−1,1] garantiza que el TIC opera sobre un espacio no vacío. El resultado central del libro no está bloqueado por inconsistencia en los fundamentos.

Estas condiciones son necesarias, no suficientes. Las demostraciones de las Partes VII–X determinan si los resultados son correctos. Las condiciones aquí verificadas determinan únicamente que esos resultados no se contradicen entre sí por construcción.

Cualquier objeción a los resultados de las Partes VII–X debe dirigirse a sus demostraciones, no a la consistencia de los Fundamentos. Esa consistencia ha sido verificada en esta proposición.

Axiomatización del Sistema de la Doble Mediación

