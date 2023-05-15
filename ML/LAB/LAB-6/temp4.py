from cProfile import label
from re import A
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Taken N = 10 as given in the pdf.
N=10

# Randomly generating data for class 0 and class 1.
x1,y1 = np.random.multivariate_normal(mean=[0,0], cov = [[1, 0], [0, 1]], size=N).T
x2,y2 = np.random.multivariate_normal(mean=[0,2], cov = [[1, 0], [0, 1]], size=N).T

# Generating data  It will return two matrices, 
# One for class 0 and another for class 1.  It will also return two vectors, one for each of the labels.
def generate_data(N):
  x_0 = np.array([np.random.multivariate_normal(mean=[a,b], cov = [[1, 0], [0, 1]], size=N) for (a,b) in zip(x2,y2)]).reshape(-1, 2)
  x_1 = np.array([np.random.multivariate_normal(mean=[a,b], cov = [[1, 0], [0, 1]], size=N) for (a,b) in zip(x1,y1)]).reshape(-1, 2)
  return x_0, x_1, [0]*x_0.shape[0], [1]*x_1.shape[0]

N = 10
a0,a1,b0,b1 = generate_data(N)
print(a0)
print(a1)
print(b0)
print(b1)
print(a0.shape)
print(a1.shape)

# Plotting the data  It will plot the data for class 0 in blue and the data for class 1 in red.

def plot_data(x_0, x_1):
    plt.title("Data Generated for class 0 and class 1")
    plt.scatter(x_0[:,0], x_0[:,1],alpha = 1, color="b", label='class 0')
    plt.scatter(x_1[:,0], x_1[:,1],alpha = 0.5, color="r", label='class 1')
    plt.legend()
    plt.show()

plot_data(a0,a1)


# KNN Classification:
def euclidean(a, b):
    d = a-b
    return np.sqrt(d.dot(d))

def distance_array(pt, x):
    return np.apply_along_axis(lambda z: euclidean(pt, z), 1, x)

def knn(k, pt, x, y):
    idxs = np.argsort(distance_array(pt, x))
    y_ones = sum(y[idxs][:k])
    if y_ones > k - y_ones:
        return 1
    return 0

def knn_predict(k, pts, x, y):
    return np.apply_along_axis(lambda p: knn(k, p, x, y), 1, pts)






