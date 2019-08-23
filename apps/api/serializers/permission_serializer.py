# django
from django.contrib.auth.models import Permission

# rest framework
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('name', 'codename')
