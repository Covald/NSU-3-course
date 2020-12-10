from numpy.random import uniform
from numpy import pi, sin, array, linspace, arange, abs as np_abs
import numpy as np
from pylab import subplot, plot, xlabel, ylabel, show, axis, axes
from numpy.fft import rfft, irfft, rfftfreq

FD = 1024  # discr frequency 1/Td
time = 200  # sec
BORDER = 0.15  # граница среза от макс аплитуды

f_first = 4.8
f_second = 5
f_third = 5.2

A_first = 5
A_second = 7
A_third = 9

w_first = (2. * pi * f_first / FD)
w_second = (2. * pi * f_second / FD)
w_third = (2. * pi * f_third / FD)

N = time * FD  # len of array
t = arange(N)

sig_first = A_first * sin(w_first * t)
sig_second = A_second * sin(w_second * t)
sig_third = A_third * sin(w_third * t)


def plot_spectrum(signal: array, pos: int):
    frq = rfftfreq(N, 1. / FD)

    spectrum = rfft(signal) / N  # fft computing and normalization

    subplot(pos).grid(True)  # plotting the spectrum
    plot(frq, np_abs(spectrum), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')


def main():
    signal = sig_first + sig_second + sig_third
    noise = (np.random.random(t.shape) - 0.5) * np.random.random(t.shape) * 50

    subplot(231).grid(True)
    plot(t / FD, sig_third, "green")
    plot(t / FD, sig_second, "yellow")
    plot(t / FD, sig_first, "blue")
    plot(t / FD, signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal, 234)

    subplot(232).grid(True)
    signal_with_noise = signal + noise
    plot(t / FD, signal_with_noise, "b")
    plot(t / FD, signal, "r")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal_with_noise, 235)

    frq = rfftfreq(N, 1. / FD)

    spectrum = rfft(signal) / N  # fft computing and normalization

    # Все сигналы меньше 20% максимальной амплитуды будем считать шумом
    border = np.amax(np.absolute(spectrum)) * BORDER
    spectrum_cut = spectrum.copy()
    spectrum_cut[np.absolute(spectrum) < border] = 0

    subplot(236).grid(True)
    plot(frq, abs(spectrum_cut), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

    signal = irfft(spectrum_cut) * N

    subplot(233).grid(True)
    plot(t / FD, signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    show()


if __name__ == "__main__":
    main()
