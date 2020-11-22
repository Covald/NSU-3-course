from numpy.random import uniform
from numpy import pi, sin, array, linspace, arange
import numpy as np
from pylab import subplot, plot, xlabel, ylabel, show, axis, axes
from numpy.fft import rfft, irfft
import scipy as sp

FD = 1024  # discr frequency
t = FD * 20  # 20 sec
t = linspace(0, 20 * pi, t)


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
    first = 3 * sin(2 * pi * 5.2 * t)
    second = 5 * sin(2 * pi * 5 * t)
    third = 7 * sin(2 * pi * 4.8 * t)
    signal = first + second + third
    noise = 0  # (np.random.random(t.shape) - 0.5) * np.random.random(t.shape) * 50

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

    border = np.amax(np.absolute(y)) * 0.20  # Все сигналы меньше 5% максимальной амплитуды будем считать шумом
    y_cut = y.copy()
    y_cut[np.absolute(y) < border] = 0

    subplot(236).grid(True)
    plot(frq, abs(y), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

    signal = irfft(y) * n

    subplot(233).grid(True)
    plot(t[:-2], signal, "red")  # TODO пофиксить амплитуду и слайс на -2
    xlabel('Time')
    ylabel('Amplitude')

    show()


# def plot_spectrum(signal: array, pos: list):
#     n = len(signal)  # length of the signal
#
#     k = arange(n)
#
#     t = n / S_RATE
#
#     frq = k / t  # two sides frequency range
#     frq = frq[range(int(n / 2))]  # one side frequency range
#
#     y = fft(signal) / n  # fft computing and normalization
#     y = y[range(int(n / 2))]
#
#     ax = subplot(*pos)  # plotting the spectrum
#     ax.grid(True)
#     plot(frq, abs(y), 'r')
#     xlabel('Freq (Hz)')
#     ylabel('|Y(freq)|')


# def clear_noise(sgn: array, t: array) -> array:
#     N = 3  # Filter order
#     Wn = 0.1  # Cutoff frequency
#     B, A = signal.butter(N, Wn, output='ba')
#     sgn = signal.filtfilt(B, A, sgn)
#     ax = subplot(2, 3, 3)
#     ax.grid(True)
#     plot(t, sgn, "r")
#     xlabel('Time')
#     ylabel('Amplitude')
#     return sgn


# def main():
#     sgn_with_noise = create_signal(t, FS)
#     plot_spectrum(sgn_with_noise, FS, [2, 3, 5])
#     sgn_without_noise = clear_noise(sgn_with_noise, t)
#     plot_spectrum(sgn_without_noise, FS, [2, 3, 6])
#
#     show()


if __name__ == "__main__":
    main()
