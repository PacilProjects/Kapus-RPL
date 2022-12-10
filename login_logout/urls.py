from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index),

    path('login/', kapusUserLogin),
    path('login/loginFailed/', loginFailedScreen),
    path('login/loginSuccess/', loginSuccessScreen),

    path('forgot/', forgetPassword),
    path('forgot/forgotFailed/', forgotFailedScreen),
    path('forgot/forgotSuccess/', forgotSuccessScreen),

    path('profile/', profile),
    path('profile/changeSuccess/', editSuccessScreen),
    path('profile/changeFailed/', editFailedScreen),

    path('register/', kapusUserRegister),
    path('register/registerFailed/', registerFailedScreen),
    path('register/registerSuccess/', registerSuccessScreen),

    path('edit/', editUser),
    path('editPerpustakaan/', addPerpustakaan),

    path('logout/', kapusUserLogout),
]
