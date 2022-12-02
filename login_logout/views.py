from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def registerUser(request):
    userKapus = UserRegister(request.POST or None)
    if (userKapus.is_valid() and request.method == 'POST'):
        userKapus.save()
        return redirect('success/')
    
    response = {
        'userKapus': userKapus
    }

    return render(request, 'registration.html', response)

def loginUser(request):
    print('1')
    userKapus = AuthenticationForm()
    if request.method == 'POST':
        print('2')
        userKapus = AuthenticationForm(request, data=request.POST)
        print(userKapus)
        username = userKapus.cleaned_data['username']
        password = userKapus.cleaned_data['password']
        
        try:
            user = AuthUserKapus.objects.get(username=username)
            print('5')
        except:
            user = None
            print('6')
        
        if (user is not None and user.password == password):
            print('3')
            login(request, user)
            print(user.is_authenticated)
            return redirect('loginSuccess/')
        else:
            print('4')
            print('Failed')
            return redirect('failed/')

    response = {
        'userKapus': userKapus
    }

    return render(request, 'login.html', response)

def index(request):
    return render(request, 'index_login_logout.html')

def successScreen(request):
    return render(request, 'success.html')

def loginSuccessScreen(request):
    return render(request, 'loginSuccess.html')

def failedScreen(request):
    return render(request, 'failed.html')