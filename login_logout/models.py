from django.db import models

class AuthUserKapus(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)
    hp = models.CharField(max_length=50)
    tipeUser = models.CharField(max_length=50)
