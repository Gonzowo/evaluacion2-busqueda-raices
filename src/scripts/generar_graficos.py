"""Crea gráficos de las funciones y de la convergencia."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from textwrap import fill


def graficar_funcion(caso, carpeta, raiz):
    if caso["intervalo"]:
        a, b = caso["intervalo"]
    else:
        a, b = 1.0, 3.0
    x = np.linspace(a, b, 400)
    y = [caso["f"](xi) for xi in x]

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"f(x) = {caso['expresion']}")
    plt.axhline(0, color="black", linewidth=0.8)
    if raiz is not None:
        if caso["multiplicidad"] == 2:
            etiqueta_raiz = f"raíz doble x = {raiz:.6f}"
        else:
            etiqueta_raiz = f"raíz x = {raiz:.6f}"
        plt.scatter(raiz, caso["f"](raiz), color="red", label=etiqueta_raiz, zorder=3)
        if caso["multiplicidad"] == 2:
            plt.annotate(etiqueta_raiz, (raiz, caso["f"](raiz)), xytext=(12, 18),
                         textcoords="offset points", arrowprops={"arrowstyle": "->"})
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"{caso['nombre']}\nf(x) = {caso['expresion']}")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{carpeta}/{caso['nombre']}.png")
    plt.close()


def graficar_convergencia(resultados, carpeta, nombre, expresion):
    plt.figure(figsize=(8, 5))
    piso_error = 1e-12
    for r in resultados:
        pasos = [paso for paso in r["historial"] if paso["error"] is not None]
        x = [paso["iteracion"] for paso in pasos]
        error = [max(paso["error"], piso_error) for paso in pasos]
        if x:
            plt.semilogy(x, error, marker="o", label=r["metodo"])
    plt.xlabel("Iteración")
    plt.ylabel("Error aproximado")
    plt.title(f"Error por iteración: {nombre}\nf(x) = {expresion}")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{carpeta}/convergencia_{nombre}.png")
    plt.close()


def graficar_resumen(resultados, carpeta):
    funciones = sorted(set(r["funcion"] for r in resultados))
    metodos = sorted(set(r["metodo"] for r in resultados))
    ancho = 0.8 / len(metodos)
    posiciones = np.arange(len(funciones))

    plt.figure(figsize=(10, 5))
    for i, metodo in enumerate(metodos):
        iteraciones = []
        for funcion in funciones:
            fila = next(r for r in resultados if r["funcion"] == funcion and r["metodo"] == metodo)
            iteraciones.append(fila["iteraciones"])
        plt.bar(posiciones + i * ancho, iteraciones, ancho, label=metodo)
    plt.xticks(posiciones + ancho * len(metodos) / 2, funciones, rotation=25)
    plt.xlabel("Función")
    plt.ylabel("Iteraciones")
    expresiones = sorted(set(r["expresion"] for r in resultados))
    detalle_funciones = fill("Funciones: " + "; ".join(expresiones), width=80)
    plt.title(
        "Iteraciones por método y función\n" + detalle_funciones,
        fontsize=10,
    )
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{carpeta}/resumen_iteraciones.png")
    plt.close()
