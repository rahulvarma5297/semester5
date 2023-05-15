import numpy as np
import matplotlib.pyplot as plt
import random


def generate_data(n):
    x1 = np.random.uniform(1, 10, n)
    x2 = np.random.uniform(2, 5, n)
    epsilon = np.random.normal(0, 0.25, n)
    t = 4 + x1 + 3*x2 + epsilon
    return x1, x2, t


def bias_variance_analysis():
    n = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    bias = []
    variance = []
    for i in n:
        x1, x2, t = generate_data(i)
        x1_test, x2_test, t_test = generate_data(i)
        x1_train = np.array([x1, x2]).T
        x1_test = np.array([x1_test, x2_test]).T
        w = np.linalg.inv(x1_train.T.dot(x1_train)).dot(x1_train.T).dot(t)
        t_predict = x1_test.dot(w)
        bias.append(np.mean((t_predict - t_test)**2))
        variance.append(np.mean((t_predict - np.mean(t_predict))**2))
    plt.plot(n, variance, label='variance')
    plt.plot(n, bias, label='bias')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    bias_variance_analysis()



