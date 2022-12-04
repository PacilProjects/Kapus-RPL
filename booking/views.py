import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core import serializers
from .models import RequestBooking, BookBorrow

def index(request):
    if request.method == "GET":
        request_model = RequestBooking.objects.all().filter(username=request.user.username).values()[::1]
        return JsonResponse(request_model, safe=False)

def booking(request):
    if request.method == "POST":
        book_name = request.POST["buku"]
        library = request.POST["perpustakaan"]
        user = request.user.username
        book = RequestBooking(username = user, book = book_name, perpustakaan = library)
        book.save()
        return redirect("listbooking")
    else:
        return render(request, "book.html", {})
    
def borrow(user, book_name, library):
    borrow = BookBorrow(username = user, perpustakaan = library, book = book_name)
    borrow.save()
    return borrow

def borrow_status(request):
    if request.method == "GET":
        borrow_model = BookBorrow.objects.all().filter(username=request.user.username).values()[::1]
        return JsonResponse(borrow_model, safe=False)