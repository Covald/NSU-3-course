import timeit
# from pylab import plot, show, axis
from numpy import random, sqrt, pi
import numba
n = 10 ** 7


def test(data):
    p = random.rand(n, 2)
    idx = sqrt(p[:, 0] ** 2 + p[:, 1] ** 2) < 1
    # x = p[idx, 0]
    # y = p[idx, 1]
    # xt = p[idx == False, 0]
    # yt= p[idx == False, 1]
    # plot(p[idx, 0], p[idx, 1], 'b.')  # point inside
    # plot(p[idx == False, 0], p[idx == False, 1], 'r.')  # point outside
    # axis([-0.1, 1.1, -0.1, 1.1])
    print('%0.16f' % (sum(idx).astype('double') / n * 4), 'result')
    # print('%0.16f' % pi, 'real pi')
    # show()


print(timeit.timeit("test(n)", setup="from __main__ import test, n", number=1))
#test(n)
