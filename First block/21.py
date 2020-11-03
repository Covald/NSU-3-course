import matplotlib.pyplot as plt
from numpy import pi, sin, cos, abs, sqrt, linspace


def main():
    def y(t):
        return 2 - 2 * sin(t) + (sin(t) * sqrt(abs(cos(t))) / (sin(t) + 7 / 3))

    t = linspace(-pi, pi, 1000)

    fig = plt.figure()
    ax1 = fig.add_subplot(projection='polar')
    ax1.plot(t, y(t))
    ax1.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
