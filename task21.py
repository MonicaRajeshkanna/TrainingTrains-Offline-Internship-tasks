from sklearn.tree import DecisionTreeClassifier

X = [[2],[4],[6],[8]]
y = [0,0,1,1]

model = DecisionTreeClassifier()
model.fit(X,y)

print(model.predict([[5]]))