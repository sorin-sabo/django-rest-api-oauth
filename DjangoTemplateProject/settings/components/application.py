# ---------------------------------------------- APP CONFIGURATION -----------------------------------------------------
DJANGO_APPS = [
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin panel
    'jet.dashboard',
    'jet',
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
    'apps.warehouse_api',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# ---------------------------------------------- END APP CONFIGURATION -------------------------------------------------
