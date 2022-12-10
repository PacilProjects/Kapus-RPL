from django.http import response
from django.shortcuts import redirect, render
from SaranPenambahanBuku.models import SaranPenambahanBuku
from SaranPenambahanBuku.forms import PenambahanBukuForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from booking.models import BookBorrow
   
@csrf_exempt
def add_book_suggestion(request):
    add_book_suggestion = PenambahanBukuForm(request.POST or None)
    if (add_book_suggestion.is_valid() and request.method == 'POST'):
        add_book_suggestion.save()
        return redirect('http://127.0.0.1:8000/saran-penambahan-buku/add/success/')
    response = {'add_book_suggestion':add_book_suggestion}
    return render(request, 'saran_penambahan_buku.html', response)

@csrf_exempt
def success(request):
    return render(request, 'success.html')