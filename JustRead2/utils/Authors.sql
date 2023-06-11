DROP TABLE IF EXISTS Authors CASCADE;

CREATE TABLE IF NOT EXISTS Authors(
    Pid serial unique not null PRIMARY KEY,
    name varchar(30)
);

DELETE FROM Authors;

--CREATE INDEX IF NOT EXISTS produce_index
--ON Produce (category, item, variety);



