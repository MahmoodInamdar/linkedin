import os
from dotenv import load_dotenv
import yaml

# Load .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

# Load settings.yaml
with open(os.path.join(os.path.dirname(__file__), '../config/settings.yaml'), 'r') as f:
    settings = yaml.safe_load(f)

# Access config values
LINKEDIN_CLIENT_ID = os.getenv('LINKEDIN_CLIENT_ID', settings['linkedin']['client_id'])
LINKEDIN_CLIENT_SECRET = os.getenv('LINKEDIN_CLIENT_SECRET', settings['linkedin']['client_secret'])
LINKEDIN_REDIRECT_URI = os.getenv('LINKEDIN_REDIRECT_URI', settings['linkedin']['redirect_uri'])
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', settings['openai']['api_key'])
DATABASE_URL = os.getenv('DATABASE_URL', settings['database']['url']) 