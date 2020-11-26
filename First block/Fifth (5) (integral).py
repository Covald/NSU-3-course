import math

from sympy import symbols, integrate, lambdify, sympify
from sympy.parsing.sympy_parser import parse_expr
from scipy import integrate as integ


def main(expr=None, a=None, b=None):
    """
    x/((x**2+1)**3)
    sqrt(2) oo
    """

    x = symbols("x")

    if not expr:
        expr = input("Enter expression - ")
    if not a or not b:
        a, b = input("Enter a, b - ").split()

        
    print(expr + "\n" + f"a = {a} \nb = {b}")
    print(integrate(expr, x))
    print(integrate(expr, (x, a, b)))

    expr = sympify(expr)
    a = sympify(a)
    b = sympify(b)
    expr = lambdify(x, expr, 'scipy')

    print(f"Численно - {integ.quad(expr, a, b)}")


def test():
    main("x/((x**2+1)**3)", "sqrt(2)", "oo")


if __name__ == "__main__":
    test()
