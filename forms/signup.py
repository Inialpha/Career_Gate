from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignupForm(FlaskForm):
    firstname = StringField(label='First Name:')
    lastname = StringField(label='Last Name:')
    email_address = StringField(label='Email Address:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')
