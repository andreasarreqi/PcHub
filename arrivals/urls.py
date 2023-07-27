from django.urls import path
from . import views


urlpatterns = [
    path('arrivals', views.arrivals, name='arrivals'),
]
