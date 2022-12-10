from django.urls import path
from .views import add_rating_suggestion, check_library, success, failed, perpustakaan

urlpatterns = [
    path('add/<str:nama_perpus>', add_rating_suggestion, name='add_rating_suggestion'),
    path('check-library/', check_library, name='check_library'),
    path('add/success/', success, name='success'),
    path('add/failed/', failed, name='failed'),
    path('daftar-perpustakaan/', perpustakaan, name='perpustakaan')
]