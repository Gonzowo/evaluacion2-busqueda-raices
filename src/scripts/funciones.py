""""
Raíces conocidas:
    polinomica_simple : x^3 - x - 2        -> 1.5213797068045676
    polinomica_doble  : (x - 2)^2          -> 2
    logaritmica       : ln(x) + x - 4      -> 2.9262710624435009
    exponencial       : exp(-x) - x        -> 0.5671432904097839
    trigonometrica    : cos(x) - x         -> 0.7390851332151607
    mixta             : sqrt(x) - cos(x)   -> 0.6417143708728827
"""

import numpy as np


casos = [
    {
        "nombre": "polinomica_simple",
        "expresion": "x^3 - x - 2",
        "categoria": "polinomica",
        "f": lambda x: x**3 - x - 2,
        "df": lambda x: 3 * x**2 - 1,
        "intervalo": (1.0, 2.0), "x0": 1.0, "x1": 2.0,
        "g": lambda x: np.cbrt(x + 2), "multiplicidad": 1,
        "raiz": 1.5213797068045676,
    },
    {
        "nombre": "polinomica_doble",
        "expresion": "(x - 2)^2",
        "categoria": "polinomica_raiz_doble",
        "f": lambda x: (x - 2) ** 2,
        "df": lambda x: 2 * (x - 2),
        "intervalo": None, "x0": 1.2, "x1": 2.5,
        "g": lambda x: (x + 2) / 2, "multiplicidad": 2,
        "raiz": 2.0,
    },
    {
        "nombre": "logaritmica",
        "expresion": "ln(x) + x - 4",
        "categoria": "logaritmica",
        "f": lambda x: np.log(x) + x - 4,
        "df": lambda x: 1 / x + 1,
        "intervalo": (2.0, 3.0), "x0": 2.0, "x1": 3.0,
        "g": lambda x: 4 - np.log(x), "multiplicidad": 1,
        "raiz": 2.9262710624435009,
    },
    {
        "nombre": "exponencial",
        "expresion": "exp(-x) - x",
        "categoria": "exponencial",
        "f": lambda x: np.exp(-x) - x,
        "df": lambda x: -np.exp(-x) - 1,
        "intervalo": (0.0, 1.0), "x0": 0.0, "x1": 1.0,
        "g": lambda x: np.exp(-x), "multiplicidad": 1,
        "raiz": 0.5671432904097839,
    },
    {
        "nombre": "trigonometrica",
        "expresion": "cos(x) - x",
        "categoria": "trigonometrica",
        "f": lambda x: np.cos(x) - x,
        "df": lambda x: -np.sin(x) - 1,
        "intervalo": (0.0, 1.0), "x0": 0.0, "x1": 1.0,
        "g": lambda x: np.cos(x), "multiplicidad": 1,
        "raiz": 0.7390851332151607,
    },
    {
        "nombre": "mixta",
        "expresion": "sqrt(x) - cos(x)",
        "categoria": "mixta",
        "f": lambda x: np.sqrt(x) - np.cos(x),
        "df": lambda x: 1 / (2 * np.sqrt(x)) + np.sin(x),
        "intervalo": (0.1, 1.0), "x0": 0.1, "x1": 1.0,
        "g": lambda x: x - 0.5 * (np.sqrt(x) - np.cos(x)), "multiplicidad": 1,
        "raiz": 0.6417143708728827,
    },
]


if __name__ == "__main__":
    for caso in casos:
        r = caso["raiz"]
        print(f"{caso['nombre']:<18} raiz = {r:.16f}  "
              f"f(raiz) = {caso['f'](r): .2e}  f'(raiz) = {caso['df'](r): .2e}")
