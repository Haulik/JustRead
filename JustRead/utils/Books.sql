DROP TABLE IF EXISTS Books CASCADE;

CREATE TABLE IF NOT EXISTS Books(
    pk serial not null PRIMARY KEY,
    title VARCHAR(1000),
    authors VARCHAR(1000),
    categories VARCHAR(1000),
    thumbnail VARCHAR(1000),
    description VARCHAR(2000),
    published_year INT,
    average_rating FLOAT,
    num_pages INT,
    ratings_count INT
);

DELETE FROM Books;


DROP TABLE IF EXISTS BooksForSale;

CREATE TABLE IF NOT EXISTS BooksForSale(
    bookstore_pk int not null REFERENCES BookStore(pk) ON DELETE CASCADE,
    books_pk int not null REFERENCES Books(pk) ON DELETE CASCADE,
    available boolean default true,
    PRIMARY KEY (bookstore_pk, books_pk)
);

CREATE INDEX IF NOT EXISTS BooksForSale_index
ON BooksForSale (bookstore_pk, available);

DELETE FROM BooksForSale;


--CREATE INDEX IF NOT EXISTS produce_index
--ON Produce (category, item, variety);



