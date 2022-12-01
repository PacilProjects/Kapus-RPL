from django.db import models

# Create your models here.
class Buku(models.Model):
    nama_buku = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, primary_key=True, null=False)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)

    class Meta:
        db_table = 'buku'