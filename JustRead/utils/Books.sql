DROP TABLE IF EXISTS Books CASCADE;

CREATE TABLE IF NOT EXISTS Books(
    isbn13 unique not null PRIMARY KEY,
    title varchar(30),
    subtitle varchar(30),
    --authors varchar(50),
    categories varchar(30),
    thumbnail varchar(30),
    description varchar(MAX),
    published_year int,
    average_rating float,
    num_pages int,
    ratings_count int
);

DELETE FROM Books;

--CREATE INDEX IF NOT EXISTS produce_index
--ON Produce (category, item, variety);



