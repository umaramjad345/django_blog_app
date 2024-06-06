from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h2>This is Home Page</h2>")

def post(request):
    return HttpResponse("<h2>This is Post Page</h2>")

def category(request):
    return HttpResponse("<h2>This is Category Page</h2>")