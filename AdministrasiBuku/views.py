from django.shortcuts import render, redirect
from django.core import serializers
from AdministrasiBuku.forms import NewBook, NewPerpustakaan
from AdministrasiBuku.models import Buku, Perpustakaan
from django.http.response import HttpResponse

# Create your views here.

def penambahan_buku(request):

    new_book = NewBook(request.POST or None)
    if new_book.is_valid() and request.method == 'POST':
        new_book.save()
        return redirect('json_buku')
    response = {'new_book': new_book}
    return render(request, 'penambahan_buku.html', response)

def penambahan_perpus(request):
    new_perpus = NewPerpustakaan(request.POST or None)
    if new_perpus.is_valid() and request.method == 'POST':
        new_perpus.save()
        return redirect('json_perpus')
    response = {'new_perpus': new_perpus}
    return render(request, 'penambahan_perpustakaan.html', response)

def json_buku(request):
    data = serializers.serialize('json', Buku.objects.all())
    return HttpResponse(data, content_type="application/json")

def json_perpus(request):
    data = serializers.serialize('json', Perpustakaan.objects.all())
    return HttpResponse(data, content_type="application/json")