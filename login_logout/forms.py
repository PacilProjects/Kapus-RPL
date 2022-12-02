from django import forms
from crispy_forms.helper import FormHelper
from django.db import connection
from .models import AuthUserKapus

class UserRegister(forms.Form):
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

class UserRegisterForm(forms.Form):
    pilihanUser = (
        ('Pengguna', 'Pengguna'),
        ('Pengelola', 'Pengelola')
    )

    tipeUser = forms.ChoiceField(
        choices = pilihanUser,
        required = True,
        widget = forms.widgets.RadioSelect(attrs={
            'required': True
        })
    )

    username = forms.CharField(
        label = 'Username',
        widget = forms.widgets.TextInput(attrs={
            'placeholder': 'Nama Lengkap',
            'type': 'text',
            'required': True
        })
    )

    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(),
        required = True
    )

    lokasi = forms.CharField(
        label = 'lokasi',
        widget = forms.TextInput(attrs={
            'placeholder': 'Lokasi',
            'type': 'text',
            'required': True
        })
    )

    email = forms.CharField(
        label = 'Email',
        widget = forms.widgets.EmailInput(
            attrs={
                'placeholder': 'Email',
                'type': 'text',
                'required': True
            }
        )
    )

    hp = forms.CharField(
        label = 'Nomor HP',
        widget = forms.widgets.TextInput(
            attrs={
                'placeholder': 'Nomor HP',
                'type': 'text',
                'required': True
            }
        )
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label = 'Username',
        widget = forms.widgets.TextInput(attrs={
            'placeholder': 'Nama Lengkap',
            'type': 'text',
            'required': True
        })
    )

    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(),
        required = True
    )

class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput(),
        required = True 
    )