import math
import numpy as np
from sympy import *
import matplotlib.pyplot as plt

init_printing(use_unicode=False, wrap_line=True)
x, y, a, b, t = symbols("x y a b t")
# Yt = Function("Y_t")
# Vy = Function("Vy_t")
# Yx = sympy.Function("Y_x")
# Xt = sympy.Function("X_t")
g = 9.81
v0 = 150
a = pi/40
b = 1
Vy0 = v0 * sin(a)
Vx0 = v0 * cos(a)

Xt = Vx0 * (1 - exp(-b * t)) / b
Yt = ((Vy0 + g / b) * (1 - exp(-b * t)) - g * t) / b

tax = np.linspace(0, 200, 1000)

plt.axis([0, 100, 0, 100])

ya = [Yt.subs(t, i).n() for i in tax]
xa = [Xt.subs(t, i).n() for i in tax]

plt.plot(xa, ya)
plt.show()
