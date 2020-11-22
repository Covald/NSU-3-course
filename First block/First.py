from cmath import sqrt


def func(a, b, c):
    d = b ** 2 - 4 * a * c
    print(f"Discriminant is {d}")
    if a == 0 and b == 0:
        raise ValueError()
    elif a == 0:
        return [-c / b]
    elif d == 0:
        return [-b / (2 * a)]
    else:
        return [(-b.real + sqrt(d)) / (2 * a.real), (-b.real - sqrt(d)) / (2 * a.real)]

# a, b, c = map(int, input("Input a,b,c from ax^2+bx+c=0 - ").split())
# print(f"Answer - {func(a, b, c)}")
