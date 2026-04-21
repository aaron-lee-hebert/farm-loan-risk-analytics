import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mssql+pyodbc://@localhost\\SQL/FarmRiskDB?driver=ODBC+Driver+17+for+SQL+Server")
df = pd.read_csv("data/processed/loans_enriched.csv")
df.to_sql("staging_loans", engine, if_exists="replace", index=False)

print("Loaded into staging_loans")