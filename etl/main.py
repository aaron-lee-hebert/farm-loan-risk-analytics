import subprocess
import pandas as pd
from sqlalchemy import create_engine
from db_utils import get_engine, run_sql_file

# Step 1: Generate synthetic data
print("Generating loan data...")
subprocess.run(["python", "etl/generate_loan.py"], check=True)

# Step 2: Transform data
print("Transforming data...")
subprocess.run(["python", "etl/transform_data.py"], check=True)

# Step 3: Setup database + tables
print("Creating database and tables...")
engine = get_engine()

run_sql_file(engine, "etl/sql/create_tables.sql")

# Step 4: Load into staging
print("Loading into staging table...")

df = pd.read_csv("data/processed/loans_enriched.csv")
df.to_sql("staging_loans", engine, if_exists="append", index=False)

# Step 5: Build dimensions
print("Building dimension tables...")
run_sql_file(engine, "etl/sql/load_dimensions.sql")

# Step 6: Build fact table
print("Building fact table...")
run_sql_file(engine, "etl/sql/load_facts.sql")

print("\nETL pipeline complete!")