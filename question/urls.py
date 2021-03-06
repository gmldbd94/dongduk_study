from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name='mypage'),
    path('main/', views.main, name='main'),
    path('allpost/', views.allpost, name='allpost'),
    path('post', views.post, name='post'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('create/',views.create,name='create'),
    path('logout/', views.logout, name='logout'),
    path('', views.allpost, name='allpost'),

    #댓글 기능
    path('<int:post_id>/comments', views.comments, name='comments'),
    path('<int:post_id>/comments/<int:comment_id>/delete', views.commnet_delete, name='comment_delete'),
    path('<int:post_id>/comments/<int:comment_id>/edit', views.commnet_update, name='comment_update'),
]