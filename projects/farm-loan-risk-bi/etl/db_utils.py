from sqlalchemy import create_engine, text

def get_engine():
    return create_engine(
    "mssql+pyodbc://@localhost\\SQL/master?driver=ODBC+Driver+17+for+SQL+Server"
    )

def run_sql_file(engine, filepath):
    with open(filepath, "r") as f:
        sql = f.read()

    with engine.connect() as conn:
        for statement in sql.split("GO"):
            stmt = statement.strip()
            if stmt:
                conn.execute(text(stmt))
        conn.commit()