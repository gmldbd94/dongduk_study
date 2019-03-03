from django.shortcuts import render
import getpass # 현재 사용중인 유저 반환
from .models import Questions, Post
import random
# Create your views here.


def main(request):
    return render(request, 'question/main.html')

def allpost(request):
    return render(request, 'question/allpost.html')

def post(request):
    all=Questions.objects.all()
    question=random.choice(all)
    return render(request, 'question/post.html', {'question':question})