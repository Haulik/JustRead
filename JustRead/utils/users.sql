DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE IF NOT EXISTS Users (
    pk serial NOT NULL PRIMARY KEY,
    user_name varchar(50) UNIQUE,
    full_name varchar(50),
    password varchar(120),
    address varchar(200)
);

DELETE FROM Users;

DROP TABLE IF EXISTS BookStore CASCADE;

CREATE TABLE IF NOT EXISTS BookStore(
    pk int PRIMARY KEY REFERENCES Users(pk)
);

DELETE FROM BookStore;

INSERT INTO Users (user_name, full_name, password, address)
VALUES ('Bookstore1', 'Saxo', 'pass', 'Universitetsparken 34');

INSERT INTO BookStore (pk)
VALUES (currval('users_pk_seq'));

DROP TABLE IF EXISTS Customers CASCADE;

CREATE TABLE IF NOT EXISTS Customers(
    pk int PRIMARY KEY REFERENCES Users(pk)
);

DELETE FROM Customers;

INSERT INTO Users (user_name, full_name, password, address)
VALUES ('customer', 'Customer', 'pass', 'Nørre alle 63');

INSERT INTO Customers (pk)
VALUES (currval('users_pk_seq'));

DROP TABLE IF EXISTS Courier CASCADE;

CREATE TABLE IF NOT EXISTS Courier(
    pk int PRIMARY KEY REFERENCES Users(pk)
);

DELETE FROM Courier;

INSERT INTO Users (user_name, full_name, password, address)
VALUES ('courier', 'Courier', 'pass', 'Nørre alle 34');

INSERT INTO Courier (pk)
VALUES (currval('users_pk_seq'));
