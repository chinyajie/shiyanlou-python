from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required


class RegisterForm(FlaskForm):
    username = StringField('???', validators=[Required(), Length(3, 24)])
    email = StringField('??', validators=[Required(), Email()])
    password = PasswordField('??', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('????', validators=[Required(), EqualTo('password')])
    submit = SubmitField('??')


class LoginForm(FlaskForm):
    email = StringField('??', validators=[Required(), Email()])
    password = PasswordField('??', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('???')
    submit = SubmitField('??')
