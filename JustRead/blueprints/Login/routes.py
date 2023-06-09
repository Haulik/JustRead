from flask import render_template, redirect, request, Blueprint
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from JustRead.models import User, BookStore, Customer, Courier
from JustRead.queries import get_user_by_user_name, insert_bookStore, insert_customer, insert_courier
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
            if user and user.check_password(form.password.data):
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect('/home')
    return render_template('pages/login.html', form=form)

@Login.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect('/home')
    form = UserSignupForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user_data = dict(full_name=form.full_name.data,
                             user_name=form.user_name.data,
                             password=form.password.data)
            if form.user_type.data == UserTypeChoices.values()[0]:
                farmer = BookStore(user_data)
                insert_bookStore(farmer)
            elif form.user_type.data == UserTypeChoices.values()[1]:
                customer = Customer(form.data)
                insert_customer(customer)
            elif form.user_type.data == UserTypeChoices.values()[2]:
                courier = Courier(form.data)
                insert_courier(courier)
            user = get_user_by_user_name(form.user_name.data)
            if user:
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect('/home')
    return render_template('pages/signup.html', form=form)

@Login.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')  # Replace with your desired URL after logout

# Initialize and register the login_manager with your Flask application
def init_app(app):
    login_manager.init_app(app)

