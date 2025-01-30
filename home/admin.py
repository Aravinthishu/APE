from django.contrib import admin
from .models import *

class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at')  # Fields to display in the list view
    search_fields = ('title', 'subtitle')  # Fields to enable searching in the admin panel
    list_filter = ('created_at',)  # Filter by creation date
    ordering = ('-created_at',)  # Order by creation date (newest first)

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('category', 'year', 'description', 'image_preview')
    list_filter = ('category', 'year')
    search_fields = ('category', 'year', 'description')
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />'
        return "No Image"
    image_preview.allow_tags = True
    image_preview.short_description = "Image Preview"

admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(Service)
admin.site.register(ClientLogo)
admin.site.register(WhyChooseUS)