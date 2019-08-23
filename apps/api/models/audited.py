# django
from django.db import models

# local apps
from .user import User


class AuditedModel(models.Model):
    """
    Audit fields to be extended in all models.
    """

    created_by = models.ForeignKey(User, editable=False, null=True, related_name="%(class)s_created",
                                   on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, editable=False, related_name="%(class)s_updated", on_delete=models.CASCADE,
                                   null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return "General Configuration"
