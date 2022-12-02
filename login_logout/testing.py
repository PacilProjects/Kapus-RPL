from django.contrib.auth import authenticate

user = authenticate(username='ardhani.dzaky', password='aabbcc')
print(user)