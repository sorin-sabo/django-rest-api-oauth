# ---------------------------------------------- DEBUG CONFIGURATION ---------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# ---------------------------------------------- END DEBUG CONFIGURATION -----------------------------------------------

# ---------------------------------------------- HOST CONFIGURATION ----------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.site.com',
    '127.0.0.1',
    'localhost',
]
# ---------------------------------------------- END HOST CONFIGURATION ------------------------------------------------

# ---------------------------------------------- SECURITY CONFIGURATION ------------------------------------------------
# Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = False

# Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
CSRF_COOKIE_SECURE = False
# ---------------------------------------------- END SECURITY CONFIGURATION --------------------------------------------

# ---------------------------------------------- EMAIL CONFIGURATION ---------------------------------------------------
SERVER_EMAIL = 'noreply@site.com'
# ---------------------------------------------- END EMAIL CONFIGURATION -----------------------------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'template_db',
        'USER': 'postgres',
        'PASSWORD': 'ADMIN',
        'HOST': 'localhost',
        'PORT': 5433,
        'TEST': {
            'NAME': 'template_db'
        }
    }
}

AUTH_DOMAIN = 'https://sorin-dev.eu.auth0.com'
JWT_ISSUER = 'https://sorin-dev.eu.auth0.com/'
JWT_CLIENT = 'https://django-template-auth'

SECRET_KEY = 'o%=segxp&to^lth4m82lq!=%vltk#2t4!ytjd)zj4z-i(z9-q9'
