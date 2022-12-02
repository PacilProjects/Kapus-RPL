from django.contrib import admin

from .models import Buku

class BukuAdmin(admin.ModelAdmin):
    list_display = ("nama_buku", "nama_penulis", "isbn")

admin.site.register(Buku, BukuAdmin)