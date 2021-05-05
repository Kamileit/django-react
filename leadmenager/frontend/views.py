from django.shortcuts import render


# Create your views here.

def index(reguest):
    return render(reguest, 'frontend/index.html')
