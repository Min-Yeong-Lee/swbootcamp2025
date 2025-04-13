# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),   # 루트(/) -> 메인 페이지
    path('company/', views.company),    # /company/ -> 회사 소개
    
]
