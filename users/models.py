from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    pass

    # user_id = models.AutoField
    role = models.IntegerField(default=0)  # 0 = User,  1 = Post Moderator, 2 = Site Admin
    private = models.BooleanField(default=True)  # Whether others can view this profile

    def __str__(self):
        return self.email
