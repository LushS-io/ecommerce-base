from flask_wtf.csrf import CSRFProtect
from extensions import app, login_manager, db
from flask import Flask
from config import Config


def create_app() -> Flask:
  """
  Creates a Flask application instance.

  Returns:
    object: Flask application instance.
  """
  # Configure the database
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
  db.init_app(app)

  # Configure the app's secret key
  app.config['SECRET_KEY'] = Config.get_key()

  # Configure CSRF protection
  csrf = CSRFProtect(app)

  login_manager.init_app(app)

  # import modules
  with app.app_context():
    import modules.models
    db.create_all()

    import modules

  return app