SELECT TOP 10
    f.loan_id,
    f.loan_amount,
    f.risk_score,
    f.risk_category,
    c.crop_type,
    r.state
FROM fact_loans f
JOIN dim_crop c ON f.crop_id = c.crop_id
JOIN dim_region r ON f.region_id = r.region_id
ORDER BY f.risk_score DESC;