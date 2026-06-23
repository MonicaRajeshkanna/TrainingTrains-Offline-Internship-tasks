from sklearn.cluster import KMeans
import pandas as pd

customers = pd.DataFrame({
    "Income":[25,30,80,90],
    "Spending":[20,25,90,95]
})

model = KMeans(n_clusters=2)

customers["Cluster"] = model.fit_predict(customers)

print(customers)