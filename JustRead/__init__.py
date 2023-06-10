import os
import psycopg2
from flask import Flask
from flask_login import LoginManager, UserMixin
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

conn_params = {
    'host': 'localhost',
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD')
}

conn = psycopg2.connect(**conn_params)
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

@app.teardown_appcontext
def close_connection(exception=None):
    conn.close()
