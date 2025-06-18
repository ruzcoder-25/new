from django.contrib.auth.models import AbstractUser
from django.db import models

class RoleChoices(models.TextChoices):
    READER =('reader','Reader')
    ADMIN =('admin','Admin')
    PUBLISHER =('publisher','Publisher')

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    role = models.CharField(default=RoleChoices.READER, max_length=20, choices=RoleChoices)
