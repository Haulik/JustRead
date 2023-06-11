DROP TABLE IF EXISTS Books CASCADE;

CREATE TABLE IF NOT EXISTS Books(
    isbn13 varchar(20) PRIMARY KEY,
    title varchar(1000),
    authors varchar(1000),
    categories varchar(1000),
    thumbnail varchar(1000),
    description varchar(2000),
    published_year int,
    average_rating float,
    num_pages int,
    ratings_count int
);

DELETE FROM Books;



