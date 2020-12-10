import time


def time_of_function(function):
    def wrapped(*args):
        start = time.perf_counter()
        res = function(*args)
        print('Time run:', time.perf_counter() - start)
        return res

    return wrapped


def cache(function):
    print(f"cahed function - {function.__name__}")
    cache = {}

    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = function(*args)
            return cache[args]

    return wrapper



@cache
def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


@time_of_function
@cache
def long_sum(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum


def main():
    start = time.perf_counter()
    fib(10)  # 0.003351
    print('Time run:', time.perf_counter() - start)
    start = time.perf_counter()
    fib(400)  # 0.37117
    print('Time run:', time.perf_counter() - start)
    start = time.perf_counter()
    fib(400)  # 0.003351
    print('Time run:', time.perf_counter() - start)
    long_sum(10 ** 7)  # 0.003351
    long_sum(10 ** 7)  # 0.003351


if __name__ == "__main__":
    main()
