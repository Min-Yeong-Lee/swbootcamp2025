#pages_views.py

from django.shortcuts import render
from .models import MainContent  
from snapfit.models import Product

def mainpage(request):
    product_list = Product.objects.all()  # 상품 가져오기
    return render(request, 'pages/mainpage.html', {'product_list': product_list})  # 넘겨주기

def why(request):
    return render(request, 'pages/why_snapfit.html')

def app_download(request):
    return render(request, 'pages/app_download.html')

def contact(request):
    return render(request, 'pages/contact.html')