# Evaluación 2: La Raiz que se Esconde

Universidad Católica del Maule - Lab evaluado 2

## Integrantes

Gonzalo Cerpa Salas

## Resumen

Este trabajo busca implementar en codigo python 6 metodos de busqueda de raices, sobre 6 funciones matematicas distintas.

Estas funciones matematicas son:
1. Polinómica
2. Polinómica doble
3. Logaritmica
4. Exponencial
5. Trigonométrica
6. Mixta

Los metodos son:
1. Bisección
2. Falsa Posición
3. Punto Fijo
4. Newton-Raphson
5. Newton-Raphson Mejorado
6. Secante

## Entorno

Requiere Python 3.10 o posterior, Numpy y MatplotLib.

Para un detalle de las dependencias del proyecto, estas se encuentran en el archivo requirements.txt.

## Ejecucion

1. Descargar el repositorio y abrir la carpeta raiz (evaluacion2-busqueda-raices)
2. Abrir la terminal de VisualStudioCode o powershell en el directorio.
3. (Solo una vez) Crear el entorno virtual con `py -m venv .venv`
4. (Solo una vez) Instalar las dependencias con `python -m pip install -r requirements.txt`
5. Desde VisualStudioCode (o desde powershell, navegando hasta la carpeta raiz) ejecutar el comando: `.\.venv\Scripts\python.exe src\scripts\evaluacion.py` .
6. Una vez termina la ejecución, se generan los CSV asociados a cada funcion en `src/data/` y gráficos PNG en `src/assets/`.

## Scripts

| Archivo | Descripcion |
| evaluacion.py | Llama a las funciones creadas por los demas archivos para realizar la comparativa de metodos en cada funcion |
| funciones.py | Define las funciones matemáticas, sus derivadas y los datos iniciales para cada caso |
| biseccion.py | Implementa el método de bisección |
| falsa_posicion.py | Implementa el método de falsa posición |
| punto_fijo.py | Implementa el método de punto fijo |
| secante.py | Implementa el método de la secante |
| newton.py | Implementa el método de Newton-Raphson |
| newton_mejorado.py | Implementa Newton-Raphson con una corrección para raíces de multiplicidad conocida |
| utilidades.py | Contiene funciones auxiliares compartidas para registrar iteraciones y organizar resultados |
| generar_datos.py | Genera archivos CSV con valores muestreados de las funciones |
| generar_graficos.py | Genera gráficos de las funciones y de la convergencia de los métodos |

## Funciones con raiz conocida

| Categoria | Funcion | Intervalo  | Raiz conocida |
| polinomica | x³ - x - 2 | Intervalo: [1, 2]; x₀ = 1, x₁ = 2 | 1.5213797068045676 |
| polinomica_raiz_doble | (x - 2)² | Sin intervalo; x₀ = 1.2, x₁ = 2.5 | 2 |
| logaritmica | ln(x) + x - 4 | Intervalo: [2, 3]; x₀ = 2, x₁ = 3 | 2.9262710624435009 |
| exponencial | exp(-x) - x | Intervalo: [0, 1]; x₀ = 0, x₁ = 1 | 0.5671432904097839 |
| trigonometrica | cos(x) - x | Intervalo: [0, 1]; x₀ = 0, x₁ = 1 | 0.7390851332151607 |
| mixta | √x - cos(x) | Intervalo: [0.1, 1]; x₀ = 0.1, x₁ = 1 | 0.6417143708728827 |

## Ambiente controlado

La razon de que algunas funciones posean un intervalo de evaluacion es para que sean reproducibles y demostrables, otras condiciones son:
1. Tamaño de paso para metodos cerrados, estimación inicial x₀ y x₁ para metodos abiertos.
2. Tolerancia de 0.000001 y maximo de 100 interaciones.
3. Cuando el caso tiene un intervalo, se calcula el producto de f(a) y f(b) para observar si hay cambio de signo.