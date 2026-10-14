from pathlib import Path

from funciones import casos
from generar_datos import guardar_funcion, guardar_resumen_convergencia
from generar_graficos import graficar_convergencia, graficar_funcion, graficar_resumen
from biseccion import biseccion
from falsa_posicion import falsa_posicion
from newton import newton
from newton_mejorado import newton_mejorado
from punto_fijo import punto_fijo
from secante import secante


tol = 1e-6
max_iter = 100
carpeta_src = Path(__file__).resolve().parent.parent
carpeta_datos = carpeta_src / "data"
carpeta_graficos = carpeta_src / "assets"
resultados = []

for indice, caso in enumerate(casos):
    if indice > 0:
        print()

    nombre = caso["nombre"]
    f = caso["f"]
    df = caso["df"]
    x0 = caso["x0"]
    x1 = caso["x1"]
    raiz_referencia = caso.get("raiz")
    salidas = []

    guardar_funcion(caso, carpeta_datos)

    if caso["intervalo"]:
        a, b = caso["intervalo"]
        fa, fb = f(a), f(b)
        producto_extremos = fa * fb
        print(nombre, "f(a)=", fa, "f(b)=", fb,
              "f(a)f(b)=", producto_extremos,
              "cambio de signo:", producto_extremos < 0)
        salidas.append(("biseccion", biseccion(f, a, b, tol, max_iter, raiz_referencia)))
        salidas.append(("falsa_posicion", falsa_posicion(f, a, b, tol, max_iter, raiz_referencia)))
    else:
        # La raíz doble toca el eje sin cambio de signo; se verifica en x = raíz.
        print(nombre, "raíz doble:", "x =", raiz_referencia,
              "f(x) =", f(raiz_referencia), "f'(x) =", df(raiz_referencia))
        salidas.append(("biseccion", {"raiz": float("nan"), "iteraciones": 0, "historial": []}))
        salidas.append(("falsa_posicion", {"raiz": float("nan"), "iteraciones": 0, "historial": []}))

    salidas.append(("punto_fijo", punto_fijo(caso["g"], f, x0, tol, max_iter, raiz_referencia)))
    salidas.append(("secante", secante(f, x0, x1, tol, max_iter, raiz_referencia)))
    salidas.append(("newton", newton(f, df, x0, tol, max_iter, raiz_referencia)))
    salidas.append(("newton_mejorado", newton_mejorado(
        f, df, x0, caso["multiplicidad"], tol, max_iter, raiz_referencia
    )))

    resultados_caso = []
    raiz_grafico = raiz_referencia
    for metodo, salida in salidas:
        raiz = salida["raiz"]
        if raiz == raiz:  # ignora el NaN 
            error = salida["historial"][-1]["error"] if salida["historial"] else ""
            if raiz_grafico is None:
                raiz_grafico = raiz
        else:
            error = ""
        fila = {
            "funcion": nombre,
            "expresion": caso["expresion"],
            "metodo": metodo,
            "iteraciones": salida["iteraciones"],
            "raiz": raiz,
            "error_final": error,
            "historial": salida["historial"],
            "convergio": salida.get("convergio", False),
            "estado": salida.get("estado", "no_aplica"),
        }
        resultados.append(fila)
        resultados_caso.append(fila)
        if salida["historial"]:
            print(metodo, "raíz =", raiz, "iteraciones =", salida["iteraciones"],
                  "error =", error, "estado =", fila["estado"])

    graficar_funcion(caso, carpeta_graficos, raiz_grafico)
    graficar_convergencia(
        resultados_caso, carpeta_graficos, nombre, caso["expresion"]
    )

guardar_resumen_convergencia(resultados, carpeta_datos)
graficar_resumen(resultados, carpeta_graficos)

print("\n Datos y gráficos creados.")
