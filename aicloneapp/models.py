from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    def __str__(self):
        return self.email