from django.shortcuts import render
from django.db.models import Q

from AdministrasiBuku.models import Buku, PerpusBuku


def search(request):
    return render(request, 'search.html')

def search_results(request):
    # for ease of reference
    search_query = request.POST.get('search_query', 'search_query')
    search_type  = request.POST.get('search_type' , 'search_type')

    # return results based on query type
    if (search_type == "nama_buku"):
        results = Buku.objects.filter(Q(nama_buku__icontains=search_query))

    elif (search_type == "nama_penulis"):
        results = Buku.objects.filter(Q(penulis__icontains=search_query))

    elif (search_type == "isbn"):
        results = Buku.objects.filter(Q(isbn__icontains=search_query))

    # package as dict & return
    response = {'buku_list': results}

    return render(request, 'search_results.html', response)

def search_available(request):
    # for ease of reference
    search_query = request.POST.get('search_query', 'search_query')
    
    isbn = Buku.objects.get(nama_buku=search_query).isbn
    results = PerpusBuku.objects.filter(isbn=isbn)

    # package as dict & return
    response = {'buku_list': results}

    return render(request, 'search_available.html', response)
