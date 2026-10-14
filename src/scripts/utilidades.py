"""Funciones internas compartidas por los métodos numéricos."""

import numpy as np


def _guardar(historial, n, x, x_anterior, f, raiz):
    fx = f(x)
    if raiz is not None:
        error = abs(x - raiz)
    elif x_anterior is not None:
        error = abs(x - x_anterior)
    else:
        error = None
    historial.append({"iteracion": n, "x": x, "error": error, "residuo": abs(fx), "f_x": fx})
    return fx, error


def _resultado(x, n, historial, convergio, estado):
    return {"raiz": x, "iteraciones": n, "historial": historial,
            "convergio": convergio, "estado": estado}


def _cumple_tolerancia(fx, x, x_anterior, tol):
    """Comprueba el residuo o la diferencia entre iteraciones consecutivas."""
    error_paso = None if x_anterior is None else abs(x - x_anterior)
    return abs(fx) < tol or (error_paso is not None and error_paso < tol)


def _orden(historial):
    errores = [p["error"] for p in historial if p["error"] not in (None, 0)]
    if len(errores) < 3:
        return ""
    e0, e1, e2 = errores[-3:]
    if e0 == e1 or e1 == e2:
        return ""
    return np.log(e2 / e1) / np.log(e1 / e0)
