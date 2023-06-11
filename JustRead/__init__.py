import os
import psycopg2
from flask import Flask
from flask_login import LoginManager, UserMixin
from psycopg2.extras import RealDictCursor
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from JustRead.utils.choices import df

conn_params = {
    'host': 'localhost',
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD')
}

conn = psycopg2.connect(**conn_params)
with conn.cursor() as cur:
    # Run users.sql
    with open('utils/users.sql') as db_file:
        cur.execute(db_file.read())
    # Run Books.sql
    with open('utils/Books.sql') as db_file:
        cur.execute(db_file.read())

    # Import all Books from the dataset
    all_books = df[['title', 'authors', 'categories', 'thumbnail', 'description',
                    'published_year', 'average_rating', 'num_pages', 'ratings_count']].to_records(index=False)
    all_books = [tuple(map(lambda x: x.item() if isinstance(x, np.int64) else x, book)) for book in all_books]
    args_str = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", book).decode('utf-8') for book in all_books)
    cur.execute("INSERT INTO Books (title, authors, categories, thumbnail, description, published_year, average_rating, num_pages, ratings_count) VALUES " + args_str)

    # Dummy Book 1 sells all book
    for_sales = [(1, i) for i in range(1, len(all_books) + 1)]
    args_str = ','.join(cur.mogrify("(%s, %s)", sale).decode('utf-8') for sale in for_sales)
    cur.execute("INSERT INTO BooksForSale (bookstore_pk, books_pk) VALUES " + args_str)

    conn.commit()

db_cursor = conn.cursor(cursor_factory=RealDictCursor)

login_manager = LoginManager(app)
login_manager.login_view = 'Login.login'  # Replace with the correct blueprint name and route for the login view
login_manager.login_message_category = 'info'

# Define the User class
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Load user function
@login_manager.user_loader
def load_user(user_id):
    # Logic to load user from the database based on the user_id
    # Create a User object and return it
    return User(user_id)

from JustRead.blueprints.Login.routes import Login
from JustRead.blueprints.Books.routes import Books

app.register_blueprint(Login)
app.register_blueprint(Books)
