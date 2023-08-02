# This file contains the Flask routes for the application. It defines the behavior of the application
# when a user navigates to a particular URL. The routes include functionality for logging in, logging out,
# registering a new user, and displaying various pages of the application. The routes are defined using the
# @app decorator, which associates a URL with a Python function that generates the content for that URL.
# The routes also make use of Flask-Login, which provides user authentication and session management
# functionality.
from app import app
from flask import render_template, flash, redirect, url_for, request
from modules.forms import LoginForm, RegistrationForm #, EditProfileForm, ProductForm, OrderForm
from flask_login import current_user, login_user, logout_user, login_required
from modules.models import User, Product, Order
from werkzeug.urls import url_parse
from datetime import datetime
from flask import flash
from extensions import db

@app.route('/')
def index():
  # products = Product.query.all()
  # return render_template('index.html', title='Home', products=products)
  return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
  # if the user is already logged in, redirect to index
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  # otherwise, display the login form
  form = LoginForm()
  # if the form is submitted, validate the data
  if form.validate_on_submit():
    # query the database for the user
    user = User.query.filter_by(username=form.username.data).first()
    # if the user doesn't exist or the password is incorrect, flash a message and redirect to login
    if user is None or not user.check_password(form.password.data):
      flash('Invalid username or password. Please try again or sign up below.')
      return redirect(url_for('register'))
    # otherwise, log the user in and redirect to index
    login_user(user, remember=form.remember_me.data)
    # if the user was redirected to login from another page, redirect them back to that page
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
      next_page = url_for('index')
    return redirect(next_page)
  # otherwise, display the login page
  return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    # log the user out and redirect to index
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  # if the user is already logged in, redirect to index
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  # otherwise, display the registration form
  form = RegistrationForm()
  # if the form is submitted, validate the data
  if form.validate_on_submit():
    # create a new user object
    user = User(username=form.username.data, email=form.email.data)
    # set the password
    user.set_password(form.password.data)
    # add the user to the database
    db.session.add(user)
    db.session.commit()
    
    # flash a message and redirect to login
    flash('Congratulations, you are now a registered user!')
    return redirect(url_for('homepage'))
  # otherwise, display the registration page
  return render_template('register.html', title='Register', form=form)

@app.route('/homepage')
def homepage():
  return render_template('homepage.html', title='Home')


# @app.route('/user/<username>')
# @login_required
# def user(username):
#   # query the database for the user
#   user = User.query.filter_by(username=username).first_or_404()
#   # query the database for the user's orders
#   orders = Order.query.filter_by(user_id=user.id).all()
#   # display the user's profile page
#   return render_template('user.html', user=user, orders=orders)

# @app.before_request
# def before_request():
#   # if the user is logged in, update their last_seen time
#   if current_user.is_authenticated:
#     current_user.last_seen = datetime.utcnow()
#     db.session.commit()
#   else:
#     return redirect(url_for('login'))

# @app.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#   # display the edit profile form
#   form = EditProfileForm(current_user.username)
#   # if the form is submitted, validate the data
#   if form.validate_on_submit():
#     # update the user's username and email
#     current_user.username = form.username.data
#     current_user.email = form.email.data
#     # commit the changes to the database
#     db.session.commit()
#     # flash a message and redirect to the user's profile page
#     flash('Your changes have been saved.')
#     return redirect(url_for('user', username=current_user.username))
#   # otherwise, display the edit profile page
#   elif request.method == 'GET':
#     form.username.data = current_user.username
#     form.email.data = current_user.email
#   return render_template('edit_profile.html', title='Edit Profile', form=form)



