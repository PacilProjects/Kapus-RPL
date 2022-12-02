from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),
    path('register/', registerUserKapus),
    path('register1/', registerUser),
    path('login/', loginUserKapus),
    path('register/success/', successScreen),
    path('register/failed/', failedScreen)
]
