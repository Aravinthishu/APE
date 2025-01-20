from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
class Posts(models.Model):
     
     title=models.CharField(max_length=200 ,)
     image=models.ImageField(upload_to='blog/')
     short_desc=models.TextField(max_length=200, blank=True,null=True)
     long_desc=RichTextField() 
     author=models.ForeignKey(User, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     is_active = models.BooleanField(default=True)

     def __str__(self):
        return self.title