from django.contrib import admin
from .models import Computers, Laptops, Monitors


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
        'image',
    )

    ordering = ('price',)


@admin.register(Monitors)
class MonitorsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'screen_size',
        'image',
    )

    ordering = ('price',)
