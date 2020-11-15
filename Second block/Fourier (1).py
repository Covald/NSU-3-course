from numpy.random import uniform
from pylab import *
from scipy import fft
from scipy import signal


def create_signal(n: array, fs: float) -> array:
    signal = sin(3 * n) + sin(7 * n) * 3 + sin(5 * n) * 5
    noise = (np.random.random(n.shape) - 0.5) * np.random.random(n.shape) * 10

    subplot(2, 3, 1)
    plot(n, signal, "r")
    xlabel('Time')
    ylabel('Amplitude')

    plot_spectrum(signal, fs, [2, 3, 4])

    subplot(2, 3, 2)
    signal_with_noise = signal + noise
    plot(n, signal_with_noise, "b")
    plot(n, signal, "r")
    xlabel('Time')
    ylabel('Amplitude')

    return signal


def plot_spectrum(signal: array, fs: float, pos: list):
    n = len(signal)  # length of the signal
    k = arange(n)
    T = n / fs
    frq = k / T  # two sides frequency range
    frq = frq[range(int(n / 2))]  # one side frequency range

    Y = fft(signal) / n  # fft computing and normalization
    Y = Y[range(int(n / 2))]

    subplot(*pos)  # plotting the spectrum
    plot(frq, abs(Y), 'r')
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')


def clear_noise(sgn: array, t: array) -> array:
    N = 3  # Filter order
    Wn = 0.1  # Cutoff frequency
    B, A = signal.butter(N, Wn, output='ba')
    sgn = signal.filtfilt(B, A, sgn)
    subplot(2, 3, 3)
    plot(t, sgn, "r")
    xlabel('Time')
    ylabel('Amplitude')
    return sgn


def main():
    FS = 1024.0
    t = linspace(0, 2 * pi, 1024)

    sgn_with_noise = create_signal(t, FS)
    plot_spectrum(sgn_with_noise, FS, [2, 3, 5])
    sgn_without_noise = clear_noise(sgn_with_noise, t)
    plot_spectrum(sgn_without_noise, FS, [2, 3, 6])

    show()


if __name__ == "__main__":
    main()
