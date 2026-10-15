"""Método de la secante."""

from utilidades import _cumple_tolerancia, _guardar, _resultado


def secante(f, x0, x1, tol=1e-6, max_iter=100, raiz=None):
    """Busca una raíz a partir de dos aproximaciones iniciales."""
    historial = []
    for n in range(1, max_iter + 1):
        denominador = f(x1) - f(x0)
        if denominador == 0:
            return _resultado(x1, n - 1, historial, False, "division_por_cero")
        x2 = x1 - f(x1) * (x1 - x0) / denominador
        fx, _ = _guardar(historial, n, x2, x1, f, raiz)
        if _cumple_tolerancia(fx, x2, x1, tol):
            return _resultado(x2, n, historial, True, "convergio")
        x0, x1 = x1, x2
    return _resultado(x1, max_iter, historial, False, "max_iteraciones")
