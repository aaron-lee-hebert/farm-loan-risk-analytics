import pandas as pd

def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


# -----------------------------
# Extract
# -----------------------------
loans_df = pd.read_csv("data/raw/loans.csv")

# -----------------------------
# Transform
# -----------------------------
loans_df = standardize_columns(loans_df)

# Clean nulls
loans_df = loans_df.dropna()

# Normalize
loans_df["state"] = loans_df["state"].str.upper().str.strip()
loans_df["crop_type"] = loans_df["crop_type"].str.lower().str.strip()

# -----------------------------
# (Optional) Join other datasets later
# -----------------------------
# crop_df = pd.read_csv("data/raw/crop_data.csv")
# weather_df = pd.read_csv("data/raw/weather_data.csv")

# merged_df = loans_df.merge(crop_df, on=["state"], how="left")
# merged_df = merged_df.merge(weather_df, on=["state"], how="left")

# -----------------------------
# Output (for next step)
# -----------------------------
loans_df.to_csv("data/processed/loans_cleaned.csv", index=False)

print("Transformation complete")
