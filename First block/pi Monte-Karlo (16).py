import random
import numpy as np
import matplotlib.pyplot as plt

r = random.randint
xl, yl = [], []

xs = np.random.uniform(-1, 1, 10**6)
ys = np.random.uniform(-1, 1, 10**6)

for i in range(len(xs)):
    if np.sqrt(xs[i] ** 2 + ys[i] ** 2) <= 1:
        xl.append(xs[i])
        yl.append(ys[i])

print(len(xl) / len(xs))
print(4 * len(xl) / len(xs))

plt.scatter(xs, ys, marker='.', s=0.5)
plt.scatter(xl, yl, marker='.', alpha=1, s=0.5)
plt.show()
