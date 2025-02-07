from django.db import models

# Create your models here.

class Timeline(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    image = models.ImageField(upload_to='timeline/', null=True, blank=True)
    
    def __str__(self):
        return self.title