from datetime import datetime
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from AdministrasiBuku.models import Buku, Perpustakaan, PerpusBuku
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
    if request.user.is_authenticated and request.user.tipeUser == 'Pengelola':
        if request.method == 'POST':
            data = request.POST
            print(data)
            isbn = Buku.objects.only('isbn').get(nama_buku=data['buku'])
            target = borrow(user=data['username'], book_name=isbn.isbn, library=request.user.perpustakaanKerjaModel_id)
            target.status = 'Sedang Dipinjam'
            target.save()
            kuantitas = PerpusBuku.objects.get(nama_perpus_id=request.user.perpustakaanKerjaModel_id, isbn_id=isbn.isbn)
            kuantitas.kuantitas = kuantitas.kuantitas - 1
            kuantitas.save()
            return HttpResponseRedirect('/')

        buku = PerpusBuku.objects.all().filter(nama_perpus_id=request.user.perpustakaanKerjaModel_id).values_list('isbn_id', flat=True)
        target = Buku.objects.all().filter(isbn__in=buku).values_list('nama_buku', flat=True)
        response = {'peminjaman_buku': target, 'perpus': request.user.perpustakaanKerjaModel_id}
        return render(request, 'peminjaman_offline.html', response)
    else:
        return HttpResponseRedirect('/')

def json_peminjaman_offline(request):
    data = serializers.serialize('json', PeminjamanOffline.objects.all())

    return HttpResponse(data, content_type="application/json")

def dashboard(request):
    if request.user.is_authenticated and request.user.tipeUser == 'Pengelola':
        book_borrow = BookBorrow.objects.all().filter(perpustakaan=request.user.perpustakaanKerjaModel_id)
        request_booking = RequestBooking.objects.all().filter(perpustakaan=request.user.perpustakaanKerjaModel_id)
        print(Perpustakaan.objects.filter(nama="Perpus1").exists())
        response = {'perpus': show_perpustakaan(request), 'book_borrow': book_borrow, 'request_booking': request_booking}
        return render(request, 'dashboard.html', response)
    else:
        return HttpResponseRedirect('/')


def ubah_request(request, id_booking):
    if request.user.is_authenticated and request.user.tipeUser == 'Pengelola':
        request_booking = RequestBooking.objects.get(id_booking=id_booking)
        buku = Buku.objects.get(isbn=request_booking.book)
        response = {"request": request_booking, 'buku': buku}
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

def update_status(request, id_borrow):
    if request.user.is_authenticated and request.user.tipeUser == 'Pengelola':
        book_borrow = BookBorrow.objects.get(id_borrow=id_borrow)
        buku = Buku.objects.get(isbn=book_borrow.book)
        response = {"book": book_borrow, 'buku': buku}
        if request.method == "POST":
            data = request.POST
            book_borrow.status = data['status']
            book_borrow.save()
            target_buku = PerpusBuku.objects.get(isbn_id=book_borrow.book, nama_perpus_id=book_borrow.perpustakaan)
            target_buku.kuantitas = target_buku.kuantitas - 1
            target_buku.save()
            return HttpResponseRedirect('../')
        return render(request, 'ubah_status.html', response)
    else:
        return HttpResponseRedirect('/')

def delete_request(request, id_booking):
    if request.user.is_authenticated and request.user.tipeUser == 'Pengelola':
        request_booking = RequestBooking.objects.get(id_booking=id_booking)
        request_booking.delete()
        return HttpResponseRedirect('../')


#make a function to check username availability using javascript
def checkuser(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': AuthUserKapus.objects.filter(username=username).exists()
    }
    return JsonResponse(data)