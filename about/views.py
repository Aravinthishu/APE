from django.shortcuts import render
from .models import *
# Create your views here.


def about(request):
    visions = Vison.objects.all()
    video = Video.objects.first()
    whatwedo = WhatWeDo.objects.all()
    testimonials = Testimonial.objects.all()
    
    context = {
        'visions': visions,
        'video': video,
        'whatwedo': whatwedo,
        'testimonials': testimonials,
    }
    return render(request, 'about.html', context)