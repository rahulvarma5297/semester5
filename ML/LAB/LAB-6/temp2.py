# Bias Varaiance Analysis for 1-Nearest Neighbor
# mean covariance matrix

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)

def g(x):
    return f(x) + np.random.normal(0, 0.1, len(x))

def h(x, w):
    return np.polyval(w, x)

def generate_data(n):
    x = np.linspace(-np.pi, np.pi, n)
    y = g(x)
    return x, y

def generate_model(x, y, m):
    w = np.polyfit(x, y, m)
    return w

def generate_plot(x, y, w):
    plt.plot(x, y, 'o')
    plt.plot(x, h(x, w))
    plt.show()

def main():
    x, y = generate_data(10)
    w = generate_model(x, y, 9)
    generate_plot(x, y, w)

if __name__ == '__main__':
    main()

