from wtforms import StringField, PasswordField, DateField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )
    
class BoardForm(FlaskForm):
    name = StringField(
        "name",
        validators=[InputRequired(), Length(min=1, max=20)],
    )

class ListForm(FlaskForm):
    name = StringField(
        "name",
        validators=[InputRequired(), Length(min=1, max=20)],
    )

class CardForm(FlaskForm):
    name = StringField(
        "name",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    content = StringField(
        "content",
        validators=[],
    )
    date = StringField(
        "date",
        validators=[],
    )