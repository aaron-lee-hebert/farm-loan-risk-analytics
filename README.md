# 🌾 Farm Loan Risk & Portfolio Dashboard

## 📌 Overview
This project simulates a data platform for an agricultural lending institution (e.g., Farm Credit organizations) to assess and monitor loan portfolio risk.

It combines agricultural production data, weather indicators, and a mock loan portfolio to generate insights into:
- Regional risk exposure
- Crop-specific volatility
- Loan portfolio concentration

The goal is to demonstrate a hybrid skillset across:
- Data Engineering
- Data Analysis
- Business Intelligence

---

## 🧠 Business Problem
Agricultural lenders operate in a highly variable environment where factors like drought, crop yield, and commodity prices directly impact borrower risk.

This project answers:
> "How exposed is our loan portfolio to agricultural and environmental risk factors?"

---

## 🏗️ Architecture

Data Sources ➡️Python ETL Pipeline ➡️PostgreSQL Data Warehouse ➡️Power BI Dashboard

---

## 📊 Data Sources

### 1. USDA Crop Data
- Crop yields
- Acreage by region
- Source: USDA National Agricultural Statistics Service (NASS)

### 2. Weather Data
- Temperature
- Precipitation
- Drought indicators (optional)
- Source: NOAA or sample datasets

### 3. Loan Data (Mock)
- Loan amount
- Interest rate
- Crop type
- Farm location
- Loan-to-value ratio

---

## 🧱 Data Model

### Fact Table
- `fact_loans`
  - loan_id
  - farm_id
  - crop_id
  - region_id
  - loan_amount
  - interest_rate
  - risk_score

### Dimension Tables
- `dim_farm`
- `dim_crop`
- `dim_region`
- `dim_time`

---

## ⚙️ ETL Process

1. Extract:
   - Pull USDA and weather datasets
   - Generate mock loan data

2. Transform:
   - Clean and standardize fields
   - Join datasets on region + crop
   - Create derived metrics:
     - Yield volatility
     - Weather risk indicators
     - Loan risk score

3. Load:
   - Store in PostgreSQL warehouse
   - Model into fact/dimension tables

---

## 📈 Dashboard Features

- Portfolio value by crop and region
- Risk score distribution
- Regional exposure map
- Drill-down by:
  - Crop type
  - Loan size
  - Risk tier

---

## 🔍 Key Insights (Example)

- Regions with high yield volatility exhibit increased portfolio risk
- Certain crops (e.g., corn) show higher exposure to environmental variability
- Portfolio concentration in specific regions increases systemic risk

---

## 🛠️ Tech Stack

- Python (pandas, numpy)
- PostgreSQL
- SQL
- Power BI or Tableau
- Optional: dbt

---

## 🚀 Getting Started

1. Clone the repo
2. Set up a PostgreSQL database
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run ETL pipeline:
   ```bash
   python eli/main.py
   ```
5. Connect BI tool to database

---

## 📌 Future Improvements
- Add commodity pricing data
- Incorporate real drought indices
- Automate pipeline scheduling
- Deploy to cloud (AWS/GCP/Azure)

---

## 🤝 Why This Project Matters

This project reflects real-world challenges in agricultural finance:

- Integrating external data sources
- Modeling risk across domains
- Delivering actionable insights to business users
