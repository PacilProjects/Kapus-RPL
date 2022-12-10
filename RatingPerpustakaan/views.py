from django.http import response
from django.shortcuts import redirect, render
from RatingPerpustakaan.models import Rating, CountRating
from RatingPerpustakaan.forms import RatingForm
from booking.models import BookBorrow
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import template
from AdministrasiBuku.models import Perpustakaan

@csrf_exempt
def index(request):
    if request.method == "GET":
        var_rating = Rating.objects.all()

@csrf_exempt
def check_library(request):
    if request.method == "POST":
        list_perpus = set(list(BookBorrow.objects.all().filter(username = request.user.username).values_list('perpustakaan', flat=True)))
        return render(request, 'add_rating.html')
    list_perpus = set(list(BookBorrow.objects.all().filter(username = request.user.username).values_list('perpustakaan', flat=True)))

    if len(list_perpus) > 0 :
        response = {'list_perpus': list_perpus}
        return render(request, 'check_library.html', response)
    else :
        return redirect("/rating-perpustakaan/add/failed/")

@csrf_exempt
def add_rating_suggestion(request, nama_perpus):
    if request.method == "POST":
        nama_perpustakaan_real = list(Perpustakaan.objects.all().values_list('nama', flat=True))
        ambil = Perpustakaan.objects.all()
        for i in range(0,len(ambil)):
            if nama_perpustakaan_real[i] != nama_perpus :
                continue
            else :
                query = CountRating.objects.all()
                list_perpus = list(CountRating.objects.all().filter(nama_perpus_banget = nama_perpus).values_list('nama_perpus_banget', flat=True))
                print(list_perpus)
                if not query or len(list_perpus) == 0:
                    score_baru = int(request.POST['score'])
                    total_score = score_baru
                    count_score = 1
                    final_score = divide(total_score, count_score)
                    rate = Rating(nama_perpus_temp = nama_perpus, score = score_baru)
                    rate.save()
                    rate_final = CountRating(nama_perpus_banget = nama_perpus, total_score = total_score, count_score = count_score, final_score = final_score)
                    rate_final.save()

                else :
                    total_score_set = list(CountRating.objects.all().filter(nama_perpus_banget = nama_perpus).values_list('total_score'))
                    total_score = int(total_score_set[0][0])        
                    count_score_set = list(CountRating.objects.all().filter(nama_perpus_banget = nama_perpus).values_list('count_score'))
                    count_score = count_score_set[0][0]
                    final_score_set = list(CountRating.objects.all().filter(nama_perpus_banget = nama_perpus).values_list('final_score'))
                    final_score = float(final_score_set[0][0])
                    score_baru = int(request.POST['score'])

                    total_score += score_baru 
                    count_score += 1
                    final_score = divide(total_score, count_score)
                    rate = Rating(nama_perpus_temp = nama_perpus, score = score_baru)
                    rate_final = CountRating.objects.get(nama_perpus_banget = nama_perpus)
                    rate.save()
                    rate_final.total_score = total_score
                    rate_final.count_score = count_score
                    rate_final.final_score = final_score
                    rate_final.save()

        return redirect("/rating-perpustakaan/add/success/")

    else:
        name = nama_perpus
        return render(request, "add_rating.html", {'name':name})


register = template.Library()
@register.simple_tag
def divide(nilai_score, count_score):
    print(float(nilai_score / count_score))
    hasil = float(nilai_score / count_score)
    print(round(hasil, 2))
    return round(hasil, 2)

@csrf_exempt
def success(request):
    return render(request, 'success.html')

@csrf_exempt
def failed(request):
    return render(request, 'failed.html')

@csrf_exempt
def perpustakaan(request):
    # base_perpus = Perpustakaan.objects.all()
    # rating_perpus = list(CountRating.objects.all().filter(nama_perpus_banget = nama_perpus).values_list('final_score'))
    # response = {'base_perpus':base_perpus}
    return render(request, 'perpustakaan.html', response)