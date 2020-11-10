from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
# def index(request):
#     context = {
#         'post' : {
#             'Author' : 'SH',
#             'Body' : 'Programming'
#         },
#         'numbers' : [1, 5, 2, 3, 4]
#     }
#     return render(request, 'posts/index.html', context)
# Python에서 dict내 값을 가져오려면, context[post][Author]라고 사용하면 됨
# 그러나 Django에서는 해당 값을 post.Author라고 HTML에 작성해야 함

## 201013
# def index(request) : 
#     posts = Post.objects.all()
#     context = {'posts' : posts}
#     return render(request, 'posts/index.html', context)

## 201020
# def index(request) :
#     posts = Post.objects.filter(author='SH_1').order_by('-created_at')
#     context = { 'posts' : post}
#     return render(request, 'posts/index.html', context)

def index(request) :
    posts = Post.objects.all()
    context = { 'posts' : posts }
    return render(request, 'posts/index.html',context)

def detail(request, post_id) : # request 다음에 변수명을 적어주어야 한다.
    post = Post.objects.get(id=post_id)
    context = { 'post' : post }
    return render(request, 'posts/detail.html', context)


@login_required
def new(request) :
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
    return render(request, 'posts/new.html')


@login_required
def create(request) :
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
    # author = request.POST['author'] # request.POST 라는 딕셔너리에서 'author'라는 key의 value를 가져와서 author에 저장
    user = request.user
    body = request.POST['body']

    image = None
    if 'image' in request.FILES:
        image = request.FILES['image']

    # post = Post(author = author, body = body, created_at=timezone.now())
    post = Post(user=user, body=body, image = image, created_at=timezone.now())
    post.save()
    return redirect('posts:index')
    # return redirect('posts:detail' post_id=post.id) # detail로 정의하고 싶으면 post_id를 정의해줘야 함


@login_required
def edit(request, post_id) :
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')
    # post = Post.objects.get(id=post_id)
    context = {'post' : post }
    return render(request, 'posts/edit.html', context)


@login_required
def update(request, post_id) :
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    # post = Post.objects.get(id=post_id)
    # post.author = request.POST['author'] # request.POST 라는 딕셔너리에서 'author'라는 key의 value를 가져와서 author에 저장
    post.body = request.POST['body']

    if 'image' in request.FILES:
        post.image = request.FILES['image']
    post.save()
    return redirect('posts:detail', post_id=post.id)


@login_required
def delete(request, post_id) :
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    # post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:index')

@login_required
def like(request, post_id) :
    if request.method == 'POST' :
        try:
            post = Post.objects.get(id=post_id)

            if request.user in post.liked_users.all():
                post.liked_users.remove(request.user)            
            else :
                post.liked_users.add(request.user)
            return redirect('posts:detail', post.id)

        except Post.DoesNotExist:
            pass

    return redirect('posts:index')
