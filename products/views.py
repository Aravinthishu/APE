from django.shortcuts import get_object_or_404, render
from .models import *

def category(request):
    categories = Product.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/category.html', context)

def products(request, category_slug):
    product = get_object_or_404(Product, slug=category_slug)
    product_varient = ProductVariant.objects.filter(main_product=product)
    print(product_varient)
    
    context = {
        'product': product,
        'product_varient': product_varient
    }
    return render(request, 'products/products.html', context)
