from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), unique=True)
    full_name = Column(String(50))
    password = Column(String(120))
    address = Column(String(200))
    # Foreign key relationship to BookStore
    bookstore_id = Column(Integer, ForeignKey('bookstore.id'))
    bookstore = relationship('BookStore', back_populates='user')
    # Foreign key relationship to Customer
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='user')
    # Foreign key relationship to Courier
    courier_id = Column(Integer, ForeignKey('courier.id'))
    courier = relationship('Courier', back_populates='user')


class BookStore(User):
    __tablename__ = 'bookstore'

    id = Column(Integer, primary_key=True)
    # Additional columns specific to BookStore


class Customer(User):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    # Additional columns specific to Customer


class Courier(User):
    __tablename__ = 'courier'

    id = Column(Integer, primary_key=True)
    # Additional columns specific to Courier


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
