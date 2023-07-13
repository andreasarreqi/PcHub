from django.shortcuts import render


def computers(request):
    """ A view to return the computers page """

    return render(request, 'products/computers.html')


def laptops(request):
    """ A view to return the laptops page """

    return render(request, 'products/laptops.html')


def monitors(request):
    """ A view to return the monitors page """

    return render(request, 'products/monitors.html')
