from django.db import models

class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    btntitle = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='Services/', blank=True, null=True)
    icon = models.ImageField(upload_to='Services/', blank=True, null=True)
    icon_hover = models.ImageField(upload_to='Services/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class ClientLogo(models.Model):
    image = models.ImageField(upload_to='clients/')
    
    def __str__(self):
        return self.image.url
    
class WhyChooseUS(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='whychooseus/')


class Awards(models.Model):
    CATEGORY_CHOICES = [
        ('Awards', 'Awards'),
        ('Certificate', 'Certificate'),
    ]

    category = models.CharField(
        max_length=200,
        choices=CATEGORY_CHOICES,
        default='Awards'
    )
    year = models.CharField(max_length=200)
    image = models.ImageField(upload_to='awards/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.category}: {self.year}"