import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# -----------------------------
# Config
# -----------------------------
fake = Faker()
random.seed(42)
np.random.seed(42)

NUM_RECORDS = 1000

states = ["TX", "KS", "OK", "NE", "IA"]

# Regional crop bias
crop_weights_by_state = {
    "TX": {"cotton": 0.5, "corn": 0.3, "wheat": 0.2},
    "KS": {"wheat": 0.6, "corn": 0.3, "cotton": 0.1},
    "OK": {"wheat": 0.5, "corn": 0.3, "cotton": 0.2},
    "NE": {"corn": 0.7, "wheat": 0.2, "cotton": 0.1},
    "IA": {"corn": 0.8, "wheat": 0.2, "cotton": 0.0},
}

# -----------------------------
# Helper Functions
# -----------------------------
def generate_crop(state):
    crops = list(crop_weights_by_state[state].keys())
    weights = list(crop_weights_by_state[state].values())
    return random.choices(crops, weights=weights, k=1)[0]

def generate_loan_amount():
    amount = np.random.lognormal(mean=12, sigma=0.8)
    return float(np.clip(amount, 50_000, 2_000_000))

def generate_interest_rate():
    return round(np.random.normal(loc=0.06, scale=0.015), 4)

def generate_ltv():
    return round(np.random.uniform(0.4, 0.9), 2)


# -----------------------------
# Generate Data
# -----------------------------
records = []

for i in range(NUM_RECORDS):
    state = random.choice(states)
    crop_type = generate_crop(state)

    loan_amount = round(generate_loan_amount(), 2)
    interest_rate = generate_interest_rate()
    loan_to_value = generate_ltv()

    risk_flag = 1 if loan_to_value > 0.8 else 0

    record = {
        "loan_id": i + 1,
        "farm_id": fake.uuid4(),
        "state": state,
        "crop_type": crop_type,
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "loan_to_value": loan_to_value,
        "risk_flag": risk_flag
    }

    records.append(record)

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(records)

# -----------------------------
# Data Quality Checks
# -----------------------------
df["interest_rate"] = df["interest_rate"].clip(0.03, 0.10)

# -----------------------------
# Save to CSV
# -----------------------------
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "loans.csv")
df.to_csv(output_path, index=False)

# -----------------------------
# Summary Output
# -----------------------------
print(f"\nGenerated {len(df)} loan records")
print(f"Saved to: {output_path}")

print("\nSample Data:")
print(df.head())

print("\nSummary Stats:")
print(df.describe())
