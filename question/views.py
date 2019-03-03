from django.shortcuts import render
import getpass # 현재 사용중인 유저 반환
from .models import Questions, Post
import random
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def main(request):
    return render(request, 'question/main.html')

def allpost(request):
    return render(request, 'question/allpost.html')

def post(request):
    # current user 받아오기

    # Question 객체 중 랜덤 반환
    all=Questions.objects.all()
    question=random.choice(all)
    return render(request, 'question/post.html', {'question':question})


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
            request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'question/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'question/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'question/login.html')