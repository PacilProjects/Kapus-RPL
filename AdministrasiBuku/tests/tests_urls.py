from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from AdministrasiBuku.views import penambahan_buku, penambahan_perpus, json_buku, json_perpus, show_perpustakaan
from login_logout.models import AuthUserKapus

# Create your tests here.
class TestsUrls(TestCase):

    # Penambhaan Buku
    def test_url_is_resolved_penambahan_buku(self):
        url = reverse('penambahan_buku')
        self.assertEquals(resolve(url).func, penambahan_buku)

    def test_url_is_resolved_penambahan_perpus(self):
        url = reverse('penambahan_perpus')
        self.assertEquals(resolve(url).func, penambahan_perpus)


    def test_url_is_resolved_json_buku(self):
        url = reverse('json_buku')
        self.assertEquals(resolve(url).func, json_buku)
    
    def test_url_is_resolved_json_perpus(self):
        url = reverse('json_perpus')
        self.assertEquals(resolve(url).func, json_perpus)
        
    def test_url_is_resolved_show_perpustakaan(self):
        url = reverse('show_perpustakaan')
        self.assertEquals(resolve(url).func, show_perpustakaan)
    
    