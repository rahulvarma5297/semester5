import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
train = pd.read_csv("training.csv")
train = train.drop(['url'], axis=1)

x_train = train.iloc[:, 0:-1]
y_train = train.iloc[:, -1]

clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(x_train, y_train)

test = pd.read_csv("testing.csv")
test = test.drop(['url'], axis=1)

x_test = test.iloc[:, 0:-1]
y_test = test.iloc[:, -1]
y_pred = clf.predict(x_test)

print("Number of test data points:", len(y_pred))
print("Accuracy: ",accuracy_score(y_test, y_pred))
print("Precision: ",precision_score(y_test, y_pred, pos_label='phishing'))
print("Recall: ",recall_score(y_test, y_pred, pos_label='phishing'))
print("F1 Score: ",f1_score(y_test, y_pred, pos_label='phishing'))
