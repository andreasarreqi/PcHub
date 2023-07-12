from django.shortcuts import render
from .models import Computers


def computers(request):
    """
    Computer views
    """
    return render(request, 'products/computers.html')
