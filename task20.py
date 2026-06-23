from sklearn.linear_model import LogisticRegression

X = [
    [2],
    [4],
    [6],
    [8]
]

y = [
    0,
    0,
    1,
    1
]

model = LogisticRegression()

model.fit(X,y)

prediction = model.predict([[5]])

print("Predicted Class:",prediction)