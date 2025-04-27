# snapfit_viesw.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Comment
from .forms import CommentForm
from django.core.exceptions import PermissionDenied

# 상품 리스트
def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'snapfit/content_list.html', {'product_list': product_list})

# 상품 상세 페이지
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'snapfit/content_detail.html', {'product': product})

# 댓글 작성
@login_required(login_url='/accounts/login/')
def comment_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    context = {'product': product, 'form': form}
    return render(request, 'snapfit/content_detail.html', context)

# 댓글 수정
@login_required(login_url='/accounts/login/')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('product_detail', product_id=comment.product.id)
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(request, 'snapfit/comment_form.html', context)

# 댓글 삭제
@login_required(login_url='/accounts/login/')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete()
    return redirect('product_detail', product_id=comment.product.id)
