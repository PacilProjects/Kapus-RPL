from django.contrib import admin
from django.urls import path, include
from booking.views import index, booking, borrow, borrow_status

urlpatterns = [
    path('', index, name='listbooking'),
    path('book/', booking, name='book'),
    path('borrow/', borrow, name='borrow'),
    path('borrow-status/', borrow_status, name='borrow-status'),
]