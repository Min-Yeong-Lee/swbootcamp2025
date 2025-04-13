# snapfit/views.py
from django.shortcuts import render
from .models import Product  # admin.py랑 일치시키게 

def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'snapfit/content_list.html', {'product_list': product_list})

