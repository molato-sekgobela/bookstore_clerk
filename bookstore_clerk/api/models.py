from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    superhero = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
