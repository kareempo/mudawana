from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

# Create your views here.
def home(req):
    post=Post()

    context ={
         'title':'Main Page',
         'posts':Post.objects.all()
         }
    

    return render(req , 'blog/index.html',context)


def about(req):
    context={'title':'من أنا'}
    return render(req , 'blog/about.html',context)
