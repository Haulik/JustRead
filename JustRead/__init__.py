import os
import psycopg2
from flask import Flask
from flask_login import LoginManager, UserMixin
from psycopg2.extras import RealDictCursor
from JustRead.utils.choices import df

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

conn_params = {
    'host': 'localhost',
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD')
}

conn = psycopg2.connect(**conn_params)
with conn.cursor() as cur:
        # Run users.sql
        with open('users.sql') as db_file:
            cur.execute(db_file.read())
        # Run Books.sql
        with open('Books.sql') as db_file:
            cur.execute(db_file.read())

        # Import all Books from the dataset
        all_books = list(
            map(lambda x: tuple(x),
                df[['isbn13', 'title', 'authors', 'categories', 'thumbnail', 'description',
                    'published_year', 'average_rating', 'num_pages', 'ratings_count']].to_records(index=False))
        )
        args_str = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", i).decode('utf-8') for i in all_books)
        cur.execute("INSERT INTO Books (category, item, unit, variety, price) VALUES " + args_str)

        # Dummy farmer 1 sells all produce
        dummy_sales = [(1, i) for i in range(1, len(all_books) + 1)]
        args_str = ','.join(cur.mogrify("(%s, %s)", i).decode('utf-8') for i in dummy_sales)
        cur.execute("INSERT INTO Sell (bookstore_pk, books_pk) VALUES " + args_str)

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

