from sklearn.linear_model import LinearRegression

days = [[1],[2],[3],[4],[5]]
price = [100,102,104,106,108]

model = LinearRegression()
model.fit(days,price)

print(model.predict([[6]]))