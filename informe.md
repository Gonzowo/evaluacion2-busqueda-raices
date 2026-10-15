# Informe evaluación 2: La raiz que se esconde

## Introduccion

En este trabajo se implementa y compara seis métodos numéricos para aproximar raíces de funciones. 

Se considera 1 ejemplo de cada una de las siguientes: polinómicas simples, polinómicas dobles, logarítmicas, exponenciales, trigonométricas y  mixtas.
Los metodos a comparar son los siguientes: bisección, falsa posición, punto fijo, secante, newton-raphson, newton-raphson mejorado.

La comparación realizada registra el número de iteraciones requerido por cada método bajo los mismos parámetros de tolerancia y límite de iteraciones.

## Funciones utilizadas

| Categoría | Función | Intervalo o valores iniciales | Raíz de referencia |
|---|---|---|---:|
| Polinómica | $x^3-x-2$ | $[1,2]$; $x_0=1$, $x_1=2$ | 1.5213797068045676 |
| Polinómica con raíz doble | $(x-2)^2$ | $x_0=1.2$, $x_1=2.5$ | 2 |
| Logarítmica | $\ln(x)+x-4$ | $[2,3]$; $x_0=2$, $x_1=3$ | 2.9262710624435009 |
| Exponencial | $e^{-x}-x$ | $[0,1]$; $x_0=0$, $x_1=1$ | 0.5671432904097839 |
| Trigonométrica | $\cos(x)-x$ | $[0,1]$; $x_0=0$, $x_1=1$ | 0.7390851332151607 |
| Mixta | $\sqrt{x}-\cos(x)$ | $[0.1,1]$; $x_0=0.1$, $x_1=1$ | 0.6417143708728827 |

Para la función polinómica con raíz doble, el intervalo se deja sin definir porque la función toca el eje en x=2 sin cambiar de signo, el resto de las cinco funciones con raíz simple tienen intervalo porque sus extremos se eligieron para que la función cambie de signo (teorema de Bolzano).


## Resultados de convergencia

La tabla resume las iteraciones registradas por los métodos. Todos alcanzaron el criterio de parada antes del máximo de iteraciones.

| Función | Bisección | Falsa posición | Punto fijo | Secante | Newton-Raphson | Newton mejorado |
|---|---:|---:|---:|---:|---:|---:|
| Polinómica | 20 | 12 | 8 | 6 | 5 | 5 |
| Polinómica con raíz doble | No aplica | No aplica | 10 | 15 | 10 | 1 |
| Logarítmica | 19 | 4 | 14 | 3 | 3 | 3 |
| Exponencial | 20 | 7 | 25 | 4 | 3 | 3 |
| Trigonométrica | 20 | 5 | 34 | 4 | 4 | 4 |
| Mixta | 20 | 4 | 15 | 3 | 3 | 3 |

"Datos obtenidos de resumen_convergencia.csv, luego de ejecutar evaluacion.py con la tolerancia, el máximo de iteraciones y los datos iniciales. Las curvas de error por iteración guardadas en `src/assets/` complementan esta tabla".

## 6. Preguntas de convergencia
# 6.1 ¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?
En la funcion polinómica simple, fue Newton-Raphson y Newton-Raphson mejorado.
En la funcion polinómica doble, fue solamente Newton-Raphson mejorado.
En la funcion logarítmica, fue el metodo de la Secante, Newton-Raphson y Newton-Raphson mejorado.
En la funcion exponencial, fue Newton-Raphson y Newton-Raphson mejorado.
En la funcion trigonométrica, fue el metodo de la Secante, Newton-Raphson y Newton-Raphson mejorado. 
En la funcion mixta, fue el metodo de la Secante, Newton-Raphson y Newton-Raphson mejorado.

La justificación de que en la mayoria de funciones haya sido el metodo Newton-Raphson y su variante mejorada los metodos mas rapidos es porque su convergencia es cuadrática (excepto en la raíz doble), mientras que la convergencia del resto de metodos es lineal o menores.

# 6.2 ¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración? (Se analiza el grafico de convergencia_mixta.png error aproximado vs iteración)
El metodo de la bisección tiene una convergencia lineal, en el grafico se ve que tiene una curva irregular, esto se justifica porque el punto medio puede caer más cerca o lejos de la raiz anterior, por eso sube y baja de forma impredecible (su tendencia sigue siendo una recta con pendiente log(1/2) = -0.30 aprox).
El metodo del punto fijo tiene una convergencia lineal, tiene una recta con una pendiente pequeña (0.39 aprox), no tiene zigzag como la bisección porque el error se aproxima desde un solo lado (sin cambio de signo).
El metodo de la falsa posicion tiene una convergencia lineal, con una pendiente de 0.05 constante y muy empinada.
El metodo de la secante tiene una convergencia superlineal, la pendiente crece *1.617 por iteracion, siendo cada vez mas pronunciada, no puede clasificarse como lineal pero tampoco como cuadratica (superlineal).
El metodo de Netwon-Raphson y Newton-Raphson mejorado tienen una convergencia cuadratica, la pendiente crece en cada iteracion generando casi una curva pero al realizar pocas iteraciones esta no se aprecia (ambos metodos se superponen en la grafica).

# 6.3 ¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?
Metodos cerrados
Solamente bisección y falsa posición requieren un intervalo con cambio de signo, esto ya que mantienen la raiz dentro del intervalo [a,b] y utilizan el teorema de Bolzano, necesitando una f continua para ello, se apoyan en descartar el subintervalo donde f NO cambia de signo y lo descartan.
Metodos abiertos
Punto fijo, secante, Newton y Newton mejorado no necesitan el intervalo con cambio de signo, esto debido a que no utilizan el teorema de Bolzano y no necesitan verificar el signo de la f continua.

# 6.4 En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?
Al ser la funcion (x - 2)^2 
Bisección y falsa posición no aplican porque, al no haber un cambio de signo, no es posible aplicar el teorema de Bolzano.
Punto fijo y newton realizaron la misma cantidad de iteraciones, alcanzando el mismo valor 0.1999921875
Secante realizo 15 iteraciones (la mayor de todos) y llego al valor 2.000825
El metodo que se comporta mejor entre los 4 es Newton mejorado, converge en 1 iteración con el valor exacto 2.

# 6.5 ¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?
Con los metodos cerrados conviene utilizar intervalos pequeños, esto para reducir la cantidad de iteraciones totales en el caso de la bisección y para una convergencia rapida en el caso de la falsa posicion, por otro lado, en los metodos abiertos como la secante, si x0 se esta muy alejado de la raiz existe la posibilidad de que diverga o que no garantice que el metodo converga.

# 6.6 ¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?
Para las funciones ya vistas, puede recomendarse un metodo de acuerdo a los experimentos realizados y a los datos recopilados en las tablas .csv y con los graficos de una forma mas visual.
1. Polinómica simple: El metodo de la secante demuestra una precision mayor que newton mejorado, sacrificando un poco de velocidad a cambio de resultados mas precisos.
2. Polinómica doble: El caso de la polinomica doble es diferente, ya que los metodos cerrados no aplican debido a que esta nunca cambia de signo (simpre positivo), en este caso, el indiscutido ganador entre los metodos abiertos es newton mejorado, alcanzando el resultado mas preciso en 1 sola iteracion, la justificacion de esto es que alcanca m = 2 desde cualquier punto inicial gracias a la primera derivada, siendo esta en este caso, la raiz buscada.
3. Logarítmica: En este tipo de funciones es aplicable tanto newton mejorado como el metodo de la secante, si se busca llegar al resultado en las menores iteraciones posibles, secante es la eleccion, mientras que newton mejorado a medida que itera posee un error aproximado cada vez menor.
4. Exponencial: Al igual que en la funcion logaritmica, en la exponencial existe una leve diferencia entre la secante y newton mejorado, pero esta vez newton mejorado siempre esta acotado por la secante, necesitando menos iteraciones, pero la secante llega a un resultado mas preciso. Mi veredicto para este caso, seria escoger el metodo de la secante.
5. Trigonométrica: En este caso newton mejorado es la opcion mas rapida y precisa.
6. Mixta: El metodo de la secante es la mas rapida y precisa entre los 3 mejores candidatos (secante, newton mejorado, falsa posicion).

# Conclusion

# Graficos (src/assets)
Graficos de convergencia y de raices generados:

1. Convergencia exponencial
2. Convergencia logaritmica
3. Convergencia mixta
4. Convergencia polinomica simple
5. Convergencia polinomica doble
6. Convergencia trigonometrica

7. Raiz de la funcion exponencial
8. Raiz de la funcion logaritmica
9. Raiz de la funcion mixta
10. Raiz de la funcion polinomica simple
11. Raiz de la funcion polinomica doble
12. Raiz de la funcion trigonometrica