import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=500)
    image_link = models.CharField(max_length=256)
    release_date = models.DateTimeField('release date')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __string__(self):
        return self.title


class PostInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " " + self.post.title

    def __string__(self):
        return self.user.username + " " + self.post.title
