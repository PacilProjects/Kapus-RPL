from django.db import models
from django.contrib.auth.models import AbstractUser
from booking.models import *
from AdministrasiBuku.models import Perpustakaan

class AuthUserKapus(AbstractUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)
    hp = models.CharField(max_length=50)
    tipeUser = models.CharField(max_length=50)
    perpustakaanKerjaChar = models.CharField(max_length=50, null=True)
    perpustakaanKerjaModel = models.ForeignKey(Perpustakaan, null=True, on_delete=models.CASCADE)
