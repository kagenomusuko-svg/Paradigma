# VAL-RSTAR-001 — Validación estructural de CAND-RSTAR-001

> **Documento derivado de mantenimiento, no fuente canónica.** Valida estructuralmente el candidato definido en `documentacion/candidato-operador-rstar.md`. No constituye por sí solo la adjudicación autoral definitiva del operador.

- **ID:** `VAL-RSTAR-001`
- **Candidato:** `CAND-RSTAR-001`
- **Estado:** **BATERÍA ESTRUCTURAL SUPERADA EN EL DOMINIO DECLARADO**
- **Dominio provisional:** grafos causales finitos con pesos no negativos, aristas primitivas y `ρ(Q_D)<1`

---

## 1. Fórmulas sometidas a prueba

Sea `D` el resultado y `Q_D` la matriz de determinaciones locales entre sus ancestros causales. Sea `b_D` el vector de influencias primitivas directas sobre `D`.

Núcleo de atribución:

`r_D=b_D+Q_D r_D`.

Solución:

`r_D=(I−Q_D)^−1 b_D`.

Normalización final:

`Z_D=1^T r_D`.

`R*(D)=r_D/Z_D`.

Operador inducido:

`η_D=1/Z_D`.

`M_R(D)=Q_D+η_D b_D 1^T`.

Propiedad espectral:

`M_R(D)R*(D)=R*(D)`.

---

## 2. Prueba sintética A — DAG simple

Grafo:

`A --0.8→ B --0.5→ D`.

Entonces:

`r_B=0.5`.

`r_A=0.8×0.5=0.4`.

Normalización:

`R*_A=0.4/0.9=44.44%`.

`R*_B=0.5/0.9=55.56%`.

Resultado:

- ambos nodos reciben participación causal;
- el nodo upstream no desaparece;
- no se requiere ciclo ni arista ficticia de retorno en el grafo causal.

**Estado:** SUPERADA.

---

## 3. Prueba sintética B — ruta directa + mediada

Grafo:

`A --0.2→ D`

más:

`A --0.8→ B --0.5→ D`.

Si la arista directa representa un mecanismo independiente:

`r_B=0.5`.

`r_A=0.2+(0.8×0.5)=0.6`.

Normalización:

`R*_A=54.55%`.

`R*_B=45.45%`.

La ruta directa y la mediada se combinan sin confundir sus niveles.

Si `A→D` fuera sólo un resumen de `A→B→D`, deberá excluirse como entrada por la regla de arista primitiva.

**Estado:** SUPERADA.

---

## 4. Prueba sintética C — rutas paralelas

Grafo:

`A --0.5→ B --0.6→ D`

`A --0.4→ C --0.7→ D`.

Entonces:

`r_B=0.6`.

`r_C=0.7`.

`r_A=(0.5×0.6)+(0.4×0.7)=0.58`.

Normalización:

- `A = 30.85%`;
- `B = 31.91%`;
- `C = 37.23%`.

La prueba muestra además algo importante: un nodo upstream o de diseño **no tiene por qué obtener el mayor R*** por definición. El resultado depende de los pesos y de la estructura causal.

**Estado:** SUPERADA.

---

## 5. Prueba sintética D — nodo desconectado

Si un nodo `X` no tiene ningún camino hacia `D`, no pertenece a `A_D`.

Puede:

- excluirse del operador específico de `D`; o
- conservarse en una representación ampliada con `R*_X=0`.

No debe imponerse positividad a un nodo que no es ancestro causal del resultado.

Esto corrige la consecuencia histórica según la cual todo nodo de un grafo conectado tendría necesariamente `R*>0`, aun cuando no participe en el resultado específico.

**Estado:** SUPERADA.

---

## 6. Prueba sintética E — feedback atenuado

Grafo activo:

`A --0.5→ B`

`B --0.4→ A`

con:

`A --0.2→ D`

`B --0.3→ D`.

El radio espectral es:

`ρ(Q)=sqrt(0.5×0.4)≈0.4472<1`.

La serie converge y produce:

`r_A=0.4375`.

`r_B=0.4750`.

Normalización:

- `A = 47.95%`;
- `B = 52.05%`.

El operador inducido conserva eigenvalor dominante `1` y satisface `M_RR*=R*`.

**Estado:** SUPERADA.

---

## 7. Prueba sintética F — feedback fuera de dominio

Se construyó un feedback ramificado con:

`ρ(Q)≈1.1314>1`.

En ese caso la serie de rutas no converge.

CAND-RSTAR-001 **rechaza el cálculo** en lugar de introducir una amortiguación arbitraria.

La salida correcta es exigir una operación previa:

- despliegue temporal;
- descomposición de eventos;
- revisión de pesos;
- o un modelo específico de interacción/feedback.

**Estado:** SUPERADA COMO PRUEBA DE FRONTERA. El caso queda fuera del dominio del operador básico.

---

## 8. Regla `w/Σw` como caso límite

Si:

`Q_D=0`,

entonces:

`r_D=b_D`.

Y:

`R*=b_D/(1^T b_D)`.

Por tanto, la normalización simple `w/Σw` utilizada en el Apéndice C de Prometeo **sí es correcta en un caso estrella sin mediaciones entre nodos activos**.

No es incorrecta en sí misma; fue universalizada fuera de su dominio.

Esto permite conservarla en segunda edición como caso especial de CAND-RSTAR-001, no como algoritmo general.

---

## 9. Prometeo Caso 2 — coincidencia exacta con la suma de rutas

Caso de la profesionista falsa.

Pesos centrales:

- `V→P=0.905`;
- `H→V=0.290`;
- `R→P=0.150`.

No hay otras rutas activas relevantes.

La atribución por rutas da:

`r_V=0.905`.

`r_H=0.290×0.905=0.26245`.

`r_R=0.150`.

Suma:

`Z=1.31745`.

Normalización:

- `V=68.693%`;
- `H=19.921%`;
- `R=11.386%`.

Prometeo publica:

- `V=68.7%`;
- `H=19.9%`;
- `R=11.4%`.

La coincidencia es exacta salvo redondeo.

### Consecuencia

En este caso, la lógica operativa de Prometeo **ya es CAND-RSTAR-001**:

- producto de pesos a lo largo de la ruta;
- suma de las contribuciones;
- una sola normalización final.

No se necesita eigenvector de `W` ni renormalización intermedia.

---

## 10. Prometeo Caso 3 — la renormalización intermedia cambia el objeto

Caso del accidente laboral.

Pesos centrales:

- `E→O=0.70`;
- `E→S=0.725`;
- `S→O=0.635`;
- `E→L=0.635`;
- `O→L=0.535`.

Si `E→L` se trata como mecanismo directo independiente, CAND-RSTAR-001 obtiene:

`r_O=0.535`.

`r_S=0.635×0.535=0.339725`.

`r_E=0.635+(0.70×0.535)+(0.725×0.635×0.535)=1.2558` aproximadamente.

Normalización:

- `E=58.94%`;
- `S=15.95%`;
- `O=25.11%`.

Prometeo publica:

- `E=57.6%`;
- `S=10.9%`;
- `O=31.5%`.

### Fuente de la diferencia

Prometeo primero calcula y **normaliza** la distribución intermedia:

`S=35.2%`, `O=64.8%`.

Después utiliza esos porcentajes normalizados como si fueran pesos causales de la siguiente ronda.

Eso reemplaza las magnitudes de ruta originales por una distribución relativa local antes de que termine la reconstrucción hacia `L`.

La operación modifica necesariamente las proporciones finales.

### Diagnóstico

La diferencia no demuestra un problema de la composición de rutas. Demuestra que:

> **normalizar antes de terminar de reconstruir la cadena causal cambia el objeto medido.**

La normalización compatible con la genealogía debe ocurrir una sola vez, después de sumar las rutas relevantes respecto de `D`.

---

## 11. Relectura del caso del banco de Prometeo

El mismo diagnóstico explica el caso del banco agregado.

La Ronda 1 normaliza cuánto reciben `R`, `A` y `P` desde nodos upstream.

La Ronda 2 utiliza después esa distribución intermedia para asignar responsabilidad a `R`, `A` y `P`, mientras `B` recibe por separado una arista directa/acumulada.

Con ello, parte de la influencia que llegó desde `B` queda atribuida al intermediario en vez de retornar causalmente a `B`.

Esto entra en tensión con el Caso 2, donde la ruta:

`H→V→P`

sí se devuelve correctamente a `H` mediante el producto `0.290×0.905`.

CAND-RSTAR-001 normaliza ambos casos con una sola regla:

- cada nodo recibe la suma de todas las rutas que parten de él y terminan en `D`;
- la normalización ocurre al final.

---

## 12. Adjudicación de `review.prometeo.design_node_presumption`

El propio capítulo 4 de Prometeo presenta el Caso 2 como:

> «la contraprueba necesaria»

a la lectura de que el nodo de diseño siempre debe tener el mayor `R*`.

La obra afirma que ese patrón puede ser frecuente, pero **no es universal**.

Por tanto:

`review.prometeo.design_node_presumption`

queda respondida negativamente:

> **un nodo de diseño no debe dominar R* por definición y un resultado contrario no demuestra por sí mismo que el grafo esté mal construido.**

La segunda edición debe tratar la dominancia del diseño como patrón empírico/hipótesis dependiente del caso, no como condición de validez del cálculo.

---

## 13. Resultado de la batería

CAND-RSTAR-001 supera las siguientes propiedades:

1. mantiene participación upstream en DAG;
2. combina ruta directa y mediada;
3. suma rutas paralelas;
4. excluye nodos sin camino al resultado;
5. maneja feedback atenuado bajo `ρ(Q)<1`;
6. rechaza feedback divergente sin regularización ad hoc;
7. reduce `w/Σw` a un caso especial correcto;
8. reproduce exactamente Prometeo Caso 2;
9. explica la divergencia de Prometeo Caso 3 por renormalización intermedia;
10. conserva `R*` como eigenvector del operador inducido `M_R(D)`;
11. mantiene independencia respecto de `α`.

No apareció una falla estructural dentro del dominio declarado.

---

## 14. Límites que siguen impidiendo declarar validación general

La batería no demuestra:

- que los pesos `w` estén empíricamente calibrados;
- que toda relación causal pueda representarse mediante un escalar multiplicativo;
- que rutas superpuestas sean aditivas;
- que condiciones conjuntas puedan reducirse a aristas binarias;
- que los ciclos con `ρ(Q)≥1` tengan solución dentro del mismo operador;
- que la suma de rutas sustituya Shapley en causalidad acumulativa.

Estos son límites de dominio, no fallas detectadas de la construcción dentro de sus hipótesis.

---

## 15. Estado de revisiones tras VAL-RSTAR-001

### Respondidas negativamente

- `review.prometeo.rstar_algorithm_equivalence`;
- `review.prometeo.design_node_presumption`.

### Respondida en su parte de reproducibilidad

- `review.calc.published_vectors_reproduction`: el operador declarado no reproduce los vectores impresos; la procedencia histórica exacta sigue abierta.

### Aún abiertas

- `review.calc.rstar_equivalence`;
- calibración y semántica cuantitativa de `w`;
- interacción entre rutas;
- ciclos fuera de `ρ(Q)<1`;
- revisiones históricas de orientación/sumidero hasta que CAND-RSTAR-001 sea adjudicado como operador vigente.

---

## 16. Recomendación para RES-RSTAR-001

La evidencia disponible permite preparar una resolución con la siguiente jerarquía:

1. `W` conserva sólo determinaciones locales primitivas de `φ₁`.
2. `D` se separa como resultado, no actor.
3. la atribución total se reconstruye mediante:

   `r_D=(I−Q_D)^−1b_D`;

4. se normaliza una sola vez:

   `R*=r_D/(1^T r_D)`;

5. se induce:

   `M_R(D)=Q_D+η_D b_D1^T`;

   con:

   `η_D=[1^T(I−Q_D)^−1b_D]^−1`;

6. `R*` es el Perron-eigenvector normalizado de `M_R(D)`;
7. las formulaciones históricas de `eig(W)`, rondas y `w/Σw` se conservan como historia formal, pero no como algoritmos equivalentes.

La resolución deberá declarar expresamente el dominio `ρ(Q_D)<1` y dejar fuera de su pretensión los problemas de interacción no aditiva y calibración empírica.
