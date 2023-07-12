from django.urls import path
from . import views


urlpatterns = [
    path('', views.Computers, name='computers'),
]
