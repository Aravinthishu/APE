from django.shortcuts import render
from .models import *
from products.models import *

# Create your views here.


def index(request):
    hero_sections = HeroSection.objects.all()  # Renaming the variable for clarity
    services = Service.objects.filter(id__in=[1, 2, 5, 7])
    logos = ClientLogo.objects.all()
    whyus = WhyChooseUS.objects.all()
    awards = Awards.objects.all()
    categories = Product.objects.all()
    
    context = {
        'hero_sections': hero_sections,  # Pass the data to the template,
        'services': services,  # Pass the data to the template,
        'logos': logos,
        'whyus': whyus,
        'awards': awards,
        'categories':categories,
    }
    return render(request, 'index.html', context)