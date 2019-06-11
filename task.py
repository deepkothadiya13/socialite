import numpy as np
import pandas as pd
import cue
txt =open ("C:\\Users\\karyan\\PycharmProjects\\tens\\data_set_IVa_aa_cnt.txt","r")
data = txt.read()
new_items = []
for item in data:
    new_items.extend(item.split())
frequency = []
for i in range(len(new_items)):
    if 8 <= i <= 30:
        frequency.append(i)

from scipy import signal
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

for i in frequency:
    def sine_generator(fs, sinefreq, duration):
        T = duration
        nsamples = fs * T
        w = 2. * np.pi * sinefreq
        t_sine = np.linspace(0, T, nsamples, endpoint=False)
        y_sine = np.sin(w * t_sine)
        result = pd.DataFrame({
            'data' : y_sine} ,index=t_sine)
        return result

    def butter_highpass(cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

    def butter_highpass_filter(data, cutoff, fs, order=5):
        b, a = butter_highpass(cutoff, fs, order=order)
        y = signal.filtfilt(b, a, data)
        return y

    fps = 30
    sine_fq = 100 #Hz
    duration = 10 #seconds
    sine_30Hz = sine_generator(fps,sine_fq,duration)
    sine_fq = 1 #Hz
    duration = 10 #seconds
    sine_8Hz = sine_generator(fps,sine_fq,duration)

    sine = sine_30Hz + sine_8Hz

    filtered_sine = butter_highpass_filter(sine.data,10,fps)

    plt.figure(figsize=(20,10))
    plt.subplot(211)
    plt.plot(range(len(sine)),sine)
    plt.title('generated signal')
    plt.subplot(212)
    plt.plot(range(len(filtered_sine)),filtered_sine)
    plt.title('filtered signal')
    plt.show()

    def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a


    def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y


    def run():
        from scipy.signal import freqz

        # Sample rate and desired cutoff frequencies (in Hz).
        fs = i
        lowcut = 500.0
        highcut = filtered_sine

        # Plot the frequency response for a few different orders.
        plt.figure(1)
        plt.clf()
        for order in [3, 6, 9]:
            b, a = butter_bandpass(lowcut, highcut, fs, order=order)
            w, h = freqz(b, a, worN=2000)
            plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

        plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
                 '--', label='sqrt(0.5)')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Gain')
        plt.grid(True)
        plt.legend(loc='best')

        # Filter a noisy signal.
        T = 0.05
        nsamples = T * fs
        t = np.linspace(0, T, nsamples, endpoint=False)
        a = 0.02
        f0 = 600.0
        x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
        x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
        x += a * np.cos(2 * np.pi * f0 * t + .11)
        x += 0.03 * np.cos(2 * np.pi * 2000 * t)
        plt.figure(2)
        plt.clf()
        plt.plot(t, x, label='Noisy signal')

        y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
        plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
        plt.xlabel('time (seconds)')
        plt.hlines([-a, a], 0, T, linestyles='--')
        plt.grid(True)
        plt.axis('tight')
        plt.legend(loc='upper left')

        plt.show()


    run()

    cue.time(duration)

