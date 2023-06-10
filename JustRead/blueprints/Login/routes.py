from flask import render_template, redirect, request, Blueprint
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from JustRead.models import User
from JustRead.queries import get_user_by_user_name
from JustRead.utils.choices import UserTypeChoices
from JustRead.forms import UserLoginForm, UserSignupForm

login_manager = LoginManager()

Login = Blueprint('Login', __name__)

@login_manager.user_loader
def load_user(user_id):
    # Implement the logic to load the user from your database
    # Return the user object if found, or None if not found
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    # Handle unauthorized access
    return redirect('/login')  # Replace with your desired URL for unauthorized users


@Login.route("/")
@Login.route("/home")
def home():
    return render_template('pages/index.html')


@Login.route("/about")
def about():
    return render_template('pages/about.html')


@Login.route("/style-guide")
def style_guide():
    return render_template('pages/style-guide.html')


@Login.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/home')
    form = UserLoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = get_user_by_user_name(form.user_name.data)
            if user and user['password'] == form.password.data:
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect('/home')
    return render_template('pages/login.html', form=form)


@Login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')  # Replace with your desired URL after logout

# Initialize and register the login_manager with your Flask application
def init_app(app):
    login_manager.init_app(app)

