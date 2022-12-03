from django.http import response
from django.shortcuts import redirect, render
from saranPenambahanBuku.models import SaranPenambahanBuku
from saranPenambahanBuku.forms import PenambahanBukuForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import HttpResponse
   

def add_book_suggestion(request):
    add_book_suggestion = PenambahanBukuForm(request.POST or None)
    if (add_book_suggestion.is_valid() and request.method == 'POST'):
        add_book_suggestion.save()
        return redirect('/json')
    response = {'add_book_suggestion':add_book_suggestion}
    return render(request, 'saran_penambahan_buku.html', response)

def json(request):
    data = serializers.serialize('json', SaranPenambahanBuku.objects.all())
    return HttpResponse(data, content_type="application/json")