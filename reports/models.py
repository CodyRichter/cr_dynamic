import datetime

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image_link = models.CharField(max_length=256)
    seen = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # @classmethod
    # def create(cls, title, description, image_link):
    #     post = cls(title=title, description=description, image_link=image_link, seen=False,
    #                pub_date=datetime.datetime.now())
    #     return post

    def __string__(self):
        if self.title is None or self.title == "":
            return self.id
        return self.title
