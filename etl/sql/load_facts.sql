USE FarmRiskDB;

INSERT INTO fact_loans (
    loan_id,
    farm_id,
    crop_id,
    region_id,
    loan_amount,
    interest_rate,
    loan_to_value,
    risk_score,
    risk_category
)
SELECT
    s.loan_id,
    s.farm_id,
    c.crop_id,
    r.region_id,
    s.loan_amount,
    s.interest_rate,
    s.loan_to_value,
    s.risk_score,
    s.risk_category
FROM staging_loans s
JOIN dim_crop c ON s.crop_type = c.crop_type
JOIN dim_region r ON s.state = r.state;