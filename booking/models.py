from django.db import models
from datetime import date, datetime, timedelta

class RequestBooking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    username = models.ForeignKey("login_logout.AuthUserKapus", on_delete=models.CASCADE, null=True)
    timestamp_request = models.DateTimeField(default=datetime.now, blank=True)
    is_reviewed = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    book = models.CharField(max_length=50, default="buku")

class BookBorrow(models.Model):
    id_borrow = models.AutoField(primary_key=True)
    username = models.ForeignKey("login_logout.AuthUserKapus", on_delete=models.CASCADE, null=True)
    timestamp_accepted = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=50, default="Siap Diambil")
    timestamp_retrieval_limit = models.DateField(default=date.today, blank=True)
    timestamp_return_limit = models.DateField(default=(date.today() + timedelta(days=7)), blank=True)
    timestamp_retrieval_limit = models.DateField(null=True)
