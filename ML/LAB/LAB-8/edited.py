# 0. We assume that the correct relationship between the dependent and independent variables is t = 4+x1+3x2
# 1. Generate data where  x1 is uniformly distributed in (1,10); and x2 is also uniformly distributed in (2, 5).
# 2. Add noise epsilon to the target where epsilon is drawn from the normal distribution with 0 mean and 0.25 variance.
# 3. Generate 10 different training sets each of size n. Training set size n should be varied from 100 to 1000 examples (you can say n is 100, 200, ..., 1000) and do the linear regression.
# 4. Generate test set of size 100 do the bias variance analysis. Note that this test set is fixed.

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

# I am trying to implement a simple linear regression model using numpy. I am using the following code:
#
# import numpy as np
# import matplotlib.pyplot as plt
#
# def generate_data(n):
#     x = np.random.uniform(1, 10, n)
#     epsilon = np.random.normal(0, 0.25, n)
#     t = 4 + x + epsilon
#     return x, t

# def linear_regression(x, t):
#     x = np.array([x]).T
#     t = np.array([t]).T
#     w = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(t)
#     return w

# def plot_data(x, t, w):
#     plt.scatter(x, t)
#     plt.plot(x, w[0] + w[1]*x, 'r')
#     plt.show()

# if __name__ == '__main__':
#     x, t = generate_data(100)
#     w = linear_regression(x, t)
#     plot_data(x, t, w)

# I am getting the following error:
#
# Traceback (most recent call last):
#   File "linear_regression.py", line 29, in <module>
#     w = linear_regression(x, t)
#   File "linear_regression.py", line 19, in linear_regression
