from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):  # This code is used for Image showing in Admin pages
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(
            object.photo.url))  # This code is used for Image showing in Admin pages

    thumbnail.short_description = 'Photo'  # This code is used for Image showing in Admin pages

    list_display = (
        'id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')  # To Display coloum Name
    list_display_links = ('id', 'thumbnail', 'first_name',)  # To Display Links
    search_fields = ('first_name', 'last_name', 'designation')  # To search Box
    list_filter = ('designation',)  # To Filter
