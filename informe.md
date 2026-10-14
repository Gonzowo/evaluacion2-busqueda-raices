# Avance del informe: búsqueda de raíces

## Introducción

Este trabajo implementa y compara seis métodos numéricos para aproximar raíces de funciones. Se consideran funciones polinómicas, logarítmicas, exponenciales, trigonométricas y una función mixta. Para cada caso se especifican una función, su derivada cuando corresponde, una función de iteración para punto fijo, valores iniciales y, en los casos aplicables, un intervalo de búsqueda.

La comparación registra el número de iteraciones requerido por cada método bajo los mismos parámetros de tolerancia y límite de iteraciones. Las aproximaciones obtenidas se contrastan con las raíces de referencia definidas en el programa.

## Funciones utilizadas

| Categoría | Función | Intervalo o valores iniciales | Raíz de referencia |
|---|---|---|---:|
| Polinómica | $x^3-x-2$ | $[1,2]$; $x_0=1$, $x_1=2$ | 1.5213797068045676 |
| Polinómica con raíz doble | $(x-2)^2$ | Sin intervalo; $x_0=1.2$, $x_1=2.5$ | 2 |
| Logarítmica | $\ln(x)+x-4$ | $[2,3]$; $x_0=2$, $x_1=3$ | 2.9262710624435009 |
| Exponencial | $e^{-x}-x$ | $[0,1]$; $x_0=0$, $x_1=1$ | 0.5671432904097839 |
| Trigonométrica | $\cos(x)-x$ | $[0,1]$; $x_0=0$, $x_1=1$ | 0.7390851332151607 |
| Mixta | $\sqrt{x}-\cos(x)$ | $[0.1,1]$; $x_0=0.1$, $x_1=1$ | 0.6417143708728827 |

Las raíces de referencia son valores conocidos incorporados en `funciones.py`. Para la función polinómica con raíz doble, el intervalo se deja sin definir porque la función toca el eje en $x=2$ sin cambiar de signo.

## Métodos numéricos

- **Bisección:** divide sucesivamente un intervalo con cambio de signo.
- **Falsa posición:** aproxima la raíz mediante la intersección con el eje $x$ de la recta que une los extremos del intervalo.
- **Punto fijo:** itera la función $g(x)$ definida para cada caso.
- **Secante:** calcula aproximaciones usando dos valores iniciales, sin requerir la derivada.
- **Newton-Raphson:** utiliza la función y su derivada para actualizar la aproximación.
- **Newton-Raphson mejorado:** aplica el método de Newton con el factor de multiplicidad indicado para cada raíz.

## Condiciones del experimento y restricciones

Los experimentos se ejecutan con las funciones, intervalos, aproximaciones iniciales, derivadas y funciones de iteración definidos en `src/scripts/funciones.py`. Estos valores permanecen fijos durante la comparación.

Se utiliza una tolerancia de $10^{-6}$ y un máximo de 100 iteraciones. El programa detiene cada método cuando el residuo $|f(x_n)|$ o la diferencia entre aproximaciones consecutivas $|x_n-x_{n-1}|$ es menor que la tolerancia. El error informado se calcula como $|x_n-r|$ porque las raíces de referencia se conocen para estos casos.

Bisección y falsa posición requieren un intervalo; en el caso de la raíz doble no se ejecutan y se registran como “No aplica”. Los resultados corresponden a estas configuraciones controladas y no incluyen variaciones de intervalos, valores iniciales, tolerancia o condiciones de redondeo.

## Resultados de convergencia

La tabla resume las iteraciones registradas por los métodos aplicables. En esta configuración, todos alcanzaron el criterio de parada antes del máximo de iteraciones.

| Función | Bisección | Falsa posición | Punto fijo | Secante | Newton-Raphson | Newton mejorado |
|---|---:|---:|---:|---:|---:|---:|
| Polinómica | 20 | 12 | 8 | 6 | 5 | 5 |
| Polinómica con raíz doble | No aplica | No aplica | 10 | 15 | 10 | 1 |
| Logarítmica | 19 | 4 | 14 | 3 | 3 | 3 |
| Exponencial | 20 | 7 | 25 | 4 | 3 | 3 |
| Trigonométrica | 20 | 5 | 34 | 4 | 4 | 4 |
| Mixta | 20 | 4 | 15 | 3 | 3 | 3 |

Los conteos corresponden a la implementación actual, con la tolerancia, el máximo de iteraciones y los datos iniciales indicados anteriormente. Las curvas de error por iteración guardadas en `src/assets/` complementan esta tabla.
