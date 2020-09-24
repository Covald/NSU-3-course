import math
from decimal import *

N = 20
K = N+500

print(Decimal(math.pi).quantize(Decimal("1."+"0"*N)))
getcontext().prec = 50


def elem_chud(y):
    return Decimal(Decimal(Decimal(pow(-1, y)) * Decimal(math.factorial(6 * y)) * Decimal(13591409 + 545140134 * y)) /
                   Decimal(Decimal((math.factorial(3 * y)) * (Decimal(math.factorial(y))**Decimal("3")) *
                           Decimal(Decimal("640320") ** Decimal(3 * y + Decimal("1.5"))))))

print([elem_chud(i) for i in range(K + 1)])
pi = (Decimal("12") * Decimal(sum([elem_chud(i) for i in range(K + 1)]))) ** -1

print(pi.quantize(Decimal("1." + "0" * N)))
