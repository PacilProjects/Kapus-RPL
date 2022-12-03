from django.db import models

# Create your models here.

class SaranPenambahanBuku(models.Model):
    nama_buku = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=30)
    nama_penulis = models.CharField(max_length=50)
    nama_penerbit = models.CharField(max_length=50)