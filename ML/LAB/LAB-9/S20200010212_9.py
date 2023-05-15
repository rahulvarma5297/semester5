import numpy as np
import matplotlib.pyplot as plt
import random
import math

# Hypothesis function


def hypothesis_function(theta, x):
    if (np.dot(theta, x) >= 0):
        return 1
    else:
        return -1

# Cost function


def cost_function(theta, x, y):
    t = len(y)
    total_cost = 0
    for i in range(t):
        total_cost += (hypothesis_function(theta, x[i])-y[i])**2
    return total_cost/(2*t)

# Defining the gradient descent function


def gradient_descent(theta, x, y, alpha, num_of_iterations):
    t = len(y)
    dup_cost = np.zeros(num_of_iterations)
    dup_history = np.zeros((num_of_iterations, 3))
    for i in range(num_of_iterations):
        # Formula given in the slides for mean squared error
        theta = theta - (1/t)*alpha*(np.dot(x.T, (np.dot(x, theta)-y)))
        dup_history[i, :] = theta.T
        dup_cost[i] = cost_function(theta, x, y)
    return theta, dup_cost, dup_history

# Defining the prediction function


def predict(theta, x):
    return hypothesis_function(theta, x)

# Defining Error function


def error(theta, x, y):
    t = len(y)
    e = 0
    for i in range(t):
        e += (hypothesis_function(theta, x[i])-y[i])**2
    return e/(2*t)

# Defining the accuracy function


def accuracy(theta, x, y):
    t = len(y)
    yes = 0
    for i in range(t):
        if predict(theta, x[i]) == y[i]:
            yes += 1
    return (yes/t)*100

# Plotting function for data


def plot_data(x, y):
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()

# Plotting function for the cost function


def plot_cost_history(cost_dup):
    plt.plot(cost_dup)
    plt.show()

# Plotting function for theta history


def plot_theta_history(costtheta_dup):
    plt.plot(costtheta_dup[:, 0], label='theta0')
    plt.plot(costtheta_dup[:, 1], label='theta1')
    plt.plot(costtheta_dup[:, 2], label='theta2')
    plt.legend()
    plt.show()

# Defining the plotting function for the decision boundary


def plot_decision_boundary(theta, x, y):
    plt.scatter(x[:, 0], x[:, 1], c=y)
    x1 = np.linspace(-2, 6, 100)
    x2 = -(theta[0]+theta[1]*x1)/theta[2]
    plt.plot(x1, x2)
    plt.show()


# Train Data for Class +1
mean1 = np.array([0, 0])
cov1 = np.array([[1, 0], [0, 1]])
mean2 = np.array([4, 5])
cov2 = np.array([[1, 0], [0, 1]])

x1 = np.random.multivariate_normal(mean1, cov1, 50)
y1 = np.ones(50)*-1
trainx1y1 = np.column_stack((x1, y1))

# Train Data for Class -1
x2 = np.random.multivariate_normal(mean2, cov2, 50)
y2 = np.ones(50)
trainx2y2 = np.column_stack((x2, y2))
train_data = np.concatenate((trainx1y1, trainx2y2), axis=0)

# Test Data for Class +1
x1_test = np.random.multivariate_normal(mean1, cov1, 25)
y1_test = np.ones(25)*-1
test_class1 = np.column_stack((x1_test, y1_test))

# Test Data for Class -1
x2_test = np.random.multivariate_normal(mean2, cov2, 25)
y2_test = np.ones(25)
test_class2 = np.column_stack((x2_test, y2_test))

# Combing Test data
test_data = np.concatenate((test_class1, test_class2), axis=0)

# Plotting the data
plot_data(train_data[:, :2], train_data[:, 2])
x = np.c_[np.ones((len(train_data), 1)), train_data[:, :2]]
y = train_data[:, 2]
theta = np.zeros(3)
# Learning rate
alpha = 0.01
# Number of Iterations
iterations = 1000

# Running the gradient descent algorithm
theta, cost_dup, costtheta_dup = gradient_descent(
    theta, x, y, alpha, iterations)

plot_decision_boundary(theta, train_data[:, :2], train_data[:, 2])

x_test = np.c_[np.ones((len(test_data), 1)), test_data[:, :2]]
y_test = test_data[:, 2]

# Printing the error on the test set
print('Error on test set is: ', error(theta, x_test, y_test))

# Accuracy on the train set
print('Accuracy for the Training data is: ', accuracy(theta, x, y))

# Accuracy on the Test set
print('Accuracy for the Test data is: ', accuracy(theta, x_test, y_test))
