from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),
    path('register/', registerUser),
    path('login/', loginUser),
    path('login/loginSuccess/', loginSuccessScreen),
    path('register/success/', successScreen),
    path('register/failed/', failedScreen)
]
