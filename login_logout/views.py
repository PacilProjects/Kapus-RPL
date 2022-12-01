from .forms import *
from django.shortcuts import render, redirect
from django.contrib import messages
import psycopg2

connection = psycopg2.connect(
    database='postgres', 
    host='localhost', 
    port='5432', 
    user='postgres', 
    password='')

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

def registerSuccess(request):
    return render(request, 'success.html')

def registerFailed(request):
    return render(request, 'failed.html')

def registerUserKapus(request):
    if request.method == 'POST':
        userKapus = userPenggunaPengelola(request.POST)
        if userKapus.is_valid():
            tipeUser = userKapus.cleaned_data['tipeUser']
            username = userKapus.cleaned_data['username']
            password = userKapus.cleaned_data['password']
            lokasi = userKapus.cleaned_data['lokasi']
            email = userKapus.cleaned_data['email']
            hp = userKapus.cleaned_data['hp']

            if checkUserNotExist(username) == 0:
                with connection.cursor() as c:
                    c.execute("INSERT INTO kapus.kapus_auth_user VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
                        tipeUser, username, password, lokasi, email, hp
                    ))
                request.session['role'] = tipeUser
                connection.commit()
                return redirect('success/')
            else:
                messages.error(request, 'User sudah terdaftar')
                return redirect('failed/')
    
    userKapus = userPenggunaPengelola()
    response = {'userKapus': userKapus}
    return render(request, 'registration.html', response)