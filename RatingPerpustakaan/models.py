from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class SaranPenambahanRating(models.Model):
    nama_perpus = models.CharField(max_length=50)
    score = models.IntegerField(default=0,
        validators =[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    
    def __str__(self):
        return str(self.pk)
   
class Perpustakaan(models.Model):
    nama_perpus = models.CharField(max_length=20)


