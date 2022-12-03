from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Works
def kapusUserRegister(request):
    userKapus = UserRegister(request.POST or None)
    if (userKapus.is_valid() and request.method == 'POST'):
        userKapus.save()
        return redirect('http://127.0.0.1:8000/accounts/login/loginSuccess/')
    
    response = {
        'userKapus': userKapus
    }

    return render(request, 'registration.html', response)

def kapusUserLogin(request):
    userKapus = UserLogin(request.POST or None)
    if (request.method == 'POST' and userKapus.is_valid()):
        print(userKapus.is_valid())
        
        username = userKapus.cleaned_data['username']
        password = userKapus.cleaned_data['password']

        try:
            user = AuthUserKapus.objects.get(username=username)
        except:
            user = None
        
        if (user is not None):
            if (user.password == password):
                login(request, user)
                return redirect('http://127.0.0.1:8000/accounts/login/loginSuccess/')
            else:
                return redirect('http://127.0.0.1:8000/accounts/login/loginSuccess/')
        else:
            return redirect('http://127.0.0.1:8000/accounts/login/loginFailed/')
            
    context = {
        'form': userKapus
    }

    return render(request, 'login.html', context)

@login_required(login_url='http://127.0.0.1:8000/accounts/login/')
def editUser(request):
    username = None

    if request.user.is_authenticated:
        username = request.user.username
    
    userKapus = UserChangeProfile(request.POST or None)
    print(userKapus.is_valid())
    if (userKapus.is_valid() and request.method == 'POST'):
        password = userKapus.cleaned_data['password']
        lokasi = userKapus.cleaned_data['lokasi']
        hp = userKapus.cleaned_data['hp']

        user = AuthUserKapus.objects.get(username=username)
        if checkLength(password): user.password = password
        if checkLength(lokasi): user.lokasi = lokasi
        if checkLength(hp): user.hp = hp
        user.save()

        return redirect('http://127.0.0.1:8000/accounts/login/loginSuccess/')
    
    response = {
        'userKapus': userKapus
    }

    return render(request, 'edit.html', response)

def checkLength(parameter):
    return len(parameter) > 0

def index(request):
    return render(request, 'index_login_logout.html')

@login_required(login_url='http://127.0.0.1:8000/accounts/login/')
def kapusUserLogout(request):
    return render(logout(request), 'logoutSuccess.html')

def successScreen(request):
    return render(request, 'success.html')

@login_required(login_url='http://127.0.0.1:8000/accounts/login/')
def loginSuccessScreen(request):
    return render(request, 'loginSuccess.html')
    
def loginFailedScreen(request):
    return render(request, 'loginFailed.html')

def failedScreen(request):
    return render(request, 'failed.html')