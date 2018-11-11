import numpy as np
import matplotlib.pyplot as plt

def rand_bytes(length):
    np.random.seed(0)
    return np.fromstring(np.random.bytes(length), dtype='uint8')

def plot_bytes(bytes):
    plt.plot(bytes)
    plt.show()
