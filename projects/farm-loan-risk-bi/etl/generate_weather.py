import pandas as pd
import numpy as np
import os

# -----------------------------
# Config
# -----------------------------
np.random.seed(42)

STATES = ["TX", "KS", "OK"]
YEARS = list(range(2015, 2026))

# Per-state climatological baselines (1991-2020 NOAA normals, averaged across
# reporting stations). Annual precipitation in inches, annual mean temp in F.
CLIMATE_BASELINES = {
    "TX": {"annual_precip_in": 30.5, "annual_temp_f": 66.0},
    "KS": {"annual_precip_in": 28.0, "annual_temp_f": 55.0},
    "OK": {"annual_precip_in": 38.7, "annual_temp_f": 60.0},
}

# Year-over-year variability around the baseline. Precipitation is multiplicative
# (good years and drought years scale with climate), temperature is additive.
PRECIP_CV = 0.18          # ~18% std-dev around the annual normal
TEMP_SD_F = 1.5           # +/- 1.5 F year-to-year swing
DROUGHT_THRESHOLD = 0.75  # annual precip < 75% of normal flags a drought year

# -----------------------------
# Helper Functions
# -----------------------------
def generate_annual_rainfall(baseline_in):
    factor = np.random.normal(loc=1.0, scale=PRECIP_CV)
    factor = max(factor, 0.3)
    return baseline_in * factor

def generate_annual_temp(baseline_f):
    return baseline_f + np.random.normal(loc=0.0, scale=TEMP_SD_F)

# -----------------------------
# Generate Data
# -----------------------------
records = []

for state in STATES:
    baseline = CLIMATE_BASELINES[state]
    baseline_precip = baseline["annual_precip_in"]
    baseline_temp   = baseline["annual_temp_f"]

    for year in YEARS:
        rainfall = generate_annual_rainfall(baseline_precip)
        temp     = generate_annual_temp(baseline_temp)

        record = {
            "state": state,
            "year": year,
            "avg_rainfall": round(rainfall, 2),
            "avg_temp": round(temp, 2),
            "drought_flag": 1 if rainfall < baseline_precip * DROUGHT_THRESHOLD else 0,
        }

        records.append(record)

# -----------------------------
# Create DataFrame
# -----------------------------
df = pd.DataFrame(records)

# -----------------------------
# Data Quality Checks
# -----------------------------
df["avg_rainfall"] = df["avg_rainfall"].clip(lower=0.0)

# -----------------------------
# Save to CSV
# -----------------------------
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "weather_data.csv")
df.to_csv(output_path, index=False)

# -----------------------------
# Summary Output
# -----------------------------
print(f"\nGenerated {len(df)} weather records across {df['state'].nunique()} states and {df['year'].nunique()} years")
print(f"Saved to: {output_path}")

print("\nSample Data:")
print(df.head())

print("\nSummary Stats:")
print(df.describe())

print("\nDrought years per state:")
print(df.groupby("state")["drought_flag"].sum())
