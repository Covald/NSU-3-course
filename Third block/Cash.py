import functools
import time


def time_of_function(function):

    def wrapped(*args, **kwargs):
        start = time.perf_counter()
        res = function(*args, **kwargs)
        print('Time run:', time.perf_counter() - start)
        return res

    return wrapped


def caching(timeout=600):
    assert isinstance(timeout, int), "Wrong type, expected <type 'int'>, got {}.".format(type(timeout))
    assert timeout > 0, '"timeout" must be bigger 0, got {}.'.format(timeout)

    def param_decorator(func):
        cache_results = {}

        @functools.wraps(func)  # Замещает атрибуты обертки на оборачиваемые
        def inner(*args, **kwargs):

            key = args + tuple(kwargs)

            if key in cache_results and cache_results[key][0] + timeout >= time.time():
                return cache_results[key][1]
            else:
                value = (time.time(), func(*args, **kwargs))
                cache_results[key] = value
                return value[1]

        return inner

    return param_decorator


@time_of_function
def fibonachi(n):
    @caching()
    def fib(num):
        if num < 2:
            return num
        return fib(num - 1) + fib(num - 2)

    return fib(n)


@time_of_function
@caching(10)
def long_sum(n):
    summa = 0
    for i in range(n):
        summa += i
    return summa


def main():
    fibonachi(400)  # 0.003351
    fibonachi(400)

    long_sum(10 ** 8)  # 6
    long_sum(10 ** 8)  # 2*10**-6
    time.sleep(20)
    long_sum(10 ** 8)
    long_sum(10 ** 8)


if __name__ == "__main__":
    main()
