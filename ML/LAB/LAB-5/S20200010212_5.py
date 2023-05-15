from math import sqrt
from math import exp
from math import pi
from random import seed
from random import randrange
import random
from re import X
from csv import reader
from tkinter import E

# Loading File.
def csv_loading(f_name):
	store_data = list()
	with open(f_name, 'r') as file:
		temp = reader(file)
		for x in temp:
			if not X:
				continue
			store_data.append(x)
	return store_data


# Without Discretizing the data
def str_float(d_set, col):
	for x in d_set:
		x[col] = float(x[col].strip())

def str_int(d_set, col):
	val = [x[col] for x in d_set]
	unq_val = set(val)
	t = dict()
	for i, j in enumerate(unq_val):
		t[j] = i
	for x in d_set:
		x[col] = t[x[col]]
	return t

# For Discretizing the data
# In Naive bayes we get better accuracy when we discretize the value.
def discretize_str_float(d_set, col):
	for x in d_set:
		x[col] = float(x[col].strip())
		x[col] = round(x[col])

def discretize_str_int(d_set, col):
	val = [x[col] for x in d_set]
	unq_val = set(val)
	t = dict()
	for i, j in enumerate(unq_val):
		t[j] = i
	for x in d_set:
		x[col] = round(t[x[col]])
	return t

	
def split_dataset(d_set, split_ratio):
    train_size = int(len(d_set) * split_ratio)
    t_set = []
    duplica = list(d_set)
    while len(t_set) < train_size:
        index = random.randrange(len(duplica))
        t_set.append(duplica.pop(index))
    return [t_set, duplica]

# Split of 0.7 => (70%, 30%).

def cross_val_split(d_set, num_cros_val):
	split_dat = list()
	copy_dat = list(d_set)
	fold_size = int(len(d_set) / num_cros_val)
	for _ in range(num_cros_val):
		temp = list()
		while len(temp) < fold_size:
			index = randrange(len(copy_dat))
			temp.append(copy_dat.pop(index))
		split_dat.append(temp)
	return split_dat


# MEAN without using numpy.
def mean_of_num(num):
	return sum(num)/float(len(num))

# STANDARD DEVIATION with out using numpy.
def standard_dev_num(num):
	average = mean_of_num(num)
	var = sum([(x-average)**2 for x in num]) / float(len(num)-1)
	return sqrt(var)

# Accuracy Measure
def acc_measure(a, p):
	c = 0
	for i in range(len(a)):
		if a[i] == p[i]:
			c += 1
	return c / float(len(a)) * 100.0

# Splitting and seggregating data
def main_func(d_set, algo, num_cros_val, *args):
	folds = cross_val_split(d_set, num_cros_val)
	s = list()
	for x in folds:
		t_set = list(folds)
		t_set.remove(x)
		t_set = sum(t_set, [])
		test = list()
		for row in x:
			row_copy = list(row)
			test.append(row_copy)
			row_copy[-1] = None
		pred = algo(t_set, test, *args)
		act = [row[-1] for row in x]
		a = acc_measure(act, pred)
		s.append(a)
	return s

# Seperation by class (Naive Bayes)
def class_seperation(d_set):
	divide = dict()
	for x in range(len(d_set)):
		v = d_set[x]
		c_val = v[-1]
		if (c_val not in divide):
			divide[c_val] = list()
		divide[c_val].append(v)
	return divide


# Summarizing used in Naive Bayes
def summ(d_set):
	sumr = [(mean_of_num(column), standard_dev_num(column), len(column)) for column in zip(*d_set)]
	del(sumr[-1])
	return sumr

def summ_class(d_set):
	divide = class_seperation(d_set)
	sumr = dict()
	for x, y in divide.items():
		sumr[x] = summ(y)
	return sumr


# Calculating Posterior Probability.
# Gaussian Formula used in this function.
# (1/root(2*pi)*std_dev) * e^(-1/2 * ((present value - mean)/std_dev)^2)
def gaussian_distribution(x, mean_of_num, standard_dev_num):
	if standard_dev_num == 0:
		standard_dev_num = 0.00001
	e = exp(-((x-mean_of_num)**2 / (2 * standard_dev_num**2 )))
	return (1 / (sqrt(2 * pi) * standard_dev_num)) * e

def class_prob(summ, row):
	tot_r = sum([summ[x][0][2] for x in summ])
	p = dict()
	for x, y in summ.items():
		p[x] = summ[x][0][2]/float(tot_r)
		for i in range(len(y)):
			mean_of_num, standard_dev_num, _ = y[i]
			p[x] *= gaussian_distribution(row[i], mean_of_num, standard_dev_num)
	return p

def predict_class(summ, row):
	p = class_prob(summ, row)
	b_label, b = None, -1
	for x, y in p.items():
		if b_label is None or y > b:
			b = y
			b_label = x
	return b_label
split_ratio = 3
# Naive Bayes
def naive_bayes(tr, ts):
	summ = summ_class(tr)
	p = list()
	for x in ts:
		ot = predict_class(summ, x)
		p.append(ot)
	return(p)



# Discrete Data.
fd_name = 'heart.csv'
dataset_dis = csv_loading(fd_name)
for i in range(len(dataset_dis[0])-1):
	discretize_str_float(dataset_dis, i)
discretize_str_int(dataset_dis, len(dataset_dis[0])-1)	

# Main Code
splt_ratio = 0.7 # (70% - training, 30 - % test)
print("--------------------------------------------------------------------------------")
print()
print("For Heart Disease Dataset :")
# Discrete :
split_dataset(dataset_dis, splt_ratio)
scores_discretizing = main_func(dataset_dis, naive_bayes, split_ratio)
print('Usually Discretization gives more accuracy in naive bayes:')
print()
print('Accuracy with Discretization data: %.8f%%' % (sum(scores_discretizing)/float(len(scores_discretizing))))


# Without Discrete.
f_name = 'heart.csv'
dataset = csv_loading(f_name)
for i in range(len(dataset[0])-1):
	str_float(dataset, i)
str_int(dataset, len(dataset[0])-1)	

# Without Discrete : 
split_dataset(dataset_dis, splt_ratio)
scores_without_discrete = main_func(dataset, naive_bayes, split_ratio)
print('Accuracy without Discretization : %.8f%%' % (sum(scores_without_discrete)/float(len(scores_without_discrete))))
print()
print("--------------------------------------------------------------------------------")

