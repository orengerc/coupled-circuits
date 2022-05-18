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


def get_max_amplitude(path):
    df = pd.read_csv(path)
    return np.amax(df.iloc[:, 4].to_numpy())


def graph_amplitudes_vs_frequencies(x, y):
    g = Graph(x, y)
    g.set_labels("Maximum Amplitude vs. Frequency", "Frequency [KHz]", "Max Amplitude [V]")
    g.set_errors(np.array(x) / 500, np.array(y) / 100)
    g.plot_with_fit_and_errors(Equations.amplitude_vs_frequency)
    print(g.get_fit_parameters())


def analyze_week1():
    """
    Analyzes the results of week1.
    :return: Nothing
    """
    directory = "data\\week1"
    freq, amp = [], []
    for filename in os.listdir(directory):
        freq.append(float((os.path.splitext(filename)[0])[:-4]))
        amp.append(get_max_amplitude(os.path.join(directory, filename)))
    graph_amplitudes_vs_frequencies(freq, amp)


if __name__ == '__main__':
    analyze_week1()
