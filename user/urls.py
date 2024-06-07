from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
]