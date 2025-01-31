from django.shortcuts import render
from .models import *


def index(request):
    hero_sections = HeroSection.objects.all()
    context = {
        'hero_sections': hero_sections, 
    }
    return render(request, 'index.html', context)