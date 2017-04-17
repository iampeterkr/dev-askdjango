# accounts/models.py

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # user = models.OneToOneField(User) # bad case
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


