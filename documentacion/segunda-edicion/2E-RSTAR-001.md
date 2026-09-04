# 2E-RSTAR-001 — Normalización y reconstrucción formal de R* desde la fórmula del ego

> **Entrada editorial derivada para segunda edición.** Pertenece al registro abierto en `documentacion/segunda-edicion.md`. Se apoya en `documentacion/normalizacion-rstar-formula-ego.md` (`NORM-RSTAR-EGO-001`) y en `documentacion/candidato-operador-rstar.md` (`AUD-RSTAR-001` / `CAND-RSTAR-001`). No modifica las fuentes canónicas de primera edición.

- **Estado:** PREPARADO PARA SEGUNDA EDICIÓN / CANDIDATO FORMAL EN PRUEBA
- **Prioridad:** MUY ALTA
- **Normalización conceptual:** `NORM-RSTAR-EGO-001`
- **Auditoría formal:** `AUD-RSTAR-001`
- **Candidato preferente:** `CAND-RSTAR-001`
- **Decisión autoral vigente:** `R*` se conserva como **eigenvector de responsabilidad**
- **No adjudicado todavía como canon:** adopción definitiva de `CAND-RSTAR-001`

---

## 1. Crosswalk obligatorio

La segunda edición deberá distinguir explícitamente:

`φ₁`

= primera mediación; produce el acto/colapso bajo voluntad y condiciones.

`W`

= representación de determinaciones causales locales bajo la convención `W_ij = w(i→j)`.

`δ_ext`

= atribución exterior del colapso producido por `φ₁` al nodo cuya cadena causal es reconstruible; reproduce la estructura atributiva de `φ₂`, pero no mide `φ₂` interna.

`M_R(D)`

= operador de responsabilidad respecto del resultado `D`; no debe identificarse automáticamente con la matriz causal cruda `W`.

`R*(D)`

= distribución relativa de participación causal respecto de `D`, normalizada a suma `1`.

`φ₂`

= segunda mediación; retorno/asunción del acto al ego.

`α`

= coeficiente de asunción efectiva conforme a `RES-ALPHA-001`.

`Δ`

= `R*−α`, conforme a `RES-DELTA-001`.

Esquema mínimo:

```text
v_i,c_i → φ₁,i → a_i → entra en c_j → φ₁,j → ... → D
                                              │
                                              └─ atribución exterior → R*(D)

a_i → φ₂,i → I_i(t+1) → α_i

Δ_i = R*_i − α_i
```

Forma compacta:

`φ₁ encadenadas → W → M_R(D) → R*(D)`

`φ₂ → α`

`Δ = R* − α`.

---

## 2. Caos — fórmula del ego

### Conservar

`Ego_i(t)=φ₂,i(φ₁,i(v_i,c_i),I_i(t))`.

### Aclarar

El paso del ego individual al campo causal ocurre cuando:

`acto de i → condición de j → nuevo colapso de j`.

Ésta es la raíz ontológica de la composición de rutas.

### No añadir retrospectivamente

El eigenvector no estaba contenido como objeto matemático dentro de la fórmula individual. La fórmula exige encadenabilidad causal; la spectralización es una formalización posterior.

---

## 3. Areópago — δ_int y δ_ext

### Conservar

- `δ_int` requiere `φ₂` interna;
- `δ_ext` requiere que `φ₁` haya ocurrido y que la cadena causal sea reconstruible.

### Aclarar

La expresión «derivada exterior de la segunda mediación» deberá acompañarse de esta precisión:

> la imputación exterior reproduce la estructura de retorno atributivo de `φ₂`, pero opera sobre actos y cadenas causales producidos por `φ₁`.

Esto separa causalidad de reconocimiento/asunción interna.

---

## 4. Transformación formal, cap. 2.1

### Conservar

- influencia transitiva;
- múltiples caminos;
- producto de pesos dentro de una ruta;
- necesidad de distribuir un resultado entre múltiples condiciones causales.

### Corregir

No mantener como identidad semántica:

`R* = distribución de φ₂`.

Usar:

`R* = distribución exterior de atribución causal de colapsos de φ₁ respecto de D`.

No mantener como teorema general:

`W R* = λR*`.

La segunda edición deberá usar el operador de responsabilidad finalmente adjudicado.

---

## 5. Axiomatización — Wᵀ, sumidero e irreducibilidad

La segunda edición deberá separar:

1. orientación local de `W`;
2. tratamiento del resultado `D`;
3. operador global de responsabilidad;
4. condiciones espectrales.

El resultado `D` no debe tratarse como actor homogéneo a las causas.

La combinación histórica:

- fila nula del sumidero;
- matriz supuestamente estocástica por filas;
- fuerte conexidad/irreducibilidad;

no debe conservarse sin corrección formal.

La transposición no resuelve el problema de fondo: una matriz de un DAG sigue siendo nilpotente tanto si se usa `W` como `Wᵀ`.

---

## 6. Metrología Causal

Conservar el objetivo de medir influencia causal total y no sólo proximidad al resultado.

Corregir la identificación automática entre:

`matriz causal local W`

y:

`operador espectral de responsabilidad`.

Las condiciones de Perron–Frobenius deberán formularse sobre `M_R(D)` si el operador adjudicado las satisface, no sobre la matriz de adyacencia causal por mera convención.

---

## 7. El cálculo de la responsabilidad

### Conservar

- `R*` como distribución causal descriptiva;
- `ΣR*_i=1`;
- independencia respecto de dolo y α;
- intención de capturar mediación/transitividad.

### Hallazgo formal ya establecido

Las matrices impresas de los casos revisados son DAG y, por tanto, nilpotentes. La iteración de potencia sobre `W` declarada por la obra no puede converger a los vectores positivos publicados.

En el Caso Eje, el código impreso termina en un vector nulo después de un número finito de multiplicaciones porque `W^m=0`.

Por ello:

`review.calc.published_vectors_reproduction`

queda adjudicada en el siguiente sentido:

> **el operador declarado no reproduce los porcentajes publicados**.

Permanece abierta únicamente la procedencia histórica exacta de esos porcentajes.

La segunda edición deberá recalcular los casos con el operador finalmente adoptado y conservar los porcentajes de primera edición sólo como registro histórico.

---

## 8. Método Prometeo

### Conservar

Prometeo preserva la intuición operativa correcta:

`diseñador → ejecutor → resultado`

puede atribuir causalidad al diseñador aunque no exista una arista directa única al resultado.

### Hallazgo formal ya establecido

Prometeo usa bajo `R*` al menos tres procedimientos distintos:

1. rondas con normalizaciones intermedias;
2. aristas/pesos acumulados de rutas y reglas especiales por caso;
3. `R*(i)=w_i/Σw_j` en el Apéndice C.

No son equivalentes entre sí ni al eigenvector de `W`.

Por tanto:

`review.prometeo.rstar_algorithm_equivalence`

queda respondida:

> **NO existe equivalencia algorítmica demostrable entre esas formulaciones; de hecho, producen objetos distintos en grafos no triviales.**

### Regla editorial nueva

Una arista acumulada que resume rutas ya presentes no puede utilizarse simultáneamente como entrada del cálculo junto con esas mismas rutas.

Debe distinguirse:

- arista primitiva documentada;
- arista derivada/acumulada para visualización o síntesis.

---

## 9. CAND-RSTAR-001 — separación Q_D / b_D

Sea `D` el resultado analizado y:

`A_D={i : i→...→D}`

el conjunto de sus ancestros causales.

`D` se excluye del espacio de causas.

Defínase:

`Q_D=[q_ij]`

con:

`q_ij=w(i→j)`

para aristas primitivas entre nodos activos.

Defínase:

`b_D=(b_i)`

con:

`b_i=w(i→D)`

para mecanismos directos primitivos hacia el resultado.

---

## 10. Núcleo computacional candidato: atribución por rutas

La recurrencia normalizada por la genealogía es:

`r_i(D)=b_i+Σ_j q_ij r_j(D)`.

En vector:

`r_D=b_D+Q_D r_D`.

Si:

`ρ(Q_D)<1`,

entonces:

`r_D=(I−Q_D)^−1 b_D`.

Y:

`r_D=Σ_{k=0}^∞ Q_D^k b_D`.

Interpretación:

- `b_D`: influencia directa;
- `Q_D b_D`: un intermediario;
- `Q_D² b_D`: dos intermediarios;
- etc.

En un DAG, `Q_D` es nilpotente, `ρ(Q_D)=0` y la suma es finita.

---

## 11. Normalización de R*

Defínase:

`Z_D=1^T r_D`.

Entonces:

`R*(D)=r_D/Z_D`.

Por construcción:

`Σ_i R*_i=1`.

Un nodo sin camino hacia `D` no pertenece a `A_D` y no recibe responsabilidad por ese resultado.

---

## 12. Operador espectral inducido

Para conservar `R*` como eigenvector de responsabilidad sin identificarlo con `eig(W)`, defínase:

`η_D=1/Z_D`.

Y:

`M_R(D)=Q_D+η_D b_D 1^T`.

Entonces:

`M_R(D)R*(D)=R*(D)`.

El eigenvalor es `1`.

Bajo:

- `Q_D≥0`;
- `b_D≥0`;
- todo nodo de `A_D` tiene un camino positivo hacia `D`;
- `ρ(Q_D)<1`;

se obtiene `R*>0` sobre `A_D`. El término de retorno hace que el operador inducido sea irreducible y aperiódico sobre el espacio causal relevante, por lo que Perron–Frobenius se aplica al **operador de responsabilidad**.

La spectralización es derivada: la suma de rutas establece la atribución causal y `M_R(D)` representa esa atribución como eigenvector estable.

---

## 13. Forma homogénea equivalente

Como control algebraico puede utilizarse:

`M~_R(D)=[[Q_D,b_D],[0^T,1]]`.

Entonces:

`M~_R(D)[r_D;1]=[r_D;1]`.

Si `ρ(Q_D)<1`, el eigenvalor `1` es estrictamente dominante sobre los eigenvalores de `Q_D`.

Esta forma sirve para demostración/implementación, pero la forma de la sección anterior conserva `R*` directamente como eigenvector sobre los nodos causales.

---

## 14. Resultados de reproducción ya obtenidos

### Prometeo — banco agregado

Con `B→C=0.80` tratado como mecanismo directo independiente:

| Nodo | CAND-RSTAR-001 | Publicado |
|---|---:|---:|
| B | 54.45% | 58.0% |
| R | 14.87% | 11.3% |
| A | 10.41% | 17.2% |
| P | 20.26% | 13.5% |

Si `B→C` se trata conforme a la propia descripción de la obra como arista acumulada y se excluye para evitar doble conteo:

| Nodo | CAND-RSTAR-001 |
|---|---:|
| B | 45.12% |
| R | 17.92% |
| A | 12.54% |
| P | 24.41% |

Ninguna variante reproduce las rondas publicadas.

### Prometeo — banco descompuesto

| Nodo | CAND-RSTAR-001 | Publicado aprox. |
|---|---:|---:|
| DG | 27.36% | 43.2% |
| DC | 19.89% | 7.2% |
| DR | 18.81% | 7.9% |
| DJ | 11.11% | 28.1% |
| P | 8.87% | plegado en DC |
| A | 13.96% | 13.7% |

La diferencia es estructural.

### El cálculo — Caso Eje

Aplicando el candidato a las aristas impresas:

| Nodo | CAND-RSTAR-001 | Publicado |
|---|---:|---:|
| Institución | 49.22% | 45.1% |
| Gerentes superiores | 19.39% | 13.7% |
| Subordinadas | 12.32% | 30.8% |
| Ex-gerente | 6.52% | 10.4% |
| Perfil de puesto | 12.54% | omitido de la suma final |

Por tanto, adoptar el candidato exige **recalcular**, no intentar conservar artificialmente los porcentajes históricos.

---

## 15. Pruebas mínimas: estado actual

| Prueba | Estado con CAND-RSTAR-001 |
|---|---|
| DAG simple | SUPERADA |
| ruta directa + mediada | SUPERADA bajo regla de arista primitiva |
| múltiples rutas | SUPERADA bajo suma aditiva explícita |
| nodo final/sumidero | SUPERADA: D separado en `b_D` |
| orientación `i→j` | SUPERADA: `r=b+Qr` |
| existencia/Unicidad en DAG | SUPERADA |
| ciclos | CONDICIONAL: requiere `ρ(Q)<1` |
| Perron–Frobenius | SUPERADA para `M_R(D)` bajo hipótesis declaradas |
| independencia de α | SUPERADA por construcción |
| reproducción histórica | NO: obliga a corrección de segunda edición |

La falta de reproducción histórica no invalida el candidato; demuestra que la primera edición utilizó procedimientos incompatibles. La adopción final requiere decidir si el candidato representa correctamente el objeto doctrinal, no si imita errores numéricos previos.

---

## 16. Problemas todavía abiertos

CAND-RSTAR-001 no resuelve por sí solo:

- calibración empírica de `w`;
- interacción no aditiva entre rutas;
- rutas que comparten mecanismos;
- causalidad acumulativa;
- hipergrafos o condiciones conjuntas;
- feedback con `ρ(Q)≥1`;
- temporalización de ciclos;
- reasignación de participación de nodos instrumentales a sus diseñadores;
- comparación con Shapley;
- `review.prometeo.design_node_presumption`.

La afirmación de que un nodo de diseño suele dominar puede conservarse como hipótesis/patrón, no como propiedad garantizada por el operador.

---

## 17. Revisiones y estado editorial

### Respondida

`review.prometeo.rstar_algorithm_equivalence`

Resultado: **NO equivalencia**.

### Respondida en su parte negativa

`review.calc.published_vectors_reproduction`

Resultado: **el algoritmo/matriz declarados no reproducen los vectores impresos**. La procedencia histórica exacta continúa abierta.

### Pendientes de adopción de CAND-RSTAR-001

- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`;
- periodicidad, autolazos, contracción y otras condiciones espectrales heredadas.

Si `CAND-RSTAR-001` se adopta, varias de estas revisiones dejan de ser problemas del grafo causal y pasan a resolverse por el tipado correcto del operador.

---

## 18. Criterio de cierre de 2E-RSTAR-001

La entrada podrá pasar a **INCORPORADO** cuando:

1. `CAND-RSTAR-001` sea adjudicado o sustituido por un operador mejor;
2. se documente la hipótesis de composición entre rutas;
3. se establezca protocolo para ciclos;
4. se recalculen sistemáticamente todos los ejemplos afectados;
5. se corrijan los teoremas de existencia/convergencia;
6. se elimine la identificación automática `W=eigen-operador`;
7. se tipen las aristas primitivas frente a las acumuladas;
8. se preserve la historia de primera edición;
9. `R*`, `α` y `Δ` permanezcan separados;
10. ninguna formalización sea presentada como validación empírica por el solo hecho de ser matemática.

---

## 19. Fórmula editorial de referencia durante la revisión

Hasta adjudicación final:

`φ₁ encadenadas → Q_D,b_D → r_D=(I−Q_D)^−1b_D → R*(D)`

`R*(D)=Perron(M_R(D))`

con:

`M_R(D)=Q_D+η_D b_D 1^T`

`η_D=[1^T(I−Q_D)^−1b_D]^−1`.

En paralelo:

`φ₂ → α`

`Δ=R*−α`.

La prioridad editorial es preservar la genealogía: la matemática debe representar el objeto causal definido por el sistema, no redefinir el objeto para salvar una fórmula histórica.
