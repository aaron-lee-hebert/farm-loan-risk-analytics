CREATE TABLE fact_loans (
    loan_id INT PRIMARY KEY,
    farm_id VARCHAR(100),

    crop_id INT,
    region_id INT,
    time_id INT,

    loan_amount DECIMAL(18,2),
    interest_rate DECIMAL(6,4),
    loan_to_value DECIMAL(5,2),

    risk_score FLOAT,
    risk_category VARCHAR(20),

    FOREIGN KEY (crop_id) REFERENCES dim_crop(crop_id),
    FOREIGN KEY (region_id) REFERENCES dim_region(region_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);