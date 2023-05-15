import numpy as np
import pandas as pd
import csv


def recurse(lst, count, curr, k, freq):
    n = len(lst)
    if len(curr) == k:
        if tuple(curr) in freq:
            freq[tuple(curr)] += 1
    else:
        l = len(curr)
        if l == 0 or tuple(curr) in fps[l]:
            for i in range(count+1, n):
                curr = [j for j in curr[:l]]
                curr.append(lst[i])
                recurse(lst, i, curr, k, freq)

# Original Code.


file = open('data.csv')
reader = csv.reader(file)

rows = []
for row in reader:
    rows.append(row)
print(rows)

support = 3


# Step 1 : Finding frequent pairs
candidates = dict()

for i in rows:
    for j in i:
        if tuple(j) not in candidates:
            candidates[tuple(j)] = 1
        else:
            candidates[tuple(j)] += 1


freq = dict()
for i in candidates:
    if candidates[tuple(i)] >= support:
        freq[tuple(i)] = candidates[tuple(i)]

cps = dict()
fps = dict()
cps[1] = candidates
fps[1] = freq
print("Candidates :")
print(cps)
print("Frequent candidates :")
print(fps)


# Step 2

k = 2
new = 1
while(new != 0):
    new = 0
    cand = dict()
    vals = list(fps[k-1].keys())
    vals.sort()
    n = len(vals)
    for i in range(n):
        s = list(vals[i])
        for j in range(i+1, n):
            s1 = list(vals[j])
            s.extend(s1)
            st = set(s)
            if len(st) == k:
                tp = list(st)
                tp.sort()
                if tuple(tp) not in cand:
                    cand[tuple(tp)] = 0
            s = list(vals[i])
    curr = []
    for j in rows:
        recurse(j, -1, curr, k, cand)
    print("Candidate Pairs :")
    print(cand)
    if cand == {}:
        new = 0
    else:
        z = list(cand.keys())[0]
        print("Frequent Pairs :")
        freq = dict()
        for i in cand:
            if cand[i] >= support:
                print(i, cand[i])
                new = 1
                freq[i] = cand[i]
        z = len(list(cand.keys())[0])

        print(z)
        print(new)
        fps[z] = freq
        k += 1
