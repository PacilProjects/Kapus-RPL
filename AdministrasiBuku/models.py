from django.db import models

# Create your models here.
class Buku(models.Model):
    nama_buku = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, primary_key=True, null=False)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    banyak = models.IntegerField(blank=True)

    class Meta:
        db_table = 'buku'


class Perpustakaan(models.Model):
    nama = models.CharField(max_length=100, primary_key=True, null=False)
    lokasi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    class Meta:
        db_table = 'perpustakaan'


