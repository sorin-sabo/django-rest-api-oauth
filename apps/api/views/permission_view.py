# django
from django.contrib.auth.models import Permission
from django.db.models.query import QuerySet

# rest framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# local api
from apps.api.serializers import PermissionSerializer


class UserPermissionList(generics.ListAPIView):
    """
    User permissions detailed.

    * Requires token authentication.
    * All users are authorized to access this view.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = PermissionSerializer

    @staticmethod
    def get_permission_code(permission_code=None):
        permission_code = str(permission_code)

        return permission_code.split('.')[1] if permission_code.find('.') != -1 else permission_code

    def get_queryset(self) -> QuerySet:
        permissions = self.request.user.get_all_permissions()
        permission_codes = [self.get_permission_code(permission) for permission in permissions]

        return Permission.objects.filter(codename__in=permission_codes)
