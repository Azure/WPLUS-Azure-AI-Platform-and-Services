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


def create_SQLMasterKey():
    """
    Creates a master key in the SQL database.
    """
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pwd};"
    )
    cursor = conn.cursor()
    sql = """
IF NOT EXISTS (
        SELECT 1
        FROM   sys.symmetric_keys
        WHERE  name = '##MS_DatabaseMasterKey##'     
)
BEGIN
    PRINT N'Creating database master key…';
  
    /* 1.  Create the master key, encrypted by a strong password                       */
    CREATE MASTER KEY;
END


"""
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()



def create_database_credential():
    """
    Creates a database scoped credential for Azure OpenAI.
    """
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pwd};"
    )
    cursor = conn.cursor()
    sql = (
        f"CREATE DATABASE SCOPED CREDENTIAL [{endpoint}] "
        f"WITH IDENTITY = 'HTTPEndpointHeaders', "
        f"SECRET = '{{\"api-key\": \"{api_key}\"}}';"
    )
    print(sql)
    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()


def create_embedding_procedure():
    """
    Creates a stored procedure to get embeddings from Azure OpenAI.
    """
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={sql_server};"
        f"DATABASE={sql_database};"
        f"UID={sql_user};"
        f"PWD={sql_pwd};"
    )
    cursor = conn.cursor()
    
    url = f"{endpoint.rstrip('/')}/openai/deployments/{deployment}/embeddings?api-version=2024-02-01"
    credential = f"[{endpoint.rstrip('/')}]"

    sql = """
    CREATE OR ALTER PROCEDURE [dbo].[get_embedding]
    @inputText NVARCHAR(MAX),
    @embedding VECTOR(1536) OUTPUT
    AS
    BEGIN
        DECLARE @retval INT;
        DECLARE @payload NVARCHAR(MAX) = JSON_OBJECT('input': @inputText);
        DECLARE @response NVARCHAR(MAX);

        EXEC @retval = sp_invoke_external_rest_endpoint
            @url = ' """ + url + """',
            @method = 'POST',
            @credential = """ + credential + """,
            @payload = @payload,
            @response = @response OUTPUT;

        SET @embedding = JSON_QUERY(@response, '$.result.data[0].embedding');

        RETURN @retval;
    END;
    """
    print(sql)

    cursor.execute(sql)
    conn.commit()
    
    cursor.close()
    conn.close()

def main():
    create_SQLMasterKey()
    create_database_credential()
    create_embedding_procedure()

if __name__ == "__main__":
    main()