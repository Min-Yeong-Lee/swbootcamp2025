#snapfit_urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list),
    path('product/', views.product_list),    # /product/ -> 제품 목록
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # 제품 상세
    path('comment/create/<int:product_id>/', views.comment_create, name='comment_create'),  # 댓글 작성
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),  # 댓글 수정
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),  # 댓글 삭제

]

