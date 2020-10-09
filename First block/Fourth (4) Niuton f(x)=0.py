import math


def F(x):
    return x**2-9


# производная
def F1(x):
    return 2*x


def Method(a, b, c=5):

    x0 = (a + b) / 2
    xn = F(x0)
    xn1 = xn - F(xn) / F1(xn)
    while abs(xn1 - xn) > math.pow(10, -1*c):
        xn = xn1  # вот так надо было
        xn1 = xn - F(xn) / F1(xn)
    return xn1





