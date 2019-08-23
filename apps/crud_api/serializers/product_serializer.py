# rest framework
from rest_framework import serializers

# local api
from apps.crud_api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id', 'uuid', 'status', 'created_at', 'updated_at', 'created_by', 'updated_by')


class BasicProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'uuid', 'name', 'type', 'price')
        read_only_fields = ('id', 'uuid')


class ExternalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'name', 'type', 'price')
        read_only_fields = ('uuid',)
