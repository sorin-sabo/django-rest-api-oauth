"""
Django settings for DjangoTemplateProject project.
Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Django project settings loader
import os

# ---------------------------------------------- PATH CONFIGURATION ----------------------------------------------------
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# ---------------------------------------------- END PATH CONFIGURATION ------------------------------------------------

# ---------------------------------------------- ENVIRONMENT CONFIG ----------------------------------------------------
config = os.environ.get('ENV_ID', 'local')

# Import the configuration settings file
config_module = __import__(f'config.{config}', globals(), locals(), ['DjangoTemplateProject'])

# Load the config settings properties into the local scope.
for setting in dir(config_module):
    if setting == setting.upper():
        locals()[setting] = getattr(config_module, setting)
# ---------------------------------------------- END ENVIRONMENT CONFIGURATION -----------------------------------------
