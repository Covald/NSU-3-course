from sympy import *

"""
x/((x**2+1)**3)
sqrt(2) oo
"""

expr = input("Enter expression - ")

x = symbols("x")

a, b = input("Enter a, b - ").split()

Integ = integrate(expr, (x, a, b))

print(Integ)
print(Integ.n())
