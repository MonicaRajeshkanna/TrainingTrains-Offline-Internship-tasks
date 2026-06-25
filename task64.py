from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()

model = DecisionTreeClassifier()

scores = cross_val_score(model,
                         iris.data,
                         iris.target,
                         cv=5)

print(scores)
print("Average:",scores.mean())