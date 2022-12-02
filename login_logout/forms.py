from django import forms
from .models import AuthUserKapus

class UserRegister(forms.ModelForm):
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(),
        required = True
    )

    class Meta:
        model = AuthUserKapus
        fields = [
            'username', 'password', 'lokasi',
            'email', 'hp', 'tipeUser'
        ]