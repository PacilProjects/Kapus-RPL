from django.urls import path
from .views import add_rating_suggestion, json, add_perpus

urlpatterns = [
    path('add/', add_rating_suggestion, name='add_rating_suggestion'),
    # path('peminjam/', add_peminjam, name='add_peminjam'),
    path('perpustakaan/', add_perpus, name='add_perpus'),
    path('json/', json, name='json')
]