from django.urls import path
from .views import add_book_suggestion, json, success

urlpatterns = [
    path('add/', add_book_suggestion, name='add_book_suggestion'),
    path('add/success/', success, name='success'),
    path('json/', json, name='json')
]