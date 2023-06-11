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


DROP TABLE IF EXISTS Sell;

CREATE TABLE IF NOT EXISTS Sell(
    bookstore_pk int not null REFERENCES BookStore(pk) ON DELETE CASCADE,
    books_pk int not null REFERENCES Books(pk) ON DELETE CASCADE,
    available boolean default true,
    PRIMARY KEY (bookstore_pk, books_pk)
);

CREATE INDEX IF NOT EXISTS sell_index
ON Sell (bookstore_pk, available);

DELETE FROM Sell;


--CREATE INDEX IF NOT EXISTS produce_index
--ON Produce (category, item, variety);


DROP TABLE IF EXISTS BookOrder;

CREATE TABLE IF NOT EXISTS BookOrder(
    pk serial not null PRIMARY KEY,
    customer_pk int not null REFERENCES Customers(pk) ON DELETE CASCADE,
    bookstore_pk int not null REFERENCES BookStore(pk) ON DELETE CASCADE,
    book_pk int not null REFERENCES Books(pk) ON DELETE CASCADE,
    created_at timestamp not null default current_timestamp
);

DELETE FROM BookOrder;


CREATE OR REPLACE VIEW vw_books
AS
SELECT b.title, b.authors, b.categories, b.thumbnail,
       b.description, b.published_year, b.average_rating,
       b.num_pages, b.ratings_count, s.available,
       b.pk as book_pk, bs.full_name as bookstore_name,
       bs.pk as bookstore_pk
FROM Books b
JOIN Sell s ON s.books_pk = b.pk
JOIN BookStore bs ON s.bookstore_pk = bs.pk
ORDER BY available, b.pk;




