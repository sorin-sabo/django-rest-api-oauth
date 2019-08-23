# django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import validate_email

# local api
from apps.api.managers import AuthManager, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom authentication User model with admin-compliant permissions.
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # DATABASE FIELDS
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, validators=[validate_email])
    status = models.BooleanField(
        _('active status'),
        default=False,
        help_text=_('Designates whether the user is active or not.'),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    # AUDIT FIELDS
    last_login_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # PROPERTIES
    @property
    def full_name(self):
        return f'{self.name} {self.surname}'

    # MANAGERS
    objects = AuthManager()
    entities = UserManager()

    # META CLASS
    class Meta:
        db_table = "user"
        app_label = "api"
        verbose_name = "User"
        verbose_name_plural = "Users"

    # TO STRING METHOD
    def __str__(self):
        return self.full_name
