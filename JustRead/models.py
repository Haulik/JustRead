from flask_login import UserMixin
from psycopg2 import sql
from typing import Dict
from JustRead import login_manager, db_cursor, conn, app


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


class Order:
    def __init__(self, oid, address, date, user_id):
        self.oid = oid
        self.address = address
        self.date = date
        self.user_id = user_id
        self.user = None
        # Additional attributes specific to Order


class Book(ModelMixin):
    def __init__(self, book_data: Dict):
        self.pk = book_data.get('book_pk')
        self.title = book_data.get('title')
        self.authors = book_data.get('authors')
        self.categories = book_data.get('categories')
        self.thumbnail = book_data.get('thumbnail')
        self.description = book_data.get('description')
        self.published_year = book_data.get('published_year')
        self.average_rating = book_data.get('average_rating')
        self.num_pages = book_data.get('num_pages')
        self.ratings_count = book_data.get('ratings_count')
        # From JOIN w/ Sell relation
        self.available = book_data.get('available')
        self.book_pk = book_data.get('book_pk')
        self.bookstore_name = book_data.get('bookstore_name')
        self.bookstore_pk = book_data.get('bookstore_pk')
        # Additional attributes specific to Book


class Author:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        # Additional attributes specific to Author


class Booksforsale(ModelMixin):
    def __init__(self, booksforsale_data: Dict):
        self.available = booksforsale_data.get('available')
        self.bookstore_pk = booksforsale_data.get('bookstore_pk')
        self.books_pk = booksforsale_data.get('books_pk')
        
class BookOrder(object):
    def __init__(self, book_order_data: Dict):
        self.pk = book_order_data.get('pk')
        self.customer_pk = book_order_data.get('customer_pk')
        self.bookstore_pk = book_order_data.get('bookstore_pk')
        self.book_pk = book_order_data.get('book_pk')
        
class BookOrder2(object):
    def __init__(self, book_order_data: Dict):
        self.pk = book_order_data.get('pk')
        self.customer_pk = book_order_data.get('customer_pk')
        self.bookstore_pk = book_order_data.get('bookstore_pk')
        self.book_pk = book_order_data.get('book_pk')
        
        self.created_at = book_order_data.get('created_at')
        self.pk = book_order_data.get('pk')
        self.title = book_order_data.get('title')
        self.authors = book_order_data.get('authors')
        self.categories = book_order_data.get('categories')
        self.thumbnail = book_order_data.get('thumbnail')
        self.description = book_order_data.get('description')
        self.published_year = book_order_data.get('published_year')
        self.average_rating = book_order_data.get('average_rating')
        self.num_pages = book_order_data.get('num_pages')
        self.ratings_count = book_order_data.get('booratings_countk_pk')
        
