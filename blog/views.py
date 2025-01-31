from django.shortcuts import render
from .models import Posts

def blog(request):
    posts=Posts.objects.all()
    context={
        'posts':posts
    }
    return render(request, 'blog/blog.html', context)

def blogView(request,slug):
    posts=Posts.objects.get(slug=slug)
    related_post=Posts.objects.all()
    context={
        'posts':posts,
        'related_post':related_post

    }
    return render(request, 'blog/blog_detail.html', context)