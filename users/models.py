from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
