IF DB_ID('FarmRiskDB') IS NULL
    CREATE DATABASE FarmRiskDB;
GO

USE FarmRiskDB;
GO

IF OBJECT_ID('fact_loans', 'U') IS NOT NULL DROP TABLE fact_loans;

CREATE TABLE fact_loans (
    loan_id INT PRIMARY KEY,
    farm_id VARCHAR(100),
    crop_id INT,
    region_id INT,
    loan_amount DECIMAL(18,2),
    interest_rate DECIMAL(6,4),
    loan_to_value DECIMAL(5,2),
    risk_score FLOAT,
    risk_category VARCHAR(20)
);

IF OBJECT_ID('staging_loans', 'U') IS NOT NULL DROP TABLE staging_loans;

CREATE TABLE staging_loans (
    loan_id INT,
    farm_id VARCHAR(100),
    state VARCHAR(10),
    crop_type VARCHAR(50),
    loan_amount DECIMAL(18,2),
    interest_rate DECIMAL(6,4),
    loan_to_value DECIMAL(5,2),
    risk_flag INT,

    avg_yield FLOAT,
    avg_rainfall FLOAT,
    avg_temp FLOAT,
    drought_years INT,
    years_observed INT,

    weather_risk INT,
    yield_risk INT,

    -- NEW FEATURES
    ltv_norm FLOAT,
    rate_norm FLOAT,
    yield_norm FLOAT,
    drought_ratio FLOAT,
    drought_norm FLOAT,

    risk_score FLOAT,
    risk_category VARCHAR(20)
);

IF OBJECT_ID('dim_crop', 'U') IS NOT NULL DROP TABLE dim_crop;
CREATE TABLE dim_crop (
    crop_id INT IDENTITY(1,1) PRIMARY KEY,
    crop_type VARCHAR(50) UNIQUE
);

IF OBJECT_ID('dim_region', 'U') IS NOT NULL DROP TABLE dim_region;
CREATE TABLE dim_region (
    region_id INT IDENTITY(1,1) PRIMARY KEY,
    state VARCHAR(10) UNIQUE
);

