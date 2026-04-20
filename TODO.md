# ✅ Farm Loan Risk & Portfolio Dashboard - TODO

## 📦 Phase 1: Project Setup

- [x] Create GitHub repository
- [x] Initialize project structure:
  - `/data`
  - `/etl`
  - `/sql`
  - `/notebooks`
  - `/dashboard`
- [x] Create virtual environment
- [x] Install dependencies:
    - pandas
    - numpy
    - sqlalchemy
    - psycopg2

---

## 🌾 Phase 2: Data Acquisition

### USDA Crop Data (REQUIRED)

**Option A (Recommended - Quickest):**
- [x] Go to: https://quickstats.nass.usda.gov/
- [x] Select:
    - Program: "SURVEY"
    - Sector: "CROPS"
    - Group: "FIELD CROPS"
    - Commodity: (Corn, Wheat, Cotton)
    - Category: "YIELD"
    - Geography: "STATE"
- [x] Download CSV

**Option B (API - Optional):**
- [ ] Sign up for USDA NASS API key:
https://quickstats.nass.usda.gov/api
- [ ] Use Python to pull data

---

### 🌦️ Weather Data (REQUIRED)

**Option A (Simple CSV):**
- [x] Download sample weather data from:
https://www.ncdc.noaa.gov/cdo-web/

**Option B (API - Optional):**
- [ ] Register for NOAA API:
https://www.ncdc.noaa.gov/cdo-web/token
- [ ] Pull:
    - Temperature
    - Precipitation

---

### 💰 Loan Data (MOCK - REQUIRED)

- [ ] Create synthetic dataset using Python:
    - loan_id
    - farm_id
    - state
    - crop_type
    - loan_amount
    - interest_rate
    - loan_to_value
- [ ] Use random distributions:
    - Loan amounts: 50k–2M
    - Interest rates: 3–10%
    - Crops: corn, wheat, cotton
- [ ] Save to `/data/raw/loans.csv`

---

## 🔄 Phase 3: Data Engineering (ETL)

### Extract
- [ ] Load all CSVs into pandas DataFrames

### Transform
- [ ] Standardize column names
- [ ] Clean missing/null values
- [ ] Normalize:
    - State names
    - Crop types
- [ ] Join datasets:
    - Crop data + weather data on state/year
    - Loan data + crop data on crop/state

---

### 🧮 Feature Engineering

- [ ] Create yield volatility metric
- [ ] Create weather risk indicator:
    - Low rainfall = higher risk
- [ ] Create `risk_score`:
    Example:
    ```
    risk_score = (yield_volatility * 0.4) + (weather_risk * 0.3) + (loan_to_value * 0.3)
    ```
---

## 🗄️ Phase 4: Data Warehouse

- [ ] Install PostgreSQL locally
- [ ] Create database: `farm_risk`
- [ ] Create tables:
    - fact_loans
    - dim_crop
    - dim_region
    - dim_time
- [ ] Load transformed data into tables

---

## 📊 Phase 5: Analytics Layer

- [ ] Write SQL queries:
    - Total loan exposure by crop
    - Average risk score by region
    - Top 10 highest risk loans

---

## 📈 Phase 6: Dashboard

### Power BI / Tableau

- [ ] Connect to PostgreSQL
- [ ] Build visuals:
    - Bar chart: loan volume by crop
    - Map: regional risk
    - Table: high-risk loans
    - KPI cards:
      - Total portfolio value
      - Avg risk score

---

## 🧾 Phase 7: Documentation

- [ ] Finalize README
- [ ] Add architecture diagram
- [ ] Document:
    - Data sources
    - Assumptions
    - Tradeoffs

---

## 🚀 Phase 8: Polish

- [ ] Clean code
- [ ] Add comments
- [ ] Push final version to GitHub
- [ ] Practice explaining project:
    - Business problem
    - Technical approach
    - Key insights

---

## ⭐ Stretch Goals (Optional)

- [ ] Add dbt transformations
- [ ] Add Airflow pipeline
- [ ] Deploy database to cloud
- [ ] Add commodity price data
