from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def research(request):
    timeline = Timeline.objects.all()
    context = {
        'timeline': timeline,
    }
    return render(request, 'research.html', context)
