import argparse
import tracemalloc
import time
from itertools import chain, combinations

start_time = time.time()
tracemalloc.start()
class typicalRule(object):
    def __init__(self, P, Q, support, confidence, t):
        self.P = P
        self.Q = Q
        self.support = support
        self.confidence = confidence
        self.t = t
    def __repr__(self):
        return '%s%s[%.3f,%.3f]' % ( '{'+','.join(sorted(list(self.P)))+'}', '{'+','.join(sorted(list(self.Q)))+'}', self.support, self.confidence)

class Apriori_implementation(object):
    def __init__(self, data, minSup, minConf):
        self.data = data
        self.minSup = minSup
        self.minConf = minConf
        self.item_st, self.transacList = self.retrieve_itemSet()
        self.freqItemSet = self.find_freq_itemSets()
    @staticmethod
    def abut_set(item_st, m):
        return set([i.union(j) for i in item_st for j in item_st if len(i.union(j)) == m])
    @staticmethod
    def findingCombinedSubsets(item_st):
        return chain(*[combinations(item_st, index + 1) for index, item in enumerate(item_st)])

    def retrieve_itemSet(self):
        item_st = set()
        transacList = list()
        for row in self.data:
            transacList.append(frozenset(row))
            for item in row:
                if item:
                    item_st.add(frozenset([item]))
        return item_st, transacList

    def find_support_list(self):
        EntireList = [(item, float(sum(1 for row in self.transacList if item.issubset(row)))/len(self.transacList))
                         for item in self.item_st]
        return dict([(item, support) for item, support in EntireList if support >= self.minSup])
    def find_freq_itemSets(self):
        freqItemSet = dict()
        m = 1
        while True:
            if m > 1:
                self.item_st = self.abut_set(next_item_st, m)
            next_item_st = self.find_support_list()
            if not next_item_st:
                break
            freqItemSet.update(next_item_st)
            m += 1
        return freqItemSet

    def run(self):
        rules, t = list(), 0
        for item, support in self.freqItemSet.items():
            if len(item) > 1:
                for P in self.findingCombinedSubsets(item):
                    Q = item.difference(P)
                    if Q:
                        P = frozenset(P)
                        PQ = P | Q
                        confidence = float(self.freqItemSet[PQ]) / self.freqItemSet[P]
                        if confidence >= self.minConf:
                            rules.append(typicalRule(P, Q, support=self.freqItemSet[PQ], confidence=confidence, t=t))
                            t += 1                 
        return rules, self.freqItemSet

def parse_arguments():
    argparser = argparse.ArgumentParser(description='Implementation of Apriori Algorithm.')
    argparser.add_argument(
        dest='filename',
        help='name of the file that comprises transactions',
        default='input.csv',
    )
    argparser.add_argument(
        dest='minSup',
        help='provide minimum support count in a floating point num',
        default=0.2,
        type=float
    )
    argparser.add_argument(
        dest='minConf',
        help='provide minimum confidence in floating point num',
        default=0.4,
        type=float
    )
    return argparser.parse_args()

def examine_input(filename):
    file = open(filename, 'r')
    for line in file:
        row = line.strip().split(' ')
        yield row
def displayAssociationRules(rules):
    rules.sort(key=lambda x: (len(x.P) + len(x.Q), x.confidence, x.support, -x.t), reverse=True)
    for rule in rules:
        print(rule)

def main():
    arguments = parse_arguments()
    data = examine_input(arguments.filename)
    rules, item_st = Apriori_implementation(data, arguments.minSup, arguments.minConf).run()
    displayAssociationRules(rules)

if __name__ == '__main__':
    main()
end_time = time.time()
elapsed_time = end_time - start_time
print("Time taken to execute the program is: ", elapsed_time, "seconds")
print("Memory used by the program is: ", tracemalloc.get_traced_memory())
tracemalloc.stop()