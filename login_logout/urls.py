from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),
    path('register/', registerUserKapus),
    path('register/success/', registerSuccess),
    path('register/failed/', registerFailed)
]
