
from operator import le
import itertools
import numpy as np
import tracemalloc
import matplotlib.pyplot as plt
import sys
msp = 4

file1 = open("apriori_mod.csv","r")
# file1 = open(sys.argv[1],"r")
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
            temp.update({key:1});


trc = []
tracemalloc.reset_peak()
tracemalloc.clear_traces()
tracemalloc.start()

frequentItem = {}
combi = list(itertools.combinations(temp.keys(), 2))
ItemSet = {}
for keys in combi:

    for i in range(0,len(transactions)):
        check =1
        for key in keys:
            if key in transactions[i]:
                check = check
            else:
                check = 0

        if check == 1:
            if keys in ItemSet.keys():
                ItemSet[keys]+=1
            else:
                ItemSet.update({keys:1});
    trc.append(tracemalloc.get_traced_memory())
for item in ItemSet:
    if ItemSet[item] >= msp:
        frequentItem.update({item:ItemSet[item]})
print("2-frequent itemSet of Apriori algo: ")
print(frequentItem)
print("\n")
tracemalloc.stop()


trc2 = []
tracemalloc.reset_peak()
tracemalloc.start()
hashTable=[0]*len(temp)
frequentItemPCY = {}

for q in temp:
    h=[]
    for w in temp:
        if q==w:
            continue
        else :
            h = [q ,w]
        for i in range(0,len(transactions)):
            check =1
            for key in h:
                if key in transactions[i]:
                    check = check
                else:
                    check = 0
            if check == 1:
                indx =0
                for c in range(len(h)):
                    indx = indx+int(h[c][1])*(pow(10,len(h)-c-1));
                hashTable[indx%len(temp)]+= 1
for t in range(len(hashTable)):
    if hashTable[t]<msp:
        hashTable[t] = 0

ItemSet = {}
for q in temp:
    ys=[]
    for w in temp :
        if q==w or q>w:
            continue
        else :
            ys = [q ,w]
            ys= tuple(ys)
        indx =0
        for c in range(len(ys)):
            indx = indx+int(h[c][1])*(pow(10,len(h)-c-1));
        if hashTable[indx%len(temp)] != 0 :
            for i in range(0,len(transactions)):
                check =1
                for key in ys:
                    if key in transactions[i]:
                        check = check
                    else:
                        check = 0

                if check == 1:
                    if tuple(ys) in ItemSet.keys():
                        ItemSet[ys]+=1
                    else:
                        ItemSet.update({ys:1});
    trc2.append(tracemalloc.get_traced_memory())
for item in ItemSet:
    if ItemSet[item] >= msp:
        frequentItemPCY.update({item:ItemSet[item]})
print("2-frequent itemSet of PCY algo: ")
print(frequentItemPCY)
tracemalloc.stop()



y1 = []
y2 = []
for x in range(len(trc2)):
    y2.append(trc2[x][0])

for x in range(len(trc)):
    if x%(len(trc)/len(y2)) == 0 :
        y1.append(trc[x][0])

plt.plot(y1)
plt.plot(y2)
plt.legend(["Apriori","PCY"])
plt.ylabel('Memory usage (bits)')
print(y1)
print(y2)
# # In[409]:
plt.show()
