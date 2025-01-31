from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
     title=models.CharField(max_length=200 ,)
     long_desc=RichTextField() 
     image=models.ImageField(upload_to='services/')

     
def __str__(self):
        return self.title