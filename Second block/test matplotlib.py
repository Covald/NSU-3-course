import math
import numpy
import sympy
import matplotlib.pyplot as plt

sympy.init_printing(use_unicode=False, wrap_line=True)
x, y = sympy.symbols("x y")
a = numpy.pi / 4
g = 9.81
v0 = 15

Vx0 = v0 * sympy.cos(a)
Vy0 = v0 * sympy.sin(a)


def y(k):
    return k * numpy.tan(a) - k ** 2 * (g / Vy0 ** 2 / 2) * (1 + numpy.tan(a) ** 2)


x_ax = numpy.linspace(0, v0 ** 2 * numpy.sin(2 * a) / g, 100)
plt.axis([0, 100, 0, 100])
plt.plot(x_ax, y(x_ax))
plt.show()
