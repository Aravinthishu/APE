from django.urls import path
from . import views
 
app_name='blog' 
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>', views.blogView, name='blog_details'),
]
