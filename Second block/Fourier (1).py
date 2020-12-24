from numpy import pi, sin, array, absolute, arange, amax, abs as np_abs
from numpy.fft import rfft, irfft, rfftfreq
from numpy.random import random
from pylab import subplot, plot, xlabel, ylabel, show


def main():
    """
    Settings
    """
    _FD = 1024  # sampling frequency 1/Td
    _TIME = 20  # sec
    _BORDER = 0.15  # граница среза от макс аплитуды

    _F_FIRST = 3
    _F_SECOND = 5
    _F_THIRD = 7

    _A_FIRST = 3
    _A_SECOND = 7
    _A_THIRD = 9

    def plot_spectrum(_signal: array, pos: int, fd: float, n: int):
        """
        Plot spectrum of signal (W0W)
        """
        frequency = rfftfreq(n, 1. / fd)

        _spectrum = rfft(_signal) / n   # fft computing and normalization

        subplot(pos).grid(True)  # plotting the spectrum
        plot(frequency, np_abs(_spectrum), 'r')
        xlabel('Freq (Hz)')
        ylabel('|Y(freq)|')

    """
    Круговые частоты для синусов
    """
    w_first = (2. * pi * _F_FIRST / _FD)
    w_second = (2. * pi * _F_SECOND / _FD)
    w_third = (2. * pi * _F_THIRD / _FD)
    """
    Вычисляем длинну массива и делаем временную шкалу
    """
    len_of_array = _TIME * _FD  # len of array
    t = arange(len_of_array)
    """
    Получаем три исходных синусойды
    """
    sig_first = _A_FIRST * sin(w_first * t)
    sig_second = _A_SECOND * sin(w_second * t)
    sig_third = _A_THIRD * sin(w_third * t)
    """
    Складываем синусойды в один сигнал и делаем случайный шум
    """
    signal = sig_first + sig_second + sig_third
    noise = (random(t.shape) - 0.5) * random(t.shape) * 50
    """
    Графики
    """
    t = t / _FD # 0 1 2 3 4 -> 0 dt 2dt

    subplot(231).grid(True)  # 241 - позиция в матрице, где 2 - колво строк, 4 - колво столбцовБ 1 - позиция
    plot(t, sig_third, "green")
    plot(t, sig_second, "yellow")
    plot(t, sig_first, "blue")
    plot(t, signal, "red")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal, 234, _FD, len_of_array)

    signal_with_noise = signal + noise

    subplot(232).grid(True)
    plot(t, signal_with_noise, "b")
    plot(t, signal, "r")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal_with_noise, 235, _FD, len_of_array)
    """
    Выдрали кусок из функции для спектра, соответственно - строим спектр 
    """
    frq = rfftfreq(len_of_array, 1. / _FD)

    spectrum = rfft(signal_with_noise) / len_of_array  # fft computing and normalization
    """
    Ищем максимальное значение в графике спектра, и берем _BORDER % от него в качестве границы,
    по которой будем отсекать частоты
    """
    border = amax(absolute(spectrum)) * _BORDER  # Режем шум по % от максимальной амплитуды
    spectrum_cut = spectrum.copy()  # Копируем, чтобы не изменять изначальный спектр
    spectrum_cut[absolute(spectrum) < border] = 0  # Все значения, которые ниже границу, зануляем

    subplot(236).grid(True)
    plot(frq, np_abs(spectrum_cut), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')

    signal_without_noise = irfft(spectrum_cut) * len_of_array  # Обратное фурье и нормировка

    subplot(233).grid(True)
    plot(t, signal, "b")
    plot(t, signal_without_noise, "orange")
    xlabel('Time')
    ylabel('Amplitude')

    show()


if __name__ == "__main__":
    main()