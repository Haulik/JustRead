from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

from JustRead.queries import get_user_by_user_name

from JustRead.utils.choices import UserTypeChoices

class FilterBookForm(FlaskForm):
    category = SelectField('Category')
    title = StringField('Title')
    author = StringField('Author')
    submit = SubmitField('Filter')

class AddBookForm(FlaskForm):
    isbn13 = StringField('ISBN-13', validators=[DataRequired(), Length(max=20)])
    title = StringField('Title', validators=[DataRequired(), Length(max=1000)])
    authors = StringField('Authors', validators=[DataRequired(), Length(max=1000)])
    categories = StringField('Categories', validators=[DataRequired(), Length(max=1000)])
    thumbnail = StringField('Thumbnail', validators=[DataRequired(), Length(max=1000)])
    description = StringField('Description', validators=[DataRequired(), Length(max=2000)])
    published_year = StringField('Published Year', validators=[DataRequired()])
    average_rating = FloatField('Average Rating', validators=[DataRequired(), NumberRange(min=0, max=5)])
    num_pages = StringField('Number of Pages', validators=[DataRequired()])
    ratings_count = StringField('Ratings Count', validators=[DataRequired()])
    submit = SubmitField('Add Book')

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