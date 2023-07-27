from django.contrib import admin
from .models import Computers, Monitors, Reviews


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


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_on',
    )

    ordering = ('created_on',)


@admin.register(Monitors)
class MonitorsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'screen_size',
        'image',
    )

    ordering = ('price',)
