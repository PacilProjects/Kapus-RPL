from AdministrasiPeminjam.models import PeminjamanOffline
from django import forms


class PeminjamanOfflineForm(forms.ModelForm):
    class Meta:
        model = PeminjamanOffline
        fields = ['nama_buku', 'perpustakaan', 'username']