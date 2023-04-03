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
La función ''is_arr_prefix'' comprueba si una cadena es prefijo de otra cadena. La función ''slow_solver'' resuelve el problema para encontrar la cantidad de formas de construir la cadena A a partir de otra cadena S, donde en cada llamado se puede agregar un carácter de S al principio o al final de la cadena actual A, donde al final se obtenga T como prefijo de A.

La función ''slow_solver_aux'' es una función auxiliar recursiva que implementa la idea anterior mediante el uso de backtracking. En cada llamada, se considera si se puede agregar un carácter al principio o al final de la cadena actual A, y se realizan dos llamadas recursivas, una para cada opción. Además, se lleva un array ''choices'' de las elecciones que se toman para formar la solución.

En cada llamada recursiva, se comprueba si la cadena actual A tiene como prefijo a la cadena T. Si es así, se cuenta como una solución válida y se devuelve el valor 1. En caso contrario, se continúa la búsqueda.

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

El método random_generator encargado de generar los parámetros de entrada S y T para probar el algoritmo. El método built-in string.ascii_lowercase devuelve una cadena del abecedario en minúscula. Luego, con el random.choices se crea random una cadena con estos caracteres de tamaño k, donde puede repetir elementos.
Para generar T se toma como máximo el tamaño de S y con random.sample crea otra con la misma frecuencia con la que aparecen los elementos de S. 

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

