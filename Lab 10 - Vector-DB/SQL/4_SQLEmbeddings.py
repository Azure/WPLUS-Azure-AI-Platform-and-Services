import pyodbc
import os
from urllib.parse import urlsplit

from dotenv import load_dotenv

load_dotenv("../../.env")

endpoint = os.getenv("AZURE_OPENAI_EMBEDDING_ADA_ENDPOINT")
deployment = os.getenv("EMBEDDING_ADA_MODEL_DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_EMBEDDING_ADA_API_KEY")
sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_user = os.getenv("SQL_USER")
sql_pwd = os.getenv("SQL_PWD")


def get_base_endpoint(value):
    if not value:
        raise ValueError("AZURE_OPENAI_EMBEDDING_ADA_ENDPOINT is required")

    parsed_endpoint = urlsplit(value)
    if parsed_endpoint.scheme.lower() != "https" or not parsed_endpoint.netloc:
        raise ValueError("AZURE_OPENAI_EMBEDDING_ADA_ENDPOINT must be a valid HTTPS URL")

    base_endpoint = f"https://{parsed_endpoint.netloc}"
    if len(base_endpoint) > 128:
        raise ValueError("The Azure OpenAI base endpoint exceeds SQL's 128-character credential-name limit")

    return base_endpoint


base_endpoint = get_base_endpoint(endpoint)


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
        f"CREATE DATABASE SCOPED CREDENTIAL [{base_endpoint}] "
        f"WITH IDENTITY = 'HTTPEndpointHeaders', "
        f"SECRET = '{{\"api-key\": \"{api_key}\"}}';"
    )
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
    
    url = f"{base_endpoint}/openai/deployments/{deployment}/embeddings?api-version=2024-02-01"
    credential = f"[{base_endpoint}]"

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

        IF @retval <> 0
        BEGIN
            DECLARE @errorMessage NVARCHAR(2048) = CONCAT(
                'Azure OpenAI embedding request failed with HTTP status ', @retval, '.'
            );
            THROW 50001, @errorMessage, 1;
        END;

        SET @embedding = JSON_QUERY(@response, '$.result.data[0].embedding');

        IF @embedding IS NULL
        BEGIN
            THROW 50002, 'Azure OpenAI returned no embedding.', 1;
        END;

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