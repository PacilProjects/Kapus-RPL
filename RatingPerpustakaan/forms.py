from django import forms
from RatingPerpustakaan.models import Rating

class RatingForm(forms.ModelForm):

    class Meta :
        model = Rating
        fields = [
        'score'
        ]