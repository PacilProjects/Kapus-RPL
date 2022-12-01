from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_pengguna = models.BooleanField(default=False)
    is_notpengguna = models.BooleanField(default=False)