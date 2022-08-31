from wtforms import FlaskForm
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileAllowed, FileField



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, Please choose a different')

   
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, Please choose a different')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    picture = FileField ('Update Profile picture ',validators=[FileAllowed(['jpeg', 'png', 'jpg'])] )
    
    submit = SubmitField('Update')


    def validate_username(self, username):
        if username.data != current_user.username:
          user = User.query.filter_by(username=username.data).first()
          if user:
            raise ValidationError('That Username is alraedy Taken!')


    def validate_email(self, email):
         
        if email.data != current_user.email:
          user = User.query.filter_by(email=email.data).first()
          if user:
            raise ValidationError('That Email is alraedy Taken!')

class RequestResetForm(FlaskForm):
     email = StringField('Email',
                        validators=[DataRequired(), Email()])
     submit = SubmitField('Request Password Reset')


     def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('There is no account with that email...Register First')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')