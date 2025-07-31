import csv
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
sql_server= os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_user = os.getenv("SQL_USER")
sql_pwd = os.getenv("SQL_PWD")  
csv_path = os.getenv("CSV_PATH")
batch_size = int(os.getenv("BATCH_SIZE", 1000))  # Default to 1000 if not set

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
    with open(csv_path, newline="", encoding="utf-8") as f:
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
    cursor.close()
    conn.close()
except Exception as e:
    print(f"An error occurred: {e} -- {sql}")
