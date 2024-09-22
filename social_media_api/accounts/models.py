from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/',blank=True , null=True)
    followers = models.ManyToManyField('self' , symmetrical=False,  related_name = 'user_followers') # this deals with the users who are following the current user
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_following') # this deals with who the user is following



    def __str__(self):
        return self.username
    