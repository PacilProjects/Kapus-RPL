from django import forms
from .models import AuthUserKapus

class UserRegister(forms.ModelForm):
    class Meta:
        model = AuthUserKapus
        fields = [
            'username', 'password', 'lokasi',
            'email', 'hp', 'tipeUser'
        ]

class UserLogin(forms.ModelForm):
    class Meta:
        model = AuthUserKapus
        fields = [
            'username', 'password'
        ]

class UserChangeProfile(forms.ModelForm):
    class Meta:
        model = AuthUserKapus
        fields = [
            'password', 'lokasi', 'hp'
        ]