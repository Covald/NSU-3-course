import time


def time_of_function(function):
    def wrapped(*args, **kwargs):
        start_time = time.perf_counter()
        res = function(*args, **kwargs)
        print(time.perf_counter() - start_time)
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


def main():
    start = time.perf_counter()
    fib(200)  # 0.003351
    print('Time run:', time.perf_counter() - start)
    start = time.perf_counter()
    fib(300)  # 0.37117
    print('Time run:', time.perf_counter() - start)
    start = time.perf_counter()
    fib(400)  # 0.003351
    print('Time run:', time.perf_counter() - start)


if __name__ == "__main__":
    main()
