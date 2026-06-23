import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Step 1: Load Dataset
data = pd.read_csv("dataset.csv")

# Step 2: Separate Features and Target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Step 3: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Predict
predictions = model.predict(X_test)

# Step 6: Evaluate
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

# Step 7: Save Model
joblib.dump(model, "trained_model.pkl")

print("AI workflow completed successfully!")