from DataHandler import *
from Graph import *
from CurveFit import *
import Equations
from PIL import Image
from ImageHandler import *
import numpy as np
from scipy.stats import linregress
import os
import matplotlib.pyplot as plt


def get_max_amplitude(path, channel):
    df = pd.read_csv(path)
    if channel == 1:
        # f = df.iloc[:, 4].to_numpy()
        # t = df.iloc[:, 3].to_numpy()
        # res1 = np.amax(f)
        # res2 = CurveFit(t, f, fit_function=lambda x, a, phi: a * np.cos(x + phi)).get_fit_params()
        # print(res1, res2[0])
        # return res2[0]
        return np.amax(df.iloc[:, 4].to_numpy())
    elif channel == 2:
        # f = df.iloc[:, 10].to_numpy()
        # t = df.iloc[:, 9].to_numpy()
        # res1 = np.amax(f)
        # res2 = CurveFit(t, f, fit_function=lambda x, a, phi: a * np.cos(x + phi)).get_fit_params()
        # print(res1, res2[0])
        # return res2[0]
        return np.amax(df.iloc[:, 10].to_numpy())


def graph_amplitudes_vs_frequencies(x, y, channel=""):
    plt.scatter(x, y, s=11)
    plt.xlabel("Frequency [KHz]")
    plt.ylabel("Max Amplitude [V]")
    plt.title("Maximum Amplitude vs. Frequency")
    plt.grid()
    plt.show()
    # g = Graph(x, y)
    # g.set_labels(f"Maximum Amplitude vs. Frequency, {channel}", "Frequency [KHz]", "Max Amplitude [V]")
    # g.simple_plot()


def analyze_week1():
    """
    Analyzes the results of week1.
    :return: Nothing
    """
    directory = "data\\week1"
    freq, amp = [], []
    for filename in os.listdir(directory):
        freq.append(float((os.path.splitext(filename)[0])[:-4]))
        amp.append(get_max_amplitude(os.path.join(directory, filename), channel=1))
    graph_amplitudes_vs_frequencies(freq, amp)


def analyze_week2():
    """
    Analyzes the results of week2.
    :return: Nothing
    """
    directory = "data\\week2\\medidot"
    freq, amp1, amp2 = [], [], []
    freq = sorted([float((os.path.splitext(filename)[0])) for filename in os.listdir(directory)])
    for f in freq:
        path = os.path.join(directory, str(f) + '.csv')
        amp1.append(get_max_amplitude(path, channel=1))
        amp2.append(get_max_amplitude(path, channel=2))
    print(freq)
    print(amp1)
    print(amp2)
    graph_amplitudes_vs_frequencies(freq, amp1)
    graph_amplitudes_vs_frequencies(freq, amp2)


def analyze_week4():
    """
    Analyzes the results of week4.
    :return: Nothing
    """
    directory = "data\\week4"
    freq, amp1, amp2 = [], [], []
    freq = sorted([float((os.path.splitext(filename)[0])) for filename in os.listdir(directory)])
    for f in freq:
        path = os.path.join(directory, str(f) + '.csv')
        amp1.append(get_max_amplitude(path, channel=1))
        amp2.append(get_max_amplitude(path, channel=2))
    print(freq)
    print(amp1)
    print(amp2)
    graph_amplitudes_vs_frequencies(freq, amp1, "ch1")
    graph_amplitudes_vs_frequencies(freq, amp2, "ch2")


def analyze_angle():
    """
    Analyzes the results of week4.
    :return: Nothing
    """
    directory = "data\\angle"
    for filename in os.listdir(directory):
        freq = float(filename)
        angles, amp1, amp2 = [], [], []
        angles = range(0, 100, 10)
        for angle in angles:
            if freq == 4.95 and angle == 90:
                continue
            path = os.path.join(directory, str(str(freq) + "\\" + str(angle) + '.csv'))
            print(directory, str("\\" + str(freq) + "\\" + str(angle) + '.csv'))
            amp1.append(get_max_amplitude(path, channel=1))
            amp2.append(get_max_amplitude(path, channel=2))
        print(angles)
        print(amp1)
        print(amp2)
        graph_amplitudes_vs_frequencies(list(angles), amp1, f"{freq} ch1")
        graph_amplitudes_vs_frequencies(list(angles), amp2, f"{freq} ch2")


if __name__ == '__main__':
    # analyze_week1()
    analyze_week2()
    # analyze_week4()
    # analyze_angle()
