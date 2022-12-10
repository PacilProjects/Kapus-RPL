from django.db import models
from AdministrasiBuku.models import Buku, Perpustakaan

# Create your models here.
class PeminjamanOffline(models.Model):
    nama_buku = models.OneToOneField(Buku, on_delete=models.CASCADE)
    perpustakaan = models.OneToOneField(Perpustakaan, on_delete=models.CASCADE)
    username = models.CharField(max_length=100) #Harus ganti jadi user nanti jadi foreign key
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'PeminjamanOffline'