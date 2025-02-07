from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.category, name= "category"),
    path('<slug:category_slug>/', views.products, name='category_view'),
    # path('details/<slug:product_slug>/', views.products_overview, name='product'),
]
