import math


def func(a, b, c):
    d = b ** 2 - 4 * a * c
    print(f"Discriminant is {d.real}")
    if d==0:
        return [-b / (2 * a)]
    else:
        return [(-b + pow(d.real, 0.5)) / (2 * a), (-b - pow(d.real, 0.5)) / (2 * a)]


a, b, c = map(complex, input("Input a,b,c from ax^2+bx+c=0 - ").split())
print(f"Answer - {func(a, b, c)}")
