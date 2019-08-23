import os

# ---------------------------------------------- DEBUG CONFIGURATION ---------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# ---------------------------------------------- END DEBUG CONFIGURATION -----------------------------------------------


# ---------------------------------------------- HOST CONFIGURATION ----------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.site.com'
]
# ---------------------------------------------- END HOST CONFIGURATION ------------------------------------------------


# ---------------------------------------------- DATABASE CONFIGURATION ------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT'),
        'TEST': {
            'NAME': os.environ.get('RDS_DB_NAME')
        }
    }
}
# ---------------------------------------------- END DATABASE CONFIGURATION --------------------------------------------


# ---------------------------------------------- GENERAL CONFIGURATION -------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/checks/
SILENCED_SYSTEM_CHECKS = ['models.E007']

LOGIN_URL = '/admin/login/'
# ---------------------------------------------- END GENERAL CONFIGURATION ---------------------------------------------


# ---------------------------------------------- STATIC FILE CONFIGURATION ---------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_URL = '/static/'
# ---------------------------------------------- END STATIC FILE CONFIGURATION -----------------------------------------


# ---------------------------------------------- SECRET CONFIGURATION --------------------------------------------------
SECRET_KEY = os.environ.get('SECRET_KEY')
# ---------------------------------------------- END SECRET CONFIGURATION ----------------------------------------------


# ---------------------------------------------- TEMPLATE CONFIGURATION ------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# ---------------------------------------------- END TEMPLATE CONFIGURATION --------------------------------------------


# ---------------------------------------------- MIDDLEWARE CONFIGURATION ----------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = [
    # Default Django middleware.
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Cors
    'corsheaders.middleware.CorsMiddleware',

    # Admin qr auth
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
]
# ---------------------------------------------- END MIDDLEWARE CONFIGURATION ------------------------------------------


# ---------------------------------------------- URL CONFIGURATION -----------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'DjangoTemplateProject.urls'
# ---------------------------------------------- END URL CONFIGURATION -------------------------------------------------


# ---------------------------------------------- CORS CONFIGURATION ----------------------------------------------------
CORS_ORIGIN_ALLOW_ALL = True
# ---------------------------------------------- END CORS CONFIGURATION ------------------------------------------------


# ---------------------------------------------- APP CONFIGURATION -----------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin panel
    'django.contrib.admin',

    # Admin security
    'django_otp',
    'django_otp.plugins.otp_totp',
]

THIRD_PARTY_APPS = [
    # Rest
    'rest_framework',

    # Cognito Auth
    'drf_yasg',

    # Cors
    'corsheaders',
]

LOCAL_APPS = [
    'apps.api',
    'apps.crud_api',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# ---------------------------------------------- END APP CONFIGURATION -------------------------------------------------


# ---------------------------------------------- REST FRAMEWORK CONFIGURATION ------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'apps.api.permissions.CustomDjangoModelPermission',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.oauth2.TokenAuthentication'
    ],
}
# ----------------------------------------------- END REST FRAMEWORK CONFIGURATION -------------------------------------


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ---------------------------------------------- DRF DOCUMENTATION CONFIGURATION ---------------------------------------

# ---------------------------------------------- END DRF DOCUMENTATION CONFIGURATION -----------------------------------


# ---------------------------------------------- WSGI CONFIGURATION ----------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'DjangoTemplateProject.wsgi.application'

# ---------------------------------------------- LOCAL APPLICATION CONFIGURATION ---------------------------------------
# Environment id
ENV_ID = os.environ.get('ENV_ID', 'local')

SERVER_EMAIL = 'noreply@site.com'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# ---------------------------------------------- OAUTH CONFIGURATION ------------------------------------------------
# Custom authentication model
AUTH_USER_MODEL = 'api.User'

# Authentication domain based on external service used; e.g. AWS Cognito - user pool; Auth0 - f'https://{AUTH0_DOMAIN}'
AUTH_DOMAIN = os.getenv('AUTH_DOMAIN', None)

# Jwt issuer based on external service used; e.g. AWS Cognito - user pool; Auth0 - f'https://{AUTH0_DOMAIN}'
JWT_ISSUER = os.getenv('JWT_ISSUER', None)

# Jwt guest client id used for extra validation of access token
JWT_CLIENT = os.getenv('JWT_CLIENT', None)

# ---------------------------------------------- SECURITY CONFIGURATION ------------------------------------------------
# Prevent browser from identifying content types incorrectly. Adds 'X-Content-Type-Options: nosniff' header.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Activate the browser's XSS filtering and help prevent XSS attacks.
SECURE_BROWSER_XSS_FILTER = True

# Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = True

# Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

# ---------------------------------------------- DOCUMENTATION CONFIGURATION -------------------------------------------
REDOC_SETTINGS = {
    'LAZY_RENDERING': True,
    'HIDE_HOSTNAME': False,
    'PATH_IN_MIDDLE': True,
}

# ---------------------------------------------- OTP CONFIGURATION -----------------------------------------------------
OTP_TOTP_ISSUER = 'Google Authenticator'

