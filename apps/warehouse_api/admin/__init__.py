# django
from django.contrib import admin

# local django
from apps.warehouse_api.models import (
    Product,
)

from .product_admin import ProductAdmin

admin.site.register(Product, ProductAdmin)
