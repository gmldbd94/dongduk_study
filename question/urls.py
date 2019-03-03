from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('allpost/', views.allpost, name='allpost'),
    path('post/', views.post, name='post'), 
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('create/',views.create,name='create')
]