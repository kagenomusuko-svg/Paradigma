# Parte I. Estructura causal y matriz de relaciones

## 1. Objeto de esta parte

La estructura causal registra qué nodos intervienen en un resultado y cómo se transmite entre ellos la influencia representada. Su forma de cálculo es un grafo dirigido ponderado:

\[
G=(N,A,W)
\]

Aquí \(N\) es el conjunto ordenado de nodos, \(A\) el conjunto de relaciones dirigidas y \(W=[w_{ij}]\) la matriz que asigna un peso a cada relación. El orden de \(N\) se conserva en todas las matrices y vectores posteriores.

Esta parte establece cómo construir y revisar la entrada estructural. El vector de responsabilidad se define sobre esta entrada en la Parte II.

## 2. Nodos y aristas

Un nodo representa una unidad distinguible para el problema: una persona, una decisión, una institución, una regla o un proceso técnico. Se separan dos funciones cuando el análisis debe atribuirles contribuciones diferentes.

Una arista \(N_i\to N_j\) indica que la actividad o condición representada por \(N_i\) influye en \(N_j\) dentro del modelo. La arista es dirigida. La precedencia temporal puede apoyar la identificación de una relación, pero no la sustituye: la relación debe especificarse en la representación causal.

El nodo terminal \(Y\) representa el resultado analizado. En un cálculo dado se fija el resultado antes de asignar pesos. Si se estudian dos resultados distintos, se construyen dos representaciones o se declara cómo se distinguen sus nodos terminales.

## 3. Matriz de pesos

Con nodos \(N_1,\ldots,N_m\), la matriz \(W\) tiene dimensión \(m\times m\). Su entrada \(w_{ij}\) corresponde a la arista \(N_i\to N_j\):

\[
w_{ij}\geq 0,\qquad
w_{ij}=0\;\text{si no se representa la arista }N_i\to N_j.
\]

En la representación normalizada, las salidas de cada nodo no terminal suman uno:

\[
\sum_{j=1}^{m}w_{ij}=1
\quad\text{para cada nodo no terminal }N_i.
\]

La fila del nodo terminal es cero:

\[
w_{Yj}=0\quad\text{para todo }j.
\]

Los pesos describen la distribución de influencia saliente que adopta el modelo. La suma unitaria permite aplicar las operaciones definidas sobre esta representación; por sí sola no convierte cada peso en una frecuencia observada ni en la probabilidad empírica de un acontecimiento.

## 4. Ejemplo: dos rutas hacia un resultado

Considérese la siguiente estructura:

- \(D\): diseño de una regla;
- \(E\): ejecución bajo esa regla;
- \(Y\): resultado.

El diseño transmite peso \(0.6\) a la ejecución y \(0.4\) directamente al resultado. La ejecución transmite todo su peso al resultado. En el orden \((D,E,Y)\):

\[
W=
\begin{pmatrix}
0 & 0.6 & 0.4\\
0 & 0 & 1\\
0 & 0 & 0
\end{pmatrix}.
\]

La verificación se hace por filas:

\[
0+0.6+0.4=1,\qquad 0+0+1=1,\qquad 0+0+0=0.
\]

Las dos primeras filas corresponden a nodos no terminales y suman uno. La fila de \(Y\) suma cero porque \(Y\) es terminal.

La matriz conserva dos rutas desde \(D\) hasta \(Y\): la ruta directa, de peso \(0.4\), y la ruta \(D\to E\to Y\), cuyo producto de pesos es \(0.6\cdot1=0.6\). La suma de ambas rutas es uno. Este cálculo de rutas comprueba la estructura del ejemplo; no debe confundirse con la definición completa de \(R^*\), que incorpora las reglas de distribución de responsabilidad de la Parte II.

## 5. Submatrices y notación de cálculo

Al separar los nodos no terminales del resultado, se puede escribir la matriz por bloques:

\[
W=
\begin{pmatrix}
Q & b\\
0 & 0
\end{pmatrix}.
\]

\(Q\) reúne las relaciones entre nodos no terminales; \(b\) reúne las relaciones directas de esos nodos con el resultado. En el ejemplo:

\[
Q=
\begin{pmatrix}
0&0.6\\
0&0
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
0.4\\
1
\end{pmatrix}.
\]

Esta separación es útil para escribir cálculos matriciales y verificar dimensiones. Con \(n\) nodos no terminales, \(Q\) tiene dimensión \(n\times n\) y \(b\) dimensión \(n\times1\).

## 6. Procedimiento de construcción

Para preparar una matriz:

1. Define el resultado que se analizará y asigna su nodo terminal.
2. Enumera los nodos y fija un orden.
3. Registra cada relación dirigida y su sentido.
4. Asigna un peso a cada salida representada.
5. Coloca los pesos en la fila del nodo de origen y en la columna del nodo de destino.
6. Asigna cero a las relaciones no representadas.
7. Comprueba que cada fila no terminal suma uno y que la fila terminal suma cero.
8. Comprueba que las dimensiones de la matriz coinciden con el número y orden de nodos.

Una fila no terminal cuya suma sea distinta de uno requiere revisar la asignación o normalizar los pesos conforme al procedimiento establecido para el caso. La normalización no debe ocultar una salida omitida ni una relación duplicada.

## 7. Criterios de consistencia

Una matriz está lista para las operaciones siguientes cuando:

- todas sus entradas son números definidos y no negativos;
- cada entrada está asociada a un par ordenado de nodos;
- el orden de filas y columnas está declarado;
- la fila de cada nodo no terminal satisface la condición de suma;
- el nodo terminal está identificado y su fila es cero;
- las dimensiones requeridas por las operaciones posteriores son compatibles.

Si la representación contiene ciclos, estos se declaran y se tratan con la operación que admita ciclos. No se reemplaza un ciclo por una cadena ficticia. La existencia y unicidad de soluciones para una operación matricial se establecen con las condiciones propias de esa operación.

## 8. Ejercicio de comprobación

Sea \(W\) una matriz en el orden \((A,B,C,Y)\), donde \(Y\) es el resultado. Antes de calcular cualquier vector:

1. identifica qué entradas codifican la relación \(A\to B\);
2. suma la fila de \(A\);
3. verifica que la fila de \(Y\) sea cero;
4. enumera las rutas dirigidas de \(A\) a \(Y\);
5. calcula el producto de pesos de cada ruta.

La respuesta permite comprobar la representación y detectar errores de orientación antes de aplicar el operador de responsabilidad.
