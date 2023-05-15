from operator import le
import itertools
import numpy as np
min_sup_count = 4

file1 = open("cla.csv","r")
str1 = file1.read()
transactions = []

mx=0
a = str1.split("\n")
for i in range(0,len(a)):
    b = a[i].split(",")
    mx = max(len(b),mx)
    b=filter(None,b)
    transactions.append(list(b))


temp = {}
for x in transactions:
    for key in x:
        if key in temp.keys():
            temp[key]+=1
        else:
            temp.update({key:1})
frequentItem = {}
for itr in range(1,mx+1):
    combi = list(itertools.combinations(temp.keys(), itr))
    ItemSet = {}
    for keys in combi:
        for i in range(0,len(transactions)):
            c =1
            for key in keys:
                if key in transactions[i]:
                    c = c
                else:
                    c = 0
                    
            if c == 1:
                if keys in ItemSet.keys():
                    ItemSet[keys]+=1
                else:
                    ItemSet.update({keys:1})
    for item in ItemSet:
        if ItemSet[item] >= min_sup_count:
            frequentItem.update({item:ItemSet[item]})
(frequentItem)


def powerset(iterable):
    s = list(iterable)
    return map(list,itertools.chain.from_iterable( itertools.combinations(s, r) for r in range(1,len(s))))


for b in frequentItem.keys():
    c=list(b)
    a=list(powerset(c))
    for x in a:
        for y in a:
            if len(x)+len(y)==len(c) and len(np.intersect1d(x, y))==0:
                support = ((frequentItem[tuple(c)]))/len(transactions)
                confidence = (frequentItem[tuple(c)])/(frequentItem[tuple(x)])
                print("{"+",".join([(t) for t in x])+"}"+"{"+",".join([(t) for t in y])+"}"+"["+str(support)+","+str(confidence)+"]")
                




