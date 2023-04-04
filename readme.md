Problema 1 de DAA

## Tema: Procrastinación++

## Integrantes:

#### Roxana Peña Mendieta C412

#### Leonardo Ulloa Ferrer C412

### Enunciado:

Roxana y Leonardo no tienen ganas de estudiar, luego de mirar al techo unos 20 minutos deciden que es hora de seguir procrastinando y proceden a entretenerse con un juego. Leonardo le da a Roxana dos strings y . A partir de , Roxana comienza a formar un nuevo string con las siguientes operaciones (una a la vez):

- Elimina el primer caracter de y lo inserta al principio de .

- Elimina el primer caracter de y lo inserta al final de .

EL objetivo del (divertidísimo) juego es encontrar la cantidad de cadenas posibles a armar, de manera que sea prefijo de . Tras 30 min de armar cadenas a lo loco, Roxana decide que es tiempo de crear un algoritmo que resuelva el juego por ella. Encuentre ese algoritmo.

### Primera solución ... no tan óptima:

Backtraking

```console
Aqui va el código slow_solver.py
```

#### Demostración Correctitud :

La función ''slow_solver'' resuelve el problema para encontrar la cantidad de formas de construir la cadena A con T como prefijo a partir de otra cadena S, donde en cada paso se puede agregar un carácter de S al principio o al final de la cadena actual A, apoyándose en el método auxiliar ''slow_solver_aux''.

La función "slow_solver_aux" es una función recursiva que utiliza la técnica de backtracking para encontrar todas las soluciones posibles. La función mantiene una solución parcial "current_sol" que representa lo que ha ido construyendo paso a paso hasta ese momento de A, una lista de opciones "choices" que indica las decisiones tomadas en cada paso(para debugguear), y un índice "index" indica el caracter donde toca decidir.

Este fue implementado usando dos llamados recursivos, una para cada opción: poner el caracter $S$[index] a la derecha o a la izquierda de 'current_sol' y comprobandese si con lo que se tiene construido hasta ese instante ya es solución pues siempre se puede decidir parar de poner letras

Sea F, la función definida como la cantidad de cadenas con prefijo T  se pueden formar partiendo de ''current_sol'' y decidiendo a partir de una posición ''index''  en adelante, se cumple que :

```console
F(current_sol, index) = alpha + F(current_sol + S[index], index+1) + F(S[index] + current_sol, index+1)
```

donde $\alpha$ es 1 si en ese estado encontró una solución válida y 0 en caso contrario. La existencia de $\alpha$ se debe a no es obligado formar la cadena A con todos los caracteres de S.

**Demostración**: Todas las soluciones que se cuentan en F[current_sol,index] se pueden agrupar en 3 conjuntos de soluciones:

Caso 1: quedarme donde está

Caso 2: poner el caracter de S a la izquierda de A

Caso 3: poner el caracter de S a la derecha de A.

Los 3 conjuntos representan 3 particiones de A, ya que cada uno contiene una decisión distinta que se tomó con S[index].  Si se toma la primera decisión entonces hay $\alpha$ soluciones pues en caso de que ya esté constituido el prefijo esta partición tiene una solución válida y en caso contrario no tiene ninguna. Si se decide poner S[index] a la izquierda entonces hay F[S[index]  + current_sol,index + 1] soluciones por definición de F y lo mismo para el término restante y si se decide derecha

El valor de retorno de la función ''slow_solver'' es el doble de la cantidad de soluciones encontradas por la función auxiliar ''slow_solver_aux'' cuando se llama con current_sol igual al primer caracter de 'S' pues esa decisión puede ser tanto izquierda como derecha que el efecto va a ser el mismo. 

El algoritmo pues la terminación de ese llamado depende de la terminación de dos llamados recursivos que se hacen con un índice mayor por lo que eventualmente van a llegar al caso base que es con index = |S|. Además, encuentra todas las posibles soluciones y las retorna ya que evalúa todas las posibles decisiónes de para caracteres de S.

Por lo tanto, la correctitud del código se basa en la idea de que se consideran todas las posibles combinaciones de caracteres y se cuenta la cantidad de soluciones válidas.

#### Demostración Complejidad Temporal :

La complejidad temporal de la función ''is_arr_prefix'' es O(m), donde m = len(T), ya que se compara cada carácter de la cadena ''arr'' con la cadena T hasta que se encuentra un carácter diferente o se alcanza el final de T.

La complejidad temporal de la función ''slow_solver_aux'' es de O($m2^n$), donde n = len(S), ya que en cada llamada recursiva se realizan dos llamadas recursivas adicionales, lo que lleva a un árbol de recursión binario con una profundidad máxima n y en cada llamado recursivo se llama is_arr_prefix. Además, se realiza una llamada a ''is_arr_prefix'' en cada llamada recursiva, lo que contribuye a la complejidad total.

### SegunDAA solución ... esta si es óptima:

```console
Aqui va el código optimal_solver.py
```

#### Demostración Correctitud :

Decimos que una solución del juego es  una secuencia de decisiones de izquierda o derecha en las que  la palabra $A$ consrtuida tiene como prefijo la palabra $T$

El conjunto de todas las soluciones de un problema se puede particionar en dos conjutos:

1. Soluciones en las que todas las letras que conforman el prefijo $T$ de $A$ fueron puestas con decisiones de Izquierdas

2. Soluciones en las que al menos una de las letras que conforman el prefijo $T$ de $A$ fue puesta con una decision de derecha

### Calculando la cantidad de soluciones de la particion 1:

Para resolver este problema vamos a seguir las siguientes ideas:

* Las últimas $|T|$ letras con las que se tomó la decisión de ponerlas a la izquierda van a conformar el prefijo de tamaño $|T|$ en $A$ en orden contrario al que estaban dispuestas en $S$

* La cantidad de soluciones  con $n$ izquierdas depende solo de la cantidad de soluciones con $n$ decisiones izquierdas en $S$[1:] y la cantidad de soluciones con $n - 1$  izquierdas  en $S$[1:]

Para la solución de este problema vamos a utilizar la siguiente definición:

* left_dp[$s$,$p$]: cantidad de formas de decidir en $S$[s:] de forma tal que solo hayan $p + 1$ decisiones izquierdas y el reverso de la concatenación de las letras que fueron izquierda sean el prefijo de $T$ desde $0$ hasta $p$

Esta cantidad cumple las siguintes propiedades

* $S$[$s$] $\neq$ $T$[$p$] $\Rightarrow$ left_dp[$s$,$p$] $=$ left_dp[$s + 1$, $p$]
  
  - **Demostración**: La decision tomada en $s$ tiene que ser derecha, porque en caso contrario para que el inverso de su concatenación con los $p$ restantes sea igual al prefijo de 0 a $p$ de $T$ se debería cumplir que $T$[$p$] $=$ $S$[$s$]

* $S$[$s$] $=$ $T$[$p$] $\Rightarrow$ left_dp[$s$,$p$] $=$ left_dp[$s + 1$, $p$] + $\alpha$
  
  - **Demostración**: Si se decide derecha con $S$[$s$] se puede y se tiene que poner en el resto cualquiera de las soluciones de $S$[$s + 1$:] con $p + 1$ decisiones izquierdas
  
  - $p = 0 \Rightarrow \alpha =$ $|S| - s$
    
    - **Demostración**: Si se decide izquierda con $S$[$s$], ya se consumió las izquierdas que se pueden poner en las formas de decidir que se están contando con left_dp[$s$,$0$] por lo que el resto solo puede ser uno y las últimas decisiones se puede decidir ponerlas o no
  
  - $e.o.c \Rightarrow $ $\alpha = $ left_dp[$s + 1$,$p -1$]
    
    - **Demostración**: Si se decide izquierda con $S$[$s$], faltan por consumir $p$ decisiones izquierdas con $S$[$s + 1$:] y esta es exactamente la cantidad que se calcula con left_dp[$s + 1$,$p - 1$]

Luego si $S[s] = T[|T| - 1]$ la cantidad de soluciones de esta partición que tienen a $S[s]$ en la posición $|T| - 1$ de $A$ es igual a $2^s$left_dp[$s + 1$,$p - 1$],pues, al escoger a $S[s]$ como primera de los $|T|$ últimas decisiones izquierdas, las $s$ primeras decisiones no afectan el prefijo por lo que pueden ser cualquiera de las $2^s$ posibles formas y las decisiones desde $s + 1$ en adelante tienen que formar el prefijo de $0$ a $p -1$ las cuales son left_dp[$s + 1$,$p - 1$]. Luego la cantidad de soluciones de esta partición se puede calcular acumulando este valor para toda  $s$ que cumpla $S[s] = T[|T| - 1]$, y esta se puede calcular usando un enfoque de programación dinámica recorriendo $S$ de atrás para alante y actualizando los valores de left_dp[$s$,$p$] para todo $p$ de $0$ a $|T|$ y acumulando en la posición left_dp[$s$,$|T| - 1$] las soluciónes tal que $s$ sea la primera de las $|T|$ últimas izquierdas

### Calculando la cantidad de soluciones de la partición 2:

Sea una solución en la que al menos una de las primeras $|T|$ letras de $A$ fue puesta con una decisión de derecha, esta solución cumple las siguientes propiedades:

- Sea $S$[$q$] la última letra de $S$ con la que se tomó la decisión derecha y cayó dentro de las primeras $|T|$ letras de $A$.
  
  - $S$[$q$] ocupa la posición $|T| - 1$ en $A$
    
    - **Demostración**: Todas las letras tomadas con decisiónes derechas van después de las que fueron tomadas con decisiónes izquierdas, y las letras tomadas con decisiones derechas ocurren en $A$ con el mismo orden que ocurren en $S$; luego como esta es la última letra tomada con decisiones derechas de las que caen en las primeras $|T|$ letras de $A$ ,$S$[$q$] tiene que ocupar la posición $|T| - 1$
  
  - Con el prefijo hasta el índice $q$ de $S$ se decide el sufijo de tamaño $q + 1$ del prefijo de tamaño $|T|$ en $A$
    
    - **Demostración**: Al poner una letra con una decisión derecha todo lo que fue decidido en las letras anteriores a ella van a estar contiguos a ella y antes de ella. Como $S$[$q$] ocupa la posición $|T| - 1$ de $A$ antonces las $q$ letras anteriores tienen que ocupar las $q$ posiciones anteriores del prefijo
  
  - El prefijo en $A$ hasta el índice $|T| - q - 2$ es calculado solo con izquierdas con $S$[$q + 1$:]
    
    - **Demostración**: $S$[$q$] fué la última letra con la que se tomó decisión derecha que ocupa una posición en el prefijo de tamaño $|T|$ en $A$ por lo que todas derechas seleccionadas en los índices de mayores que $q$, no caen en el prefijo de tamaño $|T|$. Con lo que está antes de $q$ en $S$ solo se construye el sufijo de tamaño $q + 1$ del prefijo $|T|$. Por lo que necesariamente  ese prefijo de $A$ se tiene que calcular con decisiones izquierdas en las posiciones mayores o iguales a $q + 1$

- Vamos a definir a right_dp[pos,len] como cantidad de formas de decidir para construir el substring(pos,len) de $T$ con el prefijo de tamaño 'len' de $S$
  
  - La cantidad de soluciones con $S$[$q$] como última letra con la que se tomó desición derecha que cae entre las primeras $|T|$ letras de $A$ son iguales a:
    
    - left_dp[$q + 1$,$|T| - q - 2$ ] * right_dp[$|T| - q - 1$,$q$]
    
    - **Demostración**: Como ya se dijo anteriormente si se escogió a $S$[$q$] como última letra con la que se tomó desición derecha que cae entre las primeras |T| letras de A entonces el sufijo de tamaño $q + 1$ se resuelve con el prefijo de tamaño $q + 1$ de $S$ pero ya se sabe que $S$[$q$] tomó derecha por lo que queda por decidir solo el prefijo de tamaño $q$ para resolver el substring de tamaño $q$ desde la posición $|T| - q - 1$ de $A$, la cantidad de formas de hacer esto es right_dp[$|T| - q - 1$,$q$] por definición. Luego como ya se dijo anteriormente el prefijo hasta la posición $|T| - q - 2$ de $A$ se calcula solo con izquierdas de $S$[$q + 1$:] por lo que las decisiones pueden y deben ser las que cumplen la condición para contar en left_dp[$q + 1$,|$T| - q - 2$ ]. Luego todas las soluciónes que queremos contar tiene unos primeros $|T| - q - 1$ que pueden ser cualquiera de los contados en left_dp[$q + 1$,$|T| - q - 2$] y el  resto del prefijo $T$ que puede ser cualquiera de los right_dp[$|T| - q - 1$,$q$] por lo que por principio de multiplicación la cantidad es igual a la formula planteada
  
  - right_dp[pos,len] = right_dp[pos, len - 1] + right_dp[pos + 1, len - 1]
    
    - **Demostración**: Supongamos que se tiene que construir con el prefijo de tamaño 'len' de $S$ el substring(pos,len) de $T$, si analizan las decisiones de atrás para alante y se toma una decisión derecha con la última letra esta va a caer en la última posición del substring a construir (todas las derechas van después que las izquierdas y mantienen el orden donde se ponen) por lo que quedaría por decidir el substring(pos,len - 1) de $A$ con el prefijo del tamaño len - 1 de $S$  lo cual tiene right_dp[pos, len - 1] formas de hacerse por definición, con la misma lógica se puede llegar a que si se toma la decisión izquierda con la última letra se tienen right_dp[pos + 1, len - 1]

Los valores de right_dp se pueden ir resolviendo calculando los casos para len = 1 e ir creciendo hasta len igual $|T|$ pues todos los casos, excepto el de len = 1 que es 2 si $S$[len] $=$ $T$[pos] y $0$ en otro caso, dependen del casos con su len - 1

#### Demostración Complejidad Temporal :

La complejidad de esta solución es igual a la suma de la complejidad de left_sol y right_sol. Sea n igual a |S| y m igual |T|

El método left_sol consiste en dos casos

- si el prefijo es 1 donde se realiza un for de 0 hasta S por lo que la complejidad es O(n)

- en el otro caso se realiza un doble for, donde uno realiza n iteraciones y el otro realiza m iteraciones por lo que la complejidad temporal es O(mn)

Luego como la complejidad de un método cuando se tienen varios casos es igual al máximo de las complejidades de cada uno de los casos, la complejidad de left_sol es O(mn)

El método right_sol consiste en dos casos:

- uno cuando |T| = 1 el cual se resuelve en O(1)

- en los otros casos se tienen cuatro ciclos, 3 de ellos con m iteraciones en el peor caso y el otro con un doble for ambos con m casos en el peor caso. Como la complejidad de la suma es la complejidad del máximo la complejidad de este caso es O(m$^2$)

Como la complejidad cuando se tienen varios casos es el máximo de las complejidades el método right_sol tiene complejidad O(m$^2$)

Como el método óptimal solver consiste en llamar right_sol y left_sol y la complejidad de la suma es igual al maximo de las complejidades de sus términos entonces tiene complejidad O(mn)

### Generador de cosos de prueba:

El método random_generator encargado de generar los parámetros de entrada S y T para probar el algoritmo.

Al crear S y T se realizó eliminando casos que no iban a tener solución. Ejemplo, los siguientes casos:

1- Cuando el len(T) > S.

2- Cuando en T existen caracteres que no están en S.

3- Cuando en T hay caracteres de S, pero estan repetidos en T más de las veces que están repetidos en S.

4- Cuando T está vacío

5- Cuando una cadena que es igual a S pero con los caracteres en un orden diferente.

Esto no quiere decir que se eliminaron los casos donde no haya solución, existen ejemplos de ese estilo, sino que no tenia sentido poner este tipo de ejemplos.

Con la función "random.choices" de la biblioteca "random" obtenemos una lista de caracteres aleatorios tomados del alfabeto en minúscula de la cadena "string.ascii_lowercase". 

La cadena T se genera eligiendo aleatoriamente una longitud entre 1 y len(S), y luego seleccionando caracteres aleatorios de la cadena S utilizando la función "random.sample"(no repite elementos).

Se generan los siguientes casos:

```console
1- len(T) = len(S)

2- len(T) < len(S)
```

```console
Aqui va el código random_generator.py
```

Como se puede ver de las siguientes estadísticas generadas de las soluciones con los casos de prueba obtenidos con este generador se tiene que 

```console
SUMARY:
wrong cases:
cant_cases: 2982
cant_wrong: 0
cant_dcha: 441
cant_wrong_dcha: 0
cant_wrong_izda: 0
accuracy: 1.0
dcha_rat: 0.14788732394366197
izda_rat: 0.24916163648558015
only_dcha_rat: 0.028504359490274984
only_izda_rat: 0.12977867203219315
izda_and_dcha_rat: 0.11938296445338699
zero_rat: 0.7223340040241448
dcha_accuracy: 1.0
```

Se puede notar que la probabilidad de que algun caso tenga soluciones contadas por el método right_sol es de un 14 porciento por lo que aún generando 3000 casos solo se están probando 441. Por lo que nos propusimos implemantar un generador de casos también aleatorio para aumentar esta probabilidad. Para esto nos intentamos forzar que se cumpla una condición necesaria para que exista alguna solución de las que cuenta right_sol que es que exista algún carater del prefijo de tamaño |T| de S igual T[|T| - 1] y que todo lo que está detras sea una permutación del sufijo de misma longitud en |T|

```console
SUMARY:
wrong cases:
cant_cases: 961
cant_wrong: 0
cant_dcha: 284
cant_wrong_dcha: 0
cant_wrong_izda: 0
accuracy: 1.0
dcha_rat: 0.29552549427679503
izda_rat: 0.04890738813735692
only_dcha_rat: 0.24661810613943808
only_izda_rat: 0.0
izda_and_dcha_rat: 0.04890738813735692
zero_rat: 0.704474505723205
dcha_accuracy: 1.0
```

Como se puede notar de esta forma se duplica la probabilidad de que ocurran estos casos

### Tester:

En el archivo .py hay 3 formas de analizar los resultados: 

1. gen_cases: Recibe la cantidad de casos a generar y los tamaños de las cadenas S y T. Si exite el archivotest.txt, entonces se toman los valores que contiene y se añaden los nuevos que se generaron con su valor real con el método de backtranking

2. json_tester: Si el archivo file_path existe se toman los casos generados que contiene y se comparan con el resultado de optimal_solver.

3. tester: Recibe un entero de la cantidad de casos a generar y el tamaño de S.  Crea los valores de S y T a traves del método random_generator compara los resultados de los métodos slow_solver y optimal_solver y los guarda en .txt.

```console
Aqui va el código tester.py
```
