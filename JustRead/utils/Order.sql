DROP TABLE IF EXISTS Order CASCADE;

CREATE TABLE IF NOT EXISTS Order(
    Oid serial unique not null PRIMARY KEY,
    address varchar(30)
    date varchar(50)
    id int
);

DELETE FROM Order;

--CREATE INDEX IF NOT EXISTS produce_index
--ON Produce (category, item, variety);



