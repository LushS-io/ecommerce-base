from flask_wtf.csrf import CSRFProtect
from extensions import app, login_manager, db


def create_app() -> object:
  """
  Creates a Flask application instance.

  Returns:
    object: Flask application instance.
  """
  # Configure the database
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
  db.init_app(app)

  # Configure the app's secret key
  from config import generate_key
  app.config['SECRET_KEY'] = generate_key()

  # Save the secret key in a file
  with open('.env', 'w') as f:
    f.write(f'SECRET_KEY={app.config["SECRET_KEY"]}')

  # Configure CSRF protection
  csrf = CSRFProtect(app)

  login_manager.init_app(app)

  # import modules
  with app.app_context():
    import modules.models
    db.create_all()

    import modules

  return app