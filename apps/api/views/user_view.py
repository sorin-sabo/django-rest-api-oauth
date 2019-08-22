# rest framework
from rest_framework import generics

# local api
from apps.api.serializers import UserSerializer
from apps.api.models import User


class UserList(generics.ListAPIView):
    """
    List all users.

    * Requires token authentication.
    """

    queryset = User.entities.all()
    serializer_class = UserSerializer
