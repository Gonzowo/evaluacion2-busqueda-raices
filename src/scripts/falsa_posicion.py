"""Método de falsa posición."""

from utilidades import _cumple_tolerancia, _guardar, _resultado


def falsa_posicion(f, a, b, tol=1e-6, max_iter=100, raiz=None):
    """Aproxima la raíz usando una recta entre los extremos del intervalo."""
    if f(a) * f(b) >= 0:
        raise ValueError("No hay cambio de signo en [a, b]")
    historial = []
    x_anterior = None
    for n in range(1, max_iter + 1):
        denominador = f(b) - f(a)
        if denominador == 0:
            return _resultado(b, n - 1, historial, False, "division_por_cero")
        x = b - f(b) * (b - a) / denominador
        fx, _ = _guardar(historial, n, x, x_anterior, f, raiz)
        if _cumple_tolerancia(fx, x, x_anterior, tol):
            return _resultado(x, n, historial, True, "convergio")
        if f(a) * fx < 0:
            b = x
        else:
            a = x
        x_anterior = x
    return _resultado(x, max_iter, historial, False, "max_iteraciones")
