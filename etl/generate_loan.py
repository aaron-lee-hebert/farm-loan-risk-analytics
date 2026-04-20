import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# -----------------------------
# Config
# -----------------------------
NUM_RECORDS = 1000

states = ["TX", "KS", "OK", "NE", "IA"]
crop_types = ["corn", "wheat", "cotton"]

# -----------------------------
# Generate Data
# -----------------------------
data = []

for i in range(NUM_RECORDS):
    loan_id = i + 1
    farm_id = fake.uuid4()

    state = random.choice(states)
    crop_type = random.choice(crop_types)

    # Loan amount: 50k–2M
    loan_amount = round(np.random.uniform(50_000, 2_000_000), 2)

    # Interest rate: 3%–10%
    interest_rate = round(np.random.uniform(0.03, 0.10), 4)

    # Loan-to-value: 40%–90%
    loan_to_value = round(np.random.uniform(0.4, 0.9), 2)

    data.append({
        "loan_id": loan_id,
        "farm_id": farm_id,
        "state": state,
        "crop_type": crop_type,
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "loan_to_value": loan_to_value
    })

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(data)

# -----------------------------
# Save to CSV
# -----------------------------
output_path = "data/raw/loans.csv"
df.to_csv(output_path, index=False)

print(f"Generated {NUM_RECORDS} records → {output_path}")
