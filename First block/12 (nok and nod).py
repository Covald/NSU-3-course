import math
from functools import reduce


def lcm(a, b):
    return a * b // math.gcd(a, b)


l = list(map(int, input("Input list - ").split()))

print(f"Nod - {reduce(math.gcd, l)}")
print(f"NOK - {reduce(lcm, l)}")
