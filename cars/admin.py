from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):  # This code is used for Image showing in Admin pages
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(
            object.car_photo.url))  # This code is used for Image showing in Admin pages

    thumbnail.short_description = 'car_photo'  # This code is used for Image showing in Admin pages
    list_display = (
        'id', 'thumbnail', 'car_tittle', 'city', 'color', 'model', 'year', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_tittle')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_tittle', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')
# admin.site.register(Car, CarAdmin)
