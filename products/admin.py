from django.contrib import admin
from .models import Computers, Laptops


@admin.register(Computers)
class ComputersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'motherboard',
        'proccessor',
        'ram',
        'memory',
        'image',
    )

    ordering = ('price',)


@admin.register(Laptops)
class LaptopsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'screen_size',
        'proccessor',
        'ram',
        'memory',
        'image',
    )

    ordering = ('price',)
