# AUD-RSTAR-001 / CAND-RSTAR-001 — Reconstrucción formal del operador de responsabilidad

> **Documento derivado de mantenimiento, no fuente canónica.** Continúa `NORM-RSTAR-EGO-001` y la entrada editorial `2E-RSTAR-001`. Su función es reconstruir un candidato matemático para `M_R(D)` sin alterar las fuentes de primera edición ni convertir una propuesta formal en validación empírica.

- **Auditoría:** `AUD-RSTAR-001`
- **Candidato formal:** `CAND-RSTAR-001`
- **Estado:** **CANDIDATO PREFERENTE / ADJUDICACIÓN AUTORAL Y EDITORIAL PENDIENTE**
- **Objeto:** operador de responsabilidad `M_R(D)` y distribución `R*(D)`
- **Normalización previa:** `documentacion/normalizacion-rstar-formula-ego.md`
- **Entrada de segunda edición:** `documentacion/segunda-edicion/2E-RSTAR-001.md`

---

## 1. Restricciones que el operador debe respetar

La reconstrucción parte de restricciones ya fijadas por la genealogía del sistema, no de una elección libre de teoría de redes.

1. `φ₁` produce actos o colapsos bajo voluntad y condiciones.
2. El acto de un nodo puede entrar en las condiciones de otro nodo.
3. `W_ij`, bajo la convención `i → j`, representa una determinación local: cuánto del colapso o comportamiento de `j` fue determinado por `i`.
4. El resultado `D` es el término respecto del cual se reconstruye causalidad; no es un actor homogéneo a sus causas.
5. `δ_ext` retorna exteriormente el resultado hacia los nodos cuya cadena causal es reconstruible.
6. `R*(D)` debe medir participación causal global respecto de `D`, no intención, asunción ni centralidad de red en abstracto.
7. `α` permanece independiente de `R*`; `Δ = R* − α` compara causalidad con asunción efectiva.
8. La decisión autoral vigente conserva `R*` como **eigenvector de responsabilidad**, pero no exige que sea el eigenvector de la matriz causal cruda `W`.

La consecuencia formal es que debe distinguirse:

`W` = relaciones causales locales,

frente a:

`M_R(D)` = operador de atribución causal global respecto de un resultado.

---

## 2. Qué falla en la formulación histórica `R* = eig(W)`

### 2.1 DAG y nilpotencia

Los casos de *Prometeo* y *El cálculo de la responsabilidad* usan ordinariamente grafos dirigidos hacia un nodo final.

Para un DAG ordenado topológicamente, su matriz de adyacencia ponderada es triangular estricta y, por tanto, nilpotente:

`W^m = 0`

para algún `m`.

Todos sus eigenvalores son entonces cero.

Por ello, ni:

`W R* = λR*`

ni:

`W^T R* = λR*`

pueden producir por sí solas un eigenvector dominante positivo y único que distribuya causalidad en esos casos.

La transposición no resuelve la nilpotencia.

### 2.2 Caso Eje de *El cálculo*

El código de referencia imprime una matriz con:

- Institución → Gerentes superiores `0.85`;
- Institución → Subordinadas `0.80`;
- Institución → Perfil de puesto `0.90`;
- Institución → `Nf` `0.80`;
- Gerentes superiores → Subordinadas `0.75`;
- Gerentes superiores → `Nf` `0.70`;
- Subordinadas → `Nf` `0.85`;
- Perfil → Subordinadas `0.70`;
- Perfil → Ex-gerente `0.60`;
- Ex-gerente → `Nf` `0.45`.

La matriz es un DAG y todos sus eigenvalores son `0`.

La iteración publicada `R_{t+1}=W R_t / Σ(W R_t)` no converge al vector impreso: después de sucesivas rondas la masa queda en los nodos de origen y finalmente `W R_t = 0`.

Por tanto, el vector histórico del Caso Eje no es reproducible desde la `W` impresa mediante el algoritmo declarado.

### 2.3 Método Prometeo

Prometeo tampoco ejecuta un eigenvector de `W` en sus casos. Usa:

- rondas de influencia;
- normalizaciones intermedias;
- pesos o aristas acumuladas de rutas;
- reglas especiales para nodos de diseño o nodos sin alimentadores;
- y, en el Apéndice C, una normalización simple `R*(i)=w_i/Σw_j`.

Estas operaciones no son equivalentes entre sí.

**Adjudicación formal de `review.prometeo.rstar_algorithm_equivalence`:**

`NO son algoritmos equivalentes`.

Queda abierto cuál debe sustituirlos en segunda edición.

---

## 3. Separación del grafo respecto del resultado

Sea `D` el resultado analizado.

Defínase el conjunto de nodos causales activos:

`A_D = { i : existe al menos un camino causal i → ... → D }`.

`D` se excluye de la matriz de relaciones entre causas.

Sobre `A_D`, defínase:

`Q_D = [q_ij]`,

con:

`q_ij = w(i → j)`

para relaciones **locales primitivas** entre nodos activos.

Defínase además el vector:

`b_D = (b_i)`,

con:

`b_i = w(i → D)`

cuando existe una relación directa primitiva entre `i` y `D`, y `0` en otro caso.

Esta separación evita tratar el sumidero como una fila ordinaria de una matriz que luego se exige irreducible.

---

## 4. Regla de arista primitiva

Una arista utilizada en `Q_D` o `b_D` debe representar un mecanismo causal local que no sea simplemente el resumen algebraico de rutas ya incluidas.

Si una obra escribe una arista:

`A → D`

como “arista acumulada” que resume:

`A → B → D`

más:

`A → C → D`,

esa arista acumulada puede conservarse como **resultado derivado o visualización**, pero no debe introducirse simultáneamente como entrada junto con las rutas primitivas que ya contiene.

De lo contrario, la misma influencia se contabiliza dos veces.

Esta regla afecta directamente el caso del banco de Prometeo, donde `B → C` se describe como arista estructural acumulada de rutas que también aparecen por separado.

Una arista directa y rutas mediadas sí pueden coexistir cuando la arista directa corresponde a un mecanismo causal independiente, documentado de forma separada.

---

## 5. Atribución total por rutas

La genealogía `φ₁_i → condiciones de j → φ₁_j → ... → D` conduce a la recurrencia:

`r_i(D) = b_i + Σ_j q_ij r_j(D)`.

En forma vectorial:

`r_D = b_D + Q_D r_D`.

Por tanto:

`(I − Q_D) r_D = b_D`.

Si:

`ρ(Q_D) < 1`,

entonces `I − Q_D` es invertible y existe una solución única:

`r_D = (I − Q_D)^−1 b_D`.

Mediante la serie de Neumann:

`r_D = Σ_{k=0}^∞ Q_D^k b_D`.

### Interpretación

- `b_D` = influencia directa sobre `D`;
- `Q_D b_D` = rutas con un intermediario;
- `Q_D² b_D` = rutas con dos intermediarios;
- y así sucesivamente.

Cada camino contribuye mediante el producto de sus pesos locales.

Esto formaliza directamente la intuición de *Transformación formal* y *Prometeo* de que la influencia causal transita por múltiples mediaciones.

---

## 6. Caso especial: DAG

Si el grafo causal es acíclico, `Q_D` es nilpotente.

Entonces:

`ρ(Q_D)=0`

y la serie termina después de un número finito de términos:

`r_D = (I + Q_D + Q_D² + ... + Q_D^m) b_D`.

No se requiere:

- irreducibilidad de la matriz causal;
- fuerte conexidad;
- autolazos causales artificiales;
- teleportación;
- ni convertir el sumidero en un actor.

La existencia de `r_D` es automática para un DAG finito con al menos una ruta hacia `D`.

---

## 7. Normalización

`r_D` mide masa causal relativa antes de normalizar.

Defínase:

`Z_D = 1^T r_D`.

Si `Z_D > 0`, entonces:

`R*(D) = r_D / Z_D`.

Así:

`Σ_i R*_i(D) = 1`.

La normalización expresa que la totalidad de la participación causal representada por el modelo se distribuye entre los nodos de `A_D`.

No convierte por sí sola los pesos locales en probabilidades empíricamente calibradas.

---

## 8. Spectralización sin identificar R* con eig(W)

La suma de rutas proporciona el núcleo computacional. Para conservar la decisión autoral de que `R*` es un **eigenvector de responsabilidad**, se induce después un operador distinto de `W`.

Defínase:

`η_D = 1 / Z_D`.

Y:

`M_R(D) = Q_D + η_D b_D 1^T`.

Como `Σ_i R*_i = 1`:

`M_R(D) R*`

`= Q_D R* + η_D b_D (1^T R*)`

`= Q_D (r_D/Z_D) + b_D/Z_D`

`= (Q_D r_D + b_D)/Z_D`

`= r_D/Z_D`

`= R*`.

Por tanto:

`M_R(D) R*(D) = R*(D)`.

El eigenvalor correspondiente es `1`.

### Qué significa este resultado

`R*` no es el eigenvector de la red causal local.

Es el eigenvector del **operador de responsabilidad inducido por la reconstrucción total de rutas respecto de D**.

La spectralización no sustituye el cálculo causal por rutas; lo representa como un punto fijo lineal del operador de atribución exterior.

---

## 9. Existencia, positividad y Perron–Frobenius del operador inducido

Supóngase:

1. `Q_D ≥ 0`;
2. `b_D ≥ 0`;
3. todo nodo de `A_D` tiene al menos un camino positivo hacia `D`;
4. `ρ(Q_D)<1`.

Entonces:

`r_D = (I−Q_D)^−1 b_D > 0`.

Por tanto:

`R*(D)>0` en todos los nodos que realmente son ancestros causales de `D`.

El operador:

`M_R(D)=Q_D+η_D b_D 1^T`

es no negativo.

Sobre el conjunto de ancestros de `D`, cualquier nodo puede alcanzar mediante `Q_D` algún predecesor directo de `D`; todo predecesor directo con `b_i>0` recibe mediante el término `η_D b_D 1^T` una fila positiva hacia todos los nodos del espacio del operador. Por ello, bajo las hipótesis anteriores, `M_R(D)` resulta irreducible; además, un nodo con `b_i>0` tiene autolazo positivo en `M_R(D)`, de modo que el operador es aperiódico/primitivo.

En esas condiciones, Perron–Frobenius sí se aplica al **operador de responsabilidad**, no a la matriz causal cruda.

`R*` es entonces el único eigenvector de Perron normalizado a suma `1`, y el eigenvalor dominante es `1`.

---

## 10. Forma homogénea equivalente

La recurrencia afín también puede linearizarse aumentando una coordenada:

`M~_R(D) = [[Q_D, b_D], [0^T, 1]]`.

Si:

`r_D = (I−Q_D)^−1 b_D`,

entonces:

`M~_R(D) [r_D; 1] = [r_D; 1]`.

Si `ρ(Q_D)<1`, los eigenvalores de `M~_R(D)` son los de `Q_D` más `1`; por ello `1` es estrictamente dominante en módulo.

Esta forma es útil para implementación y demostración, pero su vector propio incluye una coordenada auxiliar de homogeneización. La forma de la sección anterior mantiene `R*` directamente como eigenvector sobre el espacio de nodos causales.

---

## 11. Ciclos causales

En un sistema con ciclos reales, la serie:

`Σ Q_D^k b_D`

suma todos los recorridos que terminan en `D`.

Para que esa suma sea finita se propone como condición formal:

`ρ(Q_D)<1`.

Esto significa que la influencia total del feedback se atenúa en lugar de crecer indefinidamente.

Si:

`ρ(Q_D) ≥ 1`,

`CAND-RSTAR-001` no define automáticamente un `R*` finito.

Ese resultado debe tratarse como señal de que el sistema requiere al menos una de estas operaciones antes del cálculo:

- desplegar temporalmente el ciclo;
- distinguir eventos repetidos de un mismo nodo;
- redefinir los pesos del feedback;
- introducir una regla de interacción explícita.

No debe añadirse un factor de amortiguación arbitrario sólo para forzar convergencia.

---

## 12. Limitación central: suma de rutas no equivale a independencia causal

La expresión:

`r_D = Σ Q_D^k b_D`

suma contribuciones de caminos.

Esa suma supone que las contribuciones representadas pueden combinarse aditivamente después de componer multiplicativamente los pesos de cada camino.

No es un teorema universal de causalidad.

Si dos rutas comparten un mecanismo, interactúan de manera no aditiva o representan causalidad acumulativa donde ninguna ruta es suficiente por sí sola, será necesario un tratamiento adicional —por ejemplo descomposición de interacción o una regla tipo Shapley— antes de introducirlas en el operador.

Por tanto, `CAND-RSTAR-001` resuelve el problema de propagación y tipado del operador bajo una hipótesis de composición definida; no valida empíricamente que todos los dominios sean aditivos.

---

## 13. Prueba numérica 1 — Prometeo, banco agregado

Pesos centrales entre nodos activos:

- `B→P = 0.90`;
- `B→R = 0.69`;
- `B→A = 0.86`;
- `P→A = 0.64`.

Pesos directos al resultado:

- `R→C = 0.70`;
- `A→C = 0.49`;
- `P→C = 0.64`;
- `B→C = 0.80` en la obra, descrita como arista estructural acumulada.

### Si `B→C` se trata como mecanismo directo independiente

`CAND-RSTAR-001` produce, después de normalizar:

| Nodo | R* candidato |
|---|---:|
| B | 54.45% |
| R | 14.87% |
| A | 10.41% |
| P | 20.26% |

Prometeo publica:

| Nodo | R* publicado |
|---|---:|
| B | 58.0% |
| R | 11.3% |
| A | 17.2% |
| P | 13.5% |

No coinciden.

### Si `B→C` se trata correctamente como resumen de rutas ya presentes

Se elimina de `b_D` para evitar doble conteo.

El candidato produce:

| Nodo | R* candidato sin arista acumulada |
|---|---:|
| B | 45.12% |
| R | 17.92% |
| A | 12.54% |
| P | 24.41% |

Tampoco coincide con el vector publicado.

La diferencia prueba que el método de rondas no es simplemente una suma de caminos ni un eigenvector del operador aquí propuesto.

---

## 14. Prueba numérica 2 — Prometeo, banco descompuesto

Caso del capítulo 4, escenario central.

Relaciones activas:

- `DG→DC = 0.775`;
- `DG→DR = 0.635`;
- `DC→P = 0.920`;
- `DC→A = 0.840`;
- `P→A = 0.635`.

Relaciones directas al resultado:

- `DR→C = 0.660`;
- `DJ→C = 0.390`;
- `A→C = 0.490`.

`CAND-RSTAR-001` produce:

| Nodo | R* candidato |
|---|---:|
| DG | 27.36% |
| DC | 19.89% |
| DR | 18.81% |
| DJ | 11.11% |
| P | 8.87% |
| A | 13.96% |

Prometeo publica aproximadamente:

- DG `43.2%`;
- DC `7.2%`;
- DR `7.9%`;
- DJ `28.1%`;
- A `13.7%`;
- P se pliega editorialmente en DC.

La discrepancia es estructural, no de redondeo.

Además, la ronda publicada introduce para DG un peso acumulado `0.775×0.775=0.601` que la propia obra califica como aproximación y que no corresponde a una cadena explícita con esos dos pesos consecutivos.

---

## 15. Prueba numérica 3 — *El cálculo*, Caso Eje

Separando `Nf` del espacio de causas, se obtiene:

Nodos activos:

- Institución;
- Gerentes superiores;
- Subordinadas;
- Ex-gerente;
- Perfil de puesto.

Con las aristas impresas del código de referencia, `CAND-RSTAR-001` produce:

| Nodo | R* candidato |
|---|---:|
| Institución | 49.22% |
| Gerentes superiores | 19.39% |
| Subordinadas | 12.32% |
| Ex-gerente | 6.52% |
| Perfil de puesto | 12.54% |

La obra publica para el Hecho 1 una distribución de cuatro nodos:

- Institución `45.1%`;
- Subordinadas `30.8%`;
- Gerentes superiores `13.7%`;
- Antiguo gerente `10.4%`;

con Perfil de puesto fuera de esa suma final.

El vector publicado no se obtiene ni de la iteración de potencia impresa ni de `CAND-RSTAR-001` aplicado literalmente a la matriz publicada.

**Conclusión de `review.calc.published_vectors_reproduction`:**

queda demostrado que el operador declarado en primera edición no reproduce los porcentajes impresos. Permanece abierta la procedencia histórica exacta de esos valores y deberán recalcularse en segunda edición una vez adjudicado el operador.

---

## 16. Normalización simple `w/Σw`

La regla del Apéndice C de Prometeo:

`R*(i)=w_i/Σ_j w_j`

sólo coincide con una distribución causal por rutas en el caso degenerado donde:

- cada nodo posee un único peso directamente comparable hacia `D`;
- no existen relaciones causales entre nodos activos;
- no hay mediaciones transitivas.

En cuanto existe:

`A → B → D`,

la normalización de pesos locales no captura la participación mediada de `A`.

Por ello no puede ser el algoritmo universal de `R*`.

---

## 17. Interpretación de orientación

Bajo la convención:

`Q_ij = w(i → j)`,

la recurrencia correcta es:

`r_i = b_i + Σ_j Q_ij r_j`.

Es decir:

`r = b + Qr`.

No se necesita transponer semánticamente la matriz.

El vector `r_j` representa cuánto del resultado pertenece causalmente al nodo downstream `j`; multiplicar por `Q_ij` retorna hacia `i` la fracción de esa participación cuya condición local fue `i`.

La dirección de la arista permanece `i→j`; lo que cambia es la **dirección de lectura de la atribución exterior**.

Esto es coherente con `δ_ext`: se parte del resultado y se reconstruye hacia sus condiciones sin invertir la causalidad ontológica.

---

## 18. Tratamiento del nodo final

`D` no entra como un componente de `R*`.

Su función es definir:

- qué resultado se distribuye;
- cuáles nodos son ancestros causales relevantes;
- cuál es el vector directo `b_D`.

Por tanto, desaparece la exigencia contradictoria de que una matriz que contiene un sumidero de fila nula sea simultáneamente irreducible o fuertemente conexa.

La irreducibilidad, cuando se necesite para la representación espectral, se evalúa sobre `M_R(D)`, no sobre la red causal cruda.

---

## 19. Estatuto de las revisiones

### Respondida negativamente

`review.prometeo.rstar_algorithm_equivalence`

La equivalencia entre:

- rondas de Prometeo;
- `w/Σw`;
- eigenvector de `W`;

queda descartada formalmente.

### Respondida parcialmente

`review.calc.published_vectors_reproduction`

Se establece que los vectores publicados no son reproducibles con la matriz y algoritmo declarados. La procedencia exacta de los porcentajes históricos queda abierta.

### Candidato de resolución si se adopta CAND-RSTAR-001

- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`;
- revisiones sobre Perron–Frobenius aplicadas a la `W` causal.

No se cierran todavía porque su resolución depende de adjudicar formalmente el nuevo operador.

---

## 20. Qué CAND-RSTAR-001 resuelve

Si se adopta, el candidato resuelve simultáneamente:

1. propagación causal en DAG;
2. separación entre causalidad local y responsabilidad global;
3. tratamiento del resultado sin convertirlo en actor;
4. composición de rutas mediante productos de pesos;
5. acumulación de rutas mediante suma explícita;
6. orientación fila-origen `i→j`;
7. existencia única en DAG;
8. condición clara para ciclos: `ρ(Q)<1`;
9. conservación de `R*` como eigenvector de un operador de responsabilidad;
10. aplicación correcta de Perron–Frobenius al operador inducido y no a `W`.

---

## 21. Qué permanece abierto

Incluso si se adopta este operador, todavía requieren trabajo propio:

- validación/calibración empírica de los pesos `w`;
- independencia o interacción entre rutas;
- causalidad acumulativa;
- tratamiento de rutas que comparten mecanismos;
- reglas para hipergrafos o condiciones conjuntas;
- ciclos con `ρ(Q)≥1`;
- temporalización de feedback;
- reasignación de nodos instrumentales a diseñadores sin alterar el cálculo causal original;
- comparación con Shapley en casos sin condición necesaria individual;
- recalibración de todos los casos publicados en segunda edición.

---

## 22. Criterio de adjudicación futura

`CAND-RSTAR-001` puede pasar a resolución vigente únicamente si se acepta expresamente esta jerarquía:

1. la ontología determina qué significa causalidad y atribución;
2. `W` representa relaciones locales de `φ₁`;
3. la suma de rutas reconstruye la atribución exterior total respecto de `D`;
4. `R*` es la normalización de esa atribución;
5. el operador espectral `M_R(D)` se induce a partir de esa reconstrucción y tiene a `R*` como Perron-eigenvector.

En forma compacta:

`φ₁ encadenadas → Q_D,b_D → r_D=(I−Q_D)^−1b_D → R*(D)`

`R*(D) = Perron(M_R(D))`

con:

`M_R(D)=Q_D+η_D b_D 1^T`

`η_D=[1^T(I−Q_D)^−1b_D]^−1`.

Esta formulación conserva la genealogía del sistema y evita exigir a la matriz causal local propiedades que pertenecen al operador de atribución exterior.

---

## 23. Proveniencia revisada

Lectura transversal utilizada:

- `corpus/fuentes/Caos_El_abismo_del_ego_y_la_doble_mediacion.md` — fórmula del ego;
- `corpus/fuentes/Afrodita_Areia_Areopopago.md` — Apéndice II, `δ_int/δ_ext`;
- `corpus/fuentes/La_transformacion_formal_ontologia_del_ego_como_fundamento_del_calculo_causal.md` — cap. 2.1, caminos y eigenvector;
- `corpus/fuentes/Axiomatizacion_Sistema_Doble_Mediacion.md` — R*, orientación y sumidero;
- `corpus/fuentes/Metrologia_Causal_La_ciencia_de_la_medicion_causal.md` — propagación y validez de R*;
- `corpus/fuentes/El_calculo_de_la_responsabilidad.md` — definición, teoremas, código y Caso Eje;
- `corpus/fuentes/El_metodo_Prometeo_imputacion_causal_para_juristas_y_abogados.md` — caps. 2–4 y Apéndice C;
- `mapa/mapa-maestro.json` — revisiones históricas y rutas de recuperación.

No se ha modificado ninguna fuente canónica ni el mapa maestro congelado.
