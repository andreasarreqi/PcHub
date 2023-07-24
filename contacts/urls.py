from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.ContactUs.as_view(), name='contact'),
]
