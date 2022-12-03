
from django.contrib import admin
from django.urls import path, include
from booking.views import index, booking, borrow_status

urlpatterns = [
    path('', index, name='listbooking'),
    path('book/', booking, name='book'),
    path('borrow-status/', borrow_status, name='borrow-status'),
]