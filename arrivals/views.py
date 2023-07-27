from django.shortcuts import render


def index(request):
    """ A view to return the arrivals page """

    return render(request, 'arrivals/arrivals.html')
