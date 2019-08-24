from django.contrib.auth.models import User
from django.db import models

from cr_dynamic import settings
from users.models import SiteUser


class Post(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=5000)
    image_link = models.CharField(max_length=256)
    release_date = models.DateTimeField('release date')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __string__(self):
        return self.title


class Interaction(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('timestamp')

    def __str__(self):
        return self.title

    def __string__(self):
        return self.title

