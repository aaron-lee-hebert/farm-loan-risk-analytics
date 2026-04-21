USE FarmRiskDB;

INSERT INTO dim_crop (crop_type)
SELECT DISTINCT crop_type FROM staging_loans;

INSERT INTO dim_region (state)
SELECT DISTINCT state FROM staging_loans;