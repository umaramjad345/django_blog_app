from django.urls import path
from .views import home, post, category, about

urlpatterns = [
    path('home/', home),
    path('blog/<slug:url>/', post),
    path('category/<slug:url>/',category),
    path('about/', about),
]