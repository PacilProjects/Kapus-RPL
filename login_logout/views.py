from .forms import *
from .models import *
from AdministrasiBuku.models import Perpustakaan
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def show_perpustakaan(request):
    perpus = Perpustakaan.objects.only('nama')
    name = []
    for i in perpus:
        name.append(i.nama)
    return name

def kapusUserRegister(request):
    userKapus = UserRegister(request.POST or None)
    if request.method == 'POST':
        if userKapus.is_valid():
            userKapus.save()
            return redirect('/accounts/register/registerSuccess/')
        else:
            return redirect('/accounts/register/registerFailed/')
    
    response = {
        'form': userKapus
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
                return redirect('/accounts/login/loginSuccess/')
            else:
                return redirect('/accounts/login/loginFailed/')
        else:
            return redirect('/accounts/login/loginFailed/')
            
    context = {
        'form': userKapus
    }

    return render(request, 'login.html', context)

@login_required(login_url='/accounts/login/')
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

        try:
            user = AuthUserKapus.objects.get(username=username)
        except:
            user = None

        if user is not None:
            if checkLength(password): user.password = password
            if checkLength(lokasi): user.lokasi = lokasi
            if checkLength(hp): user.hp = hp
            user.save()

            return redirect('/accounts/profile/changeSuccess/')
        else:
            return redirect('/accounts/profile/changeFailed/')
    
    response = {
        'form': userKapus
    }

    return render(request, 'edit.html', response)

def forgetPassword(request):
    userKapus = UserLogin(request.POST or None)
    if (userKapus.is_valid() and request.method == 'POST'):
        username = userKapus.cleaned_data['username']
        password = userKapus.cleaned_data['password']

        try:
            user = AuthUserKapus.objects.get(username=username)
        except:
            user = None

        if user is not None:
            if checkLength(password): user.password = password
            user.save()
            return redirect('/accounts/forgot/forgotSuccess/')
        else:
            return redirect('/accounts/forgot/forgotFailed/')
    
    response = {
        'form': userKapus
    }

    return render(request, 'editPassword.html', response)

def checkLength(parameter):
    return len(parameter) > 0

@login_required(login_url='/accounts/login/')
def addPerpustakaan(request):
    username = None

    if request.user.is_authenticated:
        username = request.user.username

    if request.method == 'POST':
        data = request.POST
        user = AuthUserKapus.objects.get(username=username)
        user.perpustakaanKerjaChar = data['perpustakaan']
        user.perpustakaanKerjaModel = Perpustakaan.objects.get(nama=data['perpustakaan'])
        user.save()

        return redirect('/accounts/profile/')

    context = {
        'perpus': show_perpustakaan(request)
    }
    return render(request, 'editPerpustakaan.html', context)

def index(request):
    return render(request, 'index_login_logout.html')

@login_required(login_url='/accounts/login/')
def kapusUserLogout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')
    
def loginFailedScreen(request):
    return render(request, 'loginFailed.html')

def loginSuccessScreen(request):
    return render(request, 'loginSuccess.html')

def registerFailedScreen(request):
    return render(request, 'registerFailed.html')

def registerSuccessScreen(request):
    return render(request, 'registerSuccess.html')

def forgotFailedScreen(request):
    return render(request, 'forgotFailed.html')

def forgotSuccessScreen(request):
    return render(request, 'forgotSuccess.html')

def editFailedScreen(request):
    return render(request, 'editFailed.html')

def editSuccessScreen(request):
    return render(request, 'editSuccess.html')