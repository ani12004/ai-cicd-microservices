import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Load test history
data = pd.read_csv("test_history.csv")

# Select features
X = data[["execution_time", "past_failures"]]

# Predict probability of failure
data["failure_probability"] = model.predict_proba(X)[:, 1]

# Sort by highest failure probability
data = data.sort_values(by="failure_probability", ascending=False)

# Save prioritized test list
data.to_csv("prioritized_tests.csv", index=False)

print("Test cases prioritized successfully.")
