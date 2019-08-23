# django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MainApiConfig(AppConfig):
    name = 'apps.api'
    verbose_name = _('User Management')
