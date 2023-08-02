from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
login_manager = LoginManager()
db = SQLAlchemy()
CORS(app)
CORS(app, resources={r"/*": {"origins": ["https://*.azurewebsites.net", "http://localhost:5000", "http://127.0.0.1:5000", "http://127.0.0.1:5000/*"]}})
