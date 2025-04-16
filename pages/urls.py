# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),  #name:네이밍 해줘서 하드코딩 방지
    path('why/', views.why, name='why'),
    path('download/', views.app_download, name='download'),
    path('contact/', views.contact, name='contact'),
]
