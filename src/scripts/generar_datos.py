"""Genera CSV de muestreo de funciones y de resumen de convergencia."""

import csv
import numpy as np


def guardar_funcion(caso, carpeta):
    """Genera un CSV con valores muestreados de la función del caso."""
    if caso["intervalo"]:
        a, b = caso["intervalo"]
    else:
        a, b = 1.0, 3.0
    x = np.linspace(a, b, 400)

    archivo_csv = f"{carpeta}/{caso['nombre']}.csv"
    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow(["x", "f(x)"])
        for xi in x:
            f_x = caso["f"](xi)
            escritor.writerow([f"{xi:.10f}", f"{f_x:.10f}"])


def guardar_resumen_convergencia(resultados, carpeta):
    """Genera un resumen CSV con la salida final de cada método y función."""
    archivo_csv = f"{carpeta}/resumen_convergencia.csv"
    with open(archivo_csv, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo, delimiter=";")
        escritor.writerow([
            "funcion", "metodo", "iteraciones", "raiz", "error_final", "convergio", "estado"
        ])
        for resultado in resultados:
            escritor.writerow([
                resultado["funcion"],
                resultado["metodo"],
                resultado["iteraciones"],
                resultado["raiz"],
                resultado["error_final"],
                resultado["convergio"],
                resultado["estado"],
            ])


