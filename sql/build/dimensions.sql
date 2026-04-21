CREATE TABLE dim_crop (
    crop_id INT IDENTITY(1,1) PRIMARY KEY,
    crop_type VARCHAR(50) UNIQUE
);

CREATE TABLE dim_region (
    region_id INT IDENTITY(1,1) PRIMARY KEY,
    state VARCHAR(10) UNIQUE
);

CREATE TABLE dim_time (
    time_id INT IDENTITY(1,1) PRIMARY KEY,
    year INT UNIQUE
);