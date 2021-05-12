import os

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
STATIC_ROOT = 'static'
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

# ---------------------------------------------- WSGI CONFIGURATION ----------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'DjangoTemplateProject.wsgi.application'

# ---------------------------------------------- LOCAL APPLICATION CONFIGURATION ---------------------------------------
SERVER_EMAIL = 'noreply@site.com'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# ---------------------------------------------- SECURITY CONFIGURATION ------------------------------------------------
# Using a secure-only session cookie makes it more difficult for network traffic sniffers to hijack user sessions.
SESSION_COOKIE_SECURE = False  # NO HTTPS

# Using a secure-only CSRF cookie makes it more difficult for network traffic sniffers to steal the CSRF token.
CSRF_COOKIE_SECURE = False  # NO HTTPS

X_FRAME_OPTIONS = 'DENY'

# ---------------------------------------------- END SECURITY CONFIGURATION --------------------------------------------


# ---------------------------------------------- OTP CONFIGURATION -----------------------------------------------------
OTP_TOTP_ISSUER = 'Google Authenticator'

