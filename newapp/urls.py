# newapp\urls.py
from django.urls import path
from .views import create_user , login_user , get_all_users

urlpatterns = [
    path('create-user/', create_user, name='create_user'),
    path('login/', login_user),
    path('get_all_users', get_all_users, name='get_all_users'),
]
