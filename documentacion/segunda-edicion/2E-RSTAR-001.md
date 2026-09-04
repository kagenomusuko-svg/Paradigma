# 2E-RSTAR-001 — Normalización de R* desde la fórmula del ego

> **Entrada editorial derivada para segunda edición.** Pertenece al registro abierto en `documentacion/segunda-edicion.md` y se apoya en `documentacion/normalizacion-rstar-formula-ego.md` (`NORM-RSTAR-EGO-001`). No modifica las fuentes canónicas de primera edición.

- **Estado:** PREPARADO PARA SEGUNDA EDICIÓN
- **Prioridad:** MUY ALTA
- **Normalización de referencia:** `NORM-RSTAR-EGO-001`
- **Tipo de problema:** crosswalk ontológico-formal, tipado del operador de responsabilidad y múltiples algoritmos históricos
- **Decisión autoral vigente:** `R*` se conserva como **eigenvector de responsabilidad**
- **No adjudicado todavía:** construcción matemática exacta de `M_R(D)`

---

## 1. Corrección nuclear de segunda edición

La segunda edición deberá distinguir explícitamente los siguientes objetos:

`φ₁`

= primera mediación; produce el acto/colapso bajo voluntad y condiciones.

`W`

= matriz de determinaciones locales entre nodos; `W_ij` representa cuánto determinó `i` el colapso/comportamiento de `j` bajo la convención `i → j`.

`δ_ext`

= operación exterior de atribución del colapso producido por `φ₁` al nodo cuya cadena causal es reconstruible; es estructuralmente análoga al retorno atributivo de `φ₂`, pero no mide `φ₂` interna.

`M_R(D)`

= símbolo editorial provisional del operador de responsabilidad que transforma la red local `W` en atribución causal global respecto del resultado `D`.

`R*(D)`

= distribución relativa de participación causal respecto de `D`, normalizada para sumar 1, y conservada autoralmente como eigenvector de responsabilidad.

`φ₂`

= segunda mediación; retorno/asunción del acto al ego.

`α`

= coeficiente de asunción efectiva, conforme a `RES-ALPHA-001`.

`Δ`

= diferencia `R* − α`, conforme a `RES-DELTA-001`.

---

## 2. Esquema editorial obligatorio

La relación normalizada deberá presentarse de forma equivalente a:

```text
v_i, c_i
   │
   ▼
 φ₁,i
   │
   ▼
 a_i ──────────────────────────────┐
   │                               │
   │ entra en el campo de j        │ retorno/asunción
   ▼                               ▼
 c_j                              φ₂,i
   │                               │
   ▼                               ▼
 φ₁,j                           I_i(t+1)
   │                               │
   ▼                               ▼
 ...                              α_i
   │
   ▼
 D

φ₁ encadenadas → W → M_R(D) → R*(D)

R*_i − α_i = Δ_i
```

Forma compacta:

`v,c → φ₁ → a → W → M_R(D) → R*`

`a → φ₂ → I(t+1) → α`

`R* − α = Δ`.

---

## 3. Caos — fórmula del ego

### Conservar

La fórmula individual del ego como arquitectura de doble mediación:

`Ego_i(t) = φ₂,i(φ₁,i(v_i,c_i), I_i(t))`.

### Aclarar en segunda edición o aparato editorial

Cuando se conecte la fórmula del ego con responsabilidad colectiva, deberá explicitarse que el acto `a_i` puede entrar en las condiciones `c_j` de otro ego.

La transición conceptual es:

`acto de i → condición de j → nuevo colapso de j`.

Ésta es la raíz ontológica del grafo causal y de la composición de rutas.

### No añadir retrospectivamente

No debe presentarse el eigenvector como contenido ya implícito en la fórmula individual. La fórmula del ego exige encadenabilidad causal; el uso espectral es una formalización posterior.

---

## 4. Areópago — δ_int y δ_ext

### Conservar

La distinción:

- `δ_int` requiere `φ₂` interna;
- `δ_ext` atribuye exteriormente el colapso de `φ₁` cuando existe cadena causal reconstruible.

### Aclarar

La expresión «imputación como derivada exterior de la segunda mediación» deberá acompañarse de la precisión:

> la exterioridad reproduce la **estructura atributiva** de `φ₂`, pero opera sobre los colapsos y cadenas causales de `φ₁`.

Esta aclaración evita identificar imputación exterior con reconocimiento interno o asunción subjetiva.

---

## 5. Transformación formal, cap. 2.1

### Problema histórico

El capítulo presenta R* como «lectura exterior de la distribución de φ₂» y deriva el eigenvector directamente de `W`.

### Corrección conceptual

La segunda edición deberá sustituir la identidad semántica:

`R* = distribución de φ₂`

por:

`R* = distribución exterior de atribución causal de colapsos de φ₁ respecto de D`.

La operación de retorno es estructuralmente análoga a `φ₂`; el material atribuido es causal y procede de `φ₁`.

### Corrección formal pendiente

No deberá mantenerse como teorema demostrado:

`W · R* = λR*`

hasta que se pruebe que la matriz usada es efectivamente el operador de responsabilidad requerido.

La forma objetivo, pendiente de construcción, será:

`M_R(D) · R*(D) = λ_R · R*(D)`.

### Conservar

Debe conservarse la intuición correcta del capítulo:

- influencia transitiva;
- contribución por múltiples caminos;
- producto de pesos a lo largo de una ruta;
- necesidad de distribuir la totalidad del resultado entre múltiples condiciones causales.

---

## 6. Axiomatización — R*, Wᵀ y nodo sumidero

La segunda edición deberá separar tres cuestiones que la primera edición aproxima como una sola:

1. convención local de orientación de `W`;
2. construcción del operador global `M_R(D)`;
3. condiciones espectrales necesarias para obtener `R*`.

No debe resolverse `W` frente a `Wᵀ` sólo por notación antes de construir `M_R(D)`.

El nodo final `D` deberá tiparse como resultado respecto del cual se distribuye causalidad, no como nodo de responsabilidad homogéneo a sus causas.

La incompatibilidad histórica entre:

- sumidero con fila nula;
- estocasticidad por filas;
- fuerte conexidad/irreducibilidad;

debe revisarse después de fijar el operador correcto.

---

## 7. Metrología Causal

La segunda edición deberá conservar que R* intenta medir influencia causal total y no sólo proximidad al resultado.

Sin embargo, deberá distinguir:

`matriz causal local W`

frente a:

`operador de atribución global M_R(D)`.

No deberá afirmarse que la iteración de potencia sobre la matriz causal cruda resuelve automáticamente la propagación en DAG si esa matriz es nilpotente.

Las condiciones de Perron–Frobenius deberán declararse sobre el operador que realmente se utilice, no importarse automáticamente desde la matriz de adyacencia causal.

---

## 8. El cálculo de la responsabilidad

### Conservar

- R* como vector de responsabilidad causal;
- normalización `ΣR*_i = 1`;
- carácter descriptivo y no moral de R*;
- dependencia de las relaciones causales y sus pesos;
- objetivo de capturar mediación/transitividad.

### Revisar

Toda afirmación que identifique sin prueba:

`R* = eigenvector dominante de W`.

La segunda edición deberá declarar qué operador produce los vectores publicados y bajo qué condiciones.

La revisión deberá intentar reproducir todos los casos numéricos publicados.

Si un vector publicado no puede reproducirse desde el operador formal finalmente adoptado, deberá:

1. conservarse como resultado histórico de primera edición;
2. corregirse en segunda edición;
3. documentarse la diferencia y su causa.

---

## 9. Método Prometeo — rondas, rutas y normalización simple

Prometeo conserva información decisiva sobre la intención operativa de R*.

### Conservar

El método muestra que la responsabilidad debe acumular influencia a través de rutas:

`diseñador → ejecutor → resultado`.

También muestra que nodos sin arista directa al resultado pueden conservar participación causal upstream.

### Revisar

La obra utiliza al menos:

1. método de rondas en los casos;
2. aristas o pesos acumulados de rutas;
3. normalización simple `R*(i)=w_i/Σw_j` en el Apéndice C.

Estas operaciones no deben seguir presentándose como automáticamente equivalentes entre sí ni equivalentes a una formulación eigenvectorial.

### Doble contabilización

Cuando una arista acumulada ya represente rutas indirectas, la segunda edición deberá verificar que esas mismas rutas no vuelvan a añadirse separadamente.

### Nodo de diseño

La afirmación de que el nodo de diseño suele obtener R* alto puede conservarse como patrón o hipótesis del método, pero no como propiedad garantizada por definición antes de la validación formal.

---

## 10. Estatuto de M_R(D)

Hasta nueva adjudicación, `M_R(D)` es:

- una normalización conceptual;
- un tipo de objeto necesario para separar red causal y operador de responsabilidad;
- un objetivo de formalización.

No es todavía:

- una matriz explícitamente construida;
- un teorema;
- una regularización validada;
- un algoritmo listo para implementación.

La segunda edición no deberá escoger una fórmula para `M_R(D)` por elegancia matemática. La construcción deberá derivarse de las propiedades causales que el corpus exige y contrastarse con los casos publicados.

---

## 11. Pruebas formales mínimas antes de incorporar la corrección

Antes de pasar esta entrada a **INCORPORADO**, cualquier candidato a `M_R(D)` deberá superar como mínimo:

### Prueba 1 — DAG simple

Para:

`A → B → D`

con pesos positivos, `A` y `B` deben poder recibir participación causal no nula respecto de `D`.

### Prueba 2 — ruta directa + ruta mediada

Para:

`A → D`

más:

`A → B → D`,

el operador debe combinar ambas rutas sin perder la mediación ni contar dos veces la misma contribución.

### Prueba 3 — múltiples rutas

Para:

`A → B → D`

`A → C → D`,

ambas rutas deben contribuir de forma explícitamente definida.

### Prueba 4 — nodo final

`D` debe funcionar como resultado respecto del cual se atribuye causalidad. Su tratamiento no debe forzar una falsa irreducibilidad de la red de actores.

### Prueba 5 — orientación

La convención `W_ij = i → j` deberá producir el mismo significado causal en todas las ecuaciones del operador. Si se usa una transpuesta, deberá justificarse como transformación algebraica y no como cambio semántico inadvertido.

### Prueba 6 — ciclos

Debe definirse qué ocurre cuando existen ciclos causales reales sin convertir artificialmente todo DAG en grafo cíclico.

### Prueba 7 — existencia y unicidad

Deberán explicitarse las condiciones bajo las cuales existe un eigenvector relevante único y positivo.

### Prueba 8 — reproducción de Prometeo

El candidato deberá aplicarse, al menos, al caso del banco y a los casos con rutas acumuladas de Prometeo.

### Prueba 9 — reproducción de El cálculo

Deberán reconstruirse los vectores publicados a partir de los pesos y grafos impresos o documentarse por qué no son reproducibles.

### Prueba 10 — independencia de α

Modificar α sin alterar la estructura causal no deberá modificar R*.

Esto preserva la separación:

`R*` = causalidad;

`α` = asunción efectiva.

---

## 12. Revisiones que NO se cierran

Esta entrada no resuelve:

- `review.prometeo.rstar_algorithm_equivalence`;
- `review.prometeo.design_node_presumption`;
- `review.calc.rstar_equivalence`;
- `review.calc.orientation`;
- `review.calc.sinks`;
- `review.calc.published_vectors_reproduction`;
- `review.rstar.sink_irreducibility`;
- `review.tf.rstar_orientation`;
- `review.axiom.rstar_sink`;
- `review.mci.rstar_orientation`;
- `review.mcii.sink_normalization`;
- revisiones sobre periodicidad, conectividad, autolazos, contracción y condiciones de Perron–Frobenius.

Su función es proporcionar el tipado conceptual necesario para resolverlas correctamente después.

---

## 13. Criterio editorial de cierre

`2E-RSTAR-001` sólo podrá pasar a **INCORPORADO** cuando:

1. `M_R(D)` tenga una construcción formal explícita;
2. estén definidos dominio, codominio y orientación;
3. se haya demostrado la relación entre `W` y `M_R(D)`;
4. las condiciones espectrales estén correctamente formuladas;
5. se hayan probado DAG, rutas múltiples, sumidero y ciclos;
6. se haya descartado o controlado doble contabilización;
7. los casos de Prometeo y El cálculo hayan sido reproducidos o corregidos documentalmente;
8. las fórmulas por obra se hayan actualizado sin borrar la historia de primera edición;
9. `R*`, α y Δ permanezcan tipados como objetos distintos;
10. ninguna formulación matemática sea elevada a validación empírica por el mero hecho de estar formalizada.

---

## 14. Fórmula editorial de referencia

Hasta que se complete la formalización, la segunda edición deberá usar como crosswalk conceptual:

`φ₁ → W → M_R(D) → R*(D)`

`φ₂ → α`

`Δ = R* − α`.

Con la precisión:

> `R*` es el eigenvector de responsabilidad; `M_R(D)` es el operador cuya construcción formal debe determinarse. `W` representa las determinaciones causales locales y no debe identificarse automáticamente con ese operador.
