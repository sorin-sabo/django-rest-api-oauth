# django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CrudApiConfig(AppConfig):
    name = 'apps.crud_api'
    verbose_name = _('CRUD Api')
