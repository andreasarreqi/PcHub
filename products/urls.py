from django.urls import path
from . import views


urlpatterns = [
    path('computers', views.computers, name='computers'),
    path('laptops', views.laptops, name='laptops'),
    path('monitors', views.monitors, name='monitors'),
]
