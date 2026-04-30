# ✅ Flight Data Pipeline — TODO

---

# 🟢 Phase 1 — Project Setup

## Goal: Scaffold repo + basic ingestion

- [x] Initialize repo structure
- [x] Create virtual environment
- [x] Install dependencies (requests, pandas, etc.)
- [x] Create `.env` for API keys
- [x] Write basic API client
- [x] Test API response locally
- [x] Save raw JSON to local file

---

# 🟡 Phase 2 — Ingestion Pipeline

## Goal: Production-like ingestion layer

- [x] Implement pagination handling
- [x] Add retry logic (failures/timeouts)
- [x] Add logging (success/failure)
- [x] Add ingestion timestamp
- [x] Write data to Bronze layer (local or cloud)
- [x] Parameterize ingestion (date range, etc.)

---

# 🟠 Phase 3 — Cloud Setup

## Goal: Move storage to cloud

- [x] Create Azure Storage Account
- [x] Create containers (bronze/silver/gold)
- [x] Connect Python app to Blob Storage
- [x] Upload Bronze data to cloud
- [x] Validate file structure

---

# 🔵 Phase 4 — Databricks Setup

## Goal: Enable distributed processing

- [ ] Create Databricks workspace
- [ ] Create cluster
- [ ] Connect to Blob Storage
- [ ] Load Bronze data into Spark DataFrame

---

# 🟣 Phase 5 — Bronze → Silver

## Goal: Clean + normalize data

- [ ] Flatten JSON schema
- [ ] Define structured schema
- [ ] Handle null/missing values
- [ ] Deduplicate flights
- [ ] Write to Silver layer (Delta format)

---

# 🔴 Phase 6 — Silver → Gold

## Goal: Create analytics-ready data

- [ ] Create fact table (flights)
- [ ] Create dimension tables (airports, time)
- [ ] Compute metrics:
  - [ ] Flights per day
  - [ ] Delay rate
  - [ ] On-time %
- [ ] Write Gold tables

---

# 🟤 Phase 7 — Incremental Processing

## Goal: Make pipeline realistic

- [ ] Track last ingestion timestamp
- [ ] Only ingest new records
- [ ] Implement Delta MERGE (upsert)
- [ ] Handle late-arriving data

---

# ⚫ Phase 8 — Data Quality

## Goal: Add reliability

- [ ] Validate schema consistency
- [ ] Check for duplicates
- [ ] Check null thresholds
- [ ] Log data quality issues

---

# ⚪ Phase 9 — Power BI Dashboard

## Goal: Deliver insights

- [ ] Connect Power BI to Gold layer
- [ ] Build visuals:
  - [ ] Flights per day
  - [ ] Delay trends
  - [ ] Airport performance
- [ ] Add filters (airline, airport)
- [ ] Polish dashboard UI

---

# 🟩 Phase 10 — Orchestration

## Goal: Automate pipeline

- [ ] Schedule ingestion (cron / Databricks job)
- [ ] Automate transformations
- [ ] Add failure alerts

---

# 🟪 Phase 11 — Polish & Resume Prep

## Goal: Make it job-ready

- [ ] Add architecture diagram to README
- [ ] Add screenshots of dashboard
- [ ] Document challenges + solutions
- [ ] Clean code + comments
- [ ] Prepare talking points for interviews

---

# 🚀 Stretch Goals

- [ ] Add streaming ingestion
- [ ] Integrate weather data
- [ ] Build REST API for querying data
- [ ] Add CI/CD pipeline
