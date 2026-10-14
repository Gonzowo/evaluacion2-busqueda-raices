"""Método de punto fijo."""

from utilidades import _cumple_tolerancia, _guardar, _resultado


def punto_fijo(g, f, x, tol=1e-6, max_iter=100, raiz=None):
    """Repite x=g(x) hasta cumplir un criterio de parada."""
    historial = []
    for n in range(1, max_iter + 1):
        x_nuevo = g(x)
        fx, _ = _guardar(historial, n, x_nuevo, x, f, raiz)
        if _cumple_tolerancia(fx, x_nuevo, x, tol):
            return _resultado(x_nuevo, n, historial, True, "convergio")
        x = x_nuevo
    return _resultado(x, max_iter, historial, False, "max_iteraciones")
