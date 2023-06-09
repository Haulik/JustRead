from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

from JustRead.queries import get_user_by_user_name, get_customer_by_pk, get_bookstore_by_pk

from JustRead.utils.choices import UserTypeChoices

class FilterBookForm(FlaskForm):
    category = SelectField('Category')
    title = StringField('Title')
    author = StringField('Author')
    submit = SubmitField('Filter')

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=1000)])
    authors = StringField('Authors', validators=[DataRequired(), Length(max=1000)])
    categories = StringField('Categories', validators=[DataRequired(), Length(max=1000)])
    thumbnail = StringField('Thumbnail', validators=[DataRequired(), Length(max=1000)])
    description = StringField('Description', validators=[DataRequired(), Length(max=2000)])
    published_year = IntegerField('Published Year', validators=[DataRequired()])
    average_rating = FloatField('Average Rating', validators=[DataRequired(), NumberRange(min=0, max=5)])
    num_pages = IntegerField('Number of Pages', validators=[DataRequired()])
    ratings_count = IntegerField('Ratings Count', validators=[DataRequired()])
    submit = SubmitField('Add Book')
    
    def validate_submit(self, field):
        bookstore = get_bookstore_by_pk(current_user.pk)
        if not bookstore:
            raise ValidationError("You must be a bookstore in order to create books.")

class UserLoginForm(FlaskForm):
    user_name = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=50)],
                            render_kw=dict(placeholder='Username'))
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw=dict(placeholder='Password'))
    submit = SubmitField('Login')

    def validate_password(self, field):
        user = get_user_by_user_name(self.user_name.data)
        if user is None:
            raise ValidationError(f'User name "{self.user_name.data}" does not exist.')
        if user.password != self.password.data:
            raise ValidationError(f'User name or password are incorrect.')


class UserSignupForm(FlaskForm):
    full_name = StringField('Full name',
                            validators=[DataRequired(), Length(min=2, max=50)],
                            render_kw=dict(placeholder='Full name'))
    user_name = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=50)],
                            render_kw=dict(placeholder='Username'))
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw=dict(placeholder='Password'))
    password_repeat = PasswordField('Repeat Password',
                                    validators=[DataRequired()],
                                    render_kw=dict(placeholder='Password'))
    address = StringField('Address',
                            validators=[DataRequired(), Length(min=2, max=100)],
                            render_kw=dict(placeholder='Address'))
    user_type = SelectField('User type',
                            validators=[DataRequired()],
                            choices=UserTypeChoices.choices())
    submit = SubmitField('Sign up')

    def validate_user_name(self, field):
        user = get_user_by_user_name(self.user_name.data)
        if user:
            raise ValidationError(f'User name "{self.user_name.data}" already in use.')

    def validate_password_repeat(self, field):
        if not self.password.data == self.password_repeat.data:
            raise ValidationError(f'Provided passwords do not match.')
        
class UserLoginForm(FlaskForm):
    user_name = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=50)],
                            render_kw=dict(placeholder='Username', style='color: white'))  # Set placeholder text color to white
    password = PasswordField('Password',
                             validators=[DataRequired()],
                             render_kw=dict(placeholder='Password', style='color: white'))  # Set placeholder text color to white
    submit = SubmitField('Login')

    def validate_password(self, field):
        user = get_user_by_user_name(self.user_name.data)
        if user is None:
            raise ValidationError(f'User name "{self.user_name.data}" does not exist.')
        if user.password != self.password.data:
            raise ValidationError(f'User name or password are incorrect.')
        
        
class BuyBookForm(FlaskForm):
    submit = SubmitField('Yes, buy it')

    def validate_submit(self, field):
        customer = get_customer_by_pk(current_user.pk)
        if not customer:
            raise ValidationError("You must be a customer in order to create orders.")
        
class DeleteBookForm(FlaskForm):
    submit = SubmitField('Yes, delete it')

    def validate_submit(self, field):
        bookstore = get_bookstore_by_pk(current_user.pk)
        if not bookstore:
            raise ValidationError("You must be a bookstore in order to delete a book.")
        
        
class RestockBookForm(FlaskForm):
    submit = SubmitField('Yes, restock it')