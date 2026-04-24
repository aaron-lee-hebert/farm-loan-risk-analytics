SELECT 
    c.crop_type,
    SUM(f.loan_amount) AS total_loan_exposure,
    100.0 * SUM(f.loan_amount) / SUM(SUM(f.loan_amount)) OVER () AS pct_of_portfolio
FROM fact_loans f
JOIN dim_crop c ON f.crop_id = c.crop_id
GROUP BY c.crop_type
ORDER BY pct_of_portfolio DESC;