import csv
import os
from pathlib import Path

import pyodbc
from dotenv import load_dotenv

load_dotenv("../../.env")

sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_user = os.getenv("SQL_USER")
sql_pwd = os.getenv("SQL_PWD")
csv_path = os.getenv("CSV_PATH")
batch_size_value = os.getenv("BATCH_SIZE", "1000")

required_config = {
    "SQL_SERVER": sql_server,
    "SQL_DATABASE": sql_database,
    "SQL_USER": sql_user,
    "SQL_PWD": sql_pwd,
    "CSV_PATH": csv_path,
}
missing_config = [name for name, value in required_config.items() if not value]
if missing_config:
    raise ValueError(f"Missing required configuration: {', '.join(missing_config)}")

csv_file = Path(csv_path)
if not csv_file.is_file():
    raise FileNotFoundError(f"CSV_PATH does not point to a file: {csv_file}")

try:
    batch_size = int(batch_size_value)
except ValueError as error:
    raise ValueError(f"BATCH_SIZE must be an integer, got: {batch_size_value}") from error

# 1) Connect
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={sql_server};"
    f"DATABASE={sql_database};"
    f"UID={sql_user};"
    f"PWD={sql_pwd};"
)
cursor = conn.cursor()
cursor.fast_executemany = True

try:
    with csv_file.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        data_cols = headers[0:]
        placeholders = ",".join("?" for _ in data_cols)
        sql = (
            f"INSERT INTO dbo.MovieQuotes ({','.join(data_cols)}) "
            f"VALUES ({placeholders})"
        )

        batch = []
        for row in reader:
            batch.append(row[0:])
            if len(batch) >= batch_size:
                cursor.executemany(sql, batch)
                batch.clear()

        if batch:
            cursor.executemany(sql, batch)

    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    cursor.close()
    conn.close()
