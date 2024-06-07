from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from user.middlewares import auth

# Create your views here.

@auth
def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post, 'cats': cats})

def category(request, url):
    category_name = url.split('/')[-1]
    cat = Category.objects.get(url=f"{category_name}/")
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})