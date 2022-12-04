from django.shortcuts import HttpResponseRedirect, render, redirect
from django.core import serializers
from AdministrasiBuku.forms import NewBook, NewPerpustakaan
from AdministrasiBuku.models import Buku, Perpustakaan, PerpusBuku
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def penambahan_stok(request):
    if request.user.tipeUser == 'Pengelola':
        if request.method == 'POST':
            data = request.POST
            buku = Buku.objects.get(nama_buku=data['buku'])
            perpus = Perpustakaan.objects.get(nama=data['perpustakaan'])

            try:
                kuantitas = PerpusBuku.objects.get(isbn_id=buku, nama_perpus_id=perpus)
                kuantitas.kuantitas += int(data['jumlah'])
                kuantitas.save()
            except:
                buku.perpustakaan.add(perpus)
                kuantitas = PerpusBuku.objects.get(isbn_id=buku.isbn, nama_perpus_id=perpus.nama)
                kuantitas.kuantitas = data['jumlah']
                kuantitas.save()

        response = {'perpus': show_perpustakaan(request), 'buku': show_buku(request)}
        return render(request, 'add_buku_to_perpus.html', response)
    else:
        return HttpResponseRedirect('/')


def penambahan_buku(request):
    if request.user.tipeUser == 'Pengelola':
        if request.method == 'POST':
            data = request.POST
            new_book = Buku(nama_buku=data['nama_buku'], isbn=data['isbn'], penulis=data['penulis'], penerbit=data['penerbit'])
            new_book.save()
        return render(request, 'penambahan_buku.html')
    else:
        return HttpResponseRedirect('/')

def penambahan_perpus(request):
    if request.user.tipeUser == 'Pengelola':
        new_perpus = NewPerpustakaan(request.POST or None)
        if new_perpus.is_valid() and request.method == 'POST':
            new_perpus.save()
            return redirect('json_perpus')
        response = {'new_perpus': new_perpus}
        return render(request, 'penambahan_perpustakaan.html', response)
    else:
        return HttpResponseRedirect('/')

def show_perpustakaan(request):
    perpus = Perpustakaan.objects.only('nama')
    name = []
    for i in perpus:
        name.append(i.nama)
    return name

def show_buku(request):
    buku = Buku.objects.only('nama_buku')
    name = []
    for i in buku:
        name.append(i.nama_buku)
    return name

def json_buku(request):
    data = serializers.serialize('json', Buku.objects.all())
    return HttpResponse(data, content_type="application/json")

def json_perpus(request):
    data = serializers.serialize('json', Perpustakaan.objects.all())
    return HttpResponse(data, content_type="application/json")