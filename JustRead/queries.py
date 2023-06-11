from JustRead import db_cursor, conn
from JustRead.models import User, BookStore, Customer, Courier, PublishingHouse, Order, Book, Author, BookOrder, BookOrder2


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

def get_orders_by_customer_pk(pk):
    sql = """
    SELECT * FROM BookOrder po
    JOIN books p ON p.pk = po.book_pk
    WHERE customer_pk = %s
    """
    db_cursor.execute(sql, (pk,))
    orders = [BookOrder2(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return orders

def get_books_by_filters():
    sql = """
    SELECT * FROM vw_books
    WHERE available != false
    """
    

    db_cursor.execute(sql)
    book = [Book(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return book


def get_customer_by_pk(pk):
    sql = """
    SELECT * FROM Customers
    WHERE pk = %s
    """
    db_cursor.execute(sql, (pk,))
    customer = Customer(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return customer


def get_book_by_pk(pk):
    sql = """
    SELECT book_pk as pk, * FROM vw_books
    WHERE book_pk = %s
    """
    db_cursor.execute(sql, (pk,))
    books = Book(db_cursor.fetchone()) if db_cursor.rowcount > 0 else None
    return books



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
    
def insert_book_order(order: BookOrder):
    sql = """
    INSERT INTO BookOrder(book_pk, bookstore_pk, customer_pk)
    VALUES (%s, %s, %s)
    """
    db_cursor.execute(sql, (
        order.book_pk,
        order.bookstore_pk,
        order.customer_pk,
    ))
    conn.commit()
    
    
    
def get_all_produce():
    sql = """
    SELECT *
    FROM books
    """
    db_cursor.execute(sql)
    books = [Book(res) for res in db_cursor.fetchall()] if db_cursor.rowcount > 0 else []
    return books



# UPDATE QUERIES
def update_book_availability(available, book_pk, bookstore_pk):
    sql = """
    UPDATE BooksForSale
    SET available = %s
    WHERE books_pk = %s
    AND bookstore_pk = %s
    """
    db_cursor.execute(sql, (available, book_pk, bookstore_pk))
    conn.commit()
