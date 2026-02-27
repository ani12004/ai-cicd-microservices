import os
import pandas as pd
import joblib

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # ai-module folder
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
TEST_HISTORY_PATH = os.path.join(BASE_DIR, "test_history.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "prioritized_tests.csv")

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load(MODEL_PATH)

# -----------------------------
# Load test history / features
# -----------------------------
data = pd.read_csv(TEST_HISTORY_PATH)

# -----------------------------
# Ensure all expected features are present
# Replace with your actual training features
# -----------------------------
expected_features = [
    "code_changes",
    "lines_added",
    "lines_deleted",
    "test_history",
    "other_feature1",
    "other_feature2"
]

for col in expected_features:
    if col not in data.columns:
        data[col] = 0  # fill missing with default value

X = data[expected_features]

# -----------------------------
# Predict failure probability
# -----------------------------
data["failure_probability"] = model.predict_proba(X)[:, 1]

# -----------------------------
# Sort tests by probability descending
# -----------------------------
data = data.sort_values(by="failure_probability", ascending=False)

# -----------------------------
# Save prioritized tests
# -----------------------------
data.to_csv(OUTPUT_PATH, index=False)

print(f"Prioritized tests saved to {OUTPUT_PATH}")
