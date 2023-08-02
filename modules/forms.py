# forms for the following: LoginForm, RegistrationForm, EditProfileForm, ProductForm, OrderForm

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, SelectField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from modules.models import User, Product, Order

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')

# regisration form
class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')
  # password validator 
  def validate_password(self, password):
    if len(password.data) < 6:
      raise ValidationError('Password must be at least 6 characters long.')
  def validate_confirm(self, confirm):
    if self.password.data != confirm.data:
      raise ValidationError('Passwords must match.')  
  # add a validator to check that the username is unique
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Please use a different username.')
  # add a validator to check that the email is unique
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Please use a different email address.')
  

