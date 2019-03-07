from django.shortcuts import render, redirect
import getpass # 현재 사용중인 유저 반환
from .models import Questions, Post
from . import models
import random
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from . import form as form_field
from operator import eq
# Create your views here.

#
global question
global all
all=Questions.objects.all()
question=random.choice(all)
# global 사용한 이유 : user - question 을 연결하기 위해


def main(request):
    return render(request,'question/main.html')

def root(request):
    return redirect('/question/main/')
    
def allpost(request):
    allpost = Post.objects.all()
    return render(request, 'question/allpost.html', {'allpost':allpost})




def post(request):
    # current user 받아오기
    # Question 객체 중 랜덤 반환
    all=Questions.objects.all()
    question=random.choice(all)
    return render(request, 'question/post.html', {'question':question})


def create(request):
    post=Post() 
    post.pub_date=timezone.datetime.now()
    post.answer=request.GET['answer']
    post.author=request.user # 로그인한 사용자의 이름을 받아온다.
    post.question=question
    post.save()
    # 객체.delete()는 이 데이터객체를 지워라
    return redirect('/question/main')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/question/main')
    return render(request, 'question/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('question/main.html')
        else:
            return render(request, 'question/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'question/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/question/main/')
    return render(request, 'question/signup.html')

def mypage(request):
    post_list=list()
    allpost=Post.objects.all()
    for post in allpost:
        if str(request.user)==post.author:
            # request.user 와 post.author의 타입이 달라 str() 로 맞춰줌
            post_list.append(post.answer)
    return render(request, 'question/mypage.html',{'allpost':post_list})

#댓글 작성
def comments(request, post_id):
    form = form_field.CommentForm(request.POST or None)
    if form.is_valid():
        print("create")
        comment = form.save()
        comment.post = models.User.objects.get(pk=post_id)
        comment.save
        redirect('comment_create', {'post_id':post_id})

    redirect('allpost')


# 댓글 삭제
def commnet_delete(reqeust, post_id, comment_id):
    pass
# 댓글 수정
def commnet_update(reqeust, post_id, comment_id):
    pass
# 댓글 보기
# def commnets(request, post_id):
#     pass