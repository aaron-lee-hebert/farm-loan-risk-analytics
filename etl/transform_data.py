import pandas as pd
import os

# -----------------------------
# Helpers
# -----------------------------
def standardize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("%", "pct", regex=False)
    )
    return df

def normalize_state(df, col="state"):
    df[col] = df[col].astype(str).str.upper().str.strip()
    return df

def normalize_crop(df, col="crop_type"):
    df[col] = df[col].astype(str).str.lower().str.strip()
    return df

# USDA ships full state names; loans & weather use 2-letter codes.
STATE_NAME_TO_ABBREV = {
    "ALABAMA": "AL",
    "ALASKA": "AK",
    "ARIZONA": "AZ", 
    "ARKANSAS": "AR",
    "CALIFORNIA": "CA", 
    "COLORADO": "CO", 
    "CONNECTICUT": "CT", 
    "DELAWARE": "DE",
    "FLORIDA": "FL", 
    "GEORGIA": "GA", 
    "HAWAII": "HI", 
    "IDAHO": "ID",
    "ILLINOIS": "IL", 
    "INDIANA": "IN", 
    "IOWA": "IA", 
    "KANSAS": "KS",
    "KENTUCKY": "KY", 
    "LOUISIANA": "LA", 
    "MAINE": "ME", 
    "MARYLAND": "MD",
    "MASSACHUSETTS": "MA", 
    "MICHIGAN": "MI", 
    "MINNESOTA": "MN", 
    "MISSISSIPPI": "MS",
    "MISSOURI": "MO", 
    "MONTANA": "MT", 
    "NEBRASKA": "NE", 
    "NEVADA": "NV",
    "NEW HAMPSHIRE": "NH", 
    "NEW JERSEY": "NJ", 
    "NEW MEXICO": "NM", 
    "NEW YORK": "NY",
    "NORTH CAROLINA": "NC", 
    "NORTH DAKOTA": "ND", 
    "OHIO": "OH", 
    "OKLAHOMA": "OK",
    "OREGON": "OR", 
    "PENNSYLVANIA": "PA", 
    "RHODE ISLAND": "RI", 
    "SOUTH CAROLINA": "SC",
    "SOUTH DAKOTA": "SD", 
    "TENNESSEE": "TN", 
    "TEXAS": "TX", 
    "UTAH": "UT",
    "VERMONT": "VT", 
    "VIRGINIA": "VA", 
    "WASHINGTON": "WA", 
    "WEST VIRGINIA": "WV",
    "WISCONSIN": "WI", 
    "WYOMING": "WY",
}

def reshape_usda(df):
    """Turn the long-format USDA survey into tidy (state, year, crop_type, yield)."""
    df = df.copy()
    df = df[df["period"] == "YEAR"]
    df = df[df["data_item"].str.contains("YIELD", case=False, na=False)]
    df = df[df["commodity"].isin(["CORN", "COTTON", "WHEAT"])]

    df["state"] = df["state"].str.upper().map(STATE_NAME_TO_ABBREV)
    df = df.dropna(subset=["state"])

    df["value"] = (
        df["value"].astype(str).str.replace(",", "", regex=False)
    )
    df["yield"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.dropna(subset=["yield"])

    df["crop_type"] = df["commodity"].str.lower()

    return (
        df.groupby(["state", "year", "crop_type"], as_index=False)["yield"]
          .mean()
    )

# -----------------------------
# Extract
# -----------------------------
print("Loading datasets...")

loans_df   = pd.read_csv("data/raw/loans.csv")
crop_df    = pd.read_csv("data/raw/usda_crop_data.csv")
weather_df = pd.read_csv("data/raw/weather_data.csv")

# -----------------------------
# Transform: Standardize Columns
# -----------------------------
loans_df   = standardize_columns(loans_df)
crop_df    = standardize_columns(crop_df)
weather_df = standardize_columns(weather_df)

# -----------------------------
# Transform: Reshape USDA into tidy crop data
# -----------------------------
crop_df = reshape_usda(crop_df)

# -----------------------------
# Transform: Normalize Fields
# -----------------------------
loans_df   = normalize_state(loans_df)
crop_df    = normalize_state(crop_df)
weather_df = normalize_state(weather_df)

loans_df = normalize_crop(loans_df)
crop_df  = normalize_crop(crop_df)

# -----------------------------
# Transform: Clean Missing Values
# -----------------------------
loans_df   = loans_df.dropna()
crop_df    = crop_df.dropna()
weather_df = weather_df.dropna()

# -----------------------------
# Join 1: Crop + Weather (state/year)
# -----------------------------
print("Joining crop + weather data...")

crop_weather_df = crop_df.merge(
    weather_df,
    on=["state", "year"],
    how="left",
)

# -----------------------------
# Build per-(state, crop_type) baseline
# -----------------------------
agg_map = {
    "yield": "mean",
    "avg_rainfall": "mean",
    "avg_temp": "mean",
    "drought_flag": "sum",
    "year": "count",
}
available = {k: v for k, v in agg_map.items() if k in crop_weather_df.columns}
baseline_df = (
    crop_weather_df.groupby(["state", "crop_type"], as_index=False)
                   .agg(available)
                   .rename(columns={
                       "yield": "avg_yield",
                       "drought_flag": "drought_years",
                       "year": "years_observed",
                   })
)

# -----------------------------
# Join 2: Loans + per-(state, crop_type) baseline
# -----------------------------
print("Joining loans + crop/weather baseline...")

merged_df = loans_df.merge(
    baseline_df,
    on=["state", "crop_type"],
    how="left",
)

# -----------------------------
# Feature Engineering (light)
# -----------------------------
if "avg_rainfall" in merged_df.columns:
    merged_df["weather_risk"] = (merged_df["avg_rainfall"] < 20).astype(int)

if "avg_yield" in merged_df.columns:
    crop_mean = merged_df.groupby("crop_type")["avg_yield"].transform("mean")
    merged_df["yield_risk"] = (merged_df["avg_yield"] < crop_mean).astype(int)

# -----------------------------
# Normalize features (0–1 scale)
# -----------------------------
def min_max(series):
    return (series - series.min()) / (series.max() - series.min())

# Only normalize if column exists
if "loan_to_value" in merged_df.columns:
    merged_df["ltv_norm"] = min_max(merged_df["loan_to_value"])

if "interest_rate" in merged_df.columns:
    merged_df["rate_norm"] = min_max(merged_df["interest_rate"])

if "avg_yield" in merged_df.columns:
    # Lower yield = higher risk → invert
    merged_df["yield_norm"] = 1 - min_max(merged_df["avg_yield"])

if "drought_years" in merged_df.columns and "years_observed" in merged_df.columns:
    merged_df["drought_ratio"] = merged_df["drought_years"] / merged_df["years_observed"]
    merged_df["drought_norm"] = min_max(merged_df["drought_ratio"])

# -----------------------------
# Risk Score Calculation
# -----------------------------
merged_df["risk_score"] = (
    0.40 * merged_df.get("ltv_norm", 0) +
    0.20 * merged_df.get("rate_norm", 0) +
    0.20 * merged_df.get("yield_norm", 0) +
    0.20 * merged_df.get("drought_norm", 0)
)

merged_df["risk_score"] = (merged_df["risk_score"] * 100).round(2)

def risk_bucket(score):
    if score < 30:
        return "Low"
    elif score < 60:
        return "Moderate"
    else:
        return "High"

merged_df["risk_category"] = merged_df["risk_score"].apply(risk_bucket)

# -----------------------------
# Final Cleanup
# -----------------------------
merged_df = merged_df.drop_duplicates(subset=["loan_id"])

# -----------------------------
# Output
# -----------------------------
output_dir = "data/processed"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "loans_enriched.csv")
merged_df.to_csv(output_path, index=False)

print(f"\nTransformation complete")
print(f"Output saved to: {output_path}")
print(f"Final shape: {merged_df.shape}")

print("\nPreview:")
print(merged_df.head())

print("\nNull counts on enrichment columns:")
for c in ["avg_yield", "avg_rainfall", "avg_temp", "drought_years", "years_observed"]:
    if c in merged_df.columns:
        print(f"  {c}: {merged_df[c].isna().sum()} / {len(merged_df)}")

print("\nRisk Score Summary:")
print(merged_df["risk_score"].describe())
print("\nRisk Category Distribution:")
print(merged_df["risk_category"].value_counts())
