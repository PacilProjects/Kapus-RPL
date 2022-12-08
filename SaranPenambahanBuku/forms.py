from SaranPenambahanBuku.models import SaranPenambahanBuku
from django import forms

class PenambahanBukuForm(forms.ModelForm):

    class Meta:
        model = SaranPenambahanBuku
        fields = ['nama_buku',
        'ISBN',
        'nama_penulis',
        'nama_penerbit'
        ]
