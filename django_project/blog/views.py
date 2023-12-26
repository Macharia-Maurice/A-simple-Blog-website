from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Blog-home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog-about</h1')

posts=[
    {
        'author':'Maurice',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date-posted':'May 6,2024'
    },
    {
        'author':'Sharlene',
        'title': 'Blog post 2',
        'content': '2nd post content',
        'date-posted':'March 16,2024'
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
