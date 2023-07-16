from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Computers


def computers(request):
    """ A view to return the computers page """
    computers = Computers.objects.all()

    context = {
        'computers': computers,
    }
    return render(request, 'products/computers.html', context)


def computer_detail(request, computer_id):
    """ A view to show individual product details """

    computer = get_object_or_404(Computers, pk=computer_id)

    context = {
        'computer': computer,
    }

    return render(request, 'products/computer_detail.html', context)
