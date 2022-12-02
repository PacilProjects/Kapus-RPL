from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
import psycopg2

connection = psycopg2.connect(
    database='postgres', 
    host='localhost', 
    port='5432', 
    user='postgres', 
    password='rlfdz3012')

def registerUser(request):
    userKapus = UserRegister(request.POST or None)
    if (userKapus.is_valid() and request.method == 'POST'):
        userKapus.save()
        return redirect('success/')
    
    response = {
        'userKapus': userKapus
    }

    return render(request, 'registration1.html', response)

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def checkUserNotExist(username):
    with connection.cursor() as c:
        c.execute("SELECT * FROM kapus.kapus_auth_user WHERE username='{}'".format(username))
        data = dictfetchall(c)
    
    return len(data)

def index(request):
    return render(request, 'index_login_logout.html')

def successScreen(request):
    return render(request, 'success.html')

def failedScreen(request):
    return render(request, 'failed.html')

def registerUserKapus(request):
    if request.method == 'POST':
        userKapus = UserRegisterForm(request.POST)
        if userKapus.is_valid():
            tipeUser = userKapus.cleaned_data['tipeUser']
            username = userKapus.cleaned_data['username']
            password = userKapus.cleaned_data['password']
            lokasi = userKapus.cleaned_data['lokasi']
            email = userKapus.cleaned_data['email']
            hp = userKapus.cleaned_data['hp']

            if checkUserNotExist(username) == 0:
                with connection.cursor() as c:
                    c.execute("""   INSERT INTO 
                                    kapus.kapus_auth_user
                                    VALUES 
                                    ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
                        tipeUser, username, password, lokasi, email, hp
                    ))
                request.session['role'] = tipeUser
                connection.commit()
                return redirect('success/')
            else:
                messages.error(request, 'User sudah terdaftar')
                return redirect('failed/')
    
    userKapus = UserRegisterForm()
    response = {'userKapus': userKapus}
    return render(request, 'registration.html', response)

def loginUserKapus(request):
    if request.method == 'POST':
        userKapusLogin = UserLoginForm(request.POST)
        if userKapusLogin.is_valid():
            username = userKapusLogin.cleaned_data['username']
            password = userKapusLogin.cleaned_data['password']
        
            with connection.cursor() as c:
                c.execute("""   SELECT  password
                                FROM    kapus.kapus_auth_user 
                                WHERE   username = '{}'""".format(username))
                data = dictfetchall(c)

                if data[0]['password'] == password:
                    return redirect('success/')
                else:
                    return redirect('failed/')

    userKapusLogin = UserLoginForm()
    response = {'userKapusLogin': userKapusLogin}
    return render(request, 'login.html', response)

def updatePassword(request, username):
    if request.method == 'POST':
        userKapusUpdatePassword = UpdatePasswordForm(request.POST)
        if userKapusUpdatePassword.is_valid():
            passwordUpdate = userKapusUpdatePassword.cleaned_data['password']
            
            with connection.cursor() as c:
                c.execute("""   UPDATE  kapus.kapus_auth_user
                                SET     password = '{}'
                                WHERE   username = '{}'""".format(passwordUpdate, username))