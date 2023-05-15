from operator import imod
from random import seed
from random import randrange
from csv import reader
from math import sqrt
import random
import csv
 
# Loading a CSV file and collecting the data
def csv_loading(f_name):
	data = list()
	with open(f_name, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			data.append(row)
	return data

def load_data(filename, splitting, training_set=[] , testing_example=[]):
	with open(filename, 'rt') as temp:
		li = csv.reader(temp)
		original_data = list (li)
		for i in range(len(original_data)-1):
			for j in range(4):
				original_data[i][j] = float(original_data[i][j])
			if random.random() < splitting:
				training_set.append(original_data[i])
			else:
				testing_example.append(original_data[i])

# String to float
def str_float(d_set, col):
	for row in d_set:
		row[col] = float(row[col].strip())
 
# String to int
def str_int(d_set, col):
	val = [row[col] for row in d_set]
	unq_val = set(val)
	t = dict()
	for i, j in enumerate(unq_val):
		t[j] = i
	for row in d_set:
		row[col] = t[row[col]]
	return t
 
 
# Split a dataset into k folds
def cross_val_split(d_set, num_cros_val):
	d_set_spilt = list()
	d_set_copy = list(d_set)
	fold_size = int(len(d_set) / num_cros_val)
	for _ in range(num_cros_val):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(d_set_copy))
			fold.append(d_set_copy.pop(index))
		d_set_spilt.append(fold)
	return d_set_spilt
 
# Calculate accuracy percentage
def accuracy_measure(a, p):
	c = 0
	for i in range(len(a)):
		if a[i] == p[i]:
			c += 1
	return c / float(len(a)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def main_func(d_set, algo, num_cros_val, *args):
	folds = cross_val_split(d_set, num_cros_val)
	s = list()
	for x in folds:
		train_set = list(folds)
		train_set.remove(x)
		train_set = sum(train_set, [])
		test_set = list()
		for row in x:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		pred = algo(train_set, test_set, *args)
		act = [row[-1] for row in x]
		a = accuracy_measure(act, pred)
		s.append(a)
	return s
 
# Distance Between two given points
def euclidean_distance(p1, p2):
	d = 0.0
	for x in range(len(p1)-1):
		d += (p1[x] - p2[x])**2
	return sqrt(d)
 
# near similar neighbours
def get_neigh(training_set, test_row, num_neighbors):
	d = list()
	for train_row in training_set:
		dist = euclidean_distance(test_row, train_row)
		d.append((train_row, dist))
	d.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(d[i][0])
	return neighbors
 
# Make a prediction with neighbors
def predict_classification(training_set, test_row, num_neighbors):
	neighbors = get_neigh(training_set, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 
# KNN algo for finding nearest neighobour
def near_neigh(training_set, testing_set, num_neighbors):
	p = list()
	for row in testing_set:
		o = predict_classification(training_set, row, num_neighbors)
		p.append(o)
	return(p)
 
# Testing for the KNN on the given iris dataset
# 1. Implement 5-Fold Cross Validation (5M) 
seed(1)
t_set=[] # For storing 120 data
t_example=[] # For Storing remaning 30 data
split = 0.8 # 
f_name = 'iris.csv'
dataset = csv_loading(f_name)
for i in range(len(dataset[0])-1):
	str_float(dataset, i)
str_int(dataset, len(dataset[0])-1)

# 2. Perform 5-Fold cross validation on KNN Classifier (which you have implemented on Lab1) for IRIS Dataset 
num_cros_val = int(input("Enter Value for K in K-Fold cross validation (ie. K = 5) : "))
if(num_cros_val < 2):
	num_cros_val = 2
# num_cros_val = 5 (Value for 5-Fold Cross Validation)

ans = []
for x in range(1, 11):
    num_neighbors = x
    scores = main_func(dataset, near_neigh, num_cros_val, num_neighbors)
    temp = (scores[0] + scores[1]) / 2
    ans.append(temp)
    print('Accuracy for', x ,'- KNN: %s' % temp,'%')

print()
# 4. Report the validation accuracy and test accuracy of the classifier.  
# {Note, validation accuracy will have standard deviation, report that too}(1M)
total = 0.0
for x in range(0, len(ans)):
    total = total + ans[x]
print('Mean Accuracy: %.3f%%' % (total/float(len(ans))))

mean = sum(ans) / len(ans)
variance = sum([((x - mean) ** 2) for x in ans]) / len(ans)
res = variance ** 0.5
print('Variance : %.3f%%' % variance)
print('Standard Deviation : %.3f%%' %res)

# 3. Find out the best K value for the KNN Classifier using step-2. (2M)
best = 0
ma = 0
for i in range(0,10):
    if ma < ans[i]:
        ma = ans[i]
        best = i+1
print('The Best Value of K is',best)
print()
