from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    pass

    # user_id = models.AutoField
    role = models.IntegerField(default=0)  # 0 = User,  1 = Post Moderator, 2 = Site Admin

    def __str__(self):
        return self.email
