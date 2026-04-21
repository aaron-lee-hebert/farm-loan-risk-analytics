SELECT 
    r.state,
    AVG(f.risk_score) AS avg_risk_score,
    COUNT(*) AS loan_count
FROM fact_loans f
JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.state
ORDER BY avg_risk_score DESC;