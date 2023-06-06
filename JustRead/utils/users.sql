DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE IF NOT EXISTS Users(
	id serial not null PRIMARY KEY,
	user_name varchar(50) UNIQUE,
    full_name varchar(50),
	password varchar(120),
    address varchar(200),
);

--CREATE INDEX IF NOT EXISTS users_index
--ON Users (id, user_name);

DELETE FROM Users;

DROP TABLE IF EXISTS BookStore CASCADE;

CREATE TABLE IF NOT EXISTS BookStore(
    PRIMARY KEY(id)
) INHERITS (Users);

--CREATE INDEX IF NOT EXISTS bookstore_index
--ON BookStore (id, user_name);

DELETE FROM BookStore;

INSERT INTO BookStore(user_name, full_name, password, address)
VALUES ('Bookstore1', 'Saxo', 'pass', 'Universitetsparken 34');

DROP TABLE IF EXISTS Customers;

CREATE TABLE IF NOT EXISTS Customers(
    PRIMARY KEY(id)
) INHERITS (Users);

--CREATE INDEX IF NOT EXISTS customers_index
--ON Customers (id, user_name);

DELETE FROM Customers;

INSERT INTO Customers(user_name, full_name, password, address)
VALUES ('customer', 'Customer', 'pass', 'Nørre alle 63');


CREATE TABLE IF NOT EXISTS Courier(
    PRIMARY KEY(id)
) INHERITS (Users);

--CREATE INDEX IF NOT EXISTS customers_index
--ON Customers (id, user_name);

DELETE FROM Courier;

INSERT INTO Courier(user_name, full_name, password, address)
VALUES ('courier', 'Courier', 'pass', 'Nørre alle 34');