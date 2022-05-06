from django.db import models

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Note(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="notes", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        title = "ID note " + str(self.id) + " of model '" + self.content_type.model + "'"
        return title