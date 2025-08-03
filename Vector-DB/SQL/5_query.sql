
declare @x nvarchar(max) = 'texas city'
declare @retval int, @embedding vector(1536)
exec @retval = dbo.get_embedding  @x, @embedding output;
select @embedding

select top(10)
*,
vector_distance('cosine',@embedding, embedding) as dist
from MovieQuotes
order by dist asc
