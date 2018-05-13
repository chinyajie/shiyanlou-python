from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required
from simpledu.models import db, User
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    username = StringField('???', validators=[Required(), Length(3, 24)])
    email = StringField('??', validators=[Required(), Email()])
    password = PasswordField('??', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('????', validators=[Required(), EqualTo('password')])
    submit = SubmitField('??')

    def create_user(self):
        user = User()
        user.name = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('validate_username')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('validate_email')

class LoginForm(FlaskForm):
    email = StringField('??', validators=[Required(), Email()])
    password = PasswordField('??', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('???')
    submit = SubmitField('??')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('validate_email')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('validate_password')

