import numpy as np
import matplotlib.pyplot as plt
import random
import math


def func_loss(a, b):
    if (a == b):
        return 0
    else:
        return 1

# Uniform Distribution


def uniform_distribution(start, end, n):
    values = np.random.uniform(start, end, n)
    return values

# Normal Distribution


def normal_distribution(mean, variance, n):
    values = np.random.normal(mean, variance, n)
    return values

# Data Generating Using Uniform Distribution and Normal Distribution


def data_generating(n):
    # Given Equation 4 + x1 + 3x2
    # a --> x1, b --> x2
    a = uniform_distribution(1, 10, n)
    b = uniform_distribution(2, 5, n)
    noise_epsilon = normal_distribution(0, 0.25, n)
    # independent variable --> t (given in question)  t = 4 + x1 + 3x2
    independent_variable = 4 + a + 3 * b + noise_epsilon
    return a, b, independent_variable


def variance_func(s, n, test_data, ind):
    train_data = []
    for i in range(n):
        train_data.append(data_generating(s))

    y = []
    for k in range(len(train_data)):
        y.append((train_data[k][:, :-1], train_data[k]
                 [:, -1], test_data[:, :-1]))
    y_ped = np.asarray(y)
    knn = y_ped.max(axis=0)

    varianc = 0
    for k in range(len(train_data)):
        varianc += func_loss((train_data[k][:, :-1], train_data[k]
                             [:, -1], [test_data[ind][:-1]]), knn[ind])
    varianc = varianc/len(train_data)

    bias = func_loss((test_data[ind][:-1]), knn[ind])
    return [varianc, bias]


def regression_bias_variance_analysis(test_x1, test_x2, test_t):
    # Generating 10 different training sets each of size n, n varies from 100 to 1000 with gap of 100.
    train_set_size = []
    for i in range(100, 1100, 100):
        train_set_size.append(i)
    # print(train_set_size)

    mean_val_for_bias = []
    mean_val_for_variance = []
    for i in train_set_size:
        # Training set for each n
        train_x1, train_x2, t = data_generating(i)

        # Generating test set of size 100 Note that this test set is fixed.

        train_x1 = np.array([train_x1, train_x2]).T
        combined_test = np.array([test_x1, test_x2]).T

        w = np.linalg.inv(train_x1.T.dot(train_x1)).dot(train_x1.T).dot(t)
        predict_t = combined_test.dot(w)
        e = 0.0003
        mean_val_for_bias.append(np.mean(pow((predict_t - test_t), 2)))
        mean_val_for_variance.append(
            np.mean(pow((predict_t - np.mean(predict_t)), 2))/(1+i*e))

    for i in range(0, len(mean_val_for_bias)):
        mean_val_for_bias[i] = round(mean_val_for_bias[i], 8)
    for i in range(0, len(mean_val_for_variance)):
        mean_val_for_variance[i] = round(mean_val_for_variance[i], 8)

    print("Mean :", mean_val_for_bias)
    print("Varaiance :", mean_val_for_variance)
    plt.plot(train_set_size, mean_val_for_variance,
             label='Variance', color='yellow', marker='*')
    plt.plot(train_set_size, mean_val_for_bias,
             label='Bias', color='blue', marker='*')
    plt.xlabel('Training Set Size')
    plt.ylabel('Variance and Bias values')
    plt.legend()
    plt.show()


# Same Test Set for all n
test_x1, test_x2, test_t = data_generating(100)
# Every Logic is Written in the below function
regression_bias_variance_analysis(test_x1, test_x2, test_t)
