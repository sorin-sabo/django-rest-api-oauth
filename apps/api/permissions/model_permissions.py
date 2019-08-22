# standard library
import copy

# django rest framework
from rest_framework import permissions


class CustomDjangoModelPermission(permissions.DjangoModelPermissions):
    """
    Generic permission to allow/deny default CRUD permissions for models.
    To handle different permissions build those as custom permissions and define them at model level + migrate.
    """

    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)  # deepcopy for inherit dictionary type
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
