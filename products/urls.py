from django.urls import path
from . import views


urlpatterns = [
    path('computers', views.computers, name='computers'),
    path('<int:computer_id>/', views.computer_detail, name='computer_detail'),
]
