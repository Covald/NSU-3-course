import timeit
from pylab import plot, show, axis
from numpy import random, sqrt, pi

# scattering n points over the unit square
n = 10 ** 9


def test(data):
    p = random.rand(n, 2)

    # counting the points inside the unit circle
    idx = sqrt(p[:, 0] ** 2 + p[:, 1] ** 2) < 1

    plot(p[idx, 0], p[idx, 1], 'b.')  # point inside
    plot(p[idx == False, 0], p[idx == False, 1], 'r.')  # point outside
    axis([-0.1, 1.1, -0.1, 1.1])
    # show()


print(timeit.timeit("test(n)", setup="from __main__ import test, n", number=1))

# estimation of pi
# print('%0.16f' % (sum(idx).astype('double') / n * 4), 'result')
# print('%0.16f' % pi, 'real pi')
