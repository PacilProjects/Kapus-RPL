from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import psycopg2

def registerUser(request):
    userKapus = UserRegister(request.POST or None)
    if (userKapus.is_valid() and request.method == 'POST'):
        userKapus.save()
        return redirect('success/')
    
    response = {
        'userKapus': userKapus
    }

    return render(request, 'registration.html', response)

def index(request):
    return render(request, 'index_login_logout.html')

def successScreen(request):
    return render(request, 'success.html')

def failedScreen(request):
    return render(request, 'failed.html')