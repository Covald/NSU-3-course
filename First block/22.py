from numpy import *
import pylab as p
from scipy import integrate

a, b, c, d = [1., 0.1, 1.5, 0.75]  # map(float, input("Enter a, b, c, d -").split())
X0 = array([200, 100])  # array(map(float, input("Enter x0 y0 - ").split()))


def dX_dt(X, t=0):
    return array([a * X[0] - b * X[0] * X[1],
                  -c * X[1] + d * b * X[0] * X[1]])


X_f0 = array([2., 5.])
t = linspace(0, 30, 10000)  # time

X, infodict = integrate.odeint(dX_dt, X0, t, full_output=True)

Herbivorous, Predators = X.T

f1 = p.figure()
p.plot(t, Herbivorous, 'r-', label='Herbivorous')
p.plot(t, Predators, 'b-', label='Predators')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('population')
p.title('Evolution of predators and herbivorous populations')
p.show()
