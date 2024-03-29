"""kapusrpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from AdministrasiBuku import views
urlpatterns = [
    path('Form-Buku/', views.penambahan_buku, name='penambahan_buku'),
    path('Form-Perpus/', views.penambahan_perpus, name='penambahan_perpus'),
    path('penambahan-stok/', views.penambahan_stok, name='penambahan_stok'),
    path('json_buku/', views.json_buku, name='json_buku'),
    path('json_perpus/', views.json_perpus, name='json_perpus'),
    path('show/', views.show_perpustakaan, name='show_perpustakaan'),
    re_path(r'^checkisbn/$', views.checkisbn, name='checkuser'),
    re_path(r'^checkperpus/$', views.checkperpus, name='checkperpus'),
]
