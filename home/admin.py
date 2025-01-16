from django.contrib import admin
from .models import HeroSection

class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at')  # Fields to display in the list view
    search_fields = ('title', 'subtitle')  # Fields to enable searching in the admin panel
    list_filter = ('created_at',)  # Filter by creation date
    ordering = ('-created_at',)  # Order by creation date (newest first)

admin.site.register(HeroSection, HeroSectionAdmin)
