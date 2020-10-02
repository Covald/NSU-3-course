from sympy import symbols, integrate

"""
x/((x**2+1)**3)
sqrt(2) oo
"""

x = symbols("x")

expr = input("Enter expression - ")
print(map(int, input("Enter a, b - ").split()))
a, b = map(int, input("Enter a, b - ").split())

Integ = integrate(expr, x)
Integ1 = integrate(expr, (x, a, b))

print(Integ)
print(Integ1.n())
