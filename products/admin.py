from django.contrib import admin
from .models import *

# Inline class for managing ProductVariant from MainProduct admin panel
class ProductVariantInline(admin.TabularInline):  
    model = ProductVariant
    extra = 1  # Show one empty form for adding a new variant by default
    fields = ('item', 'rated_capacity', 'factory_model', 'dimensions', 'net_weight', 'packing_size', 'gross_weight', 'price')
    verbose_name = "Variant"
    verbose_name_plural = "Variants"

# Admin class for MainProduct
@admin.register(Product)
class MainProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Fields to display in the admin list view
    search_fields = ('name',)  # Add search functionality by name
    prepopulated_fields = {'slug': ('name',)}  # Auto-fill slug field based on the name
    inlines = [ProductVariantInline]  # Attach ProductVariantInline for variant management

    # Optional: Define save methods to handle complex operations if needed
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
