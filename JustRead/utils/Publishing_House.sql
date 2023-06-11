DROP TABLE IF EXISTS Publishing_House CASCADE;

CREATE TABLE IF NOT EXISTS Publishing_House(
    Pid serial unique not null PRIMARY KEY,
    name varchar(30)
);

DELETE FROM Publishing_House;

--CREATE INDEX IF NOT EXISTS produce_index
--ON Produce (category, item, variety);


INSERT INTO Publishing_House(name)
VALUES ();