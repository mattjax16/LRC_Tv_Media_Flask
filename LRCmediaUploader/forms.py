from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from LRCmediaUploader.models import User, LRCmedia


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=40)])

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

    password = PasswordField('Login Password', validators=[DataRequired(), Length(min=4, max=40)])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')






class MediaForm(FlaskForm):

    filename = StringField('Filename', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])

    file = FileField('Media File', validators=[FileAllowed(['jpg', 'png','jpeg','mp4',
                                                            'biff','MPEG-1', 'MPEG-2',
                                                            'MPEG-4','AVI','MOV','AVCHD',
                                                            'H.264', 'H.265','mp4'])])
    submit = SubmitField('Upload')





class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')