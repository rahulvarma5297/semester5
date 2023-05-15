import csv
import random
import math
import operator 


# Retriving the data from the iris.data file and storing in the list (120 -> training examles and 30 -> test examples)
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

# calulating ecludiean distance between the two points
def euclidean_distance(p1, p2, length):
	d = 0
	for i in range(length):
		d += pow((p1[i] - p2[i]), 2)
	return math.sqrt(d)

# choosing subset of points with the smallest distance which are near
def closest_neighbors(training_set, test_instance, k):
	d = []
	length = len(test_instance)-1
	for i in range(len(training_set)):
		dist = euclidean_distance(test_instance, training_set[i], length)
		d.append((training_set[i], dist))
	d.sort(key=operator.itemgetter(1))
	neighbors = []
	for i in range(k):
		neighbors.append(d[i][0])
	return neighbors

# predict the output for given input
def get_votes(neighbors):
	v = {}
	for i in range(len(neighbors)):
		response = neighbors[i][-1]
		if response in v:
			v[response] += 1
		else:
			v[response] = 1
	sortedVotes = sorted(v.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

# calculate accuracy of the code
def get_accuracy(testing_example, predictions):
	c = 0
	for i in range(len(testing_example)):
		if testing_example[i][-1] in predictions[i]: 
			c+=1			
	return (c/float(len(testing_example))*100) 


# preparing data
training_set=[] # For storing 120 data
testing_example=[] # For Storing remaning 30 data
splitting = 0.8 # 
load_data('iris.data', splitting, training_set, testing_example)
print('According to spitting the data: ')
print ('Training Data: ' + repr(len(training_set)))
print ('Testing Data: ' + repr(len(testing_example)))
# generate predictions
predictions=[]
# Number of nearst neighbours for testing the algorithm
k = 3
for i in range(len(testing_example)):
	neighbors = closest_neighbors(training_set, testing_example[i], k)
	result = get_votes(neighbors)
	predictions.append(result)
	print('-> predicted by my code = ' + repr(result) + ', actual value = ' + repr(testing_example[i][-1]))
accuracy = get_accuracy(testing_example, predictions)
print('Accuracy: ' + repr(accuracy) + '%')
	