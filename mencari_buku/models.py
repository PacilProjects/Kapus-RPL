from django.db import models

class Buku(models.Model):
    nama_buku = models.CharField(default="", max_length=30)
    nama_penulis = models.CharField(default="", max_length=30)
    isbn = models.BigIntegerField(default=0)
    tersedia = models.BooleanField(default=False)

    class Meta:
      verbose_name_plural = "Buku-buku"

    def __str__(self):
        return self.nama_buku
