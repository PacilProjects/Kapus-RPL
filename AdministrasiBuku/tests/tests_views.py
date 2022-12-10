from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from AdministrasiBuku.views import penambahan_buku, penambahan_perpus, json_buku, json_perpus, show_perpustakaan
from login_logout.models import AuthUserKapus

# Create your tests here.
class TestsUrls(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = AuthUserKapus(username='test', password='test', tipeUser='Pengelola')
        self.user2 = AuthUserKapus(username='test2', password='test', tipeUser='Pengguna')

    # Penambhaan Buku
    def test_status_penambahan_buku(self):
        request = self.factory.get('penambahan_buku')
        request.user = self.user
        response = penambahan_buku(request)
        self.assertEqual(response.status_code, 200)

    def test_status_penambahan_buku_is_not_pengelola(self):
        request = self.factory.get('penambahan_buku')
        request.user = self.user2
        response = penambahan_buku(request)
        self.assertEqual(response.status_code, 302)
    

    #Penambahan Perpus
    def test_status_penambahan_perpus(self):
        request = self.factory.get('penambahan_perpus')
        request.user = self.user
        response = penambahan_perpus(request)
        self.assertEqual(response.status_code, 200)

    def test_status_penambahan_perpus_is_not_pengelola(self):
        request = self.factory.get('penambahan_perpus')
        request.user = self.user2
        response = penambahan_buku(request)
        self.assertEqual(response.status_code, 302)

    
    
    