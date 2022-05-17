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
    print(path)


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


if __name__ == '__main__':
    analyze_week1()
