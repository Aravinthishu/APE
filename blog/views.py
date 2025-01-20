from django.shortcuts import render
from .models import Posts

def blog(request):
    posts=Posts.objects.filter(is_active=True)
    return render(request, 'blog.html', {'posts':posts})


