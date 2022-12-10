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
from django.urls import path, include
from AdministrasiPeminjam.views import peminjaman_offline, json_peminjaman_offline, dashboard, update_status, ubah_request, delete_request

urlpatterns = [
    path('offline/', peminjaman_offline, name='Index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/status/<str:id_borrow>', update_status, name='dashboard'),
    path('dashboard/request/<str:id_booking>', ubah_request, name='request'),
    path('dashboard/delete/<str:id_booking>', delete_request, name='delete'),
    path('json_peminjaman_offline/',json_peminjaman_offline, name='json_peminjaman_offline'),
]