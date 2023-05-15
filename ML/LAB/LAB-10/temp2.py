import numpy as np
import matplotlib.pyplot as plt
import warnings
X = np.arange(60, 300, 1)
X = np.radians(X)

K = np.random.normal(0, 0.15, X.shape)
Y = np.sin(X) + K

X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

# Normalizing the X values using z-score
X = (X - np.mean(X)) / np.std(X)

warnings.filterwarnings('ignore')

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

# Implementing non-linear regression from scratch
# Using Gradient Descent

def non_linear_regression(X, Y, learning_rate, iterations, degree):
      # Initialize the parameters
      m = np.zeros((degree, 1))
      c = 0
      n = len(X)
      # Performing Gradient Descent
      for i in range(iterations):
            Y_pred = np.zeros((n, 1))
            for j in range(degree):
                  Y_pred += m[j] * (X ** (j + 1))
            Y_pred += c
            D_m = np.zeros((degree, 1))
            for j in range(degree):
                  D_m[j] = (-2 / n) * sum((X ** (j + 1)) * (Y - Y_pred))
            D_c = (-2 / n) * sum(Y - Y_pred)
            m = m - learning_rate * D_m
            c = c - learning_rate * D_c
      return m, c

# Implementing Lasso regression from scratch
# Using Gradient Descent

def lasso_regression(X, Y, learning_rate, iterations, degree, l):
      # Initialize the parameters
      m = np.zeros((degree, 1))
      c = 0
      n = len(X)
      # Performing Gradient Descent
      for i in range(iterations):
            Y_pred = np.zeros((n, 1))
            for j in range(degree):
                  Y_pred += m[j] * (X ** (j + 1))
            Y_pred += c
            D_m = np.zeros((degree, 1))
            for j in range(degree):
                  D_m[j] = (-2 / n) * sum((X ** (j + 1)) * (Y - Y_pred)) + l * np.sign(m[j])
            D_c = (-2 / n) * sum(Y - Y_pred)
            m = m - learning_rate * D_m
            c = c - learning_rate * D_c
      return m, c

# Implementing Ridge regression from scratch
# Using Gradient Descent

def ridge_regression(X, Y, learning_rate, iterations, degree, l):
      # Initialize the parameters
      m = np.zeros((degree, 1))
      c = 0
      n = len(X)
      # Performing Gradient Descent
      for i in range(iterations):
            Y_pred = np.zeros((n, 1))
            for j in range(degree):
                  Y_pred += m[j] * (X ** (j + 1))
            Y_pred += c
            D_m = np.zeros((degree, 1))
            for j in range(degree):
                  D_m[j] = (-2 / n) * sum((X ** (j + 1)) * (Y - Y_pred)) + l * m[j]
            D_c = (-2 / n) * sum(Y - Y_pred)
            m = m - learning_rate * D_m
            c = c - learning_rate * D_c
      return m, c

# Plot the created models for the power of 1, 3,6,9,12 and 15, and print the SSE, Coefficients for the plotted models.

def plot_model(X, Y, m, c, degree):
      Y_pred = np.zeros((len(X), 1))
      for i in range(degree):
            Y_pred += m[i] * (X ** (i + 1))
      Y_pred += c
      plt.plot(X, Y_pred, label = 'Degree = ' + str(degree))
      plt.scatter(X, Y)
      plt.legend()
      # plt.show()
      # print('SSE = ', np.sum((Y - Y_pred) ** 2))
      # print('Coefficients = ', m, c)

# Plot the Lasso (L1) and Ridge (L2) regression models for lambda values [1e-10,1e-8,1e-4,1e-2,1,10,20],
# and print the SSE, Coefficients for the plotted models.

def plot_regularized_model(X, Y, m, c, degree, l):
      Y_pred = np.zeros((len(X), 1))
      for i in range(degree):
            Y_pred += m[i] * (X ** (i + 1))
      Y_pred += c
      plt.plot(X, Y_pred, label = 'Degree = ' + str(degree) + ', Lambda = ' + str(l))
      plt.scatter(X, Y)
      plt.legend()
      # plt.show()
      # print('SSE = ', np.sum((Y - Y_pred) ** 2))
      # print('Coefficients = ', m, c)

# Plot the created models for the power of 1, 3,6,9,12 and 15, and print the SSE, Coefficients for the plotted models.

learning_rate = 0.001
iterations = 1000
for degree in [1, 3, 6, 9, 12, 15]:
      m, c = non_linear_regression(X, Y, learning_rate, iterations, degree)
      plot_model(X, Y, m, c, degree)

# Plot the Lasso (L1) and Ridge (L2) regression models for lambda values [1e-10,1e-8,1e-4,1e-2,1,10,20],
# and print the SSE, Coefficients for the plotted models.

learning_rate = 0.001
iterations = 1000
for degree in [1, 3, 6, 9, 12, 15]:
      for l in [1e-10, 1e-8, 1e-4, 1e-2, 1, 10, 20]:
            m, c = lasso_regression(X, Y, learning_rate, iterations, degree, l)
            plot_regularized_model(X, Y, m, c, degree, l)
            m, c = ridge_regression(X, Y, learning_rate, iterations, degree, l)
            plot_regularized_model(X, Y, m, c, degree, l)


      