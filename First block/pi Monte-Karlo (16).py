import random
import numpy as np
import math
import matplotlib.pyplot as plt

r = random.randint
xl, yl = [], []

np

xs = [r(-100000, 100000) / 100000 for i in range(10000000)]
ys = [r(-100000, 100000) / 100000 for i in range(10000000)]
for i in range(len(xs)):
    if math.sqrt(xs[i] ** 2 + ys[i] ** 2) <= 1:
        xl.append(xs[i])
        yl.append(ys[i])
print(len(xl) / len(xs))
print(4 * len(xl) / len(xs))

plt.scatter(xs, ys, marker='.', s=0.5)
plt.scatter(xl, yl, marker='.', alpha=1, s=0.5)
plt.show()
