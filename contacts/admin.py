from django.contrib import admin
from .models import Contact, PcTechnician


@admin.register(Contact)
class ContactPage(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent')
    search_fields = ['name', 'message']


@admin.register(PcTechnician)
class Technician(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent')
    search_fields = ['name', 'message']
