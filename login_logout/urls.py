from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),

    path('login/', kapusUserLogin),
    path('login/loginSuccess/', loginSuccessScreen),
    path('login/loginFailed/', loginFailedScreen),

    path('register/', kapusUserRegister),
    path('register/success/', successScreen),
    path('register/failed/', failedScreen),

    path('edit/', editUser),

    path('logout/', kapusUserLogout),
]
