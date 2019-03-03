from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'question/main.html')

def allpost(request):
    return render(request, 'question/allpost.html')

def post(request):
    return render(request, 'question/post.html')