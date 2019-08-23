# rest framework
from rest_framework import serializers

# local django
from apps.api.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'email')
        read_only_fields = ('id',)

