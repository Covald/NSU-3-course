from sympy import symbols, integrate


def main(expr=None, a=None, b=None):
    """
    x/((x**2+1)**3)
    sqrt(2) oo
    """

    x = symbols("x")
    if not expr:
        expr = input("Enter expression - ")
    if not a and not b:
        a, b = input("Enter a, b - ").split()
    print(expr + "\n" + f"a = {a} \nb = {b}")
    print(integrate(expr, x).n())
    print(integrate(expr, (x, a, b)))


def test():
    main("x/((x**2+1)**3)", "sqrt(2)", "oo")


test()