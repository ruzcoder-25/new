from email.policy import default

from django.contrib.auth.models import AbstractUser
from django.db import models

class RoleChoices(models.TextChoices):
    READER =('reader','Reader')
    ADMIN =('admin','Admin')
    PUBLISHER =('publisher','Publisher')

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    role = models.CharField(default=RoleChoices.READER, max_length=20, choices=RoleChoices)
    email = models.EmailField(max_length=250)
    balance = models.FloatField(default=2000000)

class Transaction(models.Model):
    from_user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="from_user")
    to_user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="to_user")
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
