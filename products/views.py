from django.shortcuts import render
from .models import Computers


def computers(request):
    """ A view to return the computers page """
    computers = Computers.objects.all()

    context = {
        'computers': computers,
    }
    return render(request, 'products/computers.html', context)


def laptops(request):
    """ A view to return the laptops page """

    return render(request, 'products/laptops.html')


def monitors(request):
    """ A view to return the monitors page """

    return render(request, 'products/monitors.html')
