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
  - pyodbc

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

---

### 🌦️ Weather Data (REQUIRED)

**Option A (Simple CSV):**

- [x] Download sample weather data from:
      https://www.ncdc.noaa.gov/cdo-web/

---

### 💰 Loan Data (MOCK - REQUIRED)

- [x] Create synthetic dataset using Python:
  - loan_id
  - farm_id
  - state
  - crop_type
  - loan_amount
  - interest_rate
  - loan_to_value
- [x] Use realistic distributions
- [x] Save to `/data/raw/loans.csv`

---

## 🔄 Phase 3: Data Engineering (ETL)

### Extract

- [x] Load all CSVs into pandas DataFrames

### Transform

- [x] Standardize column names
- [x] Clean missing/null values
- [x] Normalize:
  - State names
  - Crop types
- [x] Join datasets:
  - Crop data + weather data on state/year
  - Loan data + crop data on crop/state

---

### 🧮 Feature Engineering

- [x] Create yield volatility metric
- [x] Create weather risk indicator
- [x] Create `risk_score`

---

## 🗄️ Phase 4: Data Warehouse

- [ ] Install SQL Server (Developer or Express)
- [ ] Install SQL Server Management Studio (SSMS)
- [ ] Create database:
  ```sql
  CREATE DATABASE FarmRiskDB;
  ```
- [ ] Create staging table:
  - staging_loans
- [ ] Create tables:
  - fact_loans
  - dim_crop
  - dim_region
  - dim_time
- [ ] Load transformed data into SQL Server using Python (SQLAlchemy + pyodbc)

---

## 📊 Phase 5: Analytics Layer

- [ ] Write SQL queries:
  - Total loan exposure by crop
  - Average risk score by region
  - Top 10 highest risk loans

---

## 📈 Phase 6: Dashboard

- [ ] Connect Power BI to SQL Server
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
- [ ] Deploy to Azure SQL Database
- [ ] Add commodity price data
