import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core import serializers
from .models import RequestBooking, BookBorrow

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "GET":
        request_model = RequestBooking.objects.all().filter(username=request.user).values()[::1]
        return JsonResponse(request_model, safe=False)

@csrf_exempt
def booking(request):
    if request.method == "POST":
        book_name = request.POST["buku"]
        print(book_name)
        user = request.user
        book = RequestBooking(username = user, book = book_name)
        book.save()
        return redirect("Index")
    else:
        return render(request, 'book.html', {})
    
@csrf_exempt
def borrow(request):
    if request.method == "POST":
        print(request.user)
        user = request.user.username
        borrow = BookBorrow(username = user)
        borrow.save()
        return HttpResponse(status=200)
    else:
        return redirect("book")

@csrf_exempt
def borrow_status(request):
    if request.method == "GET":
        borrow_model = BookBorrow.objects.all().values()[::1]
        return JsonResponse(borrow_model, safe=False)