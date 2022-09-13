from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    objects = UserManager()

    nickname = models.CharField(blank=True, max_length=50)
    introduction = models.TextField(blank=True, max_length=200)
    profile_image = models.ImageField(blank=True, null=True)
