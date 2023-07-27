from django.contrib import admin
from .models import Arrivals


@admin.register(Arrivals)
class ArrivalsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_type',
        'price',
    )

    ordering = ('name',)
