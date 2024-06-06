from django.urls import path
from .views import home, post, category

urlpatterns = [
    path('home/', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category)
]