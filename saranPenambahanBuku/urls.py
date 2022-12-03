from django.urls import path
from .views import add_book_suggestion, json

urlpatterns = [
    path('add/', add_book_suggestion, name='add_book_suggestion'),
    path('json/', json, name='json')
]