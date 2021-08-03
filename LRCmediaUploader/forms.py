from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flask_wtf.file import FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from LRCmediaUploader.models import User


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Signup Password', validators=[DataRequired(), Length(min=4, max=40)])

    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password'),
                                                                    Length(min=4, max=40)])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    # Dont think I want to use email for the login
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Login Password', validators=[DataRequired(), Length(min=4, max=40)])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'),
                                                                     Length(min=4, max=40)])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class FileForm(FlaskForm):
    image = FileField('Media')
    filename = StringField('Filename', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])

    file = FileField('file')

    # prob done need the remember field but using for debugging also with email
    remember = BooleanField('Remember Me')
    email = StringField('Email', validators=[DataRequired(), Email()])

    submit = SubmitField('Upload File')
