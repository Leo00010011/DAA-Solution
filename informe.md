# Problema 1 de DAA



## Tema: Procrastinación++



## Integrantes:
#### Roxana Peña Mendieta C412
#### Leonardo Ulloa Ferrer C412



### Enunciado:
Roxana y Leonardo no tienen ganas de estudiar, luego de mirar al techo unos 20 minutos deciden que es hora de seguir procrastinando y proceden a entretenerse con un juego. Leonardo le da a Roxana dos strings y . A partir de , Roxana comienza a formar un nuevo string con las siguientes operaciones (una a la vez): 
-   Elimina el primer caracter de y lo inserta al principio de .
-   Elimina el primer caracter de y lo inserta al final de .

EL objetivo del (divertidísimo) juego es encontrar la cantidad de cadenas posibles a armar, de manera que sea prefijo de . Tras 30 min de armar cadenas a lo loco, Roxana decide que es tiempo de crear un algoritmo que resuelva el juego por ella. Encuentre ese algoritmo.



### Primera solución no tan óptima:
Backtraking

```console
Aqui va el código slow_solver.py
```



#### Demostración Correctitud :
La función ''slow_solver'' resuelve el problema para encontrar la cantidad de formas de construir la cadena A con T como prefijo a partir de otra cadena S, donde en cada paso se puede agregar un carácter de S al principio o al final de la cadena actual A, usando backtrack.
Este fue implementado usando dos llamados recursivos, una para cada opción. Además, se lleva un array ''choices'' de las elecciones que se toman para debugguear.

El estado de cada llamado recursivo está constituido por ''current_sol'', que representa lo que ha ido construyendo hasta ese momento de A y un ''index'' que es el índice de S que toca decidir en ese estado E. La cantidad de soluciones en el estado E es igual a la cantidad de soluciones poniendo el caracter de S a la izquierda de A más la cantidad de soluciones poniendo el caracter de S a la derecha de A, es decir:

Sea F, la función definida como la cantidad de cadenas que se pueden formar partiendo de ''current_sol'' cuyo prefijo sea T y se contruya a partir de una posición ''index'' de S en adelante, se cumple que :

```console
F(current_sol, index) = alpha + F(current_sol + S[index], index+1) + F(S[index] + current_sol, index+1)
```
donde $\alpha$ es 1 si en ese estado encontró una solución válida y 0 en caso contrario. La existencia de $\alpha$ se debe a no es obligado formar la cadena A con todos los caracteres de S.

Demostración: Todas las soluciones se pueden agrupar en 3 conjuntos de soluciones: 
Caso 1: quedarme donde está
Caso 2: poner el caracter de S a la izquierda de A
Caso 3: poner el caracter de S a la derecha de A.

La cantidad de soluciones del caso 1 es igual a $\alpha$ ya que hay una solución válida si tengo el prefijo T($\alpha$ = 1) y no la hay ne caso contrario($\alpha$ = 0).

Los 3 conjuntos representan 3 particiones de A, ya que cada uno contiene una decisión distinta que se tomó.

El valor de retorno de la función ''slow_solver'' es el doble de la cantidad de soluciones encontradas por la función auxiliar ''slow_solver_aux'' porque se esta analizando cuando el primer caracter de S se pone a la derecha o a la izquieda. En cualquiera de los 2 casos, el primer movimiento es equivalente para ambas soluciones.

Por lo tanto, la correctitud del código se basa en la idea de que se consideran todas las posibles combinaciones de caracteres y se cuenta la cantidad de soluciones válidas.


#### Demostración Complejidad Temporal :

La complejidad temporal de la función ''is_arr_prefix'' es O(m), donde m = len(T), ya que se compara cada carácter de la cadena ''arr'' con la cadena T hasta que se encuentra un carácter diferente o se alcanza el final de T.

La complejidad temporal de la función ''slow_solver_aux'' es de O(2^n), donde n = len(S), ya que en cada llamada recursiva se realizan dos llamadas recursivas adicionales, lo que lleva a un árbol de recursión binario con una profundidad máxima n. Además, se realiza una llamada a ''is_arr_prefix'' en cada llamada recursiva, lo que contribuye a la complejidad total.

La complejidad temporal de la función slow_solver es O(2^n), ya que llama a ''slow_solver_aux'' y realiza algunas operaciones adicionales que no afectan significativamente la complejidad temporal total.

### Segunda solución ... esta si es óptima:

```console
Aqui va el código optimal_solver.py
```


#### Demostración Correctitud :



#### Demostración Complejidad Temporal :

Para demostrar la complejidad temporal del código, primero se debe analizar la complejidad temporal de ''left_sol''. La matriz de programación dinámica tiene O(nm) elementos, y se debe llenar cada uno de ellos. Por lo tanto, la complejidad temporal de ''left_sol'' es O(nm).

La complejidad temporal de ''right_sol'' es O(nm), ya que también se llena una matriz de programación dinámica con O(nm) elementos.

La complejidad temporal de ''optimal_solver'' es la combinación de los métodos ''left_sol'' y ''right_sol'', y ambos tienen una complejidad temporal de O(nm). Por tanto, por la regla de la suma la complejidad temporal de 
O(nm).


### Generador de cosos de prueba:

El método random_generator encargado de generar los parámetros de entrada S y T para probar el algoritmo.
Al crear S y T se realizó eliminando casos que no iban a tener solución. Ejemplo, los siguientes casos:
1- Cuando el len(T) > S.
2- Cuando en T existen caracteres que no están en S.
3- Cuando en T hay caracteres de S, pero estan repetidos en T más de las veces que están repetidos en S.
4- Cuando T está vacío
5- Cuando una cadena que es igual a S pero con los caracteres en un orden diferente. 

Esto no quiere decir que se eliminaron los casos donde no haya solución, existen ejemplos de ese estilo, sino que no tenia sentido poner este tipo de ejemplos.

La función "random.choices" de la biblioteca "random" devuelve una lista de caracteres aleatorios tomados del alfabeto en minúscula de la cadena "string.ascii_lowercase". Luego, con el random.choices se crea una cadena con estos caracteres de tamaño k, donde puede repetir elementos. 
La cadena T se genera eligiendo aleatoriamente una longitud entre 1 y len(S), y luego seleccionando caracteres aleatorios de la cadena S utilizando la función "random.sample"(no repite elementos). 

Se generan los siguientes casos:
```console
1- len(T) = len(S)
2- len(T) < len(S)
```


```console
Aqui va el código random_generator.py
```


#### Demostración: Genera todos los tipos de casos de prueba



### Tester:
    En el archivo .py hay 3 formas de analizar los resultados:

    1- gen_cases: Recibe la cantidad de casos a generar y los tamaños de las cadenas S y T. Si exite el archivotest.txt, entonces se toman los valores que contiene y se añaden los nuevos que se generaron con su
    valor real con el método de backtranking

    2- json_tester: Si el archivo file_path existe se toman los casos generados que contiene y se comparan conel resultado de optimal_solver.

    3- tester: Recibe un entero de la cantidad de casos a generar y el tamaño de S.  Crea los valores de S y T
    a traves del método random_generator compara los resultados de los métodos slow_solver y optimal_solver ylos guarda en .txt.


```console
Aqui va el código tester.py
```

