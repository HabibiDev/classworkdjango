from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.


class Note(models.Model):
    content = models.CharField(max_length=120)


class NotesItem(models.Model):
    note = models.ForeignKey(
        Note, on_delete=models.CASCADE, related_name='note_item')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
