from datetime import datetime
import json
from django.shortcuts import redirect, render
from AdministrasiPeminjam.models import PeminjamanOffline
from AdministrasiPeminjam.forms import PeminjamanOfflineForm
from django.core import serializers
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from AdministrasiBuku.models import Buku
from AdministrasiBuku.views import show_perpustakaan
from booking.models import RequestBooking, BookBorrow
from booking.views import borrow
from login_logout.models import AuthUserKapus
from django.contrib.sessions.models import Session
# Create your views here.

@csrf_exempt
def peminjaman_offline(request):
    if request.user.tipeUser == 'Pengelola':
        peminjaman_buku = PeminjamanOfflineForm(json.loads(request.body) or None) #Nanti ganti jadi request.POST
        print(json.loads(request.body)['nama_buku'])
        if peminjaman_buku.is_valid() and request.method == 'POST':
            peminjaman_buku.save()
            buku = Buku.objects.get(isbn=json.loads(request.body)['nama_buku'])
            buku.banyak = buku.banyak - 1
            buku.save()
            return redirect('json_buku')
        response = {'peminjaman_buku': peminjaman_buku}
        return render(request, 'penambahan_buku.html', response)
    else:
        return HttpResponseRedirect('/')

def json_peminjaman_offline(request):
    data = serializers.serialize('json', PeminjamanOffline.objects.all())

    return HttpResponse(data, content_type="application/json")

def dashboard(request):
    if request.user.tipeUser == 'Pengelola':
        book_borrow = BookBorrow.objects.all()
        request_booking = RequestBooking.objects.all()
        response = {'perpus': show_perpustakaan(request), 'book_borrow': book_borrow, 'request_booking': request_booking}
        return render(request, 'dashboard.html', response)
    else:
        return HttpResponseRedirect('/')


def ubah_request(request, id_booking):
    if request.user.tipeUser == 'Pengelola':
        request_booking = RequestBooking.objects.get(id_booking=id_booking)
        response = {"request": request_booking}
        print(datetime.now())
        if request.method == "POST":
            data = request.POST
            user = RequestBooking.objects.get(id_booking=id_booking)
            if data['option2']== "True":
                user.is_accepted = True
                auth_user = AuthUserKapus.objects.get(username= user.username)
                borrow(auth_user, user.book, user.perpustakaan)
            else:
                user.is_accepted = False
            user.is_reviewed = True
            user.save()
            return HttpResponseRedirect('../')
        return render(request, 'ubah_request.html', response)
    else:
        return HttpResponseRedirect('/')

def update_status(request, username):
    if request.user.tipeUser == 'Pengelola':
        book_borrow = BookBorrow.objects.get(username=username)
        response = {"book": book_borrow}
        if request.method == "POST":
            data = request.POST
            user = BookBorrow.objects.get(username=username)
            user.status = data['status']
            user.save()
            return HttpResponseRedirect('../')
        return render(request, 'ubah_status.html', response)
    else:
        return HttpResponseRedirect('/')