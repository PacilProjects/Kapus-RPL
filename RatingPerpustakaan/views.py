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
        print(request.user)
        list_perpus = list(BookBorrow.objects.all().filter(username = request.user.username).values_list('perpustakaan', flat=True))
        print(len(list_perpus))
        print('fail')
        return render(request, 'add_rating.html')
    peminjam = request.user
    # perpus = request.POST["nama_perpustakaan"]
    # skor = request.POST["score"]
    list_perpus = list(BookBorrow.objects.all().filter(username = request.user.username).values_list('perpustakaan', flat=True))
    print(list_perpus)
    if len(list_perpus) > 0 :
        print("HAI")
        response = {'list_perpus': list_perpus}
        return render(request, 'check_library.html', response)
    else :
        redirect('/')

@csrf_exempt
def available_library(request):
    perpus = request.POST["nama_perpustakaan"]
    choose_library = Rating.objects.all()  # TODO Implement this
    response = {'choose_library': choose_library}
    return render(request, 'check_availablity.html', response)

@csrf_exempt
def add_rating_suggestion(request, nama_perpus):
    if request.method == "POST":
        print("a")
        nama_perpustakaan_real = list(Perpustakaan.objects.all().values_list('nama', flat=True))
        ambil = Perpustakaan.objects.all()
        for i in range(0,len(ambil)):
            if nama_perpustakaan_real[i] != nama_perpus :
                continue
            else :
                # nama_perpus_hitung = CountRating.objects.only('nama_perpus_banget')
                # total_score = int(CountRating.objects.only('total_score'))
                # count_score = int(CountRating.objects.only('count_score'))
                # final_score = int(CountRating.objects.only('final_score'))
                # score_baru = request.POST['score']
                nama_perpus_hitung_set = list(CountRating.objects.all().values_list('nama_perpus_banget'))
                nama_perpus_hitung = nama_perpus_hitung_set[0][0]
                total_score_set = list(CountRating.objects.all().values_list('total_score'))
                total_score = int(total_score_set[0][0])        
                count_score_set = list(CountRating.objects.all().values_list('count_score'))
                count_score = count_score_set[0][0]
                final_score_set = list(CountRating.objects.all().values_list('final_score'))
                final_score = float(final_score_set[0][0])
                score_baru = int(request.POST['score'])
                print(total_score, count_score, final_score)

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

        return redirect("rating-perpustakaan/add/success/")

    else:
        name = nama_perpus
        return render(request, "add_rating.html", {'name':name})




register = template.Library()
@register.simple_tag
def divide(nilai_score, count_score):
    hasil = int(nilai_score / count_score)
    return int(nilai_score / count_score)

def success(request):
    return render(request, 'success.html')

def json(request):
    data = serializers.serialize('json', Rating.objects.all())
    return HttpResponse(data, content_type="application/json")