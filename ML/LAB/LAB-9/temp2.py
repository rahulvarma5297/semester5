import numpy as np
import matplotlib.pyplot as plt
import random
import math


# Hypothesis function

def hypothesis_function(theta, x):
    return np.round(np.dot(theta, x))


# Cost function

def cost_function(theta, x, y):
    t = len(y)
    total_cost = 0
    for i in range(t):
        total_cost += (hypothesis_function(theta, x[i])-y[i])**2
    return total_cost/(2*t)


# Gradient descent function

def gradient_descent(theta, x, y, alpha, num_of_iterations):
    t = len(y)
    cost_dup = np.zeros(num_of_iterations)
    theta_dup = np.zeros((num_of_iterations, 3))
    for i in range(num_of_iterations):
        # Formula given in the slides
        theta = theta - (1/t)*alpha*(np.dot(x.T, (np.dot(x, theta)-y)))
        theta_dup[i, :] = theta.T
        cost_dup[i] = cost_function(theta, x, y)
    return theta, cost_dup, theta_dup

#Prediction function

def predict(theta, x):
    return hypothesis_function(theta, x)

# Defining the accuracy function


def accuracy(theta, x, y):
    t = len(y)
    correct = 0
    for i in range(t):
        if predict(theta, x[i]) == y[i]:
            correct += 1
    return correct/t

# Defining the plotting function


def plot_data(x, y):
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.show()

# Defining the plotting function


def plot_decision_boundary(theta, x, y):
    plt.scatter(x[:, 0], x[:, 1], c=y)
    x1 = np.linspace(-2, 6, 100)
    x2 = -(theta[0]+theta[1]*x1)/theta[2]
    plt.plot(x1, x2)
    plt.show()

# Defining the plotting function


def plot_cost_history(cost_dup):
    plt.plot(cost_dup)
    plt.show()

# Defining the plotting function


def plot_theta_history(theta_dup):
    plt.plot(theta_dup[:, 0], label='theta0')
    plt.plot(theta_dup[:, 1], label='theta1')
    plt.plot(theta_dup[:, 2], label='theta2')
    plt.legend()
    plt.show()

# Error function of test set


def error(theta, x, y):
    t = len(y)
    error = 0
    for i in range(t):
        error += (hypothesis_function(theta, x[i])-y[i])**2
    return error/(2*t)

# Defining the main function


# Train Data:
# Generating the train data for Class - 1
mean1 = np.array([0, 0])
cov1 = np.array([[1, 0], [0, 1]])
x1 = np.random.multivariate_normal(mean1, cov1, 50)
y1 = np.ones(50)*-1
x1_y1 = np.column_stack((x1, y1))

# Generating the train data for Class - 1
mean2 = np.array([4, 5])
cov2 = np.array([[1, 0], [0, 1]])
x2 = np.random.multivariate_normal(mean2, cov2, 50)
y2 = np.ones(50)
x2_y2 = np.column_stack((x2, y2))
# Combing into a single data set for testing
train_data = np.concatenate((x1_y1, x2_y2), axis=0)


# Test Data:
# Generating the Test Data for Class - 1
mean1 = np.array([0, 0])
cov1 = np.array([[1, 0], [0, 1]])
x1_test = np.random.multivariate_normal(mean1, cov1, 25)
y1_test = np.ones(25)*-1
test_class1 = np.column_stack((x1_test, y1_test))

# Generating the Test Data for Class - 1
mean2 = np.array([4, 5])
cov2 = np.array([[1, 0], [0, 1]])
x2_test = np.random.multivariate_normal(mean2, cov2, 25)
y2_test = np.ones(25)
test_class2 = np.column_stack((x2_test, y2_test))
# Combing the Test data into single data set
test_data = np.concatenate((test_class1, test_class2), axis=0)

# Implementing Linear Regression Using Gradient Descent

# Plotting the data
plot_data(train_data[:, :2], train_data[:, 2])
# Adding the bias term
x = np.c_[np.ones((len(train_data), 1)), train_data[:, :2]]
y = train_data[:, 2]
# Initializing the parameters
theta = np.zeros(3)
# Setting the learning rate
alpha = 0.01
# Setting the number of num_of_iterations
num_of_iterations = 1000
# Running the gradient descent algorithm
theta, cost_dup, theta_dup = gradient_descent(
    theta, x, y, alpha, num_of_iterations)
# Plotting the cost history
# plot_cost_history(cost_dup)
# Plotting the theta history
# plot_theta_history(theta_dup)
# Plotting the decision boundary
plot_decision_boundary(theta, train_data[:, :2], train_data[:, 2])
# Calculating the accuracy
print('Accuracy for the training data is: ', accuracy(theta, x, y))
# Adding the bias term
x_test = np.c_[np.ones((len(test_data), 1)), test_data[:, :2]]
y_test = test_data[:, 2]
# Making predictions on test set
print('Accuracy for the test data is: ', accuracy(theta, x_test, y_test))

print("Error For the Data is: ", error(theta, x_test, y_test))
