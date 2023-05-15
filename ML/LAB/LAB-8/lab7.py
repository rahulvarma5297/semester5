import random
import pandas as pd
import numpy as np

# 1. Divide the data into train-test split of 70:30.

df = pd.read_csv('House Price.csv', sep=',')
df.insert(0, 'x', 1)
# 70 : 30 split
ratio_for_split = int(np.ceil((0.7)*df.shape[0]))
# Training data
train_data_list = df.iloc[:ratio_for_split, :]
# Testing data
test_data_list = df.iloc[ratio_for_split:, :]

# 2. Implement the Linear Regression Model to Predict the Median House Price value in Lakhs.
# Coefficients
random.seed(1)
data = []
# 12 Features
for i in range(0, 12):
    data.append(random.uniform(0, 1))
data = np.array(data).T
# Learning rate
alpha = 0.000011
# Optimized the model for up to 100 iteration

# 3. Implement the Gradient Descent with SSE to Optimize the model for up to 100 iteration and predict the test set.
# Formula Used: θ = θ - α * partial derivative of(J(θ) / θ)
for i in range(0, 100):
    data = data - alpha *\
        (np.dot((np.dot(train_data_list.iloc[:, :-1], data) -
         train_data_list.iloc[:, -1]), train_data_list.iloc[:, :-1]) / train_data_list.shape[0])

#  4. Print the Coefficients of the Optimized model.
print('The Coefficients of the Optimized model for each features are:')
for x in data:
    print(round(x, 8))
print()

# Formula Used: J(θ) = 1/2m * Σ(hθ(x) - y)^2
SSE_for_train_data = np.sum(
    (np.dot(train_data_list.iloc[:, :-1], data) - train_data_list.iloc[:, -1])**2)
SSE_for_test_data = np.sum(
    (np.dot(test_data_list.iloc[:, :-1], data) - test_data_list.iloc[:, -1])**2)

MSE_for_train_data = SSE_for_train_data / train_data_list.shape[0]
MSE_for_test_data = SSE_for_test_data / test_data_list.shape[0]

R2_for_train_data = 1 - (SSE_for_train_data / np.sum(
    (train_data_list.iloc[:, -1] - np.mean(train_data_list.iloc[:, -1]))**2))
R2_for_test_data = 1 - (SSE_for_test_data / np.sum(
    (test_data_list.iloc[:, -1] - np.mean(test_data_list.iloc[:, -1]))**2))


# 5. Print the SSE, MSE and R2 scores for the Train and Test Sets.
print("SSE Score for Training Set:", round(SSE_for_train_data, 8))
print("SSE Score for Testing  Set:", round(SSE_for_test_data, 8))
print()
print("MSE Score for Training Set:", round(MSE_for_train_data, 8))
print("MSE Score for Testing  Set:", round(MSE_for_test_data, 8))
print()
print("R2 Score for Training Set:", round(R2_for_train_data, 8))
print("R2 Score for Testing  Set:", round(R2_for_test_data, 8))
