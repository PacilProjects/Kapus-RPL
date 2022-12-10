from django.db import models
from datetime import date, datetime, timedelta

class RequestBooking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    username = models.CharField(default="name", max_length=50)
    book = models.CharField(max_length=50, default="buku")
    perpustakaan = models.CharField(default="perpustakaan", max_length=50)
    timestamp_request = models.DateTimeField(default=datetime.now, blank=True)
    is_reviewed = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)

class BookBorrow(models.Model):
    id_borrow = models.AutoField(primary_key=True)
    username = models.CharField(default="name", max_length=50)
    perpustakaan = models.CharField(default="perpustakaan", max_length=50)
    book = models.CharField(max_length=50, default="buku")
    status = models.CharField(max_length=50, default="Siap Diambil")
    timestamp_accepted = models.DateTimeField(default=datetime.now, blank=True)
    timestamp_retrieval_limit = models.DateField(default=(date.today() + timedelta(days=1)), blank=True)
    timestamp_return_limit = models.DateField(default=(date.today() + timedelta(days=7)), blank=True)
