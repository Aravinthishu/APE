from django.shortcuts import render
from .models import Service

def services(request):
   features= Service.objects.all()
   context={
        'features':features
    }

   return render(request, 'services.html',context)