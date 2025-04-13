from django.shortcuts import render
from .models import MainContent  

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

