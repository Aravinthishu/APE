from django.db import models

# Create your models here.


class Vison(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='visions/')

    def __str__(self):
        return self.title
    
class Video(models.Model):
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    
    def __str__(self):
        return self.video.url
    
class WhatWeDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    testimonial = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    
    def __str__(self):
        return self.name