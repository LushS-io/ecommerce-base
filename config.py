import secrets
from dotenv_vault import load_dotenv
load_dotenv()

def generate_key():
  return secrets.token_hex(16)