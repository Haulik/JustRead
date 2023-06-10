from JustRead import db_cursor, conn
from JustRead.models import User, BookStore, Customer, Courier, PublishingHouse, Order, Book, Author


def get_user_by_user_name(user_name):
    sql = """
    SELECT * FROM Users
    WHERE user_name = %s
    """
    db_cursor.execute(sql, (user_name,))
    user = User(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return user



# def insert_sell(sell: Sell):
#     sql = """
#     INSERT INTO Sell(farmer_pk, produce_pk)
#     VALUES (%s, %s)
#     """
#     db_cursor.execute(sql, (sell.farmer_pk, sell.produce_pk,))
#     conn.commit()


def get_books_by_filters(category=None, title=None, author=None, year=None, rating=None, user_id=None):
    sql = """
    SELECT * FROM books
    WHERE
    """
    conditionals = []
    if category:
        conditionals.append(f"categories = '{category}'")
    if title:
        conditionals.append(f"title = '{title}'")
    if author:
        conditionals.append(f"author = '{author}'")
    if year:
        conditionals.append(f"published_year = {year}")
    if rating:
        conditionals.append(f"average_rating >= {rating}")
    if user_id:
        conditionals.append(f"user_id = {user_id}")

    args_str = ' AND '.join(conditionals)
    order = " ORDER BY published_year"
    query = sql + args_str + order

    books = Book.query.filter_by(user_id=user_id).all() if user_id else Book.query.all()
    return books


