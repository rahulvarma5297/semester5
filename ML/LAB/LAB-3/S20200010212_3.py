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
def euclidean_distance(p1, p2, power):
	d = 0.0
	for x in range(len(p1)-1):
		d += (abs(p1[x] - p2[x]))**power
	return d**(1/power)
 
# near similar neighbours
def get_neigh(training_set, test_row, num_neighbors, power):
	d = list()
	for train_row in training_set:
		dist = euclidean_distance(test_row, train_row, power)
		d.append((train_row, dist))
	d.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(d[i][0])
	return neighbors
 
# Make a prediction with neighbors
def predict_classification(training_set, test_row, num_neighbors, power):
	neighbors = get_neigh(training_set, test_row, num_neighbors, power)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 
# KNN algo for finding nearest neighobour
def near_neigh(training_set, testing_set, num_neighbors, power):
	p = list()
	for row in testing_set:
		o = predict_classification(training_set, row, num_neighbors, power)
		p.append(o)
	return(p)
 

seed(1)

f_name = 'pp_tra.dat'
t_name = 'pp_tes.dat'
dataset = csv_loading(f_name)
testset = csv_loading(t_name)
for i in range(len(dataset[0])-1):
	str_float(dataset, i)
str_int(dataset, len(dataset[0])-1)

for i in range(len(testset[0])-1):
	str_float(testset, i)
str_int(testset, len(testset[0])-1)


num_cros_val = 3 #(Value for 3-Fold Cross Validation)

ans = []
for x in range(1, 21):
    num_neighbors = x
    power = 2
    scores = main_func(dataset,testset, near_neigh, num_cros_val, num_neighbors, power)
    temp = (scores[0] + scores[1]) / 2
    ans.append(temp)
    print('Accuracy for', x ,'- KNN: %s' % temp,'%')

print()

best = 0
ma = 0
for i in range(0,20):
    if ma < ans[i]:
        ma = ans[i]
        best = i+1
print('The Best Value of K in KNN is: ',best)
print()


ans2 = []
for x in range(1, 5):
    num_neighbors = best
    power = x
    scores = main_func(dataset,testset, near_neigh, num_cros_val, num_neighbors, power)
    temp = (scores[0] + scores[1]) / 2
    ans2.append(temp)
    print('Accuracy for Minkowski metric (p) = ', x ,'is: %s ' % temp,'%')

best2 = 0
ma2 = 0
for i in range(0,4):
    if ma2 < ans2[i]:
        ma2 = ans2[i]
        best2 = i+1
print()
print('The Best Value of Minkowski metric (p) is: ',best2)
print()



