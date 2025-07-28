drop table if exists dbo.MovieQuotes
go

create table dbo.MovieQuotes
(
id int identity(1,1),
quote nvarchar(max),
movie nvarchar(max),
year_released char(4),
embedding vector(1536),
constraint pk_quotes primary key clustered (id)
)
go
