import sys
import time

from numpy.random import uniform
from numpy import pi, sin, array, linspace, arange
import numpy as np
from pylab import subplot, plot, xlabel, ylabel, show, axis, axes
from numpy.fft import rfft, irfft
import scipy as sp

FD = 40800  # discr frequency
t = 20    # 20 sec 20/FD 0.0001
t = linspace(0, t*2*pi, int(2*pi*FD))


def plot_spectrum(signal: array, pos: list or tuple):
    n = len(signal)  # length of the signal

    k = arange(n)

    T = n / FD

    frq = k / T  # two sides frequency range
    frq = frq[range(int(n / 2))]  # one side frequency range

    y = rfft(signal) / n  # fft computing and normalization
    y = y[range(int(n / 2))]

    subplot(*pos).grid(True)  # plotting the spectrum
    plot(frq, abs(y), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')


def main():
    first = 7 * sin(2 * pi * 4.8 * t)
    second = 7 * sin(2 * pi * 5 * t)
    third = 7 * sin(2 * pi * 5.2 * t)
    signal = first + second + third
    noise = (np.random.random(t.shape) - 0.5) * np.random.random(t.shape) * 50

    subplot(2, 3, 1).grid(True)
    plot(t, third, "green")
    plot(t, second, "yellow")
    plot(t, first, "blue")
    plot(t, signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal, [2, 3, 4])

    subplot(2, 3, 2).grid(True)
    signal_with_noise = signal + noise
    plot(t, signal_with_noise, "b")
    plot(t, signal, "r")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal_with_noise, (2, 3, 5))

    n = len(signal_with_noise)  # length of the signal
    k = arange(n)
    T = n / FD
    frq = k / T  # two sides frequency range
    frq = frq[range(int(n / 2))]  # one side frequency range
    y = rfft(signal_with_noise) / n  # fft computing and normalization
    y = y[range(int(n / 2))]

    border = np.amax(np.absolute(y)) * 0.20  # Все сигналы меньше 20% максимальной амплитуды будем считать шумом
    y_cut = y.copy()
    y_cut[np.absolute(y) < border] = 0

    subplot(236).grid(True)
    plot(frq, abs(y_cut), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

    signal = irfft(y_cut) * n

    subplot(233).grid(True)
    plot(t[:-3], signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    show()


if __name__ == "__main__":
    main()
