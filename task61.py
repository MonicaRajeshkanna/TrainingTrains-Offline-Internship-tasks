from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

parameters = {
    "C":[1,10],
    "kernel":["linear","rbf"]
}

grid = GridSearchCV(SVC(), parameters)

print("Hyperparameter tuning model created.")