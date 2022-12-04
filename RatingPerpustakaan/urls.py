from django.urls import path
from .views import add_rating_suggestion, json, check_library, success

urlpatterns = [
    path('add/<str:nama_perpus>', add_rating_suggestion, name='add_rating_suggestion'),
    path('check-library/', check_library, name='check_library'),
    path('add/success/', success, name='success'),
    path('json/', json, name='json')
]