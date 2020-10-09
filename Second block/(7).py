import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

V0, y, x, t, a, g = sp.symbols('v0 y x t a g')


def y(t):
    return V0 * sp.sin(a * t) - g * t ** 2 / 2


print(y(x))
