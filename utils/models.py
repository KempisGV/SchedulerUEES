"""Django models utilities"""

from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class TimeStampModel(models.Model):
    """
    TimeStampModel acts as an abstract base class from which every other model in the project will inherit.
    This class
    provides every table with the following attributes:
        + created (DateTime): Store
        + modified (DateTime): Store
    """
    created = models.DateTimeField(
        "created_at",
        auto_now_add=True, blank=True,
        help_text="Date time on which the object was created.",
    )
    modified = models.DateTimeField(
        "modified_at",
        auto_now=True, blank=True,
        help_text="Date time on which the object was last modified.",
    )
    deleted_at = models.DateTimeField("deleted_at", blank=True, null=True)
    creator = UserForeignKey(auto_user_add=True, related_name="+")
    modifier = UserForeignKey(auto_user=True, related_name="+")
    status = models.BooleanField(
        "status", default=True, help_text="Status the object has currently"
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = "created"
        ordering = ["-created", "-modified"]  # descendent
