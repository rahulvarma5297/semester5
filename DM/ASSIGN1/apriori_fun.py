from apyori import apriori
import pandas as pd
import numpy as np

store_data = pd.read_csv("geeks.csv")
print(store_data)
records = list()
for i in range(0, 22):
    records.append([str(store_data.values[i, j]) for j in range(0, 6)])
association_rules = apriori(records, min_support=0.50, min_confidence=0.6, min_lift=1.2, min_length=2)
association_results = list(association_rules)
print(association_results)