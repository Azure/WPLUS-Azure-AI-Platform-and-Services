import pyodbc
import json
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_user = os.getenv("SQL_USER")
sql_pwd = os.getenv("SQL_PWD")

client = AzureOpenAI(
    api_version="2023-05-15",
    azure_endpoint=endpoint,
    api_key=api_key
)

def get_embedding(text: str) :
    """
    Returns the embedding vector for `text` using the specified embedding engine.
    """
    resp = client.embeddings.create(model=deployment, input=text)
    # resp.data is a list; we take the first item's .embedding
    return resp.data[0].embedding



# Configure your connection string
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={sql_server};"
    f"DATABASE={sql_database};"
    f"UID={sql_user};"
    f"PWD={sql_pwd};"
)
cursor = conn.cursor()

# Make sure your Quotes table has an 'embedding' column of a suitable type (e.g. NVARCHAR(MAX))
cursor.execute("SELECT id, quote FROM MovieQuotes;")
rows = cursor.fetchall()

for quote_id, quote_text in rows:
    # call your existing function
    embedding = get_embedding(quote_text)  # returns a list of floats
    
    # serialize to JSON for storage; adjust if you store differently
    embedding_json = json.dumps(embedding)
    
    _ = cursor.execute(
        "UPDATE MovieQuotes SET embedding = CAST(CAST(? AS NVARCHAR(MAX)) AS VECTOR(1536)) WHERE id = ?;",
        embedding_json,
        quote_id
    )
    conn.commit()

cursor.close()
conn.close()

print("Embeddings updated for all quotes.")
