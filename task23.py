from sklearn.svm import SVC

X = [[1],[2],[3],[4]]
y = [0,0,1,1]

model = SVC()
model.fit(X,y)

print(model.predict([[3]]))