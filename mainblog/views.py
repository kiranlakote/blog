from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    blogs = Post.objects.all()
    return render(request,'mainblog/post.html',{'blogs':blogs})


def blog(request, slug):
    blogs = Post.objects.get(slug=slug)
    allblogs = Post.objects.all()
    return render(request,'mainblog/singlepost.html',{'blog':blogs,'allblogs':allblogs})
