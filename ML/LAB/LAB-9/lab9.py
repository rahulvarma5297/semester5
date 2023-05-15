# 0. Linear regression can be used to create a linear classifier. For doing binary (2 class classification) classification we can say that value of one class is -1 and that for the other is +1 and learn the linear regression.  For a 2D problem, let the solution be y = w0+w1x1+w2x2.
# Now, w0+w1x1+w2x2  = 0 is the discriminant. And w0+w1x1+w2x2  < 0 we say class is -1, otherwise we say the class is +1.
# 1. Create a 2D data of size 100, where 50 belongs to class -1 and 50 belongs to class +1.    Both these are drawn from Gaussians. Class -1 is drawn from Gaussing of mean (0,0) and covariance I (identity matrix of size 2x2). For class +1, mean is (4,5) and covariance is I.
# 2. In a similar way create test set  of size 50.
# 3. Build the linear classifier.
# 4. Show the results along with test error.
# 5. Draw the classifier in the 2D space along with training points. Points of different classes can be coloured differently.

import numpy as np
import matplotlib.pyplot as plt
import random
import math
import sys
import pdb

def generate_data(n):
    # Generate data of size n, where n/2 belongs to class -1 and n/2 belongs to class +1.
    # Both these are drawn from Gaussians. Class -1 is drawn from Gaussing of mean (0,0) and covariance I (identity matrix of size 2x2). For class +1, mean is
    # (4,5) and covariance is I.
    # Input:
    # n: number of data points
    # Output:
    # X: data matrix of size n x 3. First column is all ones, second and third columns are the features.
    # Y: labels of size n x 1. -1 or +1
    # Hint: Use np.random.multivariate_normal to generate data from a Gaussian.
    # Hint: Use np.concatenate to concatenate two matrices.
    # YOUR CODE HERE
    #raise NotImplementedError
    X = np.zeros((n,3))
    Y = np.zeros((n,1))
    X[:,0] = 1
    X[:n/2,1:3] = np.random.multivariate_normal([0,0],np.eye(2),n/2)
    X[n/2:,1:3] = np.random.multivariate_normal([4,5],np.eye(2),n/2)
    Y[:n/2] = -1
    Y[n/2:] = 1
    return X,Y

def generate_test_data(n):
    # Generate test data of size n, where n/2 belongs to class -1 and n/2 belongs to class +1.
    # Both these are drawn from Gaussians. Class -1 is drawn from Gaussing of mean (0,0) and covariance I (identity matrix of size 2x2). For class +1, mean is
    # (4,5) and covariance is I.
    # Input:
    # n: number of data points
    # Output:
    # X: data matrix of size n x 3. First column is all ones, second and third columns are the features.
    # Y: labels of size n x 1. -1 or +1
    # Hint: Use np.random.multivariate_normal to generate data from a Gaussian.
    # Hint: Use np.concatenate to concatenate two matrices.
    # YOUR CODE HERE
    #raise NotImplementedError
    X = np.zeros((n,3))
    Y = np.zeros((n,1))
    X[:,0] = 1
    X[:n/2,1:3] = np.random.multivariate_normal([0,0],np.eye(2),n/2)
    X[n/2:,1:3] = np.random.multivariate_normal([4,5],np.eye(2),n/2)
    Y[:n/2] = -1
    Y[n/2:] = 1
    return X,Y

def linear_regression(X,Y):
    # Compute the linear regression solution.
    # Input:
    # X: data matrix of size n x 3. First column is all ones, second and third columns are the features.
    # Y: labels of size n x 1. -1 or +1
    # Output:
    # w: weight vector of size 3 x 1.
    # Hint: Use np.linalg.solve to solve a linear system.
    # YOUR CODE HERE
    #raise NotImplementedError
    w = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,Y))
    return w

def test_error_linear(X,Y,w):
    # Compute the test error of the linear regression solution.
    # Input:
    # X: data matrix of size n x 3. First column is all ones, second and third columns are the features.
    # Y: labels of size n x 1. -1 or +1
    # w: weight vector of size 3 x 1.
    # Output:
    # error: test error
    # YOUR CODE HERE
    #raise NotImplementedError
    error = np.sum(np.sign(np.dot(X,w))!=Y)/float(len(Y))
    return error

def plot_data(X,Y,w):
    # Plot the data points along with the linear classifier.
    # Input:
    # X: data matrix of size n x 3. First column is all ones, second and third columns are the features.
    # Y: labels of size n x 1. -1 or +1
    # w: weight vector of size 3 x 1.
    # YOUR CODE HERE
    #raise NotImplementedError
    plt.scatter(X[:50,1],X[:50,2],c='r')
    plt.scatter(X[50:,1],X[50:,2],c='b')
    x = np.linspace(-5,10,100)
    y = -(w[0]+w[1]*x)/w[2]
    plt.plot(x,y)
    plt.show()

def main():
    # Main script
    # 1. Create a 2D data of size 100, where 50 belongs to class -1 and 50 belongs to class +1.    Both these are drawn from Gaussians. Class -1 is drawn from Gaussing of mean (0,0) and covariance I (identity matrix of size 2x2). For class +1, mean is
    # (4,5) and covariance is I.
    # 2. In a similar way create test set  of size 50.
    # 3. Build the linear classifier.
    # 4. Show the results along with test error.
    # 5. Draw the classifier in the 2D space along with training points. Points of different classes can be coloured differently.
    # YOUR CODE HERE
    #raise NotImplementedError
    X,Y = generate_data(100)
    X_test,Y_test = generate_test_data(50)
    w = linear_regression(X,Y)
    error = test_error_linear(X_test,Y_test,w)
    print (error)
    plot_data(X,Y,w)

if __name__ == '__main__':
    main()