# django
from django_filters import rest_framework as filters

# local django
from apps.crud_api.models import Product


class MyCharFilter(filters.CharFilter):
    empty_value = ''

    def filter(self, qs, value=''):
        filter_value = value.upper()

        if filter_value != self.empty_value:
            return super(MyCharFilter, self).filter(qs, filter_value)

        return qs


class ProductFilter(filters.FilterSet):
    """
    Custom filter for products that handles type query param.
    """
    type = MyCharFilter(field_name='type')

    class Meta:
        model = Product
        fields = ['type', ]
