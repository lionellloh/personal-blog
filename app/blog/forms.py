from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, TextField
from wtforms.validators import DataRequired, Email, EqualTo

class PostForm(FlaskForm):

    title = StringField('Title', validators = [DataRequired()])

    content = TextField('Post Content', validators = [DataRequired()])

    submit = SubmitField('Post')
