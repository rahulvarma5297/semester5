import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
import math


def func_loss(a, b):
    if (a == b):
        return 0
    else:
        return 1


def prediction(X, Y, test):
    knn_sklearn = KNeighborsClassifier(n_neighbors=1)
    knn_sklearn.fit(X, Y)
    pred = knn_sklearn.predict(test)
    return pred


def data_generating(size):
  # Given in question.
    mean_class_1 = [0, 0]
    cov_class_1 = [[1, 0], [0, 1]]
    mean_class_2 = [0, 2]
    cov_class_2 = [[1, 0], [0, 1]]

    class_1 = np.random.multivariate_normal(mean_class_1, cov_class_1, int(size/2))
    a = np.zeros((int(size/2), 1))
    class_2 = np.random.multivariate_normal(mean_class_2, cov_class_2, int(size/2))
    b = np.ones((int(size/2), 1))

    x = np.concatenate((class_1, a), axis=1)
    y = np.concatenate((class_2, b), axis=1)
    data = np.concatenate((x, y), axis=0)
    return data


def bayes_classifier(t):
    mean_class_1 = [0, 0]
    cov_class_1 = [[1, 0], [0, 1]]
    mean_class_2 = [0, 2]
    cov_class_2 = [[1, 0], [0, 1]]
    classifier_1 = (1/math.sqrt(cov_class_1[0][0]*cov_class_1[1][1])) * math.exp((-1/2) * (
        (t[0]-mean_class_1[0])**2 / cov_class_1[0][0]) + ((t[1]-mean_class_1[1])**2 / cov_class_1[1][1]))
    classifier_2 = (1/math.sqrt(cov_class_2[0][0]*cov_class_2[1][1])) * math.exp((-1/2) * (
        (t[0]-mean_class_2[0])**2 / cov_class_2[0][0]) + ((t[1]-mean_class_2[1])**2 / cov_class_2[1][1]))
    if classifier_1 > classifier_2:
        return 0
    else:
        return 1


bayes_classifier([1, 5])


def variance_func(s, n, test_data, ind):
    train_data = []
    for i in range(n):
        train_data.append(data_generating(s))

    y = []
    for k in range(len(train_data)):
        y.append(prediction(
            train_data[k][:, :-1], train_data[k][:, -1], test_data[:, :-1]))
    y_ped = np.asarray(y)
    knn = y_ped.max(axis=0)

    varianc = 0
    for k in range(len(train_data)):
        varianc += func_loss(prediction(train_data[k][:, :-1], train_data[k]
                                    [:, -1], [test_data[ind][:-1]]), knn[ind])
    varianc = varianc/len(train_data)

    bias = func_loss(bayes_classifier(test_data[ind][:-1]), knn[ind])

    return [varianc, bias]


test_data = data_generating(100)
Varaince_values = []
Bias_values = []
data_points = []

for n in range(100, 1100, 100):
    a = 0
    b = 0

    for i in range(len(test_data)):
        x, y = variance_func(n, 10, test_data, i)
        a += x
        b += y
    Varaince_values.append(a/len(test_data))
    Bias_values.append(b/len(test_data))
    data_points.append(n)
print(Varaince_values)
print(Bias_values)
plt.plot(data_points, Varaince_values, color='blue', marker = '*')
plt.plot(data_points, Bias_values, color='yellow', marker = '*')
plt.legend(['Variance', 'Bias'])
plt.xlabel('Number of data points (n value)')
plt.ylabel('Variance and Bias values')
plt.show()
