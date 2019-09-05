import os

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

FIXTURE_DIRS = (
    'apps/api/fixtures/',
    'apps/warehouse_api/fixtures/',
)
# ---------------------------------------------- END DATABASE CONFIGURATION --------------------------------------------
