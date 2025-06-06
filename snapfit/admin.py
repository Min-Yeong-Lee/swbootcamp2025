from django.contrib import admin
from .models import Product, Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
