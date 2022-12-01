from django.urls import include, path
from .views import *

urlpatterns = [
    path('accounts/signup/', None, name='signup'),
    path('accounts/signup/pengguna/', None, name='signupPengguna'),
    path('accoutns/signup/adminPerpus/', None, name='signupAdminPerpus')
]