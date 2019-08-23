# django
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WarehouseApiConfig(AppConfig):
    name = 'apps.warehouse_api'
    verbose_name = _('Warehouse Manager')
