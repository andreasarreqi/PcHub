from django.shortcuts import render


def arrivals(request):
    """ A view to return the arrivals page """

    return render(request, 'arrivals/arrivals.html')
