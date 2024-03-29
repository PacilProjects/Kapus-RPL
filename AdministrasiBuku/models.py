from django.db import models

# Create your models here.
class Buku(models.Model):
    nama_buku = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, primary_key=True, null=False)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    perpustakaan  = models.ManyToManyField('Perpustakaan', through='PerpusBuku')

    class Meta:
        db_table = 'buku'
class Perpustakaan(models.Model):
    nama = models.CharField(max_length=100, primary_key=True, null=False)
    lokasi = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)
    class Meta:
        db_table = 'perpustakaan'

    def __unicode__(self):
        return self.name

class PerpusBuku(models.Model):
    isbn = models.ForeignKey('Buku', on_delete=models.CASCADE)
    nama_perpus = models.ForeignKey('Perpustakaan', on_delete=models.CASCADE)
    kuantitas = models.IntegerField(default=0)
    class Meta:
        db_table = 'PerpusBuku'


