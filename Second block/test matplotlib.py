import math
import numpy
import sympy
import matplotlib.pyplot as plt

sympy.init_printing(use_unicode=False, wrap_line=True)
x, y, a, b, t = sympy.symbols("x y a b t")
Yt = sympy.Function("Y_t")
Vy = sympy.Function("Vy_t")
Yx = sympy.Function("Y_x")
Xt = sympy.Function("X_t")
g = 9.81
v0 = 15

Vx0 = v0 * sympy.cos(a)
Vy0 = v0 * sympy.sin(a)

Ay = lambda k: -g - b * Vy(k).diff() * sympy.sign(Vy(k))
#Ax = lambda k: -g - b * c
#sympy.Equality

print(sympy.dsolve(Vy(t) - Ay(t)))
#expr = sympy.solve(Vy(0)-Vy0)

# expr =
# sympy.dsolve(Vy(0))
# print(sympy.dsolve((Yt(t).diff(2) - Ay(t), Yt(0).diff() - Vy0, Yt(0))))
