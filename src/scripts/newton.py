"""Método de Newton-Raphson."""

from utilidades import _cumple_tolerancia, _guardar, _resultado


def newton(f, df, x, tol=1e-6, max_iter=100, raiz=None):
    """Método de Newton-Raphson."""
    historial = []
    for n in range(1, max_iter + 1):
        derivada = df(x)
        if derivada == 0:
            return _resultado(x, n - 1, historial, False, "derivada_cero")
        x_nuevo = x - f(x) / derivada
        fx, _ = _guardar(historial, n, x_nuevo, x, f, raiz)
        if _cumple_tolerancia(fx, x_nuevo, x, tol):
            return _resultado(x_nuevo, n, historial, True, "convergio")
        x = x_nuevo
    return _resultado(x, max_iter, historial, False, "max_iteraciones")
