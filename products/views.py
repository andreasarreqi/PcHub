from django.shortcuts import render


def computers(request):
    """ A view to return the index page """

    return render(request, 'products/computers.html')
