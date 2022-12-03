from django.http import response
from django.shortcuts import redirect, render
from ratingPerpus.models import SaranPenambahanRating, Peminjam, Perpustakaan
from ratingPerpus.forms import PenambahanRatingForm, PerpustakaanForm, PeminjamForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
   
@csrf_exempt
def add_rating_suggestion(request):
    add_rating_suggestion = PenambahanRatingForm(request.POST or None)
    if (add_rating_suggestion.is_valid() and request.method == 'POST'):
        add_rating_suggestion.save()
        return redirect('rating-perpus/json')
    response = {'add_rating_suggestion':add_rating_suggestion}
    return render(request, 'add_rating.html', response)

@csrf_exempt
def add_perpus(request):
    add_perpus = PerpustakaanForm(request.POST or None)
    if (add_perpus.is_valid() and request.method == 'POST'):
        print("HAI")
        add_perpus.save()
        return redirect('rating-perpus/json')
    response = {'add_perpus':add_perpus}
    return render(request, 'add_perpus.html', response)

@csrf_exempt
def add_peminjam(request):
    add_peminjam = PerpustakaanForm(request.POST or None)
    if (add_peminjam.is_valid() and request.method == 'POST'):
        print("cekPinjem")
        add_peminjam.save()
        return redirect('rating-perpus/json')
    response = {'add_peminjam':add_peminjam}
    return render(request, 'add_peminjam.html', response)


def json(request):
    data = serializers.serialize('json', SaranPenambahanRating.objects.all())
    return HttpResponse(data, content_type="application/json")