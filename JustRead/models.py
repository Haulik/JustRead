from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

from sqlalchemy.ext.declarative import declared_attr

class UserMixin(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True)
    full_name = Column(String(50))
    password = Column(String(120))
    address = Column(String(200))

    @declared_attr
    def bookstore_id(cls):
        return Column(Integer, ForeignKey('bookstore.id'))

    @declared_attr
    def bookstore(cls):
        return relationship('BookStore', back_populates='users')


class User(UserMixin):
    __tablename__ = 'users'

    # Define additional columns specific to User


class Customer(User):
    __tablename__ = 'customers'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    # Additional columns specific to Customer

    # Define the relationship with User
    user = relationship('User', back_populates='customer', uselist=False)

    # Define the relationship with Bookstore and specify the foreign key columns
    bookstore = relationship('BookStore', back_populates='customer', uselist=False, foreign_keys='BookStore.customer_id')


class BookStore(User):
    __tablename__ = 'bookstore'

    id = Column(Integer, primary_key=True)
    # Additional columns specific to BookStore

    # Define the relationship with User
    users = relationship('User', back_populates='bookstore')


class Courier(User):
    __tablename__ = 'courier'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    # Additional columns specific to Courier

    # Define the relationship with User
    user = relationship('User', back_populates='courier', uselist=False)


class PublishingHouse(Base):
    __tablename__ = 'publishing_house'

    pid = Column(Integer, primary_key=True)
    name = Column(String(30))


class Order(Base):
    __tablename__ = 'orders'

    oid = Column(Integer, primary_key=True)
    address = Column(String(30))
    date = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    # Additional columns specific to Order


class Book(Base):
    __tablename__ = 'books'

    isbn13 = Column(String(13), primary_key=True)
    title = Column(String(30))
    subtitle = Column(String(30))
    categories = Column(String(30))
    thumbnail = Column(String(30))
    description = Column(String)
    published_year = Column(Integer)
    average_rating = Column(Float)
    num_pages = Column(Integer)
    ratings_count = Column(Integer)
    # Additional columns specific to Book


class Author(Base):
    __tablename__ = 'authors'

    pid = Column(Integer, primary_key=True)
    name = Column(String(30))
    # Additional columns specific to Author
