from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'home.html',{'posts':posts})

def post(request):
    return HttpResponse("<h2>This is Post Page</h2>")

def category(request):
    return HttpResponse("<h2>This is Category Page</h2>")