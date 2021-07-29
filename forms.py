from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignupForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])

    email = StringField('Email',validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired(),Length(min = 4)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('Password')])

    submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])


    #Dont think I want to use email for the login
    #email = StringField('Email',validators=[DataRequired(), Email()])

    password = PasswordField('Password',validators=[DataRequired(),Length(min = 4)])

    rembember = BooleanField('Remember Me')

    submit = SubmitField('Login')