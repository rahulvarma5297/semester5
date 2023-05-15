import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge, Lasso

# 1. Define input array X with angles from 60 deg to 300 deg converted in radians.
X = np.arange(60, 300, 1)
X = np.radians(X)

# 2. Compute Y as Y=Sin(X)+K
# where K is a random number generated from normal distribution with zero mean and 0.15 std dev.
K = np.random.normal(0, 0.15, X.shape)
Y = np.sin(X) + K

# 3. Create Linear Regression model, and different Non-Linear Regression models of 3,6,9,12 and 15th degree polynomial
# on data created in step-1 and step-2. (You may optimize the model for max. of 100 iterations using Gradient Descent)
# 4. Plot the created models for the power of 1, 3,6,9,12 and 15, and print the SSE, Coefficients for the plotted models.
degree = [1, 3, 6, 9, 12, 15]
for i in degree:
    poly = PolynomialFeatures(degree=i)
    X_poly = poly.fit_transform(X.reshape(-1, 1))
    regressor = LinearRegression()
    regressor.fit(X_poly, Y)
    y_pred = regressor.predict(X_poly)
    print("SSE for polynomial of degree", i,
          "is", mean_squared_error(Y, y_pred))
    print("Coefficients for polynomial of degree", i, "are", regressor.coef_)
    plt.scatter(X, Y, color='blue')
    plt.plot(X, y_pred, color='red')
    plt.title("Polynomial of degree " + str(i))
    plt.show()

# 5. Add the L1 and L2 regularization to the nonlinear regression model with 15th degree polynomial created in Step 3.
# (Optimize for Max. of 100 Iterations and lambda values [1e-10,1e-8,1e-4,1e-2,1,10,20])
# 6. Plot the Lasso (L1) and Ridge (L2) regression models for lambda values [1e-10,1e-8,1e-4,1e-2,1,10,20],
# and print the SSE, Coefficients for the plotted models.
poly = PolynomialFeatures(degree=15)
X_poly = poly.fit_transform(X.reshape(-1, 1))
lambda_values = [1e-10, 1e-8, 1e-4, 1e-2, 1, 10, 20]
for i in lambda_values:
    lasso_regressor = Lasso(alpha=i, max_iter=100)
    lasso_regressor.fit(X_poly, Y)
    y_pred = lasso_regressor.predict(X_poly)
    print("SSE for Lasso regression with lambda", i, "is",
          mean_squared_error(Y, y_pred))
    print("Coefficients for Lasso regression with lambda",
          i, "are", lasso_regressor.coef_)
    plt.scatter(X, Y, color='blue')
    plt.plot(X, y_pred, color='red')
    plt.title("Lasso regression with lambda " + str(i))
    plt.show()

for i in lambda_values:
    ridge_regressor = Ridge(alpha=i, max_iter=100)
    ridge_regressor.fit(X_poly, Y)
    y_pred = ridge_regressor.predict(X_poly)
    print("SSE for Ridge regression with lambda", i, "is",
          mean_squared_error(Y, y_pred))
    print("Coefficients for Ridge regression with lambda",
          i, "are", ridge_regressor.coef_)
    plt.scatter(X, Y, color='blue')
    plt.plot(X, y_pred, color='red')
    plt.title("Ridge regression with lambda " + str(i))
    plt.show()
