#snapfit_urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('product/', views.product_list),    # /product/ -> 제품 목록
]
