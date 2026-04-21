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

    risk_score FLOAT,
    risk_category VARCHAR(20)
);