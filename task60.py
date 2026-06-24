from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

parameters = {
    "C": [1, 10],
    "kernel": ["linear", "rbf"]
}

model = GridSearchCV(
    SVC(),
    parameters
)

print("Grid Search Ready")