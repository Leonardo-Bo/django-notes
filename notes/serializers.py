from rest_framework import serializers
# from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    User = get_user_model()

    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(),
        slug_field='model',
    )

    class Meta:
        model = Note
        fields = ['id', 'created_at', 'updated_at', 'content', 'author', 'content_type', 'object_id']
