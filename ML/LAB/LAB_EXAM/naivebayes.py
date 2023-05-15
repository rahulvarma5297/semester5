# naive bayes classifier from scratch

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

# Create a function to calculate the Euclidean distance
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

# Create a function to calculate the KNN
def knn(X, y, test_point, k=5):
    # Create a list for distances and targets
    distances = []
    targets = []

    for i in range(len(X)):
        # Calculate the distance
        distance = euclidean_distance(test_point, X[i])
        # Add it to list of distances
        distances.append([distance, i])

    # Sort the list
    distances = sorted(distances)

    # Make a list of the k neighbors' targets
    for i in range(k):
        index = distances[i][1]
        targets.append(y[index])

    # Return most common target
    return np.bincount(targets).argmax()

# Make predictions
predictions = []
for i in range(len(X_test)):
    predictions.append(knn(X_train, y_train, X_test[i], k=5))

# Calculate the accuracy
accuracy = np.sum(predictions == y_test) / len(y_test)
print("Accuracy:", accuracy)

# Plot the results
plt.figure(figsize=(12, 8))
plt.scatter(X_test[:, 0], X_test[:, 1], c=predictions, cmap='viridis')
plt.show()


