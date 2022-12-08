from django.http import response
from django.shortcuts import redirect, render
from SaranPenambahanBuku.models import SaranPenambahanBuku
from SaranPenambahanBuku.forms import PenambahanBukuForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
# from booking.models import BookBorrow
   

def add_book_suggestion(request):
    # print(request.user)
    # var_perpus = list(BookBorrow.objects.all().filter(username = request.user.username).values_list('perpustakaan', flat=True))
    # print(var_perpus)
    add_book_suggestion = PenambahanBukuForm(request.POST or None)
    if (add_book_suggestion.is_valid() and request.method == 'POST'):
        add_book_suggestion.save()
        return redirect('http://127.0.0.1:8000/saran-penambahan-buku/add/success/')
    response = {'add_book_suggestion':add_book_suggestion}
    return render(request, 'saran_penambahan_buku.html', response)

def success(request):
    return render(request, 'success.html')

def json(request):
    data = serializers.serialize('json', SaranPenambahanBuku.objects.all())
    return HttpResponse(data, content_type="application/json")