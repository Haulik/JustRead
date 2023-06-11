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


def get_books_by_filters():
    sql = """
    SELECT * FROM books
    """
    

    db_cursor.execute(sql)
    produce = [Book(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return produce



# INSERT QUERIES
def insert_user(user: User):
    sql = """
    INSERT INTO Users(user_name, full_name, password, address)
    VALUES (%s, %s, %s, %s)
    """
    db_cursor.execute(sql, (user.user_name, user.full_name, user.password, user.address))
    conn.commit()


def insert_bookStore(bookStore: BookStore):
    sql = """
    INSERT INTO bookStore(user_name, full_name, password, address)
    VALUES (%s, %s, %s, %s)
    """
    db_cursor.execute(sql, (bookStore.user_name, bookStore.full_name, bookStore.password, bookStore.address))
    conn.commit()


def insert_customer(customer: Customer):
    sql = """
    INSERT INTO Customers(user_name, full_name, password, address)
    VALUES (%s, %s, %s, %s)
    """
    db_cursor.execute(sql, (customer.user_name, customer.full_name, customer.password, customer.address))
    conn.commit()

def insert_courier(courier: Courier):
    sql = """
    INSERT INTO Courier(user_name, full_name, password, address)
    VALUES (%s, %s, %s, %s)
    """
    db_cursor.execute(sql, (courier.user_name, courier.full_name, courier.password, courier.address))
    conn.commit()
    
    
    
def get_all_produce():
    sql = """
    SELECT *
    FROM books
    """
    db_cursor.execute(sql)
    books = [Book(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return books
