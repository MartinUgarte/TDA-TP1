# Teoría De Algortimos I

### Alumnos

- Martina Lozano: 106267
- Martin Ugarte: 107870

## Primera Parte: *K-merge*

**Aclaración**: Definimos $k$ como la cantidad de arreglos ordenados, y $h$ como la cantidad de elementos en cada arreglo. La cantidad de elementos total por lo tanto es $n = k * h$

> 1. Determinar, utilizando el Teorema Maestro, cuál sería la complejidad del algoritmo propuesto

La fórmula del Teorema Maestro está dada por

$$T(n)=A*T(n/B) + O(n^c)$$

Donde $A$ representa la cantidad de llamados recursivos, $B$ la proporción del tamaño original de la lista con el que llamamos recursivamente y $O(n^c)$ el costo de las operaciones que no son llamadas recursivas.

En este caso, tenemos dos llamadas recursivas, el arreglo es partido a la mitad por cada uno de estos llamados, y el costo de las demás operaciones es $O(n)$ ya que el costo de mergear dos arreglos es $O(n + m) = O(n)$ sabiendo que $n$ y $m$ son las longitudes de cada arreglo “parcial” donde $l$ es la mayor, con lo cual se puede despreciar m como una constante.

Por lo cual, $A = 2$, $B = 2$ y $C = 1$.

Luego, $logB(A) = log_2(2) = 1$

Según el Teorema Maestro, como $logB(A)=C=1$, entonces la complejidad del algoritmo propuesto es $O(n^c log n)=O(n logn)$, donde $n$ es la cantidad total de elementos, es decir, $k * h$.

> 2. Describir el algoritmo que utiliza heaps, y determinar su complejidad.

Se tiene el conjunto de arreglos, el heap y un arreglo vacío, en el heap se encolan los primeros datos de cada arreglo de la forma (dato, número_arreglo). Mientras que el heap no esté vacío, se desencola del heap y se agrega el valor en el arreglo. Posteriormente se guarda el siguiente elemento del arreglo al que pertenecía el dato guardado. Se continúa así hasta que no queda ningún dato en el heap. 
Por lo tanto, se puede deducir que la complejidad de este algoritmo es O(n log k)

> 3. Implementar ambos algoritmos, y hacer mediciones (y gráficos) que permitan entender si las complejidades obtenidas para cada uno se condicen con la realidad.

Las mediciones se encuentran en el archivo *graficos.py*

> 4. En caso que la complejidad obtenida en el punto 1 no se condiga con la realidad, indicar por qué (qué condición falla).

TODO

> 5. En dicho caso, se requiere llegar a la complejidad correcta (no solamente enunciarla, sino demostrar cuál es).

TODO

> 6. Indicar cualquier conclusión adicional que les parezca relevante en base a lo analizado.

TODO

## Segunda Parte: *Contrabando*

**Aclaración**: Decidimos modelar la **mercadería** como un diccionario, donde las claves corresponden a los tipos de producto y los valores a listas que representan los distintos paquetes de contrabando. Por otra parte, los **pedidos** del aduanero son también un diccionario pero los valores están dados simplemente por la cantidad pedida por cada producto. El resultado del problema tiene el mismo formato que la mercadería.

**Ejemplo**:

```py
mercaderia = {
    "cajas de cigarrillos": [3, 8, 2],
    "botellas de vodka": [7]
}

pedido = {
    "cajas de cigarrillos": 5
}

resultado = {
    "cajas de cigarrillos": [3, 2]
}
```

> 1. Describir e implementar un algoritmo greedy que, dado un input con los productos que se tienen, y lo pedido como soborno, nos permita salir airosos de la situación, con la mayor cantidad de productos posibles. Justificar por qué el algoritmo es, efectivamente, greedy. Considerar que siempre se nos pedirá una cantidad de productos en existencias (en nuestro ejemplo anterior, no nos habrían pedido que dejemos 7 botellas de vodka radioactivo, ni tampoco mandarinas del Sahara).

En primer lugar, para la solución Greedy nos aseguramos que los paquetes queden ordenados por cantidad de mayor a menor y también disponemos de un diccionario que informa la cantidad pedida como soborno para cada tipo de producto. Gracias a esto, podemos recorrer los paquetes de nuestra mercadería disponible, por cada tipo de producto pedido, y ser capaces de decidir si agregar ese paquete a nuestro conjunto de soluciones o no. Esta acción se realiza de forma instantánea (por eso es Greedy) viendo si la diferencia entre la cantidad total hasta ese momento para ese producto puntual y la cantidad que provee el paquete es mayor o igual a la cantidad solicitada. De serlo, entonces esa solución no nos sirve y reducimos el problema a encontrar la cantidad deseada menos el valor de ese paquete. De lo contrario, agregamos ese paquete al conjunto de soluciones.

>2. Con las mismas consideraciones que en el punto anterior, describir e implementar un algoritmo (que sea óptimo) que resuelva el problema utilizando programación dinámica.

TODO

> 3. Indicar y justificar la complejidad de ambos algoritmos propuestos. Indicar casos (características y ejemplos) de deficiencias en el algoritmo greedy propuesto, para los cuales este no obtenga una solución óptima.
 
TODO

> 4. Implementar un programa que utilice ambos algoritmos, realizar mediciones y presentar resultados comparativos de ambas soluciones, en lo que refiere a su optimalidad de la solución (no de su complejidad). Incluir en la entrega del tp los sets de datos utilizados para estas simulaciones (que deben estar explicados en el informe). Estos deben incluir al menos una prueba de volumen, indicando cómo es que fueron generadas.

TODO