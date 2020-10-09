def countnod(a, b):  # Алгоритм Евклида
    if a < b:
        temp = b
        b = a
        a = temp

    while b != 0:
        x = a % b
        a = b
        b = x

    return a


def countnok_ab(a, b):
    return (a * b / countnod(a, b))


def countnok_n(l: list):
    a = l[0]

    for i in l:
        a = countnok_ab(a, i)

    return a


def countnod_n(l: list):
    return min([countnod(x, y) for x in l for y in l])


l = list(map(int, input("Input list - ").split()))
print(f"Nod - {countnod_n(l)}")
print(f"NOK - {countnok_n(l)}")
