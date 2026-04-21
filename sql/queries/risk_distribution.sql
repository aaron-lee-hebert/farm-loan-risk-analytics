SELECT 
    risk_category,
    COUNT(*) AS loan_count,
    SUM(loan_amount) AS total_exposure
FROM fact_loans
GROUP BY risk_category
ORDER BY total_exposure DESC;