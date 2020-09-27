import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#a, b, c, d = [0.8, 0.5, 0.8, 0.5]  # map(float, input("Enter a, b, c, d -").split())
a = 1.
b = 0.1
c = 1.5
d = 0.75
base = [2, 5]  # map(int, input("Enter x and y - ").split())


# create function
def f(y, t):
    y1, y2 = y
    return [(a - b * y1) * y2, (-b + c * y2) * y1]


t = np.linspace(0, 10, 41)  # vector of time
y0 = base  # start value
w = odeint(f, y0, t)  # solve eq.
y1 = w[:, 0]
y2 = w[:, 1]
fig = plt.figure(facecolor='white')
plt.plot(t, y1, '-o', t, y2, '-o', linewidth=2)
plt.ylabel("z")
plt.xlabel("t")
plt.grid(True)
plt.show()  # display
