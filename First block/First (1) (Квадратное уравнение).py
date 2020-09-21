import math


def func(a, b, c):
    d = b ** 2 - 4 * a * c
    print(f"Discriminant is {d.real}")
    if a.real==0 and b.real==0 :
        return [None]
    elif a.real==0:
        return [-c/b]
    elif d==0:
        return [-b.real / (2 * a.real)]
    else:
        return [(-b.real + pow(d.real, 0.5)) / (2 * a.real), (-b.real - pow(d.real, 0.5)) / (2 * a.real)]


a, b, c = map(complex, input("Input a,b,c from ax^2+bx+c=0 - ").split())
print(f"Answer - {func(a, b, c)}")
