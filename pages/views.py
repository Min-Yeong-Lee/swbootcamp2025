#pages_views.py

from django.shortcuts import render
from .models import MainContent  

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def why(request):
    return render(request, 'pages/why_snapfit.html')

def app_download(request):
    return render(request, 'pages/app_download.html')

def contact(request):
    return render(request, 'pages/contact.html')