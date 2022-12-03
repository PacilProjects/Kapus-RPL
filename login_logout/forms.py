from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AuthUserKapus

class UserRegister(forms.ModelForm):
    class Meta:
        model = AuthUserKapus
        fields = [
            'username', 'password', 'lokasi',
            'email', 'hp', 'tipeUser'
        ]

class UserLogin(forms.Form):
    username = forms.CharField(
        max_length=50
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=50
    )

class UserChangeProfile(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        max_length=50,
        initial='',
        required=False
    )
    lokasi = forms.CharField(
        max_length=50, 
        initial='',
        required=False
    )
    hp = forms.CharField(
        max_length=50, 
        initial='',
        required=False
    )