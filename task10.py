from sklearn.preprocessing import StandardScaler
import pandas as pd

data = pd.DataFrame({
    "Marks":[40,60,80,100]
})

scaler = StandardScaler()

data["Standardized"] = scaler.fit_transform(data)

print(data)