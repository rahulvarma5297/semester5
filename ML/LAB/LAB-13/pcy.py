# Implement the PCY algorithm for frequent itemset mining

import sys
import itertools
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Read the data from the file
def readData(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip().split(','))
    return data

# Create the candidate set
def createCandidateSet(data, k):
    candidateSet = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i][:k-2] == data[j][:k-2]:
                candidateSet.append(sorted(list(set(data[i]+data[j]))))
    return candidateSet

# Create the frequent itemset
def createFrequentItemset(data, candidateSet, minSupport):
    frequentItemset = []
    for item in candidateSet:
        count = 0
        for transaction in data:
            if set(item).issubset(set(transaction)):
                count += 1
        if count >= minSupport:
            frequentItemset.append(item)
    return frequentItemset

# Create the frequent itemset using PCY
def createFrequentItemsetPCY(data, candidateSet, minSupport, bucketSize):
    frequentItemset = []
    count = [0] * bucketSize
    for item in candidateSet:
        for transaction in data:
            if set(item).issubset(set(transaction)):
                count[hash(tuple(item)) % bucketSize] += 1
    for item in candidateSet:
        if count[hash(tuple(item)) % bucketSize] >= minSupport:
            frequentItemset.append(item)
    return frequentItemset



# Main function
def main():
    # Read the data
    data = readData('Groceries.csv')
    # Create the candidate set
    candidateSet = createCandidateSet(data, 2)
    # Create the frequent itemset
    frequentItemset = createFrequentItemset(data, candidateSet, 100)
    # Print the frequent itemset
    print(frequentItemset)
    # Create the frequent itemset using PCY
    frequentItemsetPCY = createFrequentItemsetPCY(data, candidateSet, 100, 1000)
    # Print the frequent itemset using PCY
    print(frequentItemsetPCY)

if __name__ == '__main__':
    main()

