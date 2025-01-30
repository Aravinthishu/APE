from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField  # Assuming you're using CKEditor for rich text fields

class Product(models.Model):  # Main product model
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='main_product_images/', blank=True, null=True)
    description = RichTextField(blank=True, null=True)  # Rich text field for main product description
    introduction = RichTextField(blank=True, null=True)  # Rich text field for main product description
    advantages = RichTextField(blank=True, null=True)  # Rich text field for main product description
    data_sheet = RichTextField(blank=True, null=True)  # Rich text field for main product description
    application = RichTextField(blank=True, null=True)  # Rich text field for main product description
    slug = models.SlugField(unique=True, blank=True, null=True)  # Slug field
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't exist
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class ProductVariant(models.Model):  # Variants of the main product
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    item = models.CharField(max_length=255)
    rated_capacity = models.CharField(max_length=255)
    factory_model = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255, verbose_name="Dimensions (W*D*H,MM)")
    net_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Net Weight (KG)")
    packing_size = models.CharField(max_length=255, verbose_name="Packing Size (W*D*H,MM)")
    gross_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gross Weight (KG)")
    price  = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Price", default=0)
    
    def __str__(self):
        return f"{self.factory_model} ({self.main_product.name})"
