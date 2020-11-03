from numpy import pi, sin, cos, abs, sqrt, linspace
from pylab import plot, show, axis
import matplotlib.pyplot as plt

def main():
    def y(t):
        return 2 - 2 * sin(t) + (sin(t) * sqrt(abs(cos(t))) / (sin(t) + 7 / 3))

    t = linspace(-pi, pi, 1000)

    # plot(y(t)*cos(t), y(t)*sin(t))
    # axis([-pi, pi, -pi, pi])
    # show()
    fig = plt.figure()
    ax1 = fig.add_subplot(projection='polar')
    ax1.plot(t, y(t))
    ax1.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
