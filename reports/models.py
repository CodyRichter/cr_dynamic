from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image_link = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
