import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# 1. Define input array X with angles from 60 deg to 300 deg converted in radians.
X = np.arange(60, 300, 1)
X = np.radians(X)

# 2. Compute Y as Y=Sin(X)+K where K is a random number generated from normal distribution with zero mean and 0.15 std dev.
K = np.random.normal(0, 0.15, len(X))
Y = np.sin(X) + K

def normalize(X):
    mean = np.mean(X)
    std = np.std(X)
    X = (X - mean) / std
    return X

# Normalizing the data using Z-score
X_normal = normalize(X)

# 3.Create Linear Regression model, and different Non-Linear Regression models of 3,6,9,12 and 15th degree polynomial on data created in step-1 and step-2. (You may optimize the model for max. of 100 iterations using Gradient Descent)
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)
X_normal = X_normal.reshape(-1, 1)


# Implementing Linear regression from scratch
def linear_regression(X, Y, learning_rate, iterations):
    # Initialize the parameters
    m = 0
    c = 0
    n = len(X)
    # Performing Gradient Descent
    for i in range(iterations):
        Y_pred = m * X + c
        D_m = (-2 / n) * sum(X * (Y - Y_pred))
        D_c = (-2 / n) * sum(Y - Y_pred)
        m = m - learning_rate * D_m
        c = c - learning_rate * D_c
    return m, c

# Implementing Non-Linear regression from scratch using Gradient Descent algorithm
def non_linear_regression(X, Y, learning_rate, iterations, degree):
    # Initialize the parameters
    n = len(X)
    theta = np.zeros((degree + 1, 1))
    # Performing Gradient Descent
    for i in range(iterations):
        Y_pred = np.zeros((n, 1))
        for j in range(degree + 1):
            Y_pred += theta[j] * (X ** j)
        D_theta = np.zeros((degree + 1, 1))
        for j in range(degree + 1):
            D_theta[j] = (-2 / n) * sum((Y - Y_pred) * (X ** j))
        theta = theta - learning_rate * D_theta
    return theta

# Implementing Lasso regression from scratch
def lasso_regression(X, Y, learning_rate, iterations, degree, l):
    # Initialize the parameters
    n = len(X)
    theta = np.zeros((degree + 1, 1))
    # Performing Gradient Descent
    for i in range(iterations):
        Y_pred = np.zeros((n, 1))
        for j in range(degree + 1):
            Y_pred += theta[j] * (X ** j)
        D_theta = np.zeros((degree + 1, 1))
        for j in range(degree + 1):
            D_theta[j] = (-2 / n) * sum((Y - Y_pred) * (X ** j))
        theta = theta - learning_rate * D_theta
        for j in range(degree + 1):
            if theta[j] > 0:
                theta[j] -= l
            elif theta[j] < 0:
                theta[j] += l
            else:
                theta[j] = 0
    return theta

# Implementing Ridge regression from scratch
def ridge_regression(X, Y, learning_rate, iterations, degree, l):
    # Initialize the parameters
    n = len(X)
    theta = np.zeros((degree + 1, 1))
    # Performing Gradient Descent
    for i in range(iterations):
        Y_pred = np.zeros((n, 1))
        for j in range(degree + 1):
            Y_pred += theta[j] * (X ** j)
        D_theta = np.zeros((degree + 1, 1))
        for j in range(degree + 1):
            D_theta[j] = (-2 / n) * sum((Y - Y_pred) * (X ** j))
        theta = theta - learning_rate * D_theta
        for j in range(degree + 1):
            theta[j] -= l * theta[j]
    return theta

#  Plot the created models for the power of 1, 3,6,9,12 and 15, and print the SSE, Coefficients for the plotted models.
def plot_model(X, Y, learning_rate, iterations, degree):
    # Linear Regression
    if degree == 1:
        m, c = linear_regression(X, Y, learning_rate, iterations)
        Y_pred = m * X + c
        plt.plot(X, Y_pred, color='red', label='Linear Regression')
        print('SSE for Linear Regression: ', sum((Y - Y_pred) ** 2))
        print('Coefficients for Linear Regression: ', m, c)
    # Non-Linear Regression
    else:
        theta = non_linear_regression(X, Y, learning_rate, iterations, degree)
        Y_pred = np.zeros((len(X), 1))
        for i in range(degree + 1):
            Y_pred += theta[i] * (X ** i)
        plt.plot(X, Y_pred, label='Non-Linear Regression of degree ' + str(degree))
        print('SSE for Non-Linear Regression of degree ' + str(degree) + ': ', sum((Y - Y_pred) ** 2))
        print('Coefficients for Non-Linear Regression of degree ' + str(degree) + ': ', theta)

# Plot the Lasso (L1) and Ridge (L2) regression models for lambda values [1e-10,1e-8,1e-4,1e-2,1,10,20], and print the SSE, Coefficients for the plotted models.
def plot_regularized_model(X, Y, learning_rate, iterations, degree, l):
    # Lasso Regression
    if l == 1:
        theta = lasso_regression(X, Y, learning_rate, iterations, degree, l)
        Y_pred = np.zeros((len(X), 1))
        for i in range(degree + 1):
            Y_pred += theta[i] * (X ** i)
        plt.plot(X, Y_pred, label='Lasso Regression with lambda ' + str(l))
        print('SSE for Lasso Regression with lambda ' + str(l) + ': ', sum((Y - Y_pred) ** 2))
        # print('Coefficients for Lasso Regression with lambda ' + str(l) + ': ', theta)
    # Ridge Regression
    else:
        theta = ridge_regression(X, Y, learning_rate, iterations, degree, l)
        Y_pred = np.zeros((len(X), 1))
        for i in range(degree + 1):
            Y_pred += theta[i] * (X ** i)
        plt.plot(X, Y_pred, label='Ridge Regression with lambda ' + str(l))
        print('SSE for Ridge Regression with lambda ' + str(l) + ': ', sum((Y - Y_pred) ** 2))
        # print('Coefficients for Ridge Regression with lambda ' + str(l) + ': ', theta)

# Plot the data points
plt.scatter(X, Y, color='blue', label='Data Points')
# Plot the models
plot_model(X, Y, 0.01, 100, 1)

plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

plt.scatter(X, Y, color='blue', label='Data Points')
plot_model(X, Y, 0.0001, 100, 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


plt.scatter(X_normal, Y, color='blue', label='Data Points')
plot_model(X_normal, Y, 0.001, 100, 6)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

plt.scatter(X_normal, Y, color='blue', label='Data Points')
plot_model(X_normal, Y, 0.0001, 100, 9)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

plt.scatter(X_normal, Y, color='blue', label='Data Points')
plot_model(X_normal, Y, 0.00001, 100, 12)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()


plt.scatter(X_normal, Y, color='blue', label='Data Points')
plot_model(X_normal, Y, 0.0000001, 100, 15)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

plt.scatter(X, Y, color='blue', label='Data Points')

# 1e-10,1e-8,1e-4,1e-2,1,10,20

plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 1e-10)
plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 1e-8)
plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 1e-4)
plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 1e-2)
plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 1)
plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 10)
plot_regularized_model(X_normal, Y, 0.0000001, 100, 15, 20)

plt.xlabel('X_normal')
plt.ylabel('Y')
plt.legend()
plt.show()