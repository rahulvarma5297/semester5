# Apriori Algorithm

import sys
import itertools
import collections

def get_data(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data

def get_itemset(data):
    itemset = set()
    for line in data:
        for item in line.split():
            itemset.add(item)
    return itemset

def get_itemset_count(data, itemset):
    itemset_count = collections.Counter()
    for line in data:
        for item in itemset:
            if item in line.split():
                itemset_count[item] += 1
    return itemset_count

def get_itemset_pair_count(data, itemset):
    itemset_pair_count = collections.Counter()
    for line in data:
        for item in itertools.combinations(itemset, 2):
            if item[0] in line.split() and item[1] in line.split():
                itemset_pair_count[item] += 1
    return itemset_pair_count

def get_itemset_pair(itemset):
    itemset_pair = set()
    for item in itertools.combinations(itemset, 2):
        itemset_pair.add(item)
    return itemset_pair

def get_itemset_pair_support(itemset_pair_count, itemset_count):
    itemset_pair_support = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_support[item] = itemset_pair_count[item] / itemset_count[item[0]]
    return itemset_pair_support

def get_itemset_pair_confidence(itemset_pair_count, itemset_count):
    itemset_pair_confidence = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_confidence[item] = itemset_pair_count[item] / itemset_count[item[0]]
    return itemset_pair_confidence

def get_itemset_pair_lift(itemset_pair_count, itemset_count):
    itemset_pair_lift = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_lift[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_lift

def get_itemset_pair_conviction(itemset_pair_count, itemset_count):
    itemset_pair_conviction = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_conviction[item] = (1 - itemset_count[item[1]]) / (1 - itemset_pair_count[item])
    return itemset_pair_conviction

def get_itemset_pair_jaccard(itemset_pair_count, itemset_count):
    itemset_pair_jaccard = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_jaccard[item] = itemset_pair_count[item] / (itemset_count[item[0]] + itemset_count[item[1]] - itemset_pair_count[item])
    return itemset_pair_jaccard

def get_itemset_pair_leverage(itemset_pair_count, itemset_count):
    itemset_pair_leverage = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_leverage[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_leverage

def get_itemset_pair_cosine(itemset_pair_count, itemset_count):
    itemset_pair_cosine = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_cosine[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_cosine

def get_itemset_pair_interest(itemset_pair_count, itemset_count):
    itemset_pair_interest = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_interest[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_interest

def get_itemset_pair_yulesq(itemset_pair_count, itemset_count):
    itemset_pair_yulesq = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_yulesq[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_yulesq

def get_itemset_pair_yuley(itemset_pair_count, itemset_count):
    itemset_pair_yuley = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_yuley[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_yuley

def get_itemset_pair_ochiai(itemset_pair_count, itemset_count):
    itemset_pair_ochiai = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_ochiai[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_ochiai

def get_itemset_pair_kulczynski(itemset_pair_count, itemset_count):
    itemset_pair_kulczynski = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_kulczynski[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_kulczynski

def get_itemset_pair_simpson(itemset_pair_count, itemset_count):
    itemset_pair_simpson = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson

def get_itemset_pair_simpson2(itemset_pair_count, itemset_count):
    itemset_pair_simpson2 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson2[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson2

def get_itemset_pair_simpson3(itemset_pair_count, itemset_count):
    itemset_pair_simpson3 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson3[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson3

def get_itemset_pair_simpson4(itemset_pair_count, itemset_count):
    itemset_pair_simpson4 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson4[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson4

def get_itemset_pair_simpson5(itemset_pair_count, itemset_count):
    itemset_pair_simpson5 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson5[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson5

def get_itemset_pair_simpson6(itemset_pair_count, itemset_count):
    itemset_pair_simpson6 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson6[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson6

def get_itemset_pair_simpson7(itemset_pair_count, itemset_count):
    itemset_pair_simpson7 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson7[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson7

def get_itemset_pair_simpson8(itemset_pair_count, itemset_count):
    itemset_pair_simpson8 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson8[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson8

def get_itemset_pair_simpson9(itemset_pair_count, itemset_count):
    itemset_pair_simpson9 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson9[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson9

def get_itemset_pair_simpson10(itemset_pair_count, itemset_count):
    itemset_pair_simpson10 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson10[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson10

def get_itemset_pair_simpson11(itemset_pair_count, itemset_count):
    itemset_pair_simpson11 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson11[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson11

def get_itemset_pair_simpson12(itemset_pair_count, itemset_count):
    itemset_pair_simpson12 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson12[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson12

def get_itemset_pair_simpson13(itemset_pair_count, itemset_count):
    itemset_pair_simpson13 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson13[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson13


def get_itemset_pair_simpson14(itemset_pair_count, itemset_count):
    itemset_pair_simpson14 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson14[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson14

def get_itemset_pair_simpson15(itemset_pair_count, itemset_count):
    itemset_pair_simpson15 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson15[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson15

def get_itemset_pair_simpson16(itemset_pair_count, itemset_count):
    itemset_pair_simpson16 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson16[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson16

def get_itemset_pair_simpson17(itemset_pair_count, itemset_count):
    itemset_pair_simpson17 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson17[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson17

def get_itemset_pair_simpson18(itemset_pair_count, itemset_count):
    itemset_pair_simpson18 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson18[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson18

def get_itemset_pair_simpson19(itemset_pair_count, itemset_count):
    itemset_pair_simpson19 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson19[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson19

def get_itemset_pair_simpson20(itemset_pair_count, itemset_count):
    itemset_pair_simpson20 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson20[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson20

def get_itemset_pair_simpson21(itemset_pair_count, itemset_count):
    itemset_pair_simpson21 = collections.Counter()
    for item in itemset_pair_count:
        itemset_pair_simpson21[item] = itemset_pair_count[item] / (itemset_count[item[0]] * itemset_count[item[1]])
    return itemset_pair_simpson21


    

