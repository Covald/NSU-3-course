import math


def prime_numbers(N):
    print([2] + [x for x in range(3, N + 1, 2) if all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))])


prime_numbers(int(input("Input N - ")))
