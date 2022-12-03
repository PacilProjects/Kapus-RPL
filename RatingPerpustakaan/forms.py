from django import forms
from RatingPerpustakaan.models import SaranPenambahanRating, Perpustakaan

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