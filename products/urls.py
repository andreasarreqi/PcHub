from django.urls import path
from . import views


urlpatterns = [
    path('computers', views.computers, name='computers'),
    path('monitors', views.monitors, name='monitors'),
    path('<int:computer_id>/', views.computer_detail, name='computer_detail'),
    path('<int:monitor_id>/', views.monitor_detail, name='monitor_detail'),
    path('add/', views.add_computer, name='add_computer'),
    path('edit/<int:product_id>/', views.edit_computer, name='edit_computer'),
    path(
        'delete/<int:product_id>/',
        views.delete_computer, name='delete_computer'
        ),
]
