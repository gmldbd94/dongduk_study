from django.shortcuts import render
import getpass # 현재 사용중인 유저 반환
# Create your views here.


def main(request):
    return render(request, 'question/main.html')

def allpost(request):
    return render(request, 'question/allpost.html')

def post(request):
    return render(request, 'question/post.html')