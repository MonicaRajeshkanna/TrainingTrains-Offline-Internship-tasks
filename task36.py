from statsmodels.tsa.arima.model import ARIMA

data = [20,22,25,28,30,33]

model = ARIMA(data, order=(1,1,1))

result = model.fit()

print(result.forecast())