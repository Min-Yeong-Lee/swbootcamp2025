# snapfit/models.py

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 어떤 상품에 달린 댓글인지
    content = models.TextField()  # 댓글 내용
    create_date = models.DateTimeField(auto_now_add=True)  # 최초 시간
    modify_date = models.DateTimeField(auto_now=True)  # 수정 시간

    def __str__(self):
        return f'{self.author.username} - {self.content[:20]}'