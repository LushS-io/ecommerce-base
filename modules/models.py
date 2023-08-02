from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
  """
  User model class for database table 'users'
  """
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  first_name = db.Column(db.String(64), index=True)
  last_name = db.Column(db.String(64), index=True)
  password = db.Column(db.String(128))
  email = db.Column(db.String(120), index=True, unique=True)
  phone = db.Column(db.String(20), index=True, unique=True)
  address = db.Column(db.String(120), index=True)
  city = db.Column(db.String(64), index=True)
  state = db.Column(db.String(64), index=True)
  zip_code = db.Column(db.String(10), index=True)
  country = db.Column(db.String(64), index=True)
  date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  date_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  is_active = db.Column(db.Boolean, default=False)
  is_authenticated = db.Column(db.Boolean, default=False)

  def __repr__(self):
    """
    Returns a string representation of the User object
    """
    return '<User {}>'.format(self.username)

  def set_password(self, password):
    """
    Sets the password for the User object
    """
    self.password = generate_password_hash(password)

  def check_password(self, password):
    """
    Checks if the given password matches the User object's password hash
    """
    return check_password_hash(self.password, password)

  def is_active(self):
    """
    Returns True if the User object is active
    """
    return self.is_active

  def get_id(self):
    """
    Returns the User object's id as a unicode string
    """
    return str(self.id)

  def is_authenticated(self):
    """
    Returns True if the User object is authenticated
    """
    return self.authenticated


class Product(db.Model):
  """
  Product model class for database table 'products'
  """
  __tablename__ = 'products'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), index=True)
  description = db.Column(db.String(120), index=True)
  price = db.Column(db.Float, index=True)
  date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  date_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __repr__(self):
    """
    Returns a string representation of the Product object
    """
    return '<Product {}>'.format(self.name)


class Order(db.Model):
  """
  Order model class for database table 'orders'
  """
  __tablename__ = 'orders'

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  date_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)

  def __repr__(self):
    """
    Returns a string representation of the Order object
    """
    return '<Order {}>'.format(self.id)