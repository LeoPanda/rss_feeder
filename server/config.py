import os

# flask configuration
DATABASE = '/tmp/server.db'
DEBUG = True
SECRET_KEY = 'my-secret-key'
USERPROFILE = 'user_profile'
PASSWORD = 'default'
JSON_AS_ASCII = False

CREDENTIALS = 'credentials'
REDIRECT_URL = 'redirect_url'

IS_DEVELOPMENT = os.getenv('FLASK_ENV') == 'development'
