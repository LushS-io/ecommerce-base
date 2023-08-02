# login manager module

from app import login_manager
from modules.models import User

@login_manager.user_loader
def load_user(user_id):
  # query the database for the user
  return User.query.get(int(user_id))
