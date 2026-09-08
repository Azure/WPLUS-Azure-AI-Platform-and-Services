IF OBJECT_ID(N'dbo.get_embedding', N'P') IS NULL
BEGIN
	THROW 50000, 'dbo.get_embedding is missing. Run 4_SQLEmbeddings.py before this query.', 1;
END;

declare @x nvarchar(max) = 'texas city'
declare @retval int, @embedding vector(1536)
exec @retval = dbo.get_embedding  @x, @embedding output;

IF @retval <> 0
BEGIN
	THROW 50001, 'dbo.get_embedding failed.', 1;
END;

IF @embedding IS NULL
BEGIN
	THROW 50002, 'dbo.get_embedding returned a null embedding.', 1;
END;

select top(10)
*,
vector_distance('cosine',@embedding, embedding) as dist
from MovieQuotes
order by dist asc
