import numpy as np
import sys
import math
from operator import le
import itertools
import tracemalloc
import gc
import matplotlib.pyplot as plt


input_csv = open(sys.argv[1], "r")
input_storing = input_csv.read()
data = list()

min_sup_percent = float(sys.argv[2])
min_conf_percent = float(sys.argv[3])

seperate_line = input_storing.split("\n")

min_sup = len(seperate_line) * min_sup_percent
min_sup = math.ceil(min_sup)

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

trace1 = list()
tracemalloc.reset_peak()
tracemalloc.clear_traces()
tracemalloc.start()

frequentItems = {}
pcy_frequentItems = {}
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
        trace1.append(tracemalloc.get_traced_memory())
    
    for x in ItemSets:
        if ItemSets[x] >= min_sup:
            frequentItems.update({x: ItemSets[x]})
            if i != 2:
                pcy_frequentItems.update({x: ItemSets[x]})

tracemalloc.stop()

hash_values = [0]*len(data_2)

for m in data_2:
    hash_data = list()
    for n in data_2:
        if m == n:
            continue
        else:
            hash_data = [m, n]
        for i in range(0, len(data)):
            flag = 1
            for x in hash_data:
                if x in data[i]:
                    flag = flag
                else:
                    flag = 0
            if flag == 1:
                temp = 0
                for k in range(len(hash_data)):
                    temp = temp + int(hash_data[k][1])*10+len(hash_data)
                hash_values[temp % len(data_2)] += 1

for i in range(len(hash_values)):
    if hash_values[i] < min_sup:
        hash_values[i] = 0

trace2 = list() 
tracemalloc.reset_peak()
tracemalloc.clear_traces()
tracemalloc.start()

ItemSets = {}
for m in data_2:
    temp = list()
    for n in data_2:
        if m == n or m > n:
            continue
        else:
            temp = [m, n]
            temp = tuple(temp)
        tt = 0
        for c in range(len(temp)):
            tt = tt + int(hash_data[c][1])*10+len(hash_data)
        if hash_values[tt % len(data_2)] != 0:
            for i in range(0, len(data)):
                flag = 1
                for x in temp:
                    if x in data[i]:
                        flag = flag
                    else:
                        flag = 0

                if flag == 1:
                    if tuple(temp) in ItemSets.keys():
                        ItemSets[temp] += 1
                    else:
                        ItemSets.update({temp: 1})
    trace2.append(tracemalloc.get_traced_memory())
    
for i in ItemSets:
    if ItemSets[i] >= min_sup:
        pcy_frequentItems.update({i: ItemSets[i]})

tracemalloc.stop()

def  powerset(i):
    temp = list(i)
    return map(list, itertools.chain.from_iterable(itertools.combinations(temp, j) for j in range(1, len(temp))))

for i in pcy_frequentItems.keys():
    temp1 = list(i)
    temp2 = list(powerset(temp1))
    for j in temp2:
        for k in temp2:
            if len(j) + len(k) == len(temp1) and len(np.intersect1d(j, k)) == 0:
                sup = (pcy_frequentItems[tuple(temp1)]) / len(data)
                sup = round(sup, 2)
                conf = (pcy_frequentItems[tuple(temp1)]) / (pcy_frequentItems[tuple(j)])
                conf = round(conf, 4)
                if conf >= min_conf_percent:
                    print("{"+",".join([(x) for x in j])+"}"+"{"+",".join([(x) for x in k])+"}"+"["+str(sup)+","+str(conf)+"]")


memory_data1 = list()
memory_data2 = list()
for i in range(len(trace2)):
    memory_data2.append(round(trace2[i][0]))
    

for i in range(len(trace1)):
    if i % (len(trace1)/len(memory_data2)) == 0:
        memory_data1.append(trace1[i][0])
plt.plot(memory_data1, color='blue', marker = '*')
plt.plot(memory_data2, color='yellow', marker = '*')
plt.legend(["Apriori", "PCY"])
plt.xlabel('Number of transactions and items')
plt.ylabel('Memory usage in bits')

# By uncommenting next 4 lines we can get the values of memory usage.
# print()
# print("The data of memory after varying the number of transactions in the database and the number of items:")
# print("Memory for Apriori: ",memory_data1)
# print("Memory for PCY: ",memory_data2)
plt.show()

# Command Line
# python S20200010212_pcy.py apriori.csv 0.4 0.7

