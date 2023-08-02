import os
import secrets
from dotenv_vault import load_dotenv

'''Will load .env locally and key-vault when deployed on Azure'''
load_dotenv()

class Config:
  ENV = os.getenv('ENV', 'development')

  # Set up Flask configuration options
  DEBUG = os.getenv('DEBUG', default='INFO')
  TESTING = os.getenv('TESTING', default=False)

  # Set up SQLAlchemy configuration options
  SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', default='sqlite:///app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)

  # Set up CORS configuration
  CORS_HEADERS = 'Content-Type'

  @staticmethod
  def generate_key():
    return secrets.token_hex(16)

  SECRET_KEY = os.getenv('SECRET_KEY') or generate_key()

  # Save the secret key in a file
  @staticmethod
  def save_key():
    with open('.env', 'w') as f:
      f.write(f'SECRET_KEY={Config.SECRET_KEY}')

  @staticmethod
  def get_key():
    return Config.SECRET_KEY
