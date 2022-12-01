from django import forms
from AdministrasiBuku.models import Buku, Perpustakaan


class NewBook(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['nama_buku', 'isbn', 'penulis', 'penerbit']


class NewPerpustakaan(forms.ModelForm):
    class Meta:
        model = Perpustakaan
        fields = ['nama', 'lokasi', 'alamat']

