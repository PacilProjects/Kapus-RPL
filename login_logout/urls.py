from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),

    path('login/', kapusUserLogin),
    path('profile/', loginSuccessScreen),
    path('login/loginFailed/', loginFailedScreen),

    path('register/', kapusUserRegister),
    path('register/success/', successScreen),

    path('edit/', editUser),
    path('editPerpustakaan/', addPerpustakaan),

    path('logout/', kapusUserLogout),
]
