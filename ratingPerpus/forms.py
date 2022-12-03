from django import forms
from ratingPerpus.models import SaranPenambahanRating, Peminjam, Perpustakaan

class PenambahanRatingForm(forms.ModelForm):

    class Meta :
        model = SaranPenambahanRating
        fields = ['nama_perpus',
        'score'
        ]

class PerpustakaanForm(forms.ModelForm):

    class Meta :
        model = Perpustakaan
        fields = ['nama_perpus'
        ]

class PeminjamForm(forms.ModelForm):

    class Meta :
        model = Peminjam
        fields = ['nama_peminjam',
        'perpus_id'
        ]