from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.DataFrame({
    "Marks":[40,60,80,100]
})

scaler = MinMaxScaler()

data["Normalized"] = scaler.fit_transform(data)

print(data)