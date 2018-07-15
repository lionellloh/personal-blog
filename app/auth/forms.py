from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])

    password = PasswordField('Password', validators = [DataRequired()])

    submit = SubmitField('Login')




"""class RegistrationForm(FlaskForm): 
    
    email = StringField('email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    password = PasswordField('Username', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')
    
    def validate_email"""


