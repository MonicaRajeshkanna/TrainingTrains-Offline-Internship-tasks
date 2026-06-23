from sklearn.ensemble import IsolationForest
import numpy as np

data = np.array([[100],[110],[105],[500]])

model = IsolationForest(random_state=42)
model.fit(data)

print(model.predict(data))