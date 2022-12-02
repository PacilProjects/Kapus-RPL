import json
from django.shortcuts import redirect, render
from AdministrasiPeminjam.models import PeminjamanOffline
from AdministrasiPeminjam.forms import PeminjamanOfflineForm
from django.core import serializers
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from AdministrasiBuku.models import Buku
# Create your views here.

@csrf_exempt
def peminjaman_offline(request):
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

def json_peminjaman_offline(request):
    data = serializers.serialize('json', PeminjamanOffline.objects.all())
    return HttpResponse(data, content_type="application/json")