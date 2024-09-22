from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='nofications_for_actor')
    actor  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications_for_recipient')
    verb = models.CharField(max_length=150)
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)  # Type of object (post, comment, etc.)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)  # ID of the target object
    target = GenericForeignKey('target_content_type', 'target_object_id')  # GenericForeignKey to any object
    timestamp = models.DateTimeField(auto_now_add=True)  # Time of the notification
    is_read = models.BooleanField(default=False)  # To track whether the notification has been read

    def __str__(self):
        return f'{self.actor} {self.verb} {self.target}'