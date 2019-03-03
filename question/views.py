from django.shortcuts import render, redirect
import getpass # 현재 사용중인 유저 반환
from .models import Questions, Post
import random
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone 
# Create your views here.

global question
global all
all=Questions.objects.all()
question=random.choice(all)

def main(request):
    return render(request,'question/main.html')

def root(request):
    return redirect('/question/main/')
def allpost(request):
    allpost=Post.objects
    return render(request, 'question/allpost.html', {'allpost':allpost})




def post(request):
    # current user 받아오기

    # Question 객체 중 랜덤 반환
    # all=Questions.objects.all()
    # question=random.choice(all)
    return render(request, 'question/post.html', {'question':question})


def create(request):
    post=Post() 
    post.pub_date=timezone.datetime.now()
    post.answer=request.GET['answer']
    post.author=request.GET['author']
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