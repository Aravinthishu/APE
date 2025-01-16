from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    hero_sections = HeroSection.objects.all()  # Renaming the variable for clarity
    
    context = {
        'hero_sections': hero_sections,  # Pass the data to the template
    }
    return render(request, 'index.html', context)