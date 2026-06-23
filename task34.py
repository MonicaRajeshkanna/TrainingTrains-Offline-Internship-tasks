from sklearn.linear_model import LinearRegression

month = [[1],[2],[3],[4]]
sales = [200,250,300,350]

model = LinearRegression()
model.fit(month,sales)

print(model.predict([[5]]))