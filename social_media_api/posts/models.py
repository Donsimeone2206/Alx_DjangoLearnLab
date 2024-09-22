from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post ,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # stores when the like was created at

    class Meta:
        unique_together = ('post', 'user') # restricts the user from likiing a post twice