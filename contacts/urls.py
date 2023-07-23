from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.Contact, name='contact'),
    path('pctechnician/', views.PcTechnician, name='pc-technician'),
]
