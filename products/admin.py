from django.contrib import admin
from .models import Computers


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
