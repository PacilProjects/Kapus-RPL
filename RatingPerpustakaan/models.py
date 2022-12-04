from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from AdministrasiBuku.models import Perpustakaan


class Rating(models.Model):
    nama_perpus_temp = models.CharField(max_length=50, null=True)
    score = models.IntegerField(default=0,
        validators =[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    
class CountRating(models.Model):
    nama_perpus_banget = models.CharField(Perpustakaan.objects.all().values_list('nama'), max_length=50)
    total_score = models.IntegerField()
    count_score = models.IntegerField()
    final_score = models.DecimalField(max_digits=500, decimal_places=2)



