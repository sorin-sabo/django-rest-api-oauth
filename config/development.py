# Load the production settings and overwrite them as needed this environment.
from config.production import *

# ---------------------------------------------- DEBUG CONFIGURATION ---------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# ---------------------------------------------- END DEBUG CONFIGURATION -----------------------------------------------

# LOCAL SECURITY
SESSION_COOKIE_SECURE = False  # NO HTTPS
CSRF_COOKIE_SECURE = False  # NO HTTPS
