create extension azure_ai




select azure_ai.set_setting('azure_openai.endpoint', 'https://foundryhubmain.openai.azure.com/'); 
select azure_ai.set_setting('azure_openai.subscription_key', '');

WITH params AS (
  SELECT
    azure_openai
      .create_embeddings('text-embedding-ada-002', 'trigonometry')
    ::vector(1536) AS qvec
)
SELECT
  b.book_id,
  b.title,
  b.desc_embedding <-> params.qvec AS distance
FROM books AS b
CROSS JOIN params
ORDER BY distance
LIMIT 5;

