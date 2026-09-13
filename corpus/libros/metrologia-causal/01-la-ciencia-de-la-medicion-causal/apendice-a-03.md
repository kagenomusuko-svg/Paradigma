APÉNDICES · Demostraciones formales de propiedades

### Apéndice A·3

### Propiedades de monotonía de R* ante

### modificaciones del grafo

Cómo cambia R* cuando se modifica la estructura del grafo

causal

### I.  Monotonía ante el aumento de peso de una arista

Sea W la matriz de pesos del grafo y v* = R* su eigenvector principal normalizado con eigenvalor ρ*. Supongamos que se aumenta el peso de la arista (j → i): W' = W + ε E_{ij}, donde E_{ij} es la matriz con 1 en la posición (i, j) y 0 en las demás, y ε > 0. Sea v*' = R*' el eigenvector principal de W'.

Proposición de monotonía: si se aumenta el peso de la arista j → i (la influencia de j sobre i aumenta), entonces R*'_i ≥ R*_i. Es decir, el nodo que recibe más influencia no pierde centralidad causal.

La demostración procede por el principio de perturbación espectral de primer orden. El cambio en el eigenvector v* ante la perturbación W' = W + εE_{ij} satisface, al primer orden en ε: Metrología Causal

∂v*_k / ∂w_ij = [u*_i · v*_j / (u*ᵀ v*)] · δ_{ki} − v*_k ·

[u*_i · v*_j / (u*ᵀ v*)]

donde u* es el eigenvector izquierdo principal de W (el vector tal que u*ᵀW = ρ*u*ᵀ) y δ_{ki} es la delta de Kronecker. Evaluando en k = i: ∂v*_i / ∂w_ij = [u*_i · v*_j / (u*ᵀ v*)] · (1 − v*_i). Dado que u*_i > 0, v*_j > 0, u*ᵀv* > 0 y v*_i < 1 (el vector está normalizado con suma 1 y tiene más de un componente positivo), se tiene ∂v*_i / ∂w_ij > 0. El aumento de w_ij aumenta R*_i.

### II.  Monotonía ante la adición de un nodo

Cuando se añade un nodo nuevo al grafo — un nodo que no estaba en N y que tiene aristas hacia nodos existentes — la distribución de R* sobre los nodos originales cambia. La dirección del cambio depende de la posición del nuevo nodo en el grafo.

Proposición: si se añade el nodo n+1 con aristas n+1 → i para algunos i ∈ N (aristas salientes del nuevo nodo hacia nodos existentes), entonces R*_i aumenta para los nodos i que reciben aristas del nuevo nodo, y puede disminuir para los nodos que no reciben aristas del nuevo nodo directamente.

La intuición: el nuevo nodo propaga influencia hacia los nodos existentes a los que conecta. Esos nodos reciben influencia adicional, lo que aumenta su centralidad en el eigenvector. Los nodos sin conexión directa desde el nuevo nodo solo reciben influencia indirecta (a través de los caminos que pasan por los nodos conectados al nuevo nodo), y su R* puede disminuir porque ahora compiten con el nuevo nodo en la distribución normalizada.

Metrología Causal

Consecuencia para el análisis de frontera: cuando el Error Tipo III (exclusión de nodos) está presente, añadir el nodo excluido (el nodo de diseño no incluido en el grafo) siempre aumenta el R* de los nodos que el nodo de diseño influye directamente. Dado que el nodo de diseño influye directamente sobre los ejecutores, y dado que los ejecutores reciben aristas del nodo de diseño, añadir el nodo de diseño aumenta el R* de los ejecutores relativamente al R* del nuevo nodo de diseño — pero en términos absolutos, el nodo de diseño puede tener R* mayor que cualquiera de ellos por la propiedad de multiplicidad de caminos.

### III.  Monotonía ante la eliminación de un nodo

La eliminación de un nodo del grafo — la reducción de N a N' = N \ {k} — produce el subgrafo inducido W' obtenido eliminando la fila y columna k de W. El eigenvector principal de W' es R*' sobre los nodos N'.

Proposición: si se elimina el nodo k, el ranking relativo de los nodos restantes puede cambiar de manera no monótona en general. Sin embargo, se cumple la siguiente propiedad de la estructura del ranking: si el nodo k era el de mayor R* en el grafo original (el nodo de diseño con Declaración A), entonces su eliminación produce una distribución R*' donde el nodo que tenía el segundo mayor R* en el grafo original no necesariamente tiene el mayor R*' en el grafo reducido. La redistribución depende de cuáles nodos eran más dependientes del nodo eliminado.

Consecuencia para la impugnación adversarial: la contraparte que argumenta «si se excluye a FRO del análisis, ECP es el responsable principal» está haciendo un argumento correcto en su lógica, pero incorrecto en su premisa. La exclusión de FRO produciría un grafo diferente donde ECP podría ser el

Metrología Causal

de mayor R*'. Pero FRO no puede excluirse porque es condición necesaria del daño. El argumento es equivalente a «si no incluyéramos al diseñador del sistema que hizo posible el fraude, el ejecutor sería el más responsable» — que es exactamente la paradoja de la visibilidad en su versión argumentativa.

Metrología Causal

