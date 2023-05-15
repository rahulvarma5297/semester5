import numpy as np
import sys
import math
from operator import le
import itertools

# data from csv using command line argument
input_csv = open(sys.argv[1], "r")
input_storing = input_csv.read()
data = list()

min_sup_percent = float(sys.argv[2])
min_conf_percent = float(sys.argv[3])

seperate_line = input_storing.split("\n")

min_sup = len(seperate_line) * min_sup_percent
min_sup = math.ceil(min_sup)


def powerset(i):
    temp = list(i)
    return map(list, itertools.chain.from_iterable(itertools.combinations(temp, j) for j in range(1, len(temp))))


# Stroring data in a list
max_val = 0
for i in range(0, len(seperate_line)):
    temp = seperate_line[i].split(",")
    # Stripping data if any spaces are present.
    for i in range(0, len(temp)):
        temp[i] = temp[i].strip()

    max_val = max(len(temp), max_val)
    temp = filter(None, temp)
    data.append(list(temp))

data_2 = {}
for i in data:
    for j in i:
        if j in data_2.keys():
            data_2[j] += 1
        else:
            data_2.update({j: 1})

# Main Logic
frequentItems = {}
for i in range(1, max_val+1):
    combination = list(itertools.combinations(data_2.keys(), i))
    ItemSets = {}
    for k in combination:
        for j in range(0, len(data)):
            flag = 1
            for key in k:
                if key in data[j]:
                    flag = flag
                else:
                    flag = 0

            if flag == 1:
                if k in ItemSets.keys():
                    ItemSets[k] += 1
                else:
                    ItemSets.update({k: 1})
    for x in ItemSets:
        if ItemSets[x] >= min_sup:
            frequentItems.update({x: ItemSets[x]})


# Printing in the same format as given in the instructions {I1}{I2,I3}[0.5,0.66]
for i in frequentItems.keys():
    temp1 = list(i)
    temp2 = list(powerset(temp1))
    for j in temp2:
        for k in temp2:
            if len(j) + len(k) == len(temp1) and len(np.intersect1d(j, k)) == 0:
                sup = (frequentItems[tuple(temp1)]) / len(data)
                sup = round(sup, 2)
                conf = (frequentItems[tuple(temp1)]) / \
                    (frequentItems[tuple(j)])
                conf = round(conf, 4)
                if conf >= min_conf_percent:
                    print("{"+",".join([(x) for x in j])+"}"+"{"+",".join([(x)
                          for x in k])+"}"+"["+str(sup)+","+str(conf)+"]")


# Command Line
# db4.txt
# Format: {I1}{I2,I3}[0.5,0.66]
# python S20200010212_apriori.py Q3.csv 0.2 0.2 
