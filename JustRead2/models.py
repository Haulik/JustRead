from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from psycopg2 import sql
from typing import Dict
from JustRead2 import login_manager, db_cursor, conn, app


Base = declarative_base()

from sqlalchemy.ext.declarative import declared_attr

@login_manager.user_loader
def load_user(user_id):
    user_sql = sql.SQL("""
    SELECT * FROM Users
    WHERE pk = %s
    """).format(sql.Identifier('pk'))

    db_cursor.execute(user_sql, (int(user_id),))
    return User(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None



class ModelUserMixin(UserMixin):
    @property
    def id(self):
        return self.pk


class ModelMixin:
    pass


class User(ModelUserMixin, ModelMixin):
    def __init__(self, user_data: Dict):
        self.pk = user_data.get('pk')
        self.full_name = user_data.get('full_name')
        self.user_name = user_data.get('user_name')
        self.password = user_data.get('password')
        self.address = user_data.get('address')
        
    def check_password(self, password):
        return password == self.password


class BookStore(User):
    def __init__(self, user_data: Dict):
        super().__init__(user_data)


class Courier(User):
    def __init__(self, user_data: Dict):
        super().__init__(user_data)


class PublishingHouse(User):
    pass

class Customer(User):
    def __init__(self, user_data: Dict):
        super().__init__(user_data)



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
