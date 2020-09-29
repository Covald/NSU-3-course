from typing import List


def countnod(a, b):  # Алгоритм Евклида
    if a < b:
        temp = b
        b = a
        a = temp

    while b != 0:
        x = a % b;
        a = b;
        b = x;

    return a


def countnok_ab(a, b):
    return (a * b / countnod(a, b));


def countnok_n(l: list):
    a = l[0]

    for i in l:
        a = countnok_ab(a, i)

    return a

print(countnok_n([2, 7, 5, 6]))
