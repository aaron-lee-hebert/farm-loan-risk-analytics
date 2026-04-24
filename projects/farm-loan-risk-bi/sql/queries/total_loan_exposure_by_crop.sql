SELECT 
    c.crop_type,
    SUM(f.loan_amount) AS total_loan_exposure,
    COUNT(*) AS loan_count,
    AVG(f.loan_amount) AS avg_loan_size
FROM fact_loans f
JOIN dim_crop c ON f.crop_id = c.crop_id
GROUP BY c.crop_type
ORDER BY total_loan_exposure DESC;