import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


def countnok_n(l: list):
    a = l[0]

    for i in l:
        a = lcm(a, i)

    return a


def countnod_n(l: list):
    return min([math.gcd(x, y) for x in l for y in l])


l = list(map(int, input("Input list - ").split()))
print(f"Nod - {countnod_n(l)}")
print(f"NOK - {countnok_n(l)}")
