from .forms import *
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return None

def registerPengguna(request):
    return None

def registerAdminPerpus(request):
    return None

def registerRequestPengguna(request):
    form = PenggunaSignUpForm
    if request.is_ajax():
        form = PenggunaSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            
            return JsonResponse({
                'msg': 'Success'
            })
        else:
            
            return JsonResponse({
                'msg': 'Failed'
            })

def registerAdminPerpus(request):
    form = AdminPerpusSignUpForm
    if request.is_ajax():
        form = AdminPerpusSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        
            return JsonResponse({
                'msg': 'Success'
            })
        else:
            return JsonResponse({
                'msg': 'Success'
            })