# standard library
import uuid

# django
from django.db import models
from django.utils.translation import gettext_lazy as _

# local api
from apps.api.models import AuditedModel
from apps.warehouse_api.managers import ProductManager


class Product(AuditedModel):
    """
    Model to perform CRUD operations on.
    """

    # CHOICES
    SIMPLE_PRODUCT = 'SP'
    CONFIGURABLE_PRODUCT = 'CP'
    GROUPED_PRODUCT = 'GP'
    VIRTUAL_PRODUCT = 'VP'
    BUNDLE_PRODUCT = 'BP'
    DOWNLOADABLE_PRODUCT = 'DP'

    PRODUCT_TYPE_CHOICES = (
        (SIMPLE_PRODUCT, 'Simple Product'),
        (CONFIGURABLE_PRODUCT, 'Configurable Product'),
        (GROUPED_PRODUCT, 'Grouped Product'),
        (VIRTUAL_PRODUCT, 'Virtual Product'),
        (BUNDLE_PRODUCT, 'Bundle Product'),
        (DOWNLOADABLE_PRODUCT, 'Downloadable Product'),
    )

    # DATABASE FIELDS
    uuid = models.UUIDField('external_id', default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField('product_name', max_length=30)
    type = models.CharField('product_type', max_length=3, choices=PRODUCT_TYPE_CHOICES)
    price = models.DecimalField('price', max_digits=14, decimal_places=2)
    status = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_('Designates whether the product is active or not.'),
    )

    # MANAGERS
    objects = ProductManager()

    # META CLASS
    class Meta:
        db_table = "product"
        app_label = "warehouse_api"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # TO STRING METHOD
    def __str__(self):
        return self.name
