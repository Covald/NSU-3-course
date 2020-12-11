from numpy import pi, sin, array, absolute, arange, amax, abs as np_abs
from numpy.fft import rfft, irfft, rfftfreq
from numpy.random import random
from pylab import subplot, plot, xlabel, ylabel, show


def main():
    """
    Constants
    """
    _FD = 90  # sampling frequency 1/Td
    _TIME = 200  # sec
    _BORDER = 0.15  # граница среза от макс аплитуды

    _F_FIRST = 4.8
    _F_SECOND = 5
    _F_THIRD = 5.2

    _A_FIRST = 5
    _A_SECOND = 7
    _A_THIRD = 9
    """
    /Constants
    """

    def plot_spectrum(_signal: array, pos: int, fd: float, n: int):
        """
        Plot spectrum of signal (W0W)
        """
        frequency = rfftfreq(n, 1. / fd)

        _spectrum = rfft(_signal) / n  # fft computing and normalization

        subplot(pos).grid(True)  # plotting the spectrum
        plot(frequency, np_abs(_spectrum), 'r')
        xlabel('Freq (Hz)')
        ylabel('|Y(freq)|')

    w_first = (2. * pi * _F_FIRST / _FD)
    w_second = (2. * pi * _F_SECOND / _FD)
    w_third = (2. * pi * _F_THIRD / _FD)

    len_of_array = _TIME * _FD  # len of array
    t = arange(len_of_array)

    sig_first = _A_FIRST * sin(w_first * t)
    sig_second = _A_SECOND * sin(w_second * t)
    sig_third = _A_THIRD * sin(w_third * t)

    signal = sig_first + sig_second + sig_third
    noise = (random(t.shape) - 0.5) * random(t.shape) * 50

    subplot(231).grid(True)
    plot(t / _FD, sig_third, "green")
    plot(t / _FD, sig_second, "gray")
    plot(t / _FD, sig_first, "blue")
    plot(t / _FD, signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal, 234, _FD, len_of_array)

    subplot(232).grid(True)
    signal_with_noise = signal + noise
    plot(t / _FD, signal_with_noise, "b")
    # plot(t / _FD, signal, "r")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal_with_noise, 235, _FD, len_of_array)

    frq = rfftfreq(len_of_array, 1. / _FD)

    spectrum = rfft(signal) / len_of_array  # fft computing and normalization

    border = amax(absolute(spectrum)) * _BORDER  # Режем шум по % от максимальной амплитуды
    spectrum_cut = spectrum.copy()
    spectrum_cut[absolute(spectrum) < border] = 0

    subplot(236).grid(True)
    plot(frq, np_abs(spectrum_cut), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

    signal = irfft(spectrum_cut) * len_of_array

    subplot(233).grid(True)
    plot(t / _FD, signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    show()


if __name__ == "__main__":
    main()
