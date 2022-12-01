from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class PenggunaSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pengguna = True
        if commit: user.save()

        return user

class AdminPerpusSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_notpengguna = True
        if commit: user.save()

        return user 
